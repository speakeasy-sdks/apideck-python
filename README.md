# ATS-API

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/apideck-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/apideck-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/apideck-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import apideck
import dateutil.parser
from apideck.models import operations, shared

s = apideck.Apideck(
    api_key="Bearer <your-apideck-api-key>",
)

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
    x_apideck_app_id='Small',
    x_apideck_consumer_id='West',
)

res = s.ats.applicants.add(req)

if res.create_applicant_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations



### [ats.applicants](docs/sdks/atsapplicants/README.md)

* [add](docs/sdks/atsapplicants/README.md#add) - Create Applicant
* [all](docs/sdks/atsapplicants/README.md#all) - List Applicants
* [delete](docs/sdks/atsapplicants/README.md#delete) - Delete Applicant
* [one](docs/sdks/atsapplicants/README.md#one) - Get Applicant
* [update](docs/sdks/atsapplicants/README.md#update) - Update Applicant

### [ats.applications](docs/sdks/atsapplications/README.md)

* [add](docs/sdks/atsapplications/README.md#add) - Create Application
* [all](docs/sdks/atsapplications/README.md#all) - List Applications
* [delete](docs/sdks/atsapplications/README.md#delete) - Delete Application
* [one](docs/sdks/atsapplications/README.md#one) - Get Application
* [update](docs/sdks/atsapplications/README.md#update) - Update Application

### [ats.jobs](docs/sdks/atsjobs/README.md)

* [all](docs/sdks/atsjobs/README.md#all) - List Jobs
* [one](docs/sdks/atsjobs/README.md#one) - Get Job
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
