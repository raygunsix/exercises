import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet:")
inches_label = sg.Text("Enter inches:")
feet_input_box = sg.InputText(tooltip="Enter feet")
inches_input_box = sg.InputText(tooltip="Enter inches")
convert_button = sg.Button("Convert")

window = sg.Window('Converter', layout=[[feet_label, feet_input_box],
                                        [inches_label, inches_input_box],
                                        [convert_button]])
window.read()
window.close()