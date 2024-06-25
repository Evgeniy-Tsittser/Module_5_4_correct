class Building:

    total = 0

    def __str__(self):
        return f'Экземпляр класса Building № {self.total}'


for i in range(40):
    building = Building()
    Building.total += 1
    print(building)


