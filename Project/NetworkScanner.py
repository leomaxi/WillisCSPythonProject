import socket

from pandas.io.formats.format import return_docstring


#create a function that accepts
def scan_port(ip, port, timeout=1):
    try:
        #build a socket object named sock
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            # try to connect to the target IP and port
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
    # Handle all possible exceptions
    except socket.gaierror:
        print(f"Hostname {ip} could not be resolved.")
    except socket.error:
        print(f"Could not connect to the server/host {ip}.")
    except Exception as e:
        print(f"Error scanning port number {port}: {e}")
#Create a function to start the program
def main():
    print("Python Based Interactive Network Port Scanner")
    # Ask user to input target IP
    target_to_scan_ip = input("Enter the target IP address: ").strip()
    #Find out if user would like to select from a list of common ports
    user_choice = input("Do you want a list of common port to scan? Enter - Yes or No): ")
    port_list = []
    #Check user's input and assign ports accordingly
    if user_choice.lower() == "yes":
        selectedPort = input("\n ==================     ===================\n"
                             "\n Enter 1 - Port 80: HTTP (web browsing) "
                             "\n Enter 2 - Port 443: HTTPS (secure web browsing)"
                             "\n Enter 3 - Port 21: FTP (file transfer)"
                             "\n Enter 4 - Port 22: SSH (secure shell)"
                             "\n Enter 5 - Port 53: DNS (domain name system)"
                             "\n Enter 6 - Port 137-139: NetBIOS (network basic input/output system)"
                             "\n Enter 7 - Port 445: SMB (server message block)"
                             "\n Enter 8 - Port 3389: RDP (remote desktop protocol)"
                             "\n Enter 9 - Port 5900: VNC (virtual network computing)"
                             "\n Enter 10 - Port 8080: Alternative HTTP port "
                             "\n Enter One or more options separated by ").strip()
        #Check user input and map each input to a port number
        for port in selectedPort.split(","):
            try:
                match int(port):
                    case 1:
                        port_list.append(80)
                    case 2:
                        port_list.append(433)
                    case 3:
                        port_list.append(21)
                    case 4:
                        port_list.append(22)
                    case 5:
                        port_list.append(25)
                    case 6:
                        port_list.append(137)
                        port_list.append(138)
                        port_list.append(139)
                    case 7:
                        port_list.append(445)
                    case 8:
                        port_list.append(3389)
                    case 9:
                        port_list.append(5900)
                    case 10:
                        port_list.append(8080)
                    case _:
                        print("Found an invalid input")
            except Exception as e:
                print(f"Invalid input: {e}")
                break

    else:
        # Get user's ports inputs
        target_ports_input = input("Enter ports to scan- Use comma to separate you inputs, e.g. 21,22,80): ").strip()
        try:
            #break inputs into a list
            for part in target_ports_input.split(','):
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    port_list.extend(range(start, end + 1))
                else:
                    port_list.append(int(part))
        except ValueError:
            print("Invalid port format. Please use only numbers or ranges like 137-139.")
            return

    # check if a port number list is empty or not
    if not port_list:
        print("No ports selected/Entered. Exiting.")
        return
    else:
        # start scanning each port by looping though the ports and calling the scan_port function
        print(f"\nScanning {target_to_scan_ip} on ports: {port_list}\n")
        for port in port_list:
            scan_port(target_to_scan_ip, port)

if __name__ == "__main__":
    main()
