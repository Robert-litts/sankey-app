# Flask Sankey Diagram App

## Overview

This is a simple Flask application that allows users to upload CSV files and generate Sankey diagrams. The app uses Plotly to create interactive Sankey diagrams, which visualize the flow of data between different or stages.

## Features

- Upload a CSV file with data in the following format: source,destination,amount. Here is an example:
```
source_category,target_category,amount
salary,daycare,25000
salary,mortgage,25000
salary,car,12000
salary,food,30000
daycare,child1,12500
daycare,child2,12500
```
- Generate a Sankey diagram showing the data flow.
- View the generated diagram directly in your browser.

## Prerequisites

- Python 3.6 or higher
- `pip` for managing Python packages

## Installation

   ```bash
   git clone https://github.com/Robert-Litts/sankey-app.git
   cd sankey-app
   pip install -r requirements.txt
   python app.py
   ```
