# Palmer Penguins Analytics Dashboard

An interactive dashboard built with Python and Shiny to analyze Palmer Penguins dataset.

## Features

- Interactive filtering by species and body mass
- Dynamic data visualization with customizable color themes
- Real-time statistical calculations
- Interactive data grid with sorting and filtering capabilities
- Responsive design with value boxes showing key metrics

## Technologies Used

- Python
- Shiny for Python
- Seaborn for data visualization
- pandas for data manipulation
- GitHub Pages for deployment

## Try It Out

View the live dashboard at: https://bware7.github.io/cintel-07-tdash/

## Local Development

### Prerequisites

- Python 3.x
- Git
- VS Code (recommended)

### Initial Setup

1. Clone the repository
```shell
git clone https://github.com/bware7/cintel-07-tdash
cd cintel-07-tdash
```

2. Create and activate virtual environment
```shell
py -m venv .venv
.venv\Scripts\Activate
```

3. Install dependencies
```shell
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

### Running the App

1. For development:
```shell
shiny run --reload --launch-browser app/app.py
```

2. View at http://127.0.0.1:8000/

### Deploy to GitHub Pages

1. Remove existing static assets and export
```shell
.venv\Scripts\Activate
shiny static-assets remove
shinylive export app docs
```

2. Test locally
```shell
py -m http.server --directory docs --bind localhost 8008
```

3. View at http://[::1]:8008/

### Publishing Changes

```shell
git add .
git commit -m "Your commit message"
git push -u origin main
```

## Acknowledgments

- Based on the Palmer Penguins dataset
- Built using Shiny for Python template
- Original template from PyShiny Templates Dashboard collection
