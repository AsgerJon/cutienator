"""
QNdefFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndeffilter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNdefRecord

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QNdefMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNdefMessage = WAIT['QNdefMessage']


class QNdefFilter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNdefFilter: a plain Python object standing in front
  of one C++ QNdefFilter.

  C++ hands a QNdefFilter around as a copy, so every C++ QNdefFilter behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefFilter that has a ritual and that Python can
  call so far, 7 names in all: 'clear', 'setOrderMatch', 'orderMatch',
  'appendRecord', 'recordCount', 'recordAt', 'match'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefFilter::~QNdefFilter()': the destructor: Python removes its
    C++ QNdefFilter by it, and has no other use for it.
  - Qt's 'QNdefFilter &QNdefFilter::operator=(const QNdefFilter &other)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QNdefFilter is created at the first use, not by
    'QNdefFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefFilter back gives a copy the ritual made for
    Python, in a new cute QNdefFilter.
  """

  #  The classes Qt writes inside QNdefFilter, each a class in here as in
  #  C++.

  class Record(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QNdefFilter::Record: a plain Python object standing
    in front of one C++ QNdefFilter::Record.

    C++ hands a QNdefFilter::Record around as a copy, so every C++
    QNdefFilter::Record behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QNdefFilter::Record yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QNdefFilter::Record::~Record()': the destructor: Python removes
      its C++ QNdefFilter::Record by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QNdefFilter::Record is created at the first use, not by
      'QNdefFilter::Record(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QNdefFilter::Record back gives a copy the ritual
      made for Python, in a new cute QNdefFilter::Record.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QNdefFilter::Record'

    #  Qt's '~QNdefFilter::Record()'. Naming it makes this a value class:
    #  Python owns every C++ QNdefFilter::Record behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QNdefFilter6RecordD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefFilter'

  #  Qt's '~QNdefFilter()'. Naming it makes this a value class: Python owns
  #  every C++ QNdefFilter behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QNdefFilterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def orderMatch(self) -> bool:
    """
    Calls Qt's 'bool QNdefFilter::orderMatch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#orderMatch
    """
    #  bool QNdefFilter::orderMatch() const
    return self.uglySide.call('ritual_ZNK11QNdefFilter10orderMatchEv')

  def recordCount(self) -> int:
    """
    Calls Qt's 'qsizetype QNdefFilter::recordCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#recordCount
    """
    #  qsizetype QNdefFilter::recordCount() const
    return self.uglySide.call('ritual_ZNK11QNdefFilter11recordCountEv')

  @overload(int)
  def recordAt(self, i: int) -> Record:
    """
    Calls Qt's 'Record QNdefFilter::recordAt(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#recordAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Record
      A new cute QNdefFilter::Record around the copy Qt gave back. Python
      owns it.
    """
    #  Record QNdefFilter::recordAt(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK11QNdefFilter8recordAtEx', i)
    return QNdefFilter.Record._cuteOwning(address)

  @overload(QNdefMessage)
  def match(self, message: QNdefMessage) -> bool:
    """
    Calls Qt's 'bool QNdefFilter::match(const QNdefMessage &message) const'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#match

    Parameters
    ----------

    message : QNdefMessage
      Passed on as a value: Qt reads the C++ QNdefMessage, which stays
      Python's own.
    """
    #  bool QNdefFilter::match(const QNdefMessage &message) const
    return self.uglySide.call(
        'ritual_ZNK11QNdefFilter5matchERK12QNdefMessage',
        self._valueOf(message),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setOrderMatch(self, on: bool) -> None:
    """
    Calls Qt's 'void QNdefFilter::setOrderMatch(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#setOrderMatch

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QNdefFilter::setOrderMatch(bool on)
    self.uglySide.call('ritual_ZN11QNdefFilter13setOrderMatchEb', on)

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
    Notes what was given, for Qt's 'QNdefFilter::QNdefFilter()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#QNdefFilter
    """
    #  QNdefFilter::QNdefFilter()
    self._noteCreation(QNdefFilter, lambda: Rituals.call(
        'ritual_ZN11QNdefFilterC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QNdefFilter) -> None:
    """
    Notes what was given, for Qt's 'QNdefFilter::QNdefFilter(const
    QNdefFilter &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#QNdefFilter

    Parameters
    ----------

    other : QNdefFilter
      Passed on as a value: Qt reads the C++ QNdefFilter, which stays
      Python's own.
    """
    #  QNdefFilter::QNdefFilter(const QNdefFilter &other)
    self._noteCreation(QNdefFilter, lambda: Rituals.call(
        'ritual_ZN11QNdefFilterC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QNdefFilter::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#clear
    """
    #  void QNdefFilter::clear()
    self.uglySide.call('ritual_ZN11QNdefFilter5clearEv')

  @overload(QNdefRecord.TypeNameFormat, QByteArray)
  @overload(QNdefRecord.TypeNameFormat, QByteArray, int)
  @overload(QNdefRecord.TypeNameFormat, QByteArray, int, int)
  def appendRecord(
      self,
      typeNameFormat: QNdefRecord.TypeNameFormat,
      type: QByteArray,
      min: int = 1,
      max: int = 1,
  ) -> bool:
    """
    Calls Qt's 'bool QNdefFilter::appendRecord(QNdefRecord::TypeNameFormat
    typeNameFormat, const QByteArray &type, unsigned int min, unsigned int
    max)'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#appendRecord

    Parameters
    ----------

    typeNameFormat : QNdefRecord.TypeNameFormat
      Passed on as its number.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    min : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    max : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QNdefFilter::appendRecord(QNdefRecord::TypeNameFormat
    #      typeNameFormat, const QByteArray &type, unsigned int min, unsigned
    #      int max)
    return self.uglySide.call(
        'ritual_ZN11QNdefFilter12appendRecordEN11QNdefRecord14TypeNameForma'
        'tERK10QByteArrayjj',
        typeNameFormat.value, self._valueOf(type), min, max,
    )

  @overload(Record)
  def appendRecord(self, record: Record) -> bool:
    """
    Calls Qt's 'bool QNdefFilter::appendRecord(const Record &record)'.

    Qt's own words: https://doc.qt.io/qt-6/qndeffilter.html#appendRecord

    Parameters
    ----------

    record : Record
      Passed on as a value: Qt reads the C++ QNdefFilter::Record, which stays
      Python's own.
    """
    #  bool QNdefFilter::appendRecord(const Record &record)
    return self.uglySide.call(
        'ritual_ZN11QNdefFilter12appendRecordERKNS_6RecordE',
        self._valueOf(record),
    )
