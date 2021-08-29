
from open_file import openFile
from myclasses import StrangeTeleprompter


def main():
    filepath = openFile()
    teleprompter = StrangeTeleprompter(filepath.filepath)
    teleprompter.main()

if __name__ == "__main__":
    main()
