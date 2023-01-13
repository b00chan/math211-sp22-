test = {   'name': 'q1_2',
    'points': [0, 0, 20],
    'suites': [   {   'cases': [   {'code': '>>> final_scores.num_columns\n3', 'hidden': False, 'locked': False},
                                   {'code': ">>> set(['Opponent', 'Cal Score', 'Opponent Score']) == set(final_scores.labels)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> final_scores.take(range(5, 11))\n'
                                               'Opponent     | Cal Score | Opponent Score\n'
                                               'Oregon       | 17        | 24\n'
                                               'Colorado     | 26        | 3\n'
                                               'Oregon State | 39        | 25\n'
                                               'Arizona      | 3         | 10\n'
                                               'Stanford     | 41        | 11\n'
                                               'UCLA         | 14        | 42',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
