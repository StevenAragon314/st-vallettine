import flet as ft
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
from pathlib import Path
import os
import pywhatkit as kit

list_rech = [
    'No',
    'Segura ???',
    '... no lo esperaba',
    'repitelo ...',
    'oh no entiendo',
    'me duele tu rechazo',
    '¿por qué?',
    'Deja de dar más clicks',
    'F mi corazón'
]

# First image
choochoo  = Path(r'C:\Users\Steve\Training of Different Topics\A2 - Python\rafa_san_valetin\choochoo.png').parent
resp_si = Path(r'C:\Users\Steve\Training of Different Topics\A2 - Python\rafa_san_valetin\Happy.png').parent

# UI
app_ui = ui.page_fluid(
    
    ui.output_image("image_1"),
    ui.output_text("text_question"),
    ui.input_action_button(id= "pass_question_1", label= "Siiiiiii"),
    ui.input_action_button(id= "pass_question_2", label= "No"),
    # ui.panel_conditional(
    #     "input.pass_question_1 == Siiiiiii",
    #     ui.output_text("--------"),
    #     ui.output_image("image_si"),
    # ),
    ui.panel_conditional(
        "input.pass_question_2 == No",
            ui.output_text("list_rech_no"),
            ui.output_image("image_change_no")
    ),
)
        
# Server
def server(input: Inputs, output: Outputs, session: Session):

    @output
    @render.image  
    def image_1():
        img = {"src": choochoo / "choochoo.png", "width": "250px"}  
        return img 

    @output
    @render.text
    def text_question():
        return "¿Te gustaría salir con migo?"

    @reactive.event(input.pass_question_2)
    def c_1():
        return input.pass_question_2()

    @render.text()
    @reactive.event(input.pass_question_2)
    def list_rech_no():   
        try:
            return list_rech[c_1()]
        except IndexError:
            return "Esta bien, ya no insistiré más 😥"

    @output
    @render.image
    def image_change_no():
        rafa_list = [f'rafa{i}.png' for i in range(1, 10)]
        try:
            rafa_n = rafa_list[c_1()]
            general_path = os.getcwd() + f'\{rafa_n}'
            rafa_dir = Path(general_path).parent
            img = {"src": rafa_dir / rafa_n, "width": "100px"}
            return img
        except IndexError:
            print("")

    @output
    @render.text
    def text_si():
        return "Auuuuuuu Enserio🤩"
    
    @output
    @render.image
    def image_si():
        img = {'scr': resp_si / Happy.png, "width": "100px"}
        return img

app = App(app_ui, server)
app.run()

import pywhatkit as kit
import time 
kit.sendwhatmsg("0050671247046", "Hola", 10,55)

