import os
import subprocess
import argparse


class MemorySearchTool:
    def __init__(self):
        self.args = self.parse_arguments()

    #staticmethod
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Volatility-based Memory Search Tool")
        parser.add_argument(
            "operation", type=int,
            help="""Operation types:
                0 - Search profile information.
                1 - Search PID (list all PIDs if no keyword is provided).
                2 - Search process tree used by application.
                3 - Search network connections used by application.
                4 - Search command execution."""
        )
        parser.add_argument("profile_name", type=str, help="Profile name for vol.py -f memdumpWin7.mem")
        parser.add_argument(
            "keyword", type=str, nargs="?", default="", 
            help="Keywords for search (optional for operation 1)"
        )
        try:
            return parser.parse_args()
        except SystemExit as e:
            print("Argument parsing error: {e}. Use -h for help.")
        exit(1)


    def execute(self):
        operation = self.args.operation
        profile_name = self.args.profile_name
        keyword = self.args.keyword

        if operation == 0:
            self.search_profile(profile_name)
        elif operation == 1:
            self.search_pid(profile_name, keyword)
        elif operation == 2:
            self.search_process_tree(profile_name, keyword)
        elif operation == 3:
            self.search_network_connection(profile_name, keyword)
        elif operation == 4:
            self.search_command_execution(profile_name, keyword)
        else:
            print("Invalid operation code. Please use a valid operation code (0-4).")

    def search_profile(self, profile_name):
        """Operation 0: Search profile information."""
        print("Searching profile information for profile: {}".format(profile_name))
        cmd = ('python3 vol.py -f memdumpWin7.mem --profile={} printkey'.format(profile_name))
        self.run_command(cmd)

    def search_pid(self, profile_name, keyword):
        """Operation 1: Search PID."""
        print("Searching PIDs in profile: {}".format(profile_name))
        cmd = ("python3 vol.py -f memdumpWin7.mem --profile={} pslist".format(profile_name))
        if keyword:
            cmd += " -p {keyword}"
            self.run_command(cmd)

    def search_process_tree(self, profile_name, keyword):
        """Operation 2: Search process tree."""
        print("Searching process tree for application in profile: {}".format(profile_name))
        cmd = ("vol.py -f memdumpWin7.mem --profile={} pstree".format(profile_name))
        if keyword:
            cmd += " | grep {keyword}"
        self.run_command(cmd)

    def search_network_connection(self, profile_name, keyword):
        """Operation 3: Search network connections."""
        print("Searching network connections for application in profile: {}".format(profile_name))
        cmd = ("vol.py -f memdumpWin7.mem --profile={} netscan".format(profile_name))
        if keyword:
            cmd += " | grep {keyword}"
        self.run_command(cmd)

    def search_command_execution(self, profile_name, keyword):
        """Operation 4: Search command execution."""
        print("Searching command execution in profile: {}".format(profile_name))
        cmd = ("vol.py -f memdumpWin7.mem --profile={} cmdscan".format(profile_name))
        
        self.run_command(cmd)

    #staticmethod
    def run_command(self, cmd):
        """Run a shell command and display the output."""
        try:
            result = subprocess.Popen(cmd, shell=True)
            stdout, stderr = result.communicate()

            print("Output:\n", stdout)
            if stderr:
                print("Error:\n", stderr)

            
            '''print("Output:", result.stdout)
            print("Error Output:", result.stderr)
            if result.stderr:
                print("Error:", result.stderr)
'''
        except subprocess.CalledProcessError as e:
            print("Error executing command: {e}")
            print(e.stderr)
    

if __name__ == "__main__":
    tool = MemorySearchTool()
    tool.execute()
