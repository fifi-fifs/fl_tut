#  __________________
#  Import LIBRARIES
import flet as ft
#  Import FILES
#  __________________


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Mi app"
    texto = ft.Text("Mi primera app con Flet")
    # page.add(texto)
    texto2 = ft.Text("Este es un ejemplo para mi canal de Youtube")
    # page.add(texto2)
    # pass

    

    def cambiar_texto(e):
        texto2.value = "¡Suscríbete para más Tutoriales!"
        page.update()

    boton = ft.FilledButton(text="Cambiar texto", on_click=cambiar_texto)

    page.add(texto, texto2, boton)



if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER)
