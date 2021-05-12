import pytest

from src.section_one.names_db import (
    NamesDB,
    DataAttributeError,
)


class TestNamesDB:
    def test_class_exists(self):
        """
        GIVEN a class name NamesDB
        WHEN globals() is checked for its existence
        THEN NamesDB must exist in the global namespace
        """
        assert "NamesDB" in globals()

    def test_class_has_attribute_called_data(
        self, names_db_obj
    ):
        """
        GIVEN an instance of the class
        WHEN hasattr(instance, 'attribute') is checked
        THEN the response == True
        """
        assert hasattr(names_db_obj, "data")

    def test_class_data_attr_can_only_be_list_or_tuple(
        self,
    ):
        """
        GIVEN a non-list value to data attribute
        WHEN instance is created
        THEN a DataAttributeError is raised with specific message
        """
        with pytest.raises(DataAttributeError) as exc:
            names_db_obj = NamesDB(data="")

        assert (
            str(exc.value)
            == "<data> argument must be a <<list>> or <<tuple>> type"
        )

    def test_class_data_cannot_be_empty(self):
        """
        GIVEN an empty list value is passed to data attribute
        WHEN instance is created
        THEN a DataAttributeError is raised with specific message
        """
        with pytest.raises(DataAttributeError) as exc:
            names_db_obj = NamesDB(data=[])

        assert (
            str(exc.value)
            == "<data> argument must not be empty"
        )

    def test_class_method_list_names_displays_all_names(
        self, names_db_obj, names_printed_dummy
    ):
        """
        GIVEN data of names
        WHEN list_names() is called
        THEN the output must be a new-line formatted string of all names
        """
        output = names_db_obj.list_names

        assert output == names_printed_dummy

    def test_class_method_list_names_at_pos_with_invalid_data(
        self, names_db_obj
    ):
        """
        GIVEN an invalid argument as position
        WHEN the method list_name_at_pos() is called
        THEN a DataAttributeError is raised with specific message
        """
        with pytest.raises(
            DataAttributeError
        ) as exc_empty_list:
            output = names_db_obj.list_names_at_pos([])

        with pytest.raises(
            DataAttributeError
        ) as exc_list_without_ints:
            output = names_db_obj.list_names_at_pos(
                ["*", "2", "abc"]
            )

        assert (
            str(exc_empty_list.value)
            == "<data> argument must not be empty"
        )
        assert (
            str(exc_list_without_ints.value)
            == "list <data> argument must a list of integers"
        )

    def test_class_method_list_names_at_pos(
        self, names_db_obj
    ):
        """
        GIVEN a list of positions or direct position
        WHEN the method list_name_at_pos() is called with a list or int
        THEN an output of those items are printed residing at the data index
        """
        output_1 = names_db_obj.list_names_at_pos(
            [1, 3, 5, 7]
        )
        assert output_1 == [
            "Alice",
            "Jeremy",
            "Henry",
            "Ashley",
        ]

        output_2 = names_db_obj.list_names_at_pos(4)
        assert output_2 == ["Sam"]

    def test_class_method_reverse_list_names(
        self, names_db_obj, names_list
    ):
        """
        GIVEN data of names during instantiation
        WHEN the method reverse_list_names() is called
        THEN the output is reversed
        """
        output = names_db_obj.reverse_list_names()
        assert output == list(reversed(names_list))

    def test_class_method_get_last_name(
        self, names_db_obj, names_list
    ):
        """
        GIVEN data of names during instantiation
        WHEN the property get_last_name is accessed
        THEN the output is last item in the data
        """
        output = names_db_obj.get_last_name
        assert output == names_list[-1]
