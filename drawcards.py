import random

# Define the number of cards in each suit
field_cards = 11
site_cards = 6
fieldnote_tool_cards = 6
method_cards = 8

# Simulate drawing one card from each suit
def draw_card(num_cards):
    """Draw a random card from a suit."""
    return random.randint(1, num_cards)

# Draw one card from each suit
field_draw = draw_card(field_cards)
site_draw = draw_card(site_cards)
fieldnote_tool_draw = draw_card(fieldnote_tool_cards)
method_draw = draw_card(method_cards)

# Print the drawn cards
print("Drawn Cards:")
print(f"FIELD: Card {field_draw}")
print(f"SITE: Card {site_draw}")
print(f"FIELDNOTE TOOL: Card {fieldnote_tool_draw}")
print(f"METHOD: Card {method_draw}")