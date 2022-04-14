# Test by test
def test_should_status_code_hello_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_should_status_code_other_ok(client):
    response = client.get('/other')
    assert response.status_code == 200


def test_should_status_code_exp_error(client):
    try:
        response = client.get('/exp')
        assert response.status_code == 500
    except ValueError as e:
        assert e == True


# Multiple assert
def test_multiple_assert(client):
    response_one = client.get('/')
    response_two = client.get('/other')
    response_three = client.get('/exp')
    assert (
        response_one,
        response_one.status_code == 200,

        response_two,
        response_two.status_code == 200,

        response_three,
        ValueError
    )
