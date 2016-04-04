# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Cursos(models.Model):
    _name = 'cursos.curso'

    name = fields.Char(string="Nombre del curso", required=True)
    description = fields.Text(string="Descripción del Curso")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsable", index=True)

    session_ids = fields.One2many('cursos.seccion', 'course_id', string="Secciones")

class Seccion(models.Model):
    _name = 'cursos.seccion'

    name = fields.Char(required=True, string="Nombre")
    start_date = fields.Date(string="Fecha de início")
    duration = fields.Float(digits=(6, 2), help="Duración en días", string="Duración")
    seats = fields.Integer(string="Número de puestos")

    instructor_id = fields.Many2one('res.partner', string="Instructor", 
                    domain=['|', ('instructor', '=', True),
                    ('category_id.name', 'ilike', "Profesor")]
        )

    course_id = fields.Many2one('cursos.curso', ondelete='cascade', string="Curso", required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

