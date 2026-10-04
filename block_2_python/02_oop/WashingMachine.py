import datetime


class WashingMachine:
    """Класс, представляющиий стиралку
    
    Args:
        brand (str): Бренд.
        model (str): Название модели.
        purchase_date (datetime.date): Дата покупки.
        warranty_length (int): Количество дней гарантии.
    """
    def __init__(self, brand, model, purchase_date, warranty_length):
        self.brand = brand
        self.model = model
        self.purchase_date = purchase_date
        self.warranty_length = warranty_length

    def remaining_warranty_time(self):
        """Выводит инфорамцию об оставшемся сроке гарантии.
        
        Returns:
            Информацию о сроке действия гарантии.
        """
        today = datetime.date.today()
        warranty_end_date = self.purchase_date + datetime.timedelta(
            days=self.warranty_length
        )
        remaining_time = warranty_end_date - today
        if remaining_time.days < 0:
            return "Срок действия гарантии истек."
        else:
            return "Срок действия гарантии истекает через {} дней. ".format(
                remaining_time.days
            )


my_washing_mashine = WashingMachine("LG", "FH$U@VCN2", datetime.date(2024, 5, 7), 1550)

print(my_washing_mashine.remaining_warranty_time())
