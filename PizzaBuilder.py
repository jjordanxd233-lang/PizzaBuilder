import flet as ft

def main(page: ft.Page):

    base_pizza = ft.Image(src="peperoni.gif", width=300, height=300)
    olives = ft.Image(src="olive.gif", width=300, height=300, visible=False)
    margarita = ft.Image(src="margarita.gif", width=300, height=300, visible=False)

    #Functions
    def toggle_olives(e):
        olives.visible = e.control.value

    def toggle_pepperoni(e):
        margarita.visible = e.control.value

    #Page Setup
    page.title = "Pizza Builder"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Controls
    olive_switch = ft.Switch(label="Olives Pizza", on_change=toggle_olives)
    pepperoni_switch = ft.Switch(label="Margarita Pizza", on_change=toggle_pepperoni)

    pizza_stack = ft.Stack(
        [base_pizza, olives, margarita],
        width=300,
        height=300
    )

    page.add(
        pizza_stack,
        olive_switch,
        pepperoni_switch
    )

ft.app(target=main, assets_dir="assets")
