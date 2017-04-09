import os
import shutil

os.makedirs('test_set')
shutil.move("certificate.p12", "test_set/new.p12")
