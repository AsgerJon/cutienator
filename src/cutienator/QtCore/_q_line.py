"""
QLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qline.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QLineF, QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QLine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLine: a plain Python object standing in front of one
  C++ QLine.

  C++ hands a QLine around as a copy, so every C++ QLine behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLine that has a ritual and that Python can call so
  far, 19 names in all: 'isNull', 'p1', 'p2', 'x1', 'y1', 'x2', 'y2', 'dx',
  'dy', 'translate', 'translated', 'center', 'setP1', 'setP2', 'setPoints',
  'setLine', 'toLineF', '__eq__', '__ne__'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLine::~QLine()': the destructor: Python removes its C++ QLine by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLine is created at the first use, not by 'QLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLine back gives a copy the ritual made for Python,
    in a new cute QLine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLine'

  #  Qt's '~QLine()'. Naming it makes this a value class: Python owns every
  #  C++ QLine behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QLineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QLine::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#isNull
    """
    #  bool QLine::isNull() const
    return self.uglySide.call('ritual_ZNK5QLine6isNullEv')

  def p1(self) -> QPoint:
    """
    Calls Qt's 'QPoint QLine::p1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#p1

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QLine::p1() const
    address = self.uglySide.call('ritual_ZNK5QLine2p1Ev')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def p2(self) -> QPoint:
    """
    Calls Qt's 'QPoint QLine::p2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#p2

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QLine::p2() const
    address = self.uglySide.call('ritual_ZNK5QLine2p2Ev')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def x1(self) -> int:
    """
    Calls Qt's 'int QLine::x1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#x1
    """
    #  int QLine::x1() const
    return self.uglySide.call('ritual_ZNK5QLine2x1Ev')

  def y1(self) -> int:
    """
    Calls Qt's 'int QLine::y1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#y1
    """
    #  int QLine::y1() const
    return self.uglySide.call('ritual_ZNK5QLine2y1Ev')

  def x2(self) -> int:
    """
    Calls Qt's 'int QLine::x2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#x2
    """
    #  int QLine::x2() const
    return self.uglySide.call('ritual_ZNK5QLine2x2Ev')

  def y2(self) -> int:
    """
    Calls Qt's 'int QLine::y2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#y2
    """
    #  int QLine::y2() const
    return self.uglySide.call('ritual_ZNK5QLine2y2Ev')

  def dx(self) -> int:
    """
    Calls Qt's 'int QLine::dx() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#dx
    """
    #  int QLine::dx() const
    return self.uglySide.call('ritual_ZNK5QLine2dxEv')

  def dy(self) -> int:
    """
    Calls Qt's 'int QLine::dy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#dy
    """
    #  int QLine::dy() const
    return self.uglySide.call('ritual_ZNK5QLine2dyEv')

  @overload(QPoint)
  def translated(self, p: QPoint) -> QLine:
    """
    Calls Qt's 'QLine QLine::translated(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#translated

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QLine
      A new cute QLine around the copy Qt gave back. Python owns it.
    """
    #  QLine QLine::translated(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK5QLine10translatedERK6QPoint', self._valueOf(p),
    )
    return QLine._cuteOwning(address)

  @overload(int, int)
  def translated(self, dx: int, dy: int) -> QLine:
    """
    Calls Qt's 'QLine QLine::translated(int dx, int dy) const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#translated

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    Returns
    -------

    QLine
      A new cute QLine around the copy Qt gave back. Python owns it.
    """
    #  QLine QLine::translated(int dx, int dy) const
    address = self.uglySide.call('ritual_ZNK5QLine10translatedEii', dx, dy)
    return QLine._cuteOwning(address)

  def center(self) -> QPoint:
    """
    Calls Qt's 'QPoint QLine::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#center

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QLine::center() const
    address = self.uglySide.call('ritual_ZNK5QLine6centerEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  def toLineF(self) -> QLineF:
    """
    Calls Qt's 'QLineF QLine::toLineF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#toLineF

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QLine::toLineF() const
    address = self.uglySide.call('ritual_ZNK5QLine7toLineFEv')
    from . import QLineF
    return QLineF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def setP1(self, p1: QPoint) -> None:
    """
    Calls Qt's 'void QLine::setP1(const QPoint &p1)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#setP1

    Parameters
    ----------

    p1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QLine::setP1(const QPoint &p1)
    self.uglySide.call('ritual_ZN5QLine5setP1ERK6QPoint', self._valueOf(p1))

  @overload(QPoint)
  def setP2(self, p2: QPoint) -> None:
    """
    Calls Qt's 'void QLine::setP2(const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#setP2

    Parameters
    ----------

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QLine::setP2(const QPoint &p2)
    self.uglySide.call('ritual_ZN5QLine5setP2ERK6QPoint', self._valueOf(p2))

  @overload(QPoint, QPoint)
  def setPoints(self, p1: QPoint, p2: QPoint) -> None:
    """
    Calls Qt's 'void QLine::setPoints(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#setPoints

    Parameters
    ----------

    p1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QLine::setPoints(const QPoint &p1, const QPoint &p2)
    self.uglySide.call(
        'ritual_ZN5QLine9setPointsERK6QPointS2_',
        self._valueOf(p1), self._valueOf(p2),
    )

  @overload(int, int, int, int)
  def setLine(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QLine::setLine(int x1, int y1, int x2, int y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#setLine

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
    #  void QLine::setLine(int x1, int y1, int x2, int y2)
    self.uglySide.call('ritual_ZN5QLine7setLineEiiii', x1, y1, x2, y2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QLine) -> bool:
    """
    Calls Qt's 'bool operator==(const QLine &lhs, const QLine &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#operator==

    Parameters
    ----------

    rhs : QLine
      Passed on as a value: Qt reads the C++ QLine, which stays Python's own.
    """
    #  bool operator==(const QLine &lhs, const QLine &rhs)
    return Rituals.call(
        'ritual_ZeqRK5QLineS1_',
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
  def __ne__(self, rhs: QLine) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLine &lhs, const QLine &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#operator!=

    Parameters
    ----------

    rhs : QLine
      Passed on as a value: Qt reads the C++ QLine, which stays Python's own.
    """
    #  bool operator!=(const QLine &lhs, const QLine &rhs)
    return Rituals.call(
        'ritual_ZneRK5QLineS1_',
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
    Notes what was given, for Qt's 'QLine::QLine()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#QLine
    """
    #  QLine::QLine()
    self._noteCreation(QLine, lambda: Rituals.call('ritual_ZN5QLineC1Ev'))

  @overload(QPoint, QPoint)
  def __init__(self, pt1: QPoint, pt2: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QLine::QLine(const QPoint &pt1, const
    QPoint &pt2)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#QLine

    Parameters
    ----------

    pt1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    pt2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QLine::QLine(const QPoint &pt1, const QPoint &pt2)
    self._noteCreation(QLine, lambda: Rituals.call(
        'ritual_ZN5QLineC1ERK6QPointS2_',
        self._valueOf(pt1), self._valueOf(pt2),
    ))

  @overload(int, int, int, int)
  def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Notes what was given, for Qt's 'QLine::QLine(int x1, int y1, int x2, int
    y2)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#QLine

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
    #  QLine::QLine(int x1, int y1, int x2, int y2)
    self._noteCreation(QLine, lambda: Rituals.call(
        'ritual_ZN5QLineC1Eiiii', x1, y1, x2, y2,
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

  @overload(QPoint)
  def translate(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QLine::translate(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#translate

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QLine::translate(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN5QLine9translateERK6QPoint', self._valueOf(p),
    )

  @overload(int, int)
  def translate(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QLine::translate(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qline.html#translate

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QLine::translate(int dx, int dy)
    self.uglySide.call('ritual_ZN5QLine9translateEii', dx, dy)
