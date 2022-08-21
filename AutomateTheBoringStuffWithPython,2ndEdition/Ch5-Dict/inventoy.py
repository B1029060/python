# inventory

def displayInventory(dict):
    item_cnt = 0
    print('Inventory:')
    for key, val in dict.items():
        print(val, key)
        item_cnt += val
    print(f'Total number of items: {item_cnt}')

stuff = {'rope': 1, 'touch': 6, 'gold': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)

# add item to inventory
def addToInventory(inventory, addedItems):
    for x in range(len(addedItems)):
        inventory.setdefault(addedItems[x], 0)
        inventory[addedItems[x]] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  # Kill a dragon and it's drops
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
