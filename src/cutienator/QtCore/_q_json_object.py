"""
QJsonObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsonobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QJsonValue


class QJsonObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonObject: a plain Python object standing in front
  of one C++ QJsonObject.

  C++ hands a QJsonObject around as a copy, so every C++ QJsonObject behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonObject that has a ritual and that Python can
  call so far, 9 names in all: 'size', 'count', 'length', 'isEmpty', 'value',
  'remove', 'take', 'contains', 'empty'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonObject::~QJsonObject()': the destructor: Python removes its
    C++ QJsonObject by it, and has no other use for it.
  - Qt's 'QJsonValue QJsonObject::operator[](const QString &key) const': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](const QString &key)': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValue QJsonObject::value(QStringView key) const': takes in
    Python what 'QJsonValue QJsonObject::value(const QString &key) const'
    takes.
  - Qt's 'QJsonValue QJsonObject::value(QLatin1StringView key) const': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'QJsonValue QJsonObject::operator[](QStringView key) const': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValue QJsonObject::operator[](QLatin1StringView key) const':
    an operator, which is not reflected yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](QStringView key)': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](QLatin1StringView key)': an
    operator, which is not reflected yet.
  - Qt's 'void QJsonObject::remove(QStringView key)': takes in Python what
    'void QJsonObject::remove(const QString &key)' takes.
  - Qt's 'void QJsonObject::remove(QLatin1StringView key)': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'QJsonValue QJsonObject::take(QStringView key)': takes in Python
    what 'QJsonValue QJsonObject::take(const QString &key)' takes.
  - Qt's 'QJsonValue QJsonObject::take(QLatin1StringView key)': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'bool QJsonObject::contains(QStringView key) const': takes in Python
    what 'bool QJsonObject::contains(const QString &key) const' takes.
  - Qt's 'bool QJsonObject::contains(QLatin1StringView key) const': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'iterator QJsonObject::begin()': gives 'QJsonObject::iterator',
    which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::begin() const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::cbegin() const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::constBegin() const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::end()': gives 'QJsonObject::iterator', which
    has no cute class yet.
  - Qt's 'const_iterator QJsonObject::end() const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::cend() const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::constEnd() const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::erase(iterator it)': names
    'QJsonObject::iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::find(const QString &key)': gives
    'QJsonObject::iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::find(const QString &key) const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::constFind(const QString &key) const':
    gives 'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::insert(const QString &key, const QJsonValue
    &value)': gives 'QJsonObject::iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::find(QStringView key)': gives
    'QJsonObject::iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::find(QLatin1StringView key)': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::find(QStringView key) const': gives
    'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::find(QLatin1StringView key) const':
    names 'QLatin1String', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::constFind(QStringView key) const':
    gives 'QJsonObject::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonObject::constFind(QLatin1StringView key)
    const': names 'QLatin1String', which has no cute class yet.
  - Qt's 'iterator QJsonObject::insert(QStringView key, const QJsonValue
    &value)': gives 'QJsonObject::iterator', which has no cute class yet.
  - Qt's 'iterator QJsonObject::insert(QLatin1StringView key, const
    QJsonValue &value)': names 'QLatin1String', which has no cute class yet.

  What has no ritual
  ------------------

  35 of the 82 functions Qt declares: 18 takes or gives a type that cannot be
  passed yet; 9 a template; 6 private; 2 can only be called on a value about
  to be thrown away.

  What to expect
  --------------

  - The C++ QJsonObject is created at the first use, not by
    'QJsonObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonObject back gives a copy the ritual made for
    Python, in a new cute QJsonObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonObject'

  #  Qt's '~QJsonObject()'. Naming it makes this a value class: Python owns
  #  every C++ QJsonObject behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QJsonObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonObject::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#size
    """
    #  qsizetype QJsonObject::size() const
    return self.uglySide.call('ritual_ZNK11QJsonObject4sizeEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonObject::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#count
    """
    #  qsizetype QJsonObject::count() const
    return self.uglySide.call('ritual_ZNK11QJsonObject5countEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonObject::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#length
    """
    #  qsizetype QJsonObject::length() const
    return self.uglySide.call('ritual_ZNK11QJsonObject6lengthEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QJsonObject::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#isEmpty
    """
    #  bool QJsonObject::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QJsonObject7isEmptyEv')

  @overload(str)
  def value(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::value(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::value(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK11QJsonObject5valueERK7QString', key,
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QJsonObject::contains(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJsonObject::contains(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK11QJsonObject8containsERK7QString', key,
    )

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QJsonObject::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#empty
    """
    #  bool QJsonObject::empty() const
    return self.uglySide.call('ritual_ZNK11QJsonObject5emptyEv')

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
    Notes what was given, for Qt's 'QJsonObject::QJsonObject()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#QJsonObject
    """
    #  QJsonObject::QJsonObject()
    self._noteCreation(QJsonObject, lambda: Rituals.call(
        'ritual_ZN11QJsonObjectC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QJsonObject) -> None:
    """
    Notes what was given, for Qt's 'QJsonObject::QJsonObject(const
    QJsonObject &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#QJsonObject

    Parameters
    ----------

    other : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  QJsonObject::QJsonObject(const QJsonObject &other)
    self._noteCreation(QJsonObject, lambda: Rituals.call(
        'ritual_ZN11QJsonObjectC1ERKS_', self._valueOf(other),
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

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QJsonObject::remove(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QJsonObject::remove(const QString &key)
    self.uglySide.call('ritual_ZN11QJsonObject6removeERK7QString', key)

  @overload(str)
  def take(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::take(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#take

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::take(const QString &key)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject4takeERK7QString', key,
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)
