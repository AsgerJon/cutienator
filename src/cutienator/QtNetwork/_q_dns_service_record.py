"""
QDnsServiceRecord binding of the Qt C++
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


class QDnsServiceRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsServiceRecord: a plain Python object standing in
  front of one C++ QDnsServiceRecord.

  C++ hands a QDnsServiceRecord around as a copy, so every C++
  QDnsServiceRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsServiceRecord that has a ritual and that Python
  can call so far, 6 names in all: 'name', 'port', 'priority', 'target',
  'timeToLive', 'weight'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDnsServiceRecord &QDnsServiceRecord::operator=(QDnsServiceRecord
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsServiceRecord &QDnsServiceRecord::operator=(const
    QDnsServiceRecord &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDnsServiceRecord::~QDnsServiceRecord()': the destructor: Python
    removes its C++ QDnsServiceRecord by it, and has no other use for it.
  - Qt's 'void QDnsServiceRecord::swap(QDnsServiceRecord &other)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDnsServiceRecord is created at the first use, not by
    'QDnsServiceRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsServiceRecord back gives a copy the ritual made
    for Python, in a new cute QDnsServiceRecord.
  - Each name of Qt's QDnsServiceRecord that has no cute function yet,
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
  __qt_class__ = 'QDnsServiceRecord'

  #  Qt's '~QDnsServiceRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QDnsServiceRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QDnsServiceRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsServiceRecord::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsservicerecord.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsServiceRecord::name() const
    return self.uglySide.call('ritual_ZNK17QDnsServiceRecord4nameEv')

  def port(self) -> int:
    """
    Calls Qt's 'quint16 QDnsServiceRecord::port() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsservicerecord.html#port
    """
    #  quint16 QDnsServiceRecord::port() const
    return self.uglySide.call('ritual_ZNK17QDnsServiceRecord4portEv')

  def priority(self) -> int:
    """
    Calls Qt's 'quint16 QDnsServiceRecord::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsservicerecord.html#priority
    """
    #  quint16 QDnsServiceRecord::priority() const
    return self.uglySide.call('ritual_ZNK17QDnsServiceRecord8priorityEv')

  def target(self) -> str:
    """
    Calls Qt's 'QString QDnsServiceRecord::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsservicerecord.html#target

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsServiceRecord::target() const
    return self.uglySide.call('ritual_ZNK17QDnsServiceRecord6targetEv')

  def timeToLive(self) -> int:
    """
    Calls Qt's 'quint32 QDnsServiceRecord::timeToLive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsservicerecord.html#timeToLive
    """
    #  quint32 QDnsServiceRecord::timeToLive() const
    return self.uglySide.call('ritual_ZNK17QDnsServiceRecord10timeToLiveEv')

  def weight(self) -> int:
    """
    Calls Qt's 'quint16 QDnsServiceRecord::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnsservicerecord.html#weight
    """
    #  quint16 QDnsServiceRecord::weight() const
    return self.uglySide.call('ritual_ZNK17QDnsServiceRecord6weightEv')

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
    Notes what was given, for Qt's 'QDnsServiceRecord::QDnsServiceRecord()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsservicerecord.html#QDnsServiceRecord
    """
    #  QDnsServiceRecord::QDnsServiceRecord()
    self._noteCreation(QDnsServiceRecord, lambda: Rituals.call(
        'ritual_ZN17QDnsServiceRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDnsServiceRecord) -> None:
    """
    Notes what was given, for Qt's
    'QDnsServiceRecord::QDnsServiceRecord(const QDnsServiceRecord &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnsservicerecord.html#QDnsServiceRecord

    Parameters
    ----------

    other : QDnsServiceRecord
      Passed on as a value: Qt reads the C++ QDnsServiceRecord, which stays
      Python's own.
    """
    #  QDnsServiceRecord::QDnsServiceRecord(const QDnsServiceRecord &other)
    self._noteCreation(QDnsServiceRecord, lambda: Rituals.call(
        'ritual_ZN17QDnsServiceRecordC1ERKS_', self._valueOf(other),
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
    Qt's 'void QDnsServiceRecord::swap(QDnsServiceRecord &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsServiceRecord.swap' has no cute function yet. Qt's 'void "
        "QDnsServiceRecord::swap(QDnsServiceRecord &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QDnsServiceRecord>': the list of QDnsServiceRecord, which
#  'QList[QDnsServiceRecord]' gives. It is made here, so that there is one as
#  soon as there can be a QDnsServiceRecord.
QList.createKind(
    QDnsServiceRecord, 'value',
    make='ritual_list_make_QDnsServiceRecord',
    add='ritual_list_add_QDnsServiceRecord',
    size='ritual_list_size_QDnsServiceRecord',
    at='ritual_list_at_QDnsServiceRecord',
    drop='ritual_list_drop_QDnsServiceRecord',
)
