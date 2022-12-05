# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from dash_svg import Svg, G, Path, Circle
#import dash_html_components as html
import plotly.express as px
import pandas as pd
import base64
from PIL import Image
from dash import dcc
from dash.dependencies import Input, Output
import math
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


#For when you need to do more later and to style everything
#https://dash.plotly.com/external-resources

df = pd.DataFrame({
    "District": ["Southern", "Western", "Eastern", "Northern", "Central"],
    "Amount": [4, 1, 2, 2, 4],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal"]
})

fig = px.bar(df, x="District", y="Amount", color="City", barmode="group")

image_filename = './Systematic_Media_Review_v2/Interface/images/articles_false_true.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode() 

svg_filename = './Systematic_Media_Review_v2/Interface/images/rw.svg'
encoded_svg = base64.b64encode(open(svg_filename, 'rb').read()).decode() 
#encoded_svg = 'data:image/svg+xml;base64,{}'.format(svg_filename.decode()) 


#creating pie chart:
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]
fig_2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.8)])






app.layout = html.Div(children=[
    html.H1(children='Thesis Project - Systematic media review'),
    
    html.Hr(),
    
    dcc.Markdown('''
        ### By *Ludde Jahrl*
        
        This project focuses on the design and development of a visual text analytics approach for mapping and exploring mass trauma epidemiology with an aim to increase surge capacity. Such an approach bears specific relevance for low-income and middle-income countries (LMICs) where epidemiologi- cal databases are currently unavailable. Surge capacity is defined as “*the ability to manage a sudden, unexpected increase in patient volume that would otherwise severely challenge or exceed the current capacity of the health care system.*”

        During disasters, patient numbers increase, and patients can present with specific injuries and exposures putting the health system under additional strain. To develop surge capacity, it is essential to understand the mass trauma epidemiology of the specific setting. No globally accepted definition exists for mass trauma and its definition may vary depending on context and the capacity to handle the trauma. However, difficulties in linking hospital data to information on disaster collected and reported outside the hospital setting hinder a holistic understanding of disaster medicine epidemiology. To address this challenge, researchers at LiU have developed a methodology; the “*systematic media review.*”
        
        The methodology was piloted in a study where the epidemiology of mass-trauma events in Rwanda between 2010 - 2020 was assessed. Rwandan and international news media were analyzed, using the NexisUni search engine – a software which primarily has been used for sociological research previously.
        
        This master thesis project aims to build further on this approach and develop an analytics system for performing “*systematic media reviews.*” 
        '''),
    
    html.Hr(),
    
    dcc.Markdown('''
        • Use preloaded dataset? (Rwanda)
        • Upload dataset? (csv: 'url')
        • Build dataset?
    '''),
        
    dcc.Input(
        id="input1", type="text", placeholder="country...", style={'marginRight':'100px'}
    ),
    
    html.H1(children='Output: '),
    
    html.H1(id="output"),
    
    # https://dash.plotly.com/dash-core-components/checklist
    dcc.Checklist(
    ['New York City', 'Montréal', 'San Francisco'],
    ['New York City', 'Montréal', 'San Francisco']
    ),
    
    html.Div(
        dcc.Graph(figure=fig_2)
    ),
    
    # https://plotly.com/python/pie-charts/
    # pie chart to show how documents were dropped during pre process
    
    
    html.Img(
        width="800",
        src="data:image/svg+xml;base64,{}".format(encoded_svg),
        className = 'align-self-center'
        ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    html.Img(
        width="400",
        src="data:image/png;base64,{}".format(encoded_image)
    )
])

@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
)
def update_output(input1):
    if input != 'nan':
        return u'Input 1: {}'.format(input1)


if __name__ == '__main__':
    app.run_server(debug=True)
