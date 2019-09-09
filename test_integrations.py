import pytest
import requests
import json

ROOT = 'http://127.0.0.1:5000/'

### --- HELPERS

# Does multiple tests comparing the result from a specific case
# to a specific expected result, 1:1 mapped
# Takes in a list called CASES, elements are strings that contain the URL
# Takes in a list called EXPECTS, elements are strings of the expected result from URL
# Takes in a string called KEY which is the json index of the result
# Takes in an int called CODE which is the expected status of the result
def basic_case_expected(CASES:list, EXPECTEDS:list, KEY:str, CODE:int):
    for CASE, EXPECTED in zip(CASES, EXPECTEDS):
        req = requests.get(CASE)
        assert req.status_code == CODE
        
        data = json.loads(req.text)
        assert data[KEY] == EXPECTED

### --- TESTS

# Does a simple test to make sure the root is there
# This is the same as testing if the API is online
def test_get_root():
    req = requests.get(ROOT)
    assert req.status_code == 200

    data = json.loads(req.text)
    assert data['about'] == 'Hello, World!'

# Does a simple test to make sure the root is there
# This will send a post request to root and echo it back
def test_post_root():
    # the key and value will be hashed different with each call
    # when checked, the value has no reason to be different from
    # what the hashed value generated was once we grab the result
    # from the API since it is logically just an echo
    KEY = str(hash('KEY'))
    VALUE = str(hash('VALUE'))

    data = {KEY:VALUE}
    req = requests.post(ROOT, json=data)

    assert req.status_code == 201

    data = json.loads(req.text)
    assert data['sent'][KEY] == VALUE

# Does a 1:1 compare test for a module that simply returns the 
# square root of the provided number
def test_sqrt():
    ENDPOINT = f'{ROOT}sqrt/'

    CASES = [
        f'{ENDPOINT}100',
        f'{ENDPOINT}81',
        f'{ENDPOINT}64',
    ]

    EXPECTEDS = [
        10.0,
        9.0,
        8.0,
    ]

    basic_case_expected(CASES, EXPECTEDS, 'result', 200)

# Does a 1:1 compare test for a module that calls the task delegator
# to queue a thread that will do a tail recursive fib call and pull
# the result from the queue and return the result and the execution time
# to the API
# The execution time is spontaenous and cannot be tested but, it can be tested
# to make sure it is not empty however, this is pointless because the only 
# instance that would be possible is if the function was killed amidst exection.
def test_fib():
    ENDPOINT = f'{ROOT}fib/'

    CASES = [
        f'{ENDPOINT}7',
        f'{ENDPOINT}100',
        f'{ENDPOINT}300',
    ]

    # results found from: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
    EXPECTEDS = [
        13,
        354224848179261915075,
        222232244629420445529739893461909967206666939096499764990979600,
    ]

    basic_case_expected(CASES, EXPECTEDS, 'result', 200)

    req = requests.get(f'{ENDPOINT}951')
    assert req.status_code == 500