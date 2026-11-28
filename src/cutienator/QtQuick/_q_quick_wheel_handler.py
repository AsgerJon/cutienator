"""
QQuickWheelHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickWheelHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickSinglePointHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QTimerEvent
  from ..QtGui import QPointerEvent
  from . import QQuickItem, QQuickWheelEvent, QQuickWheelHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']
  QQuickWheelEvent = WAIT['QQuickWheelEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWheelHandler(QQuickSinglePointHandler):
  """
  The cute side of Qt's QQuickWheelHandler: a plain Python object standing in
  front of one C++ QQuickWheelHandler.

  It is built on the cute 'QQuickSinglePointHandler', as Qt's
  QQuickWheelHandler is built on Qt's QQuickSinglePointHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWheelHandler that has a ritual and that Python
  can call so far, 35 names in all: 'metaObject', 'tr', 'orientation',
  'setOrientation', 'isInvertible', 'setInvertible', 'activeTimeout',
  'setActiveTimeout', 'rotation', 'setRotation', 'rotationScale',
  'setRotationScale', 'property', 'setProperty', 'targetScaleMultiplier',
  'setTargetScaleMultiplier', 'isTargetTransformAroundCursor',
  'setTargetTransformAroundCursor', 'isBlocking', 'setBlocking', 'wheel',
  'orientationChanged', 'invertibleChanged', 'activeTimeoutChanged',
  'rotationChanged', 'rotationScaleChanged', 'propertyChanged',
  'targetScaleMultiplierChanged', 'targetTransformAroundCursorChanged',
  'blockingChanged', 'wantsPointerEvent', 'onTargetChanged',
  'onActiveChanged', 'timerEvent', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWheelHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickWheelHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWheelHandler::handleEventPoint(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickWheelHandlerPrivate *QQuickWheelHandler::d_func()
    const': takes in Python what 'QQuickWheelHandlerPrivate
    *QQuickWheelHandler::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 42 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWheelHandler is created at the first use, not by
    'QQuickWheelHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWheelHandler.
  - Qt tells when it has removed the C++ QQuickWheelHandler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQuickWheelHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#tr

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
    #  QString QQuickWheelHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickWheelHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWheelHandler'

  #  A C++ QQuickWheelHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWheelHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWheelHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWheelHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickWheelHandler::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickWheelHandler::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler11orientationEv',
    ))

  def isInvertible(self) -> bool:
    """
    Calls Qt's 'bool QQuickWheelHandler::isInvertible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#isInvertible
    """
    #  bool QQuickWheelHandler::isInvertible() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler12isInvertibleEv',
    )

  def activeTimeout(self) -> float:
    """
    Calls Qt's 'qreal QQuickWheelHandler::activeTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#activeTimeout
    """
    #  qreal QQuickWheelHandler::activeTimeout() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler13activeTimeoutEv',
    )

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickWheelHandler::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#rotation
    """
    #  qreal QQuickWheelHandler::rotation() const
    return self.uglySide.call('ritual_ZNK18QQuickWheelHandler8rotationEv')

  def rotationScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickWheelHandler::rotationScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#rotationScale
    """
    #  qreal QQuickWheelHandler::rotationScale() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler13rotationScaleEv',
    )

  def property(self) -> str:
    """
    Calls Qt's 'QString QQuickWheelHandler::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWheelHandler::property() const
    return self.uglySide.call('ritual_ZNK18QQuickWheelHandler8propertyEv')

  def targetScaleMultiplier(self) -> float:
    """
    Calls Qt's 'qreal QQuickWheelHandler::targetScaleMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#targetScaleMultiplier
    """
    #  qreal QQuickWheelHandler::targetScaleMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler21targetScaleMultiplierEv',
    )

  def isTargetTransformAroundCursor(self) -> bool:
    """
    Calls Qt's 'bool QQuickWheelHandler::isTargetTransformAroundCursor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html
    """
    #  bool QQuickWheelHandler::isTargetTransformAroundCursor() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickWheelHandler29isTargetTransformAroundCursorEv',
    )

  def isBlocking(self) -> bool:
    """
    Calls Qt's 'bool QQuickWheelHandler::isBlocking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#isBlocking
    """
    #  bool QQuickWheelHandler::isBlocking() const
    return self.uglySide.call('ritual_ZNK18QQuickWheelHandler10isBlockingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickWheelHandler::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(bool)
  def setInvertible(self, invertible: bool) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setInvertible(bool invertible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setInvertible

    Parameters
    ----------

    invertible : bool
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setInvertible(bool invertible)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler13setInvertibleEb', invertible,
    )

  @overload(float)
  def setActiveTimeout(self, timeout: float) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setActiveTimeout(qreal timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setActiveTimeout

    Parameters
    ----------

    timeout : float
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setActiveTimeout(qreal timeout)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler16setActiveTimeoutEd', timeout,
    )

  @overload(float)
  def setRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setRotation(qreal rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setRotation(qreal rotation)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler11setRotationEd', rotation,
    )

  @overload(float)
  def setRotationScale(self, rotationScale: float) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setRotationScale(qreal
    rotationScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setRotationScale

    Parameters
    ----------

    rotationScale : float
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setRotationScale(qreal rotationScale)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler16setRotationScaleEd', rotationScale,
    )

  @overload(str)
  def setProperty(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setProperty(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWheelHandler::setProperty(const QString &name)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler11setPropertyERK7QString', name,
    )

  @overload(float)
  def setTargetScaleMultiplier(self, targetScaleMultiplier: float) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setTargetScaleMultiplier(qreal
    targetScaleMultiplier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setTargetScaleMultiplier

    Parameters
    ----------

    targetScaleMultiplier : float
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setTargetScaleMultiplier(qreal
    #      targetScaleMultiplier)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler24setTargetScaleMultiplierEd',
        targetScaleMultiplier,
    )

  @overload(bool)
  def setTargetTransformAroundCursor(self, ttac: bool) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setTargetTransformAroundCursor(bool
    ttac)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html

    Parameters
    ----------

    ttac : bool
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setTargetTransformAroundCursor(bool ttac)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler30setTargetTransformAroundCursorEb',
        ttac,
    )

  @overload(bool)
  def setBlocking(self, blocking: bool) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::setBlocking(bool blocking)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#setBlocking

    Parameters
    ----------

    blocking : bool
      Passed on as it is.
    """
    #  void QQuickWheelHandler::setBlocking(bool blocking)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler11setBlockingEb', blocking,
    )

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWheelHandler::QQuickWheelHandler(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#QQuickWheelHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWheelHandler::QQuickWheelHandler(QQuickItem *parent)
    self._noteCreation(QQuickWheelHandler, lambda: Rituals.call(
        'ritual_ZN18QQuickWheelHandlerC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QQuickWheelEvent)
  @overload(NoneType)
  def wheel(self, event: Optional[QQuickWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::wheel(QQuickWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#wheel

    Parameters
    ----------

    event : Optional[QQuickWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWheelHandler::wheel(QQuickWheelEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler5wheelEP16QQuickWheelEvent',
        self._addressOf(event),
    )

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#orientationChanged
    """
    #  void QQuickWheelHandler::orientationChanged()
    self.uglySide.call('ritual_ZN18QQuickWheelHandler18orientationChangedEv')

  def invertibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::invertibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#invertibleChanged
    """
    #  void QQuickWheelHandler::invertibleChanged()
    self.uglySide.call('ritual_ZN18QQuickWheelHandler17invertibleChangedEv')

  def activeTimeoutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::activeTimeoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#activeTimeoutChanged
    """
    #  void QQuickWheelHandler::activeTimeoutChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler20activeTimeoutChangedEv',
    )

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#rotationChanged
    """
    #  void QQuickWheelHandler::rotationChanged()
    self.uglySide.call('ritual_ZN18QQuickWheelHandler15rotationChangedEv')

  def rotationScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::rotationScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#rotationScaleChanged
    """
    #  void QQuickWheelHandler::rotationScaleChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler20rotationScaleChangedEv',
    )

  def propertyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::propertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#propertyChanged
    """
    #  void QQuickWheelHandler::propertyChanged()
    self.uglySide.call('ritual_ZN18QQuickWheelHandler15propertyChangedEv')

  def targetScaleMultiplierChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::targetScaleMultiplierChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html
    """
    #  void QQuickWheelHandler::targetScaleMultiplierChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler28targetScaleMultiplierChangedEv',
    )

  def targetTransformAroundCursorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWheelHandler::targetTransformAroundCursorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html
    """
    #  void QQuickWheelHandler::targetTransformAroundCursorChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickWheelHandler34targetTransformAroundCursorChangedE'
        'v',
    )

  def blockingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::blockingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#blockingChanged
    """
    #  void QQuickWheelHandler::blockingChanged()
    self.uglySide.call('ritual_ZN18QQuickWheelHandler15blockingChangedEv')

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickWheelHandler::wantsPointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWheelHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN18QQuickWheelHandler17wantsPointerEventEP13QPointerEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickWheelHandler17wantsPointerEventEP13QPointer'
          'Event')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem)
  @overload(NoneType)
  def onTargetChanged(self, oldTarget: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::onTargetChanged(QQuickItem
    *oldTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#onTargetChanged

    Parameters
    ----------

    oldTarget : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWheelHandler::onTargetChanged(QQuickItem *oldTarget)
    ritual = 'ritual_ZN18QQuickWheelHandler15onTargetChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickWheelHandler15onTargetChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(oldTarget))

  def onActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::onActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwheelhandler.html#onActiveChanged
    """
    #  void QQuickWheelHandler::onActiveChanged()
    ritual = 'ritual_ZN18QQuickWheelHandler15onActiveChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickWheelHandler15onActiveChangedEv'
    self.uglySide.call(ritual)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickWheelHandler::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWheelHandler::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN18QQuickWheelHandler10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickWheelHandler10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickWheelHandlerPrivate]:
    """
    Calls Qt's 'QQuickWheelHandlerPrivate *QQuickWheelHandler::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwheelhandler.html#d_func

    Returns
    -------

    Optional[QQuickWheelHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWheelHandlerPrivate *QQuickWheelHandler::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickWheelHandler6d_funcEv')
    from . import QQuickWheelHandlerPrivate
    return QQuickWheelHandlerPrivate._cuteAt(address)
