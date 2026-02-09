default cash =50
default inventory =[]
default items =["Rice", "Toy"]
default itemprice ={"Rice": 15, "Toy": 20}

label start:
    "Hello, you can buy things or sell your inventory"
    "It's just a shopping system test"

    call screen store

    "Now you have [len(inventory)] things in your inventory and $[cash] cash"
    return

screen store():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Your cash:[cash]$"
            hbox:
                spacing 120
                vbox:
                    for item in items:
                        textbutton "[item] [itemprice[item]]$":
                            action Function(buy, item)
                            sensitive cash >= itemprice[item]
                vbox:
                    text "Inventory:"
                    if not inventory:
                        text "Empty"
                    for item in inventory:
                        textbutton "[item]":
                            action Function(sell, item)
            textbutton "Close store" action Return()


init python:
    def buy(item):
        global cash
        price = itemprice[item]
        if cash >= price:
            cash -= price
            inventory.append(item)
        renpy.restart_interaction()

    def sell(item):
        global cash
        price = itemprice[item]
        cash += price
        inventory.remove(item)
        renpy.restart_interaction()
