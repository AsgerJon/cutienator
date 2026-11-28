"""
QSharedMemory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsharedmemory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from . import QNativeIpcKey, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject, QSharedMemoryPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSharedMemory(QObject):
  """
  The cute side of Qt's QSharedMemory: a plain Python object standing in
  front of one C++ QSharedMemory.

  It is built on the cute 'QObject', as Qt's QSharedMemory is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSharedMemory that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'd_func', 'setKey',
  'key', 'setNativeKey', 'nativeKey', 'nativeIpcKey', 'create', 'size',
  'attach', 'isAttached', 'detach', 'lock', 'unlock', 'error', 'errorString',
  'isKeyTypeSupported', 'platformSafeKey', 'legacyNativeKey'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSharedMemory::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSharedMemory::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSharedMemoryPrivate *QSharedMemory::d_func() const': takes
    in Python what 'QSharedMemoryPrivate *QSharedMemory::d_func()' takes.
  - Qt's 'QSharedMemory::~QSharedMemory()': the destructor: Python never
    removes a C++ QSharedMemory.
  - Qt's 'void *QSharedMemory::data()': gives 'void', which has no cute class
    yet.
  - Qt's 'const void *QSharedMemory::constData() const': gives 'void', which
    has no cute class yet.
  - Qt's 'const void *QSharedMemory::data() const': gives 'void', which has
    no cute class yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSharedMemory is created at the first use, not by
    'QSharedMemory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSharedMemory.
  - Qt tells when it has removed the C++ QSharedMemory. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSharedMemory that has no cute function yet,
    'constData', 'data', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSharedMemory, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AccessMode(CuteNum):
    """
    The enum 'QSharedMemory::AccessMode' of Qt, with the 2 names Qt gives in
    it.
    """

    ReadOnly = Kee[int](0)
    ReadWrite = Kee[int](1)

  class SharedMemoryError(CuteNum):
    """
    The enum 'QSharedMemory::SharedMemoryError' of Qt, with the 9 names Qt
    gives in it.
    """

    NoError = Kee[int](0)
    PermissionDenied = Kee[int](1)
    InvalidSize = Kee[int](2)
    KeyError = Kee[int](3)
    AlreadyExists = Kee[int](4)
    NotFound = Kee[int](5)
    LockError = Kee[int](6)
    OutOfResources = Kee[int](7)
    UnknownError = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QSharedMemory::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSharedMemory::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSharedMemory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def isKeyTypeSupported(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::isKeyTypeSupported(QNativeIpcKey::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsharedmemory.html#isKeyTypeSupported

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSharedMemory::isKeyTypeSupported(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN13QSharedMemory18isKeyTypeSupportedEN13QNativeIpcKey4Type'
        'E',
        type.value,
    )

  @staticmethod
  @overload(str, QNativeIpcKey.Type)
  def platformSafeKey(key: str, type: QNativeIpcKey.Type) -> QNativeIpcKey:
    """
    Calls Qt's 'QNativeIpcKey QSharedMemory::platformSafeKey(const QString
    &key, QNativeIpcKey::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#platformSafeKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    type : QNativeIpcKey.Type
      Passed on as its number.

    Returns
    -------

    QNativeIpcKey
      A new cute QNativeIpcKey around the copy Qt gave back. Python owns it.
    """
    #  QNativeIpcKey QSharedMemory::platformSafeKey(const QString &key,
    #      QNativeIpcKey::Type type)
    address = Rituals.call(
        'ritual_ZN13QSharedMemory15platformSafeKeyERK7QStringN13QNativeIpcK'
        'ey4TypeE',
        key, type.value,
    )
    return QNativeIpcKey._cuteOwning(address)

  @staticmethod
  @overload(str, QNativeIpcKey.Type)
  def legacyNativeKey(key: str, type: QNativeIpcKey.Type) -> QNativeIpcKey:
    """
    Calls Qt's 'QNativeIpcKey QSharedMemory::legacyNativeKey(const QString
    &key, QNativeIpcKey::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#legacyNativeKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    type : QNativeIpcKey.Type
      Passed on as its number.

    Returns
    -------

    QNativeIpcKey
      A new cute QNativeIpcKey around the copy Qt gave back. Python owns it.
    """
    #  QNativeIpcKey QSharedMemory::legacyNativeKey(const QString &key,
    #      QNativeIpcKey::Type type)
    address = Rituals.call(
        'ritual_ZN13QSharedMemory15legacyNativeKeyERK7QStringN13QNativeIpcK'
        'ey4TypeE',
        key, type.value,
    )
    return QNativeIpcKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSharedMemory'

  #  A C++ QSharedMemory Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSharedMemory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSharedMemory::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSharedMemory::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSharedMemory10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def key(self) -> str:
    """
    Calls Qt's 'QString QSharedMemory::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSharedMemory::key() const
    return self.uglySide.call('ritual_ZNK13QSharedMemory3keyEv')

  def nativeKey(self) -> str:
    """
    Calls Qt's 'QString QSharedMemory::nativeKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#nativeKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSharedMemory::nativeKey() const
    return self.uglySide.call('ritual_ZNK13QSharedMemory9nativeKeyEv')

  def nativeIpcKey(self) -> QNativeIpcKey:
    """
    Calls Qt's 'QNativeIpcKey QSharedMemory::nativeIpcKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#nativeIpcKey

    Returns
    -------

    QNativeIpcKey
      A new cute QNativeIpcKey around the copy Qt gave back. Python owns it.
    """
    #  QNativeIpcKey QSharedMemory::nativeIpcKey() const
    address = self.uglySide.call('ritual_ZNK13QSharedMemory12nativeIpcKeyEv')
    return QNativeIpcKey._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QSharedMemory::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#size
    """
    #  qsizetype QSharedMemory::size() const
    return self.uglySide.call('ritual_ZNK13QSharedMemory4sizeEv')

  def isAttached(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::isAttached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#isAttached
    """
    #  bool QSharedMemory::isAttached() const
    return self.uglySide.call('ritual_ZNK13QSharedMemory10isAttachedEv')

  def error(self) -> SharedMemoryError:
    """
    Calls Qt's 'SharedMemoryError QSharedMemory::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#error

    Returns
    -------

    SharedMemoryError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SharedMemoryError(number)' gives.
    """
    #  SharedMemoryError QSharedMemory::error() const
    return QSharedMemory.SharedMemoryError(self.uglySide.call(
        'ritual_ZNK13QSharedMemory5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSharedMemory::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSharedMemory::errorString() const
    return self.uglySide.call('ritual_ZNK13QSharedMemory11errorStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setKey(self, key: str) -> None:
    """
    Calls Qt's 'void QSharedMemory::setKey(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#setKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSharedMemory::setKey(const QString &key)
    self.uglySide.call('ritual_ZN13QSharedMemory6setKeyERK7QString', key)

  @overload(QNativeIpcKey)
  def setNativeKey(self, key: QNativeIpcKey) -> None:
    """
    Calls Qt's 'void QSharedMemory::setNativeKey(const QNativeIpcKey &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#setNativeKey

    Parameters
    ----------

    key : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.
    """
    #  void QSharedMemory::setNativeKey(const QNativeIpcKey &key)
    self.uglySide.call(
        'ritual_ZN13QSharedMemory12setNativeKeyERK13QNativeIpcKey',
        self._valueOf(key),
    )

  @overload(str, QNativeIpcKey.Type)
  def setNativeKey(self, key: str, type: QNativeIpcKey.Type) -> None:
    """
    Calls Qt's 'void QSharedMemory::setNativeKey(const QString &key,
    QNativeIpcKey::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#setNativeKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  void QSharedMemory::setNativeKey(const QString &key,
    #      QNativeIpcKey::Type type)
    self.uglySide.call(
        'ritual_ZN13QSharedMemory12setNativeKeyERK7QStringN13QNativeIpcKey4'
        'TypeE',
        key, type.value,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSharedMemory::QSharedMemory(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#QSharedMemory

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSharedMemory::QSharedMemory(QObject *parent)
    self._noteCreation(QSharedMemory, lambda: Rituals.call(
        'ritual_ZN13QSharedMemoryC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QNativeIpcKey)
  @overload(QNativeIpcKey, QObject)
  @overload(QNativeIpcKey, NoneType)
  def __init__(
      self,
      key: QNativeIpcKey,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSharedMemory::QSharedMemory(const
    QNativeIpcKey &key, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#QSharedMemory

    Parameters
    ----------

    key : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSharedMemory::QSharedMemory(const QNativeIpcKey &key, QObject
    #      *parent)
    self._noteCreation(QSharedMemory, lambda: Rituals.call(
        'ritual_ZN13QSharedMemoryC1ERK13QNativeIpcKeyP7QObject',
        self._valueOf(key), self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, key: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSharedMemory::QSharedMemory(const
    QString &key, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#QSharedMemory

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSharedMemory::QSharedMemory(const QString &key, QObject *parent)
    self._noteCreation(QSharedMemory, lambda: Rituals.call(
        'ritual_ZN13QSharedMemoryC1ERK7QStringP7QObject',
        key, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QSharedMemoryPrivate]:
    """
    Calls Qt's 'QSharedMemoryPrivate *QSharedMemory::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#d_func

    Returns
    -------

    Optional[QSharedMemoryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSharedMemoryPrivate *QSharedMemory::d_func()
    address = self.uglySide.call('ritual_ZN13QSharedMemory6d_funcEv')
    from . import QSharedMemoryPrivate
    return QSharedMemoryPrivate._cuteAt(address)

  @overload(int)
  @overload(int, AccessMode)
  def create(
      self,
      size: int,
      mode: AccessMode = AccessMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::create(qsizetype size, AccessMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#create

    Parameters
    ----------

    size : int
      Passed on as it is.

    mode : AccessMode
      Passed on as its number. May be left out, as in Qt: it is then
      AccessMode.ReadWrite.
    """
    #  bool QSharedMemory::create(qsizetype size, AccessMode mode)
    return self.uglySide.call(
        'ritual_ZN13QSharedMemory6createExNS_10AccessModeE',
        size, mode.value,
    )

  @overload()
  @overload(AccessMode)
  def attach(self, mode: AccessMode = AccessMode.ReadWrite) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::attach(AccessMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#attach

    Parameters
    ----------

    mode : AccessMode
      Passed on as its number. May be left out, as in Qt: it is then
      AccessMode.ReadWrite.
    """
    #  bool QSharedMemory::attach(AccessMode mode)
    return self.uglySide.call(
        'ritual_ZN13QSharedMemory6attachENS_10AccessModeE', mode.value,
    )

  def detach(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#detach
    """
    #  bool QSharedMemory::detach()
    return self.uglySide.call('ritual_ZN13QSharedMemory6detachEv')

  def lock(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#lock
    """
    #  bool QSharedMemory::lock()
    return self.uglySide.call('ritual_ZN13QSharedMemory4lockEv')

  def unlock(self) -> bool:
    """
    Calls Qt's 'bool QSharedMemory::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qsharedmemory.html#unlock
    """
    #  bool QSharedMemory::unlock()
    return self.uglySide.call('ritual_ZN13QSharedMemory6unlockEv')

  @staticmethod
  def constData(*__, **_) -> Never:
    """
    Qt's 'const void *QSharedMemory::constData() const': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSharedMemory.constData' has no cute function yet. Qt's 'const "
        "void *QSharedMemory::constData() const': gives 'void', which has "
        "no cute class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    - Qt's 'void *QSharedMemory::data()': gives 'void', which has no cute
      class yet.
    - Qt's 'const void *QSharedMemory::data() const': gives 'void', which has
      no cute class yet.
    """
    raise NotImplementedError(
        "'QSharedMemory.data' has no cute function yet. Qt's 'void "
        "*QSharedMemory::data()': gives 'void', which has no cute class "
        "yet. Qt's 'const void *QSharedMemory::data() const': gives 'void', "
        "which has no cute class yet.")
