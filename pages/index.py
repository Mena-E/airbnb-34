# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Maximize your Airbnb income

            Are you an Airbnb property owner? Do you spend a lot of time trying to figure out how much to charge your guests?
            
            Airbnb Predictor is a running app that can help you set the best price for your property, minimize property vacancy, and maximize your profits.

            """
        ),
        dcc.Link(dbc.Button('Try out the Predictor', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/airbnb_pic3.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])