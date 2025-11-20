import reflex as rx
from app.components.link_btn import link_btn

def links() -> rx.Component:
    return rx.vstack(
        link_btn("EXCEL CON TODAS LAS DEMOS Y KEYS", "https://docs.google.com/spreadsheets/d/1Nz9NeWJLAWMZSiTuRY2tL-nuwYgO02eqCttDNcZvNwY/edit?gid=0#gid=0"),
        link_btn("Call Center - STRIX", "https://gmfftfm9mn.us-east-1.awsapprunner.com/"),
        link_btn("Call Center - Contabilidad", "https://ypaibrpmni.us-east-1.awsapprunner.com/"),
        link_btn("Agente de análisis clientes - KANJI", "http://18.234.154.205:8501/"),
        link_btn("Agente gestor de facturas", "http://18.234.154.205:8501/facturas"),
        link_btn("Control de costos - DATI & KANJI", "http://18.234.154.205:8501/costos"),
        link_btn("Control de conversaciones - DATI", "http://18.234.154.205:8501/conversaciones_dati"),
        link_btn("Agente gestor de mails (NO DEPLOY)", ""),
        link_btn("Agente Capital Market (NO DEPLOY)", ""),
        link_btn("Tu chatbot en 60 segundos (NO DEPLOY)", ""),
        link_btn("Custom Agent - KANJIBOT (Redirije a FastAPI)", "https://d7pssnu3pm.us-east-1.awsapprunner.com/redoc"),
        width="100%",
        padding_x=["15px", "5px"]
    )