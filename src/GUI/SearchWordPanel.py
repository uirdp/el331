import flet as ft

class WordSearch(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):

        show_button = ft.ElevatedButton()
        search_options = ft.RadioGroup(content=ft.Row([
            ft.Radio(value="original_name", label="Original Name"),
            ft.Radio(value="updated_name", label="Updated Name"),
            ft.Radio(value="id", label="ID"), ]))

        target_file = ft.TextField()
        target_token = ft.TextField()

        v = ft.Column(
            width=600,
            spacing=25,
            controls=[
                search_options,
            ]
        )

        return ft.Column(controls=[v])

