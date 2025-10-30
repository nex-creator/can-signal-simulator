import cantools

def load_dbc(path):
    db = cantools.database.load_file(path)
    print(f"Loaded DBC: {path}\n")

    for msg in db.messages:
        print(f"Messages: {msg.name} (ID : {msg.frame_id})")
        for sig in msg.signals:
            print(f"signal:{sig.name}, Start: {sig.start},Lenght: {sig.length}, Scale: {sig.scale}, Offset: {sig.offset}")
    return db

load_dbc("./dbc/extended_vehicle.dbc")
      