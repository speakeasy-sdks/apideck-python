# GetApplicationResponse


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `data`                                            | [Application](../../models/shared/application.md) | :heavy_check_mark:                                | N/A                                               |                                                   |
| `operation`                                       | *str*                                             | :heavy_check_mark:                                | Operation performed                               | one                                               |
| `resource`                                        | *str*                                             | :heavy_check_mark:                                | Unified API resource name                         | Applications                                      |
| `service`                                         | *str*                                             | :heavy_check_mark:                                | Apideck ID of service provider                    | sap-successfactors                                |
| `status`                                          | *str*                                             | :heavy_check_mark:                                | HTTP Response Status                              | OK                                                |
| `status_code`                                     | *int*                                             | :heavy_check_mark:                                | HTTP Response Status Code                         | 200                                               |