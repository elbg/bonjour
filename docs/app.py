from shiny import ui, render, App
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


app_ui = ui.page_fluid(
    # Sidebar layout
    ui.layout_sidebar( 
        # Sidebar with the input controls
        ui.panel_sidebar(
            ui.h2("Page Charts"),
            ui.hr(),
            ui.input_slider(id="slider", label="Number of bins:", min=5, max=25, value=15)
        ),
        # Main area with the chart
        ui.panel_main(
            ui.output_plot(id="histogram")
        )
    )
)

def server(input, output, session):
    @output
    @render.plot
    def histogram():
        a = [*Path('.').iterdir()]
        print(a)
        b = [*Path('./app_b079f4l5skivoltip17d').iterdir()]
        df = pd.read_csv('./app_b079f4l5skivoltip17d/aaa.csv',index_col=0)
        print(df.loc[4, '2'])
        # 500 samples from a normal distribution centered around 100
        x = 100 + np.random.randn(500)
        plt.title("A histogram", size=20)
        plt.hist(x=x, bins=input.slider()+df.loc[4,'2'], color="gray", ec="black")



app = App(ui=app_ui, server=server)