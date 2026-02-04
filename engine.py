import importlib
from core.auth import is_authorized
from core.logger import log

class ExecutionEngine:
    def run(self, module_path, target):
        is_authorized(target)
        log(f"Executing module {module_path} on {target}")

        module = importlib.import_module(f"modules.{module_path}")
        result = module.execute(target)

        log(f"Completed module {module_path}")
        return result
