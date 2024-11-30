# MSPlanner Tools - Tasks Documentation

This section focuses on managing Microsoft Planner tasks using the functions provided in the `msplanner_tools.tasks` module.

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