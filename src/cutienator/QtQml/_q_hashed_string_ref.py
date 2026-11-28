"""
QHashedStringRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qhashedstring_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QHashedStringRef to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar
  from . import QHashedCStringRef, QHashedString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QHashedCStringRef = WAIT['QHashedCStringRef']
  QHashedString = WAIT['QHashedString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHashedStringRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHashedStringRef: a plain Python object standing in
  front of one C++ QHashedStringRef.

  C++ hands a QHashedStringRef around as a copy, so every C++
  QHashedStringRef behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHashedStringRef that has a ritual and that Python
  can call so far, 17 names in all: '__eq__', '__ne__', 'hash', 'data', 'at',
  'constData', 'startsWith', 'endsWith', 'indexOf', 'mid', 'split',
  'isEmpty', 'length', 'startsWithUpper', 'toString', 'isLatin1',
  'computeHash'. It can be made from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHashedStringRef::QHashedStringRef(QStringView a0)': takes in
    Python what 'QHashedStringRef::QHashedStringRef(const QString &a0)'
    takes.
  - Qt's 'QHashedStringRef &QHashedStringRef::operator=(const
    QHashedStringRef &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QHashedStringRef::~QHashedStringRef()': the destructor: Python
    removes its C++ QHashedStringRef by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QHashedStringRef is created at the first use, not by
    'QHashedStringRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHashedStringRef back gives a copy the ritual made
    for Python, in a new cute QHashedStringRef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHashedStringRef'

  #  Qt's '~QHashedStringRef()'. Naming it makes this a value class: Python
  #  owns every C++ QHashedStringRef behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QHashedStringRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hash(self) -> int:
    """
    Calls Qt's 'quint32 QHashedStringRef::hash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#hash
    """
    #  quint32 QHashedStringRef::hash() const
    return self.uglySide.call('ritual_ZNK16QHashedStringRef4hashEv')

  @overload(int)
  def at(self, a0: int) -> QChar:
    """
    Calls Qt's 'const QChar &QHashedStringRef::at(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#at

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  const QChar &QHashedStringRef::at(int a0) const
    address = self.uglySide.call('ritual_ZNK16QHashedStringRef2atEi', a0)
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  def constData(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QHashedStringRef::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#constData

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QHashedStringRef::constData() const
    address = self.uglySide.call('ritual_ZNK16QHashedStringRef9constDataEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  @overload(str)
  def startsWith(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::startsWith(const QString &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#startsWith

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHashedStringRef::startsWith(const QString &a0) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRef10startsWithERK7QString', a0,
    )

  @overload(str)
  def endsWith(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::endsWith(const QString &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#endsWith

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHashedStringRef::endsWith(const QString &a0) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRef8endsWithERK7QString', a0,
    )

  @overload(QChar)
  @overload(QChar, int)
  def indexOf(self, a0: QChar, from_: int = 0) -> int:
    """
    Calls Qt's 'int QHashedStringRef::indexOf(const QChar &a0, int from)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#indexOf

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QHashedStringRef::indexOf(const QChar &a0, int from) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRef7indexOfERK5QChari',
        self._valueOf(a0), from_,
    )

  @overload(int, int)
  def mid(self, a0: int, a1: int) -> QHashedStringRef:
    """
    Calls Qt's 'QHashedStringRef QHashedStringRef::mid(int a0, int a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#mid

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    Returns
    -------

    QHashedStringRef
      A new cute QHashedStringRef around the copy Qt gave back. Python owns
      it.
    """
    #  QHashedStringRef QHashedStringRef::mid(int a0, int a1) const
    address = self.uglySide.call(
        'ritual_ZNK16QHashedStringRef3midEii', a0, a1,
    )
    return QHashedStringRef._cuteOwning(address)

  @overload(QChar)
  def split(self, sep: QChar) -> QList[QHashedStringRef]:
    """
    Calls Qt's 'QList<QHashedStringRef> QHashedStringRef::split(const QChar
    sep) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#split

    Parameters
    ----------

    sep : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    QList[QHashedStringRef]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHashedStringRef> QHashedStringRef::split(const QChar sep) const
    address = self.uglySide.call(
        'ritual_ZNK16QHashedStringRef5splitE5QChar', self._valueOf(sep),
    )
    return QList[QHashedStringRef]._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#isEmpty
    """
    #  bool QHashedStringRef::isEmpty() const
    return self.uglySide.call('ritual_ZNK16QHashedStringRef7isEmptyEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QHashedStringRef::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#length
    """
    #  int QHashedStringRef::length() const
    return self.uglySide.call('ritual_ZNK16QHashedStringRef6lengthEv')

  def startsWithUpper(self) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::startsWithUpper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#startsWithUpper
    """
    #  bool QHashedStringRef::startsWithUpper() const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRef15startsWithUpperEv',
    )

  def toString(self) -> str:
    """
    Calls Qt's 'QString QHashedStringRef::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHashedStringRef::toString() const
    return self.uglySide.call('ritual_ZNK16QHashedStringRef8toStringEv')

  def isLatin1(self) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::isLatin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#isLatin1
    """
    #  bool QHashedStringRef::isLatin1() const
    return self.uglySide.call('ritual_ZNK16QHashedStringRef8isLatin1Ev')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __eq__(self, string: str) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator==(const QString &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator==

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHashedStringRef::operator==(const QString &string) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefeqERK7QString', string,
    )

  @overload(QHashedString)
  def __eq__(self, string: QHashedString) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator==(const QHashedString
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator==

    Parameters
    ----------

    string : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.
    """
    #  bool QHashedStringRef::operator==(const QHashedString &string) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefeqERK13QHashedString',
        self._valueOf(string),
    )

  @overload(THIS)
  def __eq__(self, string: QHashedStringRef) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator==(const QHashedStringRef
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator==

    Parameters
    ----------

    string : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.
    """
    #  bool QHashedStringRef::operator==(const QHashedStringRef &string)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefeqERKS_', self._valueOf(string),
    )

  @overload(QHashedCStringRef)
  def __eq__(self, string: QHashedCStringRef) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator==(const QHashedCStringRef
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator==

    Parameters
    ----------

    string : QHashedCStringRef
      Passed on as a value: Qt reads the C++ QHashedCStringRef, which stays
      Python's own.
    """
    #  bool QHashedStringRef::operator==(const QHashedCStringRef &string)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefeqERK17QHashedCStringRef',
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

  @overload(str)
  def __ne__(self, string: str) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator!=(const QString &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator!=

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHashedStringRef::operator!=(const QString &string) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefneERK7QString', string,
    )

  @overload(QHashedString)
  def __ne__(self, string: QHashedString) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator!=(const QHashedString
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator!=

    Parameters
    ----------

    string : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.
    """
    #  bool QHashedStringRef::operator!=(const QHashedString &string) const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefneERK13QHashedString',
        self._valueOf(string),
    )

  @overload(THIS)
  def __ne__(self, string: QHashedStringRef) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator!=(const QHashedStringRef
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator!=

    Parameters
    ----------

    string : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.
    """
    #  bool QHashedStringRef::operator!=(const QHashedStringRef &string)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefneERKS_', self._valueOf(string),
    )

  @overload(QHashedCStringRef)
  def __ne__(self, string: QHashedCStringRef) -> bool:
    """
    Calls Qt's 'bool QHashedStringRef::operator!=(const QHashedCStringRef
    &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#operator!=

    Parameters
    ----------

    string : QHashedCStringRef
      Passed on as a value: Qt reads the C++ QHashedCStringRef, which stays
      Python's own.
    """
    #  bool QHashedStringRef::operator!=(const QHashedCStringRef &string)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QHashedStringRefneERK17QHashedCStringRef',
        self._valueOf(string),
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
    Notes what was given, for Qt's 'QHashedStringRef::QHashedStringRef()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#QHashedStringRef
    """
    #  QHashedStringRef::QHashedStringRef()
    self._noteCreation(QHashedStringRef, lambda: Rituals.call(
        'ritual_ZN16QHashedStringRefC1Ev',
    ))

  @overload(str)
  def __init__(self, a0: str) -> None:
    """
    Notes what was given, for Qt's 'QHashedStringRef::QHashedStringRef(const
    QString &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#QHashedStringRef

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QHashedStringRef::QHashedStringRef(const QString &a0)
    self._noteCreation(QHashedStringRef, lambda: Rituals.call(
        'ritual_ZN16QHashedStringRefC1ERK7QString', a0,
    ))

  @overload(QChar, int)
  @overload(NoneType, int)
  def __init__(self, a0: Optional[QChar], a1: int) -> None:
    """
    Notes what was given, for Qt's 'QHashedStringRef::QHashedStringRef(const
    QChar *a0, int a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#QHashedStringRef

    Parameters
    ----------

    a0 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  QHashedStringRef::QHashedStringRef(const QChar *a0, int a1)
    self._noteCreation(QHashedStringRef, lambda: Rituals.call(
        'ritual_ZN16QHashedStringRefC1EPK5QChari', self._addressOf(a0), a1,
    ))

  @overload(QChar, int, int)
  @overload(NoneType, int, int)
  def __init__(self, a0: Optional[QChar], a1: int, a2: int) -> None:
    """
    Notes what was given, for Qt's 'QHashedStringRef::QHashedStringRef(const
    QChar *a0, int a1, quint32 a2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#QHashedStringRef

    Parameters
    ----------

    a0 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  QHashedStringRef::QHashedStringRef(const QChar *a0, int a1, quint32
    #      a2)
    self._noteCreation(QHashedStringRef, lambda: Rituals.call(
        'ritual_ZN16QHashedStringRefC1EPK5QCharij',
        self._addressOf(a0), a1, a2,
    ))

  @overload(QHashedString)
  def __init__(self, a0: QHashedString) -> None:
    """
    Notes what was given, for Qt's 'QHashedStringRef::QHashedStringRef(const
    QHashedString &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#QHashedStringRef

    Parameters
    ----------

    a0 : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.
    """
    #  QHashedStringRef::QHashedStringRef(const QHashedString &a0)
    self._noteCreation(QHashedStringRef, lambda: Rituals.call(
        'ritual_ZN16QHashedStringRefC1ERK13QHashedString', self._valueOf(a0),
    ))

  @overload(THIS)
  def __init__(self, a0: QHashedStringRef) -> None:
    """
    Notes what was given, for Qt's 'QHashedStringRef::QHashedStringRef(const
    QHashedStringRef &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedstringref.html#QHashedStringRef

    Parameters
    ----------

    a0 : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.
    """
    #  QHashedStringRef::QHashedStringRef(const QHashedStringRef &a0)
    self._noteCreation(QHashedStringRef, lambda: Rituals.call(
        'ritual_ZN16QHashedStringRefC1ERKS_', self._valueOf(a0),
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

  def data(self) -> Optional[QChar]:
    """
    Calls Qt's 'QChar *QHashedStringRef::data()'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#data

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChar *QHashedStringRef::data()
    address = self.uglySide.call('ritual_ZN16QHashedStringRef4dataEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def computeHash(self) -> None:
    """
    Calls Qt's 'void QHashedStringRef::computeHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedstringref.html#computeHash
    """
    #  void QHashedStringRef::computeHash() const
    self.uglySide.call('ritual_ZNK16QHashedStringRef11computeHashEv')


#  Qt's 'QList<QHashedStringRef>': the list of QHashedStringRef, which
#  'QList[QHashedStringRef]' gives. It is made here, so that there is one as
#  soon as there can be a QHashedStringRef.
QList.createKind(
    QHashedStringRef, 'value',
    make='ritual_list_make_QHashedStringRef',
    add='ritual_list_add_QHashedStringRef',
    size='ritual_list_size_QHashedStringRef',
    at='ritual_list_at_QHashedStringRef',
    drop='ritual_list_drop_QHashedStringRef',
)
