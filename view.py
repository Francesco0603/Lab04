import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        #Row 1
        def language_chosen(e):
            if self.language_dropdown.value in ["italian","english","spanish"]:
                self.txt_message.value = "lingua selezionata correttamente"
            else:
                self.txt_message.value = "lingua non supportata"
            self.page.update()
        def typeSearch_chosen(e):
            if self.type_dropdown.value in ["Default", "Linear", "Dichotomic"]:
                self.txt_message2.value = "modalità selezionata correttamente"
            else:
                self.txt_message2.value = "modalità non supportata"
            self.page.update()

        self.txt_message = ft.Text("")
        self.txt_message2 = ft.Text("")
        self.language_dropdown = ft.Dropdown(width=10000, on_change=language_chosen, options=[
                ft.dropdown.Option("italian"),
                ft.dropdown.Option("english"),
                ft.dropdown.Option("spanish"),
                ft.dropdown.Option("cirillico"),
            ])
        self.type_dropdown = ft.Dropdown(width=350, on_change=typeSearch_chosen, options=[
            ft.dropdown.Option("Default"),
            ft.dropdown.Option("Linear"),
            ft.dropdown.Option("Dichotomic"),
        ])
        self.txt_input = ft.TextField(label="Inserisci testo",width=500)
        self.txt_out = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        btn = ft.ElevatedButton(on_click=self.__controller.handleSentence,text="Spell Check",width=200)
        Row2= ft.Row([self.type_dropdown, self.txt_message2,self.txt_input,btn])
        Row3= ft.Row([self.txt_message,self.txt_message2,self.txt_out])
        self.page.add(self.language_dropdown,Row2,Row3)
        self.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
