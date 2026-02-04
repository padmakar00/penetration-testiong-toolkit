AUTHORIZED_TARGETS = [
    "127.0.0.1",
    "localhost",
    "192.168."
]

def is_authorized(target):
    for scope in AUTHORIZED_TARGETS:
        if target.startswith(scope):
            return True
    raise PermissionError("Target is NOT authorized for testing")
