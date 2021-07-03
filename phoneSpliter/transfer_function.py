import math
import os


def transfer(in_str, save_path, num_per_file, save_filename="NANA"):
    print(f"num_per_file = {num_per_file}")
    print(f"save filename = {save_filename}")
    if save_path == "":
        print("Please specify a saving path.")
        return

    num_per_file = int(num_per_file)
    in_str = in_str.split("\n")
    in_str = ["".join(filter(str.isdigit, _)) for _ in in_str]

    #  check special cases
    output = []
    while in_str:
        phone = in_str.pop()
        if len(phone) == 11 and phone[0] == "1":
            output.append(phone[1:])
        elif len(phone) == 10:
            output.append(phone)

    #  save to file
    num_groups = math.ceil(len(output) / num_per_file)
    print(f"We will have {num_groups} groups!")
    for i in range(num_groups):
        tmp_list = output[i * num_per_file: (i + 1) * num_per_file]
        print(tmp_list)
        with open(os.path.join(save_path, f"{save_filename}_{i + 1}.txt"), "w") as text_file:
            text_file.write(",\n".join(tmp_list))
            print(f"Saved {len(tmp_list)} numbers to {save_filename}_{i + 1}.txt")

    print("SUCCESS.")
    return
