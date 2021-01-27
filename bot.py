import time
from Earth import Earth

if __name__ == "__main__":
    e = Earth()
    user_infos = e.get_user_infos()
    print(f"[!] Logged in as\nusername: {user_infos['username']}\nbalance: {user_infos['balance']}\nnetworth: {user_infos['networth']}\ntotalTiles: {user_infos['totalTiles']}\nspent: {user_infos['spent']}\n===========\n\n")
    
    while True:
        print("[/] Trying to buy land ...")
        output = e.tryPayement(str([152049601403821, 42098438626221]))
        if "errors" in output.keys():
            print("[-] Got Error \n" + str(output))
        else:
            print(output)
            print("[+] Purchasing complete !")
        # Each 2 minutes
        time.sleep(120)