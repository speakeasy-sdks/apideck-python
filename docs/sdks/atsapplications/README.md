# AtsApplications
(*ats.applications*)

### Available Operations

* [add](#add) - Create Application
* [all](#all) - List Applications
* [delete](#delete) - Delete Application
* [one](#one) - Get Application
* [update](#update) - Update Application

## add

Create Application

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck()

req = operations.ApplicationsAddRequest(
    application_input=shared.ApplicationInput(
        applicant_id='12345',
        job_id='12345',
        stage=shared.ApplicationStage(
            id='12345',
            name='12345',
        ),
        status=shared.ApplicationStatus.OPEN,
    ),
    x_apideck_app_id='Small West',
    x_apideck_consumer_id='Officer impactful',
)

res = s.ats.applications.add(req, "Bearer <your-apideck-api-key>")

if res.create_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ApplicationsAddRequest](../../models/operations/applicationsaddrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ApplicationsAddSecurity](../../models/operations/applicationsaddsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ApplicationsAddResponse](../../models/operations/applicationsaddresponse.md)**


## all

List Applications

### Example Usage

```python
import apideck
from apideck.models import operations

s = apideck.Apideck()

req = operations.ApplicationsAllRequest(
    pass_through={
        "search": 'deposit',
    },
    x_apideck_app_id='Tungsten henry',
    x_apideck_consumer_id='Gasoline error',
)

res = s.ats.applications.all(req, "Bearer <your-apideck-api-key>")

if res.get_applications_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ApplicationsAllRequest](../../models/operations/applicationsallrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ApplicationsAllSecurity](../../models/operations/applicationsallsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ApplicationsAllResponse](../../models/operations/applicationsallresponse.md)**


## delete

Delete Application

### Example Usage

```python
import apideck
from apideck.models import operations

s = apideck.Apideck()

req = operations.ApplicationsDeleteRequest(
    id='<ID>',
    x_apideck_app_id='Architect Cotton port',
    x_apideck_consumer_id='qua',
)

res = s.ats.applications.delete(req, "Bearer <your-apideck-api-key>")

if res.delete_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ApplicationsDeleteRequest](../../models/operations/applicationsdeleterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ApplicationsDeleteSecurity](../../models/operations/applicationsdeletesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ApplicationsDeleteResponse](../../models/operations/applicationsdeleteresponse.md)**


## one

Get Application

### Example Usage

```python
import apideck
from apideck.models import operations

s = apideck.Apideck()

req = operations.ApplicationsOneRequest(
    id='<ID>',
    x_apideck_app_id='Northeast seize',
    x_apideck_consumer_id='bypass meter',
)

res = s.ats.applications.one(req, "Bearer <your-apideck-api-key>")

if res.get_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ApplicationsOneRequest](../../models/operations/applicationsonerequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ApplicationsOneSecurity](../../models/operations/applicationsonesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ApplicationsOneResponse](../../models/operations/applicationsoneresponse.md)**


## update

Update Application

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck()

req = operations.ApplicationsUpdateRequest(
    application_input=shared.ApplicationInput(
        applicant_id='12345',
        job_id='12345',
        stage=shared.ApplicationStage(
            id='12345',
            name='12345',
        ),
        status=shared.ApplicationStatus.OPEN,
    ),
    id='<ID>',
    x_apideck_app_id='South complexity',
    x_apideck_consumer_id='Tempe Ruble ADP',
)

res = s.ats.applications.update(req, "Bearer <your-apideck-api-key>")

if res.update_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ApplicationsUpdateRequest](../../models/operations/applicationsupdaterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ApplicationsUpdateSecurity](../../models/operations/applicationsupdatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ApplicationsUpdateResponse](../../models/operations/applicationsupdateresponse.md)**

