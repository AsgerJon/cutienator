"""
CacheData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means CacheData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractItemModelReplicaImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModelReplicaImplementation = WAIT['QAbstractItemModelReplicaImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CacheData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's CacheData: a plain Python object standing in front of
  one C++ CacheData.

  C++ hands a CacheData around as a copy, so every C++ CacheData behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's CacheData that has a ritual and that Python can call
  so far, 4 names in all: 'ensureChildren', 'insertChildren',
  'removeChildren', 'clear'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CacheData::~CacheData()': the destructor: Python removes its C++
    CacheData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ CacheData is created at the first use, not by 'CacheData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a CacheData back gives a copy the ritual made for
    Python, in a new cute CacheData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CacheData'

  #  Qt's '~CacheData()'. Naming it makes this a value class: Python owns
  #  every C++ CacheData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9CacheDataD1Ev'

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

  @overload(QAbstractItemModelReplicaImplementation)
  @overload(NoneType)
  @overload(QAbstractItemModelReplicaImplementation, THIS)
  @overload(QAbstractItemModelReplicaImplementation, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      model: Optional[QAbstractItemModelReplicaImplementation],
      parentItem: Optional[CacheData] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'CacheData::CacheData(QAbstractItemModelReplicaImplementation *model,
    CacheData *parentItem)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/cachedata.html#CacheData

    Parameters
    ----------

    model : Optional[QAbstractItemModelReplicaImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentItem : Optional[CacheData]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  CacheData::CacheData(QAbstractItemModelReplicaImplementation *model,
    #      CacheData *parentItem)
    self._noteCreation(CacheData, lambda: Rituals.call(
        'ritual_ZN9CacheDataC1EP39QAbstractItemModelReplicaImplementationPS'
        '_',
        self._addressOf(model), self._addressOf(parentItem),
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

  @overload(int, int)
  def ensureChildren(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void CacheData::ensureChildren(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/cachedata.html#ensureChildren

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void CacheData::ensureChildren(int start, int end)
    self.uglySide.call('ritual_ZN9CacheData14ensureChildrenEii', start, end)

  @overload(int, int)
  def insertChildren(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void CacheData::insertChildren(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/cachedata.html#insertChildren

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void CacheData::insertChildren(int start, int end)
    self.uglySide.call('ritual_ZN9CacheData14insertChildrenEii', start, end)

  @overload(int, int)
  def removeChildren(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void CacheData::removeChildren(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/cachedata.html#removeChildren

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void CacheData::removeChildren(int start, int end)
    self.uglySide.call('ritual_ZN9CacheData14removeChildrenEii', start, end)

  def clear(self) -> None:
    """
    Calls Qt's 'void CacheData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/cachedata.html#clear
    """
    #  void CacheData::clear()
    self.uglySide.call('ritual_ZN9CacheData5clearEv')
