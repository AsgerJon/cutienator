"""
QSharedMemoryPosix binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSharedMemoryPosix to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNativeIpcKey, QSharedMemory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSharedMemoryPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSharedMemoryPrivate = WAIT['QSharedMemoryPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSharedMemoryPosix(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSharedMemoryPosix: a plain Python object standing in
  front of one C++ QSharedMemoryPosix.

  C++ hands a QSharedMemoryPosix around as a copy, so every C++
  QSharedMemoryPosix behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSharedMemoryPosix that has a ritual and that Python
  can call so far, 7 names in all: 'supports', 'runtimeSupportCheck',
  'handle', 'cleanHandle', 'create', 'attach', 'detach'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSharedMemoryPosix::~QSharedMemoryPosix()': the destructor: Python
    removes its C++ QSharedMemoryPosix by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSharedMemoryPosix is created at the first use, not by
    'QSharedMemoryPosix(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSharedMemoryPosix back gives a copy the ritual made
    for Python, in a new cute QSharedMemoryPosix.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def supports(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::supports(QNativeIpcKey::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryposix.html#supports

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSharedMemoryPosix::supports(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN18QSharedMemoryPosix8supportsEN13QNativeIpcKey4TypeE',
        type.value,
    )

  @staticmethod
  def runtimeSupportCheck() -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::runtimeSupportCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryposix.html#runtimeSupportCheck
    """
    #  bool QSharedMemoryPosix::runtimeSupportCheck()
    return Rituals.call(
        'ritual_ZN18QSharedMemoryPosix19runtimeSupportCheckEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSharedMemoryPosix'

  #  Qt's '~QSharedMemoryPosix()'. Naming it makes this a value class: Python
  #  owns every C++ QSharedMemoryPosix behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSharedMemoryPosixD1Ev'

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

  @overload(QSharedMemoryPrivate)
  @overload(NoneType)
  def handle(self, self_: Optional[QSharedMemoryPrivate]) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::handle(QSharedMemoryPrivate
    *self_)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryposix.html#handle

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSharedMemoryPosix::handle(QSharedMemoryPrivate *self_)
    return self.uglySide.call(
        'ritual_ZN18QSharedMemoryPosix6handleEP20QSharedMemoryPrivate',
        self._addressOf(self_),
    )

  @overload(QSharedMemoryPrivate)
  @overload(NoneType)
  def cleanHandle(self, self_: Optional[QSharedMemoryPrivate]) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::cleanHandle(QSharedMemoryPrivate
    *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryposix.html#cleanHandle

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSharedMemoryPosix::cleanHandle(QSharedMemoryPrivate *self_)
    return self.uglySide.call(
        'ritual_ZN18QSharedMemoryPosix11cleanHandleEP20QSharedMemoryPrivate',
        self._addressOf(self_),
    )

  @overload(QSharedMemoryPrivate, int)
  @overload(NoneType, int)
  def create(self, self_: Optional[QSharedMemoryPrivate], size: int) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::create(QSharedMemoryPrivate *self_,
    qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryposix.html#create

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.
    """
    #  bool QSharedMemoryPosix::create(QSharedMemoryPrivate *self_, qsizetype
    #      size)
    return self.uglySide.call(
        'ritual_ZN18QSharedMemoryPosix6createEP20QSharedMemoryPrivatex',
        self._addressOf(self_), size,
    )

  @overload(QSharedMemoryPrivate, QSharedMemory.AccessMode)
  @overload(NoneType, QSharedMemory.AccessMode)
  def attach(
      self,
      self_: Optional[QSharedMemoryPrivate],
      mode: QSharedMemory.AccessMode,
  ) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::attach(QSharedMemoryPrivate *self_,
    QSharedMemory::AccessMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryposix.html#attach

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QSharedMemory.AccessMode
      Passed on as its number.
    """
    #  bool QSharedMemoryPosix::attach(QSharedMemoryPrivate *self_,
    #      QSharedMemory::AccessMode mode)
    return self.uglySide.call(
        'ritual_ZN18QSharedMemoryPosix6attachEP20QSharedMemoryPrivateN13QSh'
        'aredMemory10AccessModeE',
        self._addressOf(self_), mode.value,
    )

  @overload(QSharedMemoryPrivate)
  @overload(NoneType)
  def detach(self, self_: Optional[QSharedMemoryPrivate]) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPosix::detach(QSharedMemoryPrivate
    *self_)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryposix.html#detach

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSharedMemoryPosix::detach(QSharedMemoryPrivate *self_)
    return self.uglySide.call(
        'ritual_ZN18QSharedMemoryPosix6detachEP20QSharedMemoryPrivate',
        self._addressOf(self_),
    )
