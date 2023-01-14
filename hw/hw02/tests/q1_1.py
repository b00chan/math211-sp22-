test = {   'name': 'q1_1',
    'points': [0, 0, 4],
    'suites': [   {   'cases': [   {'code': ">>> import numpy as np\n>>> # It looks like you didn't make an array.\n>>> type(weird_numbers) == np.ndarray\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> len(weird_numbers) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.allclose(weird_numbers, np.array([   -2,    12,     3, 15625]), rtol=1e-03, atol=1e-03)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
