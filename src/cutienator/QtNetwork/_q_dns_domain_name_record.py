"""
QDnsDomainNameRecord binding of the Qt C++
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


class QDnsDomainNameRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsDomainNameRecord: a plain Python object standing
  in front of one C++ QDnsDomainNameRecord.

  C++ hands a QDnsDomainNameRecord around as a copy, so every C++
  QDnsDomainNameRecord behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsDomainNameRecord that has a ritual and that
  Python can call so far, 3 names in all: 'name', 'timeToLive', 'value'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDnsDomainNameRecord
    &QDnsDomainNameRecord::operator=(QDnsDomainNameRecord &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsDomainNameRecord &QDnsDomainNameRecord::operator=(const
    QDnsDomainNameRecord &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDnsDomainNameRecord::~QDnsDomainNameRecord()': the destructor:
    Python removes its C++ QDnsDomainNameRecord by it, and has no other use
    for it.
  - Qt's 'void QDnsDomainNameRecord::swap(QDnsDomainNameRecord &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDnsDomainNameRecord is created at the first use, not by
    'QDnsDomainNameRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsDomainNameRecord back gives a copy the ritual
    made for Python, in a new cute QDnsDomainNameRecord.
  - Each name of Qt's QDnsDomainNameRecord that has no cute function yet,
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
  __qt_class__ = 'QDnsDomainNameRecord'

  #  Qt's '~QDnsDomainNameRecord()'. Naming it makes this a value class:
  #  Python owns every C++ QDnsDomainNameRecord behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QDnsDomainNameRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsDomainNameRecord::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsdomainnamerecord.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsDomainNameRecord::name() const
    return self.uglySide.call('ritual_ZNK20QDnsDomainNameRecord4nameEv')

  def timeToLive(self) -> int:
    """
    Calls Qt's 'quint32 QDnsDomainNameRecord::timeToLive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsdomainnamerecord.html#timeToLive
    """
    #  quint32 QDnsDomainNameRecord::timeToLive() const
    return self.uglySide.call(
        'ritual_ZNK20QDnsDomainNameRecord10timeToLiveEv',
    )

  def value(self) -> str:
    """
    Calls Qt's 'QString QDnsDomainNameRecord::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsdomainnamerecord.html#value

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsDomainNameRecord::value() const
    return self.uglySide.call('ritual_ZNK20QDnsDomainNameRecord5valueEv')

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
    'QDnsDomainNameRecord::QDnsDomainNameRecord()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsdomainnamerecord.html#QDnsDomainNameRecord
    """
    #  QDnsDomainNameRecord::QDnsDomainNameRecord()
    self._noteCreation(QDnsDomainNameRecord, lambda: Rituals.call(
        'ritual_ZN20QDnsDomainNameRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDnsDomainNameRecord) -> None:
    """
    Notes what was given, for Qt's
    'QDnsDomainNameRecord::QDnsDomainNameRecord(const QDnsDomainNameRecord
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsdomainnamerecord.html#QDnsDomainNameRecord

    Parameters
    ----------

    other : QDnsDomainNameRecord
      Passed on as a value: Qt reads the C++ QDnsDomainNameRecord, which
      stays Python's own.
    """
    #  QDnsDomainNameRecord::QDnsDomainNameRecord(const QDnsDomainNameRecord
    #      &other)
    self._noteCreation(QDnsDomainNameRecord, lambda: Rituals.call(
        'ritual_ZN20QDnsDomainNameRecordC1ERKS_', self._valueOf(other),
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
    Qt's 'void QDnsDomainNameRecord::swap(QDnsDomainNameRecord &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsDomainNameRecord.swap' has no cute function yet. Qt's 'void "
        "QDnsDomainNameRecord::swap(QDnsDomainNameRecord &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QDnsDomainNameRecord>': the list of QDnsDomainNameRecord,
#  which 'QList[QDnsDomainNameRecord]' gives. It is made here, so that there
#  is one as soon as there can be a QDnsDomainNameRecord.
QList.createKind(
    QDnsDomainNameRecord, 'value',
    make='ritual_list_make_QDnsDomainNameRecord',
    add='ritual_list_add_QDnsDomainNameRecord',
    size='ritual_list_size_QDnsDomainNameRecord',
    at='ritual_list_at_QDnsDomainNameRecord',
    drop='ritual_list_drop_QDnsDomainNameRecord',
)
