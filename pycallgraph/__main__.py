#!/usr/bin/env python
"""
pycallgraph
This script is the command line interface to the pycallgraph Python library.

See http://pycallgraph.slowchop.com/ for more information.
"""


def main():
    import pycallgraph

    config = pycallgraph.Config()
    config.parse_args()
    config.strip_argv()

    globals()['__file__'] = config.command

    file_content = open(config.command).read()

    with pycallgraph.PyCallGraph(config=config):
        exec(file_content)


if __name__ == '__main__':
    # Pep366 must always be the 1st thing to run.
    if not globals().get('__package__'):
        __package__ = "polyversion"  # noqa: A001 F841 @ReservedAssignment

    main()
