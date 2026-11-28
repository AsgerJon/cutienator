"""
QtPrivate::SlotObjSharedPtr binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qobjectdefs_impl.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class SlotObjSharedPtr(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::SlotObjSharedPtr: a plain Python object
  standing in front of one C++ QtPrivate::SlotObjSharedPtr.

  C++ hands a QtPrivate::SlotObjSharedPtr around as a copy, so every C++
  QtPrivate::SlotObjSharedPtr behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::SlotObjSharedPtr that has a ritual and
  that Python can call so far, 1 name in all: '__bool__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(std::nullptr_t a0)':
    takes in Python what 'QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr()'
    takes.
  - Qt's 'SlotObjSharedPtr &QtPrivate::SlotObjSharedPtr::operator=(const
    SlotObjSharedPtr &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(SlotObjSharedPtr
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'SlotObjSharedPtr
    &QtPrivate::SlotObjSharedPtr::operator=(SlotObjSharedPtr &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QtPrivate::SlotObjSharedPtr::~SlotObjSharedPtr()': the destructor:
    Python removes its C++ QtPrivate::SlotObjSharedPtr by it, and has no
    other use for it.
  - Qt's 'void QtPrivate::SlotObjSharedPtr::swap(SlotObjSharedPtr &other)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 3 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QtPrivate::SlotObjSharedPtr is created at the first use, not by
    'QtPrivate::SlotObjSharedPtr(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::SlotObjSharedPtr back gives a copy the
    ritual made for Python, in a new cute QtPrivate::SlotObjSharedPtr.
  - Each name of Qt's QtPrivate::SlotObjSharedPtr that has no cute function
    yet, 'get', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::SlotObjSharedPtr'

  #  Qt's '~QtPrivate::SlotObjSharedPtr()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::SlotObjSharedPtr behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate16SlotObjSharedPtrD1Ev'

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

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::SlotObjSharedPtr::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-slotobjsharedptr.html#operator bool
    """
    #  bool QtPrivate::SlotObjSharedPtr::operator bool() const
    return self.uglySide.call('ritual_ZNK9QtPrivate16SlotObjSharedPtrcvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-slotobjsharedptr.html#SlotObjSharedPtr
    """
    #  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr()
    self._noteCreation(SlotObjSharedPtr, lambda: Rituals.call(
        'ritual_ZN9QtPrivate16SlotObjSharedPtrC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: SlotObjSharedPtr) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(const SlotObjSharedPtr
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-slotobjsharedptr.html#SlotObjSharedPtr

    Parameters
    ----------

    other : SlotObjSharedPtr
      Passed on as a value: Qt reads the C++ QtPrivate::SlotObjSharedPtr,
      which stays Python's own.
    """
    #  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(const SlotObjSharedPtr
    #      &other)
    self._noteCreation(SlotObjSharedPtr, lambda: Rituals.call(
        'ritual_ZN9QtPrivate16SlotObjSharedPtrC1ERKS0_',
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
  def get(*__, **_) -> Never:
    """
    Qt's 'pointer QtPrivate::SlotObjSharedPtr::get() const': the compiler
    refuses its ritual as it would be written here: unknown type name
    'pointer'.
    """
    raise NotImplementedError(
        "'QtPrivate.SlotObjSharedPtr.get' has no cute function yet. Qt's "
        "'pointer QtPrivate::SlotObjSharedPtr::get() const': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'pointer'.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::SlotObjSharedPtr::swap(SlotObjSharedPtr &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtPrivate.SlotObjSharedPtr.swap' has no cute function yet. Qt's "
        "'void QtPrivate::SlotObjSharedPtr::swap(SlotObjSharedPtr &other)': "
        "takes a type Python has no way to hand over yet.")
