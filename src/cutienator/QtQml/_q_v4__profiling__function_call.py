"""
QV4::Profiling::FunctionCall binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4profiling_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Profiling::FunctionCall to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FunctionCall(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Profiling::FunctionCall: a plain Python object
  standing in front of one C++ QV4::Profiling::FunctionCall.

  C++ hands a QV4::Profiling::FunctionCall around as a copy, so every C++
  QV4::Profiling::FunctionCall behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::Profiling::FunctionCall that has a ritual and
  that Python can call so far, 3 names in all: 'function', 'resolveLocation',
  'properties'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Profiling::FunctionCall::FunctionCall(FunctionCall &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QV4::Profiling::FunctionCall::~FunctionCall()': the destructor:
    Python removes its C++ QV4::Profiling::FunctionCall by it, and has no
    other use for it.
  - Qt's 'FunctionCall &QV4::Profiling::FunctionCall::operator=(const
    FunctionCall &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'FunctionCall &QV4::Profiling::FunctionCall::operator=(FunctionCall
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QV4::Profiling::FunctionCall::swap(FunctionCall &other)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QV4::Profiling::FunctionCall is created at the first use, not by
    'QV4::Profiling::FunctionCall(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Profiling::FunctionCall back gives a copy the
    ritual made for Python, in a new cute QV4::Profiling::FunctionCall.
  - Each name of Qt's QV4::Profiling::FunctionCall that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Profiling::FunctionCall'

  #  Qt's '~QV4::Profiling::FunctionCall()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::Profiling::FunctionCall behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV49Profiling12FunctionCallD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def function(self) -> Optional[QV4.Function]:
    """
    Calls Qt's 'Function *QV4::Profiling::FunctionCall::function() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-functioncall.html#function

    Returns
    -------

    Optional[QV4.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Function *QV4::Profiling::FunctionCall::function() const
    address = self.uglySide.call(
        'ritual_ZNK3QV49Profiling12FunctionCall8functionEv',
    )
    return QV4.Function._cuteAt(address)

  def resolveLocation(self) -> QV4.Profiling.FunctionLocation:
    """
    Calls Qt's 'FunctionLocation
    QV4::Profiling::FunctionCall::resolveLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-functioncall.html#resolveLocation

    Returns
    -------

    QV4.Profiling.FunctionLocation
      A new cute QV4::Profiling::FunctionLocation around the copy Qt gave
      back. Python owns it.
    """
    #  FunctionLocation QV4::Profiling::FunctionCall::resolveLocation() const
    address = self.uglySide.call(
        'ritual_ZNK3QV49Profiling12FunctionCall15resolveLocationEv',
    )
    return QV4.Profiling.FunctionLocation._cuteOwning(address)

  def properties(self) -> QV4.Profiling.FunctionCallProperties:
    """
    Calls Qt's 'FunctionCallProperties
    QV4::Profiling::FunctionCall::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-functioncall.html#properties

    Returns
    -------

    QV4.Profiling.FunctionCallProperties
      A new cute QV4::Profiling::FunctionCallProperties around the copy Qt
      gave back. Python owns it.
    """
    #  FunctionCallProperties QV4::Profiling::FunctionCall::properties()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV49Profiling12FunctionCall10propertiesEv',
    )
    return QV4.Profiling.FunctionCallProperties._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Profiling::FunctionCall::FunctionCall()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-functioncall.html#FunctionCall
    """
    #  QV4::Profiling::FunctionCall::FunctionCall()
    self._noteCreation(FunctionCall, lambda: Rituals.call(
        'ritual_ZN3QV49Profiling12FunctionCallC1Ev',
    ))

  @overload(WAIT['QV4.Function'], int, int)
  @overload(NoneType, int, int)
  def __init__(
      self,
      function: Optional[QV4.Function],
      start: int,
      end: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Profiling::FunctionCall::FunctionCall(Function *function, qint64
    start, qint64 end)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-functioncall.html#FunctionCall

    Parameters
    ----------

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  QV4::Profiling::FunctionCall::FunctionCall(Function *function, qint64
    #      start, qint64 end)
    self._noteCreation(FunctionCall, lambda: Rituals.call(
        'ritual_ZN3QV49Profiling12FunctionCallC1EPNS_8FunctionExx',
        self._addressOf(function), start, end,
    ))

  @overload(THIS)
  def __init__(self, other: FunctionCall) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Profiling::FunctionCall::FunctionCall(const FunctionCall &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-functioncall.html#FunctionCall

    Parameters
    ----------

    other : FunctionCall
      Passed on as a value: Qt reads the C++ QV4::Profiling::FunctionCall,
      which stays Python's own.
    """
    #  QV4::Profiling::FunctionCall::FunctionCall(const FunctionCall &other)
    self._noteCreation(FunctionCall, lambda: Rituals.call(
        'ritual_ZN3QV49Profiling12FunctionCallC1ERKS1_',
        self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QV4::Profiling::FunctionCall::swap(FunctionCall &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Profiling.FunctionCall.swap' has no cute function yet. Qt's "
        "'void QV4::Profiling::FunctionCall::swap(FunctionCall &other)': "
        "takes a type Python has no way to hand over yet.")
