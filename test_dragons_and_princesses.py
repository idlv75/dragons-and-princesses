import pytest
from dragons_and_princesses import DragonsAndPrincesses


class TestDragonsAndPrincesses:

    def test_dragons_and_princesses_marry_final_princess(self, capsys):
        DragonsAndPrincesses('input_files/example1.yml').dragons_and_princesses()
        captured = capsys.readouterr()
        assert captured[0] == '13\n2\n3 5\n'

    def test_dragons_and_princesses_dont_marry_final_princess(self, capsys):
        DragonsAndPrincesses('input_files/example2.yml').dragons_and_princesses()
        captured = capsys.readouterr()
        assert captured[0] == '-1\n'

    def test_dragons_and_princesses_value_error(self):
        with pytest.raises(ValueError):
            DragonsAndPrincesses('input_files/value_err_example.yml').dragons_and_princesses()
