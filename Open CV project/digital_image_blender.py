import cv2 as cv

# varying values of alpha according to given function
# h(x) = (1-a) * f(x) + a * g(x)
print("Simple linear Image Blending enter alpha[0.0-1.0]:")
alpha=float(input())

# loading images for Blending
src1=cv.imread('LinuxLogo.png')
cv.imshow('Linux Logo', src1)
cv.waitKey(5000)
src2=cv.imread('WindowsLogo.png')
cv.imshow('Windows Logo', src2)
cv.waitKey(5000)

# Now Blending images src1 and src2
beta=(1.0-alpha)
dst=cv.addWeighted(src1, alpha, src2, beta, 0.0)

# displaying blended images
cv.imshow('Blended Image', dst)
cv.waitKey(5000)
cv.destroyAllWindows()




