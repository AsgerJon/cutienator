"""
Qt3DCore::QNodeIdTypePair binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNodeIdTypePair(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QNodeIdTypePair: a plain Python object
  standing in front of one C++ Qt3DCore::QNodeIdTypePair.

  C++ hands a Qt3DCore::QNodeIdTypePair around as a copy, so every C++
  Qt3DCore::QNodeIdTypePair behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's Qt3DCore::QNodeIdTypePair yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QNodeIdTypePair::~QNodeIdTypePair()': the destructor:
    Python removes its C++ Qt3DCore::QNodeIdTypePair by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ Qt3DCore::QNodeIdTypePair is created at the first use, not by
    'Qt3DCore::QNodeIdTypePair(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QNodeIdTypePair back gives a copy the
    ritual made for Python, in a new cute Qt3DCore::QNodeIdTypePair.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QNodeIdTypePair'

  #  Qt's '~Qt3DCore::QNodeIdTypePair()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DCore::QNodeIdTypePair behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore15QNodeIdTypePairD1Ev'

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
    'Qt3DCore::QNodeIdTypePair::QNodeIdTypePair()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeidtypepair.html#QNodeIdTypePair
    """
    #  Qt3DCore::QNodeIdTypePair::QNodeIdTypePair()
    self._noteCreation(QNodeIdTypePair, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QNodeIdTypePairC1Ev',
    ))

  @overload(WAIT['Qt3DCore.QNodeId'], QMetaObject)
  @overload(WAIT['Qt3DCore.QNodeId'], NoneType)
  def __init__(
      self,
      _id: Qt3DCore.QNodeId,
      _type: Optional[QMetaObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QNodeIdTypePair::QNodeIdTypePair(QNodeId _id, const
    QMetaObject *_type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodeidtypepair.html#QNodeIdTypePair

    Parameters
    ----------

    _id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    _type : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DCore::QNodeIdTypePair::QNodeIdTypePair(QNodeId _id, const
    #      QMetaObject *_type)
    self._noteCreation(QNodeIdTypePair, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QNodeIdTypePairC1ENS_7QNodeIdEPK11QMetaObject',
        self._valueOf(_id), self._addressOf(_type, 'QMetaObject'),
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
