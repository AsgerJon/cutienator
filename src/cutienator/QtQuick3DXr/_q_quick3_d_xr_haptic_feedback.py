"""
QQuick3DXrHapticFeedback binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrHapticFeedback to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuick3DXrAbstractHapticEffect


class QQuick3DXrHapticFeedback(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuick3DXrHapticFeedback: a plain Python object
  standing in front of one C++ QQuick3DXrHapticFeedback.

  It is built on the cute 'QObject', as Qt's QQuick3DXrHapticFeedback is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QQuick3DXrHapticFeedback is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrHapticFeedback that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'classBegin',
  'componentComplete', 'hapticEffect', 'controller', 'trigger',
  'testAndClear', 'controllerChanged', 'hapticEffectChanged',
  'triggerChanged', 'conditionChanged', 'start', 'stop'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrHapticFeedback::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DXrHapticFeedback::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DXrHapticFeedback::~QQuick3DXrHapticFeedback()': the
    destructor: Python never removes a C++ QQuick3DXrHapticFeedback.
  - Qt's 'enum Condition QQuick3DXrHapticFeedback::condition() const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  8 of the 25 functions Qt declares: 6 leans on 'QQuick3DXrHapticFeedback; 2
  not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrHapticFeedback is created at the first use, not by
    'QQuick3DXrHapticFeedback(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrHapticFeedback.
  - Qt tells when it has removed the C++ QQuick3DXrHapticFeedback. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrHapticFeedback that has no cute function yet,
    '__init__', 'condition', 'setCondition', 'setController',
    'setHapticEffect', 'setTrigger', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DXrHapticFeedback, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Condition(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrHapticFeedback::Condition' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    RisingEdge = Kee[int](0)
    TrailingEdge = Kee[int](1)

  class Controller(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrHapticFeedback::Controller' of Qt, with the 8 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
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
  __qt_class__ = 'QQuick3DXrHapticFeedback'

  #  Qt's QQuick3DXrHapticFeedback is built on more than one class. The part
  #  of a C++ QQuick3DXrHapticFeedback that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuick3DXrHapticFeedback_QQmlParserStatus',
  }

  #  A C++ QQuick3DXrHapticFeedback Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrHapticFeedback'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrHapticFeedback::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrHapticFeedback::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DXrHapticFeedback10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hapticEffect(self) -> Optional[QQuick3DXrAbstractHapticEffect]:
    """
    Calls Qt's 'QQuick3DXrAbstractHapticEffect
    *QQuick3DXrHapticFeedback::hapticEffect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#hapticEffect

    Returns
    -------

    Optional[QQuick3DXrAbstractHapticEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrAbstractHapticEffect
    #      *QQuick3DXrHapticFeedback::hapticEffect() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DXrHapticFeedback12hapticEffectEv',
    )
    from . import QQuick3DXrAbstractHapticEffect
    return QQuick3DXrAbstractHapticEffect._cuteAt(address)

  def controller(self) -> Controller:
    """
    Calls Qt's 'Controller QQuick3DXrHapticFeedback::controller() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#controller

    Returns
    -------

    Controller
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Controller(number)'
      gives.
    """
    #  Controller QQuick3DXrHapticFeedback::controller() const
    return QQuick3DXrHapticFeedback.Controller(self.uglySide.call(
        'ritual_ZNK24QQuick3DXrHapticFeedback10controllerEv',
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
    Qt's 'QQuick3DXrHapticFeedback::QQuick3DXrHapticFeedback(QObject
    *parent)': leans on
    'QQuick3DXrHapticFeedback::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHapticFeedback.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrHapticFeedback::QQuick3DXrHapticFeedback(QObject "
        "*parent)': leans on "
        "'QQuick3DXrHapticFeedback::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'void QQuick3DXrHapticFeedback::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#classBegin
    """
    #  void QQuick3DXrHapticFeedback::classBegin()
    ritual = 'ritual_ZN24QQuick3DXrHapticFeedback10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuick3DXrHapticFeedback10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#componentComplete
    """
    #  void QQuick3DXrHapticFeedback::componentComplete()
    self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback17componentCompleteEv',
    )

  def trigger(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrHapticFeedback::trigger()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#trigger
    """
    #  bool QQuick3DXrHapticFeedback::trigger()
    return self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback7triggerEv',
    )

  def testAndClear(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrHapticFeedback::testAndClear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#testAndClear
    """
    #  bool QQuick3DXrHapticFeedback::testAndClear()
    return self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback12testAndClearEv',
    )

  def controllerChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::controllerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#controllerChanged
    """
    #  void QQuick3DXrHapticFeedback::controllerChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback17controllerChangedEv',
    )

  def hapticEffectChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::hapticEffectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#hapticEffectChanged
    """
    #  void QQuick3DXrHapticFeedback::hapticEffectChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback19hapticEffectChangedEv',
    )

  def triggerChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::triggerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#triggerChanged
    """
    #  void QQuick3DXrHapticFeedback::triggerChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback14triggerChangedEv',
    )

  def conditionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::conditionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#conditionChanged
    """
    #  void QQuick3DXrHapticFeedback::conditionChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DXrHapticFeedback16conditionChangedEv',
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#start
    """
    #  void QQuick3DXrHapticFeedback::start()
    self.uglySide.call('ritual_ZN24QQuick3DXrHapticFeedback5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHapticFeedback::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrhapticfeedback.html#stop
    """
    #  void QQuick3DXrHapticFeedback::stop()
    self.uglySide.call('ritual_ZN24QQuick3DXrHapticFeedback4stopEv')

  @staticmethod
  def condition(*__, **_) -> Never:
    """
    Qt's 'enum Condition QQuick3DXrHapticFeedback::condition() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrHapticFeedback.condition' has no cute function yet. "
        "Qt's 'enum Condition QQuick3DXrHapticFeedback::condition() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setCondition(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHapticFeedback::setCondition(enum Condition
    newCondition)': leans on 'QQuick3DXrHapticFeedback::conditionChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHapticFeedback.setCondition' has no cute function yet. "
        "Qt's 'void QQuick3DXrHapticFeedback::setCondition(enum Condition "
        "newCondition)': leans on "
        "'QQuick3DXrHapticFeedback::conditionChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setController(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHapticFeedback::setController(Controller
    newController)': leans on
    'QQuick3DXrHapticFeedback::controllerChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHapticFeedback.setController' has no cute function yet. "
        "Qt's 'void QQuick3DXrHapticFeedback::setController(Controller "
        "newController)': leans on "
        "'QQuick3DXrHapticFeedback::controllerChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setHapticEffect(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrHapticFeedback::setHapticEffect(QQuick3DXrAbstractHapticEffect
    *newHapticEffect)': leans on
    'QQuick3DXrHapticFeedback::hapticEffectChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHapticFeedback.setHapticEffect' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrHapticFeedback::setHapticEffect(QQuick3DXrAbstractHapticE"
        "ffect *newHapticEffect)': leans on "
        "'QQuick3DXrHapticFeedback::hapticEffectChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setTrigger(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHapticFeedback::setTrigger(bool newTrigger)': leans
    on 'QQuick3DXrHapticFeedback::triggerChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHapticFeedback.setTrigger' has no cute function yet. "
        "Qt's 'void QQuick3DXrHapticFeedback::setTrigger(bool newTrigger)': "
        "leans on 'QQuick3DXrHapticFeedback::triggerChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
