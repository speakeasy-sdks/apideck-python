"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getjobsresponse as shared_getjobsresponse
from ..shared import unexpectederrorresponse as shared_unexpectederrorresponse
from typing import Any, Optional



@dataclasses.dataclass
class JobsAllRequest:
    x_apideck_app_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-apideck-app-id', 'style': 'simple', 'explode': False }})
    r"""The ID of your Unify application"""
    x_apideck_consumer_id: str = dataclasses.field(metadata={'header': { 'field_name': 'x-apideck-consumer-id', 'style': 'simple', 'explode': False }})
    r"""ID of the consumer which you want to get or push data from"""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""
    fields_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \\"name\\", \\"email\\" and \\"addresses.city\\". If any other fields are available, they will be excluded."""
    limit: Optional[int] = dataclasses.field(default=20, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""
    pass_through: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pass_through', 'style': 'deepObject', 'explode': True }})
    r"""Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads"""
    raw: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'raw', 'style': 'form', 'explode': True }})
    r"""Include raw response. Mostly used for debugging purposes"""
    x_apideck_service_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'x-apideck-service-id', 'style': 'simple', 'explode': False }})
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    




@dataclasses.dataclass
class JobsAllResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_jobs_response: Optional[shared_getjobsresponse.GetJobsResponse] = dataclasses.field(default=None)
    r"""Jobs"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    unexpected_error_response: Optional[shared_unexpectederrorresponse.UnexpectedErrorResponse] = dataclasses.field(default=None)
    r"""Unexpected error"""
    

