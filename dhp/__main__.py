"""
DHP Hermes
"""

from __future__ import annotations

from dhp.kernel.boot import Boot


def main():

    boot = Boot()

    boot.discover("dhp")

    boot.start()

    boot.stop()


if __name__ == "__main__":

    main()