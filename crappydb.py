
# file format:
# <student id>,<first name>,<last name>

DB_FILENAME = "crappydb.csv"

# read student info (querying the db)
def read_file():
    with open(DB_FILENAME) as f:
        for line in f:
            print(line)

# inserting records
def insert_data():
    records = [
        ['W555666', 'bob', 'cratchet'],
        ['W666777', 'tiny tim', 'cratchet'],
        ['W777888', 'ebenezer', 'scrooge']
    ]

    with open('crappydb.csv', 'a') as f:
        for r in records:
            f.write(','.join(r))
            f.write('\n')

def delete_record(id):
    # read contents
    db = []
    with open('crappydb.csv', 'r') as f:
        for line in f:
            sid, first, last = line.split(",")
            if sid != id:
                db.append(line)

    # write contents
    with open('crappydb.csv', 'w') as f:
        for r in db:
            f.write(r)

def main():
    read_file()
    insert_data()
    delete_record('W777888')

if __name__ == "__main__":
    main()