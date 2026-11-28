"""
QStroker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QStroker to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QStrokerOps

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QLineF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLineF = WAIT['QLineF']


class QStroker(QStrokerOps):
  """
  The cute side of Qt's QStroker: a plain Python object standing in front of
  one C++ QStroker.

  It is built on the cute 'QStrokerOps', as Qt's QStroker is built on Qt's
  QStrokerOps, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStroker that has a ritual and that Python can call
  so far, 21 names in all: 'setStrokeWidth', 'strokeWidth', 'setCapStyle',
  'capStyle', 'capStyleMode', 'setJoinStyle', 'joinStyle', 'joinStyleMode',
  'setMiterLimit', 'miterLimit', 'setForceOpen', 'forceOpen', 'joinPoints',
  'emitMoveTo', 'emitLineTo', 'emitCubicTo', 'capForJoinMode',
  'joinModeForCap', 'joinForJoinMode', 'joinModeForJoin',
  'processCurrentSubpath'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStroker::~QStroker()': the destructor: Python never removes a C++
    QStroker.

  What to expect
  --------------

  - The C++ QStroker is created at the first use, not by 'QStroker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStroker.
  """

  #  The enums Qt writes inside QStroker, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class LineJoinMode(CuteNum):
    """
    The enum 'QStroker::LineJoinMode' of Qt, with the 6 names Qt gives in it.
    """

    FlatJoin = Kee[int](0)
    SquareJoin = Kee[int](1)
    MiterJoin = Kee[int](2)
    RoundJoin = Kee[int](3)
    RoundCap = Kee[int](4)
    SvgMiterJoin = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(LineJoinMode)
  def capForJoinMode(mode: LineJoinMode) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QStroker::capForJoinMode(LineJoinMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#capForJoinMode

    Parameters
    ----------

    mode : LineJoinMode
      Passed on as its number.

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QStroker::capForJoinMode(LineJoinMode mode)
    return Qt.PenCapStyle(Rituals.call(
        'ritual_ZN8QStroker14capForJoinModeENS_12LineJoinModeE', mode.value,
    ))

  @staticmethod
  @overload(Qt.PenCapStyle)
  def joinModeForCap(a0: Qt.PenCapStyle) -> LineJoinMode:
    """
    Calls Qt's 'LineJoinMode QStroker::joinModeForCap(Qt::PenCapStyle a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#joinModeForCap

    Parameters
    ----------

    a0 : Qt.PenCapStyle
      Passed on as its number.

    Returns
    -------

    LineJoinMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineJoinMode(number)'
      gives.
    """
    #  LineJoinMode QStroker::joinModeForCap(Qt::PenCapStyle a0)
    return QStroker.LineJoinMode(Rituals.call(
        'ritual_ZN8QStroker14joinModeForCapEN2Qt11PenCapStyleE', a0.value,
    ))

  @staticmethod
  @overload(LineJoinMode)
  def joinForJoinMode(mode: LineJoinMode) -> Qt.PenJoinStyle:
    """
    Calls Qt's 'Qt::PenJoinStyle QStroker::joinForJoinMode(LineJoinMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#joinForJoinMode

    Parameters
    ----------

    mode : LineJoinMode
      Passed on as its number.

    Returns
    -------

    Qt.PenJoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenJoinStyle(number)'
      gives.
    """
    #  Qt::PenJoinStyle QStroker::joinForJoinMode(LineJoinMode mode)
    return Qt.PenJoinStyle(Rituals.call(
        'ritual_ZN8QStroker15joinForJoinModeENS_12LineJoinModeE', mode.value,
    ))

  @staticmethod
  @overload(Qt.PenJoinStyle)
  def joinModeForJoin(joinStyle: Qt.PenJoinStyle) -> LineJoinMode:
    """
    Calls Qt's 'LineJoinMode QStroker::joinModeForJoin(Qt::PenJoinStyle
    joinStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#joinModeForJoin

    Parameters
    ----------

    joinStyle : Qt.PenJoinStyle
      Passed on as its number.

    Returns
    -------

    LineJoinMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineJoinMode(number)'
      gives.
    """
    #  LineJoinMode QStroker::joinModeForJoin(Qt::PenJoinStyle joinStyle)
    return QStroker.LineJoinMode(Rituals.call(
        'ritual_ZN8QStroker15joinModeForJoinEN2Qt12PenJoinStyleE',
        joinStyle.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStroker'

  #  A C++ QStroker Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStroker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def strokeWidth(self) -> float:
    """
    Calls Qt's 'qfixed QStroker::strokeWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#strokeWidth
    """
    #  qfixed QStroker::strokeWidth() const
    return self.uglySide.call('ritual_ZNK8QStroker11strokeWidthEv')

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QStroker::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QStroker::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZNK8QStroker8capStyleEv',
    ))

  def capStyleMode(self) -> LineJoinMode:
    """
    Calls Qt's 'LineJoinMode QStroker::capStyleMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#capStyleMode

    Returns
    -------

    LineJoinMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineJoinMode(number)'
      gives.
    """
    #  LineJoinMode QStroker::capStyleMode() const
    return QStroker.LineJoinMode(self.uglySide.call(
        'ritual_ZNK8QStroker12capStyleModeEv',
    ))

  def joinStyle(self) -> Qt.PenJoinStyle:
    """
    Calls Qt's 'Qt::PenJoinStyle QStroker::joinStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#joinStyle

    Returns
    -------

    Qt.PenJoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenJoinStyle(number)'
      gives.
    """
    #  Qt::PenJoinStyle QStroker::joinStyle() const
    return Qt.PenJoinStyle(self.uglySide.call(
        'ritual_ZNK8QStroker9joinStyleEv',
    ))

  def joinStyleMode(self) -> LineJoinMode:
    """
    Calls Qt's 'LineJoinMode QStroker::joinStyleMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#joinStyleMode

    Returns
    -------

    LineJoinMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineJoinMode(number)'
      gives.
    """
    #  LineJoinMode QStroker::joinStyleMode() const
    return QStroker.LineJoinMode(self.uglySide.call(
        'ritual_ZNK8QStroker13joinStyleModeEv',
    ))

  def miterLimit(self) -> float:
    """
    Calls Qt's 'qfixed QStroker::miterLimit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#miterLimit
    """
    #  qfixed QStroker::miterLimit() const
    return self.uglySide.call('ritual_ZNK8QStroker10miterLimitEv')

  def forceOpen(self) -> bool:
    """
    Calls Qt's 'bool QStroker::forceOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#forceOpen
    """
    #  bool QStroker::forceOpen() const
    return self.uglySide.call('ritual_ZNK8QStroker9forceOpenEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStrokeWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QStroker::setStrokeWidth(qfixed width)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#setStrokeWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QStroker::setStrokeWidth(qfixed width)
    self.uglySide.call('ritual_ZN8QStroker14setStrokeWidthEd', width)

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, capStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QStroker::setCapStyle(Qt::PenCapStyle capStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#setCapStyle

    Parameters
    ----------

    capStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QStroker::setCapStyle(Qt::PenCapStyle capStyle)
    self.uglySide.call(
        'ritual_ZN8QStroker11setCapStyleEN2Qt11PenCapStyleE', capStyle.value,
    )

  @overload(Qt.PenJoinStyle)
  def setJoinStyle(self, style: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void QStroker::setJoinStyle(Qt::PenJoinStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#setJoinStyle

    Parameters
    ----------

    style : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QStroker::setJoinStyle(Qt::PenJoinStyle style)
    self.uglySide.call(
        'ritual_ZN8QStroker12setJoinStyleEN2Qt12PenJoinStyleE', style.value,
    )

  @overload(float)
  def setMiterLimit(self, length: float) -> None:
    """
    Calls Qt's 'void QStroker::setMiterLimit(qfixed length)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#setMiterLimit

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void QStroker::setMiterLimit(qfixed length)
    self.uglySide.call('ritual_ZN8QStroker13setMiterLimitEd', length)

  @overload(bool)
  def setForceOpen(self, state: bool) -> None:
    """
    Calls Qt's 'void QStroker::setForceOpen(bool state)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#setForceOpen

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void QStroker::setForceOpen(bool state)
    self.uglySide.call('ritual_ZN8QStroker12setForceOpenEb', state)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStroker::QStroker()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#QStroker
    """
    #  QStroker::QStroker()
    self._noteCreation(QStroker, lambda: Rituals.call(
        'ritual_ZN8QStrokerC1Ev',
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

  @overload(float, float, QLineF, LineJoinMode)
  def joinPoints(
      self,
      x: float,
      y: float,
      nextLine: QLineF,
      join: LineJoinMode,
  ) -> None:
    """
    Calls Qt's 'void QStroker::joinPoints(qfixed x, qfixed y, const QLineF
    &nextLine, LineJoinMode join)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#joinPoints

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    nextLine : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.

    join : LineJoinMode
      Passed on as its number.
    """
    #  void QStroker::joinPoints(qfixed x, qfixed y, const QLineF &nextLine,
    #      LineJoinMode join)
    self.uglySide.call(
        'ritual_ZN8QStroker10joinPointsEddRK6QLineFNS_12LineJoinModeE',
        x, y, self._valueOf(nextLine), join.value,
    )

  @overload(float, float)
  def emitMoveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QStroker::emitMoveTo(qfixed x, qfixed y)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#emitMoveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QStroker::emitMoveTo(qfixed x, qfixed y)
    self.uglySide.call('ritual_ZN8QStroker10emitMoveToEdd', x, y)

  @overload(float, float)
  def emitLineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QStroker::emitLineTo(qfixed x, qfixed y)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#emitLineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QStroker::emitLineTo(qfixed x, qfixed y)
    self.uglySide.call('ritual_ZN8QStroker10emitLineToEdd', x, y)

  @overload(float, float, float, float, float, float)
  def emitCubicTo(
      self,
      c1x: float,
      c1y: float,
      c2x: float,
      c2y: float,
      ex: float,
      ey: float,
  ) -> None:
    """
    Calls Qt's 'void QStroker::emitCubicTo(qfixed c1x, qfixed c1y, qfixed
    c2x, qfixed c2y, qfixed ex, qfixed ey)'.

    Qt's own words: https://doc.qt.io/qt-6/qstroker.html#emitCubicTo

    Parameters
    ----------

    c1x : float
      Passed on as it is.

    c1y : float
      Passed on as it is.

    c2x : float
      Passed on as it is.

    c2y : float
      Passed on as it is.

    ex : float
      Passed on as it is.

    ey : float
      Passed on as it is.
    """
    #  void QStroker::emitCubicTo(qfixed c1x, qfixed c1y, qfixed c2x, qfixed
    #      c2y, qfixed ex, qfixed ey)
    self.uglySide.call(
        'ritual_ZN8QStroker11emitCubicToEdddddd', c1x, c1y, c2x, c2y, ex, ey,
    )

  def processCurrentSubpath(self) -> None:
    """
    Calls Qt's 'void QStroker::processCurrentSubpath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstroker.html#processCurrentSubpath
    """
    #  void QStroker::processCurrentSubpath()
    ritual = 'ritual_ZN8QStroker21processCurrentSubpathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QStroker21processCurrentSubpathEv'
    self.uglySide.call(ritual)
