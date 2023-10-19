"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from apideck import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional, Union



@dataclasses.dataclass
class BadRequestResponseDetail2(Exception):
    r"""Contains parameter or domain specific information related to the error and why it occurred."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclasses.dataclass
class BadRequestResponseDetail:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BadRequestResponse(Exception):
    detail: Optional[Union[str, BadRequestResponseDetail2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail'), 'exclude': lambda f: f is None }})
    r"""Contains parameter or domain specific information related to the error and why it occurred."""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""A human-readable message providing more details about the error."""
    ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is None }})
    r"""Link to documentation of error type"""
    status_code: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_code'), 'exclude': lambda f: f is None }})
    r"""HTTP status code"""
    type_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type_name'), 'exclude': lambda f: f is None }})
    r"""The type of error returned"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
