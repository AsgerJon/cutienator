"""
QPersistentModelIndexData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPersistentModelIndexData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPersistentModelIndexData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPersistentModelIndexData: a plain Python object
  standing in front of one C++ QPersistentModelIndexData.

  C++ hands a QPersistentModelIndexData around as a copy, so every C++
  QPersistentModelIndexData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPersistentModelIndexData that has a ritual and that
  Python can call so far, 2 names in all: 'create', 'destroy'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPersistentModelIndexData::~QPersistentModelIndexData()': the
    destructor: Python removes its C++ QPersistentModelIndexData by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QPersistentModelIndexData is created at the first use, not by
    'QPersistentModelIndexData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPersistentModelIndexData back gives a copy the
    ritual made for Python, in a new cute QPersistentModelIndexData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QModelIndex)
  def create(index: QModelIndex) -> Optional[QPersistentModelIndexData]:
    """
    Calls Qt's 'QPersistentModelIndexData
    *QPersistentModelIndexData::create(const QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindexdata.html#create

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QPersistentModelIndexData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPersistentModelIndexData *QPersistentModelIndexData::create(const
    #      QModelIndex &index)
    address = Rituals.call(
        'ritual_ZN25QPersistentModelIndexData6createERK11QModelIndex',
        CuteMixin._valueOf(index),
    )
    return QPersistentModelIndexData._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def destroy(data: Optional[QPersistentModelIndexData]) -> None:
    """
    Calls Qt's 'void
    QPersistentModelIndexData::destroy(QPersistentModelIndexData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindexdata.html#destroy

    Parameters
    ----------

    data : Optional[QPersistentModelIndexData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPersistentModelIndexData::destroy(QPersistentModelIndexData
    #      *data)
    Rituals.call(
        'ritual_ZN25QPersistentModelIndexData7destroyEPS_',
        CuteMixin._addressOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPersistentModelIndexData'

  #  Qt's '~QPersistentModelIndexData()'. Naming it makes this a value class:
  #  Python owns every C++ QPersistentModelIndexData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QPersistentModelIndexDataD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPersistentModelIndexData::QPersistentModelIndexData()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindexdata.html
    """
    #  QPersistentModelIndexData::QPersistentModelIndexData()
    self._noteCreation(QPersistentModelIndexData, lambda: Rituals.call(
        'ritual_ZN25QPersistentModelIndexDataC1Ev',
    ))

  @overload(QModelIndex)
  def __init__(self, idx: QModelIndex) -> None:
    """
    Notes what was given, for Qt's
    'QPersistentModelIndexData::QPersistentModelIndexData(const QModelIndex
    &idx)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindexdata.html

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QPersistentModelIndexData::QPersistentModelIndexData(const QModelIndex
    #      &idx)
    self._noteCreation(QPersistentModelIndexData, lambda: Rituals.call(
        'ritual_ZN25QPersistentModelIndexDataC1ERK11QModelIndex',
        self._valueOf(idx),
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


#  Qt's 'QList<QPersistentModelIndexData *>': the list of
#  QPersistentModelIndexData, which 'QList[QPersistentModelIndexData]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QPersistentModelIndexData.
QList.createKind(
    QPersistentModelIndexData, 'address',
    make='ritual_list_make_QPersistentModelIndexData_ptr',
    add='ritual_list_add_QPersistentModelIndexData_ptr',
    size='ritual_list_size_QPersistentModelIndexData_ptr',
    at='ritual_list_at_QPersistentModelIndexData_ptr',
    drop='ritual_list_drop_QPersistentModelIndexData_ptr',
)
