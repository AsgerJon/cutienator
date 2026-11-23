"""
QJsonDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsondocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QDebug, QJsonArray, QJsonObject, QJsonParseError
  from . import QJsonValue, QLatin1String, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']
  QJsonParseError = WAIT['QJsonParseError']
  QLatin1String = WAIT['QLatin1String']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJsonDocument(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonDocument: a plain Python object standing in
  front of one C++ QJsonDocument.

  C++ hands a QJsonDocument around as a copy, so every C++ QJsonDocument
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonDocument that has a ritual and that Python can
  call so far, 16 names in all: 'fromVariant', 'toVariant', 'fromJson',
  'toJson', 'isEmpty', 'isArray', 'isObject', 'object', 'array', 'setObject',
  'setArray', '__getitem__', 'isNull', '__rlshift__', '__eq__', '__ne__'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonDocument::~QJsonDocument()': the destructor: Python removes
    its C++ QJsonDocument by it, and has no other use for it.
  - Qt's 'const QJsonValue QJsonDocument::operator[](QStringView key) const':
    takes in Python what 'const QJsonValue QJsonDocument::operator[](const
    QString &key) const' takes.

  What has no ritual
  ------------------

  7 of the 31 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QJsonDocument is created at the first use, not by
    'QJsonDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonDocument back gives a copy the ritual made for
    Python, in a new cute QJsonDocument.
  """

  #  The enums Qt writes inside QJsonDocument, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class JsonFormat(CuteNum):
    """
    The enum 'QJsonDocument::JsonFormat' of Qt, with the 2 names Qt gives in
    it.
    """

    Indented = Kee[int](0)
    Compact = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant)
  def fromVariant(variant: QVariant) -> QJsonDocument:
    """
    Calls Qt's 'QJsonDocument QJsonDocument::fromVariant(const QVariant
    &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#fromVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QJsonDocument
      A new cute QJsonDocument around the copy Qt gave back. Python owns it.
    """
    #  QJsonDocument QJsonDocument::fromVariant(const QVariant &variant)
    address = Rituals.call(
        'ritual_ZN13QJsonDocument11fromVariantERK8QVariant',
        CuteMixin._valueOf(variant),
    )
    return QJsonDocument._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  @overload(QByteArray, QJsonParseError)
  @overload(QByteArray, NoneType)
  def fromJson(
      json: QByteArray,
      error: Optional[QJsonParseError] = None,
  ) -> QJsonDocument:
    """
    Calls Qt's 'QJsonDocument QJsonDocument::fromJson(const QByteArray &json,
    QJsonParseError *error)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#fromJson

    Parameters
    ----------

    json : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    error : Optional[QJsonParseError]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QJsonDocument
      A new cute QJsonDocument around the copy Qt gave back. Python owns it.
    """
    #  QJsonDocument QJsonDocument::fromJson(const QByteArray &json,
    #      QJsonParseError *error)
    address = Rituals.call(
        'ritual_ZN13QJsonDocument8fromJsonERK10QByteArrayP15QJsonParseError',
        CuteMixin._valueOf(json), CuteMixin._addressOf(error),
    )
    return QJsonDocument._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonDocument'

  #  Qt's '~QJsonDocument()'. Naming it makes this a value class: Python owns
  #  every C++ QJsonDocument behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QJsonDocumentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QJsonDocument::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJsonDocument::toVariant() const
    address = self.uglySide.call('ritual_ZNK13QJsonDocument9toVariantEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(JsonFormat)
  def toJson(self, format: JsonFormat = JsonFormat.Indented) -> QByteArray:
    """
    Calls Qt's 'QByteArray QJsonDocument::toJson(JsonFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#toJson

    Parameters
    ----------

    format : JsonFormat
      Passed on as its number. May be left out, as in Qt: it is then
      JsonFormat.Indented.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QJsonDocument::toJson(JsonFormat format) const
    address = self.uglySide.call(
        'ritual_ZNK13QJsonDocument6toJsonENS_10JsonFormatE', format.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QJsonDocument::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#isEmpty
    """
    #  bool QJsonDocument::isEmpty() const
    return self.uglySide.call('ritual_ZNK13QJsonDocument7isEmptyEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QJsonDocument::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#isArray
    """
    #  bool QJsonDocument::isArray() const
    return self.uglySide.call('ritual_ZNK13QJsonDocument7isArrayEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QJsonDocument::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#isObject
    """
    #  bool QJsonDocument::isObject() const
    return self.uglySide.call('ritual_ZNK13QJsonDocument8isObjectEv')

  def object(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonDocument::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#object

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonDocument::object() const
    address = self.uglySide.call('ritual_ZNK13QJsonDocument6objectEv')
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

  def array(self) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonDocument::array() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#array

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonDocument::array() const
    address = self.uglySide.call('ritual_ZNK13QJsonDocument5arrayEv')
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QJsonDocument::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#isNull
    """
    #  bool QJsonDocument::isNull() const
    return self.uglySide.call('ritual_ZNK13QJsonDocument6isNullEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QJsonObject)
  def setObject(self, object: QJsonObject) -> None:
    """
    Calls Qt's 'void QJsonDocument::setObject(const QJsonObject &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#setObject

    Parameters
    ----------

    object : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QJsonDocument::setObject(const QJsonObject &object)
    self.uglySide.call(
        'ritual_ZN13QJsonDocument9setObjectERK11QJsonObject',
        self._valueOf(object),
    )

  @overload(QJsonArray)
  def setArray(self, array: QJsonArray) -> None:
    """
    Calls Qt's 'void QJsonDocument::setArray(const QJsonArray &array)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#setArray

    Parameters
    ----------

    array : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  void QJsonDocument::setArray(const QJsonArray &array)
    self.uglySide.call(
        'ritual_ZN13QJsonDocument8setArrayERK10QJsonArray',
        self._valueOf(array),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __getitem__(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonDocument::operator[](const QString
    &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonDocument::operator[](const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK13QJsonDocumentixERK7QString', key,
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonDocument::operator[](QLatin1StringView
    key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#operator[]

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonDocument::operator[](QLatin1StringView key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QJsonDocumentixE13QLatin1String', self._valueOf(key),
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(int)
  def __getitem__(self, i: int) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonDocument::operator[](qsizetype i)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonDocument::operator[](qsizetype i) const
    address = self.uglySide.call('ritual_ZNK13QJsonDocumentixEx', i)
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QJsonDocument &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QJsonDocument &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK13QJsonDocument',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from . import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QJsonDocument) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonDocument &lhs, const QJsonDocument
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#operator==

    Parameters
    ----------

    rhs : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.
    """
    #  bool operator==(const QJsonDocument &lhs, const QJsonDocument &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QJsonDocumentS1_',
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
  def __ne__(self, rhs: QJsonDocument) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonDocument &lhs, const QJsonDocument
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#operator!=

    Parameters
    ----------

    rhs : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.
    """
    #  bool operator!=(const QJsonDocument &lhs, const QJsonDocument &rhs)
    return Rituals.call(
        'ritual_ZneRK13QJsonDocumentS1_',
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
    Notes what was given, for Qt's 'QJsonDocument::QJsonDocument()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#QJsonDocument
    """
    #  QJsonDocument::QJsonDocument()
    self._noteCreation(QJsonDocument, lambda: Rituals.call(
        'ritual_ZN13QJsonDocumentC1Ev',
    ))

  @overload(QJsonObject)
  def __init__(self, object: QJsonObject) -> None:
    """
    Notes what was given, for Qt's 'QJsonDocument::QJsonDocument(const
    QJsonObject &object)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#QJsonDocument

    Parameters
    ----------

    object : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  QJsonDocument::QJsonDocument(const QJsonObject &object)
    self._noteCreation(QJsonDocument, lambda: Rituals.call(
        'ritual_ZN13QJsonDocumentC1ERK11QJsonObject', self._valueOf(object),
    ))

  @overload(QJsonArray)
  def __init__(self, array: QJsonArray) -> None:
    """
    Notes what was given, for Qt's 'QJsonDocument::QJsonDocument(const
    QJsonArray &array)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#QJsonDocument

    Parameters
    ----------

    array : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  QJsonDocument::QJsonDocument(const QJsonArray &array)
    self._noteCreation(QJsonDocument, lambda: Rituals.call(
        'ritual_ZN13QJsonDocumentC1ERK10QJsonArray', self._valueOf(array),
    ))

  @overload(THIS)
  def __init__(self, other: QJsonDocument) -> None:
    """
    Notes what was given, for Qt's 'QJsonDocument::QJsonDocument(const
    QJsonDocument &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsondocument.html#QJsonDocument

    Parameters
    ----------

    other : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.
    """
    #  QJsonDocument::QJsonDocument(const QJsonDocument &other)
    self._noteCreation(QJsonDocument, lambda: Rituals.call(
        'ritual_ZN13QJsonDocumentC1ERKS_', self._valueOf(other),
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
