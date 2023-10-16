# CreateApplicantResponse


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   | Example                                       |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `data`                                        | [UnifiedID](../../models/shared/unifiedid.md) | :heavy_check_mark:                            | N/A                                           |                                               |
| `operation`                                   | *str*                                         | :heavy_check_mark:                            | Operation performed                           | add                                           |
| `resource`                                    | *str*                                         | :heavy_check_mark:                            | Unified API resource name                     | Applicants                                    |
| `service`                                     | *str*                                         | :heavy_check_mark:                            | Apideck ID of service provider                | lever                                         |
| `status`                                      | *str*                                         | :heavy_check_mark:                            | HTTP Response Status                          | OK                                            |
| `status_code`                                 | *int*                                         | :heavy_check_mark:                            | HTTP Response Status Code                     | 200                                           |