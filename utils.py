def generate_notice(name, relation):
    return f"Suo motu notice issued to {name} ({relation}). Partition window: 6 months."

def filter_records(df):
    return df[df['Relation'] != 'Spouse']
