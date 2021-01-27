import time
from Earth import Earth

if __name__ == "__main__":
    e = Earth()
    while True:
        print("[/] Trying to buy land ...")
        output = e.tryPayement(str([35082115000621]))
        if "errors" in output.keys():
            print("[-] Got Error \n" + str(output))
        else:
            print("[+] Purchasing complete !")
        # Each 6 minutes
        time.sleep(360) 