# 1. Integer Function: Calculates total RAM consumption
def get_total_ram(used: int, docker: int) -> int:
    total = used + docker
    return total

# 2. String Function: Formats the server status report
def get_status_report(server_name: str, total_ram: int) -> str:
    report = f"Server [{server_name}] current RAM usage is: {total_ram} GB."
    return report

# 3. Boolean Function: Checks if the server is overloaded (Threshold: 12 GB)
def is_server_overloaded(total_ram: int) -> bool:
    if total_ram >= 12:
        return True
    return False

# ==============================================================================
# RUNTIME SIMULATION ENVIRONMENT
# ==============================================================================
if __name__ == "__main__":
    srv_name = "DevOps-Prod-Server"
    used_ram = 7      # System base consumption
    docker_ram = 6    # Containers consumption (Total will be 13 GB)

    print("=" * 60)
    print("                INFRASTRUCTURE MONITORING SYSTEM                ")
    print("=" * 60)

    # Execute and capture Integer output
    total_consumption = get_total_ram(used_ram, docker_ram)
    print(f"[METRIC] Total Consumption: {total_consumption} GB\n")

    # Execute and capture String report
    server_report = get_status_report(srv_name, total_consumption)
    print(f"[REPORT] {server_report}\n")

    # Execute and evaluate Boolean risk status
    is_critical = is_server_overloaded(total_consumption)
    print(f"[ALERT] Is Server Overloaded?: {is_critical}")
    
    if is_critical:
        print("🚨 WARNING: High memory pressure detected! Scalability action required.")
    else:
        print("✅ SUCCESS: Server health status is optimal and stable.")
        
    print("=" * 60)