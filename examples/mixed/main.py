from easy_id import *

config = {
    "nanoid": {
        "alphabet": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz",
        "length": 21,
    },
    "snowflake": {
        "epoch": 0,
        "machine_id": 0,
    },
    "ulid": {
        "epoch": 0,
    }

}

if __name__ == '__main__':
    nano_gen = IDGenerator(EasyIdType.NANOID, config["nanoid"])
    print(nano_gen.generate())

    snow_gen = IDGenerator(EasyIdType.SNOWFLAKE, config["snowflake"])
    print(snow_gen.generate())

    ulid_gen = IDGenerator(EasyIdType.ULID, config["ulid"])
    print(ulid_gen.generate())


