"""
QStringHashBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QStringHashBase to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String
  from . import QHashedCStringRef, QHashedString, QHashedStringRef
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedCStringRef = WAIT['QHashedCStringRef']
  QHashedString = WAIT['QHashedString']
  QHashedStringRef = WAIT['QHashedStringRef']
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringHashBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringHashBase: a plain Python object standing in
  front of one C++ QStringHashBase.

  C++ hands a QStringHashBase around as a copy, so every C++ QStringHashBase
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStringHashBase that has a ritual and that Python
  can call so far, 2 names in all: 'toQString', 'hashOf'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HashedForm<QString>::Type QStringHashBase::hashedString(const
    QString &s)': gives a type Python has no way to take yet.
  - Qt's 'HashedForm<QStringView>::Type
    QStringHashBase::hashedString(QStringView s)': gives a type Python has no
    way to take yet.
  - Qt's 'HashedForm<QV4::String *>::Type
    QStringHashBase::hashedString(QV4::String *s)': gives a type Python has
    no way to take yet.
  - Qt's 'HashedForm<const QV4::String *>::Type
    QStringHashBase::hashedString(const QV4::String *s)': gives a type Python
    has no way to take yet.
  - Qt's 'HashedForm<QLatin1StringView>::Type
    QStringHashBase::hashedString(QLatin1StringView s)': gives a type Python
    has no way to take yet.
  - Qt's 'quint32 QStringHashBase::hashOf(const QV4::String *s)': takes in
    Python what 'quint32 QStringHashBase::hashOf(QV4::String *s)' takes.
  - Qt's 'QStringHashBase::~QStringHashBase()': the destructor: Python
    removes its C++ QStringHashBase by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 3 the compiler refuses its ritual as it
  would be written here; 1 a template.

  What to expect
  --------------

  - The C++ QStringHashBase is created at the first use, not by
    'QStringHashBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStringHashBase back gives a copy the ritual made for
    Python, in a new cute QStringHashBase.
  - Each name of Qt's QStringHashBase that has no cute function yet,
    'hashedString', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def toQString(s: str) -> str:
    """
    Calls Qt's 'const QString &QStringHashBase::toQString(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#toQString

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QStringHashBase::toQString(const QString &s)
    return Rituals.call('ritual_ZN15QStringHashBase9toQStringERK7QString', s)

  @staticmethod
  @overload(QHashedString)
  def toQString(s: QHashedString) -> str:
    """
    Calls Qt's 'const QString &QStringHashBase::toQString(const QHashedString
    &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#toQString

    Parameters
    ----------

    s : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QStringHashBase::toQString(const QHashedString &s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase9toQStringERK13QHashedString',
        CuteMixin._valueOf(s),
    )

  @staticmethod
  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def toQString(s: Optional[QV4.String]) -> str:
    """
    Calls Qt's 'QString QStringHashBase::toQString(const QV4::String *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#toQString

    Parameters
    ----------

    s : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringHashBase::toQString(const QV4::String *s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase9toQStringEPKN3QV46StringE',
        CuteMixin._addressOf(s),
    )

  @staticmethod
  @overload(QHashedStringRef)
  def toQString(s: QHashedStringRef) -> str:
    """
    Calls Qt's 'QString QStringHashBase::toQString(const QHashedStringRef
    &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#toQString

    Parameters
    ----------

    s : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringHashBase::toQString(const QHashedStringRef &s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase9toQStringERK16QHashedStringRef',
        CuteMixin._valueOf(s),
    )

  @staticmethod
  @overload(QLatin1String)
  def toQString(s: QLatin1String) -> str:
    """
    Calls Qt's 'QString QStringHashBase::toQString(const QLatin1String &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#toQString

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringHashBase::toQString(const QLatin1String &s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase9toQStringERK13QLatin1String',
        CuteMixin._valueOf(s),
    )

  @staticmethod
  @overload(QHashedCStringRef)
  def toQString(s: QHashedCStringRef) -> str:
    """
    Calls Qt's 'QString QStringHashBase::toQString(const QHashedCStringRef
    &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#toQString

    Parameters
    ----------

    s : QHashedCStringRef
      Passed on as a value: Qt reads the C++ QHashedCStringRef, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringHashBase::toQString(const QHashedCStringRef &s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase9toQStringERK17QHashedCStringRef',
        CuteMixin._valueOf(s),
    )

  @staticmethod
  @overload(QHashedStringRef)
  def hashOf(s: QHashedStringRef) -> int:
    """
    Calls Qt's 'quint32 QStringHashBase::hashOf(const QHashedStringRef &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#hashOf

    Parameters
    ----------

    s : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.
    """
    #  quint32 QStringHashBase::hashOf(const QHashedStringRef &s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase6hashOfERK16QHashedStringRef',
        CuteMixin._valueOf(s),
    )

  @staticmethod
  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def hashOf(s: Optional[QV4.String]) -> int:
    """
    Calls Qt's 'quint32 QStringHashBase::hashOf(QV4::String *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashbase.html#hashOf

    Parameters
    ----------

    s : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  quint32 QStringHashBase::hashOf(QV4::String *s)
    return Rituals.call(
        'ritual_ZN15QStringHashBase6hashOfEPN3QV46StringE',
        CuteMixin._addressOf(s),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringHashBase'

  #  Qt's '~QStringHashBase()'. Naming it makes this a value class: Python
  #  owns every C++ QStringHashBase behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QStringHashBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def hashedString(*__, **_) -> Never:
    """
    - Qt's 'HashedForm<QString>::Type QStringHashBase::hashedString(const
      QString &s)': gives a type Python has no way to take yet.
    - Qt's 'HashedForm<QStringView>::Type
      QStringHashBase::hashedString(QStringView s)': gives a type Python has
      no way to take yet.
    - Qt's 'HashedForm<QV4::String *>::Type
      QStringHashBase::hashedString(QV4::String *s)': gives a type Python has
      no way to take yet.
    - Qt's 'HashedForm<const QV4::String *>::Type
      QStringHashBase::hashedString(const QV4::String *s)': gives a type
      Python has no way to take yet.
    - Qt's 'HashedForm<QLatin1StringView>::Type
      QStringHashBase::hashedString(QLatin1StringView s)': gives a type
      Python has no way to take yet.
    - Qt's 'HashedForm<QHashedString>::Type
      QStringHashBase::hashedString(const QHashedString &s)': the compiler
      refuses its ritual as it would be written here:
      'ritual_ZN15QStringHashBase12hashedStringERK13QHashedString' declared
      as a pointer to a reference of type 'HashedForm<QHashedString>::Type'
      (aka 'const QHashedString &').
    - Qt's 'HashedForm<QHashedStringRef>::Type
      QStringHashBase::hashedString(const QHashedStringRef &s)': the compiler
      refuses its ritual as it would be written here:
      'ritual_ZN15QStringHashBase12hashedStringERK16QHashedStringRef'
      declared as a pointer to a reference of type
      'HashedForm<QHashedStringRef>::Type' (aka 'const QHashedStringRef &').
    - Qt's 'HashedForm<QHashedCStringRef>::Type
      QStringHashBase::hashedString(const QHashedCStringRef &s)': the
      compiler refuses its ritual as it would be written here:
      'ritual_ZN15QStringHashBase12hashedStringERK17QHashedCStringRef'
      declared as a pointer to a reference of type
      'HashedForm<QHashedCStringRef>::Type' (aka 'const QHashedCStringRef
      &').
    """
    raise NotImplementedError(
        "'QStringHashBase.hashedString' has no cute function yet. Qt's "
        "'HashedForm<QString>::Type QStringHashBase::hashedString(const "
        "QString &s)': gives a type Python has no way to take yet. Qt's "
        "'HashedForm<QStringView>::Type "
        "QStringHashBase::hashedString(QStringView s)': gives a type Python "
        "has no way to take yet. Qt's 'HashedForm<QV4::String *>::Type "
        "QStringHashBase::hashedString(QV4::String *s)': gives a type "
        "Python has no way to take yet. Qt's 'HashedForm<const QV4::String "
        "*>::Type QStringHashBase::hashedString(const QV4::String *s)': "
        "gives a type Python has no way to take yet. Qt's "
        "'HashedForm<QLatin1StringView>::Type "
        "QStringHashBase::hashedString(QLatin1StringView s)': gives a type "
        "Python has no way to take yet. Qt's "
        "'HashedForm<QHashedString>::Type "
        "QStringHashBase::hashedString(const QHashedString &s)': the "
        "compiler refuses its ritual as it would be written here: "
        "'ritual_ZN15QStringHashBase12hashedStringERK13QHashedString' "
        "declared as a pointer to a reference of type "
        "'HashedForm<QHashedString>::Type' (aka 'const QHashedString &'). "
        "Qt's 'HashedForm<QHashedStringRef>::Type "
        "QStringHashBase::hashedString(const QHashedStringRef &s)': the "
        "compiler refuses its ritual as it would be written here: "
        "'ritual_ZN15QStringHashBase12hashedStringERK16QHashedStringRef' "
        "declared as a pointer to a reference of type "
        "'HashedForm<QHashedStringRef>::Type' (aka 'const QHashedStringRef "
        "&'). Qt's 'HashedForm<QHashedCStringRef>::Type "
        "QStringHashBase::hashedString(const QHashedCStringRef &s)': the "
        "compiler refuses its ritual as it would be written here: "
        "'ritual_ZN15QStringHashBase12hashedStringERK17QHashedCStringRef' "
        "declared as a pointer to a reference of type "
        "'HashedForm<QHashedCStringRef>::Type' (aka 'const "
        "QHashedCStringRef &').")
