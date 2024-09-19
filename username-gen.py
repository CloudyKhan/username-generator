import argparse
import re

def split_name(full_name):
    """Splits a concatenated full name into first and last names using capital letters as a delimiter."""
    split_names = re.findall('[A-Z][a-z]*', full_name)
    if len(split_names) == 2:
        return split_names[0], split_names[1]
    elif len(split_names) > 2:
        return split_names[0], "".join(split_names[1:])
    return full_name, ''  # If splitting doesn't work, return full name as first name

def username_formats(first, last='', middle='', custom_formats=None):
    if custom_formats:
        # Apply custom formats
        formats = [fmt.replace('firstname', first)
                       .replace('lastname', last)
                       .replace('f', first[0])
                       .replace('l', last[0]) 
                   for fmt in custom_formats]
    else:
        # Default formats
        formats = [
            f"{first}",                           # first
            f"{first}{last}",                     # firstlast
            f"{first}.{last}",                    # first.last
            f"{first[:8]}{last[:8]}",             # first[8]last[8]
            f"{first[:4]}{last[:4]}",             # first[4]last[4]
            f"{first}{last[0] if last else ''}",  # firstl
            f"{first[0]}.{last}" if first and last else "",  # f.last
            f"{last}{first[0] if first else ''}",  # lastf
            f"{last}",                            # last
            f"{last}.{first}",                    # last.first
            f"{last.capitalize()}{first.capitalize()}",  # Last.First
            f"{first.capitalize()}{last.capitalize()}",  # FirstLast
            f"{first.lower()}{middle.lower()}{last.lower()}",  # firstmiddlelast
            f"{first[0].upper()}{middle[0].upper() if middle else ''}{last[0].upper() if last else ''}",  # FML
        ]
    return [fmt for fmt in formats if fmt]  # Filter out any empty strings

def add_numeric_variations(username, number_patterns):
    numeric_variations = []
    for pattern in number_patterns:
        numeric_variations.append(f"{username}{pattern}")
    return numeric_variations

def generate_number_range(start, end):
    """Generate a list of numbers with padding (if needed) within the specified range."""
    return [str(i).zfill(2) for i in range(start, end + 1)]  # Ensure numbers have at least two digits

def process_file(file_path, output_file, min_length=None, custom_formats=None, domain=None, use_numbers=False, number_patterns=None, number_range=None):
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f]
            
            with open(output_file, 'w') as out_f:
                for full_name in lines:
                    first, last = split_name(full_name)
                    first = first.lower()
                    last = last.lower()

                    # Collect all usernames in a single list for each name
                    for uname in username_formats(first, last, custom_formats=custom_formats):
                        if min_length is None or len(uname) >= min_length:
                            out_f.write(uname + (domain if domain else '') + '\n')
                            
                            # Append numbers only if the user wants to add them
                            if use_numbers:
                                patterns = number_range if number_range else number_patterns
                                for num_variation in add_numeric_variations(uname, patterns):
                                    out_f.write(num_variation + (domain if domain else '') + '\n')
        print(f"Usernames successfully written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate usernames from concatenated full names using various formats. "
                    "You can specify custom formats or use the default formats. Additionally, you can "
                    "apply a minimum length filter, add domain handles (e.g., '@domainexample.com'), and add "
                    "common number patterns to usernames, or specify a range of numbers."
    )
    
    parser.add_argument('-i', '--input', type=str, required=True, help="Input file path containing concatenated names.")
    parser.add_argument('-o', '--output', type=str, required=True, help="Output file path to write the generated usernames.")
    
    parser.add_argument(
        '-m', '--min_length', 
        type=int, 
        help="Specify the minimum length of usernames to include in the output. "
             "If not provided, all usernames are included regardless of length."
    )
    
    parser.add_argument(
        '-f', '--formats', 
        type=str, 
        nargs='+', 
        help="Specify custom username formats (e.g., 'firstname.lastname', 'f.lastname', etc.). "
             "The placeholders 'firstname', 'lastname', 'f' (first letter of firstname), "
             "'l' (first letter of lastname) can be used. "
             "Examples: \n"
             "  -f 'firstname.lastname' 'f.lastname' \n"
             "  -f 'firstname_lastname' 'f_lastname' \n"
             "Ensure that the formats are enclosed in quotes. If not specified, default formats will be used."
    )

    parser.add_argument(
        '-d', '--domain', 
        type=str, 
        help="Append a domain or handle to each username (e.g., '@domainexample.com')."
    )
    
    parser.add_argument(
        '-n', '--numbers', 
        action='store_true', 
        help="Use common number patterns for usernames (e.g., '01', '001', '123')."
    )
    
    parser.add_argument(
        '-r', '--range', 
        type=int, 
        nargs=2, 
        metavar=('START', 'END'), 
        help="Specify a range of numbers to append to usernames (e.g., 1 10 for numbers '01' to '10')."
    )

    args = parser.parse_args()

    # Determine number patterns
    number_patterns = ['01', '001', '123']  # Default number patterns
    if args.range:
        number_patterns = generate_number_range(args.range[0], args.range[1])
    
    process_file(args.input, args.output, args.min_length, args.formats, args.domain, args.numbers, number_patterns)

if __name__ == "__main__":
    main()
