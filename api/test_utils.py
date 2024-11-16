from utils import *


class TestHelpers():
    def test_singleton_db(self):
        db1 = SheetDatabase("Yunzdle Database")
        db2 = SheetDatabase("Yunzdle Database")
        assert (db1 is db2) == True

    def test_singleton_enum(self):
        s1 = EnumSheet()
        s2 = EnumSheet()
        assert (s1 is s2) == True


class TestDatabase():
    def test_update(self):
        s = EnumSheet()
        db = SheetDatabase("Yunzdle Database")
        db.update(s.test)
        res = db.query(s.test)
        print(res)
        assert res == [{'test1': 11, 'test2': 21}, {'test1': 12, 'test2': 22}]


if __name__ == "__main__":
    main()
