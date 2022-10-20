import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

from urllib.parse import quote_plus
cred = credentials.Certificate(r"..\..\data\firebase_config.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://tony-bot-2b6a4-default-rtdb.firebaseio.com'})


class Database(object):
    def __init__(self, columns, paths):
        self.__doc_ref = db.reference(paths)
        self.__columns = columns

    def add(self, **kwargs):
        if list(kwargs.keys()) == list(self.__columns.keys()) and \
                list(map(lambda x: type(x), kwargs.values())) == list(self.__columns.values()):
            if self.select_all():
                self.__doc_ref.update({kwargs["id"]: kwargs})
            else:
                self.__doc_ref.set({kwargs["id"]: kwargs})

    def select_all(self):
        return self.__doc_ref.get() or []

    def select(self, user_id: str):
        return self.__doc_ref.child(user_id).get() or []

    def update(self, user_id: str, **kwargs):
        self.__doc_ref.child(user_id).update(kwargs)

    def delete(self, user_id: str):
        self.__doc_ref.child(user_id).delete()


class Students(Database):
    def __init__(self, ref):
        columns = {"id": str, "name": str, "timetable": dict, "lesson_notification": bool}
        super(Students, self).__init__(columns, ref + "Students/")


class Variants(Database):
    def __init__(self, ref):
        columns = {"id": str, "category": str, "title": str, "answers": dict[str: list[str]], "release": int}
        super(Variants, self).__init__(columns, ref + "Variants/")


#---------------------------FOR TESTS-----------------------------------------------------
# if __name__ == '__main__':
#     s = Students("/")
#     v = Variants("/")
#     print(s.select_all())
#     s.add(id='123', name='egor', timetable={"12-12-12": "123"}, lesson_notification=True) #  ./#?$& break exception
#     print(s.select_all())
#     print(s.select("123"))
#     s.update("123", name="egor1", timetable={"3123": "12331"}, lesson_notification=False)
#     print(s.select("123"))
#     s.delete("123")
#     print(s.select_all())
