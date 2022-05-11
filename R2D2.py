class R2D2:
    def __init__(self, alter):
        self.alter = alter

    def reproduced(self):
        match self.alter:
            case "Jung":
                return 0
            case "Erwachsen":
                return 4
            case "Alt":
                return 2

    def set_age(self, age):
        if isinstance(age, str):
            self.alter = age
        else:
            Errorcode = 404102
            print(f"Leider ist Ihre Eingabe Fehlerhaft! \n Errorcode : {Errorcode} ")
