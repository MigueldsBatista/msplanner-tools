import requests
import json

"""
For more information on using MSAL, visit the official documentation:
https://msal-python.readthedocs.io/en/latest/

For more information on using Microsoft Graph, visit the official documentation:
https://docs.microsoft.com/en-us/graph/overview
"""

def create_plan(plan_name: str, group_id: str, access_token) -> str:
    """
    Creates a plan in Microsoft Planner based on the name and group ID it belongs to.

    Parameters
    ----------
    plan_name : str
        Name of the plan to be created
    group_id : str
        ID of the group to which the plan belongs
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ID of the created plan
    """
    plan_url = 'https://graph.microsoft.com/v1.0/planner/plans'  # URL to create a plan

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    plan_json = {
        "owner": group_id,
        "title": plan_name
    }

    # Creating the plan
    response = requests.post(plan_url, headers=headers, data=json.dumps(plan_json))  # dumps converts to JSON format

    if response.status_code == 201:
        plan_id = response.json()['id']
        print(f'Plan created successfully: {plan_id}')
        return plan_id
    
    print(f'Error creating plan: {response.json()}')
    return None


def get_plan_etag(plan_id, access_token) -> str:
    """
    Gets the ETag of a plan based on its ID and access token.

    Parameters
    ----------
    plan_id : str
        ID of the plan
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ETag value of the plan

    Notes
    -----
    The Microsoft Graph API returns the ETag of the plan in the response of the
    /planner/plans/{plan-id} API. The ETag is a string that represents the hash
    value of the plan's content. This string is used to check if the plan has
    been modified since it was last read.
    """
    plan_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}'
    
    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(plan_url, headers=headers)
    
    if response.status_code == 200:
        etag = response.headers.get('ETag')
        print(f"Plan ETag: {etag}")
        return etag
    
    print(f'Error getting plan ETag: {response.status_code} - {response.text}')
    return None

def delete_plan_by_id(plan_id, access_token) -> None:
    """
    Deletes a plan based on its ID and ETag.

    Parameters
    ----------
    plan_id : str
        ID of the plan to be deleted
    access_token :Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    None

    Notes
    -----
    The Microsoft Graph API returns the ETag of the plan in the response of the
    /planner/plans/{plan-id} API. The ETag is a string that represents the hash
    value of the plan's content. This string is used to check if the plan has
    been modified since it was last read.
    """
    etag = get_plan_etag(plan_id, access_token)

    print(f"Plan ETag: {etag}")
    if etag is None:
        print("Could not get ETag, deletion aborted.")
        return

    plan_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json',
        'If-Match': etag  # Includes the ETag in the header
    }

    response = requests.delete(plan_url, headers=headers)

    if response.status_code == 204:
        print(f'Plan {plan_id} deleted successfully.')
        return
    
    print(f'Error deleting plan: {response.status_code} - {response.text}')
    return 


def get_plans_by_group_id(group_id, access_token) -> list:
    """
    Returns a list containing all plans of a group.

    Parameters
    ----------
    group_id : str
        ID of the group
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    list
        List containing all plans of the group
    """
    plan_url = f'https://graph.microsoft.com/v1.0/groups/{group_id}/planner/plans'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(plan_url, headers=headers)

    if response.status_code == 200:
        plans = response.json().get('value', [])
        return plans
    
    print(f'Error getting group plans: {response.status_code} - {response.text}')
    return []

def update_plan_by_id(plan_id, plan_name, access_token) -> None:
    """
    Updates a plan based on its ID and name.

    Parameters
    ----------
    plan_id : str
        ID of the plan
    plan_name : str
        Name of the plan
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    None

    Notes
    -----
    The Microsoft Graph API returns the ETag of the plan in the response of the
    /planner/plans/{plan-id} API. The ETag is a string that represents the hash
    value of the plan's content. This string is used to check if the plan has
    been modified since it was last read.
    """
    plan_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }    

    plan_json = {
        "title": plan_name
    }

    response = requests.patch(plan_url, headers=headers, json=plan_json)

    if response.status_code == 200:
        print(f'Plan {plan_id} updated successfully.')
        return
    
    print(f'Error updating plan: {response.status_code} - {response.text}')    
    return
    

def get_plan_by_id(plan_id, access_token) -> dict:
    """
    Returns a plan based on its ID.

    Parameters
    ----------
    plan_id : str
        ID of the plan
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    dict
        Dictionary containing the plan data

    Notes
    -----
    The Microsoft Graph API returns the ETag of the plan in the response of the
    /planner/plans/{plan-id} API. The ETag is a string that represents the hash
    value of the plan's content. This string is used to check if the plan has
    been modified since it was last read.
    """
    plan_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(plan_url, headers=headers)

    if response.status_code == 200:
        plan = response.json()
        return plan
    
    print(f'Error getting plan: {response.status_code} - {response.text}')
    return {}

def list_plan_tasks_by_id(plan_id, access_token) -> list:
    """
    Returns a list containing all tasks of a plan.

    Parameters
    ----------
    plan_id : str
        ID of the plan
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    list
        List containing all tasks of the plan

    Notes
    -----
    The Microsoft Graph API returns the ETag of the plan in the response of the
    /planner/plans/{plan-id} API. The ETag is a string that represents the hash
    value of the plan's content. This string is used to check if the plan has
    been modified since it was last read.
    """
    plan_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}/tasks'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(plan_url, headers=headers)

    if response.status_code == 200:
        tasks = response.json().get('value', [])
        return tasks
    
    print(f'Error getting plan tasks: {response.status_code} - {response.text}')
    return []
