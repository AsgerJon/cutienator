"""
QAssociativeIterable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QAssociativeIterable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAssociativeIterable: a plain Python object standing
  in front of one C++ QAssociativeIterable.

  What exists
  -----------

  Every function of Qt's QAssociativeIterable that has a ritual and that
  Python can call so far, 6 names in all: 'containsKey', 'insertKey',
  'removeKey', 'value', 'setValue', 'canRandomAccessIterate'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAssociativeIterable::QAssociativeIterable(const QMetaAssociation
    &metaAssociation, const QMetaType &metaType, void *iterable)': names
    'void', which has no cute class yet.
  - Qt's 'QAssociativeIterable::QAssociativeIterable(const QMetaAssociation
    &metaAssociation, const QMetaType &metaType, const void *iterable)':
    names 'void', which has no cute class yet.
  - Qt's
    'QAssociativeIterable::QAssociativeIterable(QIterable<QMetaAssociation>
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QAssociativeIterable
    &QAssociativeIterable::operator=(QIterable<QMetaAssociation> &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const_iterator QAssociativeIterable::begin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QAssociativeIterable::end() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QAssociativeIterable::constBegin() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_iterator QAssociativeIterable::constEnd() const': gives a
    type Python has no way to take yet.
  - Qt's 'iterator QAssociativeIterable::mutableBegin()': gives a type Python
    has no way to take yet.
  - Qt's 'iterator QAssociativeIterable::mutableEnd()': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QAssociativeIterable::find(const QVariant &key)
    const': gives a type Python has no way to take yet.
  - Qt's 'const_iterator QAssociativeIterable::constFind(const QVariant &key)
    const': gives a type Python has no way to take yet.
  - Qt's 'iterator QAssociativeIterable::mutableFind(const QVariant &key)':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QAssociativeIterable is created at the first use, not by
    'QAssociativeIterable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAssociativeIterable.
  - Each name of Qt's QAssociativeIterable that has no cute function yet,
    'begin', 'constBegin', 'constEnd', 'constFind', 'end', 'find',
    'mutableBegin', 'mutableEnd', 'mutableFind', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAssociativeIterable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def value(self, key: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QAssociativeIterable::value(const QVariant &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qassociativeiterable.html#value

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAssociativeIterable::value(const QVariant &key) const
    address = self.uglySide.call(
        'ritual_ZNK20QAssociativeIterable5valueERK8QVariant',
        self._valueOf(key),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def canRandomAccessIterate(self) -> bool:
    """
    Calls Qt's 'bool QAssociativeIterable::canRandomAccessIterate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#canRandomAccessIterate
    """
    #  bool QAssociativeIterable::canRandomAccessIterate() const
    return self.uglySide.call(
        'ritual_ZNK20QAssociativeIterable22canRandomAccessIterateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setValue(self, key: QVariant, mapped: QVariant) -> None:
    """
    Calls Qt's 'void QAssociativeIterable::setValue(const QVariant &key,
    const QVariant &mapped)'.

    Qt's own words: https://doc.qt.io/qt-6/qassociativeiterable.html#setValue

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    mapped : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAssociativeIterable::setValue(const QVariant &key, const
    #      QVariant &mapped)
    self.uglySide.call(
        'ritual_ZN20QAssociativeIterable8setValueERK8QVariantS2_',
        self._valueOf(key), self._valueOf(mapped),
    )

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
    Notes what was given, for Qt's
    'QAssociativeIterable::QAssociativeIterable()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#QAssociativeIterable
    """
    #  QAssociativeIterable::QAssociativeIterable()
    self._noteCreation(QAssociativeIterable, lambda: Rituals.call(
        'ritual_ZN20QAssociativeIterableC1Ev',
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

  @overload(QVariant)
  def containsKey(self, key: QVariant) -> bool:
    """
    Calls Qt's 'bool QAssociativeIterable::containsKey(const QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#containsKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QAssociativeIterable::containsKey(const QVariant &key)
    return self.uglySide.call(
        'ritual_ZN20QAssociativeIterable11containsKeyERK8QVariant',
        self._valueOf(key),
    )

  @overload(QVariant)
  def insertKey(self, key: QVariant) -> None:
    """
    Calls Qt's 'void QAssociativeIterable::insertKey(const QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#insertKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAssociativeIterable::insertKey(const QVariant &key)
    self.uglySide.call(
        'ritual_ZN20QAssociativeIterable9insertKeyERK8QVariant',
        self._valueOf(key),
    )

  @overload(QVariant)
  def removeKey(self, key: QVariant) -> None:
    """
    Calls Qt's 'void QAssociativeIterable::removeKey(const QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#removeKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAssociativeIterable::removeKey(const QVariant &key)
    self.uglySide.call(
        'ritual_ZN20QAssociativeIterable9removeKeyERK8QVariant',
        self._valueOf(key),
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QAssociativeIterable::begin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.begin' has no cute function yet. Qt's "
        "'const_iterator QAssociativeIterable::begin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QAssociativeIterable::constBegin() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.constBegin' has no cute function yet. Qt's "
        "'const_iterator QAssociativeIterable::constBegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QAssociativeIterable::constEnd() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.constEnd' has no cute function yet. Qt's "
        "'const_iterator QAssociativeIterable::constEnd() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def constFind(*__, **_) -> Never:
    """
    Qt's 'const_iterator QAssociativeIterable::constFind(const QVariant &key)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.constFind' has no cute function yet. Qt's "
        "'const_iterator QAssociativeIterable::constFind(const QVariant "
        "&key) const': gives a type Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator QAssociativeIterable::end() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.end' has no cute function yet. Qt's "
        "'const_iterator QAssociativeIterable::end() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def find(*__, **_) -> Never:
    """
    Qt's 'const_iterator QAssociativeIterable::find(const QVariant &key)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.find' has no cute function yet. Qt's "
        "'const_iterator QAssociativeIterable::find(const QVariant &key) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def mutableBegin(*__, **_) -> Never:
    """
    Qt's 'iterator QAssociativeIterable::mutableBegin()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.mutableBegin' has no cute function yet. Qt's "
        "'iterator QAssociativeIterable::mutableBegin()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mutableEnd(*__, **_) -> Never:
    """
    Qt's 'iterator QAssociativeIterable::mutableEnd()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.mutableEnd' has no cute function yet. Qt's "
        "'iterator QAssociativeIterable::mutableEnd()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def mutableFind(*__, **_) -> Never:
    """
    Qt's 'iterator QAssociativeIterable::mutableFind(const QVariant &key)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAssociativeIterable.mutableFind' has no cute function yet. Qt's "
        "'iterator QAssociativeIterable::mutableFind(const QVariant &key)': "
        "gives a type Python has no way to take yet.")
