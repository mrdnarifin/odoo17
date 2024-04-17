# -*- coding: utf-8 -*-
# from odoo import http


# class HrJobExt(http.Controller):
#     @http.route('/hr_job_ext/hr_job_ext', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_job_ext/hr_job_ext/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_job_ext.listing', {
#             'root': '/hr_job_ext/hr_job_ext',
#             'objects': http.request.env['hr_job_ext.hr_job_ext'].search([]),
#         })

#     @http.route('/hr_job_ext/hr_job_ext/objects/<model("hr_job_ext.hr_job_ext"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_job_ext.object', {
#             'object': obj
#         })

