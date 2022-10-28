from user.serializer import user_to_dict_json


def test_user_to_dict_json(db, user):
    serialized_user = user_to_dict_json(user)

    assert user.id == serialized_user["id"]
    assert user.first_name == serialized_user["first_name"]
    assert user.last_name == serialized_user["last_name"]
    assert user.email == serialized_user["email"]
