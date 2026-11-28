"""
QQuickPinch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPinch to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPinch(QObject):
  """
  The cute side of Qt's QQuickPinch: a plain Python object standing in front
  of one C++ QQuickPinch.

  It is built on the cute 'QObject', as Qt's QQuickPinch is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPinch that has a ritual and that Python can
  call so far, 36 names in all: 'metaObject', 'tr', 'target', 'setTarget',
  'resetTarget', 'minimumScale', 'setMinimumScale', 'maximumScale',
  'setMaximumScale', 'minimumRotation', 'setMinimumRotation',
  'maximumRotation', 'setMaximumRotation', 'axis', 'setAxis', 'xmin',
  'setXmin', 'xmax', 'setXmax', 'ymin', 'setYmin', 'ymax', 'setYmax',
  'active', 'setActive', 'targetChanged', 'minimumScaleChanged',
  'maximumScaleChanged', 'minimumRotationChanged', 'maximumRotationChanged',
  'dragAxisChanged', 'minimumXChanged', 'maximumXChanged', 'minimumYChanged',
  'maximumYChanged', 'activeChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPinch::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPinch::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPinch is created at the first use, not by
    'QQuickPinch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPinch.
  - Qt tells when it has removed the C++ QQuickPinch. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickPinch, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Axis(CuteNum):
    """
    The enum 'QQuickPinch::Axis' of Qt, with the 5 names Qt gives in it.
    """

    NoDrag = Kee[int](0)
    XAxis = Kee[int](1)
    YAxis = Kee[int](2)
    XAndYAxis = Kee[int](3)
    XandYAxis = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickPinch::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPinch::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickPinch2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPinch'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPinch::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPinch::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickPinch10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPinch::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPinch::target() const
    address = self.uglySide.call('ritual_ZNK11QQuickPinch6targetEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def minimumScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::minimumScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#minimumScale
    """
    #  qreal QQuickPinch::minimumScale() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch12minimumScaleEv')

  def maximumScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::maximumScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#maximumScale
    """
    #  qreal QQuickPinch::maximumScale() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch12maximumScaleEv')

  def minimumRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::minimumRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#minimumRotation
    """
    #  qreal QQuickPinch::minimumRotation() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch15minimumRotationEv')

  def maximumRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::maximumRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#maximumRotation
    """
    #  qreal QQuickPinch::maximumRotation() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch15maximumRotationEv')

  def axis(self) -> Axis:
    """
    Calls Qt's 'Axis QQuickPinch::axis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#axis

    Returns
    -------

    Axis
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Axis(number)' gives.
    """
    #  Axis QQuickPinch::axis() const
    return QQuickPinch.Axis(self.uglySide.call(
        'ritual_ZNK11QQuickPinch4axisEv',
    ))

  def xmin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::xmin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#xmin
    """
    #  qreal QQuickPinch::xmin() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch4xminEv')

  def xmax(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::xmax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#xmax
    """
    #  qreal QQuickPinch::xmax() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch4xmaxEv')

  def ymin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::ymin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#ymin
    """
    #  qreal QQuickPinch::ymin() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch4yminEv')

  def ymax(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinch::ymax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#ymax
    """
    #  qreal QQuickPinch::ymax() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch4ymaxEv')

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuickPinch::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#active
    """
    #  bool QQuickPinch::active() const
    return self.uglySide.call('ritual_ZNK11QQuickPinch6activeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPinch::setTarget(QQuickItem *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setTarget

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinch::setTarget(QQuickItem *target)
    self.uglySide.call(
        'ritual_ZN11QQuickPinch9setTargetEP10QQuickItem',
        self._addressOf(target),
    )

  @overload(float)
  def setMinimumScale(self, s: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setMinimumScale(qreal s)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setMinimumScale

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QQuickPinch::setMinimumScale(qreal s)
    self.uglySide.call('ritual_ZN11QQuickPinch15setMinimumScaleEd', s)

  @overload(float)
  def setMaximumScale(self, s: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setMaximumScale(qreal s)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setMaximumScale

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QQuickPinch::setMaximumScale(qreal s)
    self.uglySide.call('ritual_ZN11QQuickPinch15setMaximumScaleEd', s)

  @overload(float)
  def setMinimumRotation(self, r: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setMinimumRotation(qreal r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinch.html#setMinimumRotation

    Parameters
    ----------

    r : float
      Passed on as it is.
    """
    #  void QQuickPinch::setMinimumRotation(qreal r)
    self.uglySide.call('ritual_ZN11QQuickPinch18setMinimumRotationEd', r)

  @overload(float)
  def setMaximumRotation(self, r: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setMaximumRotation(qreal r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinch.html#setMaximumRotation

    Parameters
    ----------

    r : float
      Passed on as it is.
    """
    #  void QQuickPinch::setMaximumRotation(qreal r)
    self.uglySide.call('ritual_ZN11QQuickPinch18setMaximumRotationEd', r)

  @overload(Axis)
  def setAxis(self, a: Axis) -> None:
    """
    Calls Qt's 'void QQuickPinch::setAxis(Axis a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setAxis

    Parameters
    ----------

    a : Axis
      Passed on as its number.
    """
    #  void QQuickPinch::setAxis(Axis a)
    self.uglySide.call('ritual_ZN11QQuickPinch7setAxisENS_4AxisE', a.value)

  @overload(float)
  def setXmin(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setXmin(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setXmin

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPinch::setXmin(qreal x)
    self.uglySide.call('ritual_ZN11QQuickPinch7setXminEd', x)

  @overload(float)
  def setXmax(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setXmax(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setXmax

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPinch::setXmax(qreal x)
    self.uglySide.call('ritual_ZN11QQuickPinch7setXmaxEd', x)

  @overload(float)
  def setYmin(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setYmin(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setYmin

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPinch::setYmin(qreal y)
    self.uglySide.call('ritual_ZN11QQuickPinch7setYminEd', y)

  @overload(float)
  def setYmax(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPinch::setYmax(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setYmax

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPinch::setYmax(qreal y)
    self.uglySide.call('ritual_ZN11QQuickPinch7setYmaxEd', y)

  @overload(bool)
  def setActive(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuickPinch::setActive(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#setActive

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuickPinch::setActive(bool a)
    self.uglySide.call('ritual_ZN11QQuickPinch9setActiveEb', a)

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
    Notes what was given, for Qt's 'QQuickPinch::QQuickPinch()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#QQuickPinch
    """
    #  QQuickPinch::QQuickPinch()
    self._noteCreation(QQuickPinch, lambda: Rituals.call(
        'ritual_ZN11QQuickPinchC1Ev',
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

  def resetTarget(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::resetTarget()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#resetTarget
    """
    #  void QQuickPinch::resetTarget()
    self.uglySide.call('ritual_ZN11QQuickPinch11resetTargetEv')

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::targetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#targetChanged
    """
    #  void QQuickPinch::targetChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch13targetChangedEv')

  def minimumScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::minimumScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinch.html#minimumScaleChanged
    """
    #  void QQuickPinch::minimumScaleChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch19minimumScaleChangedEv')

  def maximumScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::maximumScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinch.html#maximumScaleChanged
    """
    #  void QQuickPinch::maximumScaleChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch19maximumScaleChangedEv')

  def minimumRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::minimumRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinch.html#minimumRotationChanged
    """
    #  void QQuickPinch::minimumRotationChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch22minimumRotationChangedEv')

  def maximumRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::maximumRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinch.html#maximumRotationChanged
    """
    #  void QQuickPinch::maximumRotationChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch22maximumRotationChangedEv')

  def dragAxisChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::dragAxisChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#dragAxisChanged
    """
    #  void QQuickPinch::dragAxisChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch15dragAxisChangedEv')

  def minimumXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::minimumXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#minimumXChanged
    """
    #  void QQuickPinch::minimumXChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch15minimumXChangedEv')

  def maximumXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::maximumXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#maximumXChanged
    """
    #  void QQuickPinch::maximumXChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch15maximumXChangedEv')

  def minimumYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::minimumYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#minimumYChanged
    """
    #  void QQuickPinch::minimumYChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch15minimumYChangedEv')

  def maximumYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::maximumYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#maximumYChanged
    """
    #  void QQuickPinch::maximumYChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch15maximumYChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinch::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinch.html#activeChanged
    """
    #  void QQuickPinch::activeChanged()
    self.uglySide.call('ritual_ZN11QQuickPinch13activeChangedEv')
