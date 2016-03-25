# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Cursos(models.Model):
    _name = 'cursos.curso'

    name = fields.Char(string="Nombre del curso", required=True)
    instructor = fields.Char(string="Instructor", required=True)
    description = fields.Text(string="Descripción del Curso")



