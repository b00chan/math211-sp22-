test = {   'name': 'q2_7',
    'points': [1, 3],
    'suites': [   {   'cases': [   {'code': '>>> -50 < simulate_precipitation_null() < 50\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> ts = [simulate_precipitation_null() for _ in range(1000)]\n>>> 6 <= np.array(ts).std() <= 10\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
