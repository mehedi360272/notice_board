from email.policy import default

from odoo import models, fields


class NoticeType(models.Model):
    _name = 'se.notice.type'
    _description = ''

    name = fields.Char(string='Notice Type:', required=True)
    active = fields.Boolean(string='Active:', default=True)
