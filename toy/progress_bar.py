#! /usr/bin/env python3
# coding: utf-8

from __future__ import print_function


def with_color(text, fg='0', bg='0'):
    return '\033[{fg}m{text}\033[{bg}m'.format(fg=fg, bg=bg, text=text)


class ProgressBar(object):
    def __init__(self, length=40, handler='', fill='█', fg='0;34', bg='0'):
        self.fill = fill
        self.fg = fg
        self.bg = bg
        self.length = length
        self._ratio = 0

    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value
        self._update()

    def _update(self):
        value = int(self.length * self._ratio)
        checked = with_color(self.fill * value, fg=self.fg)
        unchecked = (self.length - value) * '-'
        bar = checked + unchecked
        print('\r Progress: |%s| %s%%' % (bar, int(self._ratio * 100)),
              end='\r')

    def __enter__(self):
        print('\r Progress: |%s| %s%%' % ('-' * self.length, 0), end='\r')
        return self

    def __exit__(self, type, value, traceback):
        print()


if __name__ == '__main__':
    import time

    with ProgressBar() as pb:
        time.sleep(0.5)
        for i in range(0, 100, 2):
            time.sleep(0.1)
            pb.ratio = float(i)/100
