"""
QHttpServerConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverconfiguration.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QHttpServerConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerConfiguration: a plain Python object
  standing in front of one C++ QHttpServerConfiguration.

  C++ hands a QHttpServerConfiguration around as a copy, so every C++
  QHttpServerConfiguration behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpServerConfiguration that has a ritual and that
  Python can call so far, 18 names in all: 'setRateLimitPerSecond',
  'rateLimitPerSecond', 'setMaximumConnectionsPerHost',
  'maximumConnectionsPerHost', 'setMaximumConnections', 'maximumConnections',
  'setMaximumUrlSize', 'maximumUrlSize', 'setMaximumTotalHeaderSize',
  'maximumTotalHeaderSize', 'setMaximumHeaderFieldSize',
  'maximumHeaderFieldSize', 'setMaximumHeaderFieldCount',
  'maximumHeaderFieldCount', 'setMaximumBodySize', 'maximumBodySize',
  '__eq__', '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpServerConfiguration::QHttpServerConfiguration(
    QHttpServerConfiguration &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QHttpServerConfiguration &QHttpServerConfiguration::operator=(const
    QHttpServerConfiguration &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QHttpServerConfiguration
    &QHttpServerConfiguration::operator=(QHttpServerConfiguration &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QHttpServerConfiguration::swap(QHttpServerConfiguration
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpServerConfiguration::~QHttpServerConfiguration()': the
    destructor: Python removes its C++ QHttpServerConfiguration by it, and
    has no other use for it.
  - Qt's 'void
    QHttpServerConfiguration::setKeepAliveTimeout(std::chrono::seconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::seconds QHttpServerConfiguration::keepAliveTimeout()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QHttpServerConfiguration::setWhitelist(QSpan<const
    std::pair<QHostAddress, int>> subnetList)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSpan<const std::pair<QHostAddress, int>>
    QHttpServerConfiguration::whitelist() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QHttpServerConfiguration::setBlacklist(QSpan<const
    std::pair<QHostAddress, int>> subnetList)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSpan<const std::pair<QHostAddress, int>>
    QHttpServerConfiguration::blacklist() const': gives a type Python has no
    way to take yet.

  What to expect
  --------------

  - The C++ QHttpServerConfiguration is created at the first use, not by
    'QHttpServerConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerConfiguration back gives a copy the ritual
    made for Python, in a new cute QHttpServerConfiguration.
  - Each name of Qt's QHttpServerConfiguration that has no cute function yet,
    'blacklist', 'keepAliveTimeout', 'setBlacklist', 'setKeepAliveTimeout',
    'setWhitelist', 'swap', 'whitelist', holds a function that raises
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
  __qt_class__ = 'QHttpServerConfiguration'

  #  Qt's '~QHttpServerConfiguration()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpServerConfiguration behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QHttpServerConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rateLimitPerSecond(self) -> int:
    """
    Calls Qt's 'quint32 QHttpServerConfiguration::rateLimitPerSecond()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#rateLimitPerSecond
    """
    #  quint32 QHttpServerConfiguration::rateLimitPerSecond() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration18rateLimitPerSecondEv',
    )

  def maximumConnectionsPerHost(self) -> int:
    """
    Calls Qt's 'quint32 QHttpServerConfiguration::maximumConnectionsPerHost()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html
    """
    #  quint32 QHttpServerConfiguration::maximumConnectionsPerHost() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration25maximumConnectionsPerHostEv',
    )

  def maximumConnections(self) -> int:
    """
    Calls Qt's 'quint32 QHttpServerConfiguration::maximumConnections()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#maximumConnections
    """
    #  quint32 QHttpServerConfiguration::maximumConnections() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration18maximumConnectionsEv',
    )

  def maximumUrlSize(self) -> int:
    """
    Calls Qt's 'qint64 QHttpServerConfiguration::maximumUrlSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#maximumUrlSize
    """
    #  qint64 QHttpServerConfiguration::maximumUrlSize() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration14maximumUrlSizeEv',
    )

  def maximumTotalHeaderSize(self) -> int:
    """
    Calls Qt's 'qint64 QHttpServerConfiguration::maximumTotalHeaderSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html
    """
    #  qint64 QHttpServerConfiguration::maximumTotalHeaderSize() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration22maximumTotalHeaderSizeEv',
    )

  def maximumHeaderFieldSize(self) -> int:
    """
    Calls Qt's 'qint64 QHttpServerConfiguration::maximumHeaderFieldSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html
    """
    #  qint64 QHttpServerConfiguration::maximumHeaderFieldSize() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration22maximumHeaderFieldSizeEv',
    )

  def maximumHeaderFieldCount(self) -> int:
    """
    Calls Qt's 'qint64 QHttpServerConfiguration::maximumHeaderFieldCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html
    """
    #  qint64 QHttpServerConfiguration::maximumHeaderFieldCount() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration23maximumHeaderFieldCountEv',
    )

  def maximumBodySize(self) -> int:
    """
    Calls Qt's 'qint64 QHttpServerConfiguration::maximumBodySize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#maximumBodySize
    """
    #  qint64 QHttpServerConfiguration::maximumBodySize() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerConfiguration15maximumBodySizeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRateLimitPerSecond(self, maxRequests: int) -> None:
    """
    Calls Qt's 'void QHttpServerConfiguration::setRateLimitPerSecond(quint32
    maxRequests)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    maxRequests : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setRateLimitPerSecond(quint32
    #      maxRequests)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration21setRateLimitPerSecondEj',
        maxRequests,
    )

  @overload(int)
  def setMaximumConnectionsPerHost(self, maxPerHost: int) -> None:
    """
    Calls Qt's 'void
    QHttpServerConfiguration::setMaximumConnectionsPerHost(quint32
    maxPerHost)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    maxPerHost : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumConnectionsPerHost(quint32
    #      maxPerHost)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration28setMaximumConnectionsPerHostE'
        'j',
        maxPerHost,
    )

  @overload(int)
  def setMaximumConnections(self, maxConnections: int) -> None:
    """
    Calls Qt's 'void QHttpServerConfiguration::setMaximumConnections(quint32
    maxConnections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    maxConnections : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumConnections(quint32
    #      maxConnections)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration21setMaximumConnectionsEj',
        maxConnections,
    )

  @overload(int)
  def setMaximumUrlSize(self, maxUrlSize: int) -> None:
    """
    Calls Qt's 'void QHttpServerConfiguration::setMaximumUrlSize(qint64
    maxUrlSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#setMaximumUrlSize

    Parameters
    ----------

    maxUrlSize : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumUrlSize(qint64 maxUrlSize)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration17setMaximumUrlSizeEx',
        maxUrlSize,
    )

  @overload(int)
  def setMaximumTotalHeaderSize(self, maxTotalHeadersSize: int) -> None:
    """
    Calls Qt's 'void
    QHttpServerConfiguration::setMaximumTotalHeaderSize(qint64
    maxTotalHeadersSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    maxTotalHeadersSize : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumTotalHeaderSize(qint64
    #      maxTotalHeadersSize)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration25setMaximumTotalHeaderSizeEx',
        maxTotalHeadersSize,
    )

  @overload(int)
  def setMaximumHeaderFieldSize(self, maxSingleHeaderSize: int) -> None:
    """
    Calls Qt's 'void
    QHttpServerConfiguration::setMaximumHeaderFieldSize(qint64
    maxSingleHeaderSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    maxSingleHeaderSize : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumHeaderFieldSize(qint64
    #      maxSingleHeaderSize)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration25setMaximumHeaderFieldSizeEx',
        maxSingleHeaderSize,
    )

  @overload(int)
  def setMaximumHeaderFieldCount(self, maxNumberOfHeaders: int) -> None:
    """
    Calls Qt's 'void
    QHttpServerConfiguration::setMaximumHeaderFieldCount(qint64
    maxNumberOfHeaders)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    maxNumberOfHeaders : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumHeaderFieldCount(qint64
    #      maxNumberOfHeaders)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration26setMaximumHeaderFieldCountEx',
        maxNumberOfHeaders,
    )

  @overload(int)
  def setMaximumBodySize(self, maxBodySize: int) -> None:
    """
    Calls Qt's 'void QHttpServerConfiguration::setMaximumBodySize(qint64
    maxBodySize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#setMaximumBodySize

    Parameters
    ----------

    maxBodySize : int
      Passed on as it is.
    """
    #  void QHttpServerConfiguration::setMaximumBodySize(qint64 maxBodySize)
    self.uglySide.call(
        'ritual_ZN24QHttpServerConfiguration18setMaximumBodySizeEx',
        maxBodySize,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QHttpServerConfiguration) -> bool:
    """
    Calls Qt's 'bool operator==(const QHttpServerConfiguration &lhs, const
    QHttpServerConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#operator==

    Parameters
    ----------

    rhs : QHttpServerConfiguration
      Passed on as a value: Qt reads the C++ QHttpServerConfiguration, which
      stays Python's own.
    """
    #  bool operator==(const QHttpServerConfiguration &lhs, const
    #      QHttpServerConfiguration &rhs)
    return Rituals.call(
        'ritual_ZeqRK24QHttpServerConfigurationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QHttpServerConfiguration) -> bool:
    """
    Calls Qt's 'bool operator!=(const QHttpServerConfiguration &lhs, const
    QHttpServerConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html#operator!=

    Parameters
    ----------

    rhs : QHttpServerConfiguration
      Passed on as a value: Qt reads the C++ QHttpServerConfiguration, which
      stays Python's own.
    """
    #  bool operator!=(const QHttpServerConfiguration &lhs, const
    #      QHttpServerConfiguration &rhs)
    return Rituals.call(
        'ritual_ZneRK24QHttpServerConfigurationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    'QHttpServerConfiguration::QHttpServerConfiguration()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html
    """
    #  QHttpServerConfiguration::QHttpServerConfiguration()
    self._noteCreation(QHttpServerConfiguration, lambda: Rituals.call(
        'ritual_ZN24QHttpServerConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpServerConfiguration) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerConfiguration::QHttpServerConfiguration(const
    QHttpServerConfiguration &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverconfiguration.html

    Parameters
    ----------

    other : QHttpServerConfiguration
      Passed on as a value: Qt reads the C++ QHttpServerConfiguration, which
      stays Python's own.
    """
    #  QHttpServerConfiguration::QHttpServerConfiguration(const
    #      QHttpServerConfiguration &other)
    self._noteCreation(QHttpServerConfiguration, lambda: Rituals.call(
        'ritual_ZN24QHttpServerConfigurationC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def blacklist(*__, **_) -> Never:
    """
    Qt's 'QSpan<const std::pair<QHostAddress, int>>
    QHttpServerConfiguration::blacklist() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.blacklist' has no cute function yet. "
        "Qt's 'QSpan<const std::pair<QHostAddress, int>> "
        "QHttpServerConfiguration::blacklist() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def keepAliveTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::seconds QHttpServerConfiguration::keepAliveTimeout()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.keepAliveTimeout' has no cute function "
        "yet. Qt's 'std::chrono::seconds "
        "QHttpServerConfiguration::keepAliveTimeout() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setBlacklist(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerConfiguration::setBlacklist(QSpan<const
    std::pair<QHostAddress, int>> subnetList)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.setBlacklist' has no cute function yet. "
        "Qt's 'void QHttpServerConfiguration::setBlacklist(QSpan<const "
        "std::pair<QHostAddress, int>> subnetList)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setKeepAliveTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpServerConfiguration::setKeepAliveTimeout(std::chrono::seconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.setKeepAliveTimeout' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerConfiguration::setKeepAliveTimeout(std::chrono::seconds "
        "timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setWhitelist(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerConfiguration::setWhitelist(QSpan<const
    std::pair<QHostAddress, int>> subnetList)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.setWhitelist' has no cute function yet. "
        "Qt's 'void QHttpServerConfiguration::setWhitelist(QSpan<const "
        "std::pair<QHostAddress, int>> subnetList)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerConfiguration::swap(QHttpServerConfiguration
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.swap' has no cute function yet. Qt's "
        "'void QHttpServerConfiguration::swap(QHttpServerConfiguration "
        "&other)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def whitelist(*__, **_) -> Never:
    """
    Qt's 'QSpan<const std::pair<QHostAddress, int>>
    QHttpServerConfiguration::whitelist() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QHttpServerConfiguration.whitelist' has no cute function yet. "
        "Qt's 'QSpan<const std::pair<QHostAddress, int>> "
        "QHttpServerConfiguration::whitelist() const': gives a type Python "
        "has no way to take yet.")
