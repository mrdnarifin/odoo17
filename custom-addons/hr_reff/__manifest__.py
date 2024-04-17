# -*- coding: utf-8 -*-
{
    "name": "HR References",
    "description": "HR Job References",
    "author": "Dwi Arifin",
    "website": "https://www.github.com/mrdnarifin",
    "category": "Human Resources/Employee",
    "version": "0.1",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["hr"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/grade_views.xml",
        "views/level_views.xml",
        "views/classification_views.xml",
        "views/cost_center_views.xml",
        "views/section_views.xml",
        "data/grade.xml",
        "data/level.xml",
        "data/classification.xml",
        "data/cost_center.xml",
        "data/department.xml",
        "data/work_location.xml",
        "views/employee_ext.xml",
    ],
    # only loaded in demonstration mode
    # "demo": [
    #     "data/grade.csv",
    # ],
    "application": False,
}
