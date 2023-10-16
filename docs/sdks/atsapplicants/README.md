# AtsApplicants
(*ats.applicants*)

### Available Operations

* [add](#add) - Create Applicant
* [all](#all) - List Applicants
* [delete](#delete) - Delete Applicant
* [one](#one) - Get Applicant
* [update](#update) - Update Applicant

## add

Create Applicant

### Example Usage

```python
import apideck
import dateutil.parser
from apideck.models import operations, shared

s = apideck.Apideck()

req = operations.ApplicantsAddRequest(
    applicant_input=shared.ApplicantInput(
        addresses=[
            shared.Address(
                city='San Francisco',
                contact_name='Elon Musk',
                country='US',
                county='Santa Clara',
                email='elon@musk.com',
                fax='122-111-1111',
                id='123',
                latitude='40.759211',
                line1='Main street',
                line2='apt #',
                line3='Suite #',
                line4='delivery instructions',
                longitude='-73.984638',
                name='HQ US',
                notes='Address notes or delivery instructions.',
                phone_number='111-111-1111',
                postal_code='94104',
                row_version='1-12345',
                salutation='Mr',
                state='CA',
                street_number='25',
                string='25 Spring Street, Blackburn, VIC 3130',
                type=shared.AddressType.PRIMARY,
                website='https://elonmusk.com',
            ),
        ],
        anonymized=True,
        application_ids=[
            'a0d636c6-43b3-4bde-8c70-85b707d992f4',
            'a98lfd96-43b3-4bde-8c70-85b707d992e6',
        ],
        applications=[
            'a0d636c6-43b3-4bde-8c70-85b707d992f4',
            'a98lfd96-43b3-4bde-8c70-85b707d992e6',
        ],
        archived=False,
        birthday=dateutil.parser.parse('2000-08-12').date(),
        confidential=False,
        coordinator_id='12345',
        cover_letter='I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...',
        custom_fields=[
            shared.CustomField(
                description='Employee Level',
                id='2389328923893298',
                name='employee_level',
            True,
            ),
        ],
        deleted=True,
        emails=[
            shared.Email(
                email='elon@musk.com',
                id='123',
                type=shared.EmailType.PRIMARY,
            ),
        ],
        first_name='Elon',
        followers=[
            'a0d636c6-43b3-4bde-8c70-85b707d992f4',
            'a98lfd96-43b3-4bde-8c70-85b707d992e6',
        ],
        headline='PepsiCo, Inc, Central Perk',
        initials='EM',
        last_name='Musk',
        middle_name='D.',
        name='Elon Musk',
        owner_id='54321',
        phone_numbers=[
            shared.PhoneNumber(
                area_code='323',
                country_code='1',
                extension='105',
                id='12345',
                number='111-111-1111',
                type=shared.PhoneNumberType.PRIMARY,
            ),
        ],
        photo_url='https://unavatar.io/elon-musk',
        position_id='123',
        record_url='https://app.intercom.io/contacts/12345',
        recruiter_id='12345',
        social_links=[
            shared.ApplicantSocialLinks(
                id='12345',
                type='twitter',
                url='https://www.twitter.com/apideck',
            ),
        ],
        sources=[
            'Job site',
        ],
        stage_id='12345',
        tags=[
            'New',
        ],
        title='CEO',
        websites=[
            shared.ApplicantWebsites(
                id='12345',
                type=shared.ApplicantWebsitesType.PRIMARY,
                url='http://example.com',
            ),
        ],
    ),
    x_apideck_app_id='North',
    x_apideck_consumer_id='Home indigo',
)

res = s.ats.applicants.add(req, "Bearer <your-apideck-api-key>")

if res.create_applicant_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ApplicantsAddRequest](../../models/operations/applicantsaddrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ApplicantsAddSecurity](../../models/operations/applicantsaddsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ApplicantsAddResponse](../../models/operations/applicantsaddresponse.md)**


## all

List Applicants

### Example Usage

```python
import apideck
from apideck.models import operations, shared

s = apideck.Apideck()

req = operations.ApplicantsAllRequest(
    filter=shared.ApplicantsFilter(
        job_id='1234',
    ),
    pass_through={
        "search": 'deposit',
    },
    x_apideck_app_id='Tungsten henry',
    x_apideck_consumer_id='Gasoline error',
)

res = s.ats.applicants.all(req, "Bearer <your-apideck-api-key>")

if res.get_applicants_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ApplicantsAllRequest](../../models/operations/applicantsallrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ApplicantsAllSecurity](../../models/operations/applicantsallsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ApplicantsAllResponse](../../models/operations/applicantsallresponse.md)**


## delete

Delete Applicant

### Example Usage

```python
import apideck
from apideck.models import operations

s = apideck.Apideck()

req = operations.ApplicantsDeleteRequest(
    id='<ID>',
    x_apideck_app_id='Architect Cotton port',
    x_apideck_consumer_id='qua',
)

res = s.ats.applicants.delete(req, "Bearer <your-apideck-api-key>")

if res.delete_applicant_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ApplicantsDeleteRequest](../../models/operations/applicantsdeleterequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ApplicantsDeleteSecurity](../../models/operations/applicantsdeletesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ApplicantsDeleteResponse](../../models/operations/applicantsdeleteresponse.md)**


## one

Get Applicant

### Example Usage

```python
import apideck
from apideck.models import operations

s = apideck.Apideck()

req = operations.ApplicantsOneRequest(
    id='<ID>',
    x_apideck_app_id='Northeast seize',
    x_apideck_consumer_id='bypass meter',
)

res = s.ats.applicants.one(req, "Bearer <your-apideck-api-key>")

if res.get_applicant_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ApplicantsOneRequest](../../models/operations/applicantsonerequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ApplicantsOneSecurity](../../models/operations/applicantsonesecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ApplicantsOneResponse](../../models/operations/applicantsoneresponse.md)**


## update

Update Applicant

### Example Usage

```python
import apideck
import dateutil.parser
from apideck.models import operations, shared

s = apideck.Apideck()

req = operations.ApplicantsUpdateRequest(
    applicant_input=shared.ApplicantInput(
        addresses=[
            shared.Address(
                city='San Francisco',
                contact_name='Elon Musk',
                country='US',
                county='Santa Clara',
                email='elon@musk.com',
                fax='122-111-1111',
                id='123',
                latitude='40.759211',
                line1='Main street',
                line2='apt #',
                line3='Suite #',
                line4='delivery instructions',
                longitude='-73.984638',
                name='HQ US',
                notes='Address notes or delivery instructions.',
                phone_number='111-111-1111',
                postal_code='94104',
                row_version='1-12345',
                salutation='Mr',
                state='CA',
                street_number='25',
                string='25 Spring Street, Blackburn, VIC 3130',
                type=shared.AddressType.PRIMARY,
                website='https://elonmusk.com',
            ),
        ],
        anonymized=True,
        application_ids=[
            'a0d636c6-43b3-4bde-8c70-85b707d992f4',
            'a98lfd96-43b3-4bde-8c70-85b707d992e6',
        ],
        applications=[
            'a0d636c6-43b3-4bde-8c70-85b707d992f4',
            'a98lfd96-43b3-4bde-8c70-85b707d992e6',
        ],
        archived=False,
        birthday=dateutil.parser.parse('2000-08-12').date(),
        confidential=False,
        coordinator_id='12345',
        cover_letter='I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...',
        custom_fields=[
            shared.CustomField(
                description='Employee Level',
                id='2389328923893298',
                name='employee_level',
            True,
            ),
        ],
        deleted=True,
        emails=[
            shared.Email(
                email='elon@musk.com',
                id='123',
                type=shared.EmailType.PRIMARY,
            ),
        ],
        first_name='Elon',
        followers=[
            'a0d636c6-43b3-4bde-8c70-85b707d992f4',
            'a98lfd96-43b3-4bde-8c70-85b707d992e6',
        ],
        headline='PepsiCo, Inc, Central Perk',
        initials='EM',
        last_name='Musk',
        middle_name='D.',
        name='Elon Musk',
        owner_id='54321',
        phone_numbers=[
            shared.PhoneNumber(
                area_code='323',
                country_code='1',
                extension='105',
                id='12345',
                number='111-111-1111',
                type=shared.PhoneNumberType.PRIMARY,
            ),
        ],
        photo_url='https://unavatar.io/elon-musk',
        position_id='123',
        record_url='https://app.intercom.io/contacts/12345',
        recruiter_id='12345',
        social_links=[
            shared.ApplicantSocialLinks(
                id='12345',
                type='twitter',
                url='https://www.twitter.com/apideck',
            ),
        ],
        sources=[
            'Job site',
        ],
        stage_id='12345',
        tags=[
            'New',
        ],
        title='CEO',
        websites=[
            shared.ApplicantWebsites(
                id='12345',
                type=shared.ApplicantWebsitesType.PRIMARY,
                url='http://example.com',
            ),
        ],
    ),
    id='<ID>',
    x_apideck_app_id='Gender',
    x_apideck_consumer_id='Tempe Ruble ADP',
)

res = s.ats.applicants.update(req, "Bearer <your-apideck-api-key>")

if res.update_applicant_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ApplicantsUpdateRequest](../../models/operations/applicantsupdaterequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ApplicantsUpdateSecurity](../../models/operations/applicantsupdatesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ApplicantsUpdateResponse](../../models/operations/applicantsupdateresponse.md)**

