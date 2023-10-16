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
    x_apideck_app_id='North',
    x_apideck_consumer_id='Home indigo',
)

res = s.ats.applicants.add(req)

if res.create_applicant_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->