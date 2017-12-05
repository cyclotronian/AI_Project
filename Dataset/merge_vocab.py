from __future__ import print_function

files = ['./final_datasets/cornell_dialog_small/vocab', './final_datasets/friends_dialog_s/vocab']
out_files = ['./final_datasets/cornell_dialog_small/vocab']
        
def merge_vocab(local_files,out_file):
  vocab = {}
  for filename in local_files:
    with open(filename, 'r') as file:
        for line in file:
            vocab[line[:-1]] = 1

  for filename in out_file:
      out_file_d = open(filename, 'w')
      for key in vocab:
          print(key,file=out_file_d)
          
for suffix in ['.utt','.resp']:
  new_files = [file + suffix for file in files]
  new_out_files = [file + suffix for file in out_files]
  # print (new_files)
  # print (new_out_files)
  merge_vocab(new_files, new_out_files)