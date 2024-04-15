# -*- coding: utf-8 -*-
{
    "name": "Real Estate Guide",
    "description": "Real Estate Guidelines",
    "author": "Dwi Arifin",
    "website": "https://www.github.com/mrdnarifin",
    "category": "Sales/Real Estate",
    "version": "0.1",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    # any module necessary for this one to work correctly
    # always loaded
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_menu.xml",
        "views/estate_menu_type.xml",
        "views/estate_menu_tag.xml",
        # "views/templates.xml",
    ],
}
