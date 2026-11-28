"""
QOrderedMutexLocker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qorderedmutexlocker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QOrderedMutexLocker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBasicMutex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBasicMutex = WAIT['QBasicMutex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOrderedMutexLocker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOrderedMutexLocker: a plain Python object standing
  in front of one C++ QOrderedMutexLocker.

  What exists
  -----------

  Every function of Qt's QOrderedMutexLocker that has a ritual and that
  Python can call so far, 3 names in all: 'relock', 'dismiss', 'unlock'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOrderedMutexLocker::swap(QOrderedMutexLocker &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QOrderedMutexLocker
    &QOrderedMutexLocker::operator=(QOrderedMutexLocker &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOrderedMutexLocker::QOrderedMutexLocker(QOrderedMutexLocker
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOrderedMutexLocker::~QOrderedMutexLocker()': the destructor:
    Python never removes a C++ QOrderedMutexLocker.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QOrderedMutexLocker is created at the first use, not by
    'QOrderedMutexLocker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOrderedMutexLocker.
  - Each name of Qt's QOrderedMutexLocker that has no cute function yet,
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
  __qt_class__ = 'QOrderedMutexLocker'

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

  @overload(QBasicMutex, QBasicMutex)
  @overload(QBasicMutex, NoneType)
  @overload(NoneType, QBasicMutex)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      m1: Optional[QBasicMutex],
      m2: Optional[QBasicMutex],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOrderedMutexLocker::QOrderedMutexLocker(QBasicMutex *m1, QBasicMutex
    *m2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qorderedmutexlocker.html#QOrderedMutexLocker

    Parameters
    ----------

    m1 : Optional[QBasicMutex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m2 : Optional[QBasicMutex]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOrderedMutexLocker::QOrderedMutexLocker(QBasicMutex *m1, QBasicMutex
    #      *m2)
    self._noteCreation(QOrderedMutexLocker, lambda: Rituals.call(
        'ritual_ZN19QOrderedMutexLockerC1EP11QBasicMutexS1_',
        self._addressOf(m1), self._addressOf(m2),
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

  @overload()
  def relock(self) -> None:
    """
    Calls Qt's 'void QOrderedMutexLocker::relock()'.

    Qt's own words: https://doc.qt.io/qt-6/qorderedmutexlocker.html#relock
    """
    #  void QOrderedMutexLocker::relock()
    self.uglySide.call('ritual_ZN19QOrderedMutexLocker6relockEv')

  @staticmethod
  @overload(QBasicMutex, QBasicMutex)
  @overload(QBasicMutex, NoneType)
  @overload(NoneType, QBasicMutex)
  @overload(NoneType, NoneType)
  def relock(
      mtx1: Optional[QBasicMutex],
      mtx2: Optional[QBasicMutex],
  ) -> bool:
    """
    Calls Qt's 'bool QOrderedMutexLocker::relock(QBasicMutex *mtx1,
    QBasicMutex *mtx2)'.

    Qt's own words: https://doc.qt.io/qt-6/qorderedmutexlocker.html#relock

    Parameters
    ----------

    mtx1 : Optional[QBasicMutex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mtx2 : Optional[QBasicMutex]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOrderedMutexLocker::relock(QBasicMutex *mtx1, QBasicMutex *mtx2)
    return Rituals.call(
        'ritual_ZN19QOrderedMutexLocker6relockEP11QBasicMutexS1_',
        CuteMixin._addressOf(mtx1), CuteMixin._addressOf(mtx2),
    )

  def dismiss(self) -> None:
    """
    Calls Qt's 'void QOrderedMutexLocker::dismiss()'.

    Qt's own words: https://doc.qt.io/qt-6/qorderedmutexlocker.html#dismiss
    """
    #  void QOrderedMutexLocker::dismiss()
    self.uglySide.call('ritual_ZN19QOrderedMutexLocker7dismissEv')

  def unlock(self) -> None:
    """
    Calls Qt's 'void QOrderedMutexLocker::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qorderedmutexlocker.html#unlock
    """
    #  void QOrderedMutexLocker::unlock()
    self.uglySide.call('ritual_ZN19QOrderedMutexLocker6unlockEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOrderedMutexLocker::swap(QOrderedMutexLocker &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOrderedMutexLocker.swap' has no cute function yet. Qt's 'void "
        "QOrderedMutexLocker::swap(QOrderedMutexLocker &other)': takes a "
        "type Python has no way to hand over yet.")
