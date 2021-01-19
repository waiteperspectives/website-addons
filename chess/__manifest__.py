{
    "name": """Chess""",
    "summary": """Play Chess with other users in Odoo!""",
    "category": "Website",
    "vesion": "12.0.1.0.0",
    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "apps@itpp.dev",
    "website": "https://twitter.com/gabbasov_dinar",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["base", "website", "bus", "web"],
    "external_dependencies": {"python": ["chess"], "bin": []},
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/chess_views.xml",
        "views/chess.xml",
        "views/chess_templates.xml",
        "views/tournament_views.xml",
        "views/tournament_templates.xml",
    ],
    "qweb": ["static/xml/*.xml"],
    "installable": True,
}
