"""
QSSGClipPlane binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGClipPlane to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D
  from ..QtQuick3DUtils import QSSGBounds3
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGBounds3 = WAIT['QSSGBounds3']
  QVector3D = WAIT['QVector3D']


class QSSGClipPlane(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGClipPlane: a plain Python object standing in
  front of one C++ QSSGClipPlane.

  C++ hands a QSSGClipPlane around as a copy, so every C++ QSSGClipPlane
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGClipPlane that has a ritual and that Python can
  call so far, 6 names in all: 'distance', 'intersectWithLine', 'corner',
  'intersect', 'intersectSimple', 'calculateBBoxEdges'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGClipPlane::~QSSGClipPlane()': the destructor: Python removes
    its C++ QSSGClipPlane by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGClipPlane is created at the first use, not by
    'QSSGClipPlane(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGClipPlane back gives a copy the ritual made for
    Python, in a new cute QSSGClipPlane.
  """

  #  The enums Qt writes inside QSSGClipPlane, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BoxEdgeID(CuteNum):
    """
    The enum 'QSSGClipPlane::BoxEdgeID' of Qt, with the 4 names Qt gives in
    it.
    """

    NULL = Kee[int](0)
    xMax = Kee[int](1)
    yMax = Kee[int](2)
    zMax = Kee[int](4)

  #  The classes Qt writes inside QSSGClipPlane, each a class in here as in
  #  C++.

  class BoxEdge(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGClipPlane::BoxEdge: a plain Python object
    standing in front of one C++ QSSGClipPlane::BoxEdge.

    C++ hands a QSSGClipPlane::BoxEdge around as a copy, so every C++
    QSSGClipPlane::BoxEdge behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGClipPlane::BoxEdge yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGClipPlane::BoxEdge::~BoxEdge()': the destructor: Python
      removes its C++ QSSGClipPlane::BoxEdge by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGClipPlane::BoxEdge is created at the first use, not by
      'QSSGClipPlane::BoxEdge(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGClipPlane::BoxEdge back gives a copy the ritual
      made for Python, in a new cute QSSGClipPlane::BoxEdge.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGClipPlane::BoxEdge'

    #  Qt's '~QSSGClipPlane::BoxEdge()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGClipPlane::BoxEdge behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGClipPlane7BoxEdgeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGBounds3, int)
  def corner(bounds: QSSGBounds3, edge: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGClipPlane::corner(const QSSGBounds3 &bounds,
    BoxEdgeFlag edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgclipplane.html#corner

    Parameters
    ----------

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.

    edge : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGClipPlane::corner(const QSSGBounds3 &bounds, BoxEdgeFlag
    #      edge)
    address = Rituals.call(
        'ritual_ZN13QSSGClipPlane6cornerERK11QSSGBounds3h',
        CuteMixin._valueOf(bounds), edge,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGClipPlane'

  #  Qt's '~QSSGClipPlane()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGClipPlane behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGClipPlaneD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def distance(self, pt: QVector3D) -> float:
    """
    Calls Qt's 'float QSSGClipPlane::distance(const QVector3D &pt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgclipplane.html#distance

    Parameters
    ----------

    pt : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QSSGClipPlane::distance(const QVector3D &pt) const
    return self.uglySide.call(
        'ritual_ZNK13QSSGClipPlane8distanceERK9QVector3D', self._valueOf(pt),
    )

  @overload(QVector3D, QVector3D)
  def intersectWithLine(self, p0: QVector3D, p1: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGClipPlane::intersectWithLine(const QVector3D
    &p0, const QVector3D &p1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgclipplane.html#intersectWithLine

    Parameters
    ----------

    p0 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    p1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGClipPlane::intersectWithLine(const QVector3D &p0, const
    #      QVector3D &p1) const
    address = self.uglySide.call(
        'ritual_ZNK13QSSGClipPlane17intersectWithLineERK9QVector3DS2_',
        self._valueOf(p0), self._valueOf(p1),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QSSGBounds3)
  def intersect(self, bounds: QSSGBounds3) -> int:
    """
    Calls Qt's 'int QSSGClipPlane::intersect(const QSSGBounds3 &bounds)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgclipplane.html#intersect

    Parameters
    ----------

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  int QSSGClipPlane::intersect(const QSSGBounds3 &bounds) const
    return self.uglySide.call(
        'ritual_ZNK13QSSGClipPlane9intersectERK11QSSGBounds3',
        self._valueOf(bounds),
    )

  @overload(QSSGBounds3)
  def intersectSimple(self, bounds: QSSGBounds3) -> bool:
    """
    Calls Qt's 'bool QSSGClipPlane::intersectSimple(const QSSGBounds3
    &bounds) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgclipplane.html#intersectSimple

    Parameters
    ----------

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  bool QSSGClipPlane::intersectSimple(const QSSGBounds3 &bounds) const
    return self.uglySide.call(
        'ritual_ZNK13QSSGClipPlane15intersectSimpleERK11QSSGBounds3',
        self._valueOf(bounds),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def calculateBBoxEdges(self) -> None:
    """
    Calls Qt's 'void QSSGClipPlane::calculateBBoxEdges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgclipplane.html#calculateBBoxEdges
    """
    #  void QSSGClipPlane::calculateBBoxEdges()
    self.uglySide.call('ritual_ZN13QSSGClipPlane18calculateBBoxEdgesEv')
