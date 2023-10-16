"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ats_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional, Union



@dataclasses.dataclass
class CustomFieldValue4:
    pass



@dataclasses.dataclass
class CustomFieldValue:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CustomField:
    id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier for the custom field."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""More information about the custom field"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the custom field."""
    value: Optional[Union[str, float, bool, CustomFieldValue4, list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    

