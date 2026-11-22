"""
QRect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qrect.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMargins, QPoint, QRectF, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMargins = WAIT['QMargins']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']


class QRect(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRect: a plain Python object standing in front of one
  C++ QRect.

  C++ hands a QRect around as a copy, so every C++ QRect behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRect that has a ritual and that Python can call so
  far, 64 names in all: 'isNull', 'isEmpty', 'isValid', 'left', 'top',
  'right', 'bottom', 'normalized', 'x', 'y', 'setLeft', 'setTop', 'setRight',
  'setBottom', 'setX', 'setY', 'setTopLeft', 'setBottomRight', 'setTopRight',
  'setBottomLeft', 'topLeft', 'bottomRight', 'topRight', 'bottomLeft',
  'center', 'moveLeft', 'moveTop', 'moveRight', 'moveBottom', 'moveTopLeft',
  'moveBottomRight', 'moveTopRight', 'moveBottomLeft', 'moveCenter',
  'translate', 'translated', 'transposed', 'moveTo', 'setRect', 'setCoords',
  'adjust', 'adjusted', 'size', 'width', 'height', 'setWidth', 'setHeight',
  'setSize', '__or__', '__and__', '__ior__', '__iand__', 'contains',
  'united', 'intersected', 'intersects', 'marginsAdded', 'marginsRemoved',
  '__iadd__', '__isub__', 'span', '__eq__', '__ne__', 'toRectF'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QRect::getRect(int *x, int *y, int *w, int *h) const': takes a
    number to change where it is.
  - Qt's 'void QRect::getCoords(int *x1, int *y1, int *x2, int *y2) const':
    takes a number to change where it is.
  - Qt's 'QRect::~QRect()': the destructor: Python removes its C++ QRect by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 78 functions Qt declares: 1 private.

  What to expect
  --------------

  - The C++ QRect is created at the first use, not by 'QRect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRect back gives a copy the ritual made for Python,
    in a new cute QRect.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPoint, QPoint)
  def span(p1: QPoint, p2: QPoint) -> QRect:
    """
    Calls Qt's 'QRect QRect::span(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#span

    Parameters
    ----------

    p1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::span(const QPoint &p1, const QPoint &p2)
    address = Rituals.call(
        'ritual_ZN5QRect4spanERK6QPointS2_',
        CuteMixin._valueOf(p1), CuteMixin._valueOf(p2),
    )
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRect'

  #  Qt's '~QRect()'. Naming it makes this a value class: Python owns every
  #  C++ QRect behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QRectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QRect::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#isNull
    """
    #  bool QRect::isNull() const
    return self.uglySide.call('ritual_ZNK5QRect6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QRect::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#isEmpty
    """
    #  bool QRect::isEmpty() const
    return self.uglySide.call('ritual_ZNK5QRect7isEmptyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRect::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#isValid
    """
    #  bool QRect::isValid() const
    return self.uglySide.call('ritual_ZNK5QRect7isValidEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QRect::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#left
    """
    #  int QRect::left() const
    return self.uglySide.call('ritual_ZNK5QRect4leftEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QRect::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#top
    """
    #  int QRect::top() const
    return self.uglySide.call('ritual_ZNK5QRect3topEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QRect::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#right
    """
    #  int QRect::right() const
    return self.uglySide.call('ritual_ZNK5QRect5rightEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QRect::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#bottom
    """
    #  int QRect::bottom() const
    return self.uglySide.call('ritual_ZNK5QRect6bottomEv')

  def normalized(self) -> QRect:
    """
    Calls Qt's 'QRect QRect::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#normalized

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::normalized() const
    address = self.uglySide.call('ritual_ZNK5QRect10normalizedEv')
    return QRect._cuteOwning(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QRect::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#x
    """
    #  int QRect::x() const
    return self.uglySide.call('ritual_ZNK5QRect1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QRect::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#y
    """
    #  int QRect::y() const
    return self.uglySide.call('ritual_ZNK5QRect1yEv')

  def topLeft(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRect::topLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#topLeft

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRect::topLeft() const
    address = self.uglySide.call('ritual_ZNK5QRect7topLeftEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def bottomRight(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRect::bottomRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#bottomRight

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRect::bottomRight() const
    address = self.uglySide.call('ritual_ZNK5QRect11bottomRightEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def topRight(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRect::topRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#topRight

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRect::topRight() const
    address = self.uglySide.call('ritual_ZNK5QRect8topRightEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def bottomLeft(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRect::bottomLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#bottomLeft

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRect::bottomLeft() const
    address = self.uglySide.call('ritual_ZNK5QRect10bottomLeftEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def center(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRect::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#center

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRect::center() const
    address = self.uglySide.call('ritual_ZNK5QRect6centerEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  @overload(int, int)
  def translated(self, dx: int, dy: int) -> QRect:
    """
    Calls Qt's 'QRect QRect::translated(int dx, int dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#translated

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::translated(int dx, int dy) const
    address = self.uglySide.call('ritual_ZNK5QRect10translatedEii', dx, dy)
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def translated(self, p: QPoint) -> QRect:
    """
    Calls Qt's 'QRect QRect::translated(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#translated

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::translated(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK5QRect10translatedERK6QPoint', self._valueOf(p),
    )
    return QRect._cuteOwning(address)

  def transposed(self) -> QRect:
    """
    Calls Qt's 'QRect QRect::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#transposed

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::transposed() const
    address = self.uglySide.call('ritual_ZNK5QRect10transposedEv')
    return QRect._cuteOwning(address)

  @overload(int, int, int, int)
  def adjusted(self, x1: int, y1: int, x2: int, y2: int) -> QRect:
    """
    Calls Qt's 'QRect QRect::adjusted(int x1, int y1, int x2, int y2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#adjusted

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    x2 : int
      Passed on as it is.

    y2 : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::adjusted(int x1, int y1, int x2, int y2) const
    address = self.uglySide.call(
        'ritual_ZNK5QRect8adjustedEiiii', x1, y1, x2, y2,
    )
    return QRect._cuteOwning(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QRect::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRect::size() const
    address = self.uglySide.call('ritual_ZNK5QRect4sizeEv')
    from . import QSize
    return QSize._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QRect::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#width
    """
    #  int QRect::width() const
    return self.uglySide.call('ritual_ZNK5QRect5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QRect::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#height
    """
    #  int QRect::height() const
    return self.uglySide.call('ritual_ZNK5QRect6heightEv')

  @overload(THIS)
  @overload(THIS, bool)
  def contains(self, r: QRect, proper: bool = False) -> bool:
    """
    Calls Qt's 'bool QRect::contains(const QRect &r, bool proper) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#contains

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    proper : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QRect::contains(const QRect &r, bool proper) const
    return self.uglySide.call(
        'ritual_ZNK5QRect8containsERKS_b', self._valueOf(r), proper,
    )

  @overload(QPoint)
  @overload(QPoint, bool)
  def contains(self, p: QPoint, proper: bool = False) -> bool:
    """
    Calls Qt's 'bool QRect::contains(const QPoint &p, bool proper) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#contains

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    proper : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QRect::contains(const QPoint &p, bool proper) const
    return self.uglySide.call(
        'ritual_ZNK5QRect8containsERK6QPointb', self._valueOf(p), proper,
    )

  @overload(int, int)
  def contains(self, x: int, y: int) -> bool:
    """
    Calls Qt's 'bool QRect::contains(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#contains

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  bool QRect::contains(int x, int y) const
    return self.uglySide.call('ritual_ZNK5QRect8containsEii', x, y)

  @overload(int, int, bool)
  def contains(self, x: int, y: int, proper: bool) -> bool:
    """
    Calls Qt's 'bool QRect::contains(int x, int y, bool proper) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#contains

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    proper : bool
      Passed on as it is.
    """
    #  bool QRect::contains(int x, int y, bool proper) const
    return self.uglySide.call('ritual_ZNK5QRect8containsEiib', x, y, proper)

  @overload(THIS)
  def united(self, other: QRect) -> QRect:
    """
    Calls Qt's 'QRect QRect::united(const QRect &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#united

    Parameters
    ----------

    other : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::united(const QRect &other) const
    address = self.uglySide.call(
        'ritual_ZNK5QRect6unitedERKS_', self._valueOf(other),
    )
    return QRect._cuteOwning(address)

  @overload(THIS)
  def intersected(self, other: QRect) -> QRect:
    """
    Calls Qt's 'QRect QRect::intersected(const QRect &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#intersected

    Parameters
    ----------

    other : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::intersected(const QRect &other) const
    address = self.uglySide.call(
        'ritual_ZNK5QRect11intersectedERKS_', self._valueOf(other),
    )
    return QRect._cuteOwning(address)

  @overload(THIS)
  def intersects(self, r: QRect) -> bool:
    """
    Calls Qt's 'bool QRect::intersects(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#intersects

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QRect::intersects(const QRect &r) const
    return self.uglySide.call(
        'ritual_ZNK5QRect10intersectsERKS_', self._valueOf(r),
    )

  @overload(QMargins)
  def marginsAdded(self, margins: QMargins) -> QRect:
    """
    Calls Qt's 'QRect QRect::marginsAdded(const QMargins &margins) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#marginsAdded

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::marginsAdded(const QMargins &margins) const
    address = self.uglySide.call(
        'ritual_ZNK5QRect12marginsAddedERK8QMargins', self._valueOf(margins),
    )
    return QRect._cuteOwning(address)

  @overload(QMargins)
  def marginsRemoved(self, margins: QMargins) -> QRect:
    """
    Calls Qt's 'QRect QRect::marginsRemoved(const QMargins &margins) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#marginsRemoved

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::marginsRemoved(const QMargins &margins) const
    address = self.uglySide.call(
        'ritual_ZNK5QRect14marginsRemovedERK8QMargins',
        self._valueOf(margins),
    )
    return QRect._cuteOwning(address)

  def toRectF(self) -> QRectF:
    """
    Calls Qt's 'QRectF QRect::toRectF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#toRectF

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRect::toRectF() const
    address = self.uglySide.call('ritual_ZNK5QRect7toRectFEv')
    from . import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLeft(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::setLeft(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setLeft

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::setLeft(int pos)
    self.uglySide.call('ritual_ZN5QRect7setLeftEi', pos)

  @overload(int)
  def setTop(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::setTop(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setTop

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::setTop(int pos)
    self.uglySide.call('ritual_ZN5QRect6setTopEi', pos)

  @overload(int)
  def setRight(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::setRight(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setRight

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::setRight(int pos)
    self.uglySide.call('ritual_ZN5QRect8setRightEi', pos)

  @overload(int)
  def setBottom(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::setBottom(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setBottom

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::setBottom(int pos)
    self.uglySide.call('ritual_ZN5QRect9setBottomEi', pos)

  @overload(int)
  def setX(self, x: int) -> None:
    """
    Calls Qt's 'void QRect::setX(int x)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void QRect::setX(int x)
    self.uglySide.call('ritual_ZN5QRect4setXEi', x)

  @overload(int)
  def setY(self, y: int) -> None:
    """
    Calls Qt's 'void QRect::setY(int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void QRect::setY(int y)
    self.uglySide.call('ritual_ZN5QRect4setYEi', y)

  @overload(QPoint)
  def setTopLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::setTopLeft(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setTopLeft

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::setTopLeft(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect10setTopLeftERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def setBottomRight(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::setBottomRight(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setBottomRight

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::setBottomRight(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect14setBottomRightERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def setTopRight(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::setTopRight(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setTopRight

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::setTopRight(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect11setTopRightERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def setBottomLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::setBottomLeft(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setBottomLeft

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::setBottomLeft(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect13setBottomLeftERK6QPoint', self._valueOf(p),
    )

  @overload(int, int, int, int)
  def setRect(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QRect::setRect(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QRect::setRect(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN5QRect7setRectEiiii', x, y, w, h)

  @overload(int, int, int, int)
  def setCoords(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QRect::setCoords(int x1, int y1, int x2, int y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setCoords

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    x2 : int
      Passed on as it is.

    y2 : int
      Passed on as it is.
    """
    #  void QRect::setCoords(int x1, int y1, int x2, int y2)
    self.uglySide.call('ritual_ZN5QRect9setCoordsEiiii', x1, y1, x2, y2)

  @overload(int)
  def setWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QRect::setWidth(int w)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QRect::setWidth(int w)
    self.uglySide.call('ritual_ZN5QRect8setWidthEi', w)

  @overload(int)
  def setHeight(self, h: int) -> None:
    """
    Calls Qt's 'void QRect::setHeight(int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QRect::setHeight(int h)
    self.uglySide.call('ritual_ZN5QRect9setHeightEi', h)

  @overload(QSize)
  def setSize(self, s: QSize) -> None:
    """
    Calls Qt's 'void QRect::setSize(const QSize &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#setSize

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRect::setSize(const QSize &s)
    self.uglySide.call('ritual_ZN5QRect7setSizeERK5QSize', self._valueOf(s))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __or__(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect QRect::operator|(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator|

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::operator|(const QRect &r) const
    address = self.uglySide.call('ritual_ZNK5QRectorERKS_', self._valueOf(r))
    return QRect._cuteOwning(address)

  @overload.fallback
  def __or__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __and__(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect QRect::operator&(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator&

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRect::operator&(const QRect &r) const
    address = self.uglySide.call('ritual_ZNK5QRectanERKS_', self._valueOf(r))
    return QRect._cuteOwning(address)

  @overload.fallback
  def __and__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ior__(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect &QRect::operator|=(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator|=

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QRect &QRect::operator|=(const QRect &r)
    self.uglySide.call('ritual_ZN5QRectoRERKS_', self._valueOf(r))
    return self

  @overload.fallback
  def __ior__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __iand__(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect &QRect::operator&=(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator&=

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QRect &QRect::operator&=(const QRect &r)
    self.uglySide.call('ritual_ZN5QRectaNERKS_', self._valueOf(r))
    return self

  @overload.fallback
  def __iand__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QMargins)
  def __iadd__(self, margins: QMargins) -> QRect:
    """
    Calls Qt's 'QRect &QRect::operator+=(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator+=

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QRect &QRect::operator+=(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN5QRectpLERK8QMargins', self._valueOf(margins),
    )
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QMargins)
  def __isub__(self, margins: QMargins) -> QRect:
    """
    Calls Qt's 'QRect &QRect::operator-=(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator-=

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QRect &QRect::operator-=(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN5QRectmIERK8QMargins', self._valueOf(margins),
    )
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QRect) -> bool:
    """
    Calls Qt's 'bool operator==(const QRect &lhs, const QRect &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator==

    Parameters
    ----------

    rhs : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool operator==(const QRect &lhs, const QRect &rhs)
    return Rituals.call(
        'ritual_ZeqRK5QRectS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QRect) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRect &lhs, const QRect &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#operator!=

    Parameters
    ----------

    rhs : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool operator!=(const QRect &lhs, const QRect &rhs)
    return Rituals.call(
        'ritual_ZneRK5QRectS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRect::QRect()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#QRect
    """
    #  QRect::QRect()
    self._noteCreation(QRect, lambda: Rituals.call('ritual_ZN5QRectC1Ev'))

  @overload(QPoint, QPoint)
  def __init__(self, topleft: QPoint, bottomright: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QRect::QRect(const QPoint &topleft, const
    QPoint &bottomright)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#QRect

    Parameters
    ----------

    topleft : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    bottomright : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QRect::QRect(const QPoint &topleft, const QPoint &bottomright)
    self._noteCreation(QRect, lambda: Rituals.call(
        'ritual_ZN5QRectC1ERK6QPointS2_',
        self._valueOf(topleft), self._valueOf(bottomright),
    ))

  @overload(QPoint, QSize)
  def __init__(self, topleft: QPoint, size: QSize) -> None:
    """
    Notes what was given, for Qt's 'QRect::QRect(const QPoint &topleft, const
    QSize &size)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#QRect

    Parameters
    ----------

    topleft : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QRect::QRect(const QPoint &topleft, const QSize &size)
    self._noteCreation(QRect, lambda: Rituals.call(
        'ritual_ZN5QRectC1ERK6QPointRK5QSize',
        self._valueOf(topleft), self._valueOf(size),
    ))

  @overload(int, int, int, int)
  def __init__(self, left: int, top: int, width: int, height: int) -> None:
    """
    Notes what was given, for Qt's 'QRect::QRect(int left, int top, int
    width, int height)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#QRect

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  QRect::QRect(int left, int top, int width, int height)
    self._noteCreation(QRect, lambda: Rituals.call(
        'ritual_ZN5QRectC1Eiiii', left, top, width, height,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def moveLeft(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::moveLeft(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveLeft

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::moveLeft(int pos)
    self.uglySide.call('ritual_ZN5QRect8moveLeftEi', pos)

  @overload(int)
  def moveTop(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::moveTop(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveTop

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::moveTop(int pos)
    self.uglySide.call('ritual_ZN5QRect7moveTopEi', pos)

  @overload(int)
  def moveRight(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::moveRight(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveRight

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::moveRight(int pos)
    self.uglySide.call('ritual_ZN5QRect9moveRightEi', pos)

  @overload(int)
  def moveBottom(self, pos: int) -> None:
    """
    Calls Qt's 'void QRect::moveBottom(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveBottom

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRect::moveBottom(int pos)
    self.uglySide.call('ritual_ZN5QRect10moveBottomEi', pos)

  @overload(QPoint)
  def moveTopLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::moveTopLeft(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveTopLeft

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::moveTopLeft(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect11moveTopLeftERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def moveBottomRight(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::moveBottomRight(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveBottomRight

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::moveBottomRight(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect15moveBottomRightERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def moveTopRight(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::moveTopRight(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveTopRight

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::moveTopRight(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect12moveTopRightERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def moveBottomLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::moveBottomLeft(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveBottomLeft

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::moveBottomLeft(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect14moveBottomLeftERK6QPoint', self._valueOf(p),
    )

  @overload(QPoint)
  def moveCenter(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::moveCenter(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveCenter

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::moveCenter(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect10moveCenterERK6QPoint', self._valueOf(p),
    )

  @overload(int, int)
  def translate(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QRect::translate(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#translate

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QRect::translate(int dx, int dy)
    self.uglySide.call('ritual_ZN5QRect9translateEii', dx, dy)

  @overload(QPoint)
  def translate(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::translate(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#translate

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::translate(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QRect9translateERK6QPoint', self._valueOf(p),
    )

  @overload(int, int)
  def moveTo(self, x: int, t: int) -> None:
    """
    Calls Qt's 'void QRect::moveTo(int x, int t)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveTo

    Parameters
    ----------

    x : int
      Passed on as it is.

    t : int
      Passed on as it is.
    """
    #  void QRect::moveTo(int x, int t)
    self.uglySide.call('ritual_ZN5QRect6moveToEii', x, t)

  @overload(QPoint)
  def moveTo(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRect::moveTo(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#moveTo

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRect::moveTo(const QPoint &p)
    self.uglySide.call('ritual_ZN5QRect6moveToERK6QPoint', self._valueOf(p))

  @overload(int, int, int, int)
  def adjust(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QRect::adjust(int x1, int y1, int x2, int y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qrect.html#adjust

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    x2 : int
      Passed on as it is.

    y2 : int
      Passed on as it is.
    """
    #  void QRect::adjust(int x1, int y1, int x2, int y2)
    self.uglySide.call('ritual_ZN5QRect6adjustEiiii', x1, y1, x2, y2)
