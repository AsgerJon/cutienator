"""
QMimeMagicRule binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimemagicrule_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeMagicRule to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMimeMagicRule(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeMagicRule: a plain Python object standing in
  front of one C++ QMimeMagicRule.

  C++ hands a QMimeMagicRule around as a copy, so every C++ QMimeMagicRule
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMimeMagicRule that has a ritual and that Python can
  call so far, 10 names in all: '__eq__', 'type', 'value', 'startPos',
  'endPos', 'mask', 'isValid', 'matches', 'matchSubstring', 'matchString'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMimeMagicRule::swap(QMimeMagicRule &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QMimeMagicRule::~QMimeMagicRule()': the destructor: Python removes
    its C++ QMimeMagicRule by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 a template.

  What to expect
  --------------

  - The C++ QMimeMagicRule is created at the first use, not by
    'QMimeMagicRule(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMimeMagicRule back gives a copy the ritual made for
    Python, in a new cute QMimeMagicRule.
  - Each name of Qt's QMimeMagicRule that has no cute function yet,
    '__init__', 'matchNumber', 'swap', 'typeName', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMimeMagicRule, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QMimeMagicRule::Type' of Qt, with the 9 names Qt gives in it.
    """

    Invalid = Kee[int](0)
    String = Kee[int](1)
    Host16 = Kee[int](2)
    Host32 = Kee[int](3)
    Big16 = Kee[int](4)
    Big32 = Kee[int](5)
    Little16 = Kee[int](6)
    Little32 = Kee[int](7)
    Byte = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, int, int, int, int, str, str)
  @overload(str, int, int, int, int, str, NoneType)
  @overload(str, int, int, int, int, NoneType, str)
  @overload(str, int, int, int, int, NoneType, NoneType)
  @overload(NoneType, int, int, int, int, str, str)
  @overload(NoneType, int, int, int, int, str, NoneType)
  @overload(NoneType, int, int, int, int, NoneType, str)
  @overload(NoneType, int, int, int, int, NoneType, NoneType)
  def matchSubstring(
      dataPtr: Optional[str],
      dataSize: int,
      rangeStart: int,
      rangeLength: int,
      valueLength: int,
      valueData: Optional[str],
      mask: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRule::matchSubstring(const char *dataPtr,
    qsizetype dataSize, quint64 rangeStart, quint64 rangeLength, quint64
    valueLength, const char *valueData, const char *mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#matchSubstring

    Parameters
    ----------

    dataPtr : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    dataSize : int
      Passed on as it is.

    rangeStart : int
      Passed on as it is.

    rangeLength : int
      Passed on as it is.

    valueLength : int
      Passed on as it is.

    valueData : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    mask : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QMimeMagicRule::matchSubstring(const char *dataPtr, qsizetype
    #      dataSize, quint64 rangeStart, quint64 rangeLength, quint64
    #      valueLength, const char *valueData, const char *mask)
    return Rituals.call(
        'ritual_ZN14QMimeMagicRule14matchSubstringEPKcxyyyS1_S1_',
        CuteMixin._bytesOf(dataPtr), dataSize, rangeStart, rangeLength,
        valueLength, CuteMixin._bytesOf(valueData), CuteMixin._bytesOf(mask),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeMagicRule'

  #  Qt's '~QMimeMagicRule()'. Naming it makes this a value class: Python
  #  owns every C++ QMimeMagicRule behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QMimeMagicRuleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def type(self) -> Type:
    """
    Calls Qt's 'Type QMimeMagicRule::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QMimeMagicRule::type() const
    return QMimeMagicRule.Type(self.uglySide.call(
        'ritual_ZNK14QMimeMagicRule4typeEv',
    ))

  @staticmethod
  @overload(QByteArray)
  def type(type: QByteArray) -> Type:
    """
    Calls Qt's 'Type QMimeMagicRule::type(const QByteArray &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#type

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QMimeMagicRule::type(const QByteArray &type)
    return QMimeMagicRule.Type(Rituals.call(
        'ritual_ZN14QMimeMagicRule4typeERK10QByteArray',
        CuteMixin._valueOf(type),
    ))

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMimeMagicRule::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMimeMagicRule::value() const
    address = self.uglySide.call('ritual_ZNK14QMimeMagicRule5valueEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def startPos(self) -> int:
    """
    Calls Qt's 'int QMimeMagicRule::startPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#startPos
    """
    #  int QMimeMagicRule::startPos() const
    return self.uglySide.call('ritual_ZNK14QMimeMagicRule8startPosEv')

  def endPos(self) -> int:
    """
    Calls Qt's 'int QMimeMagicRule::endPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#endPos
    """
    #  int QMimeMagicRule::endPos() const
    return self.uglySide.call('ritual_ZNK14QMimeMagicRule6endPosEv')

  def mask(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMimeMagicRule::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#mask

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMimeMagicRule::mask() const
    address = self.uglySide.call('ritual_ZNK14QMimeMagicRule4maskEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRule::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#isValid
    """
    #  bool QMimeMagicRule::isValid() const
    return self.uglySide.call('ritual_ZNK14QMimeMagicRule7isValidEv')

  @overload(QByteArray)
  def matches(self, data: QByteArray) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRule::matches(const QByteArray &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#matches

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QMimeMagicRule::matches(const QByteArray &data) const
    return self.uglySide.call(
        'ritual_ZNK14QMimeMagicRule7matchesERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray)
  def matchString(self, data: QByteArray) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRule::matchString(const QByteArray &data)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#matchString

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QMimeMagicRule::matchString(const QByteArray &data) const
    return self.uglySide.call(
        'ritual_ZNK14QMimeMagicRule11matchStringERK10QByteArray',
        self._valueOf(data),
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

  @overload(THIS)
  def __eq__(self, other: QMimeMagicRule) -> bool:
    """
    Calls Qt's 'bool QMimeMagicRule::operator==(const QMimeMagicRule &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimemagicrule.html#operator==

    Parameters
    ----------

    other : QMimeMagicRule
      Passed on as a value: Qt reads the C++ QMimeMagicRule, which stays
      Python's own.
    """
    #  bool QMimeMagicRule::operator==(const QMimeMagicRule &other) const
    return self.uglySide.call(
        'ritual_ZNK14QMimeMagicRuleeqERKS_', self._valueOf(other),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMimeMagicRule::QMimeMagicRule(const QString &typeStr, const
    QByteArray &value, const QString &offsets, const QByteArray &mask,
    QString *errorString)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'makePattern'.
    """
    raise NotImplementedError(
        "'QMimeMagicRule.__init__' has no cute function yet. Qt's "
        "'QMimeMagicRule::QMimeMagicRule(const QString &typeStr, const "
        "QByteArray &value, const QString &offsets, const QByteArray &mask, "
        "QString *errorString)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'makePattern'.")

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
  def matchNumber(*__, **_) -> Never:
    """
    Qt's 'QMimeMagicRule::matchNumber': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QMimeMagicRule.matchNumber' has no cute function yet. Qt's "
        "'QMimeMagicRule::matchNumber': a template: a pattern and no single "
        "function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMimeMagicRule::swap(QMimeMagicRule &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeMagicRule.swap' has no cute function yet. Qt's 'void "
        "QMimeMagicRule::swap(QMimeMagicRule &other)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def typeName(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMimeMagicRule::typeName(Type type)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'magicRuleTypes'.
    """
    raise NotImplementedError(
        "'QMimeMagicRule.typeName' has no cute function yet. Qt's "
        "'QByteArray QMimeMagicRule::typeName(Type type)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'magicRuleTypes'.")


#  Qt's 'QList<QMimeMagicRule>': the list of QMimeMagicRule, which
#  'QList[QMimeMagicRule]' gives. It is made here, so that there is one as
#  soon as there can be a QMimeMagicRule.
QList.createKind(
    QMimeMagicRule, 'value',
    make='ritual_list_make_QMimeMagicRule',
    add='ritual_list_add_QMimeMagicRule',
    size='ritual_list_size_QMimeMagicRule',
    at='ritual_list_at_QMimeMagicRule',
    drop='ritual_list_drop_QMimeMagicRule',
)
