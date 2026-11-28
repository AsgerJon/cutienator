"""
QGeoMapItemGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomapitemgeometry_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoMapItemGeometry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPainterPath, QVector2D
  from ..QtPositioning import QDoubleVector2D, QGeoCoordinate, QGeoRectangle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRectangle = WAIT['QGeoRectangle']
  QPointF = WAIT['QPointF']


class QGeoMapItemGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoMapItemGeometry: a plain Python object standing
  in front of one C++ QGeoMapItemGeometry.

  What exists
  -----------

  Every function of Qt's QGeoMapItemGeometry that has a ritual and that
  Python can call so far, 23 names in all: 'path', 'perimeter',
  'pathMercator', 'isSourceDirty', 'isScreenDirty', 'markSourceDirty',
  'markScreenDirty', 'markFullScreenDirty', 'markClean', 'clearScreen',
  'geoLeftBound', 'sourceBoundingBox', 'screenBoundingBox', 'clearBounds',
  'firstPointOffset', 'origin', 'screenOutline', 'contains', 'vertex',
  'vertices', 'isIndexed', 'size', 'clear'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoMapItemGeometry::~QGeoMapItemGeometry()': the destructor:
    Python never removes a C++ QGeoMapItemGeometry.
  - Qt's 'QList<quint32> QGeoMapItemGeometry::indices() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoMapItemGeometry is created at the first use, not by
    'QGeoMapItemGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoMapItemGeometry.
  - Each name of Qt's QGeoMapItemGeometry that has no cute function yet,
    'indices', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGeoRectangle)
  def path(rect: QGeoRectangle) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoMapItemGeometry::path(const
    QGeoRectangle &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#path

    Parameters
    ----------

    rect : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoMapItemGeometry::path(const QGeoRectangle
    #      &rect)
    address = Rituals.call(
        'ritual_ZN19QGeoMapItemGeometry4pathERK13QGeoRectangle',
        CuteMixin._valueOf(rect),
    )
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  @staticmethod
  @overload(QGeoRectangle)
  def perimeter(rect: QGeoRectangle) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoMapItemGeometry::perimeter(const
    QGeoRectangle &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#perimeter

    Parameters
    ----------

    rect : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoMapItemGeometry::perimeter(const
    #      QGeoRectangle &rect)
    address = Rituals.call(
        'ritual_ZN19QGeoMapItemGeometry9perimeterERK13QGeoRectangle',
        CuteMixin._valueOf(rect),
    )
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  @staticmethod
  @overload(QList[QGeoCoordinate])
  def pathMercator(p: QList[QGeoCoordinate]) -> QList[QDoubleVector2D]:
    """
    Calls Qt's 'QList<QDoubleVector2D>
    QGeoMapItemGeometry::pathMercator(const QList<QGeoCoordinate> &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#pathMercator

    Parameters
    ----------

    p : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QDoubleVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDoubleVector2D> QGeoMapItemGeometry::pathMercator(const
    #      QList<QGeoCoordinate> &p)
    address = Rituals.call(
        'ritual_ZN19QGeoMapItemGeometry12pathMercatorERK5QListI14QGeoCoordi'
        'nateE',
        CuteMixin._valueOf(p),
    )
    from ..QtPositioning import QDoubleVector2D
    return QList[QDoubleVector2D]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMapItemGeometry'

  #  A C++ QGeoMapItemGeometry Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoMapItemGeometry'

  #  The functions Qt calls itself that QGeoMapItemGeometry is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'contains': (
          ('_ZNK19QGeoMapItemGeometry8containsERK7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSourceDirty(self) -> bool:
    """
    Calls Qt's 'bool QGeoMapItemGeometry::isSourceDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#isSourceDirty
    """
    #  bool QGeoMapItemGeometry::isSourceDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry13isSourceDirtyEv',
    )

  def isScreenDirty(self) -> bool:
    """
    Calls Qt's 'bool QGeoMapItemGeometry::isScreenDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#isScreenDirty
    """
    #  bool QGeoMapItemGeometry::isScreenDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry13isScreenDirtyEv',
    )

  def sourceBoundingBox(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGeoMapItemGeometry::sourceBoundingBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#sourceBoundingBox

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGeoMapItemGeometry::sourceBoundingBox() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry17sourceBoundingBoxEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def screenBoundingBox(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGeoMapItemGeometry::screenBoundingBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#screenBoundingBox

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGeoMapItemGeometry::screenBoundingBox() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry17screenBoundingBoxEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def firstPointOffset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGeoMapItemGeometry::firstPointOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#firstPointOffset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGeoMapItemGeometry::firstPointOffset() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry16firstPointOffsetEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def origin(self) -> QGeoCoordinate:
    """
    Calls Qt's 'const QGeoCoordinate &QGeoMapItemGeometry::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#origin

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  const QGeoCoordinate &QGeoMapItemGeometry::origin() const
    address = self.uglySide.call('ritual_ZNK19QGeoMapItemGeometry6originEv')
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def screenOutline(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGeoMapItemGeometry::screenOutline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#screenOutline

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGeoMapItemGeometry::screenOutline() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry13screenOutlineEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, screenPoint: QPointF) -> bool:
    """
    Calls Qt's 'bool QGeoMapItemGeometry::contains(const QPointF
    &screenPoint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#contains

    Parameters
    ----------

    screenPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGeoMapItemGeometry::contains(const QPointF &screenPoint) const
    ritual = 'ritual_ZNK19QGeoMapItemGeometry8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoMapItemGeometry8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(screenPoint, 'QPointF'))

  @overload(int)
  def vertex(self, index: int) -> QVector2D:
    """
    Calls Qt's 'QVector2D QGeoMapItemGeometry::vertex(quint32 index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#vertex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QGeoMapItemGeometry::vertex(quint32 index) const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry6vertexEj', index,
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def vertices(self) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> QGeoMapItemGeometry::vertices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#vertices

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> QGeoMapItemGeometry::vertices() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoMapItemGeometry8verticesEv',
    )
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  def isIndexed(self) -> bool:
    """
    Calls Qt's 'bool QGeoMapItemGeometry::isIndexed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#isIndexed
    """
    #  bool QGeoMapItemGeometry::isIndexed() const
    return self.uglySide.call('ritual_ZNK19QGeoMapItemGeometry9isIndexedEv')

  def size(self) -> int:
    """
    Calls Qt's 'quint32 QGeoMapItemGeometry::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#size
    """
    #  quint32 QGeoMapItemGeometry::size() const
    return self.uglySide.call('ritual_ZNK19QGeoMapItemGeometry4sizeEv')

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
    'QGeoMapItemGeometry::QGeoMapItemGeometry()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#QGeoMapItemGeometry
    """
    #  QGeoMapItemGeometry::QGeoMapItemGeometry()
    self._noteCreation(QGeoMapItemGeometry, lambda: Rituals.call(
        'ritual_ZN19QGeoMapItemGeometryC1Ev',
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

  def markSourceDirty(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::markSourceDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#markSourceDirty
    """
    #  void QGeoMapItemGeometry::markSourceDirty()
    self.uglySide.call('ritual_ZN19QGeoMapItemGeometry15markSourceDirtyEv')

  def markScreenDirty(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::markScreenDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#markScreenDirty
    """
    #  void QGeoMapItemGeometry::markScreenDirty()
    self.uglySide.call('ritual_ZN19QGeoMapItemGeometry15markScreenDirtyEv')

  def markFullScreenDirty(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::markFullScreenDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#markFullScreenDirty
    """
    #  void QGeoMapItemGeometry::markFullScreenDirty()
    self.uglySide.call(
        'ritual_ZN19QGeoMapItemGeometry19markFullScreenDirtyEv',
    )

  def markClean(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::markClean()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#markClean
    """
    #  void QGeoMapItemGeometry::markClean()
    self.uglySide.call('ritual_ZN19QGeoMapItemGeometry9markCleanEv')

  def clearScreen(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::clearScreen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#clearScreen
    """
    #  void QGeoMapItemGeometry::clearScreen()
    self.uglySide.call('ritual_ZN19QGeoMapItemGeometry11clearScreenEv')

  def geoLeftBound(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoMapItemGeometry::geoLeftBound()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#geoLeftBound

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoMapItemGeometry::geoLeftBound()
    address = self.uglySide.call(
        'ritual_ZN19QGeoMapItemGeometry12geoLeftBoundEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def clearBounds(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::clearBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapitemgeometry.html#clearBounds
    """
    #  void QGeoMapItemGeometry::clearBounds()
    self.uglySide.call('ritual_ZN19QGeoMapItemGeometry11clearBoundsEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QGeoMapItemGeometry::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapitemgeometry.html#clear
    """
    #  void QGeoMapItemGeometry::clear()
    self.uglySide.call('ritual_ZN19QGeoMapItemGeometry5clearEv')

  @staticmethod
  def indices(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> QGeoMapItemGeometry::indices() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoMapItemGeometry.indices' has no cute function yet. Qt's "
        "'QList<quint32> QGeoMapItemGeometry::indices() const': gives a "
        "type Python has no way to take yet.")
