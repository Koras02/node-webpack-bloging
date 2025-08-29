import os 

# 원하는 순서로 
order = {
    "node-webpack-bloging": ["src", "dist", "package.json", "webpack.config.js"],
    "src": ["index.js", "server.js"],
    "dist": [],
}

def print_tree(path, prefix=""):
   folder_name = os.path.basename(path) or path 
   all_entries = os.listdir(path)
   
   # order에 있는 순서대로, 없으면 뒤로 배치
   ordered_entries = order.get(folder_name, [])
   remaining = [e for e in all_entries if e not in ordered_entries]
   entries = ordered_entries + sorted(remaining)
   
   
   for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "└─" if i == len(entries) - 1 else "├─"
        
        if os.path.isdir(full_path):
              print(f"{prefix}{connector} {entry}/")
              # 하위 폴더는 prefix를 늘려 재귀 호출
              extension = "    " if i == len(entries) - 1 else "|   "
              print_tree(full_path, prefix + extension)
        else:
              print(f"{prefix}{connector} {entry}")
              


# 시작 디렉토리
start_dir = "../node-webpack-bloging"
print(f"{os.path.basename(start_dir)}/")
print_tree(start_dir)