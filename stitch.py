from PIL import Image

column_max = 127
row_max = 127

    
def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im
    
def get_concat_v_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_v_blank(_im, im)
    return _im



# im1 = Image.open('0_3.png')
# im2 = Image.open('0_2.png')
# im3 = Image.open('0_1.png')
# im4 = Image.open('0_0.png')
# get_concat_v_multi_blank([im1, im2, im3, im4]).save('stitched0.png')

# im1 = Image.open('stitched0.png')
# im2 = Image.open('stitched1.png')
# get_concat_h_multi_blank([im1, im2]).save('stitched.png')


# Create column stitches
# for column in range(0, column_max + 1):
#     row_list = []
#     for row in range(row_max, -1, -1):
#         file_name = "{}_{}.png".format(column, row)
#         row_list.append(Image.open(file_name))
#     get_concat_v_multi_blank(row_list).save('stitched_{}.png'.format(column))


# Create entire image
column_list = []
for column in range(0, column_max + 1):
    file_name = "stitched_{}.png".format(column)
    column_list.append(Image.open(file_name))
get_concat_h_multi_blank(column_list).save('stitched.png')