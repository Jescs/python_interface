import pytest
from day_01 import make_warnings


class TestWarns():
    def test_depre(self):
        with pytest.warns(DeprecationWarning):
            make_warnings.fxn()

    def test_not_warn(self):
        with pytest.warns(DeprecationWarning):
            make_warnings.not_warn()


if __name__ == "__main__":
    pytest.main()