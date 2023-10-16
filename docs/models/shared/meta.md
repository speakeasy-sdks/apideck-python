# Meta

Response metadata


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `cursors`                                                     | [Optional[MetaCursors]](../../models/shared/metacursors.md)   | :heavy_minus_sign:                                            | Cursors to navigate to previous or next pages through the API |                                                               |
| `items_on_page`                                               | *Optional[int]*                                               | :heavy_minus_sign:                                            | Number of items returned in the data property of the response | 50                                                            |