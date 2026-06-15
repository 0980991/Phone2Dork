import re


def generatePhoneVariants(phone_number, country_code="31"):
    raw = re.sub(r"[^\d+]", "", phone_number)
    digits = raw.replace("+", "")

    if digits.startswith(country_code):
        national = "0" + digits[len(country_code):]
    elif digits.startswith("0"):
        national = digits
        digits = country_code + digits[1:]
    else:
        national = "0" + digits

    if national.startswith("06") and len(national) >= 10:
        part1 = national[:2]
        part2 = national[2:6]
        part3 = national[6:]
    else:
        part1 = national[:3]
        part2 = national[3:6]
        part3 = national[6:]

    formats = set()

    # International
    formats.add(f"+{digits}")
    formats.add(f"+{country_code} {digits[len(country_code):]}")
    formats.add(f"+{country_code} {part1[1:]} {part2}{part3}")
    formats.add(f"+{country_code} {part1[1:]} {part2} {part3}")

    # National
    formats.add(national)
    formats.add(f"{part1} {part2}{part3}")
    formats.add(f"{part1} {part2} {part3}")
    formats.add(f"{part1}-{part2}-{part3}")
    formats.add(f"{part1}.{part2}.{part3}")

    return sorted(formats)


def buildQueries(variants):
    quoted = [f'"{v}"' for v in variants]

    return {
        "google": " OR ".join(quoted),
        "bing": " OR ".join(quoted),
        "yandex": " | ".join(quoted),
    }