"""
SurfaceSeriesRenderCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceseriesrendercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SurfaceSeriesRenderCache to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import SeriesRenderCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from ..QtGui import QMatrix4x4
  from . import QSurface3DSeries, SelectionPointer, SurfaceObject
  from . import TextureHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QRect = WAIT['QRect']
  SelectionPointer = WAIT['SelectionPointer']
  TextureHelper = WAIT['TextureHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SurfaceSeriesRenderCache(SeriesRenderCache):
  """
  The cute side of Qt's SurfaceSeriesRenderCache: a plain Python object
  standing in front of one C++ SurfaceSeriesRenderCache.

  It is built on the cute 'SeriesRenderCache', as Qt's
  SurfaceSeriesRenderCache is built on Qt's SeriesRenderCache, and has
  everything that class has.

  C++ hands a SurfaceSeriesRenderCache around as a copy, so every C++
  SurfaceSeriesRenderCache behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's SurfaceSeriesRenderCache that has a ritual and that
  Python can call so far, 32 names in all: 'populate', 'cleanup',
  'surfaceVisible', 'surfaceGridVisible', 'isFlatShadingEnabled',
  'setFlatShadingEnabled', 'setFlatChangeAllowed', 'surfaceObject',
  'sliceSurfaceObject', 'sampleSpace', 'setSampleSpace', 'series',
  'renderable', 'setSelectionTexture', 'selectionTexture',
  'setSelectionIdRange', 'selectionIdStart', 'isWithinIdRange',
  'isFlatStatusDirty', 'setFlatStatusDirty', 'setMVPMatrix', 'MVPMatrix',
  'setSliceSelectionPointer', 'sliceSelectionPointer',
  'setMainSelectionPointer', 'mainSelectionPointer',
  'setSlicePointerActivity', 'slicePointerActive', 'setMainPointerActivity',
  'mainPointerActive', 'setSurfaceTexture', 'surfaceTexture'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SurfaceSeriesRenderCache::~SurfaceSeriesRenderCache()': the
    destructor: Python removes its C++ SurfaceSeriesRenderCache by it, and
    has no other use for it.
  - Qt's 'QSurfaceDataArray &SurfaceSeriesRenderCache::dataArray()': gives a
    type Python has no way to take yet.
  - Qt's 'QSurfaceDataArray &SurfaceSeriesRenderCache::sliceDataArray()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 36 functions Qt declares: 1 leans on 'SeriesRenderCache.

  What to expect
  --------------

  - The C++ SurfaceSeriesRenderCache is created at the first use, not by
    'SurfaceSeriesRenderCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a SurfaceSeriesRenderCache back gives a copy the ritual
    made for Python, in a new cute SurfaceSeriesRenderCache.
  - Each name of Qt's SurfaceSeriesRenderCache that has no cute function yet,
    '__init__', 'dataArray', 'sliceDataArray', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SurfaceSeriesRenderCache'

  #  A C++ SurfaceSeriesRenderCache Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SurfaceSeriesRenderCache'

  #  Qt's '~SurfaceSeriesRenderCache()'. Naming it makes this a value class:
  #  Python owns every C++ SurfaceSeriesRenderCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24SurfaceSeriesRenderCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def surfaceVisible(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::surfaceVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#surfaceVisible
    """
    #  bool SurfaceSeriesRenderCache::surfaceVisible() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache14surfaceVisibleEv',
    )

  def surfaceGridVisible(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::surfaceGridVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#surfaceGridVisible
    """
    #  bool SurfaceSeriesRenderCache::surfaceGridVisible() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache18surfaceGridVisibleEv',
    )

  def isFlatShadingEnabled(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::isFlatShadingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#isFlatShadingEnabled
    """
    #  bool SurfaceSeriesRenderCache::isFlatShadingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache20isFlatShadingEnabledEv',
    )

  def sampleSpace(self) -> QRect:
    """
    Calls Qt's 'const QRect &SurfaceSeriesRenderCache::sampleSpace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#sampleSpace

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  const QRect &SurfaceSeriesRenderCache::sampleSpace() const
    address = self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache11sampleSpaceEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def series(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *SurfaceSeriesRenderCache::series() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#series

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *SurfaceSeriesRenderCache::series() const
    address = self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache6seriesEv',
    )
    from . import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def renderable(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::renderable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#renderable
    """
    #  bool SurfaceSeriesRenderCache::renderable() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache10renderableEv',
    )

  def selectionTexture(self) -> int:
    """
    Calls Qt's 'GLuint SurfaceSeriesRenderCache::selectionTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#selectionTexture
    """
    #  GLuint SurfaceSeriesRenderCache::selectionTexture() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache16selectionTextureEv',
    )

  def selectionIdStart(self) -> int:
    """
    Calls Qt's 'uint SurfaceSeriesRenderCache::selectionIdStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#selectionIdStart
    """
    #  uint SurfaceSeriesRenderCache::selectionIdStart() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache16selectionIdStartEv',
    )

  @overload(int)
  def isWithinIdRange(self, selection: int) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::isWithinIdRange(uint
    selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#isWithinIdRange

    Parameters
    ----------

    selection : int
      Passed on as it is.
    """
    #  bool SurfaceSeriesRenderCache::isWithinIdRange(uint selection) const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache15isWithinIdRangeEj', selection,
    )

  def isFlatStatusDirty(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::isFlatStatusDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#isFlatStatusDirty
    """
    #  bool SurfaceSeriesRenderCache::isFlatStatusDirty() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache17isFlatStatusDirtyEv',
    )

  def sliceSelectionPointer(self) -> Optional[SelectionPointer]:
    """
    Calls Qt's 'SelectionPointer
    *SurfaceSeriesRenderCache::sliceSelectionPointer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html

    Returns
    -------

    Optional[SelectionPointer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SelectionPointer *SurfaceSeriesRenderCache::sliceSelectionPointer()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache21sliceSelectionPointerEv',
    )
    from . import SelectionPointer
    return SelectionPointer._cuteAt(address)

  def mainSelectionPointer(self) -> Optional[SelectionPointer]:
    """
    Calls Qt's 'SelectionPointer
    *SurfaceSeriesRenderCache::mainSelectionPointer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#mainSelectionPointer

    Returns
    -------

    Optional[SelectionPointer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SelectionPointer *SurfaceSeriesRenderCache::mainSelectionPointer()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache20mainSelectionPointerEv',
    )
    from . import SelectionPointer
    return SelectionPointer._cuteAt(address)

  def slicePointerActive(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::slicePointerActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#slicePointerActive
    """
    #  bool SurfaceSeriesRenderCache::slicePointerActive() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache18slicePointerActiveEv',
    )

  def mainPointerActive(self) -> bool:
    """
    Calls Qt's 'bool SurfaceSeriesRenderCache::mainPointerActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#mainPointerActive
    """
    #  bool SurfaceSeriesRenderCache::mainPointerActive() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache17mainPointerActiveEv',
    )

  def surfaceTexture(self) -> int:
    """
    Calls Qt's 'GLuint SurfaceSeriesRenderCache::surfaceTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#surfaceTexture
    """
    #  GLuint SurfaceSeriesRenderCache::surfaceTexture() const
    return self.uglySide.call(
        'ritual_ZNK24SurfaceSeriesRenderCache14surfaceTextureEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFlatShadingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setFlatShadingEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setFlatShadingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache21setFlatShadingEnabledEb',
        enabled,
    )

  @overload(bool)
  def setFlatChangeAllowed(self, allowed: bool) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setFlatChangeAllowed(bool
    allowed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setFlatChangeAllowed

    Parameters
    ----------

    allowed : bool
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setFlatChangeAllowed(bool allowed)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache20setFlatChangeAllowedEb',
        allowed,
    )

  @overload(QRect)
  def setSampleSpace(self, sampleSpace: QRect) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setSampleSpace(const QRect
    &sampleSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setSampleSpace

    Parameters
    ----------

    sampleSpace : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void SurfaceSeriesRenderCache::setSampleSpace(const QRect
    #      &sampleSpace)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache14setSampleSpaceERK5QRect',
        self._valueOf(sampleSpace),
    )

  @overload(int)
  def setSelectionTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setSelectionTexture(GLuint
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setSelectionTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setSelectionTexture(GLuint texture)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache19setSelectionTextureEj',
        texture,
    )

  @overload(int, int)
  def setSelectionIdRange(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setSelectionIdRange(uint
    start, uint end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setSelectionIdRange

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setSelectionIdRange(uint start, uint
    #      end)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache19setSelectionIdRangeEjj',
        start, end,
    )

  @overload(bool)
  def setFlatStatusDirty(self, status: bool) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setFlatStatusDirty(bool
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setFlatStatusDirty

    Parameters
    ----------

    status : bool
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setFlatStatusDirty(bool status)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache18setFlatStatusDirtyEb', status,
    )

  @overload(QMatrix4x4)
  def setMVPMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setMVPMatrix(const QMatrix4x4
    &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setMVPMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void SurfaceSeriesRenderCache::setMVPMatrix(const QMatrix4x4 &matrix)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache12setMVPMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
    )

  @overload(SelectionPointer)
  @overload(NoneType)
  def setSliceSelectionPointer(
      self,
      pointer: Optional[SelectionPointer],
  ) -> None:
    """
    Calls Qt's 'void
    SurfaceSeriesRenderCache::setSliceSelectionPointer(SelectionPointer
    *pointer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html

    Parameters
    ----------

    pointer : Optional[SelectionPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SurfaceSeriesRenderCache::setSliceSelectionPointer(
    #      SelectionPointer *pointer)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache24setSliceSelectionPointerEP16S'
        'electionPointer',
        self._addressOf(pointer),
    )

  @overload(SelectionPointer)
  @overload(NoneType)
  def setMainSelectionPointer(
      self,
      pointer: Optional[SelectionPointer],
  ) -> None:
    """
    Calls Qt's 'void
    SurfaceSeriesRenderCache::setMainSelectionPointer(SelectionPointer
    *pointer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html

    Parameters
    ----------

    pointer : Optional[SelectionPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      SurfaceSeriesRenderCache::setMainSelectionPointer(SelectionPointer
    #      *pointer)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache23setMainSelectionPointerEP16Se'
        'lectionPointer',
        self._addressOf(pointer),
    )

  @overload(bool)
  def setSlicePointerActivity(self, activity: bool) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setSlicePointerActivity(bool
    activity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html

    Parameters
    ----------

    activity : bool
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setSlicePointerActivity(bool activity)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache23setSlicePointerActivityEb',
        activity,
    )

  @overload(bool)
  def setMainPointerActivity(self, activity: bool) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setMainPointerActivity(bool
    activity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html

    Parameters
    ----------

    activity : bool
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setMainPointerActivity(bool activity)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache22setMainPointerActivityEb',
        activity,
    )

  @overload(int)
  def setSurfaceTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::setSurfaceTexture(GLuint
    texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#setSurfaceTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::setSurfaceTexture(GLuint texture)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache17setSurfaceTextureEj', texture,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'SurfaceSeriesRenderCache::SurfaceSeriesRenderCache(QAbstract3DSeries
    *series, Surface3DRenderer *renderer)': leans on
    'SeriesRenderCache::populate(bool)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SurfaceSeriesRenderCache.__init__' has no cute function yet. Qt's "
        "'SurfaceSeriesRenderCache::SurfaceSeriesRenderCache(QAbstract3DSeri"
        "es *series, Surface3DRenderer *renderer)': leans on "
        "'SeriesRenderCache::populate(bool)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(bool)
  def populate(self, newSeries: bool) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::populate(bool newSeries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#populate

    Parameters
    ----------

    newSeries : bool
      Passed on as it is.
    """
    #  void SurfaceSeriesRenderCache::populate(bool newSeries)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache8populateEb', newSeries,
    )

  @overload(TextureHelper)
  @overload(NoneType)
  def cleanup(self, texHelper: Optional[TextureHelper]) -> None:
    """
    Calls Qt's 'void SurfaceSeriesRenderCache::cleanup(TextureHelper
    *texHelper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#cleanup

    Parameters
    ----------

    texHelper : Optional[TextureHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SurfaceSeriesRenderCache::cleanup(TextureHelper *texHelper)
    self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache7cleanupEP13TextureHelper',
        self._addressOf(texHelper),
    )

  def surfaceObject(self) -> Optional[SurfaceObject]:
    """
    Calls Qt's 'SurfaceObject *SurfaceSeriesRenderCache::surfaceObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#surfaceObject

    Returns
    -------

    Optional[SurfaceObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SurfaceObject *SurfaceSeriesRenderCache::surfaceObject()
    address = self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache13surfaceObjectEv',
    )
    from . import SurfaceObject
    return SurfaceObject._cuteAt(address)

  def sliceSurfaceObject(self) -> Optional[SurfaceObject]:
    """
    Calls Qt's 'SurfaceObject
    *SurfaceSeriesRenderCache::sliceSurfaceObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#sliceSurfaceObject

    Returns
    -------

    Optional[SurfaceObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SurfaceObject *SurfaceSeriesRenderCache::sliceSurfaceObject()
    address = self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache18sliceSurfaceObjectEv',
    )
    from . import SurfaceObject
    return SurfaceObject._cuteAt(address)

  def MVPMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'const QMatrix4x4 &SurfaceSeriesRenderCache::MVPMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surfaceseriesrendercache.html#MVPMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  const QMatrix4x4 &SurfaceSeriesRenderCache::MVPMatrix()
    address = self.uglySide.call(
        'ritual_ZN24SurfaceSeriesRenderCache9MVPMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  def dataArray(*__, **_) -> Never:
    """
    Qt's 'QSurfaceDataArray &SurfaceSeriesRenderCache::dataArray()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SurfaceSeriesRenderCache.dataArray' has no cute function yet. "
        "Qt's 'QSurfaceDataArray &SurfaceSeriesRenderCache::dataArray()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def sliceDataArray(*__, **_) -> Never:
    """
    Qt's 'QSurfaceDataArray &SurfaceSeriesRenderCache::sliceDataArray()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SurfaceSeriesRenderCache.sliceDataArray' has no cute function "
        "yet. Qt's 'QSurfaceDataArray "
        "&SurfaceSeriesRenderCache::sliceDataArray()': gives a type Python "
        "has no way to take yet.")
