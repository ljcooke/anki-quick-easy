"""
Quick & Easy v1.0
Makes 'Easy' easy when you answer quickly.

Copyright (c) 2016-2018 Liam Cooke
https://github.com/ljcooke/anki-quick-easy

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
from aqt import mw
from aqt.reviewer import Reviewer


# Default configuration for Anki 2.0
LEGACY_CONFIG = {
    'seconds': 1.0,
}


def config():
    """
    Configuration via config.json (introduced in Anki 2.1)
    """
    try:
        getConfig = mw.addonManager.getConfig
    except AttributeError:
        return LEGACY_CONFIG

    return getConfig(__name__)


def my_defaultEase(self):
    ease = orig_defaultEase(self)

    if self.hadCardQueue:
        # card came from the undo queue
        return ease

    if config()['seconds'] * 1000 <= self.card.timeTaken():
        # wasn't answered quickly
        return ease

    if self.card.id in self._answeredIds:
        # card is being reviewed again
        return ease

    max_ease = self.mw.col.sched.answerButtons(self.card)
    return min(ease + 1, max_ease)


orig_defaultEase = Reviewer._defaultEase
Reviewer._defaultEase = my_defaultEase
