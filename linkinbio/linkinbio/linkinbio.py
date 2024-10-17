import reflex as rx
from linkinbio.style import *
# add launchdarkly imports
import ldclient
from ldclient.config import Config
from ldclient import Context

# initialize LD client
ldclient.set_config(Config("LD_SDK_KEY"))
client = ldclient.get()

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
    # Check the feature flags
    user = {"key": "example-user-here"}
    feature_enabled = ldclient.variation("toggle-bio", user, False)

    # Define the component and background based on the feature flag
    if feature_enabled:
        name = "Erin Mikail Staples"
        background = "linear-gradient(45deg, #FFD700, #FF8C00, #FF4500)"
        pronouns = "she/her/hers"
        bio = "Stand up comedian + co-producer of the Inside Jokes show at Grisly Pear Comedy Club"
        avatar_url = "https://avatars.githubusercontent.com/erinmikailstaples"
        links = [
            {"name": "Website", "url": "https://www.insidejokes.nyc/"},
            {"name": "Upcoming Events", "url": "lu.ma/erinmikail"},
            {"name": "Instagram", "url": "https://instagram.com/erinmikail"},
            {"name": "Inside Jokes NYC", "url": "https://instagram.com/insidejokesnyc"},
        ]
    else:
        name = "Erin Mikail Staples"
        background = "radial-gradient(circle, var(--chakra-colors-purple-100), var(--chakra-colors-blue-100))"
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
                spacing="2",
            ),
            padding="4",
            max_width="400px",
            width="100%",
            spacing="3",
        ),
        width="100%",
        height="100vh",
        background=background,
    )

app = rx.App(style=style)
app.add_page(index)
