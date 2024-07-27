from booking.booking import Booking


with Booking("../../chromedriver") as bot:
    bot.land_first_page()
