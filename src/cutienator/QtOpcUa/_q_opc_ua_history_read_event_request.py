"""
QOpcUaHistoryReadEventRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuahistoryreadeventrequest.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUaMonitoringParameters

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime
  from . import QOpcUaReadItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QOpcUaReadItem = WAIT['QOpcUaReadItem']


class QOpcUaHistoryReadEventRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaHistoryReadEventRequest: a plain Python object
  standing in front of one C++ QOpcUaHistoryReadEventRequest.

  C++ hands a QOpcUaHistoryReadEventRequest around as a copy, so every C++
  QOpcUaHistoryReadEventRequest behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryReadEventRequest that has a ritual and
  that Python can call so far, 13 names in all: 'startTimestamp',
  'setStartTimestamp', 'endTimestamp', 'setEndTimestamp', 'numValuesPerNode',
  'setNumValuesPerNode', 'filter', 'setFilter', 'nodesToRead',
  'setNodesToRead', 'addNodeToRead', '__eq__', '__ne__'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(
    QOpcUaHistoryReadEventRequest &&other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QOpcUaHistoryReadEventRequest
    &QOpcUaHistoryReadEventRequest::operator=(QOpcUaHistoryReadEventRequest
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaHistoryReadEventRequest
    &QOpcUaHistoryReadEventRequest::operator=(const
    QOpcUaHistoryReadEventRequest &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'QOpcUaHistoryReadEventRequest::~QOpcUaHistoryReadEventRequest()':
    the destructor: Python removes its C++ QOpcUaHistoryReadEventRequest by
    it, and has no other use for it.
  - Qt's 'void
    QOpcUaHistoryReadEventRequest::swap(QOpcUaHistoryReadEventRequest
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaHistoryReadEventRequest is created at the first use, not by
    'QOpcUaHistoryReadEventRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaHistoryReadEventRequest back gives a copy the
    ritual made for Python, in a new cute QOpcUaHistoryReadEventRequest.
  - Each name of Qt's QOpcUaHistoryReadEventRequest that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaHistoryReadEventRequest'

  #  Qt's '~QOpcUaHistoryReadEventRequest()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaHistoryReadEventRequest behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QOpcUaHistoryReadEventRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def startTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaHistoryReadEventRequest::startTimestamp()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#startTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaHistoryReadEventRequest::startTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadEventRequest14startTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def endTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaHistoryReadEventRequest::endTimestamp()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#endTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaHistoryReadEventRequest::endTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadEventRequest12endTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def numValuesPerNode(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaHistoryReadEventRequest::numValuesPerNode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html
    """
    #  quint32 QOpcUaHistoryReadEventRequest::numValuesPerNode() const
    return self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadEventRequest16numValuesPerNodeEv',
    )

  def filter(self) -> QOpcUaMonitoringParameters.EventFilter:
    """
    Calls Qt's 'QOpcUaMonitoringParameters::EventFilter
    QOpcUaHistoryReadEventRequest::filter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#filter

    Returns
    -------

    QOpcUaMonitoringParameters.EventFilter
      A new cute QOpcUaMonitoringParameters::EventFilter around the copy Qt
      gave back. Python owns it.
    """
    #  QOpcUaMonitoringParameters::EventFilter
    #      QOpcUaHistoryReadEventRequest::filter() const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadEventRequest6filterEv',
    )
    return QOpcUaMonitoringParameters.EventFilter._cuteOwning(address)

  def nodesToRead(self) -> QList[QOpcUaReadItem]:
    """
    Calls Qt's 'QList<QOpcUaReadItem>
    QOpcUaHistoryReadEventRequest::nodesToRead() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#nodesToRead

    Returns
    -------

    QList[QOpcUaReadItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaReadItem> QOpcUaHistoryReadEventRequest::nodesToRead()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadEventRequest11nodesToReadEv',
    )
    from . import QOpcUaReadItem
    return QList[QOpcUaReadItem]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setStartTimestamp(self, startTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadEventRequest::setStartTimestamp(const
    QDateTime &startTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html

    Parameters
    ----------

    startTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaHistoryReadEventRequest::setStartTimestamp(const QDateTime
    #      &startTimestamp)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequest17setStartTimestampERK9QDa'
        'teTime',
        self._valueOf(startTimestamp),
    )

  @overload(QDateTime)
  def setEndTimestamp(self, endTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadEventRequest::setEndTimestamp(const
    QDateTime &endTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#setEndTimestamp

    Parameters
    ----------

    endTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaHistoryReadEventRequest::setEndTimestamp(const QDateTime
    #      &endTimestamp)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequest15setEndTimestampERK9QDate'
        'Time',
        self._valueOf(endTimestamp),
    )

  @overload(int)
  def setNumValuesPerNode(self, numValuesPerNode: int) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadEventRequest::setNumValuesPerNode(quint32
    numValuesPerNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html

    Parameters
    ----------

    numValuesPerNode : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadEventRequest::setNumValuesPerNode(quint32
    #      numValuesPerNode)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequest19setNumValuesPerNodeEj',
        numValuesPerNode,
    )

  @overload(QOpcUaMonitoringParameters.EventFilter)
  def setFilter(
      self,
      filter: QOpcUaMonitoringParameters.EventFilter,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadEventRequest::setFilter(const
    QOpcUaMonitoringParameters::EventFilter &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#setFilter

    Parameters
    ----------

    filter : QOpcUaMonitoringParameters.EventFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::EventFilter, which stays Python's own.
    """
    #  void QOpcUaHistoryReadEventRequest::setFilter(const
    #      QOpcUaMonitoringParameters::EventFilter &filter)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequest9setFilterERKN26QOpcUaMoni'
        'toringParameters11EventFilterE',
        self._valueOf(filter),
    )

  @overload(QList[QOpcUaReadItem])
  def setNodesToRead(self, nodesToRead: QList[QOpcUaReadItem]) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadEventRequest::setNodesToRead(const
    QList<QOpcUaReadItem> &nodesToRead)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#setNodesToRead

    Parameters
    ----------

    nodesToRead : QList[QOpcUaReadItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaHistoryReadEventRequest::setNodesToRead(const
    #      QList<QOpcUaReadItem> &nodesToRead)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequest14setNodesToReadERK5QListI'
        '14QOpcUaReadItemE',
        self._valueOf(nodesToRead),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaHistoryReadEventRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaHistoryReadEventRequest &lhs,
    const QOpcUaHistoryReadEventRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#operator==

    Parameters
    ----------

    rhs : QOpcUaHistoryReadEventRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadEventRequest,
      which stays Python's own.
    """
    #  bool operator==(const QOpcUaHistoryReadEventRequest &lhs, const
    #      QOpcUaHistoryReadEventRequest &rhs)
    return Rituals.call(
        'ritual_ZeqRK29QOpcUaHistoryReadEventRequestS1_',
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
  def __ne__(self, rhs: QOpcUaHistoryReadEventRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaHistoryReadEventRequest &lhs,
    const QOpcUaHistoryReadEventRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaHistoryReadEventRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadEventRequest,
      which stays Python's own.
    """
    #  bool operator!=(const QOpcUaHistoryReadEventRequest &lhs, const
    #      QOpcUaHistoryReadEventRequest &rhs)
    return Rituals.call(
        'ritual_ZneRK29QOpcUaHistoryReadEventRequestS1_',
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
    'QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html
    """
    #  QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest()
    self._noteCreation(QOpcUaHistoryReadEventRequest, lambda: Rituals.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequestC1Ev',
    ))

  @overload(
      QList[QOpcUaReadItem], QDateTime, QDateTime,
      QOpcUaMonitoringParameters.EventFilter,
  )
  def __init__(
      self,
      nodesToRead: QList[QOpcUaReadItem],
      startTimestamp: QDateTime,
      endTimestamp: QDateTime,
      filter: QOpcUaMonitoringParameters.EventFilter,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(const
    QList<QOpcUaReadItem> &nodesToRead, const QDateTime &startTimestamp,
    const QDateTime &endTimestamp, const
    QOpcUaMonitoringParameters::EventFilter &filter)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html

    Parameters
    ----------

    nodesToRead : QList[QOpcUaReadItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    startTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    endTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    filter : QOpcUaMonitoringParameters.EventFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::EventFilter, which stays Python's own.
    """
    #  QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(const
    #      QList<QOpcUaReadItem> &nodesToRead, const QDateTime
    #      &startTimestamp, const QDateTime &endTimestamp, const
    #      QOpcUaMonitoringParameters::EventFilter &filter)
    self._noteCreation(QOpcUaHistoryReadEventRequest, lambda: Rituals.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequestC1ERK5QListI14QOpcUaReadIt'
        'emERK9QDateTimeS7_RKN26QOpcUaMonitoringParameters11EventFilterE',
        self._valueOf(nodesToRead), self._valueOf(startTimestamp),
        self._valueOf(endTimestamp), self._valueOf(filter),
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaHistoryReadEventRequest) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(const
    QOpcUaHistoryReadEventRequest &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html

    Parameters
    ----------

    other : QOpcUaHistoryReadEventRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadEventRequest,
      which stays Python's own.
    """
    #  QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(const
    #      QOpcUaHistoryReadEventRequest &other)
    self._noteCreation(QOpcUaHistoryReadEventRequest, lambda: Rituals.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequestC1ERKS_',
        self._valueOf(other),
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

  @overload(QOpcUaReadItem)
  def addNodeToRead(self, nodeToRead: QOpcUaReadItem) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadEventRequest::addNodeToRead(const
    QOpcUaReadItem &nodeToRead)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadeventrequest.html#addNodeToRead

    Parameters
    ----------

    nodeToRead : QOpcUaReadItem
      Passed on as a value: Qt reads the C++ QOpcUaReadItem, which stays
      Python's own.
    """
    #  void QOpcUaHistoryReadEventRequest::addNodeToRead(const QOpcUaReadItem
    #      &nodeToRead)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadEventRequest13addNodeToReadERK14QOpcUa'
        'ReadItem',
        self._valueOf(nodeToRead),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaHistoryReadEventRequest::swap(QOpcUaHistoryReadEventRequest
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaHistoryReadEventRequest.swap' has no cute function yet. "
        "Qt's 'void "
        "QOpcUaHistoryReadEventRequest::swap(QOpcUaHistoryReadEventRequest "
        "&other)': takes a type Python has no way to hand over yet.")
