# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions

class Cursos(models.Model):
    _name = 'cursos.curso'

    name = fields.Char(string="Nombre del curso", required=True)
    description = fields.Text(string="Descripción del Curso")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsable", index=True)

    session_ids = fields.One2many('cursos.seccion', 'course_id', string="Secciones")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Cursos, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


class Seccion(models.Model):
    _name = 'cursos.seccion'

    name = fields.Char(required=True, string="Nombre")
    start_date = fields.Date(string="Fecha de início", default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duración en días", string="Duración")
    seats = fields.Integer(string="Número de puestos")
    active = fields.Boolean(default=True)

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


    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

