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

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

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
    x_apideck_app_id='string',
    x_apideck_consumer_id='string',
)

res = s.ats.applications.add(req)

if res.create_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ApplicationsAddRequest](../../models/operations/applicationsaddrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ApplicationsAddResponse](../../models/operations/applicationsaddresponse.md)**


## all

List Applications

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

req = operations.ApplicationsAllRequest(
    pass_through={
        "search": 'string',
    },
    x_apideck_app_id='string',
    x_apideck_consumer_id='string',
)

res = s.ats.applications.all(req)

if res.get_applications_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ApplicationsAllRequest](../../models/operations/applicationsallrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ApplicationsAllResponse](../../models/operations/applicationsallresponse.md)**


## delete

Delete Application

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

req = operations.ApplicationsDeleteRequest(
    id='<ID>',
    x_apideck_app_id='string',
    x_apideck_consumer_id='string',
)

res = s.ats.applications.delete(req)

if res.delete_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ApplicationsDeleteRequest](../../models/operations/applicationsdeleterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ApplicationsDeleteResponse](../../models/operations/applicationsdeleteresponse.md)**


## one

Get Application

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

req = operations.ApplicationsOneRequest(
    id='<ID>',
    x_apideck_app_id='string',
    x_apideck_consumer_id='string',
)

res = s.ats.applications.one(req)

if res.get_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ApplicationsOneRequest](../../models/operations/applicationsonerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ApplicationsOneResponse](../../models/operations/applicationsoneresponse.md)**


## update

Update Application

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

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
    x_apideck_app_id='string',
    x_apideck_consumer_id='string',
)

res = s.ats.applications.update(req)

if res.update_application_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ApplicationsUpdateRequest](../../models/operations/applicationsupdaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ApplicationsUpdateResponse](../../models/operations/applicationsupdateresponse.md)**

