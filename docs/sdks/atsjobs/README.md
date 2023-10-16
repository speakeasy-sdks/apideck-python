# AtsJobs
(*ats.jobs*)

### Available Operations

* [all](#all) - List Jobs
* [one](#one) - Get Job

## all

List Jobs

### Example Usage

```python
import ats_api
from ats_api.models import operations

s = ats_api.AtsAPI()

req = operations.JobsAllRequest(
    pass_through={
        "search": 'deposit',
    },
    x_apideck_app_id='Tungsten henry',
    x_apideck_consumer_id='Gasoline error',
)

res = s.ats.jobs.all(req, "")

if res.get_jobs_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.JobsAllRequest](../../models/operations/jobsallrequest.md)   | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.JobsAllSecurity](../../models/operations/jobsallsecurity.md) | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |


### Response

**[operations.JobsAllResponse](../../models/operations/jobsallresponse.md)**


## one

Get Job

### Example Usage

```python
import ats_api
from ats_api.models import operations

s = ats_api.AtsAPI()

req = operations.JobsOneRequest(
    id='<ID>',
    x_apideck_app_id='Northeast seize',
    x_apideck_consumer_id='bypass meter',
)

res = s.ats.jobs.one(req, "")

if res.get_job_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.JobsOneRequest](../../models/operations/jobsonerequest.md)   | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.JobsOneSecurity](../../models/operations/jobsonesecurity.md) | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |


### Response

**[operations.JobsOneResponse](../../models/operations/jobsoneresponse.md)**

