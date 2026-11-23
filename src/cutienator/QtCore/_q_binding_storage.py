"""
QBindingStorage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbindingstorage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBindingStorage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBindingStorage: a plain Python object standing in
  front of one C++ QBindingStorage.

  C++ hands a QBindingStorage around as a copy, so every C++ QBindingStorage
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBindingStorage that has a ritual and that Python
  can call so far, 6 names in all: 'isEmpty', 'isValid',
  'registerDependency', 'reinitAfterThreadMove', 'clear',
  'registerDependency_helper'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBindingStorage::~QBindingStorage()': the destructor: Python
    removes its C++ QBindingStorage by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QBindingStorage is created at the first use, not by
    'QBindingStorage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBindingStorage back gives a copy the ritual made for
    Python, in a new cute QBindingStorage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBindingStorage'

  #  Qt's '~QBindingStorage()'. Naming it makes this a value class: Python
  #  owns every C++ QBindingStorage behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QBindingStorageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QBindingStorage::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbindingstorage.html#isValid
    """
    #  bool QBindingStorage::isValid() const
    return self.uglySide.call('ritual_ZNK15QBindingStorage7isValidEv')

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
    Notes what was given, for Qt's 'QBindingStorage::QBindingStorage()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbindingstorage.html#QBindingStorage
    """
    #  QBindingStorage::QBindingStorage()
    self._noteCreation(QBindingStorage, lambda: Rituals.call(
        'ritual_ZN15QBindingStorageC1Ev',
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

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QBindingStorage::isEmpty()'.

    Qt's own words: https://doc.qt.io/qt-6/qbindingstorage.html#isEmpty
    """
    #  bool QBindingStorage::isEmpty()
    return self.uglySide.call('ritual_ZN15QBindingStorage7isEmptyEv')

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def registerDependency(self, data: Optional[QUntypedPropertyData]) -> None:
    """
    Calls Qt's 'void QBindingStorage::registerDependency(const
    QUntypedPropertyData *data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbindingstorage.html#registerDependency

    Parameters
    ----------

    data : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBindingStorage::registerDependency(const QUntypedPropertyData
    #      *data) const
    self.uglySide.call(
        'ritual_ZNK15QBindingStorage18registerDependencyEPK20QUntypedProper'
        'tyData',
        self._addressOf(data),
    )

  def reinitAfterThreadMove(self) -> None:
    """
    Calls Qt's 'void QBindingStorage::reinitAfterThreadMove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbindingstorage.html#reinitAfterThreadMove
    """
    #  void QBindingStorage::reinitAfterThreadMove()
    self.uglySide.call('ritual_ZN15QBindingStorage21reinitAfterThreadMoveEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QBindingStorage::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbindingstorage.html#clear
    """
    #  void QBindingStorage::clear()
    self.uglySide.call('ritual_ZN15QBindingStorage5clearEv')

  @overload(QUntypedPropertyData)
  @overload(NoneType)
  def registerDependency_helper(
      self,
      data: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Calls Qt's 'void QBindingStorage::registerDependency_helper(const
    QUntypedPropertyData *data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbindingstorage.html#registerDependency_helper

    Parameters
    ----------

    data : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBindingStorage::registerDependency_helper(const
    #      QUntypedPropertyData *data) const
    self.uglySide.call(
        'ritual_ZNK15QBindingStorage25registerDependency_helperEPK20QUntype'
        'dPropertyData',
        self._addressOf(data),
    )
