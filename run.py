import pytest


def main():
    pytest.main(['--alluredir', './target/my_allure_results'])
    #pytest.main()
