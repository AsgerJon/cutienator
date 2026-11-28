"""
QVoice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTextToSpeech/qvoice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QVariant = WAIT['QVariant']


class QVoice(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVoice: a plain Python object standing in front of
  one C++ QVoice.

  C++ hands a QVoice around as a copy, so every C++ QVoice behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVoice that has a ritual and that Python can call so
  far, 12 names in all: '__eq__', '__ne__', 'name', 'locale', 'gender',
  'age', 'language', 'genderName', 'ageName', 'isEqual', 'data',
  '__rlshift__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVoice::~QVoice()': the destructor: Python removes its C++ QVoice
    by it, and has no other use for it.
  - Qt's 'QVoice &QVoice::operator=(const QVoice &other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QVoice::QVoice(QVoice &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QVoice &QVoice::operator=(QVoice &&other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'void QVoice::swap(QVoice &other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &str, const QVoice &voice)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &str, QVoice &voice)': an
    operator between other classes, written inside this one.
  - Qt's 'QDataStream &QVoice::writeTo(QDataStream &a0) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDataStream &QVoice::readFrom(QDataStream &a0)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 27 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QVoice is created at the first use, not by 'QVoice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVoice back gives a copy the ritual made for Python,
    in a new cute QVoice.
  - Each name of Qt's QVoice that has no cute function yet, 'readFrom',
    'swap', 'writeTo', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QVoice, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Age(CuteNum):
    """The enum 'QVoice::Age' of Qt, with the 5 names Qt gives in it."""

    Child = Kee[int](0)
    Teenager = Kee[int](1)
    Adult = Kee[int](2)
    Senior = Kee[int](3)
    Other = Kee[int](4)

  class Gender(CuteNum):
    """The enum 'QVoice::Gender' of Qt, with the 3 names Qt gives in it."""

    Male = Kee[int](0)
    Female = Kee[int](1)
    Unknown = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Gender)
  def genderName(gender: Gender) -> str:
    """
    Calls Qt's 'QString QVoice::genderName(QVoice::Gender gender)'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#genderName

    Parameters
    ----------

    gender : Gender
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVoice::genderName(QVoice::Gender gender)
    return Rituals.call(
        'ritual_ZN6QVoice10genderNameENS_6GenderE', gender.value,
    )

  @staticmethod
  @overload(Age)
  def ageName(age: Age) -> str:
    """
    Calls Qt's 'QString QVoice::ageName(QVoice::Age age)'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#ageName

    Parameters
    ----------

    age : Age
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVoice::ageName(QVoice::Age age)
    return Rituals.call('ritual_ZN6QVoice7ageNameENS_3AgeE', age.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVoice'

  #  Qt's '~QVoice()'. Naming it makes this a value class: Python owns every
  #  C++ QVoice behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QVoiceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QVoice::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVoice::name() const
    return self.uglySide.call('ritual_ZNK6QVoice4nameEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QVoice::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QVoice::locale() const
    address = self.uglySide.call('ritual_ZNK6QVoice6localeEv')
    return QLocale._cuteOwning(address)

  def gender(self) -> Gender:
    """
    Calls Qt's 'Gender QVoice::gender() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#gender

    Returns
    -------

    Gender
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Gender(number)' gives.
    """
    #  Gender QVoice::gender() const
    return QVoice.Gender(self.uglySide.call('ritual_ZNK6QVoice6genderEv'))

  def age(self) -> Age:
    """
    Calls Qt's 'Age QVoice::age() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#age

    Returns
    -------

    Age
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Age(number)' gives.
    """
    #  Age QVoice::age() const
    return QVoice.Age(self.uglySide.call('ritual_ZNK6QVoice3ageEv'))

  def language(self) -> QLocale.Language:
    """
    Calls Qt's 'QLocale::Language QVoice::language() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#language

    Returns
    -------

    QLocale.Language
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QLocale.Language(number)'
      gives.
    """
    #  QLocale::Language QVoice::language() const
    return QLocale.Language(self.uglySide.call(
        'ritual_ZNK6QVoice8languageEv',
    ))

  @overload(THIS)
  def isEqual(self, other: QVoice) -> bool:
    """
    Calls Qt's 'bool QVoice::isEqual(const QVoice &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#isEqual

    Parameters
    ----------

    other : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  bool QVoice::isEqual(const QVoice &other) const
    return self.uglySide.call(
        'ritual_ZNK6QVoice7isEqualERKS_', self._valueOf(other),
    )

  def data(self) -> QVariant:
    """
    Calls Qt's 'QVariant QVoice::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#data

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVoice::data() const
    address = self.uglySide.call('ritual_ZNK6QVoice4dataEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
  def __eq__(self, rhs: QVoice) -> bool:
    """
    Calls Qt's 'bool operator==(const QVoice &lhs, const QVoice &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#operator==

    Parameters
    ----------

    rhs : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  bool operator==(const QVoice &lhs, const QVoice &rhs)
    return Rituals.call(
        'ritual_ZeqRK6QVoiceS1_',
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
  def __ne__(self, rhs: QVoice) -> bool:
    """
    Calls Qt's 'bool operator!=(const QVoice &lhs, const QVoice &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#operator!=

    Parameters
    ----------

    rhs : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  bool operator!=(const QVoice &lhs, const QVoice &rhs)
    return Rituals.call(
        'ritual_ZneRK6QVoiceS1_',
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

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QVoice &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#operator<<

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
    #  QDebug operator<<(QDebug a0, const QVoice &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK6QVoice',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QVoice::QVoice()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#QVoice
    """
    #  QVoice::QVoice()
    self._noteCreation(QVoice, lambda: Rituals.call('ritual_ZN6QVoiceC1Ev'))

  @overload(THIS)
  def __init__(self, other: QVoice) -> None:
    """
    Notes what was given, for Qt's 'QVoice::QVoice(const QVoice &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#QVoice

    Parameters
    ----------

    other : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  QVoice::QVoice(const QVoice &other)
    self._noteCreation(QVoice, lambda: Rituals.call(
        'ritual_ZN6QVoiceC1ERKS_', self._valueOf(other),
    ))

  @overload(str, QLocale, Gender, Age, QVariant)
  def __init__(
      self,
      name: str,
      loc: QLocale,
      gender: Gender,
      age: Age,
      data: QVariant,
  ) -> None:
    """
    Notes what was given, for Qt's 'QVoice::QVoice(const QString &name, const
    QLocale &loc, Gender gender, Age age, const QVariant &data)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvoice.html#QVoice

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    loc : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    gender : Gender
      Passed on as its number.

    age : Age
      Passed on as its number.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QVoice::QVoice(const QString &name, const QLocale &loc, Gender gender,
    #      Age age, const QVariant &data)
    self._noteCreation(QVoice, lambda: Rituals.call(
        'ritual_ZN6QVoiceC1ERK7QStringRK7QLocaleNS_6GenderENS_3AgeERK8QVari'
        'ant',
        name, self._valueOf(loc), gender.value, age.value,
        self._valueOf(data),
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
  def readFrom(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QVoice::readFrom(QDataStream &a0)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVoice.readFrom' has no cute function yet. Qt's 'QDataStream "
        "&QVoice::readFrom(QDataStream &a0)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QVoice::swap(QVoice &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QVoice.swap' has no cute function yet. Qt's 'void "
        "QVoice::swap(QVoice &other)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def writeTo(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QVoice::writeTo(QDataStream &a0) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVoice.writeTo' has no cute function yet. Qt's 'QDataStream "
        "&QVoice::writeTo(QDataStream &a0) const': takes a type Python has "
        "no way to hand over yet.")


#  Qt's 'QList<QVoice>': the list of QVoice, which 'QList[QVoice]' gives. It
#  is made here, so that there is one as soon as there can be a QVoice.
QList.createKind(
    QVoice, 'value',
    make='ritual_list_make_QVoice',
    add='ritual_list_add_QVoice',
    size='ritual_list_size_QVoice',
    at='ritual_list_at_QVoice',
    drop='ritual_list_drop_QVoice',
)
