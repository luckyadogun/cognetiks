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

    def test_class_data_attr_can_only_be_list_or_tuple(self, names_list):
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

    def test_class_method_list_names_displays_all_names(self, names_list):
        """
        GIVEN data of len X with possible duplicates
        WHEN the items in the data are printed
        THEN the out must match the total length of data
        """
        names_db_obj = NamesDB(data=names_list)
        output = names_db_obj.list_names()

        assert output == [f"Hello my name is {names}" for names in names_list]


    
            

