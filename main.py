import sqlite3

connection = sqlite3.connect("gta.db")
cuser = connection.cursor()

cuser.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]    

cuser.executemany("insert into gta values (?,?,?)", release_list)

for row in cuser.execute("select * from gta"):
    print(row)

print("*******************************************************")

cuser.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cuser.fetchall()
print(gta_search)

cuser.execute("create table cities (gta_city text, real_city text)")
cuser.execute("insert into cities value (?,?)", ("Liberty City", "New York"))
cuser.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cuser.fetchall()
print(cities_search)

connection.close()
