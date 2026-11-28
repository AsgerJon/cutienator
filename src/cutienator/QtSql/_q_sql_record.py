"""
QSqlRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlrecord.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from . import QSqlField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlField = WAIT['QSqlField']
  QVariant = WAIT['QVariant']


class QSqlRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlRecord: a plain Python object standing in front
  of one C++ QSqlRecord.

  C++ hands a QSqlRecord around as a copy, so every C++ QSqlRecord behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlRecord that has a ritual and that Python can
  call so far, 22 names in all: '__eq__', '__ne__', 'value', 'setValue',
  'setNull', 'isNull', 'indexOf', 'fieldName', 'field', 'isGenerated',
  'setGenerated', 'append', 'replace', 'insert', 'remove', 'isEmpty',
  'contains', 'clear', 'clearValues', 'count', 'keyValues', 'detach'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlRecord::QSqlRecord(QSqlRecord &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QSqlRecord &QSqlRecord::operator=(const QSqlRecord &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSqlRecord &QSqlRecord::operator=(QSqlRecord &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSqlRecord::~QSqlRecord()': the destructor: Python removes its C++
    QSqlRecord by it, and has no other use for it.
  - Qt's 'void QSqlRecord::swap(QSqlRecord &other)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QSqlRecord is created at the first use, not by 'QSqlRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlRecord back gives a copy the ritual made for
    Python, in a new cute QSqlRecord.
  - Each name of Qt's QSqlRecord that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlRecord'

  #  Qt's '~QSqlRecord()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlRecord behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QSqlRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def value(self, i: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlRecord::value(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#value

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlRecord::value(int i) const
    address = self.uglySide.call('ritual_ZNK10QSqlRecord5valueEi', i)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def value(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlRecord::value(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#value

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlRecord::value(QAnyStringView name) const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlRecord5valueE14QAnyStringView', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isNull(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::isNull(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#isNull

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlRecord::isNull(int i) const
    return self.uglySide.call('ritual_ZNK10QSqlRecord6isNullEi', i)

  @overload(str)
  def isNull(self, name: str) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::isNull(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#isNull

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlRecord::isNull(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlRecord6isNullE14QAnyStringView', name,
    )

  @overload(str)
  def indexOf(self, name: str) -> int:
    """
    Calls Qt's 'int QSqlRecord::indexOf(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#indexOf

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QSqlRecord::indexOf(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlRecord7indexOfE14QAnyStringView', name,
    )

  @overload(int)
  def fieldName(self, i: int) -> str:
    """
    Calls Qt's 'QString QSqlRecord::fieldName(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#fieldName

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlRecord::fieldName(int i) const
    return self.uglySide.call('ritual_ZNK10QSqlRecord9fieldNameEi', i)

  @overload(int)
  def field(self, i: int) -> QSqlField:
    """
    Calls Qt's 'QSqlField QSqlRecord::field(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#field

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QSqlField
      A new cute QSqlField around the copy Qt gave back. Python owns it.
    """
    #  QSqlField QSqlRecord::field(int i) const
    address = self.uglySide.call('ritual_ZNK10QSqlRecord5fieldEi', i)
    from . import QSqlField
    return QSqlField._cuteOwning(address)

  @overload(str)
  def field(self, name: str) -> QSqlField:
    """
    Calls Qt's 'QSqlField QSqlRecord::field(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#field

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlField
      A new cute QSqlField around the copy Qt gave back. Python owns it.
    """
    #  QSqlField QSqlRecord::field(QAnyStringView name) const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlRecord5fieldE14QAnyStringView', name,
    )
    from . import QSqlField
    return QSqlField._cuteOwning(address)

  @overload(int)
  def isGenerated(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::isGenerated(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#isGenerated

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlRecord::isGenerated(int i) const
    return self.uglySide.call('ritual_ZNK10QSqlRecord11isGeneratedEi', i)

  @overload(str)
  def isGenerated(self, name: str) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::isGenerated(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#isGenerated

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlRecord::isGenerated(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlRecord11isGeneratedE14QAnyStringView', name,
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#isEmpty
    """
    #  bool QSqlRecord::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QSqlRecord7isEmptyEv')

  @overload(str)
  def contains(self, name: str) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::contains(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#contains

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlRecord::contains(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlRecord8containsE14QAnyStringView', name,
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QSqlRecord::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#count
    """
    #  int QSqlRecord::count() const
    return self.uglySide.call('ritual_ZNK10QSqlRecord5countEv')

  @overload(THIS)
  def keyValues(self, keyFields: QSqlRecord) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlRecord::keyValues(const QSqlRecord &keyFields)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#keyValues

    Parameters
    ----------

    keyFields : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlRecord::keyValues(const QSqlRecord &keyFields) const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlRecord9keyValuesERKS_', self._valueOf(keyFields),
    )
    return QSqlRecord._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setValue(self, i: int, val: QVariant) -> None:
    """
    Calls Qt's 'void QSqlRecord::setValue(int i, const QVariant &val)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#setValue

    Parameters
    ----------

    i : int
      Passed on as it is.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSqlRecord::setValue(int i, const QVariant &val)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord8setValueEiRK8QVariant', i, self._valueOf(val),
    )

  @overload(str, QVariant)
  def setValue(self, name: str, val: QVariant) -> None:
    """
    Calls Qt's 'void QSqlRecord::setValue(QAnyStringView name, const QVariant
    &val)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#setValue

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSqlRecord::setValue(QAnyStringView name, const QVariant &val)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord8setValueE14QAnyStringViewRK8QVariant',
        name, self._valueOf(val),
    )

  @overload(int)
  def setNull(self, i: int) -> None:
    """
    Calls Qt's 'void QSqlRecord::setNull(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#setNull

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QSqlRecord::setNull(int i)
    self.uglySide.call('ritual_ZN10QSqlRecord7setNullEi', i)

  @overload(str)
  def setNull(self, name: str) -> None:
    """
    Calls Qt's 'void QSqlRecord::setNull(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#setNull

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlRecord::setNull(QAnyStringView name)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord7setNullE14QAnyStringView', name,
    )

  @overload(str, bool)
  def setGenerated(self, name: str, generated: bool) -> None:
    """
    Calls Qt's 'void QSqlRecord::setGenerated(QAnyStringView name, bool
    generated)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#setGenerated

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    generated : bool
      Passed on as it is.
    """
    #  void QSqlRecord::setGenerated(QAnyStringView name, bool generated)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord12setGeneratedE14QAnyStringViewb',
        name, generated,
    )

  @overload(int, bool)
  def setGenerated(self, i: int, generated: bool) -> None:
    """
    Calls Qt's 'void QSqlRecord::setGenerated(int i, bool generated)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#setGenerated

    Parameters
    ----------

    i : int
      Passed on as it is.

    generated : bool
      Passed on as it is.
    """
    #  void QSqlRecord::setGenerated(int i, bool generated)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord12setGeneratedEib', i, generated,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::operator==(const QSqlRecord &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#operator==

    Parameters
    ----------

    other : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlRecord::operator==(const QSqlRecord &other) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlRecordeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlRecord::operator!=(const QSqlRecord &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#operator!=

    Parameters
    ----------

    other : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlRecord::operator!=(const QSqlRecord &other) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlRecordneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QSqlRecord::QSqlRecord()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#QSqlRecord
    """
    #  QSqlRecord::QSqlRecord()
    self._noteCreation(QSqlRecord, lambda: Rituals.call(
        'ritual_ZN10QSqlRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QSqlRecord) -> None:
    """
    Notes what was given, for Qt's 'QSqlRecord::QSqlRecord(const QSqlRecord
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#QSqlRecord

    Parameters
    ----------

    other : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  QSqlRecord::QSqlRecord(const QSqlRecord &other)
    self._noteCreation(QSqlRecord, lambda: Rituals.call(
        'ritual_ZN10QSqlRecordC1ERKS_', self._valueOf(other),
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

  @overload(QSqlField)
  def append(self, field: QSqlField) -> None:
    """
    Calls Qt's 'void QSqlRecord::append(const QSqlField &field)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#append

    Parameters
    ----------

    field : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  void QSqlRecord::append(const QSqlField &field)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord6appendERK9QSqlField', self._valueOf(field),
    )

  @overload(int, QSqlField)
  def replace(self, pos: int, field: QSqlField) -> None:
    """
    Calls Qt's 'void QSqlRecord::replace(int pos, const QSqlField &field)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#replace

    Parameters
    ----------

    pos : int
      Passed on as it is.

    field : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  void QSqlRecord::replace(int pos, const QSqlField &field)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord7replaceEiRK9QSqlField',
        pos, self._valueOf(field),
    )

  @overload(int, QSqlField)
  def insert(self, pos: int, field: QSqlField) -> None:
    """
    Calls Qt's 'void QSqlRecord::insert(int pos, const QSqlField &field)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#insert

    Parameters
    ----------

    pos : int
      Passed on as it is.

    field : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  void QSqlRecord::insert(int pos, const QSqlField &field)
    self.uglySide.call(
        'ritual_ZN10QSqlRecord6insertEiRK9QSqlField',
        pos, self._valueOf(field),
    )

  @overload(int)
  def remove(self, pos: int) -> None:
    """
    Calls Qt's 'void QSqlRecord::remove(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#remove

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QSqlRecord::remove(int pos)
    self.uglySide.call('ritual_ZN10QSqlRecord6removeEi', pos)

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlRecord::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#clear
    """
    #  void QSqlRecord::clear()
    self.uglySide.call('ritual_ZN10QSqlRecord5clearEv')

  def clearValues(self) -> None:
    """
    Calls Qt's 'void QSqlRecord::clearValues()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#clearValues
    """
    #  void QSqlRecord::clearValues()
    self.uglySide.call('ritual_ZN10QSqlRecord11clearValuesEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QSqlRecord::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrecord.html#detach
    """
    #  void QSqlRecord::detach()
    self.uglySide.call('ritual_ZN10QSqlRecord6detachEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSqlRecord::swap(QSqlRecord &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlRecord.swap' has no cute function yet. Qt's 'void "
        "QSqlRecord::swap(QSqlRecord &other)': takes a type Python has no "
        "way to hand over yet.")
