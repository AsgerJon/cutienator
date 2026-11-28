"""
QtTaskTree::StorageBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class StorageBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::StorageBase: a plain Python object
  standing in front of one C++ QtTaskTree::StorageBase.

  What exists
  -----------

  Every function of Qt's QtTaskTree::StorageBase that has a ritual and that
  Python can call so far, 2 names in all: '__eq__', '__ne__'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::StorageBase::StorageBase(StorageBase &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QtTaskTree::StorageBase::swap(StorageBase &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::StorageBase::StorageBase(const StorageCreator
    &creator)': takes a type Python has no way to hand over yet.
  - Qt's 'void *QtTaskTree::StorageBase::activeStorageVoid() const': gives
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 2 leans on
  'QExplicitlySharedDataPointer<QtTaskTree; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QtTaskTree::StorageBase is created at the first use, not by
    'QtTaskTree::StorageBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::StorageBase.
  - Each name of Qt's QtTaskTree::StorageBase that has no cute function yet,
    'activeStorageVoid', 'swap', holds a function that raises
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
  __qt_class__ = 'QtTaskTree::StorageBase'

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

  @overload(THIS)
  def __eq__(self, second: StorageBase) -> bool:
    """
    Calls Qt's 'bool operator==(const StorageBase &first, const StorageBase
    &second)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-storagebase.html#operator==

    Parameters
    ----------

    second : StorageBase
      Passed on as a value: Qt reads the C++ QtTaskTree::StorageBase, which
      stays Python's own.
    """
    #  bool operator==(const StorageBase &first, const StorageBase &second)
    return Rituals.call(
        'ritual_ZN10QtTaskTreeeqERKNS_11StorageBaseES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(second),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, second: StorageBase) -> bool:
    """
    Calls Qt's 'bool operator!=(const StorageBase &first, const StorageBase
    &second)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-storagebase.html#operator!=

    Parameters
    ----------

    second : StorageBase
      Passed on as a value: Qt reads the C++ QtTaskTree::StorageBase, which
      stays Python's own.
    """
    #  bool operator!=(const StorageBase &first, const StorageBase &second)
    return Rituals.call(
        'ritual_ZN10QtTaskTreeneERKNS_11StorageBaseES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(second),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, other: StorageBase) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::StorageBase::StorageBase(const StorageBase &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-storagebase.html#StorageBase

    Parameters
    ----------

    other : StorageBase
      Passed on as a value: Qt reads the C++ QtTaskTree::StorageBase, which
      stays Python's own.
    """
    #  QtTaskTree::StorageBase::StorageBase(const StorageBase &other)
    self._noteCreation(StorageBase, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree11StorageBaseC1ERKS0_', self._valueOf(other),
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
  def activeStorageVoid(*__, **_) -> Never:
    """
    Qt's 'void *QtTaskTree::StorageBase::activeStorageVoid() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.StorageBase.activeStorageVoid' has no cute function "
        "yet. Qt's 'void *QtTaskTree::StorageBase::activeStorageVoid() "
        "const': gives 'void', which has no cute class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::StorageBase::swap(StorageBase &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.StorageBase.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::StorageBase::swap(StorageBase &other)': takes a type "
        "Python has no way to hand over yet.")
