test = {   'name': 'q2_8',
    'points': [0, 0, 2, 2],
    'suites': [   {   'cases': [   {'code': '>>> len(sampled_stats) == 5000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.std(sampled_stats) > 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 6 < np.std(sampled_stats) < 10\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> -11.5 < percentile(10, sampled_stats) < -9\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
