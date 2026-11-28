"""
QHstsStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhstsstore_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHstsStore to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QHstsPolicy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHstsPolicy = WAIT['QHstsPolicy']


class QHstsStore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHstsStore: a plain Python object standing in front
  of one C++ QHstsStore.

  What exists
  -----------

  Every function of Qt's QHstsStore that has a ritual and that Python can
  call so far, 9 names in all: 'readPolicies', 'addToObserved',
  'synchronize', 'isWritable', 'absoluteFilePath', 'beginHstsGroups',
  'serializePolicy', 'evictPolicy', 'endHstsGroups'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHstsStore::~QHstsStore()': the destructor: Python never removes a
    C++ QHstsStore.
  - Qt's 'bool QHstsStore::deserializePolicy(const QString &key, QHstsPolicy
    &policy)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QHstsStore is created at the first use, not by 'QHstsStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHstsStore.
  - Each name of Qt's QHstsStore that has no cute function yet,
    'deserializePolicy', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def absoluteFilePath(dirName: str) -> str:
    """
    Calls Qt's 'QString QHstsStore::absoluteFilePath(const QString
    &dirName)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#absoluteFilePath

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHstsStore::absoluteFilePath(const QString &dirName)
    return Rituals.call(
        'ritual_ZN10QHstsStore16absoluteFilePathERK7QString', dirName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHstsStore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QHstsStore::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#isWritable
    """
    #  bool QHstsStore::isWritable() const
    return self.uglySide.call('ritual_ZNK10QHstsStore10isWritableEv')

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

  @overload(str)
  def __init__(self, dirName: str) -> None:
    """
    Notes what was given, for Qt's 'QHstsStore::QHstsStore(const QString
    &dirName)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#QHstsStore

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QHstsStore::QHstsStore(const QString &dirName)
    self._noteCreation(QHstsStore, lambda: Rituals.call(
        'ritual_ZN10QHstsStoreC1ERK7QString', dirName,
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

  def readPolicies(self) -> QList[QHstsPolicy]:
    """
    Calls Qt's 'QList<QHstsPolicy> QHstsStore::readPolicies()'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#readPolicies

    Returns
    -------

    QList[QHstsPolicy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHstsPolicy> QHstsStore::readPolicies()
    address = self.uglySide.call('ritual_ZN10QHstsStore12readPoliciesEv')
    from . import QHstsPolicy
    return QList[QHstsPolicy]._cuteOwning(address)

  @overload(QHstsPolicy)
  def addToObserved(self, policy: QHstsPolicy) -> None:
    """
    Calls Qt's 'void QHstsStore::addToObserved(const QHstsPolicy &policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#addToObserved

    Parameters
    ----------

    policy : QHstsPolicy
      Passed on as a value: Qt reads the C++ QHstsPolicy, which stays
      Python's own.
    """
    #  void QHstsStore::addToObserved(const QHstsPolicy &policy)
    self.uglySide.call(
        'ritual_ZN10QHstsStore13addToObservedERK11QHstsPolicy',
        self._valueOf(policy),
    )

  def synchronize(self) -> None:
    """
    Calls Qt's 'void QHstsStore::synchronize()'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#synchronize
    """
    #  void QHstsStore::synchronize()
    self.uglySide.call('ritual_ZN10QHstsStore11synchronizeEv')

  def beginHstsGroups(self) -> None:
    """
    Calls Qt's 'void QHstsStore::beginHstsGroups()'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#beginHstsGroups
    """
    #  void QHstsStore::beginHstsGroups()
    self.uglySide.call('ritual_ZN10QHstsStore15beginHstsGroupsEv')

  @overload(str, QHstsPolicy)
  def serializePolicy(self, key: str, policy: QHstsPolicy) -> bool:
    """
    Calls Qt's 'bool QHstsStore::serializePolicy(const QString &key, const
    QHstsPolicy &policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#serializePolicy

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    policy : QHstsPolicy
      Passed on as a value: Qt reads the C++ QHstsPolicy, which stays
      Python's own.
    """
    #  bool QHstsStore::serializePolicy(const QString &key, const QHstsPolicy
    #      &policy)
    return self.uglySide.call(
        'ritual_ZN10QHstsStore15serializePolicyERK7QStringRK11QHstsPolicy',
        key, self._valueOf(policy),
    )

  @overload(str)
  def evictPolicy(self, key: str) -> None:
    """
    Calls Qt's 'void QHstsStore::evictPolicy(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#evictPolicy

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHstsStore::evictPolicy(const QString &key)
    self.uglySide.call('ritual_ZN10QHstsStore11evictPolicyERK7QString', key)

  def endHstsGroups(self) -> None:
    """
    Calls Qt's 'void QHstsStore::endHstsGroups()'.

    Qt's own words: https://doc.qt.io/qt-6/qhstsstore.html#endHstsGroups
    """
    #  void QHstsStore::endHstsGroups()
    self.uglySide.call('ritual_ZN10QHstsStore13endHstsGroupsEv')

  @staticmethod
  def deserializePolicy(*__, **_) -> Never:
    """
    Qt's 'bool QHstsStore::deserializePolicy(const QString &key, QHstsPolicy
    &policy)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHstsStore.deserializePolicy' has no cute function yet. Qt's "
        "'bool QHstsStore::deserializePolicy(const QString &key, "
        "QHstsPolicy &policy)': takes a type Python has no way to hand over "
        "yet.")
