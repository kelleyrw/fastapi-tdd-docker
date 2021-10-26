import os


def test_env():
    print("\nenv:")

    def print_env(env):
        print(f"{env} : {os.getenv(env)}")

    print_env("PATH")
    print_env("PYTHONPATH")
    print_env("DATABASE_URL")
    print_env("DATABASE_TEST_URL")
    print_env("TESTING")
    print_env("ENVIRONMENT")


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!!", "testing": True}
