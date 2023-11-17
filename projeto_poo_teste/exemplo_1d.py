def get_process_ip(process_id):
    try:
        with open(f'/proc/{process_id}/net/tcp','r') as file:
            lines = file.readlines()[1:]
            ip_addresses = [line.split()[1].split(":")[0] for line in lines]
            return ip_addresses
    except FileNotFoundError:
        return f'Process with ID {process_id} not found.'

process = '7576'
ip_address = get_process_ip(process)
print(f'{process}: {ip_address}')