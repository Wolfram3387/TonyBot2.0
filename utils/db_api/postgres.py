import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\Wolfram\Downloads\tonytgbot-main\Tony-new\data\firebase_config.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://tony-bot-2b6a4-default-rtdb.firebaseio.com'})


class Students(object):
    
    def __init__(self, ref):
        self.__doc_ref = db.reference(ref + "Students/")
        self.__columns = {"id": str, "name": str, "timetable": dict, "lesson_notification": bool}

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


class Variants(object):

    def __init__(self, ref):
        self.__doc_ref = db.reference(ref + "Variants/")
        self.__columns = {"id": str, "category": str, "title": str, "answers": dict[str: list[str]], "release": int}

    def add(self, **kwargs):
        if list(kwargs.keys()) == list(self.__columns.keys()) and \
                list(map(lambda x: type(x), kwargs.values())) == list(self.__columns.values()):
            if self.select_all():
                self.__doc_ref.update({kwargs["id"]: kwargs})
            else:
                self.__doc_ref.set({kwargs["id"]: kwargs})

    def select_all(self):
        return self.__doc_ref.get() or []

    def select(self, variant_id: str):
        return self.__doc_ref.child(variant_id).get() or []

    def update(self, variant_id: int, **kwargs):
        self.__doc_ref.child(variant_id).update(kwargs)

    def delete(self, variant_id: int):
        self.__doc_ref.child(variant_id).delete()


if __name__ == '__main__':
    s = Students("/")
    v = Variants("/")
    print(s.select_all())
    s.add(id='123', name='egor', timetable={'10.10.2022': '12:00'}, lesson_notification=True)
    print(s.select_all())
    print(s.select("123"))
    s.update("123", name="egor1", timetable={"": ""}, lesson_notification=False)
    print(s.select("123"))
    s.delete("123")
    print(s.select_all())
    # ref.set({
    #     'Students': [
    #         {
    #             "id": 1,
    #             "name": "chel",
    #             "timetable": {},
    #             "lesson_notification": 0
    #         }
    #     ],
    #     'Variants': [
    #         {
    #             "id": 1,
    #             "category": "many",
    #             "title": "hello",
    #             "answer": "123"
    #         }
    #     ]
    # })
    # print(ref.get())
