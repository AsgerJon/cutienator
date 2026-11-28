"""
QtMetaContainerPrivate::Association binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
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


class Association(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::Association: a plain Python
  object standing in front of one C++ QtMetaContainerPrivate::Association.

  C++ hands a QtMetaContainerPrivate::Association around as a copy, so every
  C++ QtMetaContainerPrivate::Association behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QtMetaContainerPrivate::Association that has a
  ritual and that Python can call so far, 5 names in all: 'containsKey',
  'insertKey', 'removeKey', 'value', 'setValue'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::Association::Association(const
    QMetaAssociation &metaAssociation, QMetaType metaType, void *iterable)':
    names 'void', which has no cute class yet.
  - Qt's 'QtMetaContainerPrivate::Association::Association(const
    QMetaAssociation &metaAssociation, QMetaType metaType, const void
    *iterable)': names 'void', which has no cute class yet.
  - Qt's 'QtMetaContainerPrivate::Association::Association(
    QIterable<QMetaAssociation> &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'Association &QtMetaContainerPrivate::Association::operator=(
    QIterable<QMetaAssociation> &&other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Association::begin() const':
    gives a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Association::end() const':
    gives a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Association::constBegin()
    const': gives a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Association::constEnd()
    const': gives a type Python has no way to take yet.
  - Qt's 'Iterator QtMetaContainerPrivate::Association::mutableBegin()':
    gives a type Python has no way to take yet.
  - Qt's 'Iterator QtMetaContainerPrivate::Association::mutableEnd()': gives
    a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Association::find(const
    QVariant &key) const': gives a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Association::constFind(const
    QVariant &key) const': gives a type Python has no way to take yet.
  - Qt's 'Iterator QtMetaContainerPrivate::Association::mutableFind(const
    QVariant &key)': gives a type Python has no way to take yet.
  - Qt's 'QtMetaContainerPrivate::Association::~Association()': the
    destructor: Python removes its C++ QtMetaContainerPrivate::Association by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::Association is created at the first use,
    not by 'QtMetaContainerPrivate::Association(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::Association back gives a copy
    the ritual made for Python, in a new cute
    QtMetaContainerPrivate::Association.
  - Each name of Qt's QtMetaContainerPrivate::Association that has no cute
    function yet, 'begin', 'constBegin', 'constEnd', 'constFind', 'end',
    'find', 'mutableBegin', 'mutableEnd', 'mutableFind', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMetaContainerPrivate::Association'

  #  Qt's '~QtMetaContainerPrivate::Association()'. Naming it makes this a
  #  value class: Python owns every C++ QtMetaContainerPrivate::Association
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QtMetaContainerPrivate11AssociationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def containsKey(self, key: QVariant) -> bool:
    """
    Calls Qt's 'bool QtMetaContainerPrivate::Association::containsKey(const
    QVariant &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-association.html

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QtMetaContainerPrivate::Association::containsKey(const QVariant
    #      &key) const
    return self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate11Association11containsKeyERK8QV'
        'ariant',
        self._valueOf(key),
    )

  @overload(QVariant)
  def value(self, key: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QtMetaContainerPrivate::Association::value(const
    QVariant &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-association.html#value

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
    #  QVariant QtMetaContainerPrivate::Association::value(const QVariant
    #      &key) const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate11Association5valueERK8QVariant',
        self._valueOf(key),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setValue(self, key: QVariant, mapped: QVariant) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Association::setValue(const
    QVariant &key, const QVariant &mapped)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-association.html#setValue

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    mapped : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QtMetaContainerPrivate::Association::setValue(const QVariant
    #      &key, const QVariant &mapped)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate11Association8setValueERK8QVarian'
        'tS3_',
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
    'QtMetaContainerPrivate::Association::Association()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-association.html
    """
    #  QtMetaContainerPrivate::Association::Association()
    self._noteCreation(Association, lambda: Rituals.call(
        'ritual_ZN22QtMetaContainerPrivate11AssociationC1Ev',
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
  def insertKey(self, key: QVariant) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Association::insertKey(const
    QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-association.html#insertKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QtMetaContainerPrivate::Association::insertKey(const QVariant
    #      &key)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate11Association9insertKeyERK8QVaria'
        'nt',
        self._valueOf(key),
    )

  @overload(QVariant)
  def removeKey(self, key: QVariant) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Association::removeKey(const
    QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-association.html#removeKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QtMetaContainerPrivate::Association::removeKey(const QVariant
    #      &key)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate11Association9removeKeyERK8QVaria'
        'nt',
        self._valueOf(key),
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Association::begin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.begin' has no cute function "
        "yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Association::begin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Association::constBegin()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.constBegin' has no cute "
        "function yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Association::constBegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Association::constEnd()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.constEnd' has no cute function "
        "yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Association::constEnd() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def constFind(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Association::constFind(const
    QVariant &key) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.constFind' has no cute "
        "function yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Association::constFind(const QVariant "
        "&key) const': gives a type Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Association::end() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.end' has no cute function yet. "
        "Qt's 'ConstIterator QtMetaContainerPrivate::Association::end() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def find(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Association::find(const
    QVariant &key) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.find' has no cute function "
        "yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Association::find(const QVariant &key) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def mutableBegin(*__, **_) -> Never:
    """
    Qt's 'Iterator QtMetaContainerPrivate::Association::mutableBegin()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.mutableBegin' has no cute "
        "function yet. Qt's 'Iterator "
        "QtMetaContainerPrivate::Association::mutableBegin()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mutableEnd(*__, **_) -> Never:
    """
    Qt's 'Iterator QtMetaContainerPrivate::Association::mutableEnd()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.mutableEnd' has no cute "
        "function yet. Qt's 'Iterator "
        "QtMetaContainerPrivate::Association::mutableEnd()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mutableFind(*__, **_) -> Never:
    """
    Qt's 'Iterator QtMetaContainerPrivate::Association::mutableFind(const
    QVariant &key)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Association.mutableFind' has no cute "
        "function yet. Qt's 'Iterator "
        "QtMetaContainerPrivate::Association::mutableFind(const QVariant "
        "&key)': gives a type Python has no way to take yet.")
