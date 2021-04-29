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

model = load('assets/final_model.joblib')
ohe = load('assets/ohe.joblib')



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Select your Features

            """, className='mb-5'
        ),
        dcc.Markdown('##### Number of Beds'),
            dcc.Slider(id='Beds',
                    min=0,
                    max=21,
                    step=1,
                    value=0,
                    marks={n: str(n) for n in range(1,21,1)}
                    ),
            dcc.Markdown('',id='Output_Beds',
                        style={'textAlign':'center',
                                'font-size':20},
                                className='mb-5'),

            dcc.Markdown('##### Number of Bedrooms'),
            dcc.Slider(id='Bedrooms',
                    min=0,
                    max=21,
                    step=1,
                    value=1,
                    marks={n: str(n) for n in range(1,21,1)}
                    ),
            dcc.Markdown('',id='Output_Bedrooms',
                        style={'textAlign':'center',
                                'font-size':20},
                                className='mb-5'),

            dcc.Markdown('##### Number of Bathrooms'),
            dcc.Slider(id='Bathrooms',
                    min=0,
                    max=16,
                    step=1,
                    value=1,
                    marks={n: str(n) for n in range(1,16,1)}
                    ),
            dcc.Markdown('',id='Output_Bathrooms',
                        style={'textAlign':'center',
                                'font-size':20},
                                className='mb-5'),
    
            dcc.Markdown('##### Minimum Nights'),
            dcc.Slider(id='min_nights',
                    min=0,
                    max=21,
                    step=1,
                    value=1,
                    marks={n: str(n) for n in range(1,21,1)}
                    ),
    
            dcc.Markdown('##### Days Available per year'),
            dcc.Slider(id='avail_365',
                    min=0,
                    max=21,
                    step=1,
                    value=1,
                    marks={n: str(n) for n in range(1,21,1)}
                    ),

            dcc.Markdown('#### Room Type'),
            dcc.Dropdown(
            id='room_type',
            options=[
                {'label': 'Entire home/apt','value': 'Entire home/apt'},
                {'label': 'Private room','value': 'Private room'},
                {'label': 'Shared room','value': 'Shared room'},
                {'label': 'Hotel room','value': 'Hotel room'}
            ],
            value='Entire home/apt'
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
            html.Img(src='assets/airbnb_pic2.jpg', className='img-fluid')
    ]
)

@app.callback(
    Output(component_id='Output_Beds', component_property='children'),
    [Input(component_id='Beds', component_property='value')])
def update_output_div2(input_value):
    return 'You have selected: {} beds'.format(input_value)


@app.callback(
    Output(component_id='Output_Bedrooms', component_property='children'),
    [Input(component_id='Bedrooms', component_property='value')])
def update_output_div(input_value):
    return 'You have selected: {} bedrooms'.format(input_value)


@app.callback(
    Output(component_id='Output_Bathrooms', component_property='children'),
    [Input(component_id='Bathrooms', component_property='value')])
def update_output_div2(input_value):
    return 'You have selected: {} bathrooms'.format(input_value)


@app.callback(
    Output('prediction-content','value'),
    [Input('Beds', 'value'),
    Input('Bedrooms', 'value'),
    Input('Bathrooms', 'value')
      
     ])

def predict(bathrooms, bedrooms, beds, property_type, room_type, accommodates):
    df_ = pd.DataFrame(columns=['property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds'],
    data=[[property_type, room_type, accommodates, bathrooms, bedrooms, beds]])
    df = ohe.transform(df_)
    y_pred = model.predict(df)[0]
    result = round(np.exp(y_pred), 2)
    return result

layout = dbc.Row([column1, column2])
