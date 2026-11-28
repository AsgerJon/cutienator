"""
QSharedMemorySystemV binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSharedMemorySystemV to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNativeIpcKey, QSharedMemory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSharedMemoryPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSharedMemoryPrivate = WAIT['QSharedMemoryPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSharedMemorySystemV(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSharedMemorySystemV: a plain Python object standing
  in front of one C++ QSharedMemorySystemV.

  C++ hands a QSharedMemorySystemV around as a copy, so every C++
  QSharedMemorySystemV behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSharedMemorySystemV that has a ritual and that
  Python can call so far, 6 names in all: 'supports', 'runtimeSupportCheck',
  'cleanHandle', 'attach', 'detach', 'updateNativeKeyFile'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'key_t QSharedMemorySystemV::handle(QSharedMemoryPrivate *self_)':
    gives a type Python has no way to take yet.
  - Qt's 'QSharedMemorySystemV::~QSharedMemorySystemV()': the destructor:
    Python removes its C++ QSharedMemorySystemV by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSharedMemorySystemV is created at the first use, not by
    'QSharedMemorySystemV(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSharedMemorySystemV back gives a copy the ritual
    made for Python, in a new cute QSharedMemorySystemV.
  - Each name of Qt's QSharedMemorySystemV that has no cute function yet,
    'create', 'handle', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def supports(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSharedMemorySystemV::supports(QNativeIpcKey::Type
    type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemorysystemv.html#supports

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSharedMemorySystemV::supports(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN20QSharedMemorySystemV8supportsEN13QNativeIpcKey4TypeE',
        type.value,
    )

  @staticmethod
  def runtimeSupportCheck() -> bool:
    """
    Calls Qt's 'bool QSharedMemorySystemV::runtimeSupportCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemorysystemv.html#runtimeSupportCheck
    """
    #  bool QSharedMemorySystemV::runtimeSupportCheck()
    return Rituals.call(
        'ritual_ZN20QSharedMemorySystemV19runtimeSupportCheckEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSharedMemorySystemV'

  #  Qt's '~QSharedMemorySystemV()'. Naming it makes this a value class:
  #  Python owns every C++ QSharedMemorySystemV behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSharedMemorySystemVD1Ev'

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
  def cleanHandle(self, self_: Optional[QSharedMemoryPrivate]) -> bool:
    """
    Calls Qt's 'bool QSharedMemorySystemV::cleanHandle(QSharedMemoryPrivate
    *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemorysystemv.html#cleanHandle

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSharedMemorySystemV::cleanHandle(QSharedMemoryPrivate *self_)
    return self.uglySide.call(
        'ritual_ZN20QSharedMemorySystemV11cleanHandleEP20QSharedMemoryPriva'
        'te',
        self._addressOf(self_),
    )

  @overload(QSharedMemoryPrivate, QSharedMemory.AccessMode)
  @overload(NoneType, QSharedMemory.AccessMode)
  def attach(
      self,
      self_: Optional[QSharedMemoryPrivate],
      mode: QSharedMemory.AccessMode,
  ) -> bool:
    """
    Calls Qt's 'bool QSharedMemorySystemV::attach(QSharedMemoryPrivate
    *self_, QSharedMemory::AccessMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemorysystemv.html#attach

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QSharedMemory.AccessMode
      Passed on as its number.
    """
    #  bool QSharedMemorySystemV::attach(QSharedMemoryPrivate *self_,
    #      QSharedMemory::AccessMode mode)
    return self.uglySide.call(
        'ritual_ZN20QSharedMemorySystemV6attachEP20QSharedMemoryPrivateN13Q'
        'SharedMemory10AccessModeE',
        self._addressOf(self_), mode.value,
    )

  @overload(QSharedMemoryPrivate)
  @overload(NoneType)
  def detach(self, self_: Optional[QSharedMemoryPrivate]) -> bool:
    """
    Calls Qt's 'bool QSharedMemorySystemV::detach(QSharedMemoryPrivate
    *self_)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemorysystemv.html#detach

    Parameters
    ----------

    self_ : Optional[QSharedMemoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSharedMemorySystemV::detach(QSharedMemoryPrivate *self_)
    return self.uglySide.call(
        'ritual_ZN20QSharedMemorySystemV6detachEP20QSharedMemoryPrivate',
        self._addressOf(self_),
    )

  @overload(QNativeIpcKey)
  def updateNativeKeyFile(self, nativeKey: QNativeIpcKey) -> None:
    """
    Calls Qt's 'void QSharedMemorySystemV::updateNativeKeyFile(const
    QNativeIpcKey &nativeKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemorysystemv.html#updateNativeKeyFile

    Parameters
    ----------

    nativeKey : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.
    """
    #  void QSharedMemorySystemV::updateNativeKeyFile(const QNativeIpcKey
    #      &nativeKey)
    self.uglySide.call(
        'ritual_ZN20QSharedMemorySystemV19updateNativeKeyFileERK13QNativeIp'
        'cKey',
        self._valueOf(nativeKey),
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemorySystemV::create(QSharedMemoryPrivate *self_,
    qsizetype size)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'createUnixKeyFile'; did you mean 'QtIpcCommon::createUnixKeyFile'?.
    """
    raise NotImplementedError(
        "'QSharedMemorySystemV.create' has no cute function yet. Qt's 'bool "
        "QSharedMemorySystemV::create(QSharedMemoryPrivate *self_, "
        "qsizetype size)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'createUnixKeyFile'; did you mean "
        "'QtIpcCommon::createUnixKeyFile'?.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'key_t QSharedMemorySystemV::handle(QSharedMemoryPrivate *self_)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSharedMemorySystemV.handle' has no cute function yet. Qt's "
        "'key_t QSharedMemorySystemV::handle(QSharedMemoryPrivate *self_)': "
        "gives a type Python has no way to take yet.")
