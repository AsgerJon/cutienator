"""
QHashedString binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qhashedstring_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QHashedString to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QString

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar
  from . import QHashedStringRef
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QHashedStringRef = WAIT['QHashedStringRef']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHashedString(QString):
  """
  The cute side of Qt's QHashedString: a plain Python object standing in
  front of one C++ QHashedString.

  It is built on the cute 'QString', as Qt's QHashedString is built on Qt's
  QString, and has everything that class has.

  C++ hands a QHashedString around as a copy, so every C++ QHashedString
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHashedString that has a ritual and that Python can
  call so far, 6 names in all: '__eq__', 'hash', 'existingHash', 'compare',
  'stringHash', 'computeHash'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHashedString &QHashedString::operator=(const QHashedString
    &string)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QHashedString::~QHashedString()': the destructor: Python removes
    its C++ QHashedString by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QHashedString is created at the first use, not by
    'QHashedString(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHashedString back gives a copy the ritual made for
    Python, in a new cute QHashedString.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QChar, str, int)
  @overload(QChar, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def compare(lhs: Optional[QChar], rhs: Optional[str], length: int) -> bool:
    """
    Calls Qt's 'bool QHashedString::compare(const QChar *lhs, const char
    *rhs, int length)'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#compare

    Parameters
    ----------

    lhs : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rhs : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is.
    """
    #  bool QHashedString::compare(const QChar *lhs, const char *rhs, int
    #      length)
    return Rituals.call(
        'ritual_ZN13QHashedString7compareEPK5QCharPKci',
        CuteMixin._addressOf(lhs), CuteMixin._bytesOf(rhs), length,
    )

  @staticmethod
  @overload(str, str, int)
  @overload(str, NoneType, int)
  def compare(lhs: Optional[str], rhs: Optional[str], length: int) -> bool:
    """
    Calls Qt's 'bool QHashedString::compare(const char *lhs, const char *rhs,
    int length)'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#compare

    Parameters
    ----------

    lhs : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    rhs : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is.
    """
    #  bool QHashedString::compare(const char *lhs, const char *rhs, int
    #      length)
    return Rituals.call(
        'ritual_ZN13QHashedString7compareEPKcS1_i',
        CuteMixin._bytesOf(lhs), CuteMixin._bytesOf(rhs), length,
    )

  @staticmethod
  @overload(QChar, int)
  @overload(NoneType, int)
  def stringHash(data: Optional[QChar], length: int) -> int:
    """
    Calls Qt's 'quint32 QHashedString::stringHash(const QChar *data, int
    length)'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#stringHash

    Parameters
    ----------

    data : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length : int
      Passed on as it is.
    """
    #  quint32 QHashedString::stringHash(const QChar *data, int length)
    return Rituals.call(
        'ritual_ZN13QHashedString10stringHashEPK5QChari',
        CuteMixin._addressOf(data), length,
    )

  @staticmethod
  @overload(str, int)
  def stringHash(data: Optional[str], length: int) -> int:
    """
    Calls Qt's 'quint32 QHashedString::stringHash(const char *data, int
    length)'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#stringHash

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is.
    """
    #  quint32 QHashedString::stringHash(const char *data, int length)
    return Rituals.call(
        'ritual_ZN13QHashedString10stringHashEPKci',
        CuteMixin._bytesOf(data), length,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHashedString'

  #  Qt's '~QHashedString()'. Naming it makes this a value class: Python owns
  #  every C++ QHashedString behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QHashedStringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hash(self) -> int:
    """
    Calls Qt's 'quint32 QHashedString::hash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#hash
    """
    #  quint32 QHashedString::hash() const
    return self.uglySide.call('ritual_ZNK13QHashedString4hashEv')

  def existingHash(self) -> int:
    """
    Calls Qt's 'quint32 QHashedString::existingHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#existingHash
    """
    #  quint32 QHashedString::existingHash() const
    return self.uglySide.call('ritual_ZNK13QHashedString12existingHashEv')

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
  def __eq__(self, string: QHashedString) -> bool:
    """
    Calls Qt's 'bool QHashedString::operator==(const QHashedString &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#operator==

    Parameters
    ----------

    string : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.
    """
    #  bool QHashedString::operator==(const QHashedString &string) const
    return self.uglySide.call(
        'ritual_ZNK13QHashedStringeqERKS_', self._valueOf(string),
    )

  @overload(QHashedStringRef)
  def __eq__(self, string: QHashedStringRef) -> bool:
    """
    Calls Qt's 'bool QHashedString::operator==(const QHashedStringRef
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#operator==

    Parameters
    ----------

    string : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.
    """
    #  bool QHashedString::operator==(const QHashedStringRef &string) const
    return self.uglySide.call(
        'ritual_ZNK13QHashedStringeqERK16QHashedStringRef',
        self._valueOf(string),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QHashedString::QHashedString()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#QHashedString
    """
    #  QHashedString::QHashedString()
    self._noteCreation(QHashedString, lambda: Rituals.call(
        'ritual_ZN13QHashedStringC1Ev',
    ))

  @overload(str)
  def __init__(self, string: str) -> None:
    """
    Notes what was given, for Qt's 'QHashedString::QHashedString(const
    QString &string)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#QHashedString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QHashedString::QHashedString(const QString &string)
    self._noteCreation(QHashedString, lambda: Rituals.call(
        'ritual_ZN13QHashedStringC1ERK7QString', string,
    ))

  @overload(str, int)
  def __init__(self, string: str, a1: int) -> None:
    """
    Notes what was given, for Qt's 'QHashedString::QHashedString(const
    QString &string, quint32 a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#QHashedString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    a1 : int
      Passed on as it is.
    """
    #  QHashedString::QHashedString(const QString &string, quint32 a1)
    self._noteCreation(QHashedString, lambda: Rituals.call(
        'ritual_ZN13QHashedStringC1ERK7QStringj', string, a1,
    ))

  @overload(THIS)
  def __init__(self, string: QHashedString) -> None:
    """
    Notes what was given, for Qt's 'QHashedString::QHashedString(const
    QHashedString &string)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#QHashedString

    Parameters
    ----------

    string : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.
    """
    #  QHashedString::QHashedString(const QHashedString &string)
    self._noteCreation(QHashedString, lambda: Rituals.call(
        'ritual_ZN13QHashedStringC1ERKS_', self._valueOf(string),
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

  def computeHash(self) -> None:
    """
    Calls Qt's 'void QHashedString::computeHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstring.html#computeHash
    """
    #  void QHashedString::computeHash() const
    self.uglySide.call('ritual_ZNK13QHashedString11computeHashEv')
