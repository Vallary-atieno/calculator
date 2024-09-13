source_file='source.txt'
destination_file='destination.txt'

def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as file:
          
            content = file.read()

        with open(destination_file, 'w') as file:
         
            file.write(content)
        
        print(f"Content copied from '{source_file}' to '{destination_file}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.") 

copy_file_content(source_file, destination_file)