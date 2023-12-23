from locust import HttpUser, task, between

# Define a Locust user class for product scalability testing
class OdooProductScalabilityUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to create a product
    @task
    def create_product(self):
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

        # Payload to create a product
        create_product_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'product.template', 'create', {
                    'name': 'Test Product',
                    'type': 'product',
                    'list_price': 50,
                }]
            }
        }

        # Send a POST request to create a product
        self.client.post('/web/dataset/call_kw/product.template/create', json=create_product_payload)

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
