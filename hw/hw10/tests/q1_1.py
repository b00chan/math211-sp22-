test = {   'name': 'q1_1',
    'points': [0, 0, 0, 5],
    'suites': [   {   'cases': [   {'code': '>>> standard_units([1,2,3,4,5])\narray([-1.41421356, -0.70710678,  0.        ,  0.70710678,  1.41421356])', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(np.mean(standard_units([1,2,3,4,5])), 0)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(np.std(standard_units([1,2,3,4,5])), 0.9999999999999999)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> standard_units([-3, -2, 1, 0, 1, 2, 3])\n'
                                               'array([-1.65988202, -1.15470054,  0.36084392, -0.14433757,  0.36084392,\n'
                                               '        0.8660254 ,  1.37120689])',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
