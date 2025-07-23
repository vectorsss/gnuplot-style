"""Convenience API functions for gnuplot style."""

from .core import use


def colors() -> None:
    """Apply just gnuplot colors."""
    use("color")


def lines() -> None:
    """Apply just gnuplot line styles."""
    use("line")


def markers() -> None:
    """Apply just gnuplot markers."""
    use("marker")


def colors_lines(cycle_mode: str = "default") -> None:
    """Apply gnuplot colors and line styles.

    Parameters
    ----------
    cycle_mode : str, optional
        'default' for 8 combinations, 'extended' for 72 combinations
    """
    use("color+line", cycle_mode=cycle_mode)


def colors_markers(cycle_mode: str = "default") -> None:
    """Apply gnuplot colors and markers.

    Parameters
    ----------
    cycle_mode : str, optional
        'default' for 8 combinations, 'extended' for 128 combinations
    """
    use("color+marker", cycle_mode=cycle_mode)


def all(cycle_mode: str = "default") -> None:
    """Apply all gnuplot styles: colors, lines, and markers.

    Parameters
    ----------
    cycle_mode : str, optional
        'default' for 16 combinations, 'extended' for 16 combinations (same)
    """
    use("all", cycle_mode=cycle_mode)
