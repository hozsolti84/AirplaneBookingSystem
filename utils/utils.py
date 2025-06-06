from configparser import ConfigParser
from exceptions.exceptions import SectionNotFound, KeyNotFoundInConfig, ValueNotFoundInConfig


def get_data(section, key, path="../config.ini"):
    conf = ConfigParser()
    try:
        conf.read(path)
    except FileNotFoundError as FNF:
        raise FNF
    if not conf.has_section(section):
        raise SectionNotFound(f"The section '{section}' was not found in the config.ini!")
    if not conf.has_option(section, key):
        raise KeyNotFoundInConfig(f"The key '{key}'was not found in the config.ini!")
    if conf.get(section, key) is None:
        raise ValueNotFoundInConfig(f"The value for '{section}.{key}' was not found in the config.ini!")
    return conf.get(section, key)

