from PIL import Image

#Function to encode the message into image

def encode_image (image_filename, message):
    #First we Open image and convert to RGB format
    
    img = Image.open (image_filename).convert('RGB')
    width, height = img.size #get width and height of image
    
    # Now Convert message to binary string
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Constrain: Check if message is too long to encode in the image
    max_message_size = width * height * 3 // 8
    if len(binary_message) > max_message_size:
        raise ValueError('Message too long to encode in the image')

    # Adding delimiter to end of message to identify end of message
    binary_message += '00000000'

    pixel_index = 0
    for char in binary_message:
        x = pixel_index % width  #x index
        y = pixel_index // width #y index
        r, g, b = img.getpixel((x, y)) 
        if char == '0':
            # Set least signifilant bit to O
            r &= 0b11111110
        else:
            #set least significant bit to 1
            r |= 0b00000001
        img.putpixel((x,y), (r, g, b))
        pixel_index += 1
        
    # Finally Save Encoded Image
    encoded_filename = image_filename.split('.')[0] + '_output.png'
    img.save(encoded_filename)
    return encoded_filename
        
#taking image as an input
image_filename = input("Enter file name:")

#taking message as an input
message = input("Enter message to be encoded:")

#call encoding function
encoded_filename = encode_image(image_filename, message)

#generate output file
print(f'Encoded image saved as {encoded_filename}')