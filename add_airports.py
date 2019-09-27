import csv
from flights.models import Airport

def main():
	f = open("add_airports.csv")
	reader = csv.reader(f)
	for code, city in reader:
		airport = Airport(code=code, city=city)
		airport.save()
		print(f"Added Airport - {airport.city} ({airport.code})")


if __name__ == "__main__":
	main()
