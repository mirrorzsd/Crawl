# -*- coding:utf-8 -*-
import base64

encodestr = base64.b64encode('京剧猫喵日常'.encode('utf-8'))#
print(str(encodestr,'utf-8'))