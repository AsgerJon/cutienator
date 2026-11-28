"""
QHostInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhostinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QHostAddress, QHostInfoPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHostInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHostInfo: a plain Python object standing in front of
  one C++ QHostInfo.

  C++ hands a QHostInfo around as a copy, so every C++ QHostInfo behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHostInfo that has a ritual and that Python can call
  so far, 17 names in all: 'hostName', 'setHostName', 'addresses',
  'setAddresses', 'error', 'setError', 'errorString', 'setErrorString',
  'setLookupId', 'lookupId', 'lookupHost', 'abortHostLookup', 'fromName',
  'localHostName', 'localDomainName', 'clearCache', 'd_func'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHostInfo::QHostInfo(QHostInfo &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QHostInfo &QHostInfo::operator=(const QHostInfo &d)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QHostInfo &QHostInfo::operator=(QHostInfo &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QHostInfo::~QHostInfo()': the destructor: Python removes its C++
    QHostInfo by it, and has no other use for it.
  - Qt's 'void QHostInfo::swap(QHostInfo &other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QHostInfoPrivate *QHostInfo::d_func() const': takes in Python
    what 'QHostInfoPrivate *QHostInfo::d_func()' takes.
  - Qt's 'int QHostInfo::lookupHostImpl(const QString &name, const QObject
    *receiver, QtPrivate::QSlotObjectBase *slotObj, const char *member)':
    names 'QtPrivate::QSlotObjectBase', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 31 functions Qt declares: 3 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ QHostInfo is created at the first use, not by 'QHostInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHostInfo back gives a copy the ritual made for
    Python, in a new cute QHostInfo.
  - Each name of Qt's QHostInfo that has no cute function yet,
    'lookupHostImpl', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHostInfo, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class HostInfoError(CuteNum):
    """
    The enum 'QHostInfo::HostInfoError' of Qt, with the 3 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    HostNotFound = Kee[int](1)
    UnknownError = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, QObject, str)
  @overload(str, QObject, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  def lookupHost(
      name: str,
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> int:
    """
    Calls Qt's 'int QHostInfo::lookupHost(const QString &name, const QObject
    *receiver, const char *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#lookupHost

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QHostInfo::lookupHost(const QString &name, const QObject
    #      *receiver, const char *member)
    return Rituals.call(
        'ritual_ZN9QHostInfo10lookupHostERK7QStringPK7QObjectPKc',
        name, CuteMixin._addressOf(receiver, 'QObject'),
        CuteMixin._bytesOf(member),
    )

  @staticmethod
  @overload(int)
  def abortHostLookup(lookupId: int) -> None:
    """
    Calls Qt's 'void QHostInfo::abortHostLookup(int lookupId)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#abortHostLookup

    Parameters
    ----------

    lookupId : int
      Passed on as it is.
    """
    #  void QHostInfo::abortHostLookup(int lookupId)
    Rituals.call('ritual_ZN9QHostInfo15abortHostLookupEi', lookupId)

  @staticmethod
  @overload(str)
  def fromName(name: str) -> QHostInfo:
    """
    Calls Qt's 'QHostInfo QHostInfo::fromName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#fromName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QHostInfo
      A new cute QHostInfo around the copy Qt gave back. Python owns it.
    """
    #  QHostInfo QHostInfo::fromName(const QString &name)
    address = Rituals.call('ritual_ZN9QHostInfo8fromNameERK7QString', name)
    return QHostInfo._cuteOwning(address)

  @staticmethod
  def localHostName() -> str:
    """
    Calls Qt's 'QString QHostInfo::localHostName()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#localHostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHostInfo::localHostName()
    return Rituals.call('ritual_ZN9QHostInfo13localHostNameEv')

  @staticmethod
  def localDomainName() -> str:
    """
    Calls Qt's 'QString QHostInfo::localDomainName()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#localDomainName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHostInfo::localDomainName()
    return Rituals.call('ritual_ZN9QHostInfo15localDomainNameEv')

  @staticmethod
  def clearCache() -> None:
    """
    Calls Qt's 'void QHostInfo::clearCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#clearCache
    """
    #  void QHostInfo::clearCache()
    Rituals.call('ritual_ZN9QHostInfo10clearCacheEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHostInfo'

  #  Qt's '~QHostInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QHostInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QHostInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hostName(self) -> str:
    """
    Calls Qt's 'QString QHostInfo::hostName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#hostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHostInfo::hostName() const
    return self.uglySide.call('ritual_ZNK9QHostInfo8hostNameEv')

  def addresses(self) -> QList[QHostAddress]:
    """
    Calls Qt's 'QList<QHostAddress> QHostInfo::addresses() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#addresses

    Returns
    -------

    QList[QHostAddress]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHostAddress> QHostInfo::addresses() const
    address = self.uglySide.call('ritual_ZNK9QHostInfo9addressesEv')
    from . import QHostAddress
    return QList[QHostAddress]._cuteOwning(address)

  def error(self) -> HostInfoError:
    """
    Calls Qt's 'HostInfoError QHostInfo::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#error

    Returns
    -------

    HostInfoError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HostInfoError(number)'
      gives.
    """
    #  HostInfoError QHostInfo::error() const
    return QHostInfo.HostInfoError(self.uglySide.call(
        'ritual_ZNK9QHostInfo5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QHostInfo::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHostInfo::errorString() const
    return self.uglySide.call('ritual_ZNK9QHostInfo11errorStringEv')

  def lookupId(self) -> int:
    """
    Calls Qt's 'int QHostInfo::lookupId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#lookupId
    """
    #  int QHostInfo::lookupId() const
    return self.uglySide.call('ritual_ZNK9QHostInfo8lookupIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHostName(self, name: str) -> None:
    """
    Calls Qt's 'void QHostInfo::setHostName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#setHostName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHostInfo::setHostName(const QString &name)
    self.uglySide.call('ritual_ZN9QHostInfo11setHostNameERK7QString', name)

  @overload(QList[QHostAddress])
  def setAddresses(self, addresses: QList[QHostAddress]) -> None:
    """
    Calls Qt's 'void QHostInfo::setAddresses(const QList<QHostAddress>
    &addresses)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#setAddresses

    Parameters
    ----------

    addresses : QList[QHostAddress]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHostInfo::setAddresses(const QList<QHostAddress> &addresses)
    self.uglySide.call(
        'ritual_ZN9QHostInfo12setAddressesERK5QListI12QHostAddressE',
        self._valueOf(addresses),
    )

  @overload(HostInfoError)
  def setError(self, error: HostInfoError) -> None:
    """
    Calls Qt's 'void QHostInfo::setError(HostInfoError error)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#setError

    Parameters
    ----------

    error : HostInfoError
      Passed on as its number.
    """
    #  void QHostInfo::setError(HostInfoError error)
    self.uglySide.call(
        'ritual_ZN9QHostInfo8setErrorENS_13HostInfoErrorE', error.value,
    )

  @overload(str)
  def setErrorString(self, errorString: str) -> None:
    """
    Calls Qt's 'void QHostInfo::setErrorString(const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#setErrorString

    Parameters
    ----------

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHostInfo::setErrorString(const QString &errorString)
    self.uglySide.call(
        'ritual_ZN9QHostInfo14setErrorStringERK7QString', errorString,
    )

  @overload(int)
  def setLookupId(self, id: int) -> None:
    """
    Calls Qt's 'void QHostInfo::setLookupId(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#setLookupId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QHostInfo::setLookupId(int id)
    self.uglySide.call('ritual_ZN9QHostInfo11setLookupIdEi', id)

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
  @overload(int)
  def __init__(self, lookupId: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QHostInfo::QHostInfo(int lookupId)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#QHostInfo

    Parameters
    ----------

    lookupId : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QHostInfo::QHostInfo(int lookupId)
    self._noteCreation(QHostInfo, lambda: Rituals.call(
        'ritual_ZN9QHostInfoC1Ei', lookupId,
    ))

  @overload(THIS)
  def __init__(self, d: QHostInfo) -> None:
    """
    Notes what was given, for Qt's 'QHostInfo::QHostInfo(const QHostInfo
    &d)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#QHostInfo

    Parameters
    ----------

    d : QHostInfo
      Passed on as a value: Qt reads the C++ QHostInfo, which stays Python's
      own.
    """
    #  QHostInfo::QHostInfo(const QHostInfo &d)
    self._noteCreation(QHostInfo, lambda: Rituals.call(
        'ritual_ZN9QHostInfoC1ERKS_', self._valueOf(d),
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

  def d_func(self) -> Optional[QHostInfoPrivate]:
    """
    Calls Qt's 'QHostInfoPrivate *QHostInfo::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfo.html#d_func

    Returns
    -------

    Optional[QHostInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHostInfoPrivate *QHostInfo::d_func()
    address = self.uglySide.call('ritual_ZN9QHostInfo6d_funcEv')
    from . import QHostInfoPrivate
    return QHostInfoPrivate._cuteAt(address)

  @staticmethod
  def lookupHostImpl(*__, **_) -> Never:
    """
    Qt's 'int QHostInfo::lookupHostImpl(const QString &name, const QObject
    *receiver, QtPrivate::QSlotObjectBase *slotObj, const char *member)':
    names 'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHostInfo.lookupHostImpl' has no cute function yet. Qt's 'int "
        "QHostInfo::lookupHostImpl(const QString &name, const QObject "
        "*receiver, QtPrivate::QSlotObjectBase *slotObj, const char "
        "*member)': names 'QtPrivate::QSlotObjectBase', which has no cute "
        "class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHostInfo::swap(QHostInfo &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QHostInfo.swap' has no cute function yet. Qt's 'void "
        "QHostInfo::swap(QHostInfo &other)': takes a type Python has no way "
        "to hand over yet.")
