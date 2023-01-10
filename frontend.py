import PySimpleGUI as sg
from backend import extractor_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.InputText()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select folder:")
input2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read()

    match event:
        case "Extract":
            print(event, values)
            archivepath = values["archive"]
            destination_folder = values["folder"]
            extractor_archive(archivepath, destination_folder)
            window["output"].update("Extraction completed")
        case sg.WINDOW_CLOSED:
            break
window.close()