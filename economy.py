"""Basic economic interactions for the village simulator."""

def pay_salary(character, building, amount=1):
    """Pay a salary from a building to a character."""
    character.money += amount
    building.money -= amount


def buy_good(buyer, seller, item, price=1):
    """Transfer one unit of *item* from seller to buyer for a price."""
    if seller.inventory.get(item, 0) <= 0 or buyer.money < price:
        return False
    seller.inventory[item] -= 1
    buyer.inventory[item] = buyer.inventory.get(item, 0) + 1
    buyer.money -= price
    seller.money += price
    return True
