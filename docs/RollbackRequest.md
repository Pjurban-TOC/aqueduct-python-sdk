# RollbackRequest

Request body for rolling back a configuration entry to a previous version. Matches `config.go` RollbackRequest struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Target version number to roll back to. Must be a valid historical version. | 

## Example

```python
from aqueduct_sdk.models.rollback_request import RollbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackRequest from a JSON string
rollback_request_instance = RollbackRequest.from_json(json)
# print the JSON string representation of the object
print(RollbackRequest.to_json())

# convert the object into a dict
rollback_request_dict = rollback_request_instance.to_dict()
# create an instance of RollbackRequest from a dict
rollback_request_from_dict = RollbackRequest.from_dict(rollback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


