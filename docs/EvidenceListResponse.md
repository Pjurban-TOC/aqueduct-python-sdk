# EvidenceListResponse

Paginated response containing compliance evidence records. Matches compliance-engine EvidenceListResponse struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence** | [**List[ComplianceEvidence]**](ComplianceEvidence.md) | Compliance evidence records. | 
**next_cursor** | **str** | Cursor for the next page. Empty when no more results. | [optional] 
**total** | **int** | Total number of evidence records matching the query. | 

## Example

```python
from aqueduct_sdk.models.evidence_list_response import EvidenceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceListResponse from a JSON string
evidence_list_response_instance = EvidenceListResponse.from_json(json)
# print the JSON string representation of the object
print(EvidenceListResponse.to_json())

# convert the object into a dict
evidence_list_response_dict = evidence_list_response_instance.to_dict()
# create an instance of EvidenceListResponse from a dict
evidence_list_response_from_dict = EvidenceListResponse.from_dict(evidence_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


