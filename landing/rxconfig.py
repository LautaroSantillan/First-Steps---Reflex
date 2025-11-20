import reflex as rx

config = rx.Config(
    app_name="app",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://demo-reflex.vercel.app/"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)