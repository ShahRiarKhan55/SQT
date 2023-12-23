from locust import HttpUser, task, between
import random

# Define a Locust user class for searching stress testing
class OdooSearchStressUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to perform a search operation
    @task(1)
    def perform_search(self):
        # Payload for logging in
        login_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'login',
                'args': ['database_name', 'username', 'password']
            }
        }

        # Send a POST request to authenticate and get the session ID
        response = self.client.post('/web/session/authenticate', json=login_payload)
        session_id = response.json()['result']['session_id']

        # Define search criteria
        search_criteria = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute_kw',
                'args': ['database_name', session_id, 'password', 'res.partner', 'search_read',
                         [[['name', 'ilike', random.choice(['Customer', 'Supplier', 'Vendor'])]]],
                         {'fields': ['id', 'name']}
                         ]
            }
        }

        # Send a POST request to perform the search operation
        self.client.post('/web/dataset/call_kw/res.partner/search_read', json=search_criteria)

        # Payload for logging out and destroying the session
        logout_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'logout',
                'args': ['database_name', session_id]
            }
        }

        # Send a POST request to logout and destroy the session
        self.client.post('/web/session/destroy', json=logout_payload)
