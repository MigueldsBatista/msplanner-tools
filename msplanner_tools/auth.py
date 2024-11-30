import msal
import time
"""
For more information on using MSAL, visit the official documentation:
https://msal-python.readthedocs.io/en/latest/

For more information on using Microsoft Graph, visit the official documentation:
https://docs.microsoft.com/en-us/graph/overview
"""
class TokenManager:
    """
    TokenManager is a class responsible for managing OAuth2 tokens for accessing Microsoft Graph API.
    Attributes:
        client_id (str): The client ID of the application.
        client_secret (str): The client secret of the application.
        tenant_id (str): The tenant ID of the Azure Active Directory.
        token (str): The current access token.
        expiration_time (float): The expiration time of the current token in epoch time.
    Methods:
        get_token() -> str:
            Retrieves a valid access token. If the current token is expired or not available, it requests a new one.
        request_new_token() -> str:
            Requests a new access token from the Microsoft identity platform using MSAL (Microsoft Authentication Library).
        is_token_expired() -> bool:
            Checks if the current token is expired.
    Usage:
        # Initialize the TokenManager with your client ID, client secret, and tenant ID
        token_manager = TokenManager(client_id='your_client_id', client_secret='your_client_secret', tenant_id='your_tenant_id')
        # Get a valid access token
        access_token = token_manager.get_token()
    """
    def __init__(self, client_id, client_secret, tenant_id) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.token = None
        self.expiration_time = None

    def get_token(self) -> str:
        if self.token is None or self.is_token_expired():
            self.token = self.request_new_token()
            self.expiration_time = time.time() + 600  # 10 minutos
        return self.token

    def request_new_token(self) -> str:

        authority_url = f'https://login.microsoftonline.com/{self.tenant_id}'

        scopes = ['https://graph.microsoft.com/.default']#Esse escopo acessa as permisões que o aplicativo tem acesso

        app = msal.ConfidentialClientApplication(self.client_id, authority=authority_url, client_credential=self.client_secret)

        token_response = app.acquire_token_for_client(scopes=scopes)
        
        return token_response.get('access_token')

    def is_token_expired(self) -> bool:
        return time.time() >= self.expiration_time