from booking.booking import Booking


try:
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
except Exception as e:
    if 'in PATH' in str(e):
        print('There is a problem running this program from command line interface')
    else:
        raise
