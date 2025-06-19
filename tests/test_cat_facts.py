from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_calls_api_to_provide_cat_facts():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')
    
    requester_mock.get.return_value = response_mock
    
    response_mock.json.return_value = {
        "fact":"In Japan, cats are thought to have the power to turn into super spirits when they die. This may be because according to the Buddhist religion, the body of the cat is the temporary resting place of very spiritual people.i",
        "length":220
    }
    cat_facts = CatFacts(requester_mock)
    result = cat_facts.provide()
    assert result == 'Cat fact: In Japan, cats are thought to have the power to turn into super spirits when they die. This may be because according to the Buddhist religion, the body of the cat is the temporary resting place of very spiritual people.i'