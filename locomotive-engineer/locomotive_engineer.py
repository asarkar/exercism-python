"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_ids) -> list[int]:
    """Return a list of wagons.

    :param: wagon_ids - arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_ids)


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    x, y, locomotive_id, *rest = each_wagons_id
    return [locomotive_id, *missing_wagons, *rest, x, y]


def add_missing_stops(route: dict[str, str | list[str]], **stops) -> dict[str, str | list[str]]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route['stops'] = list(stops.values())
    return route


def extend_route_information(route: dict[str, str], more_route_information: dict[str, str]) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(x) for x in zip(*wagons_rows)]
