from PIL import Image
import numpy as np 
import math


def compute_integral(img, img_name):

    img = np.array(img)
    s_img = np.zeros(img.shape).astype(int)
    ii_img = np.zeros(img.shape).astype(int)
    #ii_img_python = img.cumsum(axis=1).cumsum(axis=0)

    #compute S which is cumulative i sum, use it to compute ii
    for i in range (0,img.shape[0]):
        for j in range (0,img.shape[1]):
            if j==0:
                s_img[i][j] =  img[i][j]
            else: 
                s_img[i][j] = s_img[i][j-1] + img[i][j]

            if i==0:
                ii_img[i][j] =  s_img[i][j] 
            else:   
                ii_img[i][j] = ii_img[i-1][j] + s_img[i][j]


    integral_img = Image.fromarray(ii_img)
    integral_img = integral_img.convert('L')
    integral_img.save(img_name)
    return ii_img


def noise_removal_filter(img, filter_size, img_name):

    ii_img = compute_integral(img, 'Camera_Integ.jpg')

    img = np.array(img)
    avg_img = np.full(img.shape, 255, dtype=int)
    #avg_img = np.ones(img.shape)*255

    b = math.floor(filter_size /2)

    for i in range (b, img.shape[0]-b):
        for j in range (b, img.shape[1]-b):
            
            #3
            #sum_neighbours = ii_img[i+1][j+1] - ii_img[i+1][j-2] - ii_img[i-2][j+1] + ii_img[i-2][j-2]
            #5
            #sum_neighbours = ii_img[i+2][j+2] - ii_img[i+2][j-3] - ii_img[i-3][j+2] + ii_img[i-3][j-3]
            #7
            #sum_neighbours = ii_img[i+3][j+3] - ii_img[i+3][j-4] - ii_img[i-4][j+3] + ii_img[i-4][j-4]

            sum_neighbours = ii_img[i+b][j+b] - ii_img[i+b][j-b-1] - ii_img[i-b-1][j+b] + ii_img[i-b-1][j-b-1]

            filter_value = sum_neighbours / (filter_size * filter_size) 
            avg_img[i][j] = int(filter_value)

    filtered_img = Image.fromarray(avg_img)
    filtered_img = filtered_img.convert('L')
    filtered_img.save(img_name)




def main():
    img = Image.open("Cameraman_noise.bmp")
    compute_integral(img, 'Camera_Integ.jpg')
    noise_removal_filter(img, 3, 'Camera_Filt_3.bmp')
    noise_removal_filter(img, 5, 'Camera_Filt_5.jpg')
    #noise_removal_filter(img, 7, 'Camera_Filt_7.jpg')
    #noise_removal_filter(img, 9, 'Camera_Filt_9.jpg')
    



if __name__ == "__main__":
    main()

