import math
import os
from phoneSplitter.helper import popup_message


def transfer(in_str, save_path, num_per_file, save_filename):
    """
    Main function to grab input, split them, and then save to txt files.
    :param in_str: the mobile column copied from excel sheet directly
    :param save_path: the directory to save outputs
    :param num_per_file:  number of phone# per file, default 170
    :param save_filename:  the prefix filenames to save, default = NANA -> NANA_1.txt
    :return: None
    """
    # null point checkers
    if not save_path:
        popup_message("Please specify a saving path.")
        return

    if not num_per_file:
        popup_message("Please specify how many phone# per file.")
        return

    if not save_filename:
        popup_message("Please specify filename prefix for saving.")
        return

    if in_str == "\n":
        popup_message("No data added in the entry textbox.")
        return

    # process input parameters
    num_per_file = int(num_per_file)
    in_str = in_str.split("\n")
    in_str = ["".join(filter(str.isdigit, _)) for _ in in_str]

    #  check special cases
    output = []
    while in_str:
        phone = in_str.pop() # shall pop 0 instead
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

    popup_message(f"Successfully saved to {num_groups} files.")
    return
