"""
QFutureInterfaceBasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFutureInterfaceBasePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QFutureInterfaceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFutureCallOutInterface, QThreadPool
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFutureCallOutInterface = WAIT['QFutureCallOutInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFutureInterfaceBasePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFutureInterfaceBasePrivate: a plain Python object
  standing in front of one C++ QFutureInterfaceBasePrivate.

  What exists
  -----------

  Every function of Qt's QFutureInterfaceBasePrivate that has a ritual and
  that Python can call so far, 8 names in all: 'pool',
  'internal_resultCount', 'internal_isResultReadyAt',
  'internal_waitForNextResult', 'internal_setThrottled',
  'connectOutputInterface', 'disconnectOutputInterface', 'setState'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFutureInterfaceBasePrivate::~QFutureInterfaceBasePrivate()': the
    destructor: Python never removes a C++ QFutureInterfaceBasePrivate.
  - Qt's 'void QFutureInterfaceBasePrivate::sendCallOut(const
    QFutureCallOutEvent &callOut)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QFutureInterfaceBasePrivate::sendCallOuts(const
    QFutureCallOutEvent &callOut1, const QFutureCallOutEvent &callOut2)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QFutureInterfaceBasePrivate is created at the first use, not by
    'QFutureInterfaceBasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFutureInterfaceBasePrivate.
  - Each name of Qt's QFutureInterfaceBasePrivate that has no cute function
    yet, 'cancelImpl', 'internal_updateProgress',
    'internal_updateProgressValue', 'sendCallOut', 'sendCallOuts', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFutureInterfaceBasePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class CancelOption(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QFutureInterfaceBasePrivate::CancelOption' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QFutureInterfaceBasePrivate::CancelOptions'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    CancelContinuations = 0x1

  CancelOptions = CancelOption

  class ContinuationState(CuteNum):
    """
    The enum 'QFutureInterfaceBasePrivate::ContinuationState' of Qt, with the
    3 names Qt gives in it.
    """

    Default = Kee[int](0)
    Canceled = Kee[int](1)
    Cleaned = Kee[int](2)

  #  The classes Qt writes inside QFutureInterfaceBasePrivate, each a class
  #  in here as in C++.

  class Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFutureInterfaceBasePrivate::Data: a plain Python
    object standing in front of one C++ QFutureInterfaceBasePrivate::Data.

    What exists
    -----------

    No function of Qt's QFutureInterfaceBasePrivate::Data yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'void QFutureInterfaceBasePrivate::Data::setException(const
      std::exception_ptr &e)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QFutureInterfaceBasePrivate::Data::~Data()': the destructor:
      Python never removes a C++ QFutureInterfaceBasePrivate::Data.

    What to expect
    --------------

    - The C++ QFutureInterfaceBasePrivate::Data is created at the first use,
      not by 'QFutureInterfaceBasePrivate::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QFutureInterfaceBasePrivate::Data.
    - Each name of Qt's QFutureInterfaceBasePrivate::Data that has no cute
      function yet, 'setException', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFutureInterfaceBasePrivate::Data'

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

    @staticmethod
    def setException(*__, **_) -> Never:
      """
      Qt's 'void QFutureInterfaceBasePrivate::Data::setException(const
      std::exception_ptr &e)': takes a type Python has no way to hand over
      yet.
      """
      raise NotImplementedError(
          "'QFutureInterfaceBasePrivate.Data.setException' has no cute "
          "function yet. Qt's 'void "
          "QFutureInterfaceBasePrivate::Data::setException(const "
          "std::exception_ptr &e)': takes a type Python has no way to hand "
          "over yet.")

  class ProgressData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFutureInterfaceBasePrivate::ProgressData: a plain
    Python object standing in front of one C++
    QFutureInterfaceBasePrivate::ProgressData.

    C++ hands a QFutureInterfaceBasePrivate::ProgressData around as a copy,
    so every C++ QFutureInterfaceBasePrivate::ProgressData behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QFutureInterfaceBasePrivate::ProgressData yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFutureInterfaceBasePrivate::ProgressData::~ProgressData()': the
      destructor: Python removes its C++
      QFutureInterfaceBasePrivate::ProgressData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QFutureInterfaceBasePrivate::ProgressData is created at the
      first use, not by 'QFutureInterfaceBasePrivate::ProgressData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFutureInterfaceBasePrivate::ProgressData back
      gives a copy the ritual made for Python, in a new cute
      QFutureInterfaceBasePrivate::ProgressData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFutureInterfaceBasePrivate::ProgressData'

    #  Qt's '~QFutureInterfaceBasePrivate::ProgressData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QFutureInterfaceBasePrivate::ProgressData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN27QFutureInterfaceBasePrivate12ProgressDataD1Ev')

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

  class RefCount(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFutureInterfaceBasePrivate::RefCount: a plain
    Python object standing in front of one C++
    QFutureInterfaceBasePrivate::RefCount.

    C++ hands a QFutureInterfaceBasePrivate::RefCount around as a copy, so
    every C++ QFutureInterfaceBasePrivate::RefCount behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QFutureInterfaceBasePrivate::RefCount that has a
    ritual and that Python can call so far, 6 names in all: 'ref', 'deref',
    'load', 'refT', 'derefT', 'loadT'. It can be made from Python, in 1 way;
    see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFutureInterfaceBasePrivate::RefCount::~RefCount()': the
      destructor: Python removes its C++
      QFutureInterfaceBasePrivate::RefCount by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QFutureInterfaceBasePrivate::RefCount is created at the first
      use, not by 'QFutureInterfaceBasePrivate::RefCount(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFutureInterfaceBasePrivate::RefCount back gives a
      copy the ritual made for Python, in a new cute
      QFutureInterfaceBasePrivate::RefCount.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFutureInterfaceBasePrivate::RefCount'

    #  Qt's '~QFutureInterfaceBasePrivate::RefCount()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QFutureInterfaceBasePrivate::RefCount behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN27QFutureInterfaceBasePrivate8RefCountD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def load(self) -> int:
      """
      Calls Qt's 'int QFutureInterfaceBasePrivate::RefCount::load() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html#load
      """
      #  int QFutureInterfaceBasePrivate::RefCount::load() const
      return self.uglySide.call(
          'ritual_ZNK27QFutureInterfaceBasePrivate8RefCount4loadEv',
      )

    def loadT(self) -> int:
      """
      Calls Qt's 'int QFutureInterfaceBasePrivate::RefCount::loadT() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html#loadT
      """
      #  int QFutureInterfaceBasePrivate::RefCount::loadT() const
      return self.uglySide.call(
          'ritual_ZNK27QFutureInterfaceBasePrivate8RefCount5loadTEv',
      )

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

    @overload()
    @overload(int)
    @overload(int, int)
    def __init__(self, r: int = 0, rt: int = 0) -> None:
      """
      Notes what was given, for Qt's
      'QFutureInterfaceBasePrivate::RefCount::RefCount(int r, int rt)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html

      Parameters
      ----------

      r : int
        Passed on as it is. May be left out, as in Qt: it is then 0.

      rt : int
        Passed on as it is. May be left out, as in Qt: it is then 0.
      """
      #  QFutureInterfaceBasePrivate::RefCount::RefCount(int r, int rt)
      self._noteCreation(
          QFutureInterfaceBasePrivate.RefCount, lambda: Rituals.call(
              'ritual_ZN27QFutureInterfaceBasePrivate8RefCountC1Eii', r, rt,
          ))

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

    def ref(self) -> bool:
      """
      Calls Qt's 'bool QFutureInterfaceBasePrivate::RefCount::ref()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html#ref
      """
      #  bool QFutureInterfaceBasePrivate::RefCount::ref()
      return self.uglySide.call(
          'ritual_ZN27QFutureInterfaceBasePrivate8RefCount3refEv',
      )

    def deref(self) -> bool:
      """
      Calls Qt's 'bool QFutureInterfaceBasePrivate::RefCount::deref()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html#deref
      """
      #  bool QFutureInterfaceBasePrivate::RefCount::deref()
      return self.uglySide.call(
          'ritual_ZN27QFutureInterfaceBasePrivate8RefCount5derefEv',
      )

    def refT(self) -> bool:
      """
      Calls Qt's 'bool QFutureInterfaceBasePrivate::RefCount::refT()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html#refT
      """
      #  bool QFutureInterfaceBasePrivate::RefCount::refT()
      return self.uglySide.call(
          'ritual_ZN27QFutureInterfaceBasePrivate8RefCount4refTEv',
      )

    def derefT(self) -> bool:
      """
      Calls Qt's 'bool QFutureInterfaceBasePrivate::RefCount::derefT()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfutureinterfacebaseprivate-refcount.html#derefT
      """
      #  bool QFutureInterfaceBasePrivate::RefCount::derefT()
      return self.uglySide.call(
          'ritual_ZN27QFutureInterfaceBasePrivate8RefCount6derefTEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFutureInterfaceBasePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pool(self) -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QFutureInterfaceBasePrivate::pool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html#pool

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QFutureInterfaceBasePrivate::pool() const
    address = self.uglySide.call(
        'ritual_ZNK27QFutureInterfaceBasePrivate4poolEv',
    )
    from . import QThreadPool
    return QThreadPool._cuteAt(address)

  def internal_resultCount(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBasePrivate::internal_resultCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html
    """
    #  int QFutureInterfaceBasePrivate::internal_resultCount() const
    return self.uglySide.call(
        'ritual_ZNK27QFutureInterfaceBasePrivate20internal_resultCountEv',
    )

  @overload(int)
  def internal_isResultReadyAt(self, index: int) -> bool:
    """
    Calls Qt's 'bool
    QFutureInterfaceBasePrivate::internal_isResultReadyAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QFutureInterfaceBasePrivate::internal_isResultReadyAt(int index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK27QFutureInterfaceBasePrivate24internal_isResultReadyAtE'
        'i',
        index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFutureInterfaceBase.State)
  def setState(self, state: QFutureInterfaceBase.State) -> None:
    """
    Calls Qt's 'void
    QFutureInterfaceBasePrivate::setState(QFutureInterfaceBase::State
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html#setState

    Parameters
    ----------

    state : QFutureInterfaceBase.State
      Passed on as its number.
    """
    #  void QFutureInterfaceBasePrivate::setState(QFutureInterfaceBase::State
    #      state)
    self.uglySide.call(
        'ritual_ZN27QFutureInterfaceBasePrivate8setStateEN20QFutureInterfac'
        'eBase5StateE',
        state.value,
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

  @overload(QFutureInterfaceBase.State)
  def __init__(self, initialState: QFutureInterfaceBase.State) -> None:
    """
    Notes what was given, for Qt's
    'QFutureInterfaceBasePrivate::QFutureInterfaceBasePrivate(
    QFutureInterfaceBase::State initialState)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html

    Parameters
    ----------

    initialState : QFutureInterfaceBase.State
      Passed on as its number.
    """
    #  QFutureInterfaceBasePrivate::QFutureInterfaceBasePrivate(
    #      QFutureInterfaceBase::State initialState)
    self._noteCreation(QFutureInterfaceBasePrivate, lambda: Rituals.call(
        'ritual_ZN27QFutureInterfaceBasePrivateC1EN20QFutureInterfaceBase5S'
        'tateE',
        initialState.value,
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

  def internal_waitForNextResult(self) -> bool:
    """
    Calls Qt's 'bool
    QFutureInterfaceBasePrivate::internal_waitForNextResult()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html
    """
    #  bool QFutureInterfaceBasePrivate::internal_waitForNextResult()
    return self.uglySide.call(
        'ritual_ZN27QFutureInterfaceBasePrivate26internal_waitForNextResult'
        'Ev',
    )

  @overload(bool)
  def internal_setThrottled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBasePrivate::internal_setThrottled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBasePrivate::internal_setThrottled(bool enable)
    self.uglySide.call(
        'ritual_ZN27QFutureInterfaceBasePrivate21internal_setThrottledEb',
        enable,
    )

  @overload(QFutureCallOutInterface)
  @overload(NoneType)
  def connectOutputInterface(
      self,
      iface: Optional[QFutureCallOutInterface],
  ) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBasePrivate::connectOutputInterface(
    QFutureCallOutInterface *iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html

    Parameters
    ----------

    iface : Optional[QFutureCallOutInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFutureInterfaceBasePrivate::connectOutputInterface(
    #      QFutureCallOutInterface *iface)
    self.uglySide.call(
        'ritual_ZN27QFutureInterfaceBasePrivate22connectOutputInterfaceEP23'
        'QFutureCallOutInterface',
        self._addressOf(iface, 'QFutureCallOutInterface'),
    )

  @overload(QFutureCallOutInterface)
  @overload(NoneType)
  def disconnectOutputInterface(
      self,
      iface: Optional[QFutureCallOutInterface],
  ) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBasePrivate::disconnectOutputInterface(
    QFutureCallOutInterface *iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebaseprivate.html

    Parameters
    ----------

    iface : Optional[QFutureCallOutInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFutureInterfaceBasePrivate::disconnectOutputInterface(
    #      QFutureCallOutInterface *iface)
    self.uglySide.call(
        'ritual_ZN27QFutureInterfaceBasePrivate25disconnectOutputInterfaceE'
        'P23QFutureCallOutInterface',
        self._addressOf(iface, 'QFutureCallOutInterface'),
    )

  @staticmethod
  def cancelImpl(*__, **_) -> Never:
    """
    Qt's 'void
    QFutureInterfaceBasePrivate::cancelImpl(QFutureInterfaceBase::CancelMode
    mode, CancelOptions options)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'suspendingOrSuspended'.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBasePrivate.cancelImpl' has no cute function yet. "
        "Qt's 'void "
        "QFutureInterfaceBasePrivate::cancelImpl(QFutureInterfaceBase::Cance"
        "lMode mode, CancelOptions options)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'suspendingOrSuspended'.")

  @staticmethod
  def internal_updateProgress(*__, **_) -> Never:
    """
    Qt's 'bool QFutureInterfaceBasePrivate::internal_updateProgress(int
    progress, const QString &progressText)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'MaxProgressEmitsPerSecond'.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBasePrivate.internal_updateProgress' has no cute "
        "function yet. Qt's 'bool "
        "QFutureInterfaceBasePrivate::internal_updateProgress(int progress, "
        "const QString &progressText)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'MaxProgressEmitsPerSecond'.")

  @staticmethod
  def internal_updateProgressValue(*__, **_) -> Never:
    """
    Qt's 'bool QFutureInterfaceBasePrivate::internal_updateProgressValue(int
    progress)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'MaxProgressEmitsPerSecond'.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBasePrivate.internal_updateProgressValue' has no "
        "cute function yet. Qt's 'bool "
        "QFutureInterfaceBasePrivate::internal_updateProgressValue(int "
        "progress)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'MaxProgressEmitsPerSecond'.")

  @staticmethod
  def sendCallOut(*__, **_) -> Never:
    """
    Qt's 'void QFutureInterfaceBasePrivate::sendCallOut(const
    QFutureCallOutEvent &callOut)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBasePrivate.sendCallOut' has no cute function "
        "yet. Qt's 'void QFutureInterfaceBasePrivate::sendCallOut(const "
        "QFutureCallOutEvent &callOut)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def sendCallOuts(*__, **_) -> Never:
    """
    Qt's 'void QFutureInterfaceBasePrivate::sendCallOuts(const
    QFutureCallOutEvent &callOut1, const QFutureCallOutEvent &callOut2)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBasePrivate.sendCallOuts' has no cute function "
        "yet. Qt's 'void QFutureInterfaceBasePrivate::sendCallOuts(const "
        "QFutureCallOutEvent &callOut1, const QFutureCallOutEvent "
        "&callOut2)': takes a type Python has no way to hand over yet.")
