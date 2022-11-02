class IDCtr:
    """
    A simple ascending integer ID counter.
    """

    def __init__(self):
        self.ctr = -1

    def count(self):
        self.ctr += 1
        return self.ctr

    def set_count(self, cnt):
        if cnt < self.ctr:
            raise Exception("Decreasing ID counters is illegal")
        else:
            self.ctr = cnt


class Base:
    """
    Base class for all abstract components. It provides:
    ...
    """

    _global_id_ctr = IDCtr()
    _prev_id_objs = {}

    @classmethod
    def obj_from_prev_id(cls, prev_id: int):
        """ returns the object with the given previous id """
        return cls._prev_id_objs.get(prev_id)

    complete_data_function = lambda data: data

    @staticmethod
    def complete_data(data: dict):
        return Base.complete_data_function(data)


    version: str = None

    # non-static

    def __init__(self):
        self.global_id = self._global_id_ctr.count()

        self.prev_global_id = None
        self.prev_version = None

    def data(self) -> dict:
        """
        Convert the object to a JSON compatible dict.
        Reserved field names are 'GID' and 'version'.
        """
        return {
            'GID': self.global_id,

            # version optional
            **({'version': self.version}
                if self.version is not None
                else {})
        }

    def load(self, data: dict):
        """
        Recreate the object state from the data dict returned by :code:`data()`.
        """
        if dict is not None:
            self.prev_global_id = data['GID']
            self._prev_id_objs[self.prev_global_id] = self
            self.prev_version = data.get('version')