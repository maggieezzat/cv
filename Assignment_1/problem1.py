from PIL import Image
import numpy as np 

'''
def compute_coocc():

    #img_list = list(img.getdata())
    #img_pixels = set(img_list)
    img_pixels = [4,5,6,7,8]

    # 256 x 256 matrix, with non existant values in matrix as well
    co_occ = np.zeros((256, 256))

    #img = np.array(img)
    img = np.array([[4,6,8,5,4],
    [5,5,8,7,7],
    [6,7,7,7,9],
    [8,8,4,8,6],
    [9,8,9,5,6]])
    for i in range (0,img.shape[0]-1):
        for j in range (0,img.shape[1]):
            x = img[i][j]
            x_south = img[i+1,j]
            co_occ[x][x_south] +=1

    print(co_occ[4])
    print(co_occ[5])
    print(co_occ[6])
    print(co_occ[7])
    print(co_occ[8])
    print(co_occ[9])

    contrast =0
    for i in range (0,co_occ.shape[0]):
        for j in range (0,co_occ.shape[1]):
            contrast += co_occ[i][j]* (i-j) * (i-j)

    print(contrast)

    return contrast  
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



def increase_contrast(img, a, b, c, d, img_name):
    
    img = np.array(img)
    new_img = np.zeros(img.shape)
    
    m1 = b/a
    c1 = b - m1*a

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


    high_contrast_img = Image.fromarray(new_img)
    high_contrast_img = high_contrast_img.convert('L')
    high_contrast_img.save(img_name)

    contrast = compute_contrast(high_contrast_img)
    with open('contrast.txt', 'a') as f:
        f.write(img_name + " contrast: " + str(contrast) + '\n')



def main():
    img = Image.open("Ocean.bmp")
    #increase_contrast(img, 30, 20, 180, 230, 'Ocean_a.bmp')
    #increase_contrast(img, 70, 20, 140, 240, 'Ocean_b.bmp')
    #compute_coocc()
    



if __name__ == "__main__":
    main()
