{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Daniel Reis",
    "category": "Services/Library",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing/Odoo-17-Development-Essentials",
    "version": "17.0.1.0.0",
    "depends": ["base"],
        "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_menu.xml",
    ],
    "application": True,
}
