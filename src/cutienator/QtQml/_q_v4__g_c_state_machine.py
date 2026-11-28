"""
QV4::GCStateMachine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::GCStateMachine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class GCStateMachine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::GCStateMachine: a plain Python object standing
  in front of one C++ QV4::GCStateMachine.

  What exists
  -----------

  Every function of Qt's QV4::GCStateMachine that has a ritual and that
  Python can call so far, 5 names in all: 'step', 'inProgress', 'reset',
  'transition', 'handleTimeout'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 3 not a gap; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::GCStateMachine is created at the first use, not by
    'QV4::GCStateMachine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::GCStateMachine.
  - Each name of Qt's QV4::GCStateMachine that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QV4::GCStateMachine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class GCState(CuteNum):
    """
    The enum 'QV4::GCStateMachine::GCState' of Qt, with the 18 names Qt gives
    in it.
    """

    MarkStart = Kee[int](0)
    MarkGlobalObject = Kee[int](1)
    MarkJSStack = Kee[int](2)
    InitMarkPersistentValues = Kee[int](3)
    MarkPersistentValues = Kee[int](4)
    InitMarkWeakValues = Kee[int](5)
    MarkWeakValues = Kee[int](6)
    MarkDrain = Kee[int](7)
    MarkReady = Kee[int](8)
    InitCallDestroyObjects = Kee[int](9)
    CrossValidateIncrementalMarkPhase = Kee[int](10)
    CallDestroyObjects = Kee[int](11)
    FreeWeakMaps = Kee[int](12)
    FreeWeakSets = Kee[int](13)
    HandleQObjectWrappers = Kee[int](14)
    DoSweep = Kee[int](15)
    Invalid = Kee[int](16)
    Count = Kee[int](17)

  #  The classes Qt writes inside QV4::GCStateMachine, each a class in here
  #  as in C++.

  class GCStateInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::GCStateMachine::GCStateInfo: a plain Python
    object standing in front of one C++ QV4::GCStateMachine::GCStateInfo.

    C++ hands a QV4::GCStateMachine::GCStateInfo around as a copy, so every
    C++ QV4::GCStateMachine::GCStateInfo behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QV4::GCStateMachine::GCStateInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::GCStateMachine::GCStateInfo::~GCStateInfo()': the
      destructor: Python removes its C++ QV4::GCStateMachine::GCStateInfo by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::GCStateMachine::GCStateInfo is created at the first use,
      not by 'QV4::GCStateMachine::GCStateInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::GCStateMachine::GCStateInfo back gives a copy
      the ritual made for Python, in a new cute
      QV4::GCStateMachine::GCStateInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::GCStateMachine::GCStateInfo'

    #  Qt's '~QV4::GCStateMachine::GCStateInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::GCStateMachine::GCStateInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV414GCStateMachine11GCStateInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class StepTiming(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::GCStateMachine::StepTiming: a plain Python
    object standing in front of one C++ QV4::GCStateMachine::StepTiming.

    C++ hands a QV4::GCStateMachine::StepTiming around as a copy, so every
    C++ QV4::GCStateMachine::StepTiming behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QV4::GCStateMachine::StepTiming yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::GCStateMachine::StepTiming::~StepTiming()': the destructor:
      Python removes its C++ QV4::GCStateMachine::StepTiming by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QV4::GCStateMachine::StepTiming is created at the first use,
      not by 'QV4::GCStateMachine::StepTiming(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::GCStateMachine::StepTiming back gives a copy
      the ritual made for Python, in a new cute
      QV4::GCStateMachine::StepTiming.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::GCStateMachine::StepTiming'

    #  Qt's '~QV4::GCStateMachine::StepTiming()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::GCStateMachine::StepTiming
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV414GCStateMachine10StepTimingD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::GCStateMachine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QV4::GCStateMachine::GCStateMachine()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcGcStepExecution'.
    """
    raise NotImplementedError(
        "'QV4.GCStateMachine.__init__' has no cute function yet. Qt's "
        "'QV4::GCStateMachine::GCStateMachine()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'lcGcStepExecution'.")

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

  def step(self) -> None:
    """
    Calls Qt's 'void QV4::GCStateMachine::step()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-gcstatemachine.html#step
    """
    #  void QV4::GCStateMachine::step()
    self.uglySide.call('ritual_ZN3QV414GCStateMachine4stepEv')

  def inProgress(self) -> bool:
    """
    Calls Qt's 'bool QV4::GCStateMachine::inProgress()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-gcstatemachine.html#inProgress
    """
    #  bool QV4::GCStateMachine::inProgress()
    return self.uglySide.call('ritual_ZN3QV414GCStateMachine10inProgressEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QV4::GCStateMachine::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-gcstatemachine.html#reset
    """
    #  void QV4::GCStateMachine::reset()
    self.uglySide.call('ritual_ZN3QV414GCStateMachine5resetEv')

  def transition(self) -> None:
    """
    Calls Qt's 'void QV4::GCStateMachine::transition()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-gcstatemachine.html#transition
    """
    #  void QV4::GCStateMachine::transition()
    self.uglySide.call('ritual_ZN3QV414GCStateMachine10transitionEv')

  @overload(GCState)
  def handleTimeout(self, state: GCState) -> None:
    """
    Calls Qt's 'void QV4::GCStateMachine::handleTimeout(GCState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-gcstatemachine.html#handleTimeout

    Parameters
    ----------

    state : GCState
      Passed on as its number.
    """
    #  void QV4::GCStateMachine::handleTimeout(GCState state)
    self.uglySide.call(
        'ritual_ZN3QV414GCStateMachine13handleTimeoutENS0_7GCStateE',
        state.value,
    )
