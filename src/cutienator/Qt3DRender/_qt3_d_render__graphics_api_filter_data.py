"""
Qt3DRender::GraphicsApiFilterData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qgraphicsapifilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::GraphicsApiFilterData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class GraphicsApiFilterData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::GraphicsApiFilterData: a plain Python
  object standing in front of one C++ Qt3DRender::GraphicsApiFilterData.

  C++ hands a Qt3DRender::GraphicsApiFilterData around as a copy, so every
  C++ Qt3DRender::GraphicsApiFilterData behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::GraphicsApiFilterData that has a ritual
  and that Python can call so far, 4 names in all: 'toString', '__eq__',
  '__ne__', '__lt__'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::GraphicsApiFilterData::~GraphicsApiFilterData()': the
    destructor: Python removes its C++ Qt3DRender::GraphicsApiFilterData by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::GraphicsApiFilterData is created at the first use,
    not by 'Qt3DRender::GraphicsApiFilterData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::GraphicsApiFilterData back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::GraphicsApiFilterData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::GraphicsApiFilterData'

  #  Qt's '~Qt3DRender::GraphicsApiFilterData()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::GraphicsApiFilterData
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender21GraphicsApiFilterDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::GraphicsApiFilterData::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-graphicsapifilterdata.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::GraphicsApiFilterData::toString() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21GraphicsApiFilterData8toStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: GraphicsApiFilterData) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::GraphicsApiFilterData::operator==(const
    GraphicsApiFilterData &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-graphicsapifilterdata.html#operator==

    Parameters
    ----------

    other : GraphicsApiFilterData
      Passed on as a value: Qt reads the C++
      Qt3DRender::GraphicsApiFilterData, which stays Python's own.
    """
    #  bool Qt3DRender::GraphicsApiFilterData::operator==(const
    #      GraphicsApiFilterData &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21GraphicsApiFilterDataeqERKS0_',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: GraphicsApiFilterData) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::GraphicsApiFilterData::operator!=(const
    GraphicsApiFilterData &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-graphicsapifilterdata.html#operator!=

    Parameters
    ----------

    other : GraphicsApiFilterData
      Passed on as a value: Qt reads the C++
      Qt3DRender::GraphicsApiFilterData, which stays Python's own.
    """
    #  bool Qt3DRender::GraphicsApiFilterData::operator!=(const
    #      GraphicsApiFilterData &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21GraphicsApiFilterDataneERKS0_',
        self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, other: GraphicsApiFilterData) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::GraphicsApiFilterData::operator<(const
    GraphicsApiFilterData &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-graphicsapifilterdata.html#operator<

    Parameters
    ----------

    other : GraphicsApiFilterData
      Passed on as a value: Qt reads the C++
      Qt3DRender::GraphicsApiFilterData, which stays Python's own.
    """
    #  bool Qt3DRender::GraphicsApiFilterData::operator<(const
    #      GraphicsApiFilterData &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21GraphicsApiFilterDataltERKS0_',
        self._valueOf(other),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::GraphicsApiFilterData::GraphicsApiFilterData()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-graphicsapifilterdata.html
    """
    #  Qt3DRender::GraphicsApiFilterData::GraphicsApiFilterData()
    self._noteCreation(GraphicsApiFilterData, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21GraphicsApiFilterDataC1Ev',
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
