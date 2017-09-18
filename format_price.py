from argparse import ArgumentParser
from contextlib import suppress


def make_cmd_arguments_parser():
    parser_description = 'Script takes unformatted price and format it'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('--price', '-p',
                        help='String with unformatted price')
    return parser.parse_args()


def format_price(unformatted_price):
    with suppress(ValueError):
        return '{:,}'.format(
            int(
                float(
                    unformatted_price.replace(',', '.')
                )
            )
        ).replace(',', ' ')


if __name__ == '__main__':
    cmd_arguments = make_cmd_arguments_parser()
    unformatted_price = cmd_arguments.price
    if unformatted_price:
        print(format_price(unformatted_price))
