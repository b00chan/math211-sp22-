test = {   'name': 'q2_2',
    'points': [0, 0, 5],
    'suites': [   {   'cases': [   {'code': '>>> # Correlation is a number between -1 and 1\n>>> -1 <= r <= 1\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # It appears that you implemented std_units, but did so incorrectly\n'
                                               '>>> standard_units(np.arange(5)) is None or np.allclose(standard_units(np.arange(5)), [-1.41421356, -0.70710678,  0,  0.70710678,  1.41421356])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.isclose(r, 0.92503257641482783)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
