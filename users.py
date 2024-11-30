import requests

"""
For more information on using MSAL, visit the official documentation:
https://msal-python.readthedocs.io/en/latest/

For more information on using Microsoft Graph, visit the official documentation:
https://docs.microsoft.com/en-us/graph/overview
"""

def find_user_id_by_email(email, group_id, access_token) -> str:
    
    """
    Returns the id of the user if the user exists in the group.

    Parameters
    ----------
    email : str
        Email of the user
    group_id : str
        ID of the group
    access_token : msal.PublicClientApplication
        Access token for the Microsoft Graph API

    Returns
    -------
    str
        ID of the user
    """
    user_url = f'https://graph.microsoft.com/v1.0/groups/{group_id}/members'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(user_url, headers=headers)

    if response.status_code == 200:
        users = response.json().get('value', [])
        for user in users:
            if user['mail'] == email:
                print(user['id'])
                return user['id']
            
        print(f'User {email} not found in the group.')
        return None

    print(f'Error fetching users: {response.status_code} - {response.text}')
    return None

def is_user_in_group(email, group_id, access_token) -> bool:
    """
    Checks if a user is in a group.

    Parameters
    ----------
    email : str
        Email of the user
    group_id : str
        ID of the group
    access_token : msal.PublicClientApplication
        Access token for the Microsoft Graph API

    Returns
    -------
    bool
        True if the user is in the group, False otherwise
    """
    user_url = f'https://graph.microsoft.com/v1.0/groups/{group_id}/members'

    headers = {
        'Authorization': f'Bearer {access_token.get_token()}',
        'Content-Type': 'application/json'
    }

    response = requests.get(user_url, headers=headers)

    if response.status_code == 200:
        users = response.json().get('value', [])
        for user in users:
            if user['mail'] == email:
                return True
        print(f'User {email} not found in the group.')
        return False
    else:
        print(f'Error fetching users: {response.status_code} - {response.text}')
        return False
