"""
QHostInfoLookupManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHostInfoLookupManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QHostInfoRunnable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostInfoRunnable = WAIT['QHostInfoRunnable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHostInfoLookupManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHostInfoLookupManager: a plain Python object
  standing in front of one C++ QHostInfoLookupManager.

  What exists
  -----------

  Every function of Qt's QHostInfoLookupManager that has a ritual and that
  Python can call so far, 5 names in all: 'clear', 'scheduleLookup',
  'abortLookup', 'lookupFinished', 'wasAborted'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHostInfoLookupManager::~QHostInfoLookupManager()': the destructor:
    Python never removes a C++ QHostInfoLookupManager.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QHostInfoLookupManager is created at the first use, not by
    'QHostInfoLookupManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHostInfoLookupManager.
  - Each name of Qt's QHostInfoLookupManager that has no cute function yet,
    'rescheduleWithMutexHeld', holds a function that raises
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
  __qt_class__ = 'QHostInfoLookupManager'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QHostInfoLookupManager::QHostInfoLookupManager()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostinfolookupmanager.html#QHostInfoLookupManager
    """
    #  QHostInfoLookupManager::QHostInfoLookupManager()
    self._noteCreation(QHostInfoLookupManager, lambda: Rituals.call(
        'ritual_ZN22QHostInfoLookupManagerC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QHostInfoLookupManager::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfolookupmanager.html#clear
    """
    #  void QHostInfoLookupManager::clear()
    self.uglySide.call('ritual_ZN22QHostInfoLookupManager5clearEv')

  @overload(QHostInfoRunnable)
  @overload(NoneType)
  def scheduleLookup(self, r: Optional[QHostInfoRunnable]) -> None:
    """
    Calls Qt's 'void QHostInfoLookupManager::scheduleLookup(QHostInfoRunnable
    *r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostinfolookupmanager.html#scheduleLookup

    Parameters
    ----------

    r : Optional[QHostInfoRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHostInfoLookupManager::scheduleLookup(QHostInfoRunnable *r)
    self.uglySide.call(
        'ritual_ZN22QHostInfoLookupManager14scheduleLookupEP17QHostInfoRunn'
        'able',
        self._addressOf(r),
    )

  @overload(int)
  def abortLookup(self, id: int) -> None:
    """
    Calls Qt's 'void QHostInfoLookupManager::abortLookup(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostinfolookupmanager.html#abortLookup

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QHostInfoLookupManager::abortLookup(int id)
    self.uglySide.call(
        'ritual_ZN22QHostInfoLookupManager11abortLookupEi', id,
    )

  @overload(QHostInfoRunnable)
  @overload(NoneType)
  def lookupFinished(self, r: Optional[QHostInfoRunnable]) -> None:
    """
    Calls Qt's 'void QHostInfoLookupManager::lookupFinished(QHostInfoRunnable
    *r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostinfolookupmanager.html#lookupFinished

    Parameters
    ----------

    r : Optional[QHostInfoRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHostInfoLookupManager::lookupFinished(QHostInfoRunnable *r)
    self.uglySide.call(
        'ritual_ZN22QHostInfoLookupManager14lookupFinishedEP17QHostInfoRunn'
        'able',
        self._addressOf(r),
    )

  @overload(int)
  def wasAborted(self, id: int) -> bool:
    """
    Calls Qt's 'bool QHostInfoLookupManager::wasAborted(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostinfolookupmanager.html#wasAborted

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QHostInfoLookupManager::wasAborted(int id)
    return self.uglySide.call(
        'ritual_ZN22QHostInfoLookupManager10wasAbortedEi', id,
    )

  @staticmethod
  def rescheduleWithMutexHeld(*__, **_) -> Never:
    """
    Qt's 'void QHostInfoLookupManager::rescheduleWithMutexHeld()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'separate_if'.
    """
    raise NotImplementedError(
        "'QHostInfoLookupManager.rescheduleWithMutexHeld' has no cute "
        "function yet. Qt's 'void "
        "QHostInfoLookupManager::rescheduleWithMutexHeld()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'separate_if'.")
