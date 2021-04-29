# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from joblib import load

# Imports from this application
from app import app

model = load('assets/model.joblib')



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Select your Features

            """, className='mb-5'
        ),
            dcc.Markdown('##### Number of Bedrooms'),
            dcc.Slider(id='Bedrooms',
                    min=0,
                    max=21,
                    step=1,
                    value=2,
                    marks={
                        0:'0',
                        3:'3',
                        6:'6',
                        9:'9',
                        12:'12',
                        15:'15',
                        18:'18',
                        21:'21'
                    }
                    ),
            dcc.Markdown('',id='Output_Bedrooms',
                        style={'textAlign':'left',
                                'font-size':18},
                                className='mb-5'),
                                
        dcc.Markdown('##### Number of Bathrooms'),
            dcc.Slider(id='Bathrooms',
                    min=0,
                    max=15.5,
                    step=0.5,
                    value=2,
                    marks={
                        0:'0',
                        4:'4.0',
                        8:'8.0',
                        12:'12.0',
                        16:'16.0'
                    },
                    ),
            dcc.Markdown('',id='Output_Bathrooms',
                        style={'textAlign':'left',
                                'font-size':18},
                                className='mb-5'),

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
    Output(component_id='Output_Bathrooms', component_property='children'),
    [Input(component_id='Bathrooms', component_property='value')])
def update_output_div(input_value):
    return 'You have selected: {} bathrooms'.format(input_value)


@app.callback(
    Output(component_id='Output_Bedrooms', component_property='children'),
    [Input(component_id='Bedrooms', component_property='value')])
def update_output_div2(input_value):
    return 'You have selected: {} bedrooms'.format(input_value)


@app.callback(
    Output('prediction-content','value'),
    [ Input('Bathrooms', 'value'),
      Input('Bedrooms', 'value')
     ])

def predict(bedrooms, bathrooms):
    df = pd.DataFrame(columns=['bedrooms', 'bathrooms'],
    data=[[bedrooms, bathrooms]])
    y_pred = model.predict(df)[0]
    result = round(y_pred, 2)
    return result

layout = dbc.Row([column1, column2])