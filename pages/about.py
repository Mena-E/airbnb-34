# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('### Creators of the app', className='mb-10'),
        dcc.Markdown('', className='mb-5'),
        dcc.Markdown('##### Dr. Israel Aikulola'),
        dcc.Link('Github', href='https://github.com/israelaikulola', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown(''),
        dcc.Link('LinkedIn', href='https://www.linkedin.com/in/dr-israel-o-aikulola/', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown('', className='mb-5'),
        dcc.Markdown('##### Mena Ekelemu'),
        dcc.Link('Github', href='https://github.com/Mena-E/', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown(''),
        dcc.Link('LinkedIn', href='https://www.linkedin.com/in/mena-ekelemu/', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown('', className='mb-5'),
        dcc.Markdown('##### Hillary Khan'),
        dcc.Link('Github', href='https://github.com/hillarykhan', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown(''),
        dcc.Link('LinkedIn', href='https://www.linkedin.com/in/hillary-khan/', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown('', className='mb-5'),
        dcc.Markdown('##### Jack Stanley'),
        dcc.Link('Github', href='https://github.com/Jack4589', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown(''),
        dcc.Link('LinkedIn', href='https://www.linkedin.com/in/s-jack-stanley/', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown('', className='mb-5'),
        dcc.Markdown('##### Allen Dela Virgen'),
        dcc.Link('Github', href='https://github.com/Abdelapv53', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown(''),
        dcc.Link('LinkedIn', href='https://www.linkedin.com/in/allen-dela-virgen/', style={'textAlign': 'left',
                            'font-size': 16}),
        dcc.Markdown('', className='mb-5')

        

    ])

layout = dbc.Row([column1])
