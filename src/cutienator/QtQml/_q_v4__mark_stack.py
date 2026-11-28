"""
QV4::MarkStack binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::MarkStack to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MarkStack(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::MarkStack: a plain Python object standing in
  front of one C++ QV4::MarkStack.

  C++ hands a QV4::MarkStack around as a copy, so every C++ QV4::MarkStack
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::MarkStack that has a ritual and that Python can
  call so far, 7 names in all: 'push', 'isEmpty', 'remainingBeforeSoftLimit',
  'engine', 'drain', 'setSoftLimit', 'pop'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::MarkStack::~MarkStack()': the destructor: Python removes its
    C++ QV4::MarkStack by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::MarkStack is created at the first use, not by
    'QV4::MarkStack(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::MarkStack back gives a copy the ritual made for
    Python, in a new cute QV4::MarkStack.
  """

  #  The enums Qt writes inside QV4::MarkStack, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DrainState(CuteNum, scoped=True):
    """
    The enum 'QV4::MarkStack::DrainState' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Ongoing = Kee[int](0)
    Complete = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::MarkStack'

  #  Qt's '~QV4::MarkStack()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::MarkStack behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV49MarkStackD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QV4::MarkStack::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#isEmpty
    """
    #  bool QV4::MarkStack::isEmpty() const
    return self.uglySide.call('ritual_ZNK3QV49MarkStack7isEmptyEv')

  def remainingBeforeSoftLimit(self) -> int:
    """
    Calls Qt's 'qptrdiff QV4::MarkStack::remainingBeforeSoftLimit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-markstack.html#remainingBeforeSoftLimit
    """
    #  qptrdiff QV4::MarkStack::remainingBeforeSoftLimit() const
    return self.uglySide.call(
        'ritual_ZNK3QV49MarkStack24remainingBeforeSoftLimitEv',
    )

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'ExecutionEngine *QV4::MarkStack::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionEngine *QV4::MarkStack::engine() const
    address = self.uglySide.call('ritual_ZNK3QV49MarkStack6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSoftLimit(self, size: int) -> None:
    """
    Calls Qt's 'void QV4::MarkStack::setSoftLimit(size_t size)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#setSoftLimit

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QV4::MarkStack::setSoftLimit(size_t size)
    self.uglySide.call('ritual_ZN3QV49MarkStack12setSoftLimitEm', size)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's 'QV4::MarkStack::MarkStack(ExecutionEngine
    *engine)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#MarkStack

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::MarkStack::MarkStack(ExecutionEngine *engine)
    self._noteCreation(MarkStack, lambda: Rituals.call(
        'ritual_ZN3QV49MarkStackC1EPNS_15ExecutionEngineE',
        self._addressOf(engine),
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

  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def push(self, m: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::MarkStack::push(Heap::Base *m)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#push

    Parameters
    ----------

    m : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::MarkStack::push(Heap::Base *m)
    self.uglySide.call(
        'ritual_ZN3QV49MarkStack4pushEPNS_4Heap4BaseE', self._addressOf(m),
    )

  @overload()
  def drain(self) -> None:
    """
    Calls Qt's 'void QV4::MarkStack::drain()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#drain
    """
    #  void QV4::MarkStack::drain()
    self.uglySide.call('ritual_ZN3QV49MarkStack5drainEv')

  @overload(QDeadlineTimer)
  def drain(self, deadline: QDeadlineTimer) -> DrainState:
    """
    Calls Qt's 'DrainState QV4::MarkStack::drain(QDeadlineTimer deadline)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#drain

    Parameters
    ----------

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.

    Returns
    -------

    DrainState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DrainState(number)'
      gives.
    """
    #  DrainState QV4::MarkStack::drain(QDeadlineTimer deadline)
    return MarkStack.DrainState(self.uglySide.call(
        'ritual_ZN3QV49MarkStack5drainE14QDeadlineTimer',
        self._valueOf(deadline),
    ))

  def pop(self) -> Optional[QV4.Heap.Base]:
    """
    Calls Qt's 'Heap::Base *QV4::MarkStack::pop()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-markstack.html#pop

    Returns
    -------

    Optional[QV4.Heap.Base]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Base *QV4::MarkStack::pop()
    address = self.uglySide.call('ritual_ZN3QV49MarkStack3popEv')
    return QV4.Heap.Base._cuteAt(address)
