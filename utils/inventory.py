def get_item_from_inventroy(inventory, item_name):
    try:
        return inventory[item_name]
    except KeyError:
        print(f"Položka '{item_name}' nebyla nalezena v inventáři.")
        return None
