import unittest
from operations import Operations


class TestOperations(unittest.TestCase):
    def setUp(self):
        self.o = Operations({})

    def test_keys_populated(self):
        self.o.dict_obj = {"test_key": "test_value"}
        result, message = self.o.keys()
        assert (result, message) == (list(["test_key"]), "success")

    def test_keys_empty(self):
        result, message = self.o.keys()
        assert (result, message) == (None, "empty set")

    def test_members_populated(self):
        self.o.dict_obj = {"test_key": ["test_value"]}
        result, message = self.o.members("test_key")
        assert (result, message) == (["test_value"], None)

    def test_members_empty(self):
        result, message = self.o.members("test_key")
        assert (result, message) == (None, "ERROR, key does not exist.")

    def test_add_key_does_not_exist(self):
        result, message = self.o.add("test_key", "test_value")
        assert (result, message) == (None, "Added")
        assert self.o.dict_obj == dict({"test_key": ["test_value"]})

    def test_add_key_exists(self):
        self.o.dict_obj = {"test_key": ["test_value"]}
        result, message = self.o.add("test_key", "test_value_2")
        assert (result, message) == (None, "Added")
        assert self.o.dict_obj == dict({"test_key": ["test_value",
                                                     "test_value_2"]})

    def test_remove_member_key_and_member_exists(self):
        self.o.dict_obj = {"test_key": ["test_value", "test_value_2"]}
        result, message = self.o.remove_member("test_key", "test_value_2")
        assert (result, message) == (None, "Removed")
        assert self.o.dict_obj == dict({"test_key": ["test_value"]})

    def test_remove_member_key_does_not_exists(self):
        result, message = self.o.remove_member("test_key", "test_value")
        assert (result, message) == (None, "ERROR, key does not exist")

    def test_remove_member_key_exist_member_does_not_exists(self):
        self.o.dict_obj = {"test_key": ["test_value"]}
        result, message = self.o.remove_member("test_key", "test_value_2")
        assert (result, message) == (None, "ERROR, member does not exist")

    def test_remove_all_key_exists(self):
        self.o.dict_obj = {"test_key": ["test_value"]}
        result, message = self.o.remove_all("test_key")
        assert (result, message) == (None, "Removed")
        assert self.o.dict_obj == dict({})

    def test_remove_all_key_does_not_exists(self):
        result, message = self.o.remove_all("test_key")
        assert (result, message) == (None, "ERROR, key does not exist")
        assert self.o.dict_obj == dict({})

    def test_clear_dict_populated(self):
        self.o.dict_obj = {"test_key": ["test_value", "test_value_2"]}
        result, message = self.o.clear()
        assert (result, message) == (None, "cleared")
        assert self.o.dict_obj == dict({})

    def test_clear_dict_empty(self):
        self.o.dict_obj = {}
        result, message = self.o.clear()
        assert (result, message) == (None, "cleared")
        assert self.o.dict_obj == dict({})

    def test_key_exists_false(self):
        self.o.dict_obj = {}
        result, message = self.o.key_exists("test_key")
        assert (result, message) == (None, False)

    def test_key_exists_true(self):
        self.o.dict_obj = {"test_key": ["test_value", "test_value_2"]}
        result, message = self.o.key_exists("test_key")
        assert (result, message) == (None, True)

    def test_member_exists_true(self):
        self.o.dict_obj = {"test_key": ["test_value", "test_value_2"]}
        result, message = self.o.member_exists("test_key", "test_value_2")
        assert (result, message) == (None, True)

    def test_member_exists_false(self):
        self.o.dict_obj = {"test_key": ["test_value"]}
        result, message = self.o.member_exists("test_key", "test_value_2")
        assert (result, message) == (None, False)

    def test_member_exists_key_does_not_exists(self):
        self.o.dict_obj = {"test_key_1": ["test_value"]}
        result, message = self.o.member_exists("test_key", "test_value")
        assert (result, message) == (None, "ERROR, Key Does Not Exist")

    def test_all_members_not_empty(self):
        self.o.dict_obj = {"test_key": ["test_value", "test_value_2"]}
        result, message = self.o.all_members()
        assert (result, message) == (["test_value", "test_value_2"], "success")

    def test_all_members_empty(self):
        self.o.dict_obj = {}
        result, message = self.o.all_members()
        assert (result, message) == (None, "empty set")

    def test_items_empty(self):
        self.o.dict_obj = {}
        result, message = self.o.items()
        assert (result, message) == (None, "empty set")

    def test_items_populated(self):
        self.o.dict_obj = {"test_key": ["test_value", "test_value_2"]}
        result, message = self.o.items()
        assert (result, message) == (dict({"test_key": ["test_value", "test_value_2"]}), "success")
