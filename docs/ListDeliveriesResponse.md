# ListDeliveriesResponse

Paginated list of delivery attempts. Handler returns: {\"deliveries\":[], \"next_cursor\":\"\", \"has_more\":bool} 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveries** | [**List[Delivery]**](Delivery.md) |  | 
**next_cursor** | **str** | Opaque cursor for the next page. Empty string when no more pages. | 
**has_more** | **bool** | True when additional pages exist. | 

## Example

```python
from aqueduct_sdk.models.list_deliveries_response import ListDeliveriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeliveriesResponse from a JSON string
list_deliveries_response_instance = ListDeliveriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDeliveriesResponse.to_json())

# convert the object into a dict
list_deliveries_response_dict = list_deliveries_response_instance.to_dict()
# create an instance of ListDeliveriesResponse from a dict
list_deliveries_response_from_dict = ListDeliveriesResponse.from_dict(list_deliveries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


