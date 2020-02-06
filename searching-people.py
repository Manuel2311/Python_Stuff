from people_data import main as load_people_data
from binary_search import binary_search


def main():
    people_data=load_people_data()

    age_key=lambda person: person.age_key

    age_sorted=sorted(people_data,key=age_key)
    age_result=binary_search(age_sorted,66.6,key=age_key)

    print(f"Found index: {age_result}")
    print(f"Person found: {age_sorted[age_result]}")

    def complex_key(person):
        if person.eye_colour=="blue" and person.age==66.6:
            if person.net_worth<30000:
                return -1
            elif person.net_worth>40000:
                return 1
            else:
                return 0

        else:
            return -1

if __name__ == "__main__":
    main()