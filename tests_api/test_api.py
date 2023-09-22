import requests
from data import TestData


def test_authorization(get_url_api):
    response1 = requests.post(f'{get_url_api}/user/login',
                              data=TestData.login_data
                              )

    response_dict = response1.json()

    token = response1.headers['x-csrf-token']
    auth_sid = response1.cookies['auth_sid']
    user_id = response_dict['user_id']

    assert response1.status_code == 200, 'Unexpected status code'

    assert 'user_id' in response_dict, 'No user_id in response'
    assert response_dict['user_id'] == 2, 'Unexpected user_id value'

    response2 = requests.get(f'{get_url_api}/user/{user_id}',
                             headers={'x-csrf-token': token},
                             cookies={'auth-sid': auth_sid}
                             )
    response2_dict = response2.json()
    assert 'username' in response2_dict, 'No username in response'
    assert response2_dict['username'] == 'Vitaliy', 'Unexpected username value'
