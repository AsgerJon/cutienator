"""
Writes the picture following one method from Qt's C++ to Python.

  python one-method-from-qt-to-python.py one-method-from-qt-to-python.svg
  rsvg-convert -o one-method-from-qt-to-python.png \\
      one-method-from-qt-to-python.svg
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import html
import sys
from typing import List, Optional, Tuple

W = 1120
LEFT = 50
MAIN_W = 720
SIDE_X = 810
SIDE_W = 270
SANS = 'Liberation Sans, Arial, sans-serif'
MONO = 'Liberation Mono, monospace'
INK = '#1F2937'
SOFT = '#4B5563'
FOLLOW = '#F59E0B'
ARROW = '#374151'

KINDS = {
  'far': ('#FFFFFF', '#7A7A7A'),
  'text': ('#FFF6D5', '#B8960C'),
  'machine': ('#DCE3EC', '#4B5B70'),
  'program': ('#FFFFFF', '#333333'),
  'python': ('#DDF3E0', '#3C8D4A'),
  'end': ('#BFE8C6', '#2E7D3A'),
}

out: List[str] = []


def esc(text: str) -> str:
  """Escapes text for SVG."""
  return html.escape(text, quote=False)


def marked(text: str, colour: str) -> str:
  """Turns '[[...]]' in text into spans in the follow colour."""
  parts, rest = [], text
  while '[[' in rest:
    before, _, after = rest.partition('[[')
    inside, _, rest = after.partition(']]')
    parts.append(esc(before))
    span = '<tspan fill="%s" font-weight="bold">%s</tspan>'
    parts.append(span % (colour, esc(inside)))
  parts.append(esc(rest))
  return ''.join(parts)


def text(x: float, y: float, content: str, **kw: object) -> None:
  """Adds one line of text."""
  size = kw.get('size', 14)
  family = kw.get('family', SANS)
  fill = kw.get('fill', INK)
  weight = kw.get('weight', 'normal')
  anchor = kw.get('anchor', 'start')
  style = kw.get('style', 'normal')
  follow = kw.get('follow', FOLLOW)
  body = marked(content, str(follow))
  out.append(
    '<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
    'font-weight="%s" font-style="%s" text-anchor="%s" '
    'xml:space="preserve">%s</text>'
    % (x, y, family, size, fill, weight, style, anchor, body)
  )


def icon(kind: str, cx: float, cy: float, label: str = '') -> None:
  """Adds a small picture of what the thing is, centred at (cx, cy)."""
  x, y = cx - 24, cy - 24
  g = '<g transform="translate(%.1f,%.1f)">' % (x, y)
  mono = 'font-family="%s"' % MONO
  if kind in ('doc', 'docs'):
    if kind == 'docs':
      g += ('<path d="M14 0 h20 l8 8 v32 h-28 z" fill="#F3F4F6" '
            'stroke="#333" stroke-width="1.6"/>')
    g += ('<path d="M6 6 h22 l10 10 v32 h-32 z" fill="white" '
          'stroke="#333" stroke-width="2"/>'
          '<path d="M28 6 v10 h10" fill="none" stroke="#333" '
          'stroke-width="2"/>')
    g += ('<text x="22" y="38" %s font-size="11" font-weight="bold" '
          'fill="#333" text-anchor="middle">%s</text>' % (mono, esc(label)))
  elif kind == 'chip':
    for i in range(4):
      p = 11 + i * 8.5
      g += ('<path d="M%.1f 2 v6 M%.1f 40 v6 M2 %.1f h6 M40 %.1f h6" '
            'stroke="#333" stroke-width="2"/>' % (p, p, p, p))
    g += ('<rect x="7" y="7" width="34" height="34" rx="5" '
          'fill="#374151" stroke="#111827" stroke-width="1.5"/>')
    g += ('<text x="24" y="22" %s font-size="9.5" fill="#E5E7EB" '
          'text-anchor="middle">0110</text>'
          '<text x="24" y="34" %s font-size="9.5" fill="#E5E7EB" '
          'text-anchor="middle">1001</text>' % (mono, mono))
  elif kind == 'gear':
    for i in range(8):
      g += ('<rect x="21" y="1" width="6" height="10" rx="1.5" fill="#333" '
            'transform="rotate(%d 24 24)"/>' % (i * 45))
    g += ('<circle cx="24" cy="24" r="14" fill="#333"/>'
          '<circle cx="24" cy="24" r="6" fill="white"/>')
  elif kind == 'bridge':
    g += ('<rect x="0" y="13" width="18" height="22" rx="4" fill="#3C8D4A"/>'
          '<text x="9" y="28" %s font-size="10" font-weight="bold" '
          'fill="white" text-anchor="middle">Py</text>'
          '<rect x="30" y="13" width="18" height="22" rx="4" '
          'fill="#4B5B70"/>'
          '<text x="39" y="28" %s font-size="8.5" font-weight="bold" '
          'fill="white" text-anchor="middle">C++</text>'
          '<path d="M18 21 h12 M18 27 h12" stroke="#333" stroke-width="2"/>'
          '<path d="M27 18 l4 3 -4 3 z M21 24 l-4 3 4 3 z" fill="#333"/>'
          % (mono, mono))
  elif kind == 'tag':
    g += ('<path d="M4 12 h30 l10 12 -10 12 h-30 z" fill="white" '
          'stroke="#333" stroke-width="2"/>'
          '<circle cx="36" cy="24" r="2.5" fill="#333"/>'
          '<text x="18" y="29" %s font-size="13" font-weight="bold" '
          'fill="#333" text-anchor="middle">0x</text>' % mono)
  elif kind == 'heart':
    g += ('<path d="M24 42 C 2 26, 6 6, 24 15 C 42 6, 46 26, 24 42 Z" '
          'fill="#E11D48" stroke="#9F1239" stroke-width="1.5"/>')
  elif kind == 'prompt':
    g += ('<rect x="2" y="8" width="44" height="32" rx="5" fill="#111827"/>'
          '<text x="24" y="30" %s font-size="15" font-weight="bold" '
          'fill="#4ADE80" text-anchor="middle">&gt;&gt;&gt;</text>' % mono)
  elif kind == 'meta':
    g += ('<rect x="3" y="9" width="42" height="30" rx="6" fill="white" '
          'stroke="#333" stroke-width="2"/>'
          '<text x="24" y="29" %s font-size="12" font-weight="bold" '
          'fill="#333" text-anchor="middle">class</text>' % mono)
  elif kind == 'memory':
    for row in range(2):
      for col in range(4):
        hot = (row, col) == (1, 1)
        g += ('<rect x="%d" y="%d" width="10" height="14" fill="%s" '
              'stroke="#333" stroke-width="1.2"/>'
              % (2 + col * 11, 9 + row * 15, '#F59E0B' if hot else 'white'))
  g += '</g>'
  out.append(g)


def miniature(
    x: float, y: float, w: float, lines: List[str], size: float = 13.5,
) -> float:
  """Adds a dark box showing the real thing; gives its height."""
  step = size + 6
  h = len(lines) * step + 18
  out.append(
    '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="7" '
    'fill="#1F2937"/>' % (x, y, w, h)
  )
  for i, line in enumerate(lines):
    text(x + 12, y + 14 + size * 0.75 + i * step, line, size=size,
         family=MONO, fill='#E5E7EB', follow='#FBBF24')
  return h


def card(
    x: float, y: float, w: float, kind: str, number: str,
    pic: Tuple[str, str], title: str, says: List[str],
    where: Optional[str], mini: List[str],
    mini_size: float = 13.5, caption: Optional[str] = None,
) -> float:
  """Adds one box of the picture and gives its height."""
  fill, stroke = KINDS[kind]
  narrow = w < 500
  tx = x + (78 if narrow else 96)
  h = 22 + 24 + len(says) * 19 + (20 if where else 0) + 8
  mini_x = x + 16 if narrow else tx
  mini_w = w - 32 if narrow else w - (tx - x) - 20
  mini_h = len(mini) * (mini_size + 6) + 18
  h += mini_h + (22 if caption else 0) + 16
  dash = ' stroke-dasharray="7 5"' if kind == 'far' else ''
  width = 3 if kind == 'end' else 1.8
  out.append(
    '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="12" fill="%s" '
    'stroke="%s" stroke-width="%s"%s/>'
    % (x, y, w, h, fill, stroke, width, dash)
  )
  cx = x + (40 if narrow else 50)
  cy = y + 46
  out.append(
    '<circle cx="%.1f" cy="%.1f" r="%d" fill="white" stroke="%s" '
    'stroke-width="1.5"/>' % (cx, cy, 31 if not narrow else 29, stroke)
  )
  icon(pic[0], cx, cy, pic[1])
  out.append(
    '<circle cx="%.1f" cy="%.1f" r="12" fill="%s"/>' % (x + 2, y + 2, stroke)
  )
  text(x + 2, y + 7, number, size=13, fill='white', weight='bold',
       anchor='middle')
  ty = y + 38
  text(tx, ty, title, size=19, weight='bold')
  for i, line in enumerate(says):
    text(tx, ty + 23 + i * 19, line, size=14, fill=SOFT)
  ty += 23 + len(says) * 19
  if where:
    text(tx, ty + 1, where, size=12, family=MONO, fill='#6B7280')
    ty += 20
  my = ty + 2 if not narrow else max(ty + 2, y + 86)
  if narrow:
    h = (my - y) + mini_h + (22 if caption else 0) + 16
    out[out.index(next(o for o in out if o.startswith(
      '<rect x="%.1f" y="%.1f" width="%.1f" height=' % (x, y, w)
    )))] = (
      '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="12" '
      'fill="%s" stroke="%s" stroke-width="%s"%s/>'
      % (x, y, w, h, fill, stroke, width, dash)
    )
  miniature(mini_x, my, mini_w, mini, mini_size)
  if caption:
    text(mini_x + 2, my + mini_h + 16, caption, size=12, fill=SOFT,
         style='italic')
  return h


def arrow(x: float, y1: float, y2: float, says: str = '') -> None:
  """Adds one downward arrow with the words that join two boxes."""
  out.append(
    '<path d="M%.1f %.1f V%.1f" stroke="%s" stroke-width="3" fill="none"/>'
    '<path d="M%.1f %.1f l-7 -11 h14 z" fill="%s"/>'
    % (x, y1, y2 - 9, ARROW, x, y2, ARROW)
  )
  if says:
    text(x + 16, (y1 + y2) / 2 + 5, says, size=14, fill=INK, style='italic')


def side(
    y: float, pic: str, title: str, says: List[str], to_x: float,
    to_y: float,
) -> None:
  """Adds a side note joined to the main column by a dashed line."""
  h = 46 + len(says) * 18 + 14
  out.append(
    '<rect x="%d" y="%.1f" width="%d" height="%.1f" rx="10" fill="white" '
    'stroke="#6B7280" stroke-width="1.4" stroke-dasharray="6 4"/>'
    % (SIDE_X, y, SIDE_W, h)
  )
  icon(pic, SIDE_X + 34, y + 34)
  text(SIDE_X + 68, y + 30, title, size=15, weight='bold')
  for i, line in enumerate(says):
    text(SIDE_X + 14, y + 68 + i * 18, line, size=13, fill=SOFT)
  out.append(
    '<path d="M%d %.1f L%.1f %.1f" stroke="#6B7280" stroke-width="1.6" '
    'stroke-dasharray="6 4" fill="none"/>' % (SIDE_X, y + 30, to_x, to_y)
  )


def main(target: str) -> None:
  """Lays the picture out from the top and writes it to 'target'."""
  spine = LEFT + 50
  right = LEFT + MAIN_W
  y = 44
  text(W / 2, y, 'One method, from Qt\'s C++ down to your Python', size=28,
       weight='bold', anchor='middle')
  y += 30
  text(W / 2, y, 'Follow [[show()]] through every box. Each dark panel '
       'shows the real thing. The last box is the line you write.', size=15,
       fill=SOFT, anchor='middle', follow='#D97706')
  y += 28

  #  0. Qt's source.
  h = card(
    LEFT, y, MAIN_W, 'far', '1', ('docs', 'C++'), 'Qt\'s source code',
    ['C++ text written by the people who make Qt. It is not on your',
     'machine. Whoever packaged Qt for your system compiled it for you.'],
    None,
    ['void QWidget::[[show]]()', '{', '    // Qt\'s own code', '}'],
  )
  y0 = y + h
  gap = 56
  #  1. The two halves.
  half = (MAIN_W - 20) / 2
  y1 = y0 + gap
  arrow(LEFT + half / 2, y0, y1)
  arrow(LEFT + half + 20 + half / 2, y0, y1)
  text(LEFT + MAIN_W / 2, y0 + gap / 2 + 5,
       'arrives on your machine as two things', size=14, style='italic',
       anchor='middle')
  ha = card(
    LEFT, y1, half, 'text', '2', ('doc', '.h'), 'Qt\'s header',
    ['Text. Says what QWidget has,', 'by name. No working code.'],
    '/usr/include/qt6/QtWidgets/qwidget.h',
    ['class QWidget : public QObject, ...', 'public Q_SLOTS:',
     '    void [[show]]();'],
    12.5,
  )
  hb = card(
    LEFT + half + 20, y1, half, 'machine', '3', ('chip', ''),
    'Qt\'s shared object',
    ['Machine code. The working show(),', 'under a scrambled name.'],
    '/usr/lib/libQt6Widgets.so.6',
    ['_ZN7QWidget4[[show]]Ev', '11110011 00001111 00011110 11111010',
     '01001000 10001011 01000111 00100000'],
    12.5,
    'its real first 8 bytes',
  )
  hrow = max(ha, hb)
  y2 = y1 + hrow + gap
  arrow(spine, y1 + ha, y2, 'we read the name from it, and write')
  #  2. Our ritual file.
  h = card(
    LEFT, y2, MAIN_W, 'text', '4', ('doc', '.cpp'), 'Our ritual file',
    ['C++ text that we write. One small function that gives show() a',
     'plain name and calls the real one.'],
    'q_widget.cpp',
    ['extern "C" void [[QWidget_show]](QWidget *self) {',
     '  self->[[show]]();', '}'],
  )
  y3 = y2 + h + gap
  arrow(spine, y2 + h, y3, 'goes into')
  #  3. The compiler.
  h = card(
    LEFT, y3, MAIN_W, 'program', '5', ('gear', ''), 'g++, the compiler',
    ['A program you run once. It reads our ritual file and Qt\'s header,',
     'and is told which Qt shared object the result calls into.'],
    None,
    ['$ g++ -shared -fPIC -I/usr/include/qt6 q_widget.cpp \\',
     '      -o librituals.so /usr/lib/libQt6Widgets.so.6'],
  )
  y4 = y3 + h + gap
  arrow(spine, y3 + h, y4, 'which writes')
  #  4. Our shared object.
  h4 = card(
    LEFT, y4, MAIN_W, 'machine', '6', ('chip', ''), 'Our shared object',
    ['Machine code again, but now under the plain name. Inside, it calls',
     'the real show() in Qt\'s shared object. "nm" lists what it offers.'],
    'librituals.so',
    ['$ nm -D --defined-only librituals.so',
     '0000000000001220 T [[QWidget_show]]'],
  )
  #  The long way round from Qt's shared object.
  gx = right + 22
  ya = y1 + hb / 2
  yb = y4 + 46
  out.append(
    '<path d="M%.1f %.1f H%.1f V%.1f H%.1f" stroke="%s" stroke-width="3" '
    'fill="none"/><path d="M%.1f %.1f l11 -7 v14 z" fill="%s"/>'
    % (right, ya, gx, yb, right + 9, ARROW, right, yb, ARROW)
  )
  text(gx + 12, (ya + yb) / 2 - 8, 'whose working', size=14, style='italic')
  text(gx + 12, (ya + yb) / 2 + 10, 'show() it calls', size=14,
       style='italic')

  #  The line between made once and every run.
  yd = y4 + h4 + 30
  out.append(
    '<path d="M%d %.1f H%d" stroke="#9CA3AF" stroke-width="2" '
    'stroke-dasharray="10 7"/>' % (20, yd, W - 20)
  )
  text(W - 24, yd - 9, 'ABOVE: made once, before anything runs', size=12.5,
       fill='#6B7280', weight='bold', anchor='end')
  text(W - 24, yd + 19, 'BELOW: every time your program runs', size=12.5,
       fill='#6B7280', weight='bold', anchor='end')
  y5 = yd + 62
  arrow(spine, y4 + h4, y5)
  text(spine + 16, yd + 36, 'which Python opens with', size=14,
       style='italic')
  #  5. ctypes.
  h5 = card(
    LEFT, y5, MAIN_W, 'python', '7', ('bridge', ''), 'ctypes',
    ['Comes with Python. Opens our shared object and runs a function in',
     'it by name. Only numbers go across: here, the widget\'s address.'],
    None,
    ['ours = ctypes.CDLL(\'librituals.so\')',
     'ours.[[QWidget_show]](address)'],
  )
  y6 = y5 + h5 + gap
  arrow(spine, y5 + h5, y6, 'used only by')
  #  6. Ugly.
  h6 = card(
    LEFT, y6, MAIN_W, 'python', '8', ('tag', ''), 'Ugly, the ugly side',
    ['Your class for the C++ side of something cute. It holds the address',
     'of the C++ widget, and is the one place that touches ctypes.'],
    None,
    ['class Ugly:',
     '  address = 0x564cb5ecea40',
     '  def call(self, name): ...   # ours.[[QWidget_show]](address)'],
    13.5,
    'a sketch: Ugly is not written yet',
  )
  y7 = y6 + h6 + gap
  arrow(spine, y6 + h6, y7, 'which sits behind')
  #  7. Cute.
  h7 = card(
    LEFT, y7, MAIN_W, 'python', '9', ('heart', ''), 'QWidget, the cute side',
    ['The plain Python class people use. Its method does nothing but ask',
     'its ugly side.'],
    None,
    ['class QWidget(CuteMixin):',
     '  def [[show]](self) -> None:',
     '    self.uglySide.call(\'[[QWidget_show]]\')'],
    13.5,
    'a sketch: this method is not written yet',
  )
  y8 = y7 + h7 + gap
  arrow(spine, y7 + h7, y8, 'whose method you call')
  #  8. The end.
  h8 = card(
    LEFT, y8, MAIN_W, 'end', '10', ('prompt', ''), 'Your program',
    ['The line you write. Everything above exists so that this works.'],
    None,
    ['widget = QWidget()', 'widget.[[show]]()'],
    16,
  )

  #  Side notes.
  side(
    y5 + 6, 'meta', 'The metaclass',
    ['Opens our shared object once', 'and hands it to every Ugly.',
     'Planned, not written yet.'],
    right, y5 + 40,
  )
  side(
    y6 + 8, 'memory', 'The C++ widget itself',
    ['Lives in the memory of your', 'running program, at that address.',
     'Qt\'s code works on it there.'],
    right, y6 + 44,
  )

  #  What the colours mean.
  yl = y8 + h8 + 40
  x = LEFT
  for kind, says in (
      ('text', 'text you can read'), ('machine', 'machine code'),
      ('python', 'Python'), ('program', 'a program you run'),
  ):
    fill, stroke = KINDS[kind]
    out.append(
      '<rect x="%.1f" y="%.1f" width="22" height="16" rx="3" fill="%s" '
      'stroke="%s" stroke-width="1.4"/>' % (x, yl, fill, stroke)
    )
    text(x + 30, yl + 13, says, size=13, fill=SOFT)
    x += 46 + len(says) * 7.3
  out.append(
    '<rect x="%.1f" y="%.1f" width="22" height="16" rx="3" fill="%s"/>'
    % (x, yl, FOLLOW)
  )
  text(x + 30, yl + 13, 'the one method we follow', size=13, fill=SOFT)
  yl += 44
  text(LEFT, yl, 'Not in this picture: C++ calling into your Python '
       '(paintEvent, signals). That direction is not built yet.', size=13,
       fill=SOFT, style='italic')
  total = yl + 30

  head = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
    'viewBox="0 0 %d %d"><rect width="%d" height="%d" fill="white"/>'
    % (W, total, W, total, W, total)
  )
  with open(target, 'w') as file:
    file.write(head + '\n' + '\n'.join(out) + '\n</svg>\n')


if __name__ == '__main__':
  main(sys.argv[1])
