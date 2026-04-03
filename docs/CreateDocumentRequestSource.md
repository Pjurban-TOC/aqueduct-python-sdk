# CreateDocumentRequestSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.create_document_request_source import CreateDocumentRequestSource

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentRequestSource from a JSON string
create_document_request_source_instance = CreateDocumentRequestSource.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentRequestSource.to_json())

# convert the object into a dict
create_document_request_source_dict = create_document_request_source_instance.to_dict()
# create an instance of CreateDocumentRequestSource from a dict
create_document_request_source_from_dict = CreateDocumentRequestSource.from_dict(create_document_request_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


