# MSPlanner Tools Documentation

MSPlanner Tools is a Python library designed to streamline interactions with Microsoft Planner via the Microsoft Graph API. This documentation provides an overview of the library's features, focusing on Authentication and managing OAuth2 tokens using the TokenManager class.

## Overview
- [Authentication](#authentication)
- [Plans](plans.md)
- [Tasks](tasks.md)
- [Buckets](buckets.md)

## Authentication

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

Next, continue to Plans, Tasks, and Buckets for interacting with Microsoft Planner resources.
[Plans](plans.md)