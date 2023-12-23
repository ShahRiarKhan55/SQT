from locust import HttpUser, task, between

# Define a Locust user class for purchase integration testing
class OdooPurchaseIntegrationUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to create a purchase order
    @task
    def create_purchase_order(self):
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

        # Payload to create a purchase order
        create_order_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'purchase.order', 'create', {
                    'partner_id': 1,  
                    'order_line': [(0, 0, {
                        'product_id': 1,  
                        'product_qty': 5,
                        'price_unit': 200,
                    })]
                }]
            }
        }

        # Send a POST request to create a purchase order
        self.client.post('/web/dataset/call_kw/purchase.order/create', json=create_order_payload)

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
