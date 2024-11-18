def west_indian_rest(meal):
        place_order = {
            "oxtail": 12,
            "stew": 9,
            "jerk": 8,
        }
        return  place_order.get(meal, "Please place a valid order")


def purchase_tickets(game):
    team_playing = {
        "Knicks": "Tuesday at 7pm",
        "Nets": "Wednesday at 7pm",
        "Lakers": "Friday at 7pm EST"
    }
    return team_playing.get(game, "Please make a valid selection")
