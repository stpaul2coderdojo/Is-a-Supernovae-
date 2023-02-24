def isSupernovae(star_mass, star_metallicity, star_age):
    if star_mass < 8:
        return 0  # Stars less than 8 solar masses do not typically undergo supernovae
    elif star_metallicity < 0.1:
        return 0.25  # Low metallicity stars have a higher likelihood of undergoing supernovae
    elif star_age < 3e7 or star_age > 1e9:
        return 0.5  # Young or old stars have a higher likelihood of undergoing supernovae
    else:
        return 0.1  # For all other stars, we assume a low probability of undergoing a supernova
