# UnauthorizedResponse


## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `detail`                                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Contains parameter or domain specific information related to the error and why it occurred. | Failed to generate valid JWT Session. Verify applicationId is correct                       |
| `error`                                                                                     | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)       | Unauthorized                                                                                |
| `message`                                                                                   | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | A human-readable message providing more details about the error.                            | Unauthorized Request                                                                        |
| `ref`                                                                                       | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Link to documentation of error type                                                         | https://developers.apideck.com/errors#unauthorizederror                                     |
| `status_code`                                                                               | *Optional[float]*                                                                           | :heavy_minus_sign:                                                                          | HTTP status code                                                                            | 401                                                                                         |
| `type_name`                                                                                 | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The type of error returned                                                                  | UnauthorizedError                                                                           |