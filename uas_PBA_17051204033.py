# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:32:03 2020

@author: husni
"""

import nltk,re
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tag import CRFTagger

#corpus yang digunakan adalah corpus kompas online 
#bisa di download di https://github.com/kmkurn/id-nlp-resource

#proses memasukkan / membaca corpus
corpus_root = 'txt/'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')

#pos tag yang digunakan berasal dari famrashel (https://github.com/famrashel/idn-tagged-corpus)
#pos tag model yang sudah dilatih bisa didownload di https://drive.google.com/open?id=12yJ82GzjnqzrjX14Ob_p9qnPKtcSmqAx

#proses membaca / memanggil pos tag model
ct = CRFTagger()
ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

#memilih text corpus yang akan digunakan
raw = newcorpus.words('1.txt')
#tidak perlu melakukan tokenisasi karena fungsi plaintextreader sudah melakukan word_tokenisasi
#berhasil

#text = [item.lower() for item in raw]
#hasil = ct.tag_sents([text])
#melakukan proses pos tag dari text yang dipilih
hasil = ct.tag_sents([raw])

#membuat filte txt untuk menyimpan hasil
file = open("hasil.txt","w") 

#proses memilih data yang akan ditampilkan (tokoh, waktu, lokasi) pada consol
#PRP untuk kata ganti orang pertama
#NNP untuk tokoh, waktu, lokasi
#CD untuk angka seperti tahunn bulan, tanggal, dsb
for tokenTag in hasil[0]:
      token, tag = tokenTag;
      if tag == 'PRP' : print(token+"–>"+tag)
      if tag == 'NNP' : print(token+"–>"+tag)
      if tag == 'CD' : print(token+"–>"+tag)
      
      
#proses memilih data yang akan disimpan pada file
for tokenTag in hasil[0]:
      token, tag = tokenTag;
      if tag == 'PRP' : file.write(token+"–>"+tag+"\n")
      if tag == 'NNP' : file.write(token+"–>"+tag+"\n")
      if tag == 'CD' : file.write(token+"–>"+tag+"\n")