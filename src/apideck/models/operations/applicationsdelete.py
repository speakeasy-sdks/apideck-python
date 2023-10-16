"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleteapplicationresponse as shared_deleteapplicationresponse
from ..shared import unexpectederrorresponse as shared_unexpectederrorresponse
from typing import Optional



@dataclasses.dataclass
class ApplicationsDeleteSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class ApplicationsDeleteRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the record you are acting upon."""
    x_apideck_app_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-apideck-app-id', 'style': 'simple', 'explode': False }})
    r"""The ID of your Unify application"""
    x_apideck_consumer_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-apideck-consumer-id', 'style': 'simple', 'explode': False }})
    r"""ID of the consumer which you want to get or push data from"""
    raw: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'raw', 'style': 'form', 'explode': True }})
    r"""Include raw response. Mostly used for debugging purposes"""
    x_apideck_service_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-apideck-service-id', 'style': 'simple', 'explode': False }})
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    




@dataclasses.dataclass
class ApplicationsDeleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_application_response: Optional[shared_deleteapplicationresponse.DeleteApplicationResponse] = dataclasses.field(default=None)
    r"""Applications"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    unexpected_error_response: Optional[shared_unexpectederrorresponse.UnexpectedErrorResponse] = dataclasses.field(default=None)
    r"""Unexpected error"""
    
