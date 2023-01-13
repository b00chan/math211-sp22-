test = {   'name': 'q1_2',
    'points': [0, 4, 4],
    'suites': [   {   'cases': [   {   'code': '>>> # Ensure your correlation function returns one number between -1 and 1\n'
                                               '>>> abs(correlation(Table().with_columns(\'a\', np.random.normal(0, 1, 10),\'b\', np.random.normal(0, 1, 10)), "a", "b")) <= 1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.allclose(standard_units(np.arange(5)), np.sqrt(2)/2 * np.arange(-2, 3))\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> np.isclose(round(correlation(birds, "Egg Weight", "Bird Weight"), 3), 0.847)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
