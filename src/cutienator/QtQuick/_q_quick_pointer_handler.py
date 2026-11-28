"""
QQuickPointerHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPointerHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QPointingDevice
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPointF
  from ..QtGui import QEventPoint, QPointerEvent
  from . import QQuickItem, QQuickPointerHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QEventPoint = WAIT['QEventPoint']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPointerHandler(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickPointerHandler: a plain Python object standing
  in front of one C++ QQuickPointerHandler.

  It is built on the cute 'QObject', as Qt's QQuickPointerHandler is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickPointerHandler is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPointerHandler that has a ritual and that
  Python can call so far, 48 names in all: 'metaObject', 'tr', 'enabled',
  'setEnabled', 'active', 'target', 'setTarget', 'parentItem',
  'setParentItem', 'handlePointerEvent', 'grabPermissions',
  'setGrabPermissions', 'margin', 'setMargin', 'dragThreshold',
  'setDragThreshold', 'resetDragThreshold', 'cursorShape', 'setCursorShape',
  'resetCursorShape', 'isCursorShapeExplicitlySet', 'enabledChanged',
  'activeChanged', 'targetChanged', 'marginChanged', 'dragThresholdChanged',
  'grabChanged', 'grabPermissionChanged', 'canceled', 'cursorShapeChanged',
  'parentChanged', 'classBegin', 'componentComplete', 'event',
  'currentEvent', 'wantsPointerEvent', 'wantsEventPoint',
  'handlePointerEventImpl', 'setActive', 'onTargetChanged',
  'onActiveChanged', 'canGrab', 'approveGrabTransition', 'setPassiveGrab',
  'setExclusiveGrab', 'eventPos', 'parentContains', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPointerHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPointerHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPointerHandler::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QQuickPointerHandler::~QQuickPointerHandler()': the destructor:
    Python never removes a C++ QQuickPointerHandler.
  - Qt's
    'QQuickPointerHandler::QQuickPointerHandler(QQuickPointerHandlerPrivate
    &dd, QQuickItem *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickPointerHandler::onGrabChanged(QQuickPointerHandler
    *grabber, QPointingDevice::GrabTransition transition, QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickPointerHandler::cancelAllGrabs(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickPointerHandlerPrivate *QQuickPointerHandler::d_func()
    const': takes in Python what 'QQuickPointerHandlerPrivate
    *QQuickPointerHandler::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 60 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPointerHandler is created at the first use, not by
    'QQuickPointerHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPointerHandler.
  - Qt tells when it has removed the C++ QQuickPointerHandler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPointerHandler that has no cute function yet,
    'cancelAllGrabs', 'onGrabChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickPointerHandler, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class GrabPermission(CuteFlags):
    """
    The flags enum 'QQuickPointerHandler::GrabPermission' of Qt, with the 10
    names Qt gives in it. Qt names the type of its combinations
    'QQuickPointerHandler::GrabPermissions'.
    """

    TakeOverForbidden = 0x0
    CanTakeOverFromHandlersOfSameType = 0x1
    CanTakeOverFromHandlersOfDifferentType = 0x2
    CanTakeOverFromItems = 0x4
    CanTakeOverFromAnything = 0xf
    ApprovesTakeOverByHandlersOfSameType = 0x10
    ApprovesTakeOverByHandlersOfDifferentType = 0x20
    ApprovesTakeOverByItems = 0x40
    ApprovesCancellation = 0x80
    ApprovesTakeOverByAnything = 0xf0

  GrabPermissions = GrabPermission

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
    Calls Qt's 'QString QQuickPointerHandler::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#tr

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
    #  QString QQuickPointerHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickPointerHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPointerHandler'

  #  Qt's QQuickPointerHandler is built on more than one class. The part of a
  #  C++ QQuickPointerHandler that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuickPointerHandler_QQmlParserStatus',
  }

  #  A C++ QQuickPointerHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPointerHandler'

  #  The functions Qt calls itself that QQuickPointerHandler is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'onGrabChanged': (
          'void QQuickPointerHandler::onGrabChanged(QQuickPointerHandler '
          '*, QPointingDevice::GrabTransition, QPointerEvent *, '
          'QEventPoint &)',
      ),
  }

  #  The functions Qt calls itself that QQuickPointerHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'wantsPointerEvent': (
          ('_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
           )),
      ),
      'wantsEventPoint': (
          ('_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK1'
           '1QEventPoint',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
               ('address', 'value', 'QtGui:QEventPoint'),
           )),
      ),
      'handlePointerEventImpl': (
          ('_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEv'
           'ent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
           )),
      ),
      'onTargetChanged': (
          ('_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'onActiveChanged': (
          ('_ZN20QQuickPointerHandler15onActiveChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'canGrab': (
          ('_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoi'
           'nt',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
               ('address', 'value', 'QtGui:QEventPoint'),
           )),
      ),
      'approveGrabTransition': (
          ('_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEve'
           'ntRK11QEventPointP7QObject',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
               ('address', 'value', 'QtGui:QEventPoint'),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPointerHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPointerHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#enabled
    """
    #  bool QQuickPointerHandler::enabled() const
    return self.uglySide.call('ritual_ZNK20QQuickPointerHandler7enabledEv')

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#active
    """
    #  bool QQuickPointerHandler::active() const
    return self.uglySide.call('ritual_ZNK20QQuickPointerHandler6activeEv')

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPointerHandler::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPointerHandler::target() const
    address = self.uglySide.call('ritual_ZNK20QQuickPointerHandler6targetEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def parentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPointerHandler::parentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#parentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPointerHandler::parentItem() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler10parentItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def grabPermissions(self) -> GrabPermissions:
    """
    Calls Qt's 'GrabPermissions QQuickPointerHandler::grabPermissions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#grabPermissions

    Returns
    -------

    GrabPermissions
      The value standing for the combination Qt gave back.
    """
    #  GrabPermissions QQuickPointerHandler::grabPermissions() const
    return QQuickPointerHandler.GrabPermissions(self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler15grabPermissionsEv',
    ))

  def margin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPointerHandler::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#margin
    """
    #  qreal QQuickPointerHandler::margin() const
    return self.uglySide.call('ritual_ZNK20QQuickPointerHandler6marginEv')

  def dragThreshold(self) -> int:
    """
    Calls Qt's 'int QQuickPointerHandler::dragThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#dragThreshold
    """
    #  int QQuickPointerHandler::dragThreshold() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler13dragThresholdEv',
    )

  def cursorShape(self) -> Qt.CursorShape:
    """
    Calls Qt's 'Qt::CursorShape QQuickPointerHandler::cursorShape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#cursorShape

    Returns
    -------

    Qt.CursorShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CursorShape(number)'
      gives.
    """
    #  Qt::CursorShape QQuickPointerHandler::cursorShape() const
    return Qt.CursorShape(self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler11cursorShapeEv',
    ))

  def isCursorShapeExplicitlySet(self) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::isCursorShapeExplicitlySet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html
    """
    #  bool QQuickPointerHandler::isCursorShapeExplicitlySet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler26isCursorShapeExplicitlySetEv',
    )

  @overload(QEventPoint)
  def eventPos(self, point: QEventPoint) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPointerHandler::eventPos(const QEventPoint
    &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#eventPos

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPointerHandler::eventPos(const QEventPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler8eventPosERK11QEventPoint',
        self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QEventPoint)
  def parentContains(self, point: QEventPoint) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::parentContains(const QEventPoint
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#parentContains

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPointerHandler::parentContains(const QEventPoint &point)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler14parentContainsERK11QEventPoint',
        self._valueOf(point),
    )

  @overload(QPointF, QPointF)
  def parentContains(
      self,
      localPosition: QPointF,
      scenePosition: QPointF,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::parentContains(const QPointF
    &localPosition, const QPointF &scenePosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#parentContains

    Parameters
    ----------

    localPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickPointerHandler::parentContains(const QPointF
    #      &localPosition, const QPointF &scenePosition) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPointerHandler14parentContainsERK7QPointFS2_',
        self._valueOf(localPosition, 'QPointF'), self._valueOf(scenePosition,
        'QPointF'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickPointerHandler::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler10setEnabledEb', enabled,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setTarget(QQuickItem *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setTarget

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPointerHandler::setTarget(QQuickItem *target)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler9setTargetEP10QQuickItem',
        self._addressOf(target),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setParentItem(self, p: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setParentItem(QQuickItem *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setParentItem

    Parameters
    ----------

    p : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPointerHandler::setParentItem(QQuickItem *p)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler13setParentItemEP10QQuickItem',
        self._addressOf(p),
    )

  @overload(GrabPermissions)
  def setGrabPermissions(self, grabPermissions: GrabPermissions) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setGrabPermissions(GrabPermissions
    grabPermissions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setGrabPermissions

    Parameters
    ----------

    grabPermissions : GrabPermissions
      Passed on as its number.
    """
    #  void QQuickPointerHandler::setGrabPermissions(GrabPermissions
    #      grabPermissions)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler18setGrabPermissionsE6QFlagsINS_14G'
        'rabPermissionEE',
        grabPermissions.value,
    )

  @overload(float)
  def setMargin(self, pointDistanceThreshold: float) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setMargin(qreal
    pointDistanceThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setMargin

    Parameters
    ----------

    pointDistanceThreshold : float
      Passed on as it is.
    """
    #  void QQuickPointerHandler::setMargin(qreal pointDistanceThreshold)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler9setMarginEd',
        pointDistanceThreshold,
    )

  @overload(int)
  def setDragThreshold(self, t: int) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setDragThreshold(int t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setDragThreshold

    Parameters
    ----------

    t : int
      Passed on as it is.
    """
    #  void QQuickPointerHandler::setDragThreshold(int t)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler16setDragThresholdEi', t,
    )

  @overload(Qt.CursorShape)
  def setCursorShape(self, shape: Qt.CursorShape) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setCursorShape(Qt::CursorShape
    shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setCursorShape

    Parameters
    ----------

    shape : Qt.CursorShape
      Passed on as its number.
    """
    #  void QQuickPointerHandler::setCursorShape(Qt::CursorShape shape)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler14setCursorShapeEN2Qt11CursorShapeE',
        shape.value,
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickPointerHandler::setActive(bool active)
    self.uglySide.call('ritual_ZN20QQuickPointerHandler9setActiveEb', active)

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  @overload(QPointerEvent, QEventPoint, bool)
  @overload(NoneType, QEventPoint, bool)
  def setPassiveGrab(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
      grab: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::setPassiveGrab(QPointerEvent
    *event, const QEventPoint &point, bool grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setPassiveGrab

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    grab : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickPointerHandler::setPassiveGrab(QPointerEvent *event, const
    #      QEventPoint &point, bool grab)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler14setPassiveGrabEP13QPointerEventRK'
        '11QEventPointb',
        self._addressOf(event), self._valueOf(point), grab,
    )

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  @overload(QPointerEvent, QEventPoint, bool)
  @overload(NoneType, QEventPoint, bool)
  def setExclusiveGrab(
      self,
      ev: Optional[QPointerEvent],
      point: QEventPoint,
      grab: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::setExclusiveGrab(QPointerEvent
    *ev, const QEventPoint &point, bool grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#setExclusiveGrab

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    grab : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QQuickPointerHandler::setExclusiveGrab(QPointerEvent *ev, const
    #      QEventPoint &point, bool grab)
    return self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler16setExclusiveGrabEP13QPointerEvent'
        'RK11QEventPointb',
        self._addressOf(ev), self._valueOf(point), grab,
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
    'QQuickPointerHandler::QQuickPointerHandler(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#QQuickPointerHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPointerHandler::QQuickPointerHandler(QQuickItem *parent)
    self._noteCreation(QQuickPointerHandler, lambda: Rituals.call(
        'ritual_ZN20QQuickPointerHandlerC1EP10QQuickItem',
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
  def handlePointerEvent(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::handlePointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#handlePointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPointerHandler::handlePointerEvent(QPointerEvent *event)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler18handlePointerEventEP13QPointerEve'
        'nt',
        self._addressOf(event),
    )

  def resetDragThreshold(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::resetDragThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#resetDragThreshold
    """
    #  void QQuickPointerHandler::resetDragThreshold()
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler18resetDragThresholdEv',
    )

  def resetCursorShape(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::resetCursorShape()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#resetCursorShape
    """
    #  void QQuickPointerHandler::resetCursorShape()
    self.uglySide.call('ritual_ZN20QQuickPointerHandler16resetCursorShapeEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#enabledChanged
    """
    #  void QQuickPointerHandler::enabledChanged()
    self.uglySide.call('ritual_ZN20QQuickPointerHandler14enabledChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#activeChanged
    """
    #  void QQuickPointerHandler::activeChanged()
    self.uglySide.call('ritual_ZN20QQuickPointerHandler13activeChangedEv')

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#targetChanged
    """
    #  void QQuickPointerHandler::targetChanged()
    self.uglySide.call('ritual_ZN20QQuickPointerHandler13targetChangedEv')

  def marginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::marginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#marginChanged
    """
    #  void QQuickPointerHandler::marginChanged()
    self.uglySide.call('ritual_ZN20QQuickPointerHandler13marginChangedEv')

  def dragThresholdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::dragThresholdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#dragThresholdChanged
    """
    #  void QQuickPointerHandler::dragThresholdChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler20dragThresholdChangedEv',
    )

  @overload(QPointingDevice.GrabTransition, QEventPoint)
  def grabChanged(
      self,
      transition: QPointingDevice.GrabTransition,
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickPointerHandler::grabChanged(QPointingDevice::GrabTransition
    transition, QEventPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#grabChanged

    Parameters
    ----------

    transition : QPointingDevice.GrabTransition
      Passed on as its number.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QQuickPointerHandler::grabChanged(QPointingDevice::GrabTransition
    #      transition, QEventPoint point)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler11grabChangedEN15QPointingDevice14G'
        'rabTransitionE11QEventPoint',
        transition.value, self._valueOf(point),
    )

  def grabPermissionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::grabPermissionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#grabPermissionChanged
    """
    #  void QQuickPointerHandler::grabPermissionChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler21grabPermissionChangedEv',
    )

  @overload(QEventPoint)
  def canceled(self, point: QEventPoint) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::canceled(QEventPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#canceled

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QQuickPointerHandler::canceled(QEventPoint point)
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler8canceledE11QEventPoint',
        self._valueOf(point),
    )

  def cursorShapeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::cursorShapeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#cursorShapeChanged
    """
    #  void QQuickPointerHandler::cursorShapeChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler18cursorShapeChangedEv',
    )

  def parentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::parentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#parentChanged
    """
    #  void QQuickPointerHandler::parentChanged()
    self.uglySide.call('ritual_ZN20QQuickPointerHandler13parentChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#classBegin
    """
    #  void QQuickPointerHandler::classBegin()
    ritual = 'ritual_ZN20QQuickPointerHandler10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickPointerHandler10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#componentComplete
    """
    #  void QQuickPointerHandler::componentComplete()
    ritual = 'ritual_ZN20QQuickPointerHandler17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickPointerHandler17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPointerHandler::event(QEvent *a0)
    ritual = 'ritual_ZN20QQuickPointerHandler5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickPointerHandler5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def currentEvent(self) -> Optional[QPointerEvent]:
    """
    Calls Qt's 'QPointerEvent *QQuickPointerHandler::currentEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#currentEvent

    Returns
    -------

    Optional[QPointerEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointerEvent *QQuickPointerHandler::currentEvent()
    address = self.uglySide.call(
        'ritual_ZN20QQuickPointerHandler12currentEventEv',
    )
    from ..QtGui import QPointerEvent
    return QPointerEvent._cuteAt(address)

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::wantsPointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPointerHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickPointerHandler17wantsPointerEventEP13QPoint'
          'erEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def wantsEventPoint(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::wantsEventPoint(const
    QPointerEvent *event, const QEventPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#wantsEventPoint

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent *event,
    #      const QEventPoint &point)
    ritual = (
        'ritual_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEvent'
        'RK11QEventPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointe'
          'rEventRK11QEventPoint')
    return self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(point),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def handlePointerEventImpl(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickPointerHandler::handlePointerEventImpl(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#handlePointerEventImpl

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPointerHandler::handlePointerEventImpl(QPointerEvent
    #      *event)
    ritual = (
        'ritual_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointe'
        'rEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickPointerHandler22handlePointerEventImplEP13Q'
          'PointerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem)
  @overload(NoneType)
  def onTargetChanged(self, oldTarget: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::onTargetChanged(QQuickItem
    *oldTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#onTargetChanged

    Parameters
    ----------

    oldTarget : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
    ritual = 'ritual_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(oldTarget))

  def onActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandler::onActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#onActiveChanged
    """
    #  void QQuickPointerHandler::onActiveChanged()
    ritual = 'ritual_ZN20QQuickPointerHandler15onActiveChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickPointerHandler15onActiveChangedEv'
    self.uglySide.call(ritual)

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def canGrab(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandler::canGrab(QPointerEvent *event,
    const QEventPoint &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#canGrab

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
    #      QEventPoint &point)
    ritual = (
        'ritual_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEvent'
        'Point')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11'
          'QEventPoint')
    return self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(point),
    )

  @overload(QPointerEvent, QEventPoint, QObject)
  @overload(QPointerEvent, QEventPoint, NoneType)
  @overload(NoneType, QEventPoint, QObject)
  @overload(NoneType, QEventPoint, NoneType)
  def approveGrabTransition(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
      proposedGrabber: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickPointerHandler::approveGrabTransition(QPointerEvent *event, const
    QEventPoint &point, QObject *proposedGrabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandler.html#approveGrabTransition

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    proposedGrabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPointerHandler::approveGrabTransition(QPointerEvent *event,
    #      const QEventPoint &point, QObject *proposedGrabber)
    ritual = (
        'ritual_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointer'
        'EventRK11QEventPointP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickPointerHandler21approveGrabTransitionEP13QP'
          'ointerEventRK11QEventPointP7QObject')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._valueOf(point),
        self._addressOf(proposedGrabber, 'QObject'),
    )

  def d_func(self) -> Optional[QQuickPointerHandlerPrivate]:
    """
    Calls Qt's 'QQuickPointerHandlerPrivate *QQuickPointerHandler::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerhandler.html#d_func

    Returns
    -------

    Optional[QQuickPointerHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerHandlerPrivate *QQuickPointerHandler::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickPointerHandler6d_funcEv')
    from . import QQuickPointerHandlerPrivate
    return QQuickPointerHandlerPrivate._cuteAt(address)

  @staticmethod
  def cancelAllGrabs(*__, **_) -> Never:
    """
    Qt's 'void QQuickPointerHandler::cancelAllGrabs(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPointerHandler.cancelAllGrabs' has no cute function yet. "
        "Qt's 'void QQuickPointerHandler::cancelAllGrabs(QPointerEvent "
        "*event, QEventPoint &point)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def onGrabChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickPointerHandler::onGrabChanged(QQuickPointerHandler
    *grabber, QPointingDevice::GrabTransition transition, QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickPointerHandler.onGrabChanged' has no cute function yet. "
        "Qt's 'void "
        "QQuickPointerHandler::onGrabChanged(QQuickPointerHandler *grabber, "
        "QPointingDevice::GrabTransition transition, QPointerEvent *event, "
        "QEventPoint &point)': takes a type Python has no way to hand over "
        "yet.")
