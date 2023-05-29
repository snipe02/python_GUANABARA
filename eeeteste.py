class Passenger:
    def __init__(self, passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked):
        self.passenger_id = passenger_id
        self.survived = survived
        self.pclass = pclass
        self.name = name
        self.sex = sex
        self.age = age
        self.sibsp = sibsp
        self.parch = parch
        self.ticket = ticket
        self.fare = fare
        self.cabin = cabin
        self.embarked = embarked


class TitanicData:
    def __init__(self):
        self.passengers = []

    def read_data(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)  # pula a linha de cabeçalho
            for row in reader:
                passenger = Passenger(int(row[0]), bool(int(row[1])), int(row[2]), row[3], row[4], float(row[5]),
                                      int(row[6]), int(row[7]), row[8], float(row[9]), row[10], row[11])
                self.passengers.append(passenger)

    def count_survivors(self):
        return sum(1 for passenger in self.passengers if passenger.survived)

    def average_age(self):
        total_age = sum(passenger.age for passenger in self.passengers if passenger.age)
        num_passengers_with_age = sum(1 for passenger in self.passengers if passenger.age)
        return total_age / num_passengers_with_age if num_passengers_with_age > 0 else None