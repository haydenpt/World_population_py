from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None


# country_code_updated = {}
# for code, country in COUNTRIES.items():
#     country_code_updated[code] = country
#
# for code, country in country_code_updated.items():
