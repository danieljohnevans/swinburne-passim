import ht_text_prep as htp
import os
import glob

# only run this once to get clean text
# data_dir = '/Users/user/Documents/uiuc/swinburne/swinburne-passim/data/htrc_swinburne'
output_dir = '/Users/user/Documents/uiuc/swinburne/swinburne-passim/data/htrc_swinburne_clean'

# htp.get_zips(data_dir, output_dir, delete_zips=False)
 
f = os.listdir(output_dir)
temp = map(lambda name: os.path.join(output_dir, name), f)
vol_dir = list(temp)

# to rename files
# for filename in glob.iglob('/Users/user/Documents/uiuc/swinburne/swinburne-passim/data/htrc_swinburne_clean/**', recursive=True):
#     if os.path.isdir(filename):
#         os.rename(filename, filename.replace('ark+=', 'ark'))

# to normalize txt names
# for folder in vol_dir:
# 	htp.normalize_txt_file_names(folder, prnt=True)



out_dir = '/Users/user/Documents/uiuc/swinburne/swinburne-passim/htrc_out'

htp.clean_vol(vol_dir, out_dir)