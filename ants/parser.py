def parse_entry(raw_line, sep=None):
    values = raw_line.split(sep)
    _, _, ascii_name, _, _, _, feature_class, feature_code, country_code, _, \
    _, _, _, _, population, _, _, _, _ = values
    population = int(population, 10)

    return ascii_name, feature_class, feature_code, country_code, population


def parse(file_name, validator):
    result = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            values = parse_entry(line, '\t')
            is_valid = validator(*values)

            if is_valid:
                result.append(values[0])

    return sorted(set(result))


def save_to_file(file_name, iterable):
    with open(file_name, 'w', encoding='utf-8') as file:
        lines = '\n'.join(iterable)
        file.writelines(lines)


def filter_ukraine_cities(name, feature_class, feature_code, country_code, population):
    return population >= 20000 and feature_class in ('P',) and country_code in ('UA',)


if __name__ == '__main__':
    db_file = './../dumps/cities5000.txt'
    out_file = './../data/ua_cities.txt'

    cities = parse(db_file, filter_ukraine_cities)
    save_to_file(out_file, cities)

    template = 'Parsed from: {}\nSaved to: {}\nLoaded cities: {}'
    info_msg = template.format(db_file, out_file, len(cities))
    
    print(info_msg)
