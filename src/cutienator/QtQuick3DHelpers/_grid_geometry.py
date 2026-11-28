"""
GridGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/gridgeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means GridGeometry to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GridGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's GridGeometry: a plain Python object standing in front
  of one C++ GridGeometry.

  What exists
  -----------

  Every function of Qt's GridGeometry that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'horizontalLines',
  'verticalLines', 'horizontalStep', 'verticalStep', 'setHorizontalLines',
  'setVerticalLines', 'setHorizontalStep', 'setVerticalStep',
  'horizontalLinesChanged', 'verticalLinesChanged', 'horizontalStepChanged',
  'verticalStepChanged', 'updateData'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *GridGeometry::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int GridGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'GridGeometry::~GridGeometry()': the destructor: Python never
    removes a C++ GridGeometry.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ GridGeometry is created at the first use, not by
    'GridGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ GridGeometry.
  - Qt tells when it has removed the C++ GridGeometry. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString GridGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString GridGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12GridGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'GridGeometry'

  #  A C++ GridGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_GridGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *GridGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *GridGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK12GridGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def horizontalLines(self) -> int:
    """
    Calls Qt's 'int GridGeometry::horizontalLines() const'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#horizontalLines
    """
    #  int GridGeometry::horizontalLines() const
    return self.uglySide.call('ritual_ZNK12GridGeometry15horizontalLinesEv')

  def verticalLines(self) -> int:
    """
    Calls Qt's 'int GridGeometry::verticalLines() const'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#verticalLines
    """
    #  int GridGeometry::verticalLines() const
    return self.uglySide.call('ritual_ZNK12GridGeometry13verticalLinesEv')

  def horizontalStep(self) -> float:
    """
    Calls Qt's 'float GridGeometry::horizontalStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#horizontalStep
    """
    #  float GridGeometry::horizontalStep() const
    return self.uglySide.call('ritual_ZNK12GridGeometry14horizontalStepEv')

  def verticalStep(self) -> float:
    """
    Calls Qt's 'float GridGeometry::verticalStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#verticalStep
    """
    #  float GridGeometry::verticalStep() const
    return self.uglySide.call('ritual_ZNK12GridGeometry12verticalStepEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setHorizontalLines(self, count: int) -> None:
    """
    Calls Qt's 'void GridGeometry::setHorizontalLines(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/gridgeometry.html#setHorizontalLines

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void GridGeometry::setHorizontalLines(int count)
    self.uglySide.call(
        'ritual_ZN12GridGeometry18setHorizontalLinesEi', count,
    )

  @overload(int)
  def setVerticalLines(self, count: int) -> None:
    """
    Calls Qt's 'void GridGeometry::setVerticalLines(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#setVerticalLines

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void GridGeometry::setVerticalLines(int count)
    self.uglySide.call('ritual_ZN12GridGeometry16setVerticalLinesEi', count)

  @overload(float)
  def setHorizontalStep(self, step: float) -> None:
    """
    Calls Qt's 'void GridGeometry::setHorizontalStep(float step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/gridgeometry.html#setHorizontalStep

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void GridGeometry::setHorizontalStep(float step)
    self.uglySide.call('ritual_ZN12GridGeometry17setHorizontalStepEf', step)

  @overload(float)
  def setVerticalStep(self, step: float) -> None:
    """
    Calls Qt's 'void GridGeometry::setVerticalStep(float step)'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#setVerticalStep

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void GridGeometry::setVerticalStep(float step)
    self.uglySide.call('ritual_ZN12GridGeometry15setVerticalStepEf', step)

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
    Notes what was given, for Qt's 'GridGeometry::GridGeometry()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#GridGeometry
    """
    #  GridGeometry::GridGeometry()
    self._noteCreation(GridGeometry, lambda: Rituals.call(
        'ritual_ZN12GridGeometryC1Ev',
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

  def horizontalLinesChanged(self) -> None:
    """
    Calls Qt's 'void GridGeometry::horizontalLinesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/gridgeometry.html#horizontalLinesChanged
    """
    #  void GridGeometry::horizontalLinesChanged()
    self.uglySide.call('ritual_ZN12GridGeometry22horizontalLinesChangedEv')

  def verticalLinesChanged(self) -> None:
    """
    Calls Qt's 'void GridGeometry::verticalLinesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/gridgeometry.html#verticalLinesChanged
    """
    #  void GridGeometry::verticalLinesChanged()
    self.uglySide.call('ritual_ZN12GridGeometry20verticalLinesChangedEv')

  def horizontalStepChanged(self) -> None:
    """
    Calls Qt's 'void GridGeometry::horizontalStepChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/gridgeometry.html#horizontalStepChanged
    """
    #  void GridGeometry::horizontalStepChanged()
    self.uglySide.call('ritual_ZN12GridGeometry21horizontalStepChangedEv')

  def verticalStepChanged(self) -> None:
    """
    Calls Qt's 'void GridGeometry::verticalStepChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/gridgeometry.html#verticalStepChanged
    """
    #  void GridGeometry::verticalStepChanged()
    self.uglySide.call('ritual_ZN12GridGeometry19verticalStepChangedEv')

  def updateData(self) -> None:
    """
    Calls Qt's 'void GridGeometry::updateData()'.

    Qt's own words: https://doc.qt.io/qt-6/gridgeometry.html#updateData
    """
    #  void GridGeometry::updateData()
    self.uglySide.call('ritual_ZN12GridGeometry10updateDataEv')
