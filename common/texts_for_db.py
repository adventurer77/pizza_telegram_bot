from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Food', 'Drinks']

description_for_info_pages = {
    "main": "Welcome!",
    "about": "Italian Dream Pizzeria.\nWorking hours - 9-18.",
    "payment": as_marked_section(
        Bold("Payment options:"),
        "By card in the bot",
        "Upon receipt of the card/cash",
        "At the establishment",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Delivery/Order Options:"),
            "Courier",
            "Self-pickup",
            "Eat at the establishment",
            marker="✅ ",
        ),
        as_marked_section(Bold("Delivery impossible:"), "Post",  marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Category:',
    'cart': 'Cart is empty!'
}
