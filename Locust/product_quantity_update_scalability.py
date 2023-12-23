from locust import HttpUser, task, between

# Define a Locust user class for inventory scalability testing
class OdooInventoryScalabilityUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to update product quantity
    @task
    def update_product_quantity(self):
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

        # Payload to update product quantity using stock.quant
        update_quantity_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'stock.quant', 'write', [[1], {'quantity': 50}]]
            }
        }

        # Send a POST request to update product quantity
        self.client.post('/web/dataset/call_kw/stock.quant/write', json=update_quantity_payload)

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

    # Method executed on the start of the user's task execution
    def on_start(self):
        pass
