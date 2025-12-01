def positive_integer(prompt):
    is_valid = False
    value = -1 
    
    while not is_valid:
        user_input = input(prompt).strip()
        
        if user_input.isdigit():
            value = int(user_input)
            if value > 0:
                is_valid = True
            else:
                print("Input must be a positive integer.")
        else:
            print("Invalid input. Please type a whole number.")
            
    return value

def spruce_box():
    print(">Spruce Configuration<")
    
    spruce_height = positive_integer("Spruce height: ")

    max_spruce_width = 2 * spruce_height - 1
    
    is_valid_box_size = False
    required_box_size = max_spruce_width + 2
    box_size = 0 
    
    while not is_valid_box_size:
        box_size = positive_integer("Box Size: ")
        
        if box_size - 2 >= max_spruce_width:
            is_valid_box_size = True
        else:
            print(f"Invalid Box Size. The box size must be at least {required_box_size} to fit the spruce (max width {max_spruce_width}).")
            
    content_width = box_size - 2
    
    center_padding_length = (content_width - max_spruce_width) // 2
    
    print("--------------------")
    top_bottom_border = '-' * box_size
    print(top_bottom_border)

    def make_line(content):
        right_padding_length = content_width - len(content)
        right_pad = ' ' * right_padding_length
        
        return f"|{content}{right_pad}|"

    print(make_line(' ' * content_width))

    for i in range(1, spruce_height + 1):
        current_stars = 2 * i - 1
        
        branch_inner_padding = (max_spruce_width - current_stars) // 2
        
        left_pad_content = ' ' * center_padding_length + ' ' * branch_inner_padding
        branch_content = left_pad_content + '*' * current_stars
        
        print(make_line(branch_content))

    trunk_width = 1
    trunk_inner_padding = (max_spruce_width - trunk_width) // 2
    
    left_pad_content = ' ' * center_padding_length + ' ' * trunk_inner_padding
    trunk_content = left_pad_content + '*'
    
    print(make_line(trunk_content))

    print(top_bottom_border)


if __name__ == "__main__":
    spruce_box()