import DatabaseManager

import flet as ft
from typing import Dict

class UploadFilePanel(ft.UserControl, db):
    def __init__(self):
        super().__init__()

    def build(self):

        prog_bars: Dict[str, ft.ProgressRing] = {}
        files = ft.Ref[ft.Column]()
        upload_button = ft.Ref[ft.ElevatedButton]()

        def file_picker_result(e: ft.FilePickerResultEvent):
            upload_button.current.disabled = True if e.files is None else False
            prog_bars.clear()
            files.current.controls.clear()
            if e.files is not None:
                for f in e.files:
                    prog = ft.ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                    prog_bars[f.name] = prog
                    files.current.controls.append(ft.Row([prog, ft.Text(f.name)]))


        def on_upload_progress(e: ft.FilePickerUploadEvent):
            prog_bars[e.file_name].value = e.progress
            prog_bars[e.file_name].update()

        file_picker = ft.FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

        def upload_files(e):
            file_manager = ft.FileManager.FileManager()

            uf = []
            if file_picker.result is not None and file_picker.result.files is not None:

                for f in file_picker.result.files:
                    name, content = file_manager.get_file_content_and_name(f.path)
                    self.db.insert_to_database(name, content)

        v = ft.Column(
            controls=[
                ft.ElevatedButton(
                    "Select files...",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: file_picker.pick_files(allow_multiple=True),
                ),
                ft.Column(ref=files),
                ft.ElevatedButton(
                    "Upload",
                    ref=upload_button,
                    icon=ft.icons.UPLOAD,
                    on_click=upload_files,
                ),
            ]
        )

        return v

