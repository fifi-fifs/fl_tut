#  __________________
#  Import LIBRARIES
import flet as ft
#  Import FILES
#  __________________


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "Mi app mejorada con filas y columnas"
    
    
    texto1 = ft.Text(value="Texto 1", size=24, color=ft.Colors.WHITE)
    texto2 = ft.Text(value="Texto 2", size=24, color=ft.Colors.WHITE)
    texto3 = ft.Text(value="Texto 3", size=24, color=ft.Colors.WHITE)
    # texto2 = ft.Text(value="Texto 2", size=18, color=ft.Colors.WHITE)

    fila_textos = ft.Row(controls=[texto1,texto2,texto3],alignment=ft.MainAxisAlignment.CENTER, spacing=50)

    boton1 = ft.FilledButton(text="Botón 1")
    boton2 = ft.FilledButton(text="Botón 2")
    boton3 = ft.FilledButton(text="Botón 3")

    fila_botones = ft.Row(controls=[boton1, boton2, boton3],alignment=ft.MainAxisAlignment.CENTER,spacing=50)


    textos_columna1 = [
        ft.Text(value="Columna 1 - Fila 1", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 1 - Fila 2", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 1 - Fila 3", size=18, color=ft.Colors.WHITE)
    ]   

    columna_texto1 = ft.Column(
        controls=textos_columna1
    )

    textos_columna2 = [
        ft.Text(value="Columna 2 - Fila 1", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 2 - Fila 2", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Columna 2 - Fila 3", size=18, color=ft.Colors.WHITE)
    ]   

    columna_texto2 = ft.Column(
        controls=textos_columna2
        # controls=textos_columna2, alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=50
    )

    page.add(fila_textos, fila_botones)

    fila_columns = ft.Row(
        controls=[columna_texto1, columna_texto2], alignment=ft.MainAxisAlignment.CENTER,spacing=150,
    )
    page.add(fila_columns)




    # page.add(columna_texto1)
    # page.add(fila_textos, fila_botones, columna_texto1, columna_texto2)



    # page.add(texto1,texto2,texto3)



if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER)
