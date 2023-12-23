from locust import HttpUser, task, between

# Define a Locust user class for invoicing performance testing
class OdooInvoicingPerformanceUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to create an invoice
    @task
    def create_invoice(self):
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

        # Payload to create an invoice
        create_invoice_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'account.move', 'create', {
                    'partner_id': 1,  
                    'invoice_line_ids': [(0, 0, {
                        'name': 'Product ABC',  
                        'quantity': 2,
                        'price_unit': 50,
                    })]
                }]
            }
        }

        # Send a POST request to create an invoice
        self.client.post('/web/dataset/call_kw/account.move/create', json=create_invoice_payload)

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
