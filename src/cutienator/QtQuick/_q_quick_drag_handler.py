"""
QQuickDragHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdraghandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickDragHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtGui import QPointingDevice
from . import QQuickMultiPointHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QPointerEvent, QVector2D
  from . import QQuickDragAxis, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDragHandler(QQuickMultiPointHandler):
  """
  The cute side of Qt's QQuickDragHandler: a plain Python object standing in
  front of one C++ QQuickDragHandler.

  It is built on the cute 'QQuickMultiPointHandler', as Qt's
  QQuickDragHandler is built on Qt's QQuickMultiPointHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDragHandler that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr',
  'handlePointerEventImpl', 'xAxis', 'yAxis', 'translation',
  'activeTranslation', 'setActiveTranslation', 'persistentTranslation',
  'setPersistentTranslation', 'snapMode', 'setSnapMode',
  'translationChanged', 'snapModeChanged', 'wantsPointerEvent',
  'onActiveChanged', 'enforceAxisConstraints', 'targetCentroidPosition'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDragHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickDragHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDragHandler::onGrabChanged(QQuickPointerHandler
    *grabber, QPointingDevice::GrabTransition transition, QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickDragHandler is created at the first use, not by
    'QQuickDragHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDragHandler.
  - Qt tells when it has removed the C++ QQuickDragHandler. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickDragHandler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SnapMode(CuteNum):
    """
    The enum 'QQuickDragHandler::SnapMode' of Qt, with the 4 names Qt gives
    in it.
    """

    NoSnap = Kee[int](0)
    SnapAuto = Kee[int](1)
    SnapIfPressedOutsideTarget = Kee[int](2)
    SnapAlways = Kee[int](3)

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
    Calls Qt's 'QString QQuickDragHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#tr

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
    #  QString QQuickDragHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickDragHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDragHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDragHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDragHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickDragHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def translation(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickDragHandler::translation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#translation

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickDragHandler::translation() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickDragHandler11translationEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def activeTranslation(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickDragHandler::activeTranslation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#activeTranslation

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickDragHandler::activeTranslation() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickDragHandler17activeTranslationEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def persistentTranslation(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickDragHandler::persistentTranslation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#persistentTranslation

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickDragHandler::persistentTranslation() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickDragHandler21persistentTranslationEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'QQuickDragHandler::SnapMode QQuickDragHandler::snapMode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  QQuickDragHandler::SnapMode QQuickDragHandler::snapMode() const
    return QQuickDragHandler.SnapMode(self.uglySide.call(
        'ritual_ZNK17QQuickDragHandler8snapModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector2D)
  def setActiveTranslation(self, trans: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::setActiveTranslation(const QVector2D
    &trans)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#setActiveTranslation

    Parameters
    ----------

    trans : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickDragHandler::setActiveTranslation(const QVector2D &trans)
    self.uglySide.call(
        'ritual_ZN17QQuickDragHandler20setActiveTranslationERK9QVector2D',
        self._valueOf(trans),
    )

  @overload(QVector2D)
  def setPersistentTranslation(self, trans: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::setPersistentTranslation(const
    QVector2D &trans)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#setPersistentTranslation

    Parameters
    ----------

    trans : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickDragHandler::setPersistentTranslation(const QVector2D
    #      &trans)
    self.uglySide.call(
        'ritual_ZN17QQuickDragHandler24setPersistentTranslationERK9QVector2'
        'D',
        self._valueOf(trans),
    )

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void
    QQuickDragHandler::setSnapMode(QQuickDragHandler::SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickDragHandler::setSnapMode(QQuickDragHandler::SnapMode mode)
    self.uglySide.call(
        'ritual_ZN17QQuickDragHandler11setSnapModeENS_8SnapModeE',
        mode.value,
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
    'QQuickDragHandler::QQuickDragHandler(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#QQuickDragHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDragHandler::QQuickDragHandler(QQuickItem *parent)
    self._noteCreation(QQuickDragHandler, lambda: Rituals.call(
        'ritual_ZN17QQuickDragHandlerC1EP10QQuickItem',
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

  @overload(QPointerEvent)
  @overload(NoneType)
  def handlePointerEventImpl(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::handlePointerEventImpl(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#handlePointerEventImpl

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragHandler::handlePointerEventImpl(QPointerEvent *event)
    ritual = (
        'ritual_ZN17QQuickDragHandler22handlePointerEventImplEP13QPointerEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickDragHandler22handlePointerEventImplEP13QPoi'
          'nterEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def xAxis(self) -> Optional[QQuickDragAxis]:
    """
    Calls Qt's 'QQuickDragAxis *QQuickDragHandler::xAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#xAxis

    Returns
    -------

    Optional[QQuickDragAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAxis *QQuickDragHandler::xAxis()
    address = self.uglySide.call('ritual_ZN17QQuickDragHandler5xAxisEv')
    from . import QQuickDragAxis
    return QQuickDragAxis._cuteAt(address)

  def yAxis(self) -> Optional[QQuickDragAxis]:
    """
    Calls Qt's 'QQuickDragAxis *QQuickDragHandler::yAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraghandler.html#yAxis

    Returns
    -------

    Optional[QQuickDragAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAxis *QQuickDragHandler::yAxis()
    address = self.uglySide.call('ritual_ZN17QQuickDragHandler5yAxisEv')
    from . import QQuickDragAxis
    return QQuickDragAxis._cuteAt(address)

  @overload(QVector2D)
  def translationChanged(self, delta: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::translationChanged(QVector2D delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#translationChanged

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickDragHandler::translationChanged(QVector2D delta)
    self.uglySide.call(
        'ritual_ZN17QQuickDragHandler18translationChangedE9QVector2D',
        self._valueOf(delta),
    )

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::snapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#snapModeChanged
    """
    #  void QQuickDragHandler::snapModeChanged()
    self.uglySide.call('ritual_ZN17QQuickDragHandler15snapModeChangedEv')

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDragHandler::wantsPointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDragHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN17QQuickDragHandler17wantsPointerEventEP13QPointerEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickDragHandler17wantsPointerEventEP13QPointerE'
          'vent')
    return self.uglySide.call(ritual, self._addressOf(event))

  def onActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::onActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#onActiveChanged
    """
    #  void QQuickDragHandler::onActiveChanged()
    ritual = 'ritual_ZN17QQuickDragHandler15onActiveChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickDragHandler15onActiveChangedEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  @overload(NoneType)
  def enforceAxisConstraints(self, localPos: Optional[QPointF]) -> None:
    """
    Calls Qt's 'void QQuickDragHandler::enforceAxisConstraints(QPointF
    *localPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#enforceAxisConstraints

    Parameters
    ----------

    localPos : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragHandler::enforceAxisConstraints(QPointF *localPos)
    self.uglySide.call(
        'ritual_ZN17QQuickDragHandler22enforceAxisConstraintsEP7QPointF',
        self._addressOf(localPos, 'QPointF'),
    )

  def targetCentroidPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickDragHandler::targetCentroidPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraghandler.html#targetCentroidPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickDragHandler::targetCentroidPosition()
    address = self.uglySide.call(
        'ritual_ZN17QQuickDragHandler22targetCentroidPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)
