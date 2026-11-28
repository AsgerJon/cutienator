"""
QSystemSemaphoreWin32 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSystemSemaphoreWin32 to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QNativeIpcKey

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSystemSemaphoreWin32(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemSemaphoreWin32: a plain Python object standing
  in front of one C++ QSystemSemaphoreWin32.

  C++ hands a QSystemSemaphoreWin32 around as a copy, so every C++
  QSystemSemaphoreWin32 behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSystemSemaphoreWin32 that has a ritual and that
  Python can call so far, 2 names in all: 'supports', 'runtimeSupportCheck'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemSemaphoreWin32::~QSystemSemaphoreWin32()': the destructor:
    Python removes its C++ QSystemSemaphoreWin32 by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSystemSemaphoreWin32 is created at the first use, not by
    'QSystemSemaphoreWin32(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSystemSemaphoreWin32 back gives a copy the ritual
    made for Python, in a new cute QSystemSemaphoreWin32.
  - Each name of Qt's QSystemSemaphoreWin32 that has no cute function yet,
    'cleanHandle', 'handle', 'modifySemaphore', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def supports(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSystemSemaphoreWin32::supports(QNativeIpcKey::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphorewin32.html#supports

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSystemSemaphoreWin32::supports(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN21QSystemSemaphoreWin328supportsEN13QNativeIpcKey4TypeE',
        type.value,
    )

  @staticmethod
  def runtimeSupportCheck() -> bool:
    """
    Calls Qt's 'bool QSystemSemaphoreWin32::runtimeSupportCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphorewin32.html#runtimeSupportCheck
    """
    #  bool QSystemSemaphoreWin32::runtimeSupportCheck()
    return Rituals.call(
        'ritual_ZN21QSystemSemaphoreWin3219runtimeSupportCheckEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemSemaphoreWin32'

  #  Qt's '~QSystemSemaphoreWin32()'. Naming it makes this a value class:
  #  Python owns every C++ QSystemSemaphoreWin32 behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSystemSemaphoreWin32D1Ev'

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

  @staticmethod
  def cleanHandle(*__, **_) -> Never:
    """
    Qt's 'void QSystemSemaphoreWin32::cleanHandle(QSystemSemaphorePrivate
    *self_)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CloseHandle'.
    """
    raise NotImplementedError(
        "'QSystemSemaphoreWin32.cleanHandle' has no cute function yet. Qt's "
        "'void QSystemSemaphoreWin32::cleanHandle(QSystemSemaphorePrivate "
        "*self_)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'CloseHandle'.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QSystemSemaphoreWin32::handle(QSystemSemaphorePrivate
    *self_, QSystemSemaphore::AccessMode mode)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'HANDLE'; did you mean 'Qt::HANDLE'?.
    """
    raise NotImplementedError(
        "'QSystemSemaphoreWin32.handle' has no cute function yet. Qt's "
        "'Qt::HANDLE QSystemSemaphoreWin32::handle(QSystemSemaphorePrivate "
        "*self_, QSystemSemaphore::AccessMode mode)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'HANDLE'; did you mean "
        "'Qt::HANDLE'?.")

  @staticmethod
  def modifySemaphore(*__, **_) -> Never:
    """
    Qt's 'bool QSystemSemaphoreWin32::modifySemaphore(QSystemSemaphorePrivate
    *self_, int count)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'ReleaseSemaphore'.
    """
    raise NotImplementedError(
        "'QSystemSemaphoreWin32.modifySemaphore' has no cute function yet. "
        "Qt's 'bool "
        "QSystemSemaphoreWin32::modifySemaphore(QSystemSemaphorePrivate "
        "*self_, int count)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'ReleaseSemaphore'.")
