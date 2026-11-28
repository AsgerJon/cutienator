"""
QDnsTextRecord binding of the Qt C++
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

  from ..QtCore import QByteArray


class QDnsTextRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsTextRecord: a plain Python object standing in
  front of one C++ QDnsTextRecord.

  C++ hands a QDnsTextRecord around as a copy, so every C++ QDnsTextRecord
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsTextRecord that has a ritual and that Python can
  call so far, 3 names in all: 'name', 'timeToLive', 'values'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDnsTextRecord &QDnsTextRecord::operator=(QDnsTextRecord &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsTextRecord &QDnsTextRecord::operator=(const QDnsTextRecord
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsTextRecord::~QDnsTextRecord()': the destructor: Python removes
    its C++ QDnsTextRecord by it, and has no other use for it.
  - Qt's 'void QDnsTextRecord::swap(QDnsTextRecord &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDnsTextRecord is created at the first use, not by
    'QDnsTextRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsTextRecord back gives a copy the ritual made for
    Python, in a new cute QDnsTextRecord.
  - Each name of Qt's QDnsTextRecord that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDnsTextRecord'

  #  Qt's '~QDnsTextRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QDnsTextRecord behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QDnsTextRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsTextRecord::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnstextrecord.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsTextRecord::name() const
    return self.uglySide.call('ritual_ZNK14QDnsTextRecord4nameEv')

  def timeToLive(self) -> int:
    """
    Calls Qt's 'quint32 QDnsTextRecord::timeToLive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnstextrecord.html#timeToLive
    """
    #  quint32 QDnsTextRecord::timeToLive() const
    return self.uglySide.call('ritual_ZNK14QDnsTextRecord10timeToLiveEv')

  def values(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QDnsTextRecord::values() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnstextrecord.html#values

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QDnsTextRecord::values() const
    address = self.uglySide.call('ritual_ZNK14QDnsTextRecord6valuesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

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
    Notes what was given, for Qt's 'QDnsTextRecord::QDnsTextRecord()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnstextrecord.html#QDnsTextRecord
    """
    #  QDnsTextRecord::QDnsTextRecord()
    self._noteCreation(QDnsTextRecord, lambda: Rituals.call(
        'ritual_ZN14QDnsTextRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDnsTextRecord) -> None:
    """
    Notes what was given, for Qt's 'QDnsTextRecord::QDnsTextRecord(const
    QDnsTextRecord &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnstextrecord.html#QDnsTextRecord

    Parameters
    ----------

    other : QDnsTextRecord
      Passed on as a value: Qt reads the C++ QDnsTextRecord, which stays
      Python's own.
    """
    #  QDnsTextRecord::QDnsTextRecord(const QDnsTextRecord &other)
    self._noteCreation(QDnsTextRecord, lambda: Rituals.call(
        'ritual_ZN14QDnsTextRecordC1ERKS_', self._valueOf(other),
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
    Qt's 'void QDnsTextRecord::swap(QDnsTextRecord &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsTextRecord.swap' has no cute function yet. Qt's 'void "
        "QDnsTextRecord::swap(QDnsTextRecord &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QDnsTextRecord>': the list of QDnsTextRecord, which
#  'QList[QDnsTextRecord]' gives. It is made here, so that there is one as
#  soon as there can be a QDnsTextRecord.
QList.createKind(
    QDnsTextRecord, 'value',
    make='ritual_list_make_QDnsTextRecord',
    add='ritual_list_add_QDnsTextRecord',
    size='ritual_list_size_QDnsTextRecord',
    at='ritual_list_at_QDnsTextRecord',
    drop='ritual_list_drop_QDnsTextRecord',
)
