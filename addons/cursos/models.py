# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Cursos(models.Model):
    _name = 'cursos.curso'

    name = fields.Char(string="Nombre del curso", required=True)
    description = fields.Text(string="Descripción del Curso")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsable", index=True)


class Seccion(models.Model):
    _name = 'cursos.seccion'

    name = fields.Char(required=True, string="Nombre")
    start_date = fields.Date(string="Fecha de início")
    duration = fields.Float(digits=(6, 2), help="Duración en días", string="Duración")
    seats = fields.Integer(string="Número de puestos")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('cursos.curso', ondelete='cascade', string="Curso", required=True)

