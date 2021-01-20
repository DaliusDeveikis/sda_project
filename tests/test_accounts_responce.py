def test_with_authenticated_client(client, django_user_model):
    username = "username_test"
    password = "12345"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
