# -*- coding: utf-8 -*-
{
    "name": "Library Management",
    "summary": "Manage Library ctalog and book lending",
    "author": "Dwi Arifin",
    "website": "https://www.github.com/mrdnarifin",
    "category": "Services/Library",
    "version": "16.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["base"],
    # always loaded
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "demo": [
        "data/res.partner.csv",
        "data/library.book.csv",
        "data/book_demo.xml",
    ],
    # only loaded in demonstration mode
    "application": True,
}
