import pymongo
# coding:utf-8
connection = pymongo.MongoClient()
tdb = connection.jikexueyuan
post_info = tdb.test

jike = {'name':u'极客','age':'4','skill':'python'}
god = {'name':u'玉皇大帝','age':36000,'skill':'connection','other':u'hahaha'}

post_info.insert(jike)
post_info.insert(god)
post_info.remove({'name':u'极客'})
