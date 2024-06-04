from shiny import ui, render, App, reactive
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
app_ui = ui.page_fluid(
    ui.layout_sidebar( 
        ui.panel_sidebar(
            ui.h2("Definit un objectif"),
            ui.hr(),
            ui.input_select('course', 'Course', ['Diagonale des Fous', "Trail de Bourbon", "Mascareignes"]),
            ui.input_slider(id="slider", label="Temps cible:", min=5, max=25, value=15),

        ),

        ui.panel_main(
            ui.output_plot(id="histogram")
        )
    )
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.course)
    def aa():
        print(input.course())
        dic = {'Diagonale des Fous': [25,60],
               "Trail de Bourbon": [17, 40],
              "Mascareignes": [9, 19]}
        min, max = dic[input.course()]
        ui.update_slider(id="slider", label="Temps cible:", min=min, max=max, value=(min+max)//2)

    
    @output
    @render.plot
    def histogram():
        b = [p for p in Path('.').iterdir() if str(p).startswith('app')][0]
        df = pd.read_csv(f'{b}/aaa.csv',index_col=0)

        x = 100 + np.random.randn(500)
        plt.title("Cet histogramme n'a rien a voir \navec la prédiction\n des temps de passage...\n mais il bouge avec le curseur !", size=20)
        plt.hist(x=x, bins=input.slider()+df.loc[4,'2'], color="gray", ec="black")



app = App(ui=app_ui, server=server)