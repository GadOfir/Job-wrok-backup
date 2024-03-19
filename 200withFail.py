import unittest
import requests
from collections import OrderedDict


class ErrorTest(unittest.TestCase):
    default_params = OrderedDict([
        ('h_width', 6),
        ('h_length', 12),
        ('grip_type', 'FINGERTIP'),
        ('leniency', 0),
        ('wireless', 'false'),
        ('lefthanded', 'false'),
        ('buttons', -1),
        ('shape', 'both')
    ])

    def setUp(self):
        self.base_url = 'https://www.rocketjumpninja.com/api/search/mice'

    def _send_request(self, params):
        param_order = ['h_width', 'h_length', 'grip_type', 'leniency', 'wireless', 'lefthanded', 'buttons', 'shape']
        url = self.base_url + '?' + '&'.join([f"{k}={params[k]}" for k in param_order if k in params])

        print("Request URL:", url)
        response = requests.get(url)
        return response

    def send_test_request(self, params=None):
        if params is None:
            params = self.default_params
        return self._send_request(params)

    def test_server_error(self):
        # Sending a request that deliberately causes a server error

        response = self.send_test_request({'invalid_param': 'value'})
        #r=response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        if '{"success": false, "error"' in response.content.decode('utf-8'):
            print("Response Text:", response.content.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
