# MSPlanner Tools - Plans Documentation

This section focuses on managing Microsoft Planner plans using the functions provided in the `msplanner_tools.plans` module.

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
[Tasks](tasks.md)