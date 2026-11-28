"""
QQmlDelayedCallQueue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldelayedcallqueue_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlDelayedCallQueue to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlV4Function = WAIT['QQmlV4Function']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelayedCallQueue(QObject):
  """
  The cute side of Qt's QQmlDelayedCallQueue: a plain Python object standing
  in front of one C++ QQmlDelayedCallQueue.

  It is built on the cute 'QObject', as Qt's QQmlDelayedCallQueue is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelayedCallQueue that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject',
  'addUniquelyAndExecuteLater', 'ticked', 'executeAllExpired_Later'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelayedCallQueue::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlDelayedCallQueue::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDelayedCallQueue::~QQmlDelayedCallQueue()': the destructor:
    Python never removes a C++ QQmlDelayedCallQueue.
  - Qt's 'void QQmlDelayedCallQueue::storeAnyArguments(DelayedFunctionCall
    &dfc, QQmlV4FunctionPtr args, int offset, QV4::ExecutionEngine *engine)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 leans on 'QQmlDelayedCallQueue; 2 not
  a gap.

  What to expect
  --------------

  - The C++ QQmlDelayedCallQueue is created at the first use, not by
    'QQmlDelayedCallQueue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelayedCallQueue.
  - Qt tells when it has removed the C++ QQmlDelayedCallQueue. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDelayedCallQueue that has no cute function yet,
    '__init__', 'init', 'storeAnyArguments', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QQmlV4Function)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QQmlV4Function)
  @overload(NoneType, NoneType)
  def addUniquelyAndExecuteLater(
      engine: Optional[QV4.ExecutionEngine],
      args: Optional[QQmlV4Function],
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QQmlDelayedCallQueue::addUniquelyAndExecuteLater(QV4::ExecutionEngine
    *engine, QQmlV4FunctionPtr args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayedcallqueue.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::ReturnedValue
    #      QQmlDelayedCallQueue::addUniquelyAndExecuteLater(QV4::
    #      ExecutionEngine *engine, QQmlV4FunctionPtr args)
    return Rituals.call(
        'ritual_ZN20QQmlDelayedCallQueue26addUniquelyAndExecuteLaterEPN3QV4'
        '15ExecutionEngineEP14QQmlV4Function',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(args),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelayedCallQueue'

  #  A C++ QQmlDelayedCallQueue Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelayedCallQueue'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDelayedCallQueue::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayedcallqueue.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelayedCallQueue::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlDelayedCallQueue10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QQmlDelayedCallQueue::QQmlDelayedCallQueue()': leans on
    'QQmlDelayedCallQueue::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelayedCallQueue.__init__' has no cute function yet. Qt's "
        "'QQmlDelayedCallQueue::QQmlDelayedCallQueue()': leans on "
        "'QQmlDelayedCallQueue::qt_metacall(QMetaObject::Call, int, "
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

  def ticked(self) -> None:
    """
    Calls Qt's 'void QQmlDelayedCallQueue::ticked()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelayedcallqueue.html#ticked
    """
    #  void QQmlDelayedCallQueue::ticked()
    self.uglySide.call('ritual_ZN20QQmlDelayedCallQueue6tickedEv')

  def executeAllExpired_Later(self) -> None:
    """
    Calls Qt's 'void QQmlDelayedCallQueue::executeAllExpired_Later()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayedcallqueue.html#executeAllExpired_Later
    """
    #  void QQmlDelayedCallQueue::executeAllExpired_Later()
    self.uglySide.call(
        'ritual_ZN20QQmlDelayedCallQueue23executeAllExpired_LaterEv',
    )

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelayedCallQueue::init(QV4::ExecutionEngine *a0)': leans
    on 'QQmlDelayedCallQueue::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelayedCallQueue.init' has no cute function yet. Qt's 'void "
        "QQmlDelayedCallQueue::init(QV4::ExecutionEngine *a0)': leans on "
        "'QQmlDelayedCallQueue::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def storeAnyArguments(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelayedCallQueue::storeAnyArguments(DelayedFunctionCall
    &dfc, QQmlV4FunctionPtr args, int offset, QV4::ExecutionEngine *engine)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelayedCallQueue.storeAnyArguments' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelayedCallQueue::storeAnyArguments(DelayedFunctionCall &dfc, "
        "QQmlV4FunctionPtr args, int offset, QV4::ExecutionEngine "
        "*engine)': takes a type Python has no way to hand over yet.")
