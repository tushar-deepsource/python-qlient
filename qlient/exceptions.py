""" This file contains all qlient specific exceptions

:author: Daniel Seifert
:created: 12.09.2021
:copyright: Swisscom
"""
from typing import Dict


class QlientException(Exception):
    """ Base class for client exceptions """


class SchemaException(QlientException):
    """ Indicates that something is wrong regarding the graphql schema """

    def __init__(self, schema: Dict, *args):
        self.schema: Dict = schema
        super(SchemaException, self).__init__(*args)


class SchemaParseException(SchemaException):
    """ This exception gets thrown when the parses was unable to parse the graphql schema """


class NoTypesFound(SchemaParseException):
    """ Indicates that the schema does not have any types defined """