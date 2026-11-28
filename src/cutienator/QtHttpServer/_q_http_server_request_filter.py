"""
QHttpServerRequestFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrequestfilter_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QHttpServerRequestFilter to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtNetwork import QHostAddress
  from . import QHttpServerConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QHttpServerConfiguration = WAIT['QHttpServerConfiguration']


class QHttpServerRequestFilter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerRequestFilter: a plain Python object
  standing in front of one C++ QHttpServerRequestFilter.

  C++ hands a QHttpServerRequestFilter around as a copy, so every C++
  QHttpServerRequestFilter behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpServerRequestFilter that has a ritual and that
  Python can call so far, 9 names in all: 'setConfiguration',
  'isRequestAllowed', 'isRequestWithinRate', 'isUrlSizeAllowed',
  'isTotalHeaderSizeAllowed', 'isHeaderFieldSizeAllowed',
  'isNumberOfHeaderFieldsAllowed', 'isBodySizeAllowed',
  'maxRequestPerPeriod'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QHttpServerRequestFilter::cleanIpInfoGarbage(QHash<QHostAddress,
    IpInfo>::iterator it, qint64 currTime)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QHttpServerRequestFilter::~QHttpServerRequestFilter()': the
    destructor: Python removes its C++ QHttpServerRequestFilter by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QHttpServerRequestFilter is created at the first use, not by
    'QHttpServerRequestFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerRequestFilter back gives a copy the ritual
    made for Python, in a new cute QHttpServerRequestFilter.
  - Each name of Qt's QHttpServerRequestFilter that has no cute function yet,
    'cleanIpInfoGarbage', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerRequestFilter'

  #  Qt's '~QHttpServerRequestFilter()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpServerRequestFilter behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QHttpServerRequestFilterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress)
  def isRequestAllowed(self, peerAddress: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QHttpServerRequestFilter::isRequestAllowed(const
    QHostAddress &peerAddress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#isRequestAllowed

    Parameters
    ----------

    peerAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QHttpServerRequestFilter::isRequestAllowed(const QHostAddress
    #      &peerAddress) const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter16isRequestAllowedERK12QHostAd'
        'dress',
        self._valueOf(peerAddress),
    )

  @overload(int)
  def isUrlSizeAllowed(self, urlSize: int) -> bool:
    """
    Calls Qt's 'bool QHttpServerRequestFilter::isUrlSizeAllowed(qsizetype
    urlSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#isUrlSizeAllowed

    Parameters
    ----------

    urlSize : int
      Passed on as it is.
    """
    #  bool QHttpServerRequestFilter::isUrlSizeAllowed(qsizetype urlSize)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter16isUrlSizeAllowedEx', urlSize,
    )

  @overload(int)
  def isTotalHeaderSizeAllowed(self, headerSize: int) -> bool:
    """
    Calls Qt's 'bool
    QHttpServerRequestFilter::isTotalHeaderSizeAllowed(qsizetype headerSize)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html

    Parameters
    ----------

    headerSize : int
      Passed on as it is.
    """
    #  bool QHttpServerRequestFilter::isTotalHeaderSizeAllowed(qsizetype
    #      headerSize) const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter24isTotalHeaderSizeAllowedEx',
        headerSize,
    )

  @overload(int)
  def isHeaderFieldSizeAllowed(self, headerSize: int) -> bool:
    """
    Calls Qt's 'bool
    QHttpServerRequestFilter::isHeaderFieldSizeAllowed(qsizetype headerSize)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html

    Parameters
    ----------

    headerSize : int
      Passed on as it is.
    """
    #  bool QHttpServerRequestFilter::isHeaderFieldSizeAllowed(qsizetype
    #      headerSize) const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter24isHeaderFieldSizeAllowedEx',
        headerSize,
    )

  @overload(int)
  def isNumberOfHeaderFieldsAllowed(self, headerSize: int) -> bool:
    """
    Calls Qt's 'bool
    QHttpServerRequestFilter::isNumberOfHeaderFieldsAllowed(qsizetype
    headerSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html

    Parameters
    ----------

    headerSize : int
      Passed on as it is.
    """
    #  bool QHttpServerRequestFilter::isNumberOfHeaderFieldsAllowed(qsizetype
    #      headerSize) const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter29isNumberOfHeaderFieldsAllowe'
        'dEx',
        headerSize,
    )

  @overload(int)
  def isBodySizeAllowed(self, bodySize: int) -> bool:
    """
    Calls Qt's 'bool QHttpServerRequestFilter::isBodySizeAllowed(qint64
    bodySize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#isBodySizeAllowed

    Parameters
    ----------

    bodySize : int
      Passed on as it is.
    """
    #  bool QHttpServerRequestFilter::isBodySizeAllowed(qint64 bodySize)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter17isBodySizeAllowedEx',
        bodySize,
    )

  def maxRequestPerPeriod(self) -> int:
    """
    Calls Qt's 'unsigned int QHttpServerRequestFilter::maxRequestPerPeriod()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#maxRequestPerPeriod
    """
    #  unsigned int QHttpServerRequestFilter::maxRequestPerPeriod() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpServerRequestFilter19maxRequestPerPeriodEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHttpServerConfiguration)
  def setConfiguration(self, config: QHttpServerConfiguration) -> None:
    """
    Calls Qt's 'void QHttpServerRequestFilter::setConfiguration(const
    QHttpServerConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#setConfiguration

    Parameters
    ----------

    config : QHttpServerConfiguration
      Passed on as a value: Qt reads the C++ QHttpServerConfiguration, which
      stays Python's own.
    """
    #  void QHttpServerRequestFilter::setConfiguration(const
    #      QHttpServerConfiguration &config)
    self.uglySide.call(
        'ritual_ZN24QHttpServerRequestFilter16setConfigurationERK24QHttpSer'
        'verConfiguration',
        self._valueOf(config),
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

  @overload(QHostAddress)
  def isRequestWithinRate(self, peerAddress: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QHttpServerRequestFilter::isRequestWithinRate(const
    QHostAddress &peerAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#isRequestWithinRate

    Parameters
    ----------

    peerAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QHttpServerRequestFilter::isRequestWithinRate(const QHostAddress
    #      &peerAddress)
    return self.uglySide.call(
        'ritual_ZN24QHttpServerRequestFilter19isRequestWithinRateERK12QHost'
        'Address',
        self._valueOf(peerAddress),
    )

  @overload(QHostAddress, int)
  def isRequestWithinRate(
      self,
      peerAddress: QHostAddress,
      currTimeMSec: int,
  ) -> bool:
    """
    Calls Qt's 'bool QHttpServerRequestFilter::isRequestWithinRate(const
    QHostAddress &peerAddress, qint64 currTimeMSec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestfilter.html#isRequestWithinRate

    Parameters
    ----------

    peerAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    currTimeMSec : int
      Passed on as it is.
    """
    #  bool QHttpServerRequestFilter::isRequestWithinRate(const QHostAddress
    #      &peerAddress, qint64 currTimeMSec)
    return self.uglySide.call(
        'ritual_ZN24QHttpServerRequestFilter19isRequestWithinRateERK12QHost'
        'Addressx',
        self._valueOf(peerAddress), currTimeMSec,
    )

  @staticmethod
  def cleanIpInfoGarbage(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpServerRequestFilter::cleanIpInfoGarbage(QHash<QHostAddress,
    IpInfo>::iterator it, qint64 currTime)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerRequestFilter.cleanIpInfoGarbage' has no cute function "
        "yet. Qt's 'void "
        "QHttpServerRequestFilter::cleanIpInfoGarbage(QHash<QHostAddress, "
        "IpInfo>::iterator it, qint64 currTime)': takes a type Python has "
        "no way to hand over yet.")
