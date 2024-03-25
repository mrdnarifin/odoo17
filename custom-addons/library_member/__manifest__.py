# -*- coding: utf-8 -*-
{
    "name": "Library Member",
    "summary": "Manage Member borrowing books",
    "author": "Dwi Arifin",
    "website": "https://www.github.com/mrdnarifin",
    "category": "Services/Library",
    "version": "16.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["library_app", "mail"],
    # only loaded in demonstration mode
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "application": False,
}
