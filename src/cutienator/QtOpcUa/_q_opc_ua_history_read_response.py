"""
QOpcUaHistoryReadResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuahistoryreadresponse.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QOpcUaHistoryData, QOpcUaHistoryEvent
  from . import QOpcUaHistoryReadResponseImpl
  from . import QOpcUaHistoryReadResponsePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaHistoryData = WAIT['QOpcUaHistoryData']
  QOpcUaHistoryEvent = WAIT['QOpcUaHistoryEvent']
  QOpcUaHistoryReadResponseImpl = WAIT['QOpcUaHistoryReadResponseImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaHistoryReadResponse(QObject):
  """
  The cute side of Qt's QOpcUaHistoryReadResponse: a plain Python object
  standing in front of one C++ QOpcUaHistoryReadResponse.

  It is built on the cute 'QObject', as Qt's QOpcUaHistoryReadResponse is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryReadResponse that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'd_func',
  'hasMoreData', 'readMoreData', 'state', 'releaseContinuationPoints',
  'data', 'events', 'serviceResult', 'readHistoryDataFinished',
  'readHistoryEventsFinished', 'stateChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaHistoryReadResponse::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QOpcUaHistoryReadResponse::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QOpcUaHistoryReadResponsePrivate
    *QOpcUaHistoryReadResponse::d_func() const': takes in Python what
    'QOpcUaHistoryReadResponsePrivate *QOpcUaHistoryReadResponse::d_func()'
    takes.
  - Qt's 'QOpcUaHistoryReadResponse::~QOpcUaHistoryReadResponse()': the
    destructor: Python never removes a C++ QOpcUaHistoryReadResponse.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaHistoryReadResponse is created at the first use, not by
    'QOpcUaHistoryReadResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaHistoryReadResponse.
  - Qt tells when it has removed the C++ QOpcUaHistoryReadResponse. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpcUaHistoryReadResponse, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QOpcUaHistoryReadResponse::State' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    Reading = Kee[int](1)
    Finished = Kee[int](2)
    MoreDataAvailable = Kee[int](3)
    Error = Kee[int](4)

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
    Calls Qt's 'QString QOpcUaHistoryReadResponse::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#tr

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
    #  QString QOpcUaHistoryReadResponse::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QOpcUaHistoryReadResponse2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaHistoryReadResponse'

  #  A C++ QOpcUaHistoryReadResponse Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaHistoryReadResponse'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaHistoryReadResponse::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaHistoryReadResponse::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaHistoryReadResponse10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasMoreData(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaHistoryReadResponse::hasMoreData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#hasMoreData
    """
    #  bool QOpcUaHistoryReadResponse::hasMoreData() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaHistoryReadResponse11hasMoreDataEv',
    )

  def state(self) -> State:
    """
    Calls Qt's 'State QOpcUaHistoryReadResponse::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QOpcUaHistoryReadResponse::state() const
    return QOpcUaHistoryReadResponse.State(self.uglySide.call(
        'ritual_ZNK25QOpcUaHistoryReadResponse5stateEv',
    ))

  def data(self) -> QList[QOpcUaHistoryData]:
    """
    Calls Qt's 'QList<QOpcUaHistoryData> QOpcUaHistoryReadResponse::data()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#data

    Returns
    -------

    QList[QOpcUaHistoryData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaHistoryData> QOpcUaHistoryReadResponse::data() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaHistoryReadResponse4dataEv',
    )
    from . import QOpcUaHistoryData
    return QList[QOpcUaHistoryData]._cuteOwning(address)

  def events(self) -> QList[QOpcUaHistoryEvent]:
    """
    Calls Qt's 'QList<QOpcUaHistoryEvent> QOpcUaHistoryReadResponse::events()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#events

    Returns
    -------

    QList[QOpcUaHistoryEvent]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaHistoryEvent> QOpcUaHistoryReadResponse::events() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaHistoryReadResponse6eventsEv',
    )
    from . import QOpcUaHistoryEvent
    return QList[QOpcUaHistoryEvent]._cuteOwning(address)

  def serviceResult(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode
    QOpcUaHistoryReadResponse::serviceResult() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#serviceResult

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaHistoryReadResponse::serviceResult() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK25QOpcUaHistoryReadResponse13serviceResultEv',
    ))

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

  @overload(QOpcUaHistoryReadResponseImpl)
  @overload(NoneType)
  def __init__(self, impl: Optional[QOpcUaHistoryReadResponseImpl]) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadResponse::QOpcUaHistoryReadResponse(
    QOpcUaHistoryReadResponseImpl *impl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html

    Parameters
    ----------

    impl : Optional[QOpcUaHistoryReadResponseImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpcUaHistoryReadResponse::QOpcUaHistoryReadResponse(
    #      QOpcUaHistoryReadResponseImpl *impl)
    self._noteCreation(QOpcUaHistoryReadResponse, lambda: Rituals.call(
        'ritual_ZN25QOpcUaHistoryReadResponseC1EP29QOpcUaHistoryReadRespons'
        'eImpl',
        self._addressOf(impl),
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

  def d_func(self) -> Optional[QOpcUaHistoryReadResponsePrivate]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponsePrivate
    *QOpcUaHistoryReadResponse::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#d_func

    Returns
    -------

    Optional[QOpcUaHistoryReadResponsePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponsePrivate *QOpcUaHistoryReadResponse::d_func()
    address = self.uglySide.call(
        'ritual_ZN25QOpcUaHistoryReadResponse6d_funcEv',
    )
    from . import QOpcUaHistoryReadResponsePrivate
    return QOpcUaHistoryReadResponsePrivate._cuteAt(address)

  def readMoreData(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaHistoryReadResponse::readMoreData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#readMoreData
    """
    #  bool QOpcUaHistoryReadResponse::readMoreData()
    return self.uglySide.call(
        'ritual_ZN25QOpcUaHistoryReadResponse12readMoreDataEv',
    )

  def releaseContinuationPoints(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaHistoryReadResponse::releaseContinuationPoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html
    """
    #  bool QOpcUaHistoryReadResponse::releaseContinuationPoints()
    return self.uglySide.call(
        'ritual_ZN25QOpcUaHistoryReadResponse25releaseContinuationPointsEv',
    )

  @overload(QList[QOpcUaHistoryData], QOpcUa.UaStatusCode)
  def readHistoryDataFinished(
      self,
      results: QList[QOpcUaHistoryData],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadResponse::readHistoryDataFinished(const
    QList<QOpcUaHistoryData> &results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html

    Parameters
    ----------

    results : QList[QOpcUaHistoryData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponse::readHistoryDataFinished(const
    #      QList<QOpcUaHistoryData> &results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN25QOpcUaHistoryReadResponse23readHistoryDataFinishedERK5Q'
        'ListI17QOpcUaHistoryDataEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(QList[QOpcUaHistoryEvent], QOpcUa.UaStatusCode)
  def readHistoryEventsFinished(
      self,
      results: QList[QOpcUaHistoryEvent],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponse::readHistoryEventsFinished(const
    QList<QOpcUaHistoryEvent> &results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html

    Parameters
    ----------

    results : QList[QOpcUaHistoryEvent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponse::readHistoryEventsFinished(const
    #      QList<QOpcUaHistoryEvent> &results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN25QOpcUaHistoryReadResponse25readHistoryEventsFinishedERK'
        '5QListI18QOpcUaHistoryEventEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(State)
  def stateChanged(self, state: State) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadResponse::stateChanged(State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponse.html#stateChanged

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponse::stateChanged(State state)
    self.uglySide.call(
        'ritual_ZN25QOpcUaHistoryReadResponse12stateChangedENS_5StateE',
        state.value,
    )
