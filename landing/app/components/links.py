import reflex as rx
from app.components.link_btn import link_btn
from app.components.link_card import link_card

def links() -> rx.Component:
    return rx.vstack(
        link_card(
            url="https://docs.google.com/spreadsheets/d/1Nz9NeWJLAWMZSiTuRY2tL-nuwYgO02eqCttDNcZvNwY/edit?gid=0#gid=0",
            image="/credenciales.png",
            title="Excel Base",
            description="Excel con todas las demos y keys (credenciales) para las distintas demos."
        ),
        link_card(
            url="https://gmfftfm9mn.us-east-1.awsapprunner.com/",
            image="/robotIA.jpg",
            title="Call Center - STRIX",
            description="Call center inteligente para seguros que gestiona turnos, cobranzas y servicio técnico. Atiende llamadas, envía mails automáticos y resuelve consultas sin intervención humana."
        ),
        link_card(
            url="https://ypaibrpmni.us-east-1.awsapprunner.com/",
            image="/robotIA.jpg",
            title="Call Center - Contabilidad",
            description="Call center automatizado para estudios contables que responde consultas sobre impuestos, vencimientos y trámites frecuentes. Optimizado para contadores y pymes."
        ),
        link_card(
            url="http://18.234.154.205:8501/",
            image="/robotIA.jpg",
            title="Agente de análisis de clientes - KANJI",
            description="Centraliza la gestión de correos: clasifica, responde y redacta mails automáticamente. Tambien puede buscar y resumir correos historicos."
        ),
        link_card(
            url="http://18.234.154.205:8501/facturas",
            image="/robotIA.jpg",
            title="Agente de gestor de facturas",
            description="Procesa PDFs y documentos de facturación, estructurando la información en base de datos. Permite consultas y reportes directamente desde un chatbot conversacional."
        ),
        link_card(
            url="http://18.234.154.205:8501/costos",
            image="/robotIA.jpg",
            title="DATI & KANJI",
            description="Control de Costos (DATI y KANJI WEB)."
        ),
        link_card(
            url="http://18.234.154.205:8501/conversaciones_dati",
            image="/robotIA.jpg",
            title="DATI",
            description="Control de conversaciones DATI."
        ),
        link_card(
            url="/",
            image="/error-404.jpg",
            title="Agente de gestor de mails",
            description="Procesa PDFs y documentos de facturación, estructurando la información en base de datos. Permite consultas y reportes directamente desde un chatbot conversacional."
        ),
        link_card(
            url="/",
            image="/error-404.jpg",
            title="Agente - CAPITAL MARKET",
            description="Investiga noticias en tiempo real sobre mercados financieros y las combina con análisis histórico de datos. Genera gráficos y métricas clave para decisiones de inversión."
        ),
        link_card(
            url="/",
            image="/error-404.jpg",
            title="Agente 'tu chatbot en 60 segundos!'",
            description="Permite crear una agente especializado a partir de pdfs, docuementos, o investigacion realtime, en menos de 1 minuto."
        ),
        link_card(
            url="https://d7pssnu3pm.us-east-1.awsapprunner.com/redoc",
            image="/error-404.jpg",
            title="Custom Agent (redirige a FastAPI)",
            description="Es la version del Kanjibot que responde por Whatsapp. En el endpoint de costos se puede hacer el seguimiento de los costos."
        ),
        width="100%",
        padding_x=["15px", "5px"]
    )