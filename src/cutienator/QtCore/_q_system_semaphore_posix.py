"""
QSystemSemaphorePosix binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSystemSemaphorePosix to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNativeIpcKey, QSystemSemaphore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSystemSemaphorePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSystemSemaphorePrivate = WAIT['QSystemSemaphorePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemSemaphorePosix(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemSemaphorePosix: a plain Python object standing
  in front of one C++ QSystemSemaphorePosix.

  C++ hands a QSystemSemaphorePosix around as a copy, so every C++
  QSystemSemaphorePosix behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSystemSemaphorePosix that has a ritual and that
  Python can call so far, 5 names in all: 'supports', 'runtimeSupportCheck',
  'handle', 'cleanHandle', 'modifySemaphore'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemSemaphorePosix::~QSystemSemaphorePosix()': the destructor:
    Python removes its C++ QSystemSemaphorePosix by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSystemSemaphorePosix is created at the first use, not by
    'QSystemSemaphorePosix(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSystemSemaphorePosix back gives a copy the ritual
    made for Python, in a new cute QSystemSemaphorePosix.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def supports(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSystemSemaphorePosix::supports(QNativeIpcKey::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreposix.html#supports

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSystemSemaphorePosix::supports(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN21QSystemSemaphorePosix8supportsEN13QNativeIpcKey4TypeE',
        type.value,
    )

  @staticmethod
  def runtimeSupportCheck() -> bool:
    """
    Calls Qt's 'bool QSystemSemaphorePosix::runtimeSupportCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreposix.html#runtimeSupportCheck
    """
    #  bool QSystemSemaphorePosix::runtimeSupportCheck()
    return Rituals.call(
        'ritual_ZN21QSystemSemaphorePosix19runtimeSupportCheckEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemSemaphorePosix'

  #  Qt's '~QSystemSemaphorePosix()'. Naming it makes this a value class:
  #  Python owns every C++ QSystemSemaphorePosix behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSystemSemaphorePosixD1Ev'

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

  @overload(QSystemSemaphorePrivate, QSystemSemaphore.AccessMode)
  @overload(NoneType, QSystemSemaphore.AccessMode)
  def handle(
      self,
      self_: Optional[QSystemSemaphorePrivate],
      mode: QSystemSemaphore.AccessMode,
  ) -> bool:
    """
    Calls Qt's 'bool QSystemSemaphorePosix::handle(QSystemSemaphorePrivate
    *self_, QSystemSemaphore::AccessMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphoreposix.html#handle

    Parameters
    ----------

    self_ : Optional[QSystemSemaphorePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QSystemSemaphore.AccessMode
      Passed on as its number.
    """
    #  bool QSystemSemaphorePosix::handle(QSystemSemaphorePrivate *self_,
    #      QSystemSemaphore::AccessMode mode)
    return self.uglySide.call(
        'ritual_ZN21QSystemSemaphorePosix6handleEP23QSystemSemaphorePrivate'
        'N16QSystemSemaphore10AccessModeE',
        self._addressOf(self_), mode.value,
    )

  @overload(QSystemSemaphorePrivate)
  @overload(NoneType)
  def cleanHandle(self, self_: Optional[QSystemSemaphorePrivate]) -> None:
    """
    Calls Qt's 'void
    QSystemSemaphorePosix::cleanHandle(QSystemSemaphorePrivate *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreposix.html#cleanHandle

    Parameters
    ----------

    self_ : Optional[QSystemSemaphorePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSystemSemaphorePosix::cleanHandle(QSystemSemaphorePrivate
    #      *self_)
    self.uglySide.call(
        'ritual_ZN21QSystemSemaphorePosix11cleanHandleEP23QSystemSemaphoreP'
        'rivate',
        self._addressOf(self_),
    )

  @overload(QSystemSemaphorePrivate, int)
  @overload(NoneType, int)
  def modifySemaphore(
      self,
      self_: Optional[QSystemSemaphorePrivate],
      count: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QSystemSemaphorePosix::modifySemaphore(QSystemSemaphorePrivate *self_,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreposix.html#modifySemaphore

    Parameters
    ----------

    self_ : Optional[QSystemSemaphorePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  bool QSystemSemaphorePosix::modifySemaphore(QSystemSemaphorePrivate
    #      *self_, int count)
    return self.uglySide.call(
        'ritual_ZN21QSystemSemaphorePosix15modifySemaphoreEP23QSystemSemaph'
        'orePrivatei',
        self._addressOf(self_), count,
    )
