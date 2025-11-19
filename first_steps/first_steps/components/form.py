import reflex as rx

class ContactFormState(rx.State):
    """Estado para manejar un formulario de contacto estático."""
    # Aquí almacenaremos los datos enviados
    form_data: dict = {}
    @rx.event
    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        # Los datos recibidos serán: {"first_name": "...", "last_name": "...", "email": "...", "mensaje": "..."}
        self.form_data = form_data
        print("Datos recibidos:", self.form_data)

def contact_form() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(placeholder="Nombre", name="first_name"),
                rx.input(placeholder="Apellido", name="last_name"),
                rx.input(placeholder="Email", name="email", type="email"),
                rx.text_area(placeholder="Tu Mensaje", name="mensaje"),
                rx.button(
                    "Enviar Consulta", 
                    type="submit",
                    #height=["3em", "4em"] 
                ),  
                width="100%",
                spacing="3"
            ),
            on_submit=ContactFormState.handle_submit,
            reset_on_submit=True,
            width="100%"
        ),
        
        rx.divider(),
        rx.heading("Datos Recibidos (Debug)", size="5"),
        rx.text(ContactFormState.form_data.to_string()),
        width="100%",
        padding_x=["1em", "2em", "4em"], 
        spacing="5"
    )