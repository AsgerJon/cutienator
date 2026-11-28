"""
QOpcUaHistoryEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuahistoryevent.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QOpcUaHistoryEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaHistoryEvent: a plain Python object standing in
  front of one C++ QOpcUaHistoryEvent.

  C++ hands a QOpcUaHistoryEvent around as a copy, so every C++
  QOpcUaHistoryEvent behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryEvent that has a ritual and that Python
  can call so far, 8 names in all: 'statusCode', 'setStatusCode', 'count',
  'addEvent', 'nodeId', 'setNodeId', '__eq__', '__ne__'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaHistoryEvent &QOpcUaHistoryEvent::operator=(const
    QOpcUaHistoryEvent &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaHistoryEvent::QOpcUaHistoryEvent(QOpcUaHistoryEvent
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaHistoryEvent
    &QOpcUaHistoryEvent::operator=(QOpcUaHistoryEvent &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QOpcUaHistoryEvent::~QOpcUaHistoryEvent()': the destructor: Python
    removes its C++ QOpcUaHistoryEvent by it, and has no other use for it.
  - Qt's 'void QOpcUaHistoryEvent::swap(QOpcUaHistoryEvent &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<QVariantList> QOpcUaHistoryEvent::events() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaHistoryEvent is created at the first use, not by
    'QOpcUaHistoryEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaHistoryEvent back gives a copy the ritual made
    for Python, in a new cute QOpcUaHistoryEvent.
  - Each name of Qt's QOpcUaHistoryEvent that has no cute function yet,
    'events', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaHistoryEvent'

  #  Qt's '~QOpcUaHistoryEvent()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaHistoryEvent behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QOpcUaHistoryEventD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaHistoryEvent::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaHistoryEvent::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK18QOpcUaHistoryEvent10statusCodeEv',
    ))

  def count(self) -> int:
    """
    Calls Qt's 'int QOpcUaHistoryEvent::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#count
    """
    #  int QOpcUaHistoryEvent::count() const
    return self.uglySide.call('ritual_ZNK18QOpcUaHistoryEvent5countEv')

  def nodeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaHistoryEvent::nodeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#nodeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaHistoryEvent::nodeId() const
    return self.uglySide.call('ritual_ZNK18QOpcUaHistoryEvent6nodeIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryEvent::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryevent.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaHistoryEvent::setStatusCode(QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN18QOpcUaHistoryEvent13setStatusCodeEN6QOpcUa12UaStatusCod'
        'eE',
        statusCode.value,
    )

  @overload(str)
  def setNodeId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryEvent::setNodeId(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#setNodeId

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaHistoryEvent::setNodeId(const QString &nodeId)
    self.uglySide.call(
        'ritual_ZN18QOpcUaHistoryEvent9setNodeIdERK7QString', nodeId,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaHistoryEvent) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaHistoryEvent &lhs, const
    QOpcUaHistoryEvent &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#operator==

    Parameters
    ----------

    rhs : QOpcUaHistoryEvent
      Passed on as a value: Qt reads the C++ QOpcUaHistoryEvent, which stays
      Python's own.
    """
    #  bool operator==(const QOpcUaHistoryEvent &lhs, const
    #      QOpcUaHistoryEvent &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QOpcUaHistoryEventS1_',
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
  def __ne__(self, rhs: QOpcUaHistoryEvent) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaHistoryEvent &lhs, const
    QOpcUaHistoryEvent &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaHistoryEvent
      Passed on as a value: Qt reads the C++ QOpcUaHistoryEvent, which stays
      Python's own.
    """
    #  bool operator!=(const QOpcUaHistoryEvent &lhs, const
    #      QOpcUaHistoryEvent &rhs)
    return Rituals.call(
        'ritual_ZneRK18QOpcUaHistoryEventS1_',
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
    'QOpcUaHistoryEvent::QOpcUaHistoryEvent()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryevent.html#QOpcUaHistoryEvent
    """
    #  QOpcUaHistoryEvent::QOpcUaHistoryEvent()
    self._noteCreation(QOpcUaHistoryEvent, lambda: Rituals.call(
        'ritual_ZN18QOpcUaHistoryEventC1Ev',
    ))

  @overload(str)
  def __init__(self, nodeId: str) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryEvent::QOpcUaHistoryEvent(const QString &nodeId)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryevent.html#QOpcUaHistoryEvent

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QOpcUaHistoryEvent::QOpcUaHistoryEvent(const QString &nodeId)
    self._noteCreation(QOpcUaHistoryEvent, lambda: Rituals.call(
        'ritual_ZN18QOpcUaHistoryEventC1ERK7QString', nodeId,
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaHistoryEvent) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryEvent::QOpcUaHistoryEvent(const QOpcUaHistoryEvent
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryevent.html#QOpcUaHistoryEvent

    Parameters
    ----------

    other : QOpcUaHistoryEvent
      Passed on as a value: Qt reads the C++ QOpcUaHistoryEvent, which stays
      Python's own.
    """
    #  QOpcUaHistoryEvent::QOpcUaHistoryEvent(const QOpcUaHistoryEvent
    #      &other)
    self._noteCreation(QOpcUaHistoryEvent, lambda: Rituals.call(
        'ritual_ZN18QOpcUaHistoryEventC1ERKS_', self._valueOf(other),
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

  @overload(QList[QVariant])
  def addEvent(self, value: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryEvent::addEvent(const QVariantList
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuahistoryevent.html#addEvent

    Parameters
    ----------

    value : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaHistoryEvent::addEvent(const QVariantList &value)
    self.uglySide.call(
        'ritual_ZN18QOpcUaHistoryEvent8addEventERK5QListI8QVariantE',
        self._valueOf(value),
    )

  @staticmethod
  def events(*__, **_) -> Never:
    """
    Qt's 'QList<QVariantList> QOpcUaHistoryEvent::events() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaHistoryEvent.events' has no cute function yet. Qt's "
        "'QList<QVariantList> QOpcUaHistoryEvent::events() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaHistoryEvent::swap(QOpcUaHistoryEvent &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaHistoryEvent.swap' has no cute function yet. Qt's 'void "
        "QOpcUaHistoryEvent::swap(QOpcUaHistoryEvent &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QOpcUaHistoryEvent>': the list of QOpcUaHistoryEvent, which
#  'QList[QOpcUaHistoryEvent]' gives. It is made here, so that there is one
#  as soon as there can be a QOpcUaHistoryEvent.
QList.createKind(
    QOpcUaHistoryEvent, 'value',
    make='ritual_list_make_QOpcUaHistoryEvent',
    add='ritual_list_add_QOpcUaHistoryEvent',
    size='ritual_list_size_QOpcUaHistoryEvent',
    at='ritual_list_at_QOpcUaHistoryEvent',
    drop='ritual_list_drop_QOpcUaHistoryEvent',
)
