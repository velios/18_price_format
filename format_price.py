from argparse import ArgumentParser
from contextlib import suppress


def fetch_cmd_arguments():
    parser_description = 'Script takes unformatted price and format it'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('--price', '-p',
                        help='String with unformatted price')
    return parser.parse_args()


def format_price(unformatted_price):
    with suppress(ValueError):
        return '{:,.2f}'.format(
                float(
                    unformatted_price.replace(',', '.')
            )
        ).replace(',', ' ')


if __name__ == '__main__':
    cmd_arguments = fetch_cmd_arguments()
    unformatted_price = cmd_arguments.price
    if unformatted_price:
        print(format_price(unformatted_price))
