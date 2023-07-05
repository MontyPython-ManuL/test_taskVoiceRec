import argparse


def get_input_path_from_cli():
    """
    Parses command-line arguments.

    Returns:
    tuple: A tuple containing the following elements:
            - file (str): The input file path for reading.
            - order (str): The sort order ('--asc' or '--desc').
            - driver (str): The driver's name.
    """
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--path', type=str, help='Input file path for read')

    data = parser.parse_args()

    return data.path
