class Operations:

    # init method or constructor
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj

    def keys(self):
        """ KEYS """
        """ Returns all the keys in the dictionary. Order is not guaranteed.
        """
        if len(list(self.dict_obj.keys())) > 0:
            return list(self.dict_obj.keys()), "success"
        else:
            return None, "empty set"

    def members(self, the_key):
        """ MEMBERS """
        """ Returns the collection of strings for the given key. Return order is not guaranteed.
        Returns an error if the key does not exist."""

        if self.key_exists(the_key)[1]:
            return self.dict_obj[the_key], None
        else:
            return None, "ERROR, key does not exist."

    def add(self, the_key, new_member):
        """ ADD """
        """ Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
        """
        if not self.key_exists(the_key)[1]:
            self.dict_obj[the_key] = []

        existing_members = self.dict_obj[the_key]
        if new_member not in existing_members:
            existing_members.append(new_member)
            self.dict_obj[the_key] = existing_members
            return None, "Added"
        else:
            return None, "ERROR, member already exists for key"

    def remove_member(self, the_key, member):
        """ REMOVE """
        """ Removes a member from a key. If the last member is removed from the key, the key is removed from the dictionary.
        If the key or member does not exist, displays an error."""

        if self.key_exists(the_key)[1]:
            existing_members = self.dict_obj[the_key]
            if not self.member_exists(the_key, member)[1]:
                return None, "ERROR, member does not exist"
            else:
                existing_members.remove(member)
                if len(existing_members) == 0:
                    del self.dict_obj[the_key]
                else:
                    self.dict_obj[the_key] = existing_members
                return None, "Removed"
        else:
            return None, "ERROR, key does not exist"

    def remove_all(self, the_key):
        """ REMOVEALL """
        if self.key_exists(the_key)[1]:
            del self.dict_obj[the_key]
            return None, "Removed"
        else:
            return None, "ERROR, key does not exist"

    def clear(self):
        """ CLEAR """
        """ Removes all keys and all members from the dictionary"""
        auxiliary_copy = self.dict_obj.copy()
        for k in auxiliary_copy:
            del self.dict_obj[k]

        return None, "cleared"

    def key_exists(self, the_key):
        """ KEYEXISTS """
        """ Returns whether a key exists or not."""
        if the_key in self.dict_obj.keys():
            return None, True
        else:
            return None, False

    def member_exists(self, the_key, member):
        """ MEMBEREXISTS """
        """ Returns whether a member exists within a key. Returns false if the key does not exist. """
        if self.key_exists(the_key)[1]:
            existing_members = self.dict_obj[the_key]
            if member in existing_members:
                return None, True
            else:
                return None, False
        else:
            return None, "ERROR, Key Does Not Exist"

    def all_members(self):
        """ ALLMEMBERS """
        """ Returns all the members in the dictionary. Returns nothing if there are none. Order is not guaranteed."""
        all_the_members = []
        for the_key in self.dict_obj.keys():
            all_the_members.extend(self.dict_obj[the_key])

        if len(all_the_members) > 0:
            return all_the_members, "success"
        else:
            return None, "empty set"

    def items(self):
        """ ITEMS """
        """ Returns all keys in the dictionary and all of their members. Returns nothing if there are none.
        Order is not guaranteed.
    """
        if len(list(self.dict_obj.keys())) == 0:
            return None, "empty set"
        else:
            return self.dict_obj, "success"
