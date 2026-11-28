"""
QQuickDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDrag to be private: it declares the class in a header it
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
  from . import QQuickDragAttached, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDrag(QObject):
  """
  The cute side of Qt's QQuickDrag: a plain Python object standing in front
  of one C++ QQuickDrag.

  It is built on the cute 'QObject', as Qt's QQuickDrag is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDrag that has a ritual and that Python can
  call so far, 35 names in all: 'metaObject', 'tr', 'target', 'setTarget',
  'resetTarget', 'axis', 'setAxis', 'xmin', 'setXmin', 'xmax', 'setXmax',
  'ymin', 'setYmin', 'ymax', 'setYmax', 'smoothed', 'setSmoothed',
  'threshold', 'setThreshold', 'resetThreshold', 'active', 'setActive',
  'filterChildren', 'setFilterChildren', 'qmlAttachedProperties',
  'targetChanged', 'axisChanged', 'minimumXChanged', 'maximumXChanged',
  'minimumYChanged', 'maximumYChanged', 'activeChanged',
  'filterChildrenChanged', 'smoothedChanged', 'thresholdChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDrag::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickDrag::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDrag::qt_qmlMarker_uncreatable()': one of Qt's own inner
    workings.
  - Qt's 'void QQuickDrag::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'QQuickDrag::~QQuickDrag()': the destructor: Python never removes a
    C++ QQuickDrag.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDrag is created at the first use, not by 'QQuickDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDrag.
  - Qt tells when it has removed the C++ QQuickDrag. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickDrag, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Axis(CuteNum):
    """The enum 'QQuickDrag::Axis' of Qt, with the 4 names Qt gives in it."""

    XAxis = Kee[int](1)
    YAxis = Kee[int](2)
    XAndYAxis = Kee[int](3)
    XandYAxis = Kee[int](3)

  class DragType(CuteNum):
    """
    The enum 'QQuickDrag::DragType' of Qt, with the 3 names Qt gives in it.
    """

    NULL = Kee[int](0)
    Automatic = Kee[int](1)
    Internal = Kee[int](2)

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
    Calls Qt's 'QString QQuickDrag::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#tr

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
    #  QString QQuickDrag::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickDrag2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQuickDragAttached]:
    """
    Calls Qt's 'QQuickDragAttached *QQuickDrag::qmlAttachedProperties(QObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrag.html#qmlAttachedProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDragAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAttached *QQuickDrag::qmlAttachedProperties(QObject *obj)
    address = Rituals.call(
        'ritual_ZN10QQuickDrag21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    from . import QQuickDragAttached
    return QQuickDragAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDrag'

  #  A C++ QQuickDrag Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDrag'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDrag::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDrag::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickDrag10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickDrag::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDrag::target() const
    address = self.uglySide.call('ritual_ZNK10QQuickDrag6targetEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def axis(self) -> Axis:
    """
    Calls Qt's 'Axis QQuickDrag::axis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#axis

    Returns
    -------

    Axis
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Axis(number)' gives.
    """
    #  Axis QQuickDrag::axis() const
    return QQuickDrag.Axis(self.uglySide.call(
        'ritual_ZNK10QQuickDrag4axisEv',
    ))

  def xmin(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrag::xmin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#xmin
    """
    #  qreal QQuickDrag::xmin() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag4xminEv')

  def xmax(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrag::xmax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#xmax
    """
    #  qreal QQuickDrag::xmax() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag4xmaxEv')

  def ymin(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrag::ymin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#ymin
    """
    #  qreal QQuickDrag::ymin() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag4yminEv')

  def ymax(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrag::ymax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#ymax
    """
    #  qreal QQuickDrag::ymax() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag4ymaxEv')

  def smoothed(self) -> bool:
    """
    Calls Qt's 'bool QQuickDrag::smoothed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#smoothed
    """
    #  bool QQuickDrag::smoothed() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag8smoothedEv')

  def threshold(self) -> float:
    """
    Calls Qt's 'qreal QQuickDrag::threshold() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#threshold
    """
    #  qreal QQuickDrag::threshold() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag9thresholdEv')

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuickDrag::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#active
    """
    #  bool QQuickDrag::active() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag6activeEv')

  def filterChildren(self) -> bool:
    """
    Calls Qt's 'bool QQuickDrag::filterChildren() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#filterChildren
    """
    #  bool QQuickDrag::filterChildren() const
    return self.uglySide.call('ritual_ZNK10QQuickDrag14filterChildrenEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDrag::setTarget(QQuickItem *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setTarget

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDrag::setTarget(QQuickItem *target)
    self.uglySide.call(
        'ritual_ZN10QQuickDrag9setTargetEP10QQuickItem',
        self._addressOf(target),
    )

  @overload(Axis)
  def setAxis(self, a0: Axis) -> None:
    """
    Calls Qt's 'void QQuickDrag::setAxis(Axis a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setAxis

    Parameters
    ----------

    a0 : Axis
      Passed on as its number.
    """
    #  void QQuickDrag::setAxis(Axis a0)
    self.uglySide.call('ritual_ZN10QQuickDrag7setAxisENS_4AxisE', a0.value)

  @overload(float)
  def setXmin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickDrag::setXmin(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setXmin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickDrag::setXmin(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickDrag7setXminEd', a0)

  @overload(float)
  def setXmax(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickDrag::setXmax(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setXmax

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickDrag::setXmax(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickDrag7setXmaxEd', a0)

  @overload(float)
  def setYmin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickDrag::setYmin(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setYmin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickDrag::setYmin(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickDrag7setYminEd', a0)

  @overload(float)
  def setYmax(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickDrag::setYmax(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setYmax

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickDrag::setYmax(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickDrag7setYmaxEd', a0)

  @overload(bool)
  def setSmoothed(self, smooth: bool) -> None:
    """
    Calls Qt's 'void QQuickDrag::setSmoothed(bool smooth)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setSmoothed

    Parameters
    ----------

    smooth : bool
      Passed on as it is.
    """
    #  void QQuickDrag::setSmoothed(bool smooth)
    self.uglySide.call('ritual_ZN10QQuickDrag11setSmoothedEb', smooth)

  @overload(float)
  def setThreshold(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickDrag::setThreshold(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setThreshold

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickDrag::setThreshold(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickDrag12setThresholdEd', a0)

  @overload(bool)
  def setActive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickDrag::setActive(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setActive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickDrag::setActive(bool a0)
    self.uglySide.call('ritual_ZN10QQuickDrag9setActiveEb', a0)

  @overload(bool)
  def setFilterChildren(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickDrag::setFilterChildren(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#setFilterChildren

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickDrag::setFilterChildren(bool a0)
    self.uglySide.call('ritual_ZN10QQuickDrag17setFilterChildrenEb', a0)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickDrag::QQuickDrag(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#QQuickDrag

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDrag::QQuickDrag(QObject *parent)
    self._noteCreation(QQuickDrag, lambda: Rituals.call(
        'ritual_ZN10QQuickDragC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QQuickDrag::resetTarget()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#resetTarget
    """
    #  void QQuickDrag::resetTarget()
    self.uglySide.call('ritual_ZN10QQuickDrag11resetTargetEv')

  def resetThreshold(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::resetThreshold()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#resetThreshold
    """
    #  void QQuickDrag::resetThreshold()
    self.uglySide.call('ritual_ZN10QQuickDrag14resetThresholdEv')

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::targetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#targetChanged
    """
    #  void QQuickDrag::targetChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag13targetChangedEv')

  def axisChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::axisChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#axisChanged
    """
    #  void QQuickDrag::axisChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag11axisChangedEv')

  def minimumXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::minimumXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#minimumXChanged
    """
    #  void QQuickDrag::minimumXChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag15minimumXChangedEv')

  def maximumXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::maximumXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#maximumXChanged
    """
    #  void QQuickDrag::maximumXChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag15maximumXChangedEv')

  def minimumYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::minimumYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#minimumYChanged
    """
    #  void QQuickDrag::minimumYChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag15minimumYChangedEv')

  def maximumYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::maximumYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#maximumYChanged
    """
    #  void QQuickDrag::maximumYChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag15maximumYChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#activeChanged
    """
    #  void QQuickDrag::activeChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag13activeChangedEv')

  def filterChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::filterChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdrag.html#filterChildrenChanged
    """
    #  void QQuickDrag::filterChildrenChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag21filterChildrenChangedEv')

  def smoothedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::smoothedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#smoothedChanged
    """
    #  void QQuickDrag::smoothedChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag15smoothedChangedEv')

  def thresholdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDrag::thresholdChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdrag.html#thresholdChanged
    """
    #  void QQuickDrag::thresholdChanged()
    self.uglySide.call('ritual_ZN10QQuickDrag16thresholdChangedEv')
