"""
QNetworkAddressEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDeadlineTimer
  from . import QHostAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QHostAddress = WAIT['QHostAddress']


class QNetworkAddressEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkAddressEntry: a plain Python object standing
  in front of one C++ QNetworkAddressEntry.

  C++ hands a QNetworkAddressEntry around as a copy, so every C++
  QNetworkAddressEntry behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkAddressEntry that has a ritual and that
  Python can call so far, 19 names in all: '__eq__', '__ne__',
  'dnsEligibility', 'setDnsEligibility', 'ip', 'setIp', 'netmask',
  'setNetmask', 'prefixLength', 'setPrefixLength', 'broadcast',
  'setBroadcast', 'isLifetimeKnown', 'preferredLifetime', 'validityLifetime',
  'setAddressLifetime', 'clearAddressLifetime', 'isPermanent', 'isTemporary'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkAddressEntry
    &QNetworkAddressEntry::operator=(QNetworkAddressEntry &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkAddressEntry &QNetworkAddressEntry::operator=(const
    QNetworkAddressEntry &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QNetworkAddressEntry::~QNetworkAddressEntry()': the destructor:
    Python removes its C++ QNetworkAddressEntry by it, and has no other use
    for it.
  - Qt's 'void QNetworkAddressEntry::swap(QNetworkAddressEntry &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QNetworkAddressEntry is created at the first use, not by
    'QNetworkAddressEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkAddressEntry back gives a copy the ritual
    made for Python, in a new cute QNetworkAddressEntry.
  - Each name of Qt's QNetworkAddressEntry that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QNetworkAddressEntry, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DnsEligibilityStatus(CuteNum):
    """
    The enum 'QNetworkAddressEntry::DnsEligibilityStatus' of Qt, with the 3
    names Qt gives in it.
    """

    DnsEligibilityUnknown = Kee[int](-1)
    DnsIneligible = Kee[int](0)
    DnsEligible = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAddressEntry'

  #  Qt's '~QNetworkAddressEntry()'. Naming it makes this a value class:
  #  Python owns every C++ QNetworkAddressEntry behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QNetworkAddressEntryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dnsEligibility(self) -> DnsEligibilityStatus:
    """
    Calls Qt's 'DnsEligibilityStatus QNetworkAddressEntry::dnsEligibility()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#dnsEligibility

    Returns
    -------

    DnsEligibilityStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'DnsEligibilityStatus(number)' gives.
    """
    #  DnsEligibilityStatus QNetworkAddressEntry::dnsEligibility() const
    return QNetworkAddressEntry.DnsEligibilityStatus(self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry14dnsEligibilityEv',
    ))

  def ip(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QNetworkAddressEntry::ip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaddressentry.html#ip

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNetworkAddressEntry::ip() const
    address = self.uglySide.call('ritual_ZNK20QNetworkAddressEntry2ipEv')
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def netmask(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QNetworkAddressEntry::netmask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaddressentry.html#netmask

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNetworkAddressEntry::netmask() const
    address = self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry7netmaskEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def prefixLength(self) -> int:
    """
    Calls Qt's 'int QNetworkAddressEntry::prefixLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#prefixLength
    """
    #  int QNetworkAddressEntry::prefixLength() const
    return self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry12prefixLengthEv',
    )

  def broadcast(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QNetworkAddressEntry::broadcast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#broadcast

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNetworkAddressEntry::broadcast() const
    address = self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry9broadcastEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def isLifetimeKnown(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAddressEntry::isLifetimeKnown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#isLifetimeKnown
    """
    #  bool QNetworkAddressEntry::isLifetimeKnown() const
    return self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry15isLifetimeKnownEv',
    )

  def preferredLifetime(self) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer QNetworkAddressEntry::preferredLifetime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#preferredLifetime

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer QNetworkAddressEntry::preferredLifetime() const
    address = self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry17preferredLifetimeEv',
    )
    from ..QtCore import QDeadlineTimer
    return QDeadlineTimer._cuteOwning(address)

  def validityLifetime(self) -> QDeadlineTimer:
    """
    Calls Qt's 'QDeadlineTimer QNetworkAddressEntry::validityLifetime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#validityLifetime

    Returns
    -------

    QDeadlineTimer
      A new cute QDeadlineTimer around the copy Qt gave back. Python owns it.
    """
    #  QDeadlineTimer QNetworkAddressEntry::validityLifetime() const
    address = self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry16validityLifetimeEv',
    )
    from ..QtCore import QDeadlineTimer
    return QDeadlineTimer._cuteOwning(address)

  def isPermanent(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAddressEntry::isPermanent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#isPermanent
    """
    #  bool QNetworkAddressEntry::isPermanent() const
    return self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry11isPermanentEv',
    )

  def isTemporary(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAddressEntry::isTemporary() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#isTemporary
    """
    #  bool QNetworkAddressEntry::isTemporary() const
    return self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntry11isTemporaryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DnsEligibilityStatus)
  def setDnsEligibility(self, status: DnsEligibilityStatus) -> None:
    """
    Calls Qt's 'void
    QNetworkAddressEntry::setDnsEligibility(DnsEligibilityStatus status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#setDnsEligibility

    Parameters
    ----------

    status : DnsEligibilityStatus
      Passed on as its number.
    """
    #  void QNetworkAddressEntry::setDnsEligibility(DnsEligibilityStatus
    #      status)
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry17setDnsEligibilityENS_20DnsEligibi'
        'lityStatusE',
        status.value,
    )

  @overload(QHostAddress)
  def setIp(self, newIp: QHostAddress) -> None:
    """
    Calls Qt's 'void QNetworkAddressEntry::setIp(const QHostAddress &newIp)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaddressentry.html#setIp

    Parameters
    ----------

    newIp : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QNetworkAddressEntry::setIp(const QHostAddress &newIp)
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry5setIpERK12QHostAddress',
        self._valueOf(newIp),
    )

  @overload(QHostAddress)
  def setNetmask(self, newNetmask: QHostAddress) -> None:
    """
    Calls Qt's 'void QNetworkAddressEntry::setNetmask(const QHostAddress
    &newNetmask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#setNetmask

    Parameters
    ----------

    newNetmask : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QNetworkAddressEntry::setNetmask(const QHostAddress &newNetmask)
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry10setNetmaskERK12QHostAddress',
        self._valueOf(newNetmask),
    )

  @overload(int)
  def setPrefixLength(self, length: int) -> None:
    """
    Calls Qt's 'void QNetworkAddressEntry::setPrefixLength(int length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#setPrefixLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QNetworkAddressEntry::setPrefixLength(int length)
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry15setPrefixLengthEi', length,
    )

  @overload(QHostAddress)
  def setBroadcast(self, newBroadcast: QHostAddress) -> None:
    """
    Calls Qt's 'void QNetworkAddressEntry::setBroadcast(const QHostAddress
    &newBroadcast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#setBroadcast

    Parameters
    ----------

    newBroadcast : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QNetworkAddressEntry::setBroadcast(const QHostAddress
    #      &newBroadcast)
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry12setBroadcastERK12QHostAddress',
        self._valueOf(newBroadcast),
    )

  @overload(QDeadlineTimer, QDeadlineTimer)
  def setAddressLifetime(
      self,
      preferred: QDeadlineTimer,
      validity: QDeadlineTimer,
  ) -> None:
    """
    Calls Qt's 'void QNetworkAddressEntry::setAddressLifetime(QDeadlineTimer
    preferred, QDeadlineTimer validity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#setAddressLifetime

    Parameters
    ----------

    preferred : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.

    validity : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  void QNetworkAddressEntry::setAddressLifetime(QDeadlineTimer
    #      preferred, QDeadlineTimer validity)
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry18setAddressLifetimeE14QDeadlineTim'
        'erS0_',
        self._valueOf(preferred), self._valueOf(validity),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNetworkAddressEntry) -> bool:
    """
    Calls Qt's 'bool QNetworkAddressEntry::operator==(const
    QNetworkAddressEntry &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#operator==

    Parameters
    ----------

    other : QNetworkAddressEntry
      Passed on as a value: Qt reads the C++ QNetworkAddressEntry, which
      stays Python's own.
    """
    #  bool QNetworkAddressEntry::operator==(const QNetworkAddressEntry
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntryeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QNetworkAddressEntry) -> bool:
    """
    Calls Qt's 'bool QNetworkAddressEntry::operator!=(const
    QNetworkAddressEntry &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#operator!=

    Parameters
    ----------

    other : QNetworkAddressEntry
      Passed on as a value: Qt reads the C++ QNetworkAddressEntry, which
      stays Python's own.
    """
    #  bool QNetworkAddressEntry::operator!=(const QNetworkAddressEntry
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK20QNetworkAddressEntryneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAddressEntry::QNetworkAddressEntry()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#QNetworkAddressEntry
    """
    #  QNetworkAddressEntry::QNetworkAddressEntry()
    self._noteCreation(QNetworkAddressEntry, lambda: Rituals.call(
        'ritual_ZN20QNetworkAddressEntryC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkAddressEntry) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAddressEntry::QNetworkAddressEntry(const QNetworkAddressEntry
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#QNetworkAddressEntry

    Parameters
    ----------

    other : QNetworkAddressEntry
      Passed on as a value: Qt reads the C++ QNetworkAddressEntry, which
      stays Python's own.
    """
    #  QNetworkAddressEntry::QNetworkAddressEntry(const QNetworkAddressEntry
    #      &other)
    self._noteCreation(QNetworkAddressEntry, lambda: Rituals.call(
        'ritual_ZN20QNetworkAddressEntryC1ERKS_', self._valueOf(other),
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

  def clearAddressLifetime(self) -> None:
    """
    Calls Qt's 'void QNetworkAddressEntry::clearAddressLifetime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaddressentry.html#clearAddressLifetime
    """
    #  void QNetworkAddressEntry::clearAddressLifetime()
    self.uglySide.call(
        'ritual_ZN20QNetworkAddressEntry20clearAddressLifetimeEv',
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAddressEntry::swap(QNetworkAddressEntry &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkAddressEntry.swap' has no cute function yet. Qt's 'void "
        "QNetworkAddressEntry::swap(QNetworkAddressEntry &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QNetworkAddressEntry>': the list of QNetworkAddressEntry,
#  which 'QList[QNetworkAddressEntry]' gives. It is made here, so that there
#  is one as soon as there can be a QNetworkAddressEntry.
QList.createKind(
    QNetworkAddressEntry, 'value',
    make='ritual_list_make_QNetworkAddressEntry',
    add='ritual_list_add_QNetworkAddressEntry',
    size='ritual_list_size_QNetworkAddressEntry',
    at='ritual_list_at_QNetworkAddressEntry',
    drop='ritual_list_drop_QNetworkAddressEntry',
)
