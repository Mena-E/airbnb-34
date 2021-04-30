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
        dcc.Markdown('## Airbnb Predictor App Team', className='mb-10'),
        dcc.Markdown('', className='mb-5'),
        dcc.Markdown('#### Dr Israel Aikulola, Data Science - Modelling', className='mb-2'),
        html.P(
                [
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/israelaikulola/'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/dr-israel-o-aikulola/'), 
             
                ]
        ), 
        html.P(
                [
                    html.Img(src='assets/israel.jpeg', className='img-fluid') 
                ], 
                className='mb-5'
        ),

        dcc.Markdown('#### Mena Ekelemu, Data Science - Web Deployment', className='mb-2'),
        html.P(
                [
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Mena-E/'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/mena-ekelemu/'), 
             
                ]
        ), 
        html.P(
                [
                    html.Img(src='assets/mena.jpeg', className='img-fluid') 
                ], 
                className='mb-5'
        ),

        dcc.Markdown('#### Hillary Khan, Data Science - Modelling', className='mb-2'),
        html.P(
                [
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/hillarykhan/'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/hillary-khan/'), 
             
                ]
        ), 
        html.P(
                [
                    html.Img(src='assets/Hillary.jpeg', className='img-fluid') 
                ], 
                className='mb-5'
        ),

        dcc.Markdown('#### Jack Stanley, Data Science - Web Deployment', className='mb-2'),
        html.P(
                [
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Jack4589/'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/s-jack-stanley/'), 
             
                ]
        ), 
        html.P(
                [
                    html.Img(src='assets/jack.jpeg', className='img-fluid') 
                ], 
                className='mb-5'
        ),

        dcc.Markdown('#### Allen Dela Virgen, Data Science - Web Deployment', className='mb-2'),
        html.P(
                [
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Abdelapv53/'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/allen-dela-virgen/'), 
             
                ]
        ), 
        html.P(
                [
                    html.Img(src='assets/allen.jpeg', className='img-fluid') 
                ]
        )

   ])

layout = dbc.Row([column1])
