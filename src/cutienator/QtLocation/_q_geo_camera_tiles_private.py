"""
QGeoCameraTilesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoCameraTilesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtPositioning import QDoubleVector3D
  from . import Frustum, QGeoCameraTiles
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Frustum = WAIT['Frustum']
  QDoubleVector3D = WAIT['QDoubleVector3D']
  QGeoCameraTiles = WAIT['QGeoCameraTiles']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoCameraTilesPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoCameraTilesPrivate: a plain Python object
  standing in front of one C++ QGeoCameraTilesPrivate.

  C++ hands a QGeoCameraTilesPrivate around as a copy, so every C++
  QGeoCameraTilesPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCameraTilesPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'updateMetadata', 'updateGeometry',
  'createFrustum', 'frustumFootprint', 'clipFootprintToMap', 'get'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPair<PolygonVector, PolygonVector>
    QGeoCameraTilesPrivate::splitPolygonAtAxisValue(const PolygonVector
    &polygon, int axis, double value) const': gives a type Python has no way
    to take yet.
  - Qt's 'QList<QPair<double, int>>
    QGeoCameraTilesPrivate::tileIntersections(double p1, int t1, double p2,
    int t2) const': gives a type Python has no way to take yet.
  - Qt's 'QSet<QGeoTileSpec> QGeoCameraTilesPrivate::tilesFromPolygon(const
    PolygonVector &polygon) const': gives a type Python has no way to take
    yet.
  - Qt's 'QGeoCameraTilesPrivate::~QGeoCameraTilesPrivate()': the destructor:
    Python removes its C++ QGeoCameraTilesPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QGeoCameraTilesPrivate is created at the first use, not by
    'QGeoCameraTilesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCameraTilesPrivate back gives a copy the ritual
    made for Python, in a new cute QGeoCameraTilesPrivate.
  - Each name of Qt's QGeoCameraTilesPrivate that has no cute function yet,
    'splitPolygonAtAxisValue', 'tileIntersections', 'tilesFromPolygon', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QGeoCameraTilesPrivate, each a class in
  #  here as in C++.

  class ClippedFootprint(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGeoCameraTilesPrivate::ClippedFootprint: a plain
    Python object standing in front of one C++
    QGeoCameraTilesPrivate::ClippedFootprint.

    C++ hands a QGeoCameraTilesPrivate::ClippedFootprint around as a copy, so
    every C++ QGeoCameraTilesPrivate::ClippedFootprint behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QGeoCameraTilesPrivate::ClippedFootprint yet. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGeoCameraTilesPrivate::ClippedFootprint::~ClippedFootprint()':
      the destructor: Python removes its C++
      QGeoCameraTilesPrivate::ClippedFootprint by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QGeoCameraTilesPrivate::ClippedFootprint is created at the
      first use, not by 'QGeoCameraTilesPrivate::ClippedFootprint(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGeoCameraTilesPrivate::ClippedFootprint back gives
      a copy the ritual made for Python, in a new cute
      QGeoCameraTilesPrivate::ClippedFootprint.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDoubleVector3D = WAIT['QDoubleVector3D']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGeoCameraTilesPrivate::ClippedFootprint'

    #  Qt's '~QGeoCameraTilesPrivate::ClippedFootprint()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QGeoCameraTilesPrivate::ClippedFootprint behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QGeoCameraTilesPrivate16ClippedFootprintD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGeoCameraTilesPrivate::ClippedFootprint::ClippedFootprint()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeocameratilesprivate-clippedfootprint.html
      """
      #  QGeoCameraTilesPrivate::ClippedFootprint::ClippedFootprint()
      self._noteCreation(
          QGeoCameraTilesPrivate.ClippedFootprint, lambda: Rituals.call(
              'ritual_ZN22QGeoCameraTilesPrivate16ClippedFootprintC1Ev',
          ))

    @overload(
        QList[QDoubleVector3D], QList[QDoubleVector3D],
        QList[QDoubleVector3D],
    )
    def __init__(
        self,
        left_: QList[QDoubleVector3D],
        mid_: QList[QDoubleVector3D],
        right_: QList[QDoubleVector3D],
    ) -> None:
      """
      Notes what was given, for Qt's
      'QGeoCameraTilesPrivate::ClippedFootprint::ClippedFootprint(const
      PolygonVector &left_, const PolygonVector &mid_, const PolygonVector
      &right_)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeocameratilesprivate-clippedfootprint.html

      Parameters
      ----------

      left_ : QList[QDoubleVector3D]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.

      mid_ : QList[QDoubleVector3D]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.

      right_ : QList[QDoubleVector3D]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  QGeoCameraTilesPrivate::ClippedFootprint::ClippedFootprint(const
      #      PolygonVector &left_, const PolygonVector &mid_, const
      #      PolygonVector &right_)
      self._noteCreation(
          QGeoCameraTilesPrivate.ClippedFootprint, lambda: Rituals.call(
              'ritual_ZN22QGeoCameraTilesPrivate16ClippedFootprintC1ERK5QLi'
              'stI15QDoubleVector3DES5_S5_',
              self._valueOf(left_), self._valueOf(mid_),
              self._valueOf(right_),
          ))

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

  class TileMap(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGeoCameraTilesPrivate::TileMap: a plain Python
    object standing in front of one C++ QGeoCameraTilesPrivate::TileMap.

    C++ hands a QGeoCameraTilesPrivate::TileMap around as a copy, so every
    C++ QGeoCameraTilesPrivate::TileMap behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QGeoCameraTilesPrivate::TileMap that has a ritual
    and that Python can call so far, 1 name in all: 'add'. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGeoCameraTilesPrivate::TileMap::~TileMap()': the destructor:
      Python removes its C++ QGeoCameraTilesPrivate::TileMap by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QGeoCameraTilesPrivate::TileMap is created at the first use,
      not by 'QGeoCameraTilesPrivate::TileMap(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGeoCameraTilesPrivate::TileMap back gives a copy
      the ritual made for Python, in a new cute
      QGeoCameraTilesPrivate::TileMap.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGeoCameraTilesPrivate::TileMap'

    #  Qt's '~QGeoCameraTilesPrivate::TileMap()'. Naming it makes this a
    #  value class: Python owns every C++ QGeoCameraTilesPrivate::TileMap
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QGeoCameraTilesPrivate7TileMapD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGeoCameraTilesPrivate::TileMap::TileMap()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeocameratilesprivate-tilemap.html#TileMap
      """
      #  QGeoCameraTilesPrivate::TileMap::TileMap()
      self._noteCreation(
          QGeoCameraTilesPrivate.TileMap, lambda: Rituals.call(
              'ritual_ZN22QGeoCameraTilesPrivate7TileMapC1Ev',
          ))

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

    @overload(int, int)
    def add(self, tileX: int, tileY: int) -> None:
      """
      Calls Qt's 'void QGeoCameraTilesPrivate::TileMap::add(int tileX, int
      tileY)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeocameratilesprivate-tilemap.html#add

      Parameters
      ----------

      tileX : int
        Passed on as it is.

      tileY : int
        Passed on as it is.
      """
      #  void QGeoCameraTilesPrivate::TileMap::add(int tileX, int tileY)
      self.uglySide.call(
          'ritual_ZN22QGeoCameraTilesPrivate7TileMap3addEii', tileX, tileY,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGeoCameraTiles)
  @overload(NoneType)
  def get(o: Optional[QGeoCameraTiles]) -> Optional[QGeoCameraTilesPrivate]:
    """
    Calls Qt's 'QGeoCameraTilesPrivate
    *QGeoCameraTilesPrivate::get(QGeoCameraTiles *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameratilesprivate.html#get

    Parameters
    ----------

    o : Optional[QGeoCameraTiles]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGeoCameraTilesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCameraTilesPrivate *QGeoCameraTilesPrivate::get(QGeoCameraTiles
    #      *o)
    address = Rituals.call(
        'ritual_ZN22QGeoCameraTilesPrivate3getEP15QGeoCameraTiles',
        CuteMixin._addressOf(o),
    )
    return QGeoCameraTilesPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCameraTilesPrivate'

  #  Qt's '~QGeoCameraTilesPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoCameraTilesPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QGeoCameraTilesPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def createFrustum(self, viewExpansion: float) -> Frustum:
    """
    Calls Qt's 'Frustum QGeoCameraTilesPrivate::createFrustum(double
    viewExpansion) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratilesprivate.html#createFrustum

    Parameters
    ----------

    viewExpansion : float
      Passed on as it is.

    Returns
    -------

    Frustum
      A new cute Frustum around the copy Qt gave back. Python owns it.
    """
    #  Frustum QGeoCameraTilesPrivate::createFrustum(double viewExpansion)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoCameraTilesPrivate13createFrustumEd', viewExpansion,
    )
    from . import Frustum
    return Frustum._cuteOwning(address)

  @overload(Frustum)
  def frustumFootprint(self, frustum: Frustum) -> QList[QDoubleVector3D]:
    """
    Calls Qt's 'PolygonVector QGeoCameraTilesPrivate::frustumFootprint(const
    Frustum &frustum) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratilesprivate.html#frustumFootprint

    Parameters
    ----------

    frustum : Frustum
      Passed on as a value: Qt reads the C++ Frustum, which stays Python's
      own.

    Returns
    -------

    QList[QDoubleVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  PolygonVector QGeoCameraTilesPrivate::frustumFootprint(const Frustum
    #      &frustum) const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoCameraTilesPrivate16frustumFootprintERK7Frustum',
        self._valueOf(frustum),
    )
    from ..QtPositioning import QDoubleVector3D
    return QList[QDoubleVector3D]._cuteOwning(address)

  @overload(QList[QDoubleVector3D])
  def clipFootprintToMap(
      self,
      footprint: QList[QDoubleVector3D],
  ) -> ClippedFootprint:
    """
    Calls Qt's 'ClippedFootprint
    QGeoCameraTilesPrivate::clipFootprintToMap(const PolygonVector
    &footprint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratilesprivate.html#clipFootprintToMap

    Parameters
    ----------

    footprint : QList[QDoubleVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    ClippedFootprint
      A new cute QGeoCameraTilesPrivate::ClippedFootprint around the copy Qt
      gave back. Python owns it.
    """
    #  ClippedFootprint QGeoCameraTilesPrivate::clipFootprintToMap(const
    #      PolygonVector &footprint) const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoCameraTilesPrivate18clipFootprintToMapERK5QListI15'
        'QDoubleVector3DE',
        self._valueOf(footprint),
    )
    return QGeoCameraTilesPrivate.ClippedFootprint._cuteOwning(address)

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

  def updateMetadata(self) -> None:
    """
    Calls Qt's 'void QGeoCameraTilesPrivate::updateMetadata()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratilesprivate.html#updateMetadata
    """
    #  void QGeoCameraTilesPrivate::updateMetadata()
    self.uglySide.call('ritual_ZN22QGeoCameraTilesPrivate14updateMetadataEv')

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QGeoCameraTilesPrivate::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameratilesprivate.html#updateGeometry
    """
    #  void QGeoCameraTilesPrivate::updateGeometry()
    self.uglySide.call('ritual_ZN22QGeoCameraTilesPrivate14updateGeometryEv')

  @staticmethod
  def splitPolygonAtAxisValue(*__, **_) -> Never:
    """
    Qt's 'QPair<PolygonVector, PolygonVector>
    QGeoCameraTilesPrivate::splitPolygonAtAxisValue(const PolygonVector
    &polygon, int axis, double value) const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QGeoCameraTilesPrivate.splitPolygonAtAxisValue' has no cute "
        "function yet. Qt's 'QPair<PolygonVector, PolygonVector> "
        "QGeoCameraTilesPrivate::splitPolygonAtAxisValue(const "
        "PolygonVector &polygon, int axis, double value) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def tileIntersections(*__, **_) -> Never:
    """
    Qt's 'QList<QPair<double, int>>
    QGeoCameraTilesPrivate::tileIntersections(double p1, int t1, double p2,
    int t2) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoCameraTilesPrivate.tileIntersections' has no cute function "
        "yet. Qt's 'QList<QPair<double, int>> "
        "QGeoCameraTilesPrivate::tileIntersections(double p1, int t1, "
        "double p2, int t2) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def tilesFromPolygon(*__, **_) -> Never:
    """
    Qt's 'QSet<QGeoTileSpec> QGeoCameraTilesPrivate::tilesFromPolygon(const
    PolygonVector &polygon) const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QGeoCameraTilesPrivate.tilesFromPolygon' has no cute function "
        "yet. Qt's 'QSet<QGeoTileSpec> "
        "QGeoCameraTilesPrivate::tilesFromPolygon(const PolygonVector "
        "&polygon) const': gives a type Python has no way to take yet.")
