from PIL import Image
import numpy as np 



'''
def compute_contrast(img):

    img_list = list(img.getdata())
    img_pixels = set(img_list)

    # 256 x 256 matrix, with non existant values in matrix as well
    co_occ = np.zeros((256, 256))

    img = np.array(img)
    for i in range (0,img.shape[0]-1):
        for j in range (0,img.shape[1]):
            x = img[i][j]
            x_south = img[i+1,j]
            co_occ[x][x_south] +=1

    contrast =0
    for i in range (0,co_occ.shape[0]):
        for j in range (0,co_occ.shape[1]):
            contrast += co_occ[i][j]* (i-j) * (i-j)

    return contrast    
'''
def compute_contrast(img):

    # 256 x 256 matrix, with non existant values in the cooccurence matrix as well
    # this is in order to make the indices as the intensity values
    co_occ = np.zeros((256, 256)).astype(int)

    img = np.array(img)
    for i in range (0,img.shape[0]-1):
        for j in range (0,img.shape[1]):
            x = img[i][j]
            x_south = img[i+1,j]
            co_occ[x][x_south] = co_occ[x][x_south]+1

    

    contrast =0
    for i in range (0,co_occ.shape[0]):
        for j in range (0,co_occ.shape[1]):
            contrast += co_occ[i][j]* ((i-j)**2)

    return contrast  

'''
def increase_contrast(img, a, b, c, d, img_name):
    
    img = np.array(img)
    new_img = np.zeros(img.shape)
    
    m1 = b/a
    #c1 = b - m1*a
    c1 = 0

    m2 = (d-b)/(c-a) 
    c2 = d - m2*c

    m3 = (255-d)/(255-c)
    c3 = 255 - m3*255

    for i in range (0,img.shape[0]):
        for j in range (0,img.shape[1]):
            x = img[i][j]
            if x<a:
                y = m1*x + c1
            elif x<c:
                y = m2*x + c2
            elif x<255:
                y = m3*x + c3
            else:
                y = 255
            new_img[i][j] = int(y)

    new_img = new_img.astype('uint8')
    high_contrast_img = Image.fromarray(new_img)
    #high_contrast_img = high_contrast_img.convert('L')
    high_contrast_img.save(img_name)

    contrast = compute_contrast(high_contrast_img)
    with open('contrast.txt', 'a') as f:
        f.write(img_name + " contrast: " + str(contrast) + '\n')
'''

def increase_contrast(img, a, b, c, d):
    
    img_arr = np.array(img)
    
    m1 = b/a
    c1 = 0

    m2 = (d-b)/(c-a) 
    c2 = d - (m2 * c)
    #c2 = -22.0

    m3 = (255-d)/(255-c)
    c3 = 255 - m3*255

    for i in range (0,img_arr.shape[0]):
        for j in range (0,img_arr.shape[1]):
            x = img_arr[i][j]
            if x<=a:
                y = m1*x + c1
            elif x<=c:
                y = m2*x + c2
            elif x<=255:
                y = m3*x + c3
            else:
                y = 255
            img_arr[i][j] = int(y)
            
    #img = img.astype('uint8')
    output_img = Image.fromarray(img_arr)
    contrast = compute_contrast(output_img)
    #img = Image.convert('L')
    return (output_img, contrast)


def main():
    #read the image
    img = Image.open("Ocean.bmp")
    #image A
    (img_a, contrast_a) = increase_contrast(img, 30, 20, 180, 230)
    #img_a.save('Ocean_a.bmp')
    #image B
    (img_b, contrast_b) = increase_contrast(img, 70, 20, 140, 240)
    #img_b.save('Ocean_b.bmp')

    print(contrast_a)
    print(contrast_b)

    #writing the contrast in a text file
    #with open('contrast.txt', 'w') as f:
    #    f.write("Ocean_a.bmp contrast: " + str(contrast_a) + '\n')
    #    f.write("Ocean_b.bmp contrast: " + str(contrast_b) + '\n')
    



if __name__ == "__main__":
    main()
