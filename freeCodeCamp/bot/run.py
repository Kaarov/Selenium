from booking.booking import Booking


with Booking("../../chromedriver") as bot:
    bot.land_first_page()
    try:
        bot.close_sign_in_info()
    except:
        print("Skipping ...")
    # bot.change_currency("EUR")
    bot.select_place_to_go("New York")
    bot.select_dates("2024-07-31", "2024-08-06")
    bot.select_adults(5)
    bot.click_search()
    bot.apply_filtration()
