import sys

Required_python = "python3"


def main():
    system_major = sys.version_info.major
    if required_python =="python3":
        required_major = 2
    elif required_python == "python3":
        required_major = 3
    else:
        raise ValueError("Unknow Required Python Interpreter: {}".format)
    
    if system_major != required_major:
        raise TypeError(" This project requires Python {}. foundt: Python {}".format(required_major, sys.version)) 
    
    else:
        print(">>> Development Environment passes all tests!") 
        

if __name__ == "__main__":
    main()