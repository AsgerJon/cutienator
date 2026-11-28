"""
QQuick3DXrInputAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrInputAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuick3DXrInputAction(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuick3DXrInputAction: a plain Python object standing
  in front of one C++ QQuick3DXrInputAction.

  It is built on the cute 'QObject', as Qt's QQuick3DXrInputAction is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuick3DXrInputAction is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrInputAction that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'value', 'pressed',
  'actionName', 'classBegin', 'componentComplete', 'hand', 'enabled',
  'controller', 'valueChanged', 'pressedChanged', 'triggered',
  'actionNameChanged', 'actionIdChanged', 'handChanged', 'enabledChanged',
  'controllerChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrInputAction::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrInputAction::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DXrInputAction::~QQuick3DXrInputAction()': the destructor:
    Python never removes a C++ QQuick3DXrInputAction.
  - Qt's 'QList<Action> QQuick3DXrInputAction::actionId() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  11 of the 32 functions Qt declares: 9 leans on 'QQuick3DXrInputAction; 2
  not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrInputAction is created at the first use, not by
    'QQuick3DXrInputAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrInputAction.
  - Qt tells when it has removed the C++ QQuick3DXrInputAction. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrInputAction that has no cute function yet,
    '__init__', 'actionId', 'setActionId', 'setActionName', 'setController',
    'setEnabled', 'setHand', 'setPressed', 'setValue', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DXrInputAction, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Action(CuteNum):
    """
    The enum 'QQuick3DXrInputAction::Action' of Qt, with the 32 names Qt
    gives in it.
    """

    CustomAction = Kee[int](-1)
    Button1Pressed = Kee[int](0)
    Button1Touched = Kee[int](1)
    Button2Pressed = Kee[int](2)
    Button2Touched = Kee[int](3)
    ButtonMenuPressed = Kee[int](4)
    ButtonMenuTouched = Kee[int](5)
    ButtonSystemPressed = Kee[int](6)
    ButtonSystemTouched = Kee[int](7)
    SqueezeValue = Kee[int](8)
    SqueezeForce = Kee[int](9)
    SqueezePressed = Kee[int](10)
    TriggerValue = Kee[int](11)
    TriggerPressed = Kee[int](12)
    TriggerTouched = Kee[int](13)
    ThumbstickX = Kee[int](14)
    ThumbstickY = Kee[int](15)
    ThumbstickPressed = Kee[int](16)
    ThumbstickTouched = Kee[int](17)
    ThumbrestTouched = Kee[int](18)
    TrackpadX = Kee[int](19)
    TrackpadY = Kee[int](20)
    TrackpadForce = Kee[int](21)
    TrackpadTouched = Kee[int](22)
    TrackpadPressed = Kee[int](23)
    IndexFingerPinch = Kee[int](24)
    MiddleFingerPinch = Kee[int](25)
    RingFingerPinch = Kee[int](26)
    LittleFingerPinch = Kee[int](27)
    HandTrackingMenuPress = Kee[int](28)
    NumHandActions = Kee[int](29)
    NumActions = Kee[int](30)

  class Controller(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrInputAction::Controller' of Qt, with the 8 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    LeftController = Kee[int](0)
    RightController = Kee[int](1)
    UnknownController = Kee[int](2)
    LeftHand = Kee[int](0)
    RightHand = Kee[int](1)
    ControllerLeft = Kee[int](0)
    ControllerRight = Kee[int](1)
    ControllerNone = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrInputAction'

  #  Qt's QQuick3DXrInputAction is built on more than one class. The part of
  #  a C++ QQuick3DXrInputAction that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuick3DXrInputAction_QQmlParserStatus',
  }

  #  A C++ QQuick3DXrInputAction Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrInputAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrInputAction::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrInputAction::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DXrInputAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrInputAction::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrinputaction.html#value
    """
    #  float QQuick3DXrInputAction::value() const
    return self.uglySide.call('ritual_ZNK21QQuick3DXrInputAction5valueEv')

  def pressed(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrInputAction::pressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrinputaction.html#pressed
    """
    #  bool QQuick3DXrInputAction::pressed() const
    return self.uglySide.call('ritual_ZNK21QQuick3DXrInputAction7pressedEv')

  def actionName(self) -> str:
    """
    Calls Qt's 'QString QQuick3DXrInputAction::actionName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#actionName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrInputAction::actionName() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DXrInputAction10actionNameEv',
    )

  def hand(self) -> Controller:
    """
    Calls Qt's 'Controller QQuick3DXrInputAction::hand() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrinputaction.html#hand

    Returns
    -------

    Controller
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Controller(number)'
      gives.
    """
    #  Controller QQuick3DXrInputAction::hand() const
    return QQuick3DXrInputAction.Controller(self.uglySide.call(
        'ritual_ZNK21QQuick3DXrInputAction4handEv',
    ))

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrInputAction::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrinputaction.html#enabled
    """
    #  bool QQuick3DXrInputAction::enabled() const
    return self.uglySide.call('ritual_ZNK21QQuick3DXrInputAction7enabledEv')

  def controller(self) -> Controller:
    """
    Calls Qt's 'Controller QQuick3DXrInputAction::controller() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#controller

    Returns
    -------

    Controller
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Controller(number)'
      gives.
    """
    #  Controller QQuick3DXrInputAction::controller() const
    return QQuick3DXrInputAction.Controller(self.uglySide.call(
        'ritual_ZNK21QQuick3DXrInputAction10controllerEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QQuick3DXrInputAction::QQuick3DXrInputAction(QObject *parent)':
    leans on 'QQuick3DXrInputAction::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrInputAction::QQuick3DXrInputAction(QObject *parent)': "
        "leans on 'QQuick3DXrInputAction::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#classBegin
    """
    #  void QQuick3DXrInputAction::classBegin()
    ritual = 'ritual_ZN21QQuick3DXrInputAction10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuick3DXrInputAction10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#componentComplete
    """
    #  void QQuick3DXrInputAction::componentComplete()
    self.uglySide.call(
        'ritual_ZN21QQuick3DXrInputAction17componentCompleteEv',
    )

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::valueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#valueChanged
    """
    #  void QQuick3DXrInputAction::valueChanged()
    self.uglySide.call('ritual_ZN21QQuick3DXrInputAction12valueChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#pressedChanged
    """
    #  void QQuick3DXrInputAction::pressedChanged()
    self.uglySide.call('ritual_ZN21QQuick3DXrInputAction14pressedChangedEv')

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::triggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#triggered
    """
    #  void QQuick3DXrInputAction::triggered()
    self.uglySide.call('ritual_ZN21QQuick3DXrInputAction9triggeredEv')

  def actionNameChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::actionNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#actionNameChanged
    """
    #  void QQuick3DXrInputAction::actionNameChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DXrInputAction17actionNameChangedEv',
    )

  def actionIdChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::actionIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#actionIdChanged
    """
    #  void QQuick3DXrInputAction::actionIdChanged()
    self.uglySide.call('ritual_ZN21QQuick3DXrInputAction15actionIdChangedEv')

  def handChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::handChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#handChanged
    """
    #  void QQuick3DXrInputAction::handChanged()
    self.uglySide.call('ritual_ZN21QQuick3DXrInputAction11handChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#enabledChanged
    """
    #  void QQuick3DXrInputAction::enabledChanged()
    self.uglySide.call('ritual_ZN21QQuick3DXrInputAction14enabledChangedEv')

  def controllerChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputAction::controllerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputaction.html#controllerChanged
    """
    #  void QQuick3DXrInputAction::controllerChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DXrInputAction17controllerChangedEv',
    )

  @staticmethod
  def actionId(*__, **_) -> Never:
    """
    Qt's 'QList<Action> QQuick3DXrInputAction::actionId() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.actionId' has no cute function yet. Qt's "
        "'QList<Action> QQuick3DXrInputAction::actionId() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setActionId(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setActionId(const QList<Action>
    &newActionId)': leans on 'QQuick3DXrInputAction::actionIdChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setActionId' has no cute function yet. Qt's "
        "'void QQuick3DXrInputAction::setActionId(const QList<Action> "
        "&newActionId)': leans on "
        "'QQuick3DXrInputAction::actionIdChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setActionName(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setActionName(const QString
    &newActionName)': leans on 'QQuick3DXrInputAction::actionNameChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setActionName' has no cute function yet. "
        "Qt's 'void QQuick3DXrInputAction::setActionName(const QString "
        "&newActionName)': leans on "
        "'QQuick3DXrInputAction::actionNameChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setController(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setController(Controller
    newController)': leans on 'QQuick3DXrInputAction::handChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setController' has no cute function yet. "
        "Qt's 'void QQuick3DXrInputAction::setController(Controller "
        "newController)': leans on 'QQuick3DXrInputAction::handChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setEnabled(bool newEnabled)': leans on
    'QQuick3DXrInputAction::enabledChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setEnabled' has no cute function yet. Qt's "
        "'void QQuick3DXrInputAction::setEnabled(bool newEnabled)': leans "
        "on 'QQuick3DXrInputAction::enabledChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setHand(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setHand(Controller newHand)': leans on
    'QQuick3DXrInputAction::handChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setHand' has no cute function yet. Qt's "
        "'void QQuick3DXrInputAction::setHand(Controller newHand)': leans "
        "on 'QQuick3DXrInputAction::handChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setPressed(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setPressed(bool newPressed)': leans on
    'QQuick3DXrInputAction::pressedChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setPressed' has no cute function yet. Qt's "
        "'void QQuick3DXrInputAction::setPressed(bool newPressed)': leans "
        "on 'QQuick3DXrInputAction::pressedChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setValue(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputAction::setValue(float newValue)': leans on
    'QQuick3DXrInputAction::valueChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputAction.setValue' has no cute function yet. Qt's "
        "'void QQuick3DXrInputAction::setValue(float newValue)': leans on "
        "'QQuick3DXrInputAction::valueChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
