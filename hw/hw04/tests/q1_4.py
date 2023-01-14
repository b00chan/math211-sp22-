test = {   'name': 'q1_4',
    'points': [1, 1, 7],
    'suites': [   {   'cases': [   {'code': '>>> # Number of columns should be 2\n>>> california_burritos.num_columns == 2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> # Number of rows should be 19\n>>> california_burritos.num_rows == 19\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(round(california_burritos.where(0, "California").column(1).item(0), 4), 3.5242)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
