"""
Quick & Easy v0.1
Makes 'Easy' easy when you answer quickly.

Copyright (c) 2016 Liam Cooke
https://github.com/araile/anki-addons

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import time

from anki.hooks import addHook

from aqt.reviewer import Reviewer


class Timer(object):

    def __init__(self):
        self._t = 0.0

    def start(self):
        self._t = time.time()

    def stop(self):
        elapsed, self._t = time.time() - self._t, 0.0
        return elapsed


timer = Timer()

def onShowQuestion():
    timer.start()

def my_defaultEase(self):
    ease = orig_defaultEase(self)

    answer_time = timer.stop()
    if 1.0 <= answer_time:
        return ease

    max_ease = self.mw.col.sched.answerButtons(self.card)
    return min(ease + 1, max_ease)


addHook('showQuestion', onShowQuestion)

orig_defaultEase = Reviewer._defaultEase
Reviewer._defaultEase = my_defaultEase
