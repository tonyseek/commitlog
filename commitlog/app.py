# coding: utf-8

import random
from flask import Flask

messages = [
    '修了修了别再催我了',
    '诶我去, 上一个提交好像不太对',
    '打错字了',
    '这样应该就可以了吧?',
    '那可能是需要这么搞一下',
    '啊啊啊啊啊终于好了',
    '我艹好像还是没好, 那这么改一下试试',
    '你妈啊这样总可以了吧',
    '谁写的sb代码, 改了改了',
    '先这样吧, 明天再说...',
    '快到点了, 准备闪人了',
    '写的什么鬼, 不过能跑, 就酱吧',
    '啊啊啊啊写错了, 还好这次改对了',
    '这次的提交能值多少钱呢?',
    '我是sb...',
]

app = Flask(__name__)


@app.route('/')
def index():
    return '%s\n' % random.choice(messages)
