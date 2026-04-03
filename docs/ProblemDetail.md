# ProblemDetail

RFC 7807 Problem Details response. All error responses from the Aqueduct API use this format with `application/problem+json` content type. Matches `common/errors/rfc7807.go:34` ProblemDetail struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | URI reference identifying the problem type. | 
**title** | **str** | Short, human-readable summary of the problem type. | 
**status** | **int** | HTTP status code. | 
**detail** | **str** | Human-readable explanation specific to this occurrence. | 
**instance** | **str** | URI reference identifying the specific occurrence. | [optional] 
**code** | **str** | Machine-readable error code (ERR-API-001-XXX). | 
**trace_id** | **str** | Distributed tracing ID (ULID format) for support correlation. | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp of when the error occurred. | 
**retry_after** | **int** | Seconds until retry is recommended (for 429 and 503 responses). | [optional] 
**errors** | [**List[ValidationError]**](ValidationError.md) | Field-level validation errors (for 400 responses). | [optional] 

## Example

```python
from aqueduct_sdk.models.problem_detail import ProblemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetail from a JSON string
problem_detail_instance = ProblemDetail.from_json(json)
# print the JSON string representation of the object
print(ProblemDetail.to_json())

# convert the object into a dict
problem_detail_dict = problem_detail_instance.to_dict()
# create an instance of ProblemDetail from a dict
problem_detail_from_dict = ProblemDetail.from_dict(problem_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


