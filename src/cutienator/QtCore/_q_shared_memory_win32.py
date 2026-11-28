"""
QSharedMemoryWin32 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSharedMemoryWin32 to be private: it declares the class in a
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


class QSharedMemoryWin32(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSharedMemoryWin32: a plain Python object standing in
  front of one C++ QSharedMemoryWin32.

  C++ hands a QSharedMemoryWin32 around as a copy, so every C++
  QSharedMemoryWin32 behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSharedMemoryWin32 that has a ritual and that Python
  can call so far, 2 names in all: 'runtimeSupportCheck', 'supports'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSharedMemoryWin32::~QSharedMemoryWin32()': the destructor: Python
    removes its C++ QSharedMemoryWin32 by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 8 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSharedMemoryWin32 is created at the first use, not by
    'QSharedMemoryWin32(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSharedMemoryWin32 back gives a copy the ritual made
    for Python, in a new cute QSharedMemoryWin32.
  - Each name of Qt's QSharedMemoryWin32 that has no cute function yet,
    'attach', 'cleanHandle', 'create', 'detach', 'handle', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def runtimeSupportCheck() -> bool:
    """
    Calls Qt's 'bool QSharedMemoryWin32::runtimeSupportCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemorywin32.html#runtimeSupportCheck
    """
    #  bool QSharedMemoryWin32::runtimeSupportCheck()
    return Rituals.call(
        'ritual_ZN18QSharedMemoryWin3219runtimeSupportCheckEv',
    )

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def supports(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryWin32::supports(QNativeIpcKey::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemorywin32.html#supports

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSharedMemoryWin32::supports(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN18QSharedMemoryWin328supportsEN13QNativeIpcKey4TypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSharedMemoryWin32'

  #  Qt's '~QSharedMemoryWin32()'. Naming it makes this a value class: Python
  #  owns every C++ QSharedMemoryWin32 behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSharedMemoryWin32D1Ev'

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
  def attach(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemoryWin32::attach(QSharedMemoryPrivate *self_,
    QSharedMemory::AccessMode mode)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'FILE_MAP_READ'.
    """
    raise NotImplementedError(
        "'QSharedMemoryWin32.attach' has no cute function yet. Qt's 'bool "
        "QSharedMemoryWin32::attach(QSharedMemoryPrivate *self_, "
        "QSharedMemory::AccessMode mode)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'FILE_MAP_READ'.")

  @staticmethod
  def cleanHandle(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemoryWin32::cleanHandle(QSharedMemoryPrivate *self_)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'CloseHandle'.
    """
    raise NotImplementedError(
        "'QSharedMemoryWin32.cleanHandle' has no cute function yet. Qt's "
        "'bool QSharedMemoryWin32::cleanHandle(QSharedMemoryPrivate "
        "*self_)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'CloseHandle'.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemoryWin32::create(QSharedMemoryPrivate *self_,
    qsizetype size)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name 'DWORD'.
    """
    raise NotImplementedError(
        "'QSharedMemoryWin32.create' has no cute function yet. Qt's 'bool "
        "QSharedMemoryWin32::create(QSharedMemoryPrivate *self_, qsizetype "
        "size)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'DWORD'.")

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemoryWin32::detach(QSharedMemoryPrivate *self_)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'UnmapViewOfFile'.
    """
    raise NotImplementedError(
        "'QSharedMemoryWin32.detach' has no cute function yet. Qt's 'bool "
        "QSharedMemoryWin32::detach(QSharedMemoryPrivate *self_)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'UnmapViewOfFile'.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QSharedMemoryWin32::handle(QSharedMemoryPrivate
    *self_)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'HANDLE'; did you
    mean 'Qt::HANDLE'?.
    """
    raise NotImplementedError(
        "'QSharedMemoryWin32.handle' has no cute function yet. Qt's "
        "'Qt::HANDLE QSharedMemoryWin32::handle(QSharedMemoryPrivate "
        "*self_)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'HANDLE'; did you mean 'Qt::HANDLE'?.")
