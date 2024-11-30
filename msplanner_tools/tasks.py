import requests
import json

from .users import find_user_id_by_email

"""
For more information on using MSAL, visit the official documentation:
https://msal-python.readthedocs.io/en/latest/

For more information on using Microsoft Graph, visit the official documentation:
https://docs.microsoft.com/en-us/graph/overview
"""

def create_task(item_list, bucket_id: str, plan_id: str, access_token: str, group_id: str) -> str:
    """
    Creates a task based on its name, list of owners, start date, due date, and priority.
    
    Parameters
    ----------
    item_list : dict
        Dictionary with the task data:
            - title: task name
            - assignments: list of owners emails
            - startDateTime: task start date in the format YYYY-MM-DDTHH:MM:SSZ
            - dueDateTime: task due date in the format YYYY-MM-DDTHH:MM:SSZ
            - priority: task priority (1-5)
            - labels_list: list of labels in the format ['category1', 'category2', ...]
    bucket_id : str
        ID of the bucket to which the task belongs
    plan_id : str
        ID of the plan to which the task belongs
    access_token : str
        Access token for the Microsoft Graph API
    group_id : str
        ID of the group to which the task belongs
    
    Returns
    -------
    str
        ID of the created task
    """
    task_url = 'https://graph.microsoft.com/v1.0/planner/tasks'
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    task_name = item_list.get('title', 'Untitled Task')
    assignments_list = item_list.get('assignments', [])
    startDate = item_list.get('startDateTime', None)
    dueDate = item_list.get('dueDateTime', None)
    priority = item_list.get('priority', 1)
    categories = item_list.get('appliedCategories', [])

    assignments_data = {
        find_user_id_by_email(email, group_id, access_token): {
            "@odata.type": "#microsoft.graph.plannerAssignment",
            "orderHint": f" {index}!"
        } for index, email in enumerate(assignments_list)
    }

    appliedCategories = {
        category: True for category in categories
    }

    task_data = {
        "planId": plan_id,
        "bucketId": bucket_id,
        "title": task_name,
        "assignments": assignments_data,
        "orderHint": f" 0!",
        "startDateTime": startDate,
        "dueDateTime": dueDate,
        "priority": priority,
        "appliedCategories": appliedCategories
    }

    response = requests.post(task_url, headers=headers, data=json.dumps(task_data))

    if response.status_code == 201:
        task_id = response.json()['id']
        print(f'Task created successfully: {task_id}')
        return task_id
    
    print(f'Error creating task: {response.json()}')
    return None

def update_task_details(task_id, item_list, etag, access_token):
    """
    Updates a task based on its ID, task data, ETag, and access token.

    Parameters
    ----------
    task_id : str
        ID of the task to be updated
    item_list : dict
        Dictionary with the task data to be updated
    etag : str
        ETag value of the task, obtained with the get_task_etag function
    access_token : str
        Access token for the Microsoft Graph API

    Returns
    -------
    None

    Notes
    -----
    The Microsoft Graph API returns the ETag of the task in the response of the API
    /planner/tasks/{task_id}/details. The ETag is a string that represents the
    hash value of the task content. This string is used to verify if the task
    has been modified since it was last read.
    """
    
    task_url = f'https://graph.microsoft.com/v1.0/planner/tasks/{task_id}/details'
    description = item_list.get('description', None)
    checklist_titles = item_list.get('checklist', [])

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation',
        'If-Match': etag  # Includes the ETag in the header
    }
    
    import uuid  # To generate unique UUIDs

    # Generate unique UUIDs for each checklist item
    checklist_items = {
        str(uuid.uuid4()): {
            "@odata.type": "microsoft.graph.plannerChecklistItem",
            "title": checklist,
            "isChecked": False
        } for checklist in checklist_titles
    }

    task_data = {
        "description": description,
        "checklist": checklist_items,
    }

    response = requests.patch(task_url, headers=headers, data=json.dumps(task_data))

    if response.status_code == 200:
        print(f'Task {task_id} updated successfully.\n')
        print(response.json())
    else:
        print(f'Error updating task: {response.status_code} - {response.text}')

def get_task_etag(task_id, access_token):
    """
    Gets the ETag of a task based on its ID and access token.

    Parameters
    ----------
    task_id : str
        ID of the task
    access_token : str
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ETag value of the task

    Notes
    -----
    The Microsoft Graph API returns the ETag of the task in the response of the API
    /planner/tasks/{task-id}/details. The ETag is a string that represents the
    hash value of the task content. This string is used to verify if the task
    has been modified since it was last read.
    """
    plan_url = f'https://graph.microsoft.com/v1.0/planner/tasks/{task_id}/details'
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(plan_url, headers=headers)
    
    if response.status_code == 200:
        etag = response.headers.get('ETag')
        print(f"Task ETag: {etag}")
        return etag
    
    print(f'Error getting task ETag: {response.status_code} - {response.text}')
    return None

def delete_task(task_id, access_token):
    """
    Deletes a task based on its ID and access token.

    Parameters
    ----------
    task_id : str
        ID of the task
    access_token : str
        Access token for the Microsoft Graph API

    Returns
    -------
    None

    Notes
    -----
    The Microsoft Graph API returns the ETag of the task in the response of the API
    /planner/tasks/{task-id}/details. The ETag is a string that represents the
    hash value of the task content. This string is used to verify if the task
    has been modified since it was last read.
    """
    task_url = f'https://graph.microsoft.com/v1.0/planner/tasks/{task_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.delete(task_url, headers=headers)
    
    if response.status_code == 204:
        print(f'Task {task_id} deleted successfully.\n')
    else:
        print(f'Error deleting task: {response.status_code} - {response.text}')

def get_task_by_id(task_id, access_token):
    """
    Returns a task based on its ID and access token.

    Parameters
    ----------
    task_id : str
        ID of the task
    access_token : str
        Access token for the Microsoft Graph API

    Returns
    -------
    dict
        Dictionary containing the task data

    Notes
    -----
    The Microsoft Graph API returns the ETag of the task in the response of the API
    /planner/tasks/{task-id}/details. The ETag is a string that represents the
    hash value of the task content. This string is used to verify if the task
    has been modified since it was last read.
    """
    task_url = f'https://graph.microsoft.com/v1.0/planner/tasks/{task_id}/details'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(task_url, headers=headers)
    
    if response.status_code == 200:
        task = response.json()
        return task
    else:
        print(f'Error getting task: {response.status_code} - {response.text}')
        return None
