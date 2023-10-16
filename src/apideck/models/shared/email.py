"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from apideck import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class EmailType(str, Enum):
    r"""Email type"""
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    WORK = 'work'
    PERSONAL = 'personal'
    BILLING = 'billing'
    OTHER = 'other'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Email:
    email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""Email address"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier for the email address"""
    type: Optional[EmailType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Email type"""
    
