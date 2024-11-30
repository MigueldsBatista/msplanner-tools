# MSPlanner Tools - Buckets Documentation

This section focuses on managing Microsoft Planner buckets using the functions provided in the `msplanner_tools.buckets` module.

## Buckets Management

The `msplanner_tools.buckets` module provides functions to create, retrieve, and delete buckets in Microsoft Planner via the Microsoft Graph API.

### Functions Overview

#### `create_bucket`

Creates a new bucket in Microsoft Planner.

**Parameters:**
- `bucket_name` (str): Name of the bucket to be created.
- `plan_id` (str): ID of the plan to which the bucket belongs.
- `access_token` (str): Access token for the Microsoft Graph API.
- `bucket_num` (int): Number of the bucket to be created (starts at 0).

**Returns:**
- `str`: ID of the created bucket.

**Example:**
```python
from msplanner_tools.buckets import create_bucket
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
bucket_id = create_bucket("New Bucket", "plan_id", token_manager.get_token(), 0)
if bucket_id:
    print("Bucket successfully created!")
```

#### `delete_bucket_by_id`

Deletes a bucket based on its ID.

**Parameters:**
- `bucket_id` (str): ID of the bucket to be deleted.
- `access_token` (str): Access token for the Microsoft Graph API.

**Returns:**
- `None`

**Example:**
```python
from msplanner_tools.buckets import delete_bucket_by_id
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
delete_bucket_by_id("bucket_id", token_manager.get_token())
print("Bucket deleted successfully.")
```

## References

- [MSAL Python Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-python)
- [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview)