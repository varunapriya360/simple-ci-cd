from app import home

def test_home():
    assert "CI/CD" in home()
