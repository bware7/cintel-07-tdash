import seaborn as sns
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui
import palmerpenguins
import pandas as pd
from pathlib import Path

# Load the Palmer Penguins dataset
df = palmerpenguins.load_penguins()

# Get the current directory
app_dir = Path(__file__).parent

# Configure the page options with custom favicon
ui.page_opts(
    title="Palmer Penguins Analytics Dashboard",
    favicon="favicon.ico",
    fillable=True
)

# Include custom CSS
ui.include_css(app_dir / "styles.css")

# Create the sidebar with enhanced filter controls
with ui.sidebar(title="Dashboard Controls"):
    ui.h3("Filter Data")
    ui.input_slider(
        "mass",
        "Body Mass (g)",
        min=2000,
        max=6000,
        value=6000,
        step=100
    )
    
    ui.input_checkbox_group(
        "species",
        "Select Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    
    ui.input_selectize(
        "color_theme",
        "Color Theme",
        ["husl", "Set1", "Set2", "Set3", "deep"],
        selected="husl"
    )
    
    ui.hr()
    ui.h3("Resources")
    
    ui.a(
        "GitHub Source",
        href="https://github.com/bware7/cintel-07-tdash",
        target="_blank",
    )
    ui.a(
        "Live App",
        href="https://bware7.github.io/cintel-07-tdash/",
        target="_blank",
    )
    ui.a(
        "Issues",
        href="https://github.com/bware7/cintel-07-tdash/issues",
        target="_blank",
    )

# Create enhanced value boxes for key metrics
with ui.layout_column_wrap(fill=False):
    with ui.value_box(
        showcase=icon_svg("earlybirds", "brands")
    ):
        "Total Penguins in Selection"
        
        @render.text
        def count():
            return f"{filtered_df().shape[0]:,}"
    
    with ui.value_box(
        showcase=icon_svg("ruler-horizontal", "solid")
    ):
        "Average Bill Length"
        
        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"
    
    with ui.value_box(
        showcase=icon_svg("ruler-vertical", "solid")
    ):
        "Average Bill Depth"
        
        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

# Create the main layout with enhanced plots and data
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Bill Dimensions Analysis")
        
        @render.plot
        def length_depth():
            sns.set_theme(style="whitegrid")
            # Create figure and axes objects explicitly
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Create the scatter plot
            sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",
                size="body_mass_g",
                sizes=(20, 200),
                palette=input.color_theme(),
                ax=ax
            )
            
            # Customize the plot
            ax.set_title("Bill Length vs Depth by Species")
            ax.set_xlabel("Bill Length (mm)")
            ax.set_ylabel("Bill Depth (mm)")
            
            return fig
    
    with ui.card(full_screen=True):
        ui.card_header("Comprehensive Dataset Explorer")
        ui.markdown("""
        ### Interactive Data Grid
        - Click column headers to sort
        - Use filters to search specific values
        - Drag columns to reorder
        """)
        
        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(
                filtered_df()[cols],
                filters=True,
                height="400px"
            )

# Define the reactive calculation for filtering data
@reactive.calc
def filtered_df():
    """
    Filters the penguin dataset based on user selections.
    Returns filtered DataFrame containing only selected species and mass range.
    """
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df