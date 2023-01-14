test = {   'name': 'q1_9_2',
    'points': [0, 0, 10],
    'suites': [   {   'cases': [   {'code': '>>> type(prob_test) in set([float, np.float32, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> # Should be a decimal, not a percentage\n>>> 0 <= prob_test <= 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(prob_test, 0.5)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
