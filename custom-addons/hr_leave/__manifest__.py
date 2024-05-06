# -*- coding: utf-8 -*-
{
    "name": "HR Time Off",
    "description": "HR Time Off",
    "author": "Dwi Arifin",
    "website": "https://www.github.com/mrdnarifin",
    "category": "Human Resources/HR Time Off",
    "version": "0.1",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["hr_holidays"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/leave_ext.xml",
    ],
    # only loaded in demonstration mode
    # "demo": [
    #     "data/grade.csv",
    # ],
    "application": False,
}
