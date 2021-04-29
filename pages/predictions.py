# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from joblib import load

# Imports from this application
from app import app

model = load('assets/final_model2.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Select your Features

            """, className='mb-5'
        ),
        dcc.Markdown('#### City'),
        dcc.Dropdown(
            id='city',
            options=[
                {'label': 'Austin', 'value': 'Austin'},
                {'label': 'Chicago', 'value': 'Chicago'},
                {'label': 'Columbus', 'value': 'Columbus'},
                {'label': 'Los Angeles', 'value': 'Los Angeles'},
                {'label': 'New York City', 'value': 'New York City'},
                {'label': 'San Diego', 'value': 'San Diego'}

            ],
            value='Austin', className='mb-5'
        ),

        dcc.Markdown('##### Number of Beds'),
        dcc.Slider(id='Beds',
                   min=0,
                   max=20,
                   step=1,
                   value=0,
                   marks={n: str(n) for n in range(1, 20, 2)}
                   ),
        dcc.Markdown('', id='Output_Beds',
                     style={'textAlign': 'left',
                            'font-size': 18},
                     className='mb-5'),

        dcc.Markdown('##### Number of Bedrooms'),
        dcc.Slider(id='Bedrooms',
                   min=0,
                   max=10,
                   step=1,
                   value=0,
                   marks={n: str(n) for n in range(1, 10, 1)}
                   ),
        dcc.Markdown('', id='Output_Bedrooms',
                     style={'textAlign': 'left',
                            'font-size': 18},
                     className='mb-5'),

        dcc.Markdown('##### Number of Bathrooms'),
        dcc.Slider(id='Bathrooms',
                   min=0,
                   max=10,
                   step=1,
                   value=0,
                   marks={n: str(n) for n in range(1, 10, 1)}
                   ),
        dcc.Markdown('', id='Output_Bathrooms',
                     style={'textAlign': 'left',
                            'font-size': 18},
                     className='mb-5'),

        dcc.Markdown('##### Accommodates'),
        dcc.Slider(id='accommodates',
                   min=1,
                   max=20,
                   step=1,
                   value=1,
                   marks={n: str(n) for n in range(1, 20, 2)}
                   ),
        dcc.Markdown('', id='Output_Accommodates',
                     style={'textAlign': 'left',
                            'font-size': 18},
                     className='mb-5'),

        dcc.Markdown('#### Property type'),
        dcc.Dropdown(
            id='property_type',
            options=[
                {'label': 'Apartment', 'value': 'Apartment'},
                {'label': 'Guest suite', 'value': 'Guest suite'},
                {'label': 'Townhouse', 'value': 'Townhouse'},
                {'label': 'Loft', 'value': 'Loft'},
                {'label': 'Bed and breakfast', 'value': 'Bed and breakfast'},
                {'label': 'Condominium', 'value': 'Condominium'},
                {'label': 'House', 'value': 'House'},
                {'label': 'Botique hotel', 'value': 'Botique hotel'},
                {'label': 'Tiny house', 'value': 'Tiny house'},
                {'label': 'Guesthouse', 'value': 'Guesthouse'},
                {'label': 'Cabin', 'value': 'Cabin'},
                {'label': 'Hostel', 'value': 'Hostel'},
                {'label': 'Other', 'value': 'Other'},
                {'label': 'Resort', 'value': 'Resort'},
                {'label': 'Boat', 'value': 'Boat'},
                {'label': 'Serviced apartment', 'value': 'Serviced apartment'},
                {'label': 'Earth house', 'value': 'Earth house'},
                {'label': 'Bungalow', 'value': 'Bungalow'},
                {'label': 'Cottage', 'value': 'Cottage'},
                {'label': 'Aparthotel', 'value': 'Aparthotel'},
                {'label': 'Villa', 'value': 'Villa'},
                {'label': 'Cave', 'value': 'Cave'},
                {'label': 'Hotel', 'value': 'Hotel'},
                {'label': 'Houseboat', 'value': 'Houseboat'},
                {'label': 'Castle', 'value': 'Castle'},
                {'label': 'Tent', 'value': 'Tent'},
                {'label': 'Camper/RV', 'value': 'Camper/RV'},
                {'label': 'Bus', 'value': 'Bus'},
                {'label': 'Dome house', 'value': 'Dome house'},
                {'label': 'Farm stay', 'value': 'Farm stay'},
                {'label': 'Casa particular (Cuba)',
                 'value': 'Casa particular (Cuba)'},
                {'label': 'Dorm', 'value': 'Dorm'},
                {'label': 'Island', 'value': 'Island'},
                {'label': 'Yurt', 'value': 'Yurt'},
                {'label': 'Barn', 'value': 'Barn'},

            ],
            value='Apartment', className='mb-5'
        ),

        dcc.Markdown('#### Room Type'),
        dcc.Dropdown(
            id='room_type',
            options=[
                {'label': 'Entire home/apt', 'value': 'Entire home/apt'},
                {'label': 'Private room', 'value': 'Private room'},
                {'label': 'Shared room', 'value': 'Shared room'},
                {'label': 'Hotel room', 'value': 'Hotel room'}
            ],
            value='Entire home/apt', className='mb-5'
        )

    ],
    md=6,
)

column2 = dbc.Col(
    [
        dcc.Markdown('### Predicted Rental price ($)'),
        daq.LEDDisplay(
            id='prediction-content',
            size=25,
            color="#42f55d"),
        html.Img(src='assets/airbnb_pic7.jpg', className='img-fluid')
    ]
)


@app.callback(
    Output(component_id='Output_Beds', component_property='children'),
    [Input(component_id='Beds', component_property='value')])
def update_output_div1(input_value):
    return 'You have selected: {} beds'.format(input_value)


@app.callback(
    Output(component_id='Output_Bedrooms', component_property='children'),
    [Input(component_id='Bedrooms', component_property='value')])
def update_output_div2(input_value):
    return 'You have selected: {} bedrooms'.format(input_value)


@app.callback(
    Output(component_id='Output_Bathrooms', component_property='children'),
    [Input(component_id='Bathrooms', component_property='value')])
def update_output_div3(input_value):
    return 'You have selected: {} bathrooms'.format(input_value)


@app.callback(
    Output(component_id='Output_Accommodates', component_property='children'),
    [Input(component_id='accommodates', component_property='value')])
def update_output_div4(input_value):
    return 'You have selected: {} accommodations'.format(input_value)


@app.callback(
    Output('prediction-content', 'value'),
    [
        Input('property_type', 'value'),
        Input('room_type', 'value'),
        Input('accommodates', 'value'),
        Input('Bathrooms', 'value'),
        Input('Bedrooms', 'value'),
        Input('Beds', 'value'),
        Input('city', 'value')
    ])
def predict(property_type, room_type, accommodates, bathrooms, bedrooms, beds,
            city):
    df = pd.DataFrame(
        columns=["property_type", "room_type", "accommodates", "bathrooms",
                 "bedrooms", "beds", "city"],
        data=[
            [property_type, room_type, accommodates, bathrooms, bedrooms, beds,
             city]])
    y_pred = model.predict(df)[0][0]
    result = np.exp(y_pred)
    return np.round(result, 2)


layout = dbc.Row([column1, column2])
