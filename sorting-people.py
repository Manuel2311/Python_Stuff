from people_data import main as load_people_data
from pprint import pprint

def main():
    people_data=load_people_data()

    chosen_people=people_data[:40]

    default_sort=sorted(chosen_people)

    reversed_default=sorted(chosen_people,reverse=True)

    def networth_fc(person):
        return person.net_worth

    
    age_fc=lambda person: person.age

    networth_sort=sorted(chosen_people, key=networth_fc)

    pprint(networth_sort)

    
    def age_fc(person):
        return person.age

    age_sort=sorted(chosen_people, key=age_fc)

    #pprint(age_sort)

    def worth_age_fc(person):
        return person.age*1000+person.net_worth

    complex_sort=sorted(chosen_people,key=worth_age_fc)

if __name__ == "__main__":
    main()