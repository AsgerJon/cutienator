"""
QSharedMemoryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSharedMemoryPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNativeIpcKey, QObjectPrivate, QSharedMemory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLatin1String, QSharedMemoryLocker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']
  QSharedMemoryLocker = WAIT['QSharedMemoryLocker']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSharedMemoryPrivate(QObjectPrivate):
  """
  The cute side of Qt's QSharedMemoryPrivate: a plain Python object standing
  in front of one C++ QSharedMemoryPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QSharedMemoryPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSharedMemoryPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'q_func', 'constructBackend',
  'destructBackend', 'handle', 'cleanHandle', 'attach', 'detach', 'setError',
  'setUnixErrorString', 'tryLocker'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSharedMemory *QSharedMemoryPrivate::q_func() const': takes
    in Python what 'QSharedMemory *QSharedMemoryPrivate::q_func()' takes.
  - Qt's 'QSharedMemoryPrivate::~QSharedMemoryPrivate()': the destructor:
    Python never removes a C++ QSharedMemoryPrivate.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 a template;
  1 leans on 'QSharedMemoryPrivate; 1 leans on 'QSharedMemorySystemV.

  What to expect
  --------------

  - The C++ QSharedMemoryPrivate is created at the first use, not by
    'QSharedMemoryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSharedMemoryPrivate.
  - Each name of Qt's QSharedMemoryPrivate that has no cute function yet,
    'create', 'initKey', 'semaphoreNativeKey', 'setWindowsErrorString',
    'visit', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QSharedMemoryPrivate, each a class in here
  #  as in C++.

  class Backend(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSharedMemoryPrivate::Backend: a plain Python
    object standing in front of one C++ QSharedMemoryPrivate::Backend.

    What exists
    -----------

    No function of Qt's QSharedMemoryPrivate::Backend yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSharedMemoryPrivate::Backend::~Backend()': the destructor:
      Python never removes a C++ QSharedMemoryPrivate::Backend.

    What to expect
    --------------

    - The C++ QSharedMemoryPrivate::Backend is created at the first use, not
      by 'QSharedMemoryPrivate::Backend(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QSharedMemoryPrivate::Backend.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSharedMemoryPrivate::Backend'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSharedMemoryPrivate::Backend::Backend()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsharedmemoryprivate-backend.html#Backend
      """
      #  QSharedMemoryPrivate::Backend::Backend()
      self._noteCreation(QSharedMemoryPrivate.Backend, lambda: Rituals.call(
          'ritual_ZN20QSharedMemoryPrivate7BackendC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSharedMemoryPrivate'

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

  @overload(QSharedMemory.SharedMemoryError, str)
  def setError(
      self,
      e: QSharedMemory.SharedMemoryError,
      message: str,
  ) -> None:
    """
    Calls Qt's 'void
    QSharedMemoryPrivate::setError(QSharedMemory::SharedMemoryError e, const
    QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryprivate.html#setError

    Parameters
    ----------

    e : QSharedMemory.SharedMemoryError
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSharedMemoryPrivate::setError(QSharedMemory::SharedMemoryError
    #      e, const QString &message)
    self.uglySide.call(
        'ritual_ZN20QSharedMemoryPrivate8setErrorEN13QSharedMemory17SharedM'
        'emoryErrorERK7QString',
        e.value, message,
    )

  @overload(QLatin1String)
  def setUnixErrorString(self, function: QLatin1String) -> None:
    """
    Calls Qt's 'void
    QSharedMemoryPrivate::setUnixErrorString(QLatin1StringView function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryprivate.html#setUnixErrorString

    Parameters
    ----------

    function : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QSharedMemoryPrivate::setUnixErrorString(QLatin1StringView
    #      function)
    self.uglySide.call(
        'ritual_ZN20QSharedMemoryPrivate18setUnixErrorStringE13QLatin1Strin'
        'g',
        self._valueOf(function),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNativeIpcKey.Type)
  def __init__(self, type: QNativeIpcKey.Type) -> None:
    """
    Notes what was given, for Qt's
    'QSharedMemoryPrivate::QSharedMemoryPrivate(QNativeIpcKey::Type type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryprivate.html#QSharedMemoryPrivate

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  QSharedMemoryPrivate::QSharedMemoryPrivate(QNativeIpcKey::Type type)
    self._noteCreation(QSharedMemoryPrivate, lambda: Rituals.call(
        'ritual_ZN20QSharedMemoryPrivateC1EN13QNativeIpcKey4TypeE',
        type.value,
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

  def q_func(self) -> Optional[QSharedMemory]:
    """
    Calls Qt's 'QSharedMemory *QSharedMemoryPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryprivate.html#q_func

    Returns
    -------

    Optional[QSharedMemory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSharedMemory *QSharedMemoryPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QSharedMemoryPrivate6q_funcEv')
    return QSharedMemory._cuteAt(address)

  def constructBackend(self) -> None:
    """
    Calls Qt's 'void QSharedMemoryPrivate::constructBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryprivate.html#constructBackend
    """
    #  void QSharedMemoryPrivate::constructBackend()
    self.uglySide.call('ritual_ZN20QSharedMemoryPrivate16constructBackendEv')

  def destructBackend(self) -> None:
    """
    Calls Qt's 'void QSharedMemoryPrivate::destructBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryprivate.html#destructBackend
    """
    #  void QSharedMemoryPrivate::destructBackend()
    self.uglySide.call('ritual_ZN20QSharedMemoryPrivate15destructBackendEv')

  def handle(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPrivate::handle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryprivate.html#handle
    """
    #  bool QSharedMemoryPrivate::handle()
    return self.uglySide.call('ritual_ZN20QSharedMemoryPrivate6handleEv')

  def cleanHandle(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPrivate::cleanHandle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryprivate.html#cleanHandle
    """
    #  bool QSharedMemoryPrivate::cleanHandle()
    return self.uglySide.call(
        'ritual_ZN20QSharedMemoryPrivate11cleanHandleEv',
    )

  @overload(QSharedMemory.AccessMode)
  def attach(self, mode: QSharedMemory.AccessMode) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPrivate::attach(QSharedMemory::AccessMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryprivate.html#attach

    Parameters
    ----------

    mode : QSharedMemory.AccessMode
      Passed on as its number.
    """
    #  bool QSharedMemoryPrivate::attach(QSharedMemory::AccessMode mode)
    return self.uglySide.call(
        'ritual_ZN20QSharedMemoryPrivate6attachEN13QSharedMemory10AccessMod'
        'eE',
        mode.value,
    )

  def detach(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPrivate::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemoryprivate.html#detach
    """
    #  bool QSharedMemoryPrivate::detach()
    return self.uglySide.call('ritual_ZN20QSharedMemoryPrivate6detachEv')

  @overload(QSharedMemoryLocker, str)
  @overload(NoneType, str)
  def tryLocker(
      self,
      locker: Optional[QSharedMemoryLocker],
      function: str,
  ) -> bool:
    """
    Calls Qt's 'bool QSharedMemoryPrivate::tryLocker(QSharedMemoryLocker
    *locker, const QString &function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemoryprivate.html#tryLocker

    Parameters
    ----------

    locker : Optional[QSharedMemoryLocker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSharedMemoryPrivate::tryLocker(QSharedMemoryLocker *locker,
    #      const QString &function)
    return self.uglySide.call(
        'ritual_ZN20QSharedMemoryPrivate9tryLockerEP19QSharedMemoryLockerRK'
        '7QString',
        self._addressOf(locker), function,
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemoryPrivate::create(qsizetype sz)': leans on
    'QSharedMemorySystemV::create(QSharedMemoryPrivate*, long long)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSharedMemoryPrivate.create' has no cute function yet. Qt's 'bool "
        "QSharedMemoryPrivate::create(qsizetype sz)': leans on "
        "'QSharedMemorySystemV::create(QSharedMemoryPrivate*, long long)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def initKey(*__, **_) -> Never:
    """
    Qt's 'bool QSharedMemoryPrivate::initKey(SemaphoreAccessMode mode)':
    leans on 'QSharedMemoryPrivate::semaphoreNativeKey() const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSharedMemoryPrivate.initKey' has no cute function yet. Qt's "
        "'bool QSharedMemoryPrivate::initKey(SemaphoreAccessMode mode)': "
        "leans on 'QSharedMemoryPrivate::semaphoreNativeKey() const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def semaphoreNativeKey(*__, **_) -> Never:
    """
    Qt's 'QNativeIpcKey QSharedMemoryPrivate::semaphoreNativeKey() const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'IpcType'; did
    you mean 'QtIpcCommon::IpcType'?.
    """
    raise NotImplementedError(
        "'QSharedMemoryPrivate.semaphoreNativeKey' has no cute function "
        "yet. Qt's 'QNativeIpcKey "
        "QSharedMemoryPrivate::semaphoreNativeKey() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'IpcType'; did "
        "you mean 'QtIpcCommon::IpcType'?.")

  @staticmethod
  def setWindowsErrorString(*__, **_) -> Never:
    """
    Qt's 'void QSharedMemoryPrivate::setWindowsErrorString(QLatin1StringView
    function)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'DWORD'.
    """
    raise NotImplementedError(
        "'QSharedMemoryPrivate.setWindowsErrorString' has no cute function "
        "yet. Qt's 'void "
        "QSharedMemoryPrivate::setWindowsErrorString(QLatin1StringView "
        "function)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'DWORD'.")

  @staticmethod
  def visit(*__, **_) -> Never:
    """
    Qt's 'QSharedMemoryPrivate::visit': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QSharedMemoryPrivate.visit' has no cute function yet. Qt's "
        "'QSharedMemoryPrivate::visit': a template: a pattern and no single "
        "function.")
