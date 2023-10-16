"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import unifiedid as shared_unifiedid
from ats_api import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateApplicationResponse:
    data: shared_unifiedid.UnifiedID = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    operation: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation') }})
    r"""Operation performed"""
    resource: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    r"""Unified API resource name"""
    service: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service') }})
    r"""Apideck ID of service provider"""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""HTTP Response Status"""
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_code') }})
    r"""HTTP Response Status Code"""
    

