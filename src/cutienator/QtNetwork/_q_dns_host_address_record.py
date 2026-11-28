"""
QDnsHostAddressRecord binding of the Qt C++
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

  from . import QHostAddress


class QDnsHostAddressRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsHostAddressRecord: a plain Python object standing
  in front of one C++ QDnsHostAddressRecord.

  C++ hands a QDnsHostAddressRecord around as a copy, so every C++
  QDnsHostAddressRecord behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsHostAddressRecord that has a ritual and that
  Python can call so far, 3 names in all: 'name', 'timeToLive', 'value'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDnsHostAddressRecord
    &QDnsHostAddressRecord::operator=(QDnsHostAddressRecord &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsHostAddressRecord &QDnsHostAddressRecord::operator=(const
    QDnsHostAddressRecord &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QDnsHostAddressRecord::~QDnsHostAddressRecord()': the destructor:
    Python removes its C++ QDnsHostAddressRecord by it, and has no other use
    for it.
  - Qt's 'void QDnsHostAddressRecord::swap(QDnsHostAddressRecord &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDnsHostAddressRecord is created at the first use, not by
    'QDnsHostAddressRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsHostAddressRecord back gives a copy the ritual
    made for Python, in a new cute QDnsHostAddressRecord.
  - Each name of Qt's QDnsHostAddressRecord that has no cute function yet,
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
  __qt_class__ = 'QDnsHostAddressRecord'

  #  Qt's '~QDnsHostAddressRecord()'. Naming it makes this a value class:
  #  Python owns every C++ QDnsHostAddressRecord behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QDnsHostAddressRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsHostAddressRecord::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnshostaddressrecord.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsHostAddressRecord::name() const
    return self.uglySide.call('ritual_ZNK21QDnsHostAddressRecord4nameEv')

  def timeToLive(self) -> int:
    """
    Calls Qt's 'quint32 QDnsHostAddressRecord::timeToLive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnshostaddressrecord.html#timeToLive
    """
    #  quint32 QDnsHostAddressRecord::timeToLive() const
    return self.uglySide.call(
        'ritual_ZNK21QDnsHostAddressRecord10timeToLiveEv',
    )

  def value(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QDnsHostAddressRecord::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnshostaddressrecord.html#value

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QDnsHostAddressRecord::value() const
    address = self.uglySide.call('ritual_ZNK21QDnsHostAddressRecord5valueEv')
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

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
    'QDnsHostAddressRecord::QDnsHostAddressRecord()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnshostaddressrecord.html#QDnsHostAddressRecord
    """
    #  QDnsHostAddressRecord::QDnsHostAddressRecord()
    self._noteCreation(QDnsHostAddressRecord, lambda: Rituals.call(
        'ritual_ZN21QDnsHostAddressRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDnsHostAddressRecord) -> None:
    """
    Notes what was given, for Qt's
    'QDnsHostAddressRecord::QDnsHostAddressRecord(const QDnsHostAddressRecord
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnshostaddressrecord.html#QDnsHostAddressRecord

    Parameters
    ----------

    other : QDnsHostAddressRecord
      Passed on as a value: Qt reads the C++ QDnsHostAddressRecord, which
      stays Python's own.
    """
    #  QDnsHostAddressRecord::QDnsHostAddressRecord(const
    #      QDnsHostAddressRecord &other)
    self._noteCreation(QDnsHostAddressRecord, lambda: Rituals.call(
        'ritual_ZN21QDnsHostAddressRecordC1ERKS_', self._valueOf(other),
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
    Qt's 'void QDnsHostAddressRecord::swap(QDnsHostAddressRecord &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsHostAddressRecord.swap' has no cute function yet. Qt's 'void "
        "QDnsHostAddressRecord::swap(QDnsHostAddressRecord &other)': takes "
        "a type Python has no way to hand over yet.")


#  Qt's 'QList<QDnsHostAddressRecord>': the list of QDnsHostAddressRecord,
#  which 'QList[QDnsHostAddressRecord]' gives. It is made here, so that there
#  is one as soon as there can be a QDnsHostAddressRecord.
QList.createKind(
    QDnsHostAddressRecord, 'value',
    make='ritual_list_make_QDnsHostAddressRecord',
    add='ritual_list_add_QDnsHostAddressRecord',
    size='ritual_list_size_QDnsHostAddressRecord',
    at='ritual_list_at_QDnsHostAddressRecord',
    drop='ritual_list_drop_QDnsHostAddressRecord',
)
