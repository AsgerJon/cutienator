"""
QOpcUaHistoryReadRawRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuahistoryreadrawrequest.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

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


class QOpcUaHistoryReadRawRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaHistoryReadRawRequest: a plain Python object
  standing in front of one C++ QOpcUaHistoryReadRawRequest.

  C++ hands a QOpcUaHistoryReadRawRequest around as a copy, so every C++
  QOpcUaHistoryReadRawRequest behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryReadRawRequest that has a ritual and
  that Python can call so far, 15 names in all: 'startTimestamp',
  'setStartTimestamp', 'endTimestamp', 'setEndTimestamp', 'numValuesPerNode',
  'setNumValuesPerNode', 'returnBounds', 'setReturnBounds',
  'timestampsToReturn', 'setTimestampsToReturn', 'nodesToRead',
  'setNodesToRead', 'addNodeToRead', '__eq__', '__ne__'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaHistoryReadRawRequest::~QOpcUaHistoryReadRawRequest()': the
    destructor: Python removes its C++ QOpcUaHistoryReadRawRequest by it, and
    has no other use for it.
  - Qt's 'void QOpcUaHistoryReadRawRequest::swap(QOpcUaHistoryReadRawRequest
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaHistoryReadRawRequest
    &QOpcUaHistoryReadRawRequest::operator=(const QOpcUaHistoryReadRawRequest
    &other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QOpcUaHistoryReadRawRequest is created at the first use, not by
    'QOpcUaHistoryReadRawRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaHistoryReadRawRequest back gives a copy the
    ritual made for Python, in a new cute QOpcUaHistoryReadRawRequest.
  - Each name of Qt's QOpcUaHistoryReadRawRequest that has no cute function
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
  __qt_class__ = 'QOpcUaHistoryReadRawRequest'

  #  Qt's '~QOpcUaHistoryReadRawRequest()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaHistoryReadRawRequest behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QOpcUaHistoryReadRawRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def startTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaHistoryReadRawRequest::startTimestamp()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#startTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaHistoryReadRawRequest::startTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK27QOpcUaHistoryReadRawRequest14startTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def endTimestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QOpcUaHistoryReadRawRequest::endTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#endTimestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOpcUaHistoryReadRawRequest::endTimestamp() const
    address = self.uglySide.call(
        'ritual_ZNK27QOpcUaHistoryReadRawRequest12endTimestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def numValuesPerNode(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaHistoryReadRawRequest::numValuesPerNode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#numValuesPerNode
    """
    #  quint32 QOpcUaHistoryReadRawRequest::numValuesPerNode() const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaHistoryReadRawRequest16numValuesPerNodeEv',
    )

  def returnBounds(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaHistoryReadRawRequest::returnBounds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#returnBounds
    """
    #  bool QOpcUaHistoryReadRawRequest::returnBounds() const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaHistoryReadRawRequest12returnBoundsEv',
    )

  def timestampsToReturn(self) -> QOpcUa.TimestampsToReturn:
    """
    Calls Qt's 'QOpcUa::TimestampsToReturn
    QOpcUaHistoryReadRawRequest::timestampsToReturn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html

    Returns
    -------

    QOpcUa.TimestampsToReturn
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.TimestampsToReturn(number)' gives.
    """
    #  QOpcUa::TimestampsToReturn
    #      QOpcUaHistoryReadRawRequest::timestampsToReturn() const
    return QOpcUa.TimestampsToReturn(self.uglySide.call(
        'ritual_ZNK27QOpcUaHistoryReadRawRequest18timestampsToReturnEv',
    ))

  def nodesToRead(self) -> QList[QOpcUaReadItem]:
    """
    Calls Qt's 'QList<QOpcUaReadItem>
    QOpcUaHistoryReadRawRequest::nodesToRead() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#nodesToRead

    Returns
    -------

    QList[QOpcUaReadItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaReadItem> QOpcUaHistoryReadRawRequest::nodesToRead() const
    address = self.uglySide.call(
        'ritual_ZNK27QOpcUaHistoryReadRawRequest11nodesToReadEv',
    )
    from . import QOpcUaReadItem
    return QList[QOpcUaReadItem]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setStartTimestamp(self, startTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadRawRequest::setStartTimestamp(const
    QDateTime &startTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#setStartTimestamp

    Parameters
    ----------

    startTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaHistoryReadRawRequest::setStartTimestamp(const QDateTime
    #      &startTimestamp)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest17setStartTimestampERK9QDate'
        'Time',
        self._valueOf(startTimestamp),
    )

  @overload(QDateTime)
  def setEndTimestamp(self, endTimestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadRawRequest::setEndTimestamp(const
    QDateTime &endTimestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#setEndTimestamp

    Parameters
    ----------

    endTimestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOpcUaHistoryReadRawRequest::setEndTimestamp(const QDateTime
    #      &endTimestamp)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest15setEndTimestampERK9QDateTi'
        'me',
        self._valueOf(endTimestamp),
    )

  @overload(int)
  def setNumValuesPerNode(self, numValuesPerNode: int) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadRawRequest::setNumValuesPerNode(quint32
    numValuesPerNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html

    Parameters
    ----------

    numValuesPerNode : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadRawRequest::setNumValuesPerNode(quint32
    #      numValuesPerNode)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest19setNumValuesPerNodeEj',
        numValuesPerNode,
    )

  @overload(bool)
  def setReturnBounds(self, returnBounds: bool) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadRawRequest::setReturnBounds(bool
    returnBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#setReturnBounds

    Parameters
    ----------

    returnBounds : bool
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadRawRequest::setReturnBounds(bool returnBounds)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest15setReturnBoundsEb',
        returnBounds,
    )

  @overload(QOpcUa.TimestampsToReturn)
  def setTimestampsToReturn(
      self,
      timestampsToReturn: QOpcUa.TimestampsToReturn,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadRawRequest::setTimestampsToReturn(QOpcUa::
    TimestampsToReturn timestampsToReturn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html

    Parameters
    ----------

    timestampsToReturn : QOpcUa.TimestampsToReturn
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadRawRequest::setTimestampsToReturn(QOpcUa::
    #      TimestampsToReturn timestampsToReturn)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest21setTimestampsToReturnEN6QO'
        'pcUa18TimestampsToReturnE',
        timestampsToReturn.value,
    )

  @overload(QList[QOpcUaReadItem])
  def setNodesToRead(self, nodesToRead: QList[QOpcUaReadItem]) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadRawRequest::setNodesToRead(const
    QList<QOpcUaReadItem> &nodesToRead)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#setNodesToRead

    Parameters
    ----------

    nodesToRead : QList[QOpcUaReadItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaHistoryReadRawRequest::setNodesToRead(const
    #      QList<QOpcUaReadItem> &nodesToRead)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest14setNodesToReadERK5QListI14'
        'QOpcUaReadItemE',
        self._valueOf(nodesToRead),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaHistoryReadRawRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaHistoryReadRawRequest &lhs, const
    QOpcUaHistoryReadRawRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#operator==

    Parameters
    ----------

    rhs : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.
    """
    #  bool operator==(const QOpcUaHistoryReadRawRequest &lhs, const
    #      QOpcUaHistoryReadRawRequest &rhs)
    return Rituals.call(
        'ritual_ZeqRK27QOpcUaHistoryReadRawRequestS1_',
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
  def __ne__(self, rhs: QOpcUaHistoryReadRawRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaHistoryReadRawRequest &lhs, const
    QOpcUaHistoryReadRawRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.
    """
    #  bool operator!=(const QOpcUaHistoryReadRawRequest &lhs, const
    #      QOpcUaHistoryReadRawRequest &rhs)
    return Rituals.call(
        'ritual_ZneRK27QOpcUaHistoryReadRawRequestS1_',
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
    'QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html
    """
    #  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest()
    self._noteCreation(QOpcUaHistoryReadRawRequest, lambda: Rituals.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequestC1Ev',
    ))

  @overload(QList[QOpcUaReadItem], QDateTime, QDateTime)
  @overload(QList[QOpcUaReadItem], QDateTime, QDateTime, int)
  @overload(QList[QOpcUaReadItem], QDateTime, QDateTime, int, bool)
  def __init__(
      self,
      nodesToRead: QList[QOpcUaReadItem],
      startTimestamp: QDateTime,
      endTimestamp: QDateTime,
      numValuesPerNode: int = 0,
      returnBounds: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
    QList<QOpcUaReadItem> &nodesToRead, const QDateTime &startTimestamp,
    const QDateTime &endTimestamp, quint32 numValuesPerNode, bool
    returnBounds)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html

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

    numValuesPerNode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    returnBounds : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
    #      QList<QOpcUaReadItem> &nodesToRead, const QDateTime
    #      &startTimestamp, const QDateTime &endTimestamp, quint32
    #      numValuesPerNode, bool returnBounds)
    self._noteCreation(QOpcUaHistoryReadRawRequest, lambda: Rituals.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequestC1ERK5QListI14QOpcUaReadItem'
        'ERK9QDateTimeS7_jb',
        self._valueOf(nodesToRead), self._valueOf(startTimestamp),
        self._valueOf(endTimestamp), numValuesPerNode, returnBounds,
    ))

  @overload(
      QList[QOpcUaReadItem], QDateTime, QDateTime, QOpcUa.TimestampsToReturn,
  )
  def __init__(
      self,
      nodesToRead: QList[QOpcUaReadItem],
      startTimestamp: QDateTime,
      endTimestamp: QDateTime,
      timestampsToReturn: QOpcUa.TimestampsToReturn,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
    QList<QOpcUaReadItem> &nodesToRead, const QDateTime &startTimestamp,
    const QDateTime &endTimestamp, QOpcUa::TimestampsToReturn
    timestampsToReturn)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html

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

    timestampsToReturn : QOpcUa.TimestampsToReturn
      Passed on as its number.
    """
    #  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
    #      QList<QOpcUaReadItem> &nodesToRead, const QDateTime
    #      &startTimestamp, const QDateTime &endTimestamp,
    #      QOpcUa::TimestampsToReturn timestampsToReturn)
    self._noteCreation(QOpcUaHistoryReadRawRequest, lambda: Rituals.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequestC1ERK5QListI14QOpcUaReadItem'
        'ERK9QDateTimeS7_N6QOpcUa18TimestampsToReturnE',
        self._valueOf(nodesToRead), self._valueOf(startTimestamp),
        self._valueOf(endTimestamp), timestampsToReturn.value,
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaHistoryReadRawRequest) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
    QOpcUaHistoryReadRawRequest &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html

    Parameters
    ----------

    other : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.
    """
    #  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
    #      QOpcUaHistoryReadRawRequest &other)
    self._noteCreation(QOpcUaHistoryReadRawRequest, lambda: Rituals.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequestC1ERKS_',
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
    Calls Qt's 'void QOpcUaHistoryReadRawRequest::addNodeToRead(const
    QOpcUaReadItem &nodeToRead)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadrawrequest.html#addNodeToRead

    Parameters
    ----------

    nodeToRead : QOpcUaReadItem
      Passed on as a value: Qt reads the C++ QOpcUaReadItem, which stays
      Python's own.
    """
    #  void QOpcUaHistoryReadRawRequest::addNodeToRead(const QOpcUaReadItem
    #      &nodeToRead)
    self.uglySide.call(
        'ritual_ZN27QOpcUaHistoryReadRawRequest13addNodeToReadERK14QOpcUaRe'
        'adItem',
        self._valueOf(nodeToRead),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaHistoryReadRawRequest::swap(QOpcUaHistoryReadRawRequest
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaHistoryReadRawRequest.swap' has no cute function yet. Qt's "
        "'void "
        "QOpcUaHistoryReadRawRequest::swap(QOpcUaHistoryReadRawRequest "
        "&other)': takes a type Python has no way to hand over yet.")
