def read_and_write_file():
    """
    Reads a file from user input, converts its content to uppercase,
    and writes it to a new file named 'modified_output.txt'.
    Handles errors if file doesn't exist or can't be read.
    """
    # Ask user for filename
    filename = input("Enter the filename to read: ").strip()

    try:
        # Open and read the original file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read '{filename}'")
            print(f"Original content:\n{content}")

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_filename = "modified_output.txt"
        with open(output_filename, 'w') as out_file:
            out_file.write(modified_content)
        print(f"\nModified content written to '{output_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found. Please check the filename.")
    except PermissionError:
        print(f"❌ Error: No permission to read '{filename}'. Check file access.")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")


# Run the function
if __name__ == "__main__":
    read_and_write_file()
