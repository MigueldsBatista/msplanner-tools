# MSPlanner Tools Documentation
MSPlanner Tools is a Python library designed to streamline interactions with Microsoft Planner via the Microsoft Graph API. This documentation provides an overview of the library's features, focusing on Authentication and managing OAuth2 tokens using the TokenManager class.

### Project Repository
To further details and better navigation visit the project page on [Github.](https://github.com/MigueldsBatista/msplanner-tools)

### Learn how you can contribute
[Contributing](https://github.com/MigueldsBatista/msplanner-tools/blob/main/contributing.md)

## Overview
* <a href="#authentication"><p>Authentication</p></a>
* <a href="#plans"><p>Plans</p></a>
* <a href="#tasks"><p>Tasks</p></a>
* <a href="#buckets">Buckets</p></a>
* <a href="#users"><p>Users</p></a>

---
# Authentication

The TokenManager class provides a robust way to handle authentication and token management for accessing the Microsoft Graph API. This is essential for secure and seamless communication with Microsoft Planner.

### Features of TokenManager
- Automatically manages OAuth2 tokens for authentication.
- Requests new tokens when the current token expires.
- Supports Azure Active Directory authentication using the Microsoft Authentication Library (MSAL).

### Prerequisites
Before using the TokenManager class, ensure you have the following:
- **Client ID**: Obtain from your Azure AD app registration.
- **Client Secret**: Set up in your Azure AD app registration.
- **Tenant ID**: Find this in your Azure Active Directory overview.

### Usage
Here's how to use the TokenManager class for authentication:

#### Import and Initialize
```python
from msplanner_tools.authentication import TokenManager

# Replace with your Azure AD app credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'
```

If you don't know how to register an Azure app, visit [Microsoft how to register an app guide](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory).

**Permissions:**
- Group.ReadWrite.All
- Tasks.ReadWrite.All
- User.ReadBasic.All

Here is an example on how to use the TokenManager class:

```python
# Initialize the TokenManager
token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

# Get a valid access token
access_token = token_manager.get_token()
print(f'Access Token: {access_token}')
# The get_token method ensures that a valid token is always returned, automatically handling token expiration.
```

**Token Management Details**
- **Request a New Token**: If the token has expired or is unavailable, a new token is automatically requested using `request_new_token`.
- **Expiration Handling**: The class keeps track of the token's expiration time and validates it using `is_token_expired`.

## Example Workflow
```python
# Using the token in an API request
import requests

# Get the access token
access_token = token_manager.get_token()

# Set up the headers for Microsoft Graph API requests
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
```

### Example: Create a new plan
```python
from msplanner_tools.plans import create_plan
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

plan_id = create_plan("my new plan", "my_group_id", token_manager.get_token())

if plan_id:
    print("Plan successfully created!")
```

**References**
- [MSAL Python Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview)

---
# Plans

This section focuses on managing Microsoft Planner plans using the functions provided in the `msplanner_tools.plans` module.
<br>
[Return to the top](#authentication)
## Plans Management
The `msplanner_tools.plans` module provides functions to create, retrieve, update, and delete plans in Microsoft Planner via the Microsoft Graph API.

### Functions Overview

#### `create_plan`
Creates a new plan in Microsoft Planner.

**Parameters:**
- `plan_name` (str): Name of the plan to be created.
- `group_id` (str): ID of the group to which the plan belongs.
- `access_token`: Access token for the Microsoft Graph API.

**Returns:**
- `str`: ID of the created plan.

**Example:**
```python
from msplanner_tools.plans import create_plan
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
plan_id = create_plan("my new plan", "my_group_id", token_manager.get_token())

if plan_id:
    print("Plan successfully created!")
```

#### `get_plan_by_id`
Retrieves a plan based on its ID.

**Parameters:**
- `plan_id` (str): ID of the plan.
- `access_token`: Access token for the Microsoft Graph API.

**Returns:**
- `dict`: Dictionary containing the plan data.

**Example:**
```python
from msplanner_tools.plans import get_plan_by_id

plan = get_plan_by_id("plan_id", token_manager.get_token())
print(plan)
```

#### `update_plan_by_id`
Updates a plan based on its ID and name.

**Parameters:**
- `plan_id` (str): ID of the plan.
- `plan_name` (str): New name of the plan.
- `access_token`: Access token for the Microsoft Graph API.

**Returns:**
- `None`

**Example:**
```python
from msplanner_tools.plans import update_plan_by_id

update_plan_by_id("plan_id", "updated plan name", token_manager.get_token())
print("Plan updated successfully.")
```

#### `delete_plan_by_id`
Deletes a plan based on its ID.

**Parameters:**
- `plan_id` (str): ID of the plan to be deleted.
- `access_token`: Access token for the Microsoft Graph API.

**Returns:**
- `None`

**Example:**
```python
from msplanner_tools.plans import delete_plan_by_id

delete_plan_by_id("plan_id", token_manager.get_token())
print("Plan deleted successfully.")
```

#### `get_plans_by_group_id`
Returns a list of all plans in a group.

**Parameters:**
- `group_id` (str): ID of the group.
- `access_token`: Access token for the Microsoft Graph API.

**Returns:**
- `list`: List of plans in the group.

**Example:**
```python
from msplanner_tools.plans import get_plans_by_group_id

plans = get_plans_by_group_id("group_id", token_manager.get_token())
print(plans)
```

#### `list_plan_tasks_by_id`
Returns a list of all tasks in a plan.

**Parameters:**
- `plan_id` (str): ID of the plan.
- `access_token`: Access token for the Microsoft Graph API.

**Returns:**
- `list`: List of tasks in the plan.

**Example:**
```python
from msplanner_tools.plans import list_plan_tasks_by_id

tasks = list_plan_tasks_by_id("plan_id", token_manager.get_token())
print(tasks)
```

**References**
- [MSAL Python Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview)

Next, continue to Tasks and Buckets for interacting with Microsoft Planner resources.
---
# Tasks

This section focuses on managing Microsoft Planner tasks using the functions provided in the `msplanner_tools.tasks` module.
<br>
[Return to the top](#authentication)

## Tasks Management

The `msplanner_tools.tasks` module provides functions to create, retrieve, update, and delete tasks in Microsoft Planner via the Microsoft Graph API.

### Functions Overview

#### `create_task`

Creates a new task in Microsoft Planner.

**Parameters:**
- `item_list` (dict): Dictionary with the task data:
    - `title` (str): Task name.
    - `assignments` (list): List of owners' emails.
    - `startDateTime` (str): Task start date in the format `YYYY-MM-DDTHH:MM:SSZ`.
    - `dueDateTime` (str): Task due date in the format `YYYY-MM-DDTHH:MM:SSZ`.
    - `priority` (int): Task priority (1-5).
    - `labels_list` (list): List of labels in the format `['category1', 'category2', ...]`.
- `bucket_id` (str): ID of the bucket to which the task belongs.
- `plan_id` (str): ID of the plan to which the task belongs.
- `access_token` (str): Access token for the Microsoft Graph API.
- `group_id` (str): ID of the group to which the task belongs.

**Returns:**
- `str`: ID of the created task.

**Example:**
```python
from msplanner_tools.tasks import create_task
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
item_list = {
        "title": "New Task",
        "assignments": ["owner@example.com"],
        "startDateTime": "2023-01-01T00:00:00Z",
        "dueDateTime": "2023-01-10T00:00:00Z",
        "priority": 1,
        "labels_list": ["category1", "category2"]
}
task_id = create_task(item_list, "bucket_id", "plan_id", token_manager.get_token(), "group_id")
if task_id:
        print("Task successfully created!")
```

#### `update_task_details`

Updates a task based on its ID, task data, ETag, and access token.

**Parameters:**
- `task_id` (str): ID of the task to be updated.
- `item_list` (dict): Dictionary with the task data to be updated.
- `etag` (str): ETag value of the task, obtained with the `get_task_etag` function.
- `access_token` (str): Access token for the Microsoft Graph API.

**Returns:**
- `None`

**Example:**
```python
from msplanner_tools.tasks import update_task_details
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
item_list = {
        "description": "Updated task description",
        "checklist": ["item1", "item2"]
}
etag = "etag_value"
update_task_details("task_id", item_list, etag, token_manager.get_token())
print("Task updated successfully.")
```

## References

- [MSAL Python Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-python)
- [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview)

Next, continue to [Buckets](buckets.md) for interacting with Microsoft Planner resources.

---
# Buckets

The `msplanner_tools.buckets` module provides functions to create, retrieve, and delete buckets in Microsoft Planner via the Microsoft Graph API.
<br>
[Return to the top](#authentication)

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
---
# Users

This section focuses on managing Microsoft Planner users using the functions provided in the `msplanner_tools.users` module.
<br>
[Return to the top](#authentication)

## Users Management

The `msplanner_tools.users` module provides functions to retrieve user information from Microsoft Planner via the Microsoft Graph API.

### Functions Overview

#### `find_user_id_by_email`
Finds a user ID based on their email address.

**Parameters:**
- `email` (str): Email address of the user.
- `group_id` (str): ID of the group to which the user belongs.
- `access_token` (str): Access token for the Microsoft Graph API.

**Returns:**
- `str`: ID of the user.

**Example:**
```python
from msplanner_tools.users import find_user_id_by_email
from msplanner_tools.auth import TokenManager

token_manager = TokenManager(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
user_id = find_user_id_by_email("user@example.com", "group_id", token_manager.get_token())
print(f'User ID: {user_id}')
```

**References**
- [MSAL Python Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview)
