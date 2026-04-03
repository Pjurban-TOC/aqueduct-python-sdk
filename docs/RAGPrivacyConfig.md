# RAGPrivacyConfig

Privacy configuration for RAG retrieval. Per Privacy-Preserving RAG [arXiv:2412.04697], differential privacy budget parameters support HIPAA/FedRAMP compliance. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dp_enabled** | **bool** | Whether differential privacy is enabled for retrieval. | [optional] [default to False]
**epsilon** | **float** | Differential privacy epsilon parameter (privacy budget). | [optional] 
**access_control** | **str** | Granularity of access control enforcement. | [optional] [default to 'document_level']

## Example

```python
from aqueduct_sdk.models.rag_privacy_config import RAGPrivacyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RAGPrivacyConfig from a JSON string
rag_privacy_config_instance = RAGPrivacyConfig.from_json(json)
# print the JSON string representation of the object
print(RAGPrivacyConfig.to_json())

# convert the object into a dict
rag_privacy_config_dict = rag_privacy_config_instance.to_dict()
# create an instance of RAGPrivacyConfig from a dict
rag_privacy_config_from_dict = RAGPrivacyConfig.from_dict(rag_privacy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


