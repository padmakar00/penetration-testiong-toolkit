from core.engine import ExecutionEngine
from reports.report_generator import generate
from reports.risk_scoring import score

engine = ExecutionEngine()
target = "127.0.0.1"

results = {}
results["recon.port_scan"] = engine.run("recon.port_scan", target)
results["recon.service_enum"] = engine.run("recon.service_enum", target)
results["audit.password_policy"] = engine.run("audit.password_policy", target)
results["audit.tls_check"] = engine.run("audit.tls_check", target)

risk = score(results)
generate(results, risk)

print("Assessment completed. Report generated.")
