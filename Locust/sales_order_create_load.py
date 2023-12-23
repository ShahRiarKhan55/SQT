from locust import HttpUser, task, between


# Define a Locust user class
class OdooUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to create a sales order
    @task(1)
    def create_sales_order(self):
        # Login payload for authentication
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

        # Payload to create a sales order
        create_order_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'sale.order', 'create', {
                    'partner_id': 1,
                    'order_line': [(0, 0, {
                        'product_id': 1,
                        'product_uom_qty': 2,
                        'price_unit': 100,
                    })]
                }]
            }
        }

        # Send a POST request to create a sales order
        self.client.post('/web/dataset/call_kw/sale.order/create', json=create_order_payload)

        # Payload to log out and destroy the session
        logout_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'logout',
                'args': ['database_name', session_id]
            }
        }

        # Send a POST request to log out and destroy the session
        self.client.post('/web/session/destroy', json=logout_payload)
