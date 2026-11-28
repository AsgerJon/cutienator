"""
QSharedMemoryLocker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSharedMemoryLocker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSharedMemory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSharedMemory = WAIT['QSharedMemory']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSharedMemoryLocker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSharedMemoryLocker: a plain Python object standing
  in front of one C++ QSharedMemoryLocker.

  What exists
  -----------

  Every function of Qt's QSharedMemoryLocker that has a ritual and that
  Python can call so far, 1 name in all: 'lock'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSharedMemoryLocker::QSharedMemoryLocker(QSharedMemoryLocker
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QSharedMemoryLocker
    &QSharedMemoryLocker::operator=(QSharedMemoryLocker &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QSharedMemoryLocker::swap(QSharedMemoryLocker &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QSharedMemoryLocker::~QSharedMemoryLocker()': the destructor:
    Python never removes a C++ QSharedMemoryLocker.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSharedMemoryLocker is created at the first use, not by
    'QSharedMemoryLocker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSharedMemoryLocker.
  - Each name of Qt's QSharedMemoryLocker that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QSharedMemoryLocker'

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

  @overload(QSharedMemory)
  @overload(NoneType)
  def __init__(self, sharedMemory: Optional[QSharedMemory]) -> None:
    """
    Notes what was given, for Qt's
    'QSharedMemoryLocker::QSharedMemoryLocker(QSharedMemory *sharedMemory)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemorylocker.html#QSharedMemoryLocker

    Parameters
    ----------

    sharedMemory : Optional[QSharedMemory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSharedMemoryLocker::QSharedMemoryLocker(QSharedMemory *sharedMemory)
    self._noteCreation(QSharedMemoryLocker, lambda: Rituals.call(
        'ritual_ZN19QSharedMemoryLockerC1EP13QSharedMemory',
        self._addressOf(sharedMemory),
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

  def lock(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryLocker::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemorylocker.html#lock
    """
    #  bool QSharedMemoryLocker::lock()
    return self.uglySide.call('ritual_ZN19QSharedMemoryLocker4lockEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSharedMemoryLocker::swap(QSharedMemoryLocker &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSharedMemoryLocker.swap' has no cute function yet. Qt's 'void "
        "QSharedMemoryLocker::swap(QSharedMemoryLocker &other)': takes a "
        "type Python has no way to hand over yet.")
