from os import listdir, linesep
from os.path import isfile, join


def make_files_list(path):
    fileslist = [f for f in listdir(path) if isfile(join(path, f))]
    files = []
    for f in fileslist:
        ext_pos = f.rfind(".")
        ext = f[ext_pos:]
        if(ext == ".md"):
            idx = f.find("_")
            try:
                row = (int(f[:idx]), f[idx+1: ext_pos].replace("_"," "), f)
                files.append(row)
            except:
                pass
    files.sort()
    return files
         
         
def render_to_md(rows, output_file="Readme.md"):
    f = open(output_file, "w")
    f.write("# C++ Solutions to leetcode problems\n")
    f.write(f"{len(rows)} [leetcode problems](https://leetcode.com/problemset/all/) solutions:\n")
    f.write("Number | Problem " + "\n")
    f.write("--- | --- " + "\n")
    for num, title, file in rows:
        f.write(f"{num} | [{title}]({file})" + "\n")
    f.close()
    
    
if __name__ == "__main__":
    render_to_md(make_files_list("."))
    
