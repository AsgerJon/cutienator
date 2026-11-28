"""
QQmlListModelWorkerAgent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodelworkeragent_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlListModelWorkerAgent to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtQml import QJSValue, QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQmlV4Function = WAIT['QQmlV4Function']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlListModelWorkerAgent(QObject):
  """
  The cute side of Qt's QQmlListModelWorkerAgent: a plain Python object
  standing in front of one C++ QQmlListModelWorkerAgent.

  It is built on the cute 'QObject', as Qt's QQmlListModelWorkerAgent is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlListModelWorkerAgent that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'engine', 'addref',
  'release', 'count', 'clear', 'remove', 'append', 'insert', 'get', 'move',
  'sync', 'modelDestroyed', 'engineChanged', 'event'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlListModelWorkerAgent::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlListModelWorkerAgent::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlListModelWorkerAgent::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.
  - Qt's 'QQmlListModelWorkerAgent::~QQmlListModelWorkerAgent()': the
    destructor: Python never removes a C++ QQmlListModelWorkerAgent.

  What has no ritual
  ------------------

  7 of the 26 functions Qt declares: 3 leans on 'QQmlListModelWorkerAgent; 2
  not a gap; 2 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlListModelWorkerAgent is created at the first use, not by
    'QQmlListModelWorkerAgent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlListModelWorkerAgent.
  - Qt tells when it has removed the C++ QQmlListModelWorkerAgent. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlListModelWorkerAgent that has no cute function yet,
    '__init__', 'set', 'setEngine', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListModelWorkerAgent'

  #  A C++ QQmlListModelWorkerAgent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlListModelWorkerAgent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlListModelWorkerAgent::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlListModelWorkerAgent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlListModelWorkerAgent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQmlListModelWorkerAgent::engine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQmlListModelWorkerAgent::engine() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlListModelWorkerAgent6engineEv',
    )
    return QV4.ExecutionEngine._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlListModelWorkerAgent::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#count
    """
    #  int QQmlListModelWorkerAgent::count() const
    return self.uglySide.call('ritual_ZNK24QQmlListModelWorkerAgent5countEv')

  @overload(int)
  def get(self, index: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlListModelWorkerAgent::get(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlListModelWorkerAgent::get(int index) const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlListModelWorkerAgent3getEi', index,
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

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
    Qt's 'QQmlListModelWorkerAgent::QQmlListModelWorkerAgent(QQmlListModel
    *a0)': leans on 'QQmlListModelWorkerAgent::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListModelWorkerAgent.__init__' has no cute function yet. Qt's "
        "'QQmlListModelWorkerAgent::QQmlListModelWorkerAgent(QQmlListModel "
        "*a0)': leans on "
        "'QQmlListModelWorkerAgent::qt_metacall(QMetaObject::Call, int, "
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

  def addref(self) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::addref()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#addref
    """
    #  void QQmlListModelWorkerAgent::addref()
    self.uglySide.call('ritual_ZN24QQmlListModelWorkerAgent6addrefEv')

  def release(self) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#release
    """
    #  void QQmlListModelWorkerAgent::release()
    self.uglySide.call('ritual_ZN24QQmlListModelWorkerAgent7releaseEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#clear
    """
    #  void QQmlListModelWorkerAgent::clear()
    self.uglySide.call('ritual_ZN24QQmlListModelWorkerAgent5clearEv')

  @overload(QQmlV4Function)
  @overload(NoneType)
  def remove(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::remove(QQmlV4FunctionPtr
    args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#remove

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModelWorkerAgent::remove(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent6removeEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def append(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::append(QQmlV4FunctionPtr
    args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#append

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModelWorkerAgent::append(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent6appendEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def insert(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::insert(QQmlV4FunctionPtr
    args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#insert

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModelWorkerAgent::insert(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent6insertEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(int, int, int)
  def move(self, from_: int, to: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::move(int from, int to, int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#move

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlListModelWorkerAgent::move(int from, int to, int count)
    self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent4moveEiii', from_, to, count,
    )

  def sync(self) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#sync
    """
    #  void QQmlListModelWorkerAgent::sync()
    self.uglySide.call('ritual_ZN24QQmlListModelWorkerAgent4syncEv')

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QQmlListModelWorkerAgent::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#modelDestroyed
    """
    #  void QQmlListModelWorkerAgent::modelDestroyed()
    self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent14modelDestroyedEv',
    )

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def engineChanged(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void
    QQmlListModelWorkerAgent::engineChanged(QQmlV4ExecutionEnginePtr
    engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#engineChanged

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlListModelWorkerAgent::engineChanged(QQmlV4ExecutionEnginePtr
    #      engine)
    self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent13engineChangedEPN3QV415Executi'
        'onEngineE',
        self._addressOf(engine),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQmlListModelWorkerAgent::event(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelworkeragent.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlListModelWorkerAgent::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_ZN24QQmlListModelWorkerAgent5eventEP6QEvent',
        self._addressOf(a0),
    )

  @staticmethod
  def set(*__, **_) -> Never:
    """
    Qt's 'void QQmlListModelWorkerAgent::set(int index, const QJSValue
    &value)': the compiler refuses its ritual as it would be written here:
    redefinition of 'index' with a different type: 'const int' vs 'int'.
    """
    raise NotImplementedError(
        "'QQmlListModelWorkerAgent.set' has no cute function yet. Qt's "
        "'void QQmlListModelWorkerAgent::set(int index, const QJSValue "
        "&value)': the compiler refuses its ritual as it would be written "
        "here: redefinition of 'index' with a different type: 'const int' "
        "vs 'int'.")

  @staticmethod
  def setEngine(*__, **_) -> Never:
    """
    Qt's 'void QQmlListModelWorkerAgent::setEngine(QV4::ExecutionEngine
    *eng)': leans on
    'QQmlListModelWorkerAgent::engineChanged(QV4::ExecutionEngine*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListModelWorkerAgent.setEngine' has no cute function yet. "
        "Qt's 'void "
        "QQmlListModelWorkerAgent::setEngine(QV4::ExecutionEngine *eng)': "
        "leans on "
        "'QQmlListModelWorkerAgent::engineChanged(QV4::ExecutionEngine*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
