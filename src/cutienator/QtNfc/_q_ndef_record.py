"""
QNdefRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndefrecord.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QNdefRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNdefRecord: a plain Python object standing in front
  of one C++ QNdefRecord.

  C++ hands a QNdefRecord around as a copy, so every C++ QNdefRecord behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefRecord that has a ritual and that Python can
  call so far, 12 names in all: 'setTypeNameFormat', 'typeNameFormat',
  'setType', 'type', 'setId', 'id', 'setPayload', 'payload', 'isEmpty',
  '__eq__', '__ne__', 'clear'. It can be made from Python, in 5 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefRecord::~QNdefRecord()': the destructor: Python removes its
    C++ QNdefRecord by it, and has no other use for it.
  - Qt's 'QNdefRecord &QNdefRecord::operator=(const QNdefRecord &other)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QNdefRecord is created at the first use, not by
    'QNdefRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefRecord back gives a copy the ritual made for
    Python, in a new cute QNdefRecord.
  - Each name of Qt's QNdefRecord that has no cute function yet,
    'isRecordType', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QNdefRecord, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class TypeNameFormat(CuteNum):
    """
    The enum 'QNdefRecord::TypeNameFormat' of Qt, with the 6 names Qt gives
    in it.
    """

    Empty = Kee[int](0)
    NfcRtd = Kee[int](1)
    Mime = Kee[int](2)
    Uri = Kee[int](3)
    ExternalRtd = Kee[int](4)
    Unknown = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefRecord'

  #  Qt's '~QNdefRecord()'. Naming it makes this a value class: Python owns
  #  every C++ QNdefRecord behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QNdefRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeNameFormat(self) -> TypeNameFormat:
    """
    Calls Qt's 'TypeNameFormat QNdefRecord::typeNameFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#typeNameFormat

    Returns
    -------

    TypeNameFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TypeNameFormat(number)'
      gives.
    """
    #  TypeNameFormat QNdefRecord::typeNameFormat() const
    return QNdefRecord.TypeNameFormat(self.uglySide.call(
        'ritual_ZNK11QNdefRecord14typeNameFormatEv',
    ))

  def type(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNdefRecord::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#type

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNdefRecord::type() const
    address = self.uglySide.call('ritual_ZNK11QNdefRecord4typeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def id(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNdefRecord::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#id

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNdefRecord::id() const
    address = self.uglySide.call('ritual_ZNK11QNdefRecord2idEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNdefRecord::payload() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNdefRecord::payload() const
    address = self.uglySide.call('ritual_ZNK11QNdefRecord7payloadEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QNdefRecord::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#isEmpty
    """
    #  bool QNdefRecord::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QNdefRecord7isEmptyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TypeNameFormat)
  def setTypeNameFormat(self, typeNameFormat: TypeNameFormat) -> None:
    """
    Calls Qt's 'void QNdefRecord::setTypeNameFormat(TypeNameFormat
    typeNameFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#setTypeNameFormat

    Parameters
    ----------

    typeNameFormat : TypeNameFormat
      Passed on as its number.
    """
    #  void QNdefRecord::setTypeNameFormat(TypeNameFormat typeNameFormat)
    self.uglySide.call(
        'ritual_ZN11QNdefRecord17setTypeNameFormatENS_14TypeNameFormatE',
        typeNameFormat.value,
    )

  @overload(QByteArray)
  def setType(self, type: QByteArray) -> None:
    """
    Calls Qt's 'void QNdefRecord::setType(const QByteArray &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#setType

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNdefRecord::setType(const QByteArray &type)
    self.uglySide.call(
        'ritual_ZN11QNdefRecord7setTypeERK10QByteArray', self._valueOf(type),
    )

  @overload(QByteArray)
  def setId(self, id: QByteArray) -> None:
    """
    Calls Qt's 'void QNdefRecord::setId(const QByteArray &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#setId

    Parameters
    ----------

    id : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNdefRecord::setId(const QByteArray &id)
    self.uglySide.call(
        'ritual_ZN11QNdefRecord5setIdERK10QByteArray', self._valueOf(id),
    )

  @overload(QByteArray)
  def setPayload(self, payload: QByteArray) -> None:
    """
    Calls Qt's 'void QNdefRecord::setPayload(const QByteArray &payload)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#setPayload

    Parameters
    ----------

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNdefRecord::setPayload(const QByteArray &payload)
    self.uglySide.call(
        'ritual_ZN11QNdefRecord10setPayloadERK10QByteArray',
        self._valueOf(payload),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNdefRecord) -> bool:
    """
    Calls Qt's 'bool QNdefRecord::operator==(const QNdefRecord &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#operator==

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  bool QNdefRecord::operator==(const QNdefRecord &other) const
    return self.uglySide.call(
        'ritual_ZNK11QNdefRecordeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QNdefRecord) -> bool:
    """
    Calls Qt's 'bool QNdefRecord::operator!=(const QNdefRecord &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#operator!=

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  bool QNdefRecord::operator!=(const QNdefRecord &other) const
    return self.uglySide.call(
        'ritual_ZNK11QNdefRecordneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QNdefRecord::QNdefRecord()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#QNdefRecord
    """
    #  QNdefRecord::QNdefRecord()
    self._noteCreation(QNdefRecord, lambda: Rituals.call(
        'ritual_ZN11QNdefRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's 'QNdefRecord::QNdefRecord(const
    QNdefRecord &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#QNdefRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefRecord::QNdefRecord(const QNdefRecord &other)
    self._noteCreation(QNdefRecord, lambda: Rituals.call(
        'ritual_ZN11QNdefRecordC1ERKS_', self._valueOf(other),
    ))

  @overload(THIS, TypeNameFormat, QByteArray)
  def __init__(
      self,
      other: QNdefRecord,
      typeNameFormat: TypeNameFormat,
      type: QByteArray,
  ) -> None:
    """
    Notes what was given, for Qt's 'QNdefRecord::QNdefRecord(const
    QNdefRecord &other, TypeNameFormat typeNameFormat, const QByteArray
    &type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#QNdefRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.

    typeNameFormat : TypeNameFormat
      Passed on as its number.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QNdefRecord::QNdefRecord(const QNdefRecord &other, TypeNameFormat
    #      typeNameFormat, const QByteArray &type)
    self._noteCreation(QNdefRecord, lambda: Rituals.call(
        'ritual_ZN11QNdefRecordC1ERKS_NS_14TypeNameFormatERK10QByteArray',
        self._valueOf(other), typeNameFormat.value, self._valueOf(type),
    ))

  @overload(THIS, TypeNameFormat)
  def __init__(
      self,
      other: QNdefRecord,
      typeNameFormat: TypeNameFormat,
  ) -> None:
    """
    Notes what was given, for Qt's 'QNdefRecord::QNdefRecord(const
    QNdefRecord &other, TypeNameFormat typeNameFormat)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#QNdefRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.

    typeNameFormat : TypeNameFormat
      Passed on as its number.
    """
    #  QNdefRecord::QNdefRecord(const QNdefRecord &other, TypeNameFormat
    #      typeNameFormat)
    self._noteCreation(QNdefRecord, lambda: Rituals.call(
        'ritual_ZN11QNdefRecordC1ERKS_NS_14TypeNameFormatE',
        self._valueOf(other), typeNameFormat.value,
    ))

  @overload(TypeNameFormat, QByteArray)
  def __init__(
      self,
      typeNameFormat: TypeNameFormat,
      type: QByteArray,
  ) -> None:
    """
    Notes what was given, for Qt's 'QNdefRecord::QNdefRecord(TypeNameFormat
    typeNameFormat, const QByteArray &type)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#QNdefRecord

    Parameters
    ----------

    typeNameFormat : TypeNameFormat
      Passed on as its number.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QNdefRecord::QNdefRecord(TypeNameFormat typeNameFormat, const
    #      QByteArray &type)
    self._noteCreation(QNdefRecord, lambda: Rituals.call(
        'ritual_ZN11QNdefRecordC1ENS_14TypeNameFormatERK10QByteArray',
        typeNameFormat.value, self._valueOf(type),
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
    Calls Qt's 'void QNdefRecord::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qndefrecord.html#clear
    """
    #  void QNdefRecord::clear()
    self.uglySide.call('ritual_ZN11QNdefRecord5clearEv')

  @staticmethod
  def isRecordType(*__, **_) -> Never:
    """
    Qt's 'QNdefRecord::isRecordType': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QNdefRecord.isRecordType' has no cute function yet. Qt's "
        "'QNdefRecord::isRecordType': a template: a pattern and no single "
        "function.")


#  Qt's 'QList<QNdefRecord>': the list of QNdefRecord, which
#  'QList[QNdefRecord]' gives. It is made here, so that there is one as soon
#  as there can be a QNdefRecord.
QList.createKind(
    QNdefRecord, 'value',
    make='ritual_list_make_QNdefRecord',
    add='ritual_list_add_QNdefRecord',
    size='ritual_list_size_QNdefRecord',
    at='ritual_list_at_QNdefRecord',
    drop='ritual_list_drop_QNdefRecord',
)
