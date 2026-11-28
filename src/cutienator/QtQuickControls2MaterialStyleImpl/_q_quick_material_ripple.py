"""
QQuickMaterialRipple binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialripple_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMaterialRipple to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QTimerEvent
  from ..QtGui import QColor
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QSGNode = WAIT['QSGNode']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMaterialRipple(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickMaterialRipple: a plain Python object standing
  in front of one C++ QQuickMaterialRipple.

  What exists
  -----------

  Every function of Qt's QQuickMaterialRipple that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'color', 'setColor',
  'clipRadius', 'setClipRadius', 'isActive', 'setActive', 'isPressed',
  'setPressed', 'trigger', 'setTrigger', 'anchorPoint', 'anchor',
  'setAnchor', 'diameter', 'itemChange', 'updatePaintNode', 'timerEvent',
  'prepareWave', 'enterWave', 'exitWave'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMaterialRipple::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickMaterialRipple::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickMaterialRipple; 1 leans on 'vtable for QQuickMaterialRipple', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQuickMaterialRipple is created at the first use, not by
    'QQuickMaterialRipple(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMaterialRipple.
  - Qt tells when it has removed the C++ QQuickMaterialRipple. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMaterialRipple that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuickMaterialRipple, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Trigger(CuteNum):
    """
    The enum 'QQuickMaterialRipple::Trigger' of Qt, with the 2 names Qt gives
    in it.
    """

    Press = Kee[int](0)
    Release = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMaterialRipple'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMaterialRipple::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMaterialRipple::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickMaterialRipple10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialRipple::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialRipple::color() const
    address = self.uglySide.call('ritual_ZNK20QQuickMaterialRipple5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def clipRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialRipple::clipRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#clipRadius
    """
    #  qreal QQuickMaterialRipple::clipRadius() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickMaterialRipple10clipRadiusEv',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialRipple::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#isActive
    """
    #  bool QQuickMaterialRipple::isActive() const
    return self.uglySide.call('ritual_ZNK20QQuickMaterialRipple8isActiveEv')

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialRipple::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#isPressed
    """
    #  bool QQuickMaterialRipple::isPressed() const
    return self.uglySide.call('ritual_ZNK20QQuickMaterialRipple9isPressedEv')

  def trigger(self) -> Trigger:
    """
    Calls Qt's 'Trigger QQuickMaterialRipple::trigger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#trigger

    Returns
    -------

    Trigger
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Trigger(number)' gives.
    """
    #  Trigger QQuickMaterialRipple::trigger() const
    return QQuickMaterialRipple.Trigger(self.uglySide.call(
        'ritual_ZNK20QQuickMaterialRipple7triggerEv',
    ))

  def anchorPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickMaterialRipple::anchorPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#anchorPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickMaterialRipple::anchorPoint() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickMaterialRipple11anchorPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def anchor(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMaterialRipple::anchor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#anchor

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMaterialRipple::anchor() const
    address = self.uglySide.call('ritual_ZNK20QQuickMaterialRipple6anchorEv')
    return QQuickItem._cuteAt(address)

  def diameter(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialRipple::diameter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#diameter
    """
    #  qreal QQuickMaterialRipple::diameter() const
    return self.uglySide.call('ritual_ZNK20QQuickMaterialRipple8diameterEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMaterialRipple::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN20QQuickMaterialRipple8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setClipRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::setClipRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#setClipRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickMaterialRipple::setClipRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN20QQuickMaterialRipple13setClipRadiusEd', radius,
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickMaterialRipple::setActive(bool active)
    self.uglySide.call('ritual_ZN20QQuickMaterialRipple9setActiveEb', active)

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::setPressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickMaterialRipple::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN20QQuickMaterialRipple10setPressedEb', pressed,
    )

  @overload(Trigger)
  def setTrigger(self, trigger: Trigger) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::setTrigger(Trigger trigger)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#setTrigger

    Parameters
    ----------

    trigger : Trigger
      Passed on as its number.
    """
    #  void QQuickMaterialRipple::setTrigger(Trigger trigger)
    self.uglySide.call(
        'ritual_ZN20QQuickMaterialRipple10setTriggerENS_7TriggerE',
        trigger.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setAnchor(self, anchor: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::setAnchor(QQuickItem *anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#setAnchor

    Parameters
    ----------

    anchor : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMaterialRipple::setAnchor(QQuickItem *anchor)
    self.uglySide.call(
        'ritual_ZN20QQuickMaterialRipple9setAnchorEP10QQuickItem',
        self._addressOf(anchor),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickMaterialRipple::QQuickMaterialRipple(QQuickItem *parent)':
    leans on 'vtable for QQuickMaterialRipple', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialRipple.__init__' has no cute function yet. Qt's "
        "'QQuickMaterialRipple::QQuickMaterialRipple(QQuickItem *parent)': "
        "leans on 'vtable for QQuickMaterialRipple', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::itemChange(ItemChange change,
    const ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickMaterialRipple::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN20QQuickMaterialRipple10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickMaterialRipple10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickMaterialRipple::updatePaintNode(QSGNode
    *oldNode, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickMaterialRipple::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *a1)
    address = self.uglySide.call(
        'ritual_ZN20QQuickMaterialRipple15updatePaintNodeEP7QSGNodePN10QQui'
        'ckItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::timerEvent(QTimerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMaterialRipple::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN20QQuickMaterialRipple10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickMaterialRipple10timerEventEP11QTimerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def prepareWave(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::prepareWave()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#prepareWave
    """
    #  void QQuickMaterialRipple::prepareWave()
    self.uglySide.call('ritual_ZN20QQuickMaterialRipple11prepareWaveEv')

  def enterWave(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::enterWave()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialripple.html#enterWave
    """
    #  void QQuickMaterialRipple::enterWave()
    self.uglySide.call('ritual_ZN20QQuickMaterialRipple9enterWaveEv')

  def exitWave(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialRipple::exitWave()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialripple.html#exitWave
    """
    #  void QQuickMaterialRipple::exitWave()
    self.uglySide.call('ritual_ZN20QQuickMaterialRipple8exitWaveEv')
