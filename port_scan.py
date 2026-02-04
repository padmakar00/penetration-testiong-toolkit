import nmap

def execute(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments="-T4 -F")

    results = {}
    for host in scanner.all_hosts():
        results[host] = []
        for proto in scanner[host].all_protocols():
            for port in scanner[host][proto]:
                if scanner[host][proto][port]["state"] == "open":
                    results[host].append(port)
    return results
