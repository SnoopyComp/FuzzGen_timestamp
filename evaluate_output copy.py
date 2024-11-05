#!/usr/bin/env python3.11

import os
import re
import sys


def main():
    project_name = sys.argv[1]
    folder_name = sys.argv[2]

    project_path = os.path.join("./results", project_name)
    folder_path = os.path.join(project_path, folder_name)
    print(project_path)
    print(folder_path)

    # signature_list 경로 설정
    signature_list = os.listdir(folder_path)
    for s in signature_list:
        log_dir = os.path.join(folder_path, s, "logs", "run")
        if not os.path.isdir(os.path.join(folder_path,s)):
            continue
        for i in range(1, 3):
            result_path = os.path.join(folder_path,s, f"0{i}_result.txt")
            with open(result_path, 'w') as fw:

                for j in range(6, 0, -1):
                    log_file_name = f"0{i}.cc-F{j}.log"
                    log_file_path = os.path.join(log_dir, log_file_name)
                    if not os.path.isfile(log_file_path):
                        continue

                    total_rate_sum = 0.0
                    timestamp_count = 0

                    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as fs:
                        lines = fs.readlines()
                        for line in lines:
                            if "Target runtime" in line and "Function runtime" in line:
                                timestamp_count += 1
                                numbers = re.findall(r'\d+', line)

                                target_runtime = int(numbers[0])
                                function_runtime = int(numbers[1])
                                if target_runtime == 0:
                                    continue
                                time_rate = function_runtime / target_runtime
                                total_rate_sum += time_rate

                    if timestamp_count != 0:
                        avg_rate = total_rate_sum / timestamp_count
                        fw.write(f"{avg_rate}\n")
                        print(avg_rate)
                    break


if __name__ == '__main__':
    main()
