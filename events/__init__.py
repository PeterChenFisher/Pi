from .events import starting_up
from . import schedules


def debug_code(debug):
    if debug:
        from events import events
        events.send_ip_address_to_dding()

        import sys
        sys.exit()
