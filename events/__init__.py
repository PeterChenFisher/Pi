from .events import initiator
from . import schedules


def debug_code(debug):
    if debug:
        from events import events
        events.ip_addr_monitor()

        import sys
        sys.exit()
