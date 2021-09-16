from tinydb import TinyDB, Query
db=TinyDB('db.json', indent=4)
tournament=db.table('tournament')
query=Query()

# reload_tournament=tournament.search(query.name=='Pegasus')
# print(reload_tournament[0])
# print (tournament.all())
all_tournament=tournament.all()
for tournament in all_tournament:
    if len(tournament['rounds'])!=4:
        print (tournament.doc_id, tournament['name'])


