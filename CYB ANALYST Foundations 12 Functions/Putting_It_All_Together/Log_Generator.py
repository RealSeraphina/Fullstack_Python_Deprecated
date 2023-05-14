# Write a Function called log_generator that takes 5 arguments:
#     a string date in the form 'mm-dd-yyyy' (exactly 10 characters)
#     a string ip_addr in the form 'xxx.xxx.xxx.xxx' (minimum 7 characters, maximum 15 characters)
#     a string proto (either 'TCP' or 'UDP')
#     an int src_port (in the range of 0-65535)
#     an int dst_port (in the range of 0-65535)

# Your function should test for proper date length:
#     if the length of the given date is not exactly 10 charaters (dashes included), return "Error: Incorrect date format given. Date must formatted as mm-dd-yyyy"
# Your function should test for proper IP address length:
#     if the length of the given ip address is less than 7 or greater than 15, your function should return "Error: Impossible IP address length given"
# Your function should test for proper protocols:
#     if a string other than "TCP"or "UDP" is given (capitalization counts), your function should return "Error: Incorrect protocol given. Must be TCP or UDP"
# Your function should test for proper port ranges:
#     if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for src/dst_port: <src/dst_port>"
# If everything is formatted correctly, your function should create a log entry and return it in the format:
#     "<date> | <ip_addr> | <proto> | <src_port> | <dst_port>"

# # Examples:
# log_generator('01-25-2019', '23.245.36.15', 'TCP', 12001, 80)  ==> "01-25-2019 | 23.245.36.15 | TCP | 12001 | 80"
# log_generator('dec 5', '23.245.36.15', 'TCP', 12001, 80)  ==> "Error: Incorrect date format given. Date must formatted as mm-dd-yyyy"
# log_generator('01-25-2019', '23.245.36.15', 'TCP', 1000000, 80)  ==> "Error: Incorrect port number given for src_port: 1000000"

# Hint: Pseudocode breakdown
#     Define your function log_generator with the 5 given arguments date, ip_addr, proto, src_port, dst_port
#     Test the length given for date
#     Test the length given for ip_addr
#     Test the string given for proto and make sure it is either TCP or UDP
#     Test the int given for src_port and make sure it is in the range of 0 - 65535
#     Test the int given for dst_port and make sure it is in the range of 0 - 65535
#     Concatenate the log in the form "date | ip_addr | proto | src_port | dst_port"

#     Define your function log_generator with the 5 given arguments date, ip_addr, proto, src_port, dst_port
def log_generator(date, ip_addr, proto, src_port, dst_port):
#     Test the length given for date
        if len(date) != 10:
             return "Error: Incorrect date format given. Date must formatted as mm-dd-yyyy"
#     Test the length given for ip_addr
        if len(ip_addr) not in range(7,16):
            return "Error: Impossible IP address length given"
#     Test the string given for proto and make sure it is either TCP or UDP
        if proto not in ["TCP","UDP"]:
            return "Error: Incorrect protocol given. Must be TCP or UDP"
#     Test the int given for src_port and make sure it is in the range of 0 - 65535
        if src_port not in range(0,65536):
            return "Error: Incorrect port number given for src_port:" + str(src_port)
#     Test the int given for dst_port and make sure it is in the range of 0 - 65535
        if dst_port not in range(0,65536):
            return "Error: Incorrect port number given for dst_port:" + str(dst_port)
#     Concatenate the log in the form "date | ip_addr | proto | src_port | dst_port"
        return str(date) + " | " + str(ip_addr)  + " | " + str(proto)  + " | " + str(src_port)  + " | " + str(dst_port)

def main():
    print(log_generator('01-25-2019', '23.245.36.15', 'TCP', 12001, 80))
    print(log_generator('dec 5', '23.245.36.15', 'TCP', 12001, 80))
    print(log_generator('01-25-2019', '23.245.36.15', 'TCP', 1000000, 80))
    
if __name__ == "__main__":
    main()

