import requests
import json
"""
For more information on using MSAL, visit the official documentation:
https://msal-python.readthedocs.io/en/latest/

For more information on using Microsoft Graph, visit the official documentation:
https://docs.microsoft.com/en-us/graph/overview
"""

def create_bucket(bucket_name, plan_id, access_token, bucket_num) -> str:    
    """
    Creates a bucket in Microsoft Planner based on the name and the plan ID to which it belongs.

    Parameters
    ----------
    bucket_name : str
        Name of the bucket to be created
    plan_id : str
        ID of the plan to which the bucket belongs
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API
    bucket_num : int
        Number of the bucket to be created (starts at 0)

    Returns
    -------
    str
        ID of the created bucket
    """
    bucket_url = 'https://graph.microsoft.com/v1.0/planner/buckets'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    bucket_data = {
        "name": bucket_name,
        "planId": plan_id,
        "orderHint": f" {bucket_num}!"
    }

    response = requests.post(bucket_url, headers=headers, data=json.dumps(bucket_data))

    if response.status_code == 201:
        bucket_id = response.json()['id']
        bucket_num += 1
        print(f'Bucket {bucket_name} created successfully: {bucket_id}')
        return bucket_id
    
    print(f'Error creating bucket: {response.json()}')
    return None

def get_bucket_id(bucket_name, plan_id, access_token) -> str:
    """
    Retrieves the ID of a bucket based on its name and the plan ID to which it belongs.

    Parameters
    ----------
    bucket_name : str
        Name of the bucket to be retrieved
    plan_id : str
        ID of the plan to which the bucket belongs
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ID of the found bucket. If the bucket is not found, returns None.
    """
    bucket_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}/buckets'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(bucket_url, headers=headers)

    if response.status_code == 200:
        buckets = response.json().get('value', [])
        for bucket in buckets:
            if bucket['name'] == bucket_name and bucket['planId'] == plan_id:
                return bucket['id']
        print(f'Bucket {bucket_name} not found in plan {plan_id}.')
    else:
        print(f'Error retrieving buckets: {response.status_code} - {response.text}')
    
    return None

def get_bucket_name(bucket_id, plan_id, access_token) -> str:
    """
    Retrieves the name of a bucket based on its ID and the plan ID to which it belongs.

    Parameters
    ----------
    bucket_id : str
        ID of the bucket to be retrieved
    plan_id : str
        ID of the plan to which the bucket belongs
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        Name of the found bucket. If the bucket is not found, returns None.
    """
    bucket_url = f'https://graph.microsoft.com/v1.0/planner/plans/{plan_id}/buckets/{bucket_id}'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(bucket_url, headers=headers)

    if response.status_code == 200:
        bucket = response.json()
        return bucket['name']
    else:
        print(f'Error retrieving bucket: {response.status_code} - {response.text}')
    
    return None

def delete_bucket(bucket_id, access_token) -> str:
    """
    Deletes a bucket based on its ID and the access token.

    Parameters
    ----------
    bucket_id : str
        ID of the bucket
    access_token :Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ID of the deleted bucket
    """
    bucket_url = f'https://graph.microsoft.com/v1.0/planner/buckets/{bucket_id}'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.delete(bucket_url, headers=headers)

    if response.status_code == 204:
        print(f'Bucket {bucket_id} deleted successfully.')
        return bucket_id
    else:
        print(f'Error deleting bucket: {response.status_code} - {response.text}')
    
    return None

def update_bucket(bucket_id, bucket_name, access_token) -> str:
    """
    Updates the name of a bucket based on its ID and the access token.

    Parameters
    ----------
    bucket_id : str
        ID of the bucket
    bucket_name : str
        Name of the bucket
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ID of the updated bucket
    """
    bucket_url = f'https://graph.microsoft.com/v1.0/planner/buckets/{bucket_id}'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    bucket_data = {
        "name": bucket_name
    }

    response = requests.patch(bucket_url, headers=headers, data=json.dumps(bucket_data))

    if response.status_code == 204:
        print(f'Bucket {bucket_id} updated successfully.')
        return bucket_id
    else:
        print(f'Error updating bucket: {response.status_code} - {response.text}')
    
    return None

def list_bucket_tasks(bucket_id, access_token) -> list:
    """
    Lists the tasks of a bucket based on its ID and the access token.

    Parameters
    ----------
    bucket_id : str
        ID of the bucket
    access_token : Use the get_token() method of the TokenManager class to get the access token.
        Access token for the Microsoft Graph API

    Returns
    -------
    list
        List of tasks in the bucket
    """
    bucket_url = f'https://graph.microsoft.com/v1.0/planner/buckets/{bucket_id}/tasks'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(bucket_url, headers=headers)

    if response.status_code == 200:
        tasks = response.json().get('value', [])
        return tasks
    else:
        print(f'Error retrieving tasks: {response.status_code} - {response.text}')
    
    return None
