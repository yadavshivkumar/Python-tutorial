chai_type = "Ginger tea"
customer_name = "John Doe"  

print(f"order for {customer_name}: {chai_type} Please!")

#Strings are immutable in Python, which means that once a string is created, it cannot be changed. However, you can create new strings based on existing ones.  

chai_description = "A soothing blend of ginger and spices." 
print(f"First word: {chai_description[0:8:2]}")  # Output: "Aso"
print(f"Last word: {chai_description[8:16:2]}")  # Output: "bln"

#indexing and slicing can be used to extract specific parts of a string. The syntax for slicing is [start:stop:step], where 'start' is the index to begin the slice, 'stop' is the index to end the slice (exclusive), and 'step' is the interval between indices.  

#core is a string method that returns a copy of the string with leading and trailing whitespace removed. It does not modify the original string, as strings are immutable.  

label_text = "   Freshly brewed ginger tea   "
encoded_label = label_text.encode("utf-8")  # Encoding the string to bytes
print(f"Encoded label: {encoded_label}")  # Output: b'   Freshly brewed ginger tea   '
decoded_label = encoded_label.decode("utf-8")  # Decoding the bytes back to string
print(f"Decoded label: {decoded_label}")  # Output: "   Freshly brewed ginger tea   "
stripped_label = decoded_label.strip()  # Removing leading and trailing whitespace
print(f"Stripped label: '{stripped_label}'")  # Output: "Freshly brewed ginger tea" 


