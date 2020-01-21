import os

class GenerateSmali():
    def __init__(self):
        super().__init__()
        self.java2class_command = "javac res/Test.java"
        self.class2dex_command = "tools/d2j-jar2dex.sh res/Test.class -o res/Test.dex --force"
        self.dex2smali_command = "tools/d2j-dex2smali.sh res/Test.dex -o res/output --force"

    def generate_smali_code(self):
        self.exec_system_command(self.java2class_command)
        self.exec_system_command(self.class2dex_command)
        self.exec_system_command(self.dex2smali_command)

    def exec_system_command(self, command):
        os.system(command)

