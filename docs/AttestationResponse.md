# AttestationResponse

Remote attestation evidence for an HSM key per IETF RATS (RFC 9334).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Identifier of the attested key. | 
**format** | **str** | Attestation evidence format (e.g. TPM2, IETF-EAT). | 
**evidence** | **str** | Base64-encoded attestation evidence blob. | 
**certificate_chain** | **List[str]** | PEM-encoded certificate chain anchoring the attestation to the HSM vendor root. | 
**timestamp** | **datetime** | Timestamp when the attestation evidence was generated. | 

## Example

```python
from aqueduct_sdk.models.attestation_response import AttestationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttestationResponse from a JSON string
attestation_response_instance = AttestationResponse.from_json(json)
# print the JSON string representation of the object
print(AttestationResponse.to_json())

# convert the object into a dict
attestation_response_dict = attestation_response_instance.to_dict()
# create an instance of AttestationResponse from a dict
attestation_response_from_dict = AttestationResponse.from_dict(attestation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


