# HSMKeyMetadata

HSM-managed key metadata. Matches `handler.go` HSMKeyMetadata struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Unique identifier for the HSM key. | 
**key_type** | **str** | Cryptographic key type (see HSMKeyType enum). | 
**label** | **str** | Human-readable label for the key. | 
**state** | **str** | Current key lifecycle state per NIST SP 800-57. | 
**algorithm_oid** | **str** | OID of the key algorithm (e.g. 2.16.840.1.101.3.4.1.46 for AES-256-GCM). | 
**provider_id** | **str** | HSM provider or partition identifier. | 
**fips_level** | **int** | FIPS 140-3 validation level of the HSM hosting this key. | 
**attestation_available** | **bool** | Whether remote attestation evidence is available for this key. | 
**created_at** | **datetime** | Timestamp when the key was generated. | 
**deactivated_at** | **datetime** | Timestamp when the key was deactivated, or null if still active. | [optional] 
**destroyed_at** | **datetime** | Timestamp when the key was destroyed (zeroized), or null if not destroyed. | [optional] 
**rotated_at** | **datetime** | Timestamp of the most recent key rotation, or null if never rotated. | [optional] 

## Example

```python
from aqueduct_sdk.models.hsm_key_metadata import HSMKeyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of HSMKeyMetadata from a JSON string
hsm_key_metadata_instance = HSMKeyMetadata.from_json(json)
# print the JSON string representation of the object
print(HSMKeyMetadata.to_json())

# convert the object into a dict
hsm_key_metadata_dict = hsm_key_metadata_instance.to_dict()
# create an instance of HSMKeyMetadata from a dict
hsm_key_metadata_from_dict = HSMKeyMetadata.from_dict(hsm_key_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


