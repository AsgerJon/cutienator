"""
SurfaceObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceobject_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SurfaceObject to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import AbstractObjectHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QVector3D
  from . import Surface3DRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QVector3D = WAIT['QVector3D']
  Surface3DRenderer = WAIT['Surface3DRenderer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SurfaceObject(AbstractObjectHelper):
  """
  The cute side of Qt's SurfaceObject: a plain Python object standing in
  front of one C++ SurfaceObject.

  It is built on the cute 'AbstractObjectHelper', as Qt's SurfaceObject is
  built on Qt's AbstractObjectHelper, and has everything that class has.

  C++ hands a SurfaceObject around as a copy, so every C++ SurfaceObject
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's SurfaceObject that has a ritual and that Python can
  call so far, 18 names in all: 'createSmoothIndices',
  'createCoarseSubSection', 'createSmoothGridlineIndices',
  'createCoarseGridlineIndices', 'uploadBuffers', 'gridElementBuf', 'uvBuf',
  'gridIndexCount', 'vertexAt', 'clear', 'minYValue', 'maxYValue',
  'activateSurfaceTexture', 'setLineColor', 'wireframeColor',
  'createSmoothNormalBodyLineItem', 'createSmoothNormalUpperLineItem',
  'normal'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SurfaceObject::~SurfaceObject()': the destructor: Python removes
    its C++ SurfaceObject by it, and has no other use for it.
  - Qt's 'void SurfaceObject::smoothUVs(const QSurfaceDataArray &dataArray,
    const QSurfaceDataArray &modelArray)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void SurfaceObject::coarseUVs(const QSurfaceDataArray &dataArray,
    const QSurfaceDataArray &modelArray)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void SurfaceObject::createCoarseIndices(GLint *indices, int &p, int
    row, int upperRow, int j)': takes a number to change where it is.
  - Qt's 'void SurfaceObject::createNormals(int &p, int row, int upperRow,
    int j)': takes a number to change where it is.
  - Qt's 'void SurfaceObject::createSmoothNormalBodyLine(int &totalIndex, int
    column)': takes a number to change where it is.
  - Qt's 'void SurfaceObject::createSmoothNormalUpperLine(int &totalIndex)':
    takes a number to change where it is.
  - Qt's 'void SurfaceObject::createBuffers(const QList<QVector3D> &vertices,
    const QList<QVector2D> &uvs, const QList<QVector3D> &normals, const GLint
    *indices)': names 'GLint', which has no cute class yet.
  - Qt's 'void SurfaceObject::checkDirections(const QSurfaceDataArray
    &array)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 35 functions Qt declares: 7 leans on 'Abstract3DRenderer.

  What to expect
  --------------

  - The C++ SurfaceObject is created at the first use, not by
    'SurfaceObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a SurfaceObject back gives a copy the ritual made for
    Python, in a new cute SurfaceObject.
  - Each name of Qt's SurfaceObject that has no cute function yet,
    'checkDirections', 'coarseUVs', 'createBuffers', 'createCoarseIndices',
    'createNormals', 'createSmoothNormalBodyLine',
    'createSmoothNormalUpperLine', 'getNormalizedVertex', 'setUpData',
    'setUpSmoothData', 'smoothUVs', 'updateCoarseItem', 'updateCoarseRow',
    'updateSmoothItem', 'updateSmoothRow', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside SurfaceObject, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DataDimension(CuteFlags):
    """
    The flags enum 'SurfaceObject::DataDimension' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'SurfaceObject::DataDimensions'.
    """

    BothAscending = 0x0
    XDescending = 0x1
    ZDescending = 0x2
    BothDescending = 0x3

  DataDimensions = DataDimension

  class SurfaceType(CuteNum):
    """
    The enum 'SurfaceObject::SurfaceType' of Qt, with the 3 names Qt gives in
    it.
    """

    SurfaceSmooth = Kee[int](0)
    SurfaceFlat = Kee[int](1)
    Undefined = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SurfaceObject'

  #  A C++ SurfaceObject Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SurfaceObject'

  #  Qt's '~SurfaceObject()'. Naming it makes this a value class: Python owns
  #  every C++ SurfaceObject behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13SurfaceObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minYValue(self) -> float:
    """
    Calls Qt's 'float SurfaceObject::minYValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#minYValue
    """
    #  float SurfaceObject::minYValue() const
    return self.uglySide.call('ritual_ZNK13SurfaceObject9minYValueEv')

  def maxYValue(self) -> float:
    """
    Calls Qt's 'float SurfaceObject::maxYValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#maxYValue
    """
    #  float SurfaceObject::maxYValue() const
    return self.uglySide.call('ritual_ZNK13SurfaceObject9maxYValueEv')

  def wireframeColor(self) -> QColor:
    """
    Calls Qt's 'const QColor &SurfaceObject::wireframeColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#wireframeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &SurfaceObject::wireframeColor() const
    address = self.uglySide.call(
        'ritual_ZNK13SurfaceObject14wireframeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setLineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void SurfaceObject::setLineColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#setLineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void SurfaceObject::setLineColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN13SurfaceObject12setLineColorERK6QColor',
        self._valueOf(color),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Surface3DRenderer)
  @overload(NoneType)
  def __init__(self, renderer: Optional[Surface3DRenderer]) -> None:
    """
    Notes what was given, for Qt's
    'SurfaceObject::SurfaceObject(Surface3DRenderer *renderer)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#SurfaceObject

    Parameters
    ----------

    renderer : Optional[Surface3DRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  SurfaceObject::SurfaceObject(Surface3DRenderer *renderer)
    self._noteCreation(SurfaceObject, lambda: Rituals.call(
        'ritual_ZN13SurfaceObjectC1EP17Surface3DRenderer',
        self._addressOf(renderer),
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

  @overload(int, int, int, int)
  def createSmoothIndices(
      self,
      x: int,
      y: int,
      endX: int,
      endY: int,
  ) -> None:
    """
    Calls Qt's 'void SurfaceObject::createSmoothIndices(int x, int y, int
    endX, int endY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#createSmoothIndices

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    endX : int
      Passed on as it is.

    endY : int
      Passed on as it is.
    """
    #  void SurfaceObject::createSmoothIndices(int x, int y, int endX, int
    #      endY)
    self.uglySide.call(
        'ritual_ZN13SurfaceObject19createSmoothIndicesEiiii',
        x, y, endX, endY,
    )

  @overload(int, int, int, int)
  def createCoarseSubSection(
      self,
      x: int,
      y: int,
      columns: int,
      rows: int,
  ) -> None:
    """
    Calls Qt's 'void SurfaceObject::createCoarseSubSection(int x, int y, int
    columns, int rows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#createCoarseSubSection

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    columns : int
      Passed on as it is.

    rows : int
      Passed on as it is.
    """
    #  void SurfaceObject::createCoarseSubSection(int x, int y, int columns,
    #      int rows)
    self.uglySide.call(
        'ritual_ZN13SurfaceObject22createCoarseSubSectionEiiii',
        x, y, columns, rows,
    )

  @overload(int, int, int, int)
  def createSmoothGridlineIndices(
      self,
      x: int,
      y: int,
      endX: int,
      endY: int,
  ) -> None:
    """
    Calls Qt's 'void SurfaceObject::createSmoothGridlineIndices(int x, int y,
    int endX, int endY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#createSmoothGridlineIndices

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    endX : int
      Passed on as it is.

    endY : int
      Passed on as it is.
    """
    #  void SurfaceObject::createSmoothGridlineIndices(int x, int y, int
    #      endX, int endY)
    self.uglySide.call(
        'ritual_ZN13SurfaceObject27createSmoothGridlineIndicesEiiii',
        x, y, endX, endY,
    )

  @overload(int, int, int, int)
  def createCoarseGridlineIndices(
      self,
      x: int,
      y: int,
      endX: int,
      endY: int,
  ) -> None:
    """
    Calls Qt's 'void SurfaceObject::createCoarseGridlineIndices(int x, int y,
    int endX, int endY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#createCoarseGridlineIndices

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    endX : int
      Passed on as it is.

    endY : int
      Passed on as it is.
    """
    #  void SurfaceObject::createCoarseGridlineIndices(int x, int y, int
    #      endX, int endY)
    self.uglySide.call(
        'ritual_ZN13SurfaceObject27createCoarseGridlineIndicesEiiii',
        x, y, endX, endY,
    )

  def uploadBuffers(self) -> None:
    """
    Calls Qt's 'void SurfaceObject::uploadBuffers()'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#uploadBuffers
    """
    #  void SurfaceObject::uploadBuffers()
    self.uglySide.call('ritual_ZN13SurfaceObject13uploadBuffersEv')

  def gridElementBuf(self) -> int:
    """
    Calls Qt's 'GLuint SurfaceObject::gridElementBuf()'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#gridElementBuf
    """
    #  GLuint SurfaceObject::gridElementBuf()
    return self.uglySide.call('ritual_ZN13SurfaceObject14gridElementBufEv')

  def uvBuf(self) -> int:
    """
    Calls Qt's 'GLuint SurfaceObject::uvBuf()'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#uvBuf
    """
    #  GLuint SurfaceObject::uvBuf()
    ritual = 'ritual_ZN13SurfaceObject5uvBufEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13SurfaceObject5uvBufEv'
    return self.uglySide.call(ritual)

  def gridIndexCount(self) -> int:
    """
    Calls Qt's 'GLuint SurfaceObject::gridIndexCount()'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#gridIndexCount
    """
    #  GLuint SurfaceObject::gridIndexCount()
    return self.uglySide.call('ritual_ZN13SurfaceObject14gridIndexCountEv')

  @overload(int, int)
  def vertexAt(self, column: int, row: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D SurfaceObject::vertexAt(int column, int row)'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#vertexAt

    Parameters
    ----------

    column : int
      Passed on as it is.

    row : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D SurfaceObject::vertexAt(int column, int row)
    address = self.uglySide.call(
        'ritual_ZN13SurfaceObject8vertexAtEii', column, row,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void SurfaceObject::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#clear
    """
    #  void SurfaceObject::clear()
    self.uglySide.call('ritual_ZN13SurfaceObject5clearEv')

  @overload(bool)
  def activateSurfaceTexture(self, value: bool) -> None:
    """
    Calls Qt's 'void SurfaceObject::activateSurfaceTexture(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#activateSurfaceTexture

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void SurfaceObject::activateSurfaceTexture(bool value)
    self.uglySide.call(
        'ritual_ZN13SurfaceObject22activateSurfaceTextureEb', value,
    )

  @overload(int, int)
  def createSmoothNormalBodyLineItem(self, x: int, y: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D SurfaceObject::createSmoothNormalBodyLineItem(int
    x, int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#createSmoothNormalBodyLineItem

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D SurfaceObject::createSmoothNormalBodyLineItem(int x, int y)
    address = self.uglySide.call(
        'ritual_ZN13SurfaceObject30createSmoothNormalBodyLineItemEii', x, y,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int, int)
  def createSmoothNormalUpperLineItem(self, x: int, y: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D SurfaceObject::createSmoothNormalUpperLineItem(int
    x, int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceobject.html#createSmoothNormalUpperLineItem

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D SurfaceObject::createSmoothNormalUpperLineItem(int x, int y)
    address = self.uglySide.call(
        'ritual_ZN13SurfaceObject31createSmoothNormalUpperLineItemEii', x, y,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D, QVector3D, QVector3D)
  def normal(self, a: QVector3D, b: QVector3D, c: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D SurfaceObject::normal(const QVector3D &a, const
    QVector3D &b, const QVector3D &c)'.

    Qt's own words: https://doc.qt.io/qt-6/surfaceobject.html#normal

    Parameters
    ----------

    a : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    b : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    c : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D SurfaceObject::normal(const QVector3D &a, const QVector3D
    #      &b, const QVector3D &c)
    address = self.uglySide.call(
        'ritual_ZN13SurfaceObject6normalERK9QVector3DS2_S2_',
        self._valueOf(a), self._valueOf(b), self._valueOf(c),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @staticmethod
  def checkDirections(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::checkDirections(const QSurfaceDataArray
    &array)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'SurfaceObject.checkDirections' has no cute function yet. Qt's "
        "'void SurfaceObject::checkDirections(const QSurfaceDataArray "
        "&array)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def coarseUVs(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::coarseUVs(const QSurfaceDataArray &dataArray,
    const QSurfaceDataArray &modelArray)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'SurfaceObject.coarseUVs' has no cute function yet. Qt's 'void "
        "SurfaceObject::coarseUVs(const QSurfaceDataArray &dataArray, const "
        "QSurfaceDataArray &modelArray)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def createBuffers(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::createBuffers(const QList<QVector3D> &vertices,
    const QList<QVector2D> &uvs, const QList<QVector3D> &normals, const GLint
    *indices)': names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'SurfaceObject.createBuffers' has no cute function yet. Qt's 'void "
        "SurfaceObject::createBuffers(const QList<QVector3D> &vertices, "
        "const QList<QVector2D> &uvs, const QList<QVector3D> &normals, "
        "const GLint *indices)': names 'GLint', which has no cute class yet."
    )

  @staticmethod
  def createCoarseIndices(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::createCoarseIndices(GLint *indices, int &p, int
    row, int upperRow, int j)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'SurfaceObject.createCoarseIndices' has no cute function yet. Qt's "
        "'void SurfaceObject::createCoarseIndices(GLint *indices, int &p, "
        "int row, int upperRow, int j)': takes a number to change where it "
        "is.")

  @staticmethod
  def createNormals(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::createNormals(int &p, int row, int upperRow,
    int j)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'SurfaceObject.createNormals' has no cute function yet. Qt's 'void "
        "SurfaceObject::createNormals(int &p, int row, int upperRow, int "
        "j)': takes a number to change where it is.")

  @staticmethod
  def createSmoothNormalBodyLine(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::createSmoothNormalBodyLine(int &totalIndex, int
    column)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'SurfaceObject.createSmoothNormalBodyLine' has no cute function "
        "yet. Qt's 'void SurfaceObject::createSmoothNormalBodyLine(int "
        "&totalIndex, int column)': takes a number to change where it is.")

  @staticmethod
  def createSmoothNormalUpperLine(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::createSmoothNormalUpperLine(int &totalIndex)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'SurfaceObject.createSmoothNormalUpperLine' has no cute function "
        "yet. Qt's 'void SurfaceObject::createSmoothNormalUpperLine(int "
        "&totalIndex)': takes a number to change where it is.")

  @staticmethod
  def getNormalizedVertex(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::getNormalizedVertex(const QSurfaceDataItem
    &data, QVector3D &vertex, bool polar, bool flipXZ)': leans on
    'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, float&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.getNormalizedVertex' has no cute function yet. Qt's "
        "'void SurfaceObject::getNormalizedVertex(const QSurfaceDataItem "
        "&data, QVector3D &vertex, bool polar, bool flipXZ)': leans on "
        "'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, "
        "float&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def setUpData(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::setUpData(const QSurfaceDataArray &dataArray,
    const QRect &space, bool changeGeometry, bool polar, bool flipXZ)': leans
    on 'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&,
    float&) const', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.setUpData' has no cute function yet. Qt's 'void "
        "SurfaceObject::setUpData(const QSurfaceDataArray &dataArray, const "
        "QRect &space, bool changeGeometry, bool polar, bool flipXZ)': "
        "leans on 'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, "
        "float&, float&) const', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setUpSmoothData(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::setUpSmoothData(const QSurfaceDataArray
    &dataArray, const QRect &space, bool changeGeometry, bool polar, bool
    flipXZ)': leans on 'Abstract3DRenderer::calculatePolarXZ(QVector3D
    const&, float&, float&) const', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.setUpSmoothData' has no cute function yet. Qt's "
        "'void SurfaceObject::setUpSmoothData(const QSurfaceDataArray "
        "&dataArray, const QRect &space, bool changeGeometry, bool polar, "
        "bool flipXZ)': leans on "
        "'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, "
        "float&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def smoothUVs(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::smoothUVs(const QSurfaceDataArray &dataArray,
    const QSurfaceDataArray &modelArray)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'SurfaceObject.smoothUVs' has no cute function yet. Qt's 'void "
        "SurfaceObject::smoothUVs(const QSurfaceDataArray &dataArray, const "
        "QSurfaceDataArray &modelArray)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def updateCoarseItem(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::updateCoarseItem(const QSurfaceDataArray
    &dataArray, int row, int column, bool polar)': leans on
    'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, float&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.updateCoarseItem' has no cute function yet. Qt's "
        "'void SurfaceObject::updateCoarseItem(const QSurfaceDataArray "
        "&dataArray, int row, int column, bool polar)': leans on "
        "'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, "
        "float&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateCoarseRow(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::updateCoarseRow(const QSurfaceDataArray
    &dataArray, int rowIndex, bool polar)': leans on
    'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, float&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.updateCoarseRow' has no cute function yet. Qt's "
        "'void SurfaceObject::updateCoarseRow(const QSurfaceDataArray "
        "&dataArray, int rowIndex, bool polar)': leans on "
        "'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, "
        "float&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateSmoothItem(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::updateSmoothItem(const QSurfaceDataArray
    &dataArray, int row, int column, bool polar)': leans on
    'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, float&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.updateSmoothItem' has no cute function yet. Qt's "
        "'void SurfaceObject::updateSmoothItem(const QSurfaceDataArray "
        "&dataArray, int row, int column, bool polar)': leans on "
        "'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, "
        "float&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateSmoothRow(*__, **_) -> Never:
    """
    Qt's 'void SurfaceObject::updateSmoothRow(const QSurfaceDataArray
    &dataArray, int startRow, bool polar)': leans on
    'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, float&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceObject.updateSmoothRow' has no cute function yet. Qt's "
        "'void SurfaceObject::updateSmoothRow(const QSurfaceDataArray "
        "&dataArray, int startRow, bool polar)': leans on "
        "'Abstract3DRenderer::calculatePolarXZ(QVector3D const&, float&, "
        "float&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
