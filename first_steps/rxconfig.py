import reflex as rx

config = rx.Config(
    app_name="first_steps",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://first-steps"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)