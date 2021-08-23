import codecs
import os
import shutil
import time

from colorama import Fore, init
import fire
from tqdm import tqdm
import yaml



class Birk:
    """CLI tool for backup files and folders."""
    def __init__(self):
        init(autoreset=True)
        self.src, self.dst = load()

    def run(self, path=None):
        if path is None:
            path = self.dst

        # Check for existence of save destination.
        if not os.path.isdir(path):
            return Fore.RED + "Save destination directory does not exist."

        for i in tqdm(self.src, ncols=60):
            if os.path.isdir(i):
                shutil.copytree(i, f"{path}/{os.path.basename(i)}",
                                dirs_exist_ok=True)
                tqdm.write(Fore.GREEN + f"'{i}' copied!")
            elif os.path.isfile(i):
                shutil.copy2(i, path)
                tqdm.write(Fore.GREEN + f"'{i}' copied!")
            else:
                tqdm.write(Fore.RED + f"'{i}' does not exist")

    def add(self, path):
        if path in self.src:
            return Fore.RED + "Path is duplicated and cannot be added."
        else:
            self.src.append(path)
            dump(self.src, self.dst)
            print(Fore.GREEN + "Added!")
            for i in range(len(self.src)-1):
                print(f"   - {self.src[i]}")
            return Fore.GREEN + f"   - {self.src[-1]}"

    def set(self, path):
        dump(self.src, path)
        return Fore.GREEN + f"Current save destination is '{path}'."

    def remove(self):
        # Exit if there are no items in source list.
        if not self.src:
            return Fore.RED + "Exit because there are no items in source list."

        print("Select number to be deleted from source list.")
        for i in range(len(self.src)):
            print(f"   {i}: {self.src[i]}")
        try:
            self.src.remove(x := self.src[int(input("\nEnter number: "))])
            dump(self.src, self.dst)
            return Fore.GREEN + f"'{x}' removed!"
        except KeyboardInterrupt:
            return
        except ValueError:
            return Fore.RED + "Please enter number!"
        except IndexError:
            return Fore.RED + "Select in range of source list!"

    def list(self):
        print("Source list:")
        for i in self.src:
            print(f"   - {i}")
        print("\nSave destination:")
        return f"   - {self.dst}"

    def destroy(self):
        if input("Destroy path list? [y/N]: ").lower() in ["y", "ye", "yes"]:
            if os.path.isfile("paths.yml"):
                os.remove("paths.yml")
                return "Destroyed"
        return



def load():
    # If there is no `paths.yml`, create an empty yaml file.
    if not os.path.isfile("paths.yml"):
        dump([], "")

    with open("paths.yml", "r", encoding="utf_8") as f:
        paths = yaml.safe_load(f)
    return [i["path"] for i in paths[0]["src"]], paths[1]["dst"][0]["path"]


def dump(src, dst):
    paths = [{"src": [dict(path=i) for i in src]}, {"dst": [dict(path=dst)]}]
    with codecs.open("paths.yml", "w", "utf_8") as f:
        yaml.dump(paths, f, encoding="utf_8", allow_unicode=True)


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    fire.Fire(Birk)
