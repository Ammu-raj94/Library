# -*- coding: utf-8 -*-

from odoo import fields,models

class Book(models.Model):
    """Model for adding Book details"""
    _name = 'book'
    _description = 'Book'
    _rec_name = 'name'

    name = fields.Char(string='Name', help='Name of the Book', required=True)
    author = fields.Char(string='Author', help='The Person who wrote the book',
                         required=True)
    publication_date = fields.Date(string='Published Date', help='The Published'
                                                                 'date of book')

