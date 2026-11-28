"""
QDnsMailExchangeRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDnsMailExchangeRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsMailExchangeRecord: a plain Python object
  standing in front of one C++ QDnsMailExchangeRecord.

  C++ hands a QDnsMailExchangeRecord around as a copy, so every C++
  QDnsMailExchangeRecord behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsMailExchangeRecord that has a ritual and that
  Python can call so far, 4 names in all: 'exchange', 'name', 'preference',
  'timeToLive'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDnsMailExchangeRecord
    &QDnsMailExchangeRecord::operator=(QDnsMailExchangeRecord &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsMailExchangeRecord &QDnsMailExchangeRecord::operator=(const
    QDnsMailExchangeRecord &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QDnsMailExchangeRecord::~QDnsMailExchangeRecord()': the destructor:
    Python removes its C++ QDnsMailExchangeRecord by it, and has no other use
    for it.
  - Qt's 'void QDnsMailExchangeRecord::swap(QDnsMailExchangeRecord &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDnsMailExchangeRecord is created at the first use, not by
    'QDnsMailExchangeRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsMailExchangeRecord back gives a copy the ritual
    made for Python, in a new cute QDnsMailExchangeRecord.
  - Each name of Qt's QDnsMailExchangeRecord that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QDnsMailExchangeRecord'

  #  Qt's '~QDnsMailExchangeRecord()'. Naming it makes this a value class:
  #  Python owns every C++ QDnsMailExchangeRecord behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QDnsMailExchangeRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def exchange(self) -> str:
    """
    Calls Qt's 'QString QDnsMailExchangeRecord::exchange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsmailexchangerecord.html#exchange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsMailExchangeRecord::exchange() const
    return self.uglySide.call(
        'ritual_ZNK22QDnsMailExchangeRecord8exchangeEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsMailExchangeRecord::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsmailexchangerecord.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsMailExchangeRecord::name() const
    return self.uglySide.call('ritual_ZNK22QDnsMailExchangeRecord4nameEv')

  def preference(self) -> int:
    """
    Calls Qt's 'quint16 QDnsMailExchangeRecord::preference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsmailexchangerecord.html#preference
    """
    #  quint16 QDnsMailExchangeRecord::preference() const
    return self.uglySide.call(
        'ritual_ZNK22QDnsMailExchangeRecord10preferenceEv',
    )

  def timeToLive(self) -> int:
    """
    Calls Qt's 'quint32 QDnsMailExchangeRecord::timeToLive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsmailexchangerecord.html#timeToLive
    """
    #  quint32 QDnsMailExchangeRecord::timeToLive() const
    return self.uglySide.call(
        'ritual_ZNK22QDnsMailExchangeRecord10timeToLiveEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDnsMailExchangeRecord::QDnsMailExchangeRecord()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsmailexchangerecord.html#QDnsMailExchangeRecord
    """
    #  QDnsMailExchangeRecord::QDnsMailExchangeRecord()
    self._noteCreation(QDnsMailExchangeRecord, lambda: Rituals.call(
        'ritual_ZN22QDnsMailExchangeRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDnsMailExchangeRecord) -> None:
    """
    Notes what was given, for Qt's
    'QDnsMailExchangeRecord::QDnsMailExchangeRecord(const
    QDnsMailExchangeRecord &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsmailexchangerecord.html#QDnsMailExchangeRecord

    Parameters
    ----------

    other : QDnsMailExchangeRecord
      Passed on as a value: Qt reads the C++ QDnsMailExchangeRecord, which
      stays Python's own.
    """
    #  QDnsMailExchangeRecord::QDnsMailExchangeRecord(const
    #      QDnsMailExchangeRecord &other)
    self._noteCreation(QDnsMailExchangeRecord, lambda: Rituals.call(
        'ritual_ZN22QDnsMailExchangeRecordC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDnsMailExchangeRecord::swap(QDnsMailExchangeRecord &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsMailExchangeRecord.swap' has no cute function yet. Qt's 'void "
        "QDnsMailExchangeRecord::swap(QDnsMailExchangeRecord &other)': "
        "takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QDnsMailExchangeRecord>': the list of QDnsMailExchangeRecord,
#  which 'QList[QDnsMailExchangeRecord]' gives. It is made here, so that
#  there is one as soon as there can be a QDnsMailExchangeRecord.
QList.createKind(
    QDnsMailExchangeRecord, 'value',
    make='ritual_list_make_QDnsMailExchangeRecord',
    add='ritual_list_add_QDnsMailExchangeRecord',
    size='ritual_list_size_QDnsMailExchangeRecord',
    at='ritual_list_at_QDnsMailExchangeRecord',
    drop='ritual_list_drop_QDnsMailExchangeRecord',
)
