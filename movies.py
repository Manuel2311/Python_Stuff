from statistics import mean

def reader(filename):
    file= open(filename,"r", encoding="utf-8")
    while True:
        yield file.readline()

#################################
#                               #
#    GENERATORS PROVIDE DATA    #
#      ONE ITEM AT A TIME       #
#                               #
#################################



def main():
    generator=reader("data.tsv")
    genres={}

    next(generator)

    while True:
        value=next(generator)

        if value=="":
            break
        id,title_type,primary_title,secondary_title,a,start_year,end_year,runtime,genre_string=value.strip("\n").split("\t")

        for genre in genre_string.split(","):
            if genre in  genres.keys():
                genres[genre]+=1
            else:
                genres[genre]=1

    with open("imdb-data-outout.txt", "w") as file:
        file.write("\n".join(map(str,genres.items())))     
    print(len(genres))
    print(genres)

main()