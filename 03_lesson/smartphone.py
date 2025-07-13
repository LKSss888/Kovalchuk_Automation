class Smartphone:

    def __init__(self, marka, model, number):
        self.marka = marka
        self.model = model

        if not (number.startswith("+79") and len(number) == 12 and number[1:].isdigit()):
            raise ValueError("Номер должен быть в формате '+79XXXXXXXXX' (12 символов)")
        self.number = number
    
    def __str__(self):
        return f"{self.marka} - {self.model}. {self.number}"