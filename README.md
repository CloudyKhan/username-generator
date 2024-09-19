# username-gen
This Python script is designed to generate usernames from concatenated full names using a variety of predefined formats. It can also apply custom username formats, append domain handles, and add common number patterns (like those often used in Windows environments). Simple alternative to username-anarchy

### Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Options](#command-line-options)
  - [Examples](#examples)
- [Customization](#customization)
  - [Common Number Patterns](#common-number-patterns)
  - [Username Formats](#username-formats)

---

## Features

- **Automatic Username Generation**: Generates usernames from full names using various common formats.
- **Custom Formats**: Users can specify custom formats for generating usernames (e.g., `firstname.lastname`, `f.lastname`).
- **Domain Appending**: Supports appending domain handles (e.g., `@example.local`).
- **Common Number Patterns**: Can append common number patterns (e.g., `01`, `001`, `123`) to usernames.
- **Custom Number Ranges**: Allows the user to define a range of numbers to append to usernames.
- **Minimum Length Filtering**: Filters usernames by a minimum length specified by the user.

---

## Installation

1. **Clone the Repository**:
    ```
    git clone https://github.com/CloudyKhan/username-generator.git
    ```

2. **Navigate to the Directory**:
    ```
    cd username-generator
    ```

3. **Ensure Python 3.x is Installed**:
    Verify Python 3 is installed by running:
    ```
    python3 --version
    ```
    If Python is not installed, follow the [official Python installation guide](https://www.python.org/downloads/).

---

## Usage

### Command-Line Options

Use the following command-line arguments to control the behavior of `username-gen.py`:

```
usage: python3 username-gen.py [-h] [-i INPUT] [-o OUTPUT] [-m MIN_LENGTH] [-f FORMATS] [-d DOMAIN] [-n] [-r RANGE]
```

| Option            | Description                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------|
| `-i INPUT`        | Specify the input file path containing concatenated names (required).                        |
| `-o OUTPUT`       | Specify the output file path where generated usernames will be saved (required).             |
| `-m MIN_LENGTH`   | Set the minimum username length (optional).                                                  |
| `-f FORMATS`      | Specify custom formats for username generation (optional).                                   |
| `-d DOMAIN`       | Append a domain or handle to each username (e.g., `@example.com`) (optional).                  |
| `-n, --numbers`   | Append common number patterns (`01`, `001`, `123`) to usernames (optional).                  |
| `-r RANGE`        | Specify a range of numbers to append to usernames (e.g., `-r 1 10` for numbers `01` to `10`).|

---

### Examples

#### Example 1: Basic Username Generation
Generate usernames from an input file without any customization:
```
python3 username-gen.py -i input.txt -o usernames_output.txt
```

#### Example 2: Custom Username Formats
Specify custom formats like `firstname.lastname` and `f.lastname`:
```
python3 username-gen.py -i input.txt -o usernames_output.txt -f 'firstname.lastname' 'f.lastname'
```

#### Example 3: Append Domain
Append a domain like `@example.com` to the generated usernames:
```
python3 username-gen.py -i input.txt -o usernames_output.txt -d '@example.com'
```

#### Example 4: Add Common Number Patterns
Append common number patterns (`01`, `001`, `123`) to each username:
```
python3 username-gen.py -i input.txt -o usernames_output.txt -n
```

#### Example 5: Use a Range of Numbers
Specify a custom range of numbers to append to usernames:
```
python3 username-gen.py -i input.txt -o usernames_output.txt -r 1 10
```

#### Example 6: Filter by Minimum Length
Only include usernames that are at least 8 characters long:
```
python3 username-gen.py -i input.txt -o usernames_output.txt -m 8
```

---

## Customization

### Common Number Patterns

If the `-n` flag is used, common number patterns (`01`, `001`, `123`) will be appended to each generated username. For example, with the name `john.smith`:
```
john.smith
john.smith01
john.smith001
john.smith123
```

### Username Formats

By default, the script generates usernames using the following formats:
- `first`
- `firstlast`
- `first.last`
- `first[8]last[8]`
- `f.lastname`
- `last.first`
- `FirstLast`
- `FML` (initials)
- And more...

You can also define custom formats using placeholders like `firstname`, `lastname`, `f` (first letter of the first name), and `l` (first letter of the last name). For example:
```
-f 'firstname.lastname' 'f.lastname'
```
Ensure that the file containing the names you plan to use is formatted with first and last names on the same line like so:
```
JohnDoe
FredSmith
JaneAdams
```

