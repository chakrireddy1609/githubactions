import pytest
@pytest.mark.usefixtures("setup")
class Test_Sample():

    def test_sample(self):
        self.driver.get("https://accounts.staging.joveo.com")
        assert self.driver.title == "Joveo Account"

