"""
QNdefMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndefmessage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QNdefRecord
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNdefRecord = WAIT['QNdefRecord']


class QNdefMessage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNdefMessage: a plain Python object standing in front
  of one C++ QNdefMessage.

  C++ hands a QNdefMessage around as a copy, so every C++ QNdefMessage behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefMessage that has a ritual and that Python can
  call so far, 3 names in all: '__eq__', 'toByteArray', 'fromByteArray'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefMessage &QNdefMessage::operator=(const QNdefMessage &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QNdefMessage &QNdefMessage::operator=(QNdefMessage &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QNdefMessage::~QNdefMessage()': the destructor: Python removes its
    C++ QNdefMessage by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefMessage is created at the first use, not by
    'QNdefMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefMessage back gives a copy the ritual made for
    Python, in a new cute QNdefMessage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def fromByteArray(message: QByteArray) -> QNdefMessage:
    """
    Calls Qt's 'QNdefMessage QNdefMessage::fromByteArray(const QByteArray
    &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#fromByteArray

    Parameters
    ----------

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QNdefMessage
      A new cute QNdefMessage around the copy Qt gave back. Python owns it.
    """
    #  QNdefMessage QNdefMessage::fromByteArray(const QByteArray &message)
    address = Rituals.call(
        'ritual_ZN12QNdefMessage13fromByteArrayERK10QByteArray',
        CuteMixin._valueOf(message),
    )
    return QNdefMessage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefMessage'

  #  Qt's '~QNdefMessage()'. Naming it makes this a value class: Python owns
  #  every C++ QNdefMessage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QNdefMessageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNdefMessage::toByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#toByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNdefMessage::toByteArray() const
    address = self.uglySide.call('ritual_ZNK12QNdefMessage11toByteArrayEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNdefMessage) -> bool:
    """
    Calls Qt's 'bool QNdefMessage::operator==(const QNdefMessage &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#operator==

    Parameters
    ----------

    other : QNdefMessage
      Passed on as a value: Qt reads the C++ QNdefMessage, which stays
      Python's own.
    """
    #  bool QNdefMessage::operator==(const QNdefMessage &other) const
    return self.uglySide.call(
        'ritual_ZNK12QNdefMessageeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QNdefMessage::QNdefMessage()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#QNdefMessage
    """
    #  QNdefMessage::QNdefMessage()
    self._noteCreation(QNdefMessage, lambda: Rituals.call(
        'ritual_ZN12QNdefMessageC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, record: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's 'QNdefMessage::QNdefMessage(const
    QNdefRecord &record)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#QNdefMessage

    Parameters
    ----------

    record : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefMessage::QNdefMessage(const QNdefRecord &record)
    self._noteCreation(QNdefMessage, lambda: Rituals.call(
        'ritual_ZN12QNdefMessageC1ERK11QNdefRecord', self._valueOf(record),
    ))

  @overload(THIS)
  def __init__(self, message: QNdefMessage) -> None:
    """
    Notes what was given, for Qt's 'QNdefMessage::QNdefMessage(const
    QNdefMessage &message)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#QNdefMessage

    Parameters
    ----------

    message : QNdefMessage
      Passed on as a value: Qt reads the C++ QNdefMessage, which stays
      Python's own.
    """
    #  QNdefMessage::QNdefMessage(const QNdefMessage &message)
    self._noteCreation(QNdefMessage, lambda: Rituals.call(
        'ritual_ZN12QNdefMessageC1ERKS_', self._valueOf(message),
    ))

  @overload(QList[QNdefRecord])
  def __init__(self, records: QList[QNdefRecord]) -> None:
    """
    Notes what was given, for Qt's 'QNdefMessage::QNdefMessage(const
    QList<QNdefRecord> &records)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefmessage.html#QNdefMessage

    Parameters
    ----------

    records : QList[QNdefRecord]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QNdefMessage::QNdefMessage(const QList<QNdefRecord> &records)
    self._noteCreation(QNdefMessage, lambda: Rituals.call(
        'ritual_ZN12QNdefMessageC1ERK5QListI11QNdefRecordE',
        self._valueOf(records),
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


#  Qt's 'QList<QNdefMessage>': the list of QNdefMessage, which
#  'QList[QNdefMessage]' gives. It is made here, so that there is one as soon
#  as there can be a QNdefMessage.
QList.createKind(
    QNdefMessage, 'value',
    make='ritual_list_make_QNdefMessage',
    add='ritual_list_add_QNdefMessage',
    size='ritual_list_size_QNdefMessage',
    at='ritual_list_at_QNdefMessage',
    drop='ritual_list_drop_QNdefMessage',
)
