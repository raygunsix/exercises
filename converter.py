import FreeSimpleGUI as sg

def convert(feet, inches):
    """ converts feet and inches to meters """
    inches_in_feet = inches / 12.0
    total_feet = feet + inches_in_feet
    meters = total_feet * 0.3048
    return meters


feet_label = sg.Text("Enter feet:")
feet_input_box = sg.InputText(tooltip="Enter feet", key="feet")

inches_label = sg.Text("Enter inches:")
inches_input_box = sg.InputText(tooltip="Enter inches", key="inches")

convert_button = sg.Button("Convert")
status_text = sg.Text("", key="status")

window = sg.Window('Converter', layout=[[feet_label, feet_input_box],
                                        [inches_label, inches_input_box],
                                        [convert_button, status_text]])

while True:
    event, values = window.read()
    print("Event: " + str(event))
    print("Values: " + str(values))

    inches = float(values['inches'])
    feet = float(values['feet'])

    meters = convert(feet, inches)

    message = "Meters: " + str(round(meters, 3)) + " m"
    window["status"].update(value=message)
    print(message)

window.close()
