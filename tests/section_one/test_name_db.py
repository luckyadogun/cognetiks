import pytest

from src.section_one.names_db import NamesDB, DataAttributeError

class TestNamesDB:
    def test_class_exists(self):
        """
        GIVEN a class name NamesDB
        WHEN globals() is checked for its existence
        THEN NamesDB must exist in the global namespace
        """
        assert 'NamesDB' in globals()

    def test_class_has_attribute_called_data(self, names_list):
        """
        GIVEN an instance of the class
        WHEN hasattr(instance, 'attribute') is checked
        THEN the response == True
        """
        names_db_obj = NamesDB(data=names_list)
        assert hasattr(names_db_obj, 'data')

    def test_class_data_attr_is_array(self, names_list):
        """
        GIVEN a non-list value to data attribute
        WHEN instance is created
        THEN a DataAttributeError is raised with specific message
        """
        with pytest.raises(DataAttributeError) as exc:
            names_db_obj = NamesDB(data="")

        assert str(exc.value) == "<data> argument must be a <<list>> or <<tuple>> type"

    def test_class_data_cannot_be_empty(self):
        """
        GIVEN an empty list value is passed to data attribute
        WHEN instance is created
        THEN a DataAttributeError is raised with specific message
        """
        with pytest.raises(DataAttributeError) as exc:
            names_db_obj = NamesDB(data=[])

        assert str(exc.value) == "<data> argument must not be empty"

    def test_class_method_list_names_can_print_duplicates(self, names_list):
        """
        """

    
            

