"""
QModelRoleData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QVariant


class QModelRoleData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModelRoleData: a plain Python object standing in
  front of one C++ QModelRoleData.

  C++ hands a QModelRoleData around as a copy, so every C++ QModelRoleData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModelRoleData that has a ritual and that Python can
  call so far, 3 names in all: 'role', 'data', 'clearData'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModelRoleData::~QModelRoleData()': the destructor: Python removes
    its C++ QModelRoleData by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QModelRoleData is created at the first use, not by
    'QModelRoleData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModelRoleData back gives a copy the ritual made for
    Python, in a new cute QModelRoleData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModelRoleData'

  #  Qt's '~QModelRoleData()'. Naming it makes this a value class: Python
  #  owns every C++ QModelRoleData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QModelRoleDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def role(self) -> int:
    """
    Calls Qt's 'int QModelRoleData::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledata.html#role
    """
    #  int QModelRoleData::role() const
    return self.uglySide.call('ritual_ZNK14QModelRoleData4roleEv')

  def data(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QModelRoleData::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledata.html#data

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QModelRoleData::data() const
    address = self.uglySide.call('ritual_ZNK14QModelRoleData4dataEv')
    from . import QVariant
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __init__(self, role: int) -> None:
    """
    Notes what was given, for Qt's 'QModelRoleData::QModelRoleData(int
    role)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledata.html#QModelRoleData

    Parameters
    ----------

    role : int
      Passed on as it is.
    """
    #  QModelRoleData::QModelRoleData(int role)
    self._noteCreation(QModelRoleData, lambda: Rituals.call(
        'ritual_ZN14QModelRoleDataC1Ei', role,
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

  def clearData(self) -> None:
    """
    Calls Qt's 'void QModelRoleData::clearData()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledata.html#clearData
    """
    #  void QModelRoleData::clearData()
    self.uglySide.call('ritual_ZN14QModelRoleData9clearDataEv')
