"""
Quick & Easy v0.3
Makes 'Easy' easy when you answer quickly.

Copyright (c) 2016 Liam Cooke
https://github.com/araile/anki-quick-easy

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


# Edit this line to adjust how quickly you must reveal the answer
EASY_SECONDS = 1.0


def my_defaultEase(self):
    ease = orig_defaultEase(self)

    if self.hadCardQueue:
        # card came from the undo queue
        return ease

    if EASY_SECONDS * 1000 <= self.card.timeTaken():
        # wasn't answered quickly
        return ease

    if self.card.id in self._answeredIds:
        # card is being reviewed again
        return ease

    max_ease = self.mw.col.sched.answerButtons(self.card)
    return min(ease + 1, max_ease)


orig_defaultEase = Reviewer._defaultEase
Reviewer._defaultEase = my_defaultEase
