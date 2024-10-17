import reflex as rx
from linkinbio.style import *

def link_button(name: str, url: str, icon: str) -> rx.Component:
    icon_map = {
        "globe": "globe",
        "twitter": "twitter",
        "github": "github",
        "linkedin": "linkedin",
    }
    icon_tag = icon_map.get(icon.lower(), "link")
    return rx.link(
        rx.button(
            rx.icon(tag=icon_tag),
            name,
            width="100%",
        ),
        href=url,
        is_external=True,
    )

def index() -> rx.Component:
    name = "Erin Mikail Staples"
    pronouns = "she/her/hers"
    bio = "Developer Experience Engineer @ LaunchDarkly"
    avatar_url = "https://avatars.githubusercontent.com/erinmikailstaples"
    links = [
        {"name": "Website", "url": "https://erinmikailstaples.com", "icon": "globe"},
        {"name": "Twitter", "url": "https://twitter.com/erinmikail", "icon": "twitter"},
        {"name": "GitHub", "url": "https://github.com/erinmikailstaples", "icon": "github"},
        {"name": "LinkedIn", "url": "https://linkedin.com/in/erinmikail", "icon": "linkedin"},
    ]
    return rx.center(
        rx.vstack(
            rx.avatar(src=avatar_url, size="2xl"),
            rx.heading(name, size="lg"),
            rx.text(pronouns, font_size="sm"),
            rx.text(bio),
            rx.vstack(
                rx.foreach(
                    links,
                    lambda link: link_button(link["name"], link["url"], link["icon"])
                ),
                width="100%",
                spacing="2",  # Reduced spacing
            ),
            padding="4",  # Reduced padding
            max_width="400px",
            width="100%",
            spacing="3",  # Reduced spacing
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle, var(--chakra-colors-purple-100), var(--chakra-colors-blue-100))",
    )

app = rx.App(style=style)
app.add_page(index)