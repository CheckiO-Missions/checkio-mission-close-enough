"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [9, 10, 5],
            "answer": [1, 1],
        },
        {
            "input": [2, 4, 100],
            "answer": [2, 1],
        },
        {
            "input": [2, 7, 100],
            "answer": [73, 26],
        },
        {
            "input": [3, 6, 100],
            "answer": [137, 84],
        },
    ],
    "Extra": [
        {
            "input": [4, 5, 1000],
            "answer": [916, 789],
        },
        {
            "input": [10, 11, 1000],
            "answer": [1107, 1063],
        },
        # {
        #     "input": [42, 99, 100000],
        #     "answer": [33896, 27571],
        # },
    ]
}
