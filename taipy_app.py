# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

from taipy.gui import Gui, navigate, Icon
import taipy.gui.builder as tgb

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'


def menu_option_selected(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

def create_menu():
    return     tgb.menu(label="Curiosity Data Analytics",
                    lov=[('page1', Icon('https://img.icons8.com/?size=100&id=63288&format=png&color=000000', 'Initial Set-up')),
                        ('page2', Icon('https://img.icons8.com/?size=100&id=63287&format=png&color=000000', 'Text Elements')),
                        ('page3', Icon('https://img.icons8.com/?size=100&id=63291&format=png&color=000000', 'User Inputs')),
                        ('page4', Icon('https://img.icons8.com/?size=100&id=63286&format=png&color=000000', 'Other Elements')),
                        ('page5', Icon('https://img.icons8.com/?size=100&id=63292&format=png&color=000000', 'Charts'))],
                    on_action=menu_option_selected)

with tgb.Page() as page1:

    create_menu()
    tgb.text("# 1️⃣ Initial Set-up", mode='md')

    tgb.text("my_taipy_app.py", mode='md')
    tgb.text("""from taipy.gui import Gui
import taipy.gui.builder as tgb  

with tbg.Page() as page1:
    # This is where you build your app
    ...
             
pages = (
    "page1" : page1,
    "page2" : page2,
    ...
)
             

if __name__ == "__main__":
    Gui(pages=pages).run(title="My Taipy App")
        """,mode='pre', class_name='code_block')

    tgb.text("In terminal, you launch your app like this:", mode='md')
    tgb.text(">taipy run my_taipy_app.py", mode='pre', class_name='code_block')

with tgb.Page() as page2:

    create_menu()
    tgb.text("# 2️⃣ Text Elements", mode='md')

    with tgb.layout("1 1"):
        tgb.text("""tgb.text("**This is a bold text**", mode='md')""", mode='pre', class_name='code_block')
        tgb.text("**This is a bold text**", mode='md')

        tgb.text("""tgb.text("*This is an italicized text* ", mode='md')""", mode='pre', class_name='code_block')
        tgb.text("*This is an italicized text* ", mode='md')
    
        tgb.text("""tgb.text("# This is a H1 text ", mode='md')""", mode='pre', class_name='code_block')
        tgb.text("# This is a H1 text ", mode='md')
        
        tgb.text("""tgb.text("This is a text in size 20pt ", mode='md', class_name='size20')""", mode='pre', class_name='code_block')
        tgb.text("This is a text in size 20pt ", mode='md', class_name='size20')
        tgb.text('You must pair this with a custom CSS class name defined as follows:', mode='md')
        tgb.text('')
        tgb.text(""".taipy-text.size20 (
        font-size: 20px;
    )""", mode='pre', class_name='code_block')
        tgb.text('')
        tgb.text('You must name the CSS file the exact same way as your Python file:', mode='md')
        tgb.text('')
        tgb.text("""my_python_file.py
my_python_file.css""", mode='pre', class_name='code_block')
        tgb.text('')

        tgb.text("""tgb.text("This is a yellow-colored text ", mode='md', class_name='yellow')""", mode='pre', class_name='code_block')
        tgb.text("This is a yellow-colored text ", mode='md', class_name='yellow')
        tgb.text('You must pair this with a custom CSS class name defined as follows:', mode='md')
        tgb.text('')
        tgb.text(""".taipy-text.yellow (
        color: #d4d804;
    )""", mode='pre', class_name='code_block')
    
    
with tgb.Page() as page3:

    create_menu()
    tgb.text("# 3️⃣ User Inputs", mode='md')   

    content=''
    

    with tgb.layout("1 15", gap="20px"):
        tgb.text('## Buttons', mode='md', class_name='blue')
    with tgb.layout("1 1 1", gap="20px"):
        with tgb.part():
            tgb.text("tgb.button('Default')", mode='pre', class_name='code_block')
            tgb.button('Default')
            tgb.text("tgb.button('Error',class_name='error')", mode='pre', class_name='code_block')
            tgb.button('Error',class_name='error')

        with tgb.part():
            tgb.text("tgb.button('Secondary',class_name='secondary')", mode='pre', class_name='code_block')
            tgb.button('Secondary',class_name='secondary')
            tgb.text("tgb.button('Warning',class_name='warning')", mode='pre', class_name='code_block')
            tgb.button('Warning',class_name='warning')

        with tgb.part():
            tgb.text("tgb.button('Success',class_name='success')", mode='pre', class_name='code_block')
            tgb.button('Success',class_name='success')
            tgb.text("tgb.button('Plain',class_name='plain')", mode='pre', class_name='code_block')
            tgb.button('Plain',class_name='plain')
    
    with tgb.layout("1 7", gap="20px"):
        tgb.text('## Value Inputs', mode='md', class_name='blue')
    with tgb.layout("1 1 1 2", gap="20px"):
        with tgb.part():
            tgb.text('### Number', mode='md')
            tgb.text("""input=0
tgb.number(input)""", mode='pre', class_name='code_block')
            nb_input_value=0  
            tgb.number("{nb_input_value}")
        with tgb.part():
            tgb.text('### Text', mode='md')
            tgb.text("""input=''
tgb.input(input)""", mode='pre', class_name='code_block')
            txt_input_value=''
            tgb.input("{txt_input_value}")
        with tgb.part():
            tgb.text('### Date', mode='md')
            tgb.text("""input = dt.datetime(2025,1,1).date()
tgb.date(input)""", mode='pre', class_name='code_block')
            dt_input = dt.datetime(2025,1,1).date()
            tgb.date("{dt_input}")
        with tgb.part():
            tgb.text('### Date Range', mode='md')
            tgb.text("""input = [dt.datetime(2024,1,1).date(), dt.datetime(2024,12,31).date()]
tgb.date_range(input)""", mode='pre', class_name='code_block')
            dt_input_range1 = dt.datetime(2024,1,1).date()
            dt_input_range2 = dt.datetime(2024,12,31).date()
            dates = [dt_input_range1, dt_input_range2]
            tgb.date_range("{dates}")

    with tgb.layout("1 14", gap="20px"):
        tgb.text('## Selectors', mode='md', class_name='blue')
    with tgb.layout("1 1 1 1", gap="20px"):
        with tgb.part():
            tgb.text('### Segmented Buttons', mode='md')
            tgb.text("""input = ''
tgb.toggle(input, lov="Item 1;Item 2;Item 3")""", mode='pre', class_name='code_block')
            sel_box_input = ''
            tgb.toggle("{sel_box_input}", lov="Item 1;Item 2;Item 3")
        with tgb.part():
            tgb.text('### Toggle', mode='md')
            tgb.text("""input=''
tgb.toggle(input)""", mode='pre', class_name='code_block')
            bol_input=''
            tgb.toggle("{bol_input}")
        with tgb.part():
            tgb.text('### Slider', mode='md')
            tgb.text("""input=0
tgb.slider(input, min=0, max=10)""", mode='pre', class_name='code_block')
            slider_input=0
            tgb.slider("{slider_input}", min=0, max=10)
        with tgb.part():
            tgb.text('### Dropdown', mode='md')
            tgb.text("""input=''
tgb.selector(input, lov="Item 1;Item 2;Item 3", dropdown=True)""", mode='pre', class_name='code_block')
            dropdown_value=''
            tgb.selector("{dropdown_value}", lov="Item 1;Item 2;Item 3", dropdown=True)
        with tgb.part():
            tgb.text('### Checkbox', mode='md')
            tgb.text("""input=''
tgb.selector(input, lov="Item 1;Item 2;Item 3", mode='check')""", mode='pre', class_name='code_block')
            checkbox_value=''
            tgb.selector("{checkbox_value}", lov="Item 1;Item 2;Item 3", mode='check')
        with tgb.part():
            tgb.text('### Radio Buttons', mode='md')
            tgb.text("""input=''
tgb.selector(input, lov="Item 1;Item 2;Item 3", mode='radio')""", mode='pre', class_name='code_block')
            radio_value=''
            tgb.selector("{radio_value}", lov="Item 1;Item 2;Item 3", mode='radio')
        with tgb.part():
            tgb.text('### Selection Box', mode='md')
            tgb.text("""input=''
tgb.selector(input, lov="Item 1;Item 2;Item 3")""", mode='pre', class_name='code_block')
            selbox=''
            tgb.selector("{selbox}", lov="Item 1;Item 2;Item 3")

    
    with tgb.layout("1 20", gap="20px"):
        tgb.text('## Files', mode='md', class_name='blue')
    with tgb.layout("1 1 1 2", gap="20px"):
        with tgb.part():
            tgb.text('### File Downloader', mode='md')
            tgb.text("""content=''
tgb.file_download(content, label='Download File')""", mode='pre', class_name='code_block')            
            tgb.file_download(content, label='Download File')
        with tgb.part():
            tgb.text('### File Uploader', mode='md')
            tgb.text("""content=''
tgb.file_selector(content, label='Upload File')""", mode='pre', class_name='code_block')            
            tgb.file_selector(content, label='Upload File') 

with tgb.Page() as page4:

    create_menu()
    tgb.text("# 4️⃣ Other Elements", mode='md') 


    tgb.text('## Status', mode='md')
    with tgb.layout("1 1 1 1 1", gap="20px"):
        with tgb.part():
            tgb.text("""status = ("info", "This is an info status.")
tgb.status(status)""", mode='pre', class_name='code_block')    
            status1 = ("info", "This is an info status.")
            tgb.status("{status1}")

        with tgb.part():
            tgb.text("""status = ("success", "This is a success status.")
tgb.status(status)""", mode='pre', class_name='code_block') 
            status2 = ("success", "This is a success status.")
            tgb.status("{status2}")

        with tgb.part():
            tgb.text("""status = ("warning", "This is a warning status.")
tgb.status(status)""", mode='pre', class_name='code_block') 
            status3 = ("warning", "This is a warning status.")
            tgb.status("{status3}")

        with tgb.part():
            tgb.text("""status = ("error", "This is an error status.")
tgb.status(status)""", mode='pre', class_name='code_block') 
            status4 = ("error", "This is an error status.")
            tgb.status("{status4}")

        with tgb.part():
            tgb.text("""status = [
    ("info", "Task is launched."),
    ("info", "Taks is waiting."),
    ("error", "1 error found."),
    ("success", "Task completed.")
]
tgb.status(status)""", mode='pre', class_name='code_block') 
            status5 = [
                ("info", "Task is launched."),
                ("info", "Taks is waiting."),
                ("error", "1 error found."),
                ("success", "Task completed.")
            ]
            tgb.status("{status5}")

    tgb.text('## Progress Bar', mode='md')
    progress_value = 0
    tgb.slider("{progress_value}")
    with tgb.layout("1 1 2", gap="20px"):
        tgb.text("""progress_value = 0
tgb.progress(value=progress_value, title="Loading...", title_anchor="top", show_value=True)                 
""", mode='pre', class_name='code_block')
        tgb.text("""progress_value = 0
tgb.progress(value=progress_value, title="Loading...", title_anchor="top", show_value=True, linear=True)                 
""", mode='pre', class_name='code_block')
        tgb.text(' ')
        tgb.progress(value="{progress_value}", title="Loading...", title_anchor="top", show_value=True)
        tgb.progress(value="{progress_value}", title="Loading...", title_anchor="top", show_value=True, linear=True)

    tgb.text('## Chat', mode='md')
    users = ["User", "Assistant"]
    messages: list[tuple[str, str, str]] = []

    tgb.text("""users = ["User", "Assistant"]
messages: list[tuple[str, str, str]] = []
tgb.chat(messages, users=users, sender_id=users[0])
""", mode='pre', class_name='code_block')
    tgb.chat("{messages}", users="{users}", sender_id="{users[0]}", on_action="evaluate")

    def evaluate(state, var_name: str, payload: dict):
        (_, _, expression, sender_id) = payload.get("args", [])
        messages.append((f"{len(messages)}", expression, sender_id))
        result = "Hello! :)"
        try:
            result = f"= {eval(expression)}"
        except Exception:
            pass
        messages.append((f"{len(messages)}", result, users[1]))
        state.messages = messages
    
    tgb.text('## Navigation Bar', mode='md')
    tgb.text("""tgb.navbar(lov=[('/page1', 'Page 1'), ('/page2', 'Page 2'), ('http://www.google.com', 'Google')])
""", mode='pre', class_name='code_block') 
    tgb.navbar(lov=[('/page1', 'Page 1'), ('/page2', 'Page 2'), ('http://www.google.com', 'Google')])

with tgb.Page() as page5:
    

    create_menu()
    tgb.text("# 5️⃣ Charts", mode='md') 

    with tgb.layout("1 1", gap="20px"):

        df1 = pd.DataFrame({
            'Date': pd.date_range(start="2024-01-01", periods=90, freq='D'),
            'Stock1': np.cumsum(np.random.randint(-2, 3, 90)) + 100,
            'Stock2': np.cumsum(np.random.randint(-3, 4, 90)) + 50,
            'Stock3': np.cumsum(np.random.randint(-1, 2, 90)) + 75
        })

        with tgb.part():
            tgb.text('## Table', mode='md')
            tgb.text("""df = pd.DataFrame((
    'Date': pd.date_range(start="2024-01-01", periods=90, freq='D'),
    'Stock1': np.cumsum(np.random.randint(-2, 3, 90)) + 100,
    'Stock2': np.cumsum(np.random.randint(-3, 4, 90)) + 50,
    'Stock3': np.cumsum(np.random.randint(-1, 2, 90)) + 75
))
tgb.table(df)
                     """, mode='pre', class_name='code_block')
            tgb.table("{df1.head(10)}")

        with tgb.part():
            tgb.text('## Line Plot', mode='md')
            tgb.text("""df = pd.DataFrame((
    'Date': pd.date_range(start="2024-01-01", periods=90, freq='D'),
    'Stock1': np.cumsum(np.random.randint(-2, 3, 90)) + 100,
    'Stock2': np.cumsum(np.random.randint(-3, 4, 90)) + 50,
    'Stock3': np.cumsum(np.random.randint(-1, 2, 90)) + 75
))
tgb.chart(df, mode="lines+markers", marker='o', title='Line Plot', x="Date", y__1="Stock1", y__2="Stock2", y__3="Stock3", color__1="yellow", color__2="blue", color__3="red")""", mode='pre', class_name='code_block')
            

            tgb.chart("{df1}", mode="lines+markers", marker='o', title='Line Plot', x="Date", y__1="Stock1", y__2="Stock2", y__3="Stock3", color__1="yellow", color__2="blue", color__3="red")

        with tgb.part():
            tgb.text('## Scatter Plot', mode='md')
            tgb.text("""df = pd.DataFrame((
    'Altitude': np.linspace(0, 5000, 100),
    'TempA': 25 - (np.linspace(0, 5000, 100) * 6.5 / 1000) + np.random.normal(0, 3, 100),
    'TempB': 30 - (np.linspace(0, 5000, 100) * 5.1 / 1000) + np.random.normal(0, 4, 100)
))
tgb.chart(df, mode="markers", x="Altitude", y__1="TempA", y__2="TempB")
                
                     """, mode='pre', class_name='code_block')
        
            df2 = pd.DataFrame({
                'Altitude': np.linspace(0, 5000, 100),
                'TempA': 25 - (np.linspace(0, 5000, 100) * 6.5 / 1000) + np.random.normal(0, 3, 100),
                'TempB': 30 - (np.linspace(0, 5000, 100) * 5.1 / 1000) + np.random.normal(0, 4, 100)
            })
            tgb.chart("{df2}", mode="markers", x="Altitude", y__1="TempA", y__2="TempB")

        with tgb.part():
            tgb.text('## Histogram', mode='md')
            tgb.text("""df = pd.DataFrame((
    'Speed': np.random.normal(loc=60, scale=15, size=1000)
))
tgb.chart(df, type="histogram")
                     

                     
                     """, mode='pre', class_name='code_block')
            df3 = pd.DataFrame({
                'Speed': np.random.normal(loc=60, scale=15, size=1000)
            })
            tgb.chart("{df3}", type="histogram")

        with tgb.part():
            tgb.text('## Bar Plot', mode='md')
            tgb.text("""df = pd.DataFrame((
                'Country': ['USA', 'Canada', 'Germany', 'France', 'Brazil'],
                'GDP': [27.7, 2.2, 4.5, 3.1, 2.2]
            ))
tgb.chart(df, type="bar", x="Country", y="GDP")
                     
                     
                     
                    """, mode='pre', class_name='code_block')
            df4 = pd.DataFrame({
                'Country': ['USA', 'Canada', 'Germany', 'France', 'Brazil'],
                'GDP': [23.3, 2.2, 4.5, 3.0, 2.1]
            })
            tgb.chart("{df4}", type="bar", x="Country", y="GDP")

        with tgb.part():
            tgb.text('## Heatmap', mode='md')
            tgb.text("""df = (
"Temperatures": [[17.2, 27.4, 28.6, 21.5],
                [5.6, 15.1, 20.2, 8.1],
                [26.6, 22.8, 21.8, 24.0],
                [22.3, 15.5, 13.4, 19.6]],
"Cities": ["Hanoi", "Paris", "Rio", "Sydney"],
"Seasons": ["Winter", "Spring", "Summer", "Autumn"]
)
tgb.chart(df, type="heatmap", z="Temperatures", x="Seasons", y="Cities")""", mode='pre', class_name='code_block')
            df5 = {
                "Temperatures": [[17.2, 27.4, 28.6, 21.5],
                                [5.6, 15.1, 20.2, 8.1],
                                [26.6, 22.8, 21.8, 24.0],
                                [22.3, 15.5, 13.4, 19.6]],
                "Cities": ["Hanoi", "Paris", "Rio", "Sydney"],
                "Seasons": ["Winter", "Spring", "Summer", "Autumn"]
            }
            tgb.chart("{df5}", type="heatmap", z="Temperatures", x="Seasons", y="Cities")

        with tgb.part():
            tgb.text('## Map', mode='md')
            tgb.text("""df = pd.DataFrame([
    ("name": "Tokyo", "lat": 35.6895, "lon": 139.6917, "magnitude": 5.1, "size": 32.5),
    ("name": "Osaka", "lat": 34.6937, "lon": 135.5023, "magnitude": 4.8, "size": 5),
    ("name": "Sendai", "lat": 38.2682, "lon": 140.8694, "magnitude": 5.4, "size": 60),
    ("name": "Nagoya", "lat": 35.1815, "lon": 136.9066, "magnitude": 4.9, "size": 13.75),
    ("name": "Sapporo", "lat": 43.0621, "lon": 141.3544, "magnitude": 5.2, "size": 41.25),
])
tgb.chart(df, type="scattergeo", mode="markers", lat="lat", lon="lon", marker=("size": "size"), text="name", layout=("geo": ("showland": True,"landcolor": "4A4"))""", mode='pre', class_name='code_block')
            data = pd.DataFrame([
                {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917, "magnitude": 5.1, "size": 32.5},
                {"name": "Osaka", "lat": 34.6937, "lon": 135.5023, "magnitude": 4.8, "size": 5},
                {"name": "Sendai", "lat": 38.2682, "lon": 140.8694, "magnitude": 5.4, "size": 60},
                {"name": "Nagoya", "lat": 35.1815, "lon": 136.9066, "magnitude": 4.9, "size": 13.75},
                {"name": "Sapporo", "lat": 43.0621, "lon": 141.3544, "magnitude": 5.2, "size": 41.25},
            ])
            tgb.chart("{data}", type="scattergeo", mode="markers", lat="lat", lon="lon", marker={"size": "size"}, text="name", layout={"geo": {"showland": True,"landcolor": "4A4"}})

        with tgb.part():
            tgb.text('## Plotly', mode='md')
            tgb.text("""import plotly.figure_factory as ff
                     
df = np.random.normal(loc=50, scale=15, size=500)
fig = ff.create_distplot([df], group_labels=["Data"], show_hist=True, show_rug=False)
tgb.chart(figure=fig)
                     
                     
                     
                    """, mode='pre', class_name='code_block')
            import plotly.figure_factory as ff

            df7 = np.random.normal(loc=50, scale=15, size=500)
            fig = ff.create_distplot([df7], group_labels=["Data"], show_hist=True, show_rug=False)
            tgb.chart(figure="{fig}")


pages = {
    "page1" : page1,
    "page2" : page2,
    "page3" : page3,
    "page4" : page4,
    "page5" : page5
}

def on_change(state, name, value):
    if name == 'nb_input_value':
        state.nb_input_value = value
    if name == 'txt_input_value':
        state.txt_input_value = value
    if name == 'dt_input':
        state.dt_input = value
    if name == 'dates':
        state.dates = value

if __name__ == "__main__":
    Gui(pages=pages).run(title="Taipy App", debug=True, use_reloader=True)