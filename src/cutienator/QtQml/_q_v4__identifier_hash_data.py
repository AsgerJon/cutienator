"""
QV4::IdentifierHashData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4identifierhashdata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::IdentifierHashData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class IdentifierHashData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::IdentifierHashData: a plain Python object
  standing in front of one C++ QV4::IdentifierHashData.

  What exists
  -----------

  Every function of Qt's QV4::IdentifierHashData that has a ritual and that
  Python can call so far, 1 name in all: 'markObjects'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::IdentifierHashData::~IdentifierHashData()': the destructor:
    Python never removes a C++ QV4::IdentifierHashData.

  What to expect
  --------------

  - The C++ QV4::IdentifierHashData is created at the first use, not by
    'QV4::IdentifierHashData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::IdentifierHashData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::IdentifierHashData'

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

  @overload(WAIT['QV4.IdentifierTable'], int)
  @overload(NoneType, int)
  def __init__(
      self,
      table: Optional[QV4.IdentifierTable],
      numBits: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::IdentifierHashData::IdentifierHashData(IdentifierTable *table, int
    numBits)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhashdata.html#IdentifierHashData

    Parameters
    ----------

    table : Optional[QV4.IdentifierTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    numBits : int
      Passed on as it is.
    """
    #  QV4::IdentifierHashData::IdentifierHashData(IdentifierTable *table,
    #      int numBits)
    self._noteCreation(IdentifierHashData, lambda: Rituals.call(
        'ritual_ZN3QV418IdentifierHashDataC1EPNS_15IdentifierTableEi',
        self._addressOf(table), numBits,
    ))

  @overload(THIS)
  @overload(NoneType)
  def __init__(self, other: Optional[IdentifierHashData]) -> None:
    """
    Notes what was given, for Qt's
    'QV4::IdentifierHashData::IdentifierHashData(IdentifierHashData *other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhashdata.html#IdentifierHashData

    Parameters
    ----------

    other : Optional[IdentifierHashData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::IdentifierHashData::IdentifierHashData(IdentifierHashData *other)
    self._noteCreation(IdentifierHashData, lambda: Rituals.call(
        'ritual_ZN3QV418IdentifierHashDataC1EPS0_', self._addressOf(other),
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

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def markObjects(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::IdentifierHashData::markObjects(MarkStack
    *markStack) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhashdata.html#markObjects

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::IdentifierHashData::markObjects(MarkStack *markStack) const
    self.uglySide.call(
        'ritual_ZNK3QV418IdentifierHashData11markObjectsEPNS_9MarkStackE',
        self._addressOf(markStack),
    )
