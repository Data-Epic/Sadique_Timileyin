from main import *
import pytest


# Test cases for open spreadsheet function
def test_open_one():
    assert open_spreadsheet("project 1202")


def test_open_two():
    with pytest.raises(ValueError, match="The sheet name expected a string object"):
        open_spreadsheet(1022)


def test_open_three():
    with pytest.raises(ValueError, match="The sheet name expected a string object"):
        open_spreadsheet(True)


# Test cases for create spreadsheet function
def test_create_one():
    assert create_spreadsheet("Opening")


def test_create_two():
    with pytest.raises(ValueError, match="The sheet name expected a string object"):
        create_spreadsheet(22.343)


def test_create_three():
    with pytest.raises(ValueError, match="The sheet name expected a string object"):
        create_spreadsheet(True)


# Test cases for select spreadsheet function
def test_select_one():
    assert select_spreadsheet("project 1202", "Sheet1")


def test_select_two():
    with pytest.raises(ValueError, match="The input expected a string object"):
        select_spreadsheet(1202, "Sheet1")


def test_select_three():
    with pytest.raises(ValueError, match="The input expected a string object"):
        select_spreadsheet(float, True)


# Test cases for worksheet format
def test_format_one():
    assert spreadsheet_format('project 1202', 'Sheet1', 'A1', 'C1')


def test_format_two():
    with pytest.raises(ValueError, match="The input expected a string object e.g 'A1' for the cols and rows input."
                                        "Wrong input expected a string object."):
        assert spreadsheet_format(110, float, 1, 3)


def test_format_three():
    with pytest.raises(ValueError, match="The input expected a string object e.g 'A1' for the cols and rows input."
                                        "Wrong input expected a string object."):
        assert spreadsheet_format(True, False, 1, 3)


def test_new_sheet_one():
    with pytest.raises(FileExistsError, match="This worksheet already exists"):
        assert new_worksheet("project 1202", "Companies", 100, 3)


def test_new_sheet_two():
    with pytest.raises(ValueError, match="The input expected a number/integer for the "
                                         "rows ands cols input, other inputs are strings"):
        assert new_worksheet("project 1202", True, 100, 3)


def test_new_sheet_three():
    with pytest.raises(ValueError, match="The input expected a number/integer for the "
                                         "rows ands cols input, other inputs are strings"):
        assert new_worksheet(False, True, float, 3)
