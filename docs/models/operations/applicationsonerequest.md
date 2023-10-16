# ApplicationsOneRequest


## Fields

| Field                                                                                                                                         | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |
| `x_apideck_app_id`                                                                                                                            | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The ID of your Unify application                                                                                                              |
| `x_apideck_consumer_id`                                                                                                                       | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the consumer which you want to get or push data from                                                                                    |
| `x_apideck_service_id`                                                                                                                        | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. |