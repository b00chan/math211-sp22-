test = {   'name': 'q3_7',
    'points': [0, 0, 3],
    'suites': [   {   'cases': [   {'code': '>>> type(fit_line(example_table)) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(fit_line(example_table).item(0)) in set([float, np.float32, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(fit_line(example_table).item(0), 2) and np.isclose(fit_line(example_table).item(1), 1)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
