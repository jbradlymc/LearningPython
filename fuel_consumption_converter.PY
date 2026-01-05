def liters_100km_to_miles_gallon(liters):
    liters_km = liters / 100
    gal_km = liters_km / 3.785411784
    gal_m = gal_km / 1000
    gal_mile = gal_m * 1609.344
    mpg = 1 / gal_mile
    return mpg


def miles_gallon_to_liters_100km(miles):
    m_gal = miles * 1609.344
    m_li = m_gal / 3.785411784
    km_li = m_li / 1000
    hundredkm_li = km_li / 100
    li_km = 1 / hundredkm_li
    return li_km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
