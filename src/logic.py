def make_greeting(name, greeting):
    name = (name or "world").strip()[:50]
    return f"{greeting}, {name}!"