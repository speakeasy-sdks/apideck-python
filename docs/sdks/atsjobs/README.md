# AtsJobs
(*ats.jobs*)

### Available Operations

* [all](#all) - List Jobs
* [one](#one) - Get Job

## all

List Jobs

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

req = operations.JobsAllRequest(
    pass_through=shared.PassThroughQuery(
        additional_properties={
            "search": 'deposit',
        },
    ),
    x_apideck_app_id='Mobility',
    x_apideck_consumer_id='Mobility',
)

res = s.ats.jobs.all(req)

if res.get_jobs_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.JobsAllRequest](../../models/operations/jobsallrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.JobsAllResponse](../../models/operations/jobsallresponse.md)**


## one

Get Job

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

req = operations.JobsOneRequest(
    id='<ID>',
    x_apideck_app_id='primary',
    x_apideck_consumer_id='Fall',
)

res = s.ats.jobs.one(req)

if res.get_job_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.JobsOneRequest](../../models/operations/jobsonerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.JobsOneResponse](../../models/operations/jobsoneresponse.md)**

