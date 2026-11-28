"""
ScatterSeriesRenderCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatterseriesrendercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ScatterSeriesRenderCache to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import SeriesRenderCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QScatter3DSeries, ScatterObjectBufferHelper
  from . import ScatterPointBufferHelper, TextureHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ScatterObjectBufferHelper = WAIT['ScatterObjectBufferHelper']
  ScatterPointBufferHelper = WAIT['ScatterPointBufferHelper']
  TextureHelper = WAIT['TextureHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScatterSeriesRenderCache(SeriesRenderCache):
  """
  The cute side of Qt's ScatterSeriesRenderCache: a plain Python object
  standing in front of one C++ ScatterSeriesRenderCache.

  It is built on the cute 'SeriesRenderCache', as Qt's
  ScatterSeriesRenderCache is built on Qt's SeriesRenderCache, and has
  everything that class has.

  C++ hands a ScatterSeriesRenderCache around as a copy, so every C++
  ScatterSeriesRenderCache behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ScatterSeriesRenderCache that has a ritual and that
  Python can call so far, 18 names in all: 'cleanup', 'series',
  'setItemSize', 'itemSize', 'setSelectionIndexOffset',
  'selectionIndexOffset', 'setStaticBufferDirty', 'staticBufferDirty',
  'oldArraySize', 'setOldArraySize', 'oldMeshFileName', 'setOldMeshFileName',
  'setBufferObject', 'bufferObject', 'setBufferPoints', 'bufferPoints',
  'setVisibilityChanged', 'visibilityChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ScatterSeriesRenderCache::~ScatterSeriesRenderCache()': the
    destructor: Python removes its C++ ScatterSeriesRenderCache by it, and
    has no other use for it.
  - Qt's 'ScatterRenderItemArray &ScatterSeriesRenderCache::renderArray()':
    gives a type Python has no way to take yet.
  - Qt's 'QList<int> &ScatterSeriesRenderCache::updateIndices()': gives a
    type Python has no way to take yet.
  - Qt's 'QList<int> &ScatterSeriesRenderCache::bufferIndices()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 23 functions Qt declares: 1 leans on 'SeriesRenderCache.

  What to expect
  --------------

  - The C++ ScatterSeriesRenderCache is created at the first use, not by
    'ScatterSeriesRenderCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ScatterSeriesRenderCache back gives a copy the ritual
    made for Python, in a new cute ScatterSeriesRenderCache.
  - Each name of Qt's ScatterSeriesRenderCache that has no cute function yet,
    '__init__', 'bufferIndices', 'renderArray', 'updateIndices', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterSeriesRenderCache'

  #  A C++ ScatterSeriesRenderCache Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ScatterSeriesRenderCache'

  #  Qt's '~ScatterSeriesRenderCache()'. Naming it makes this a value class:
  #  Python owns every C++ ScatterSeriesRenderCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24ScatterSeriesRenderCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def series(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *ScatterSeriesRenderCache::series() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#series

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *ScatterSeriesRenderCache::series() const
    address = self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache6seriesEv',
    )
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  def itemSize(self) -> float:
    """
    Calls Qt's 'float ScatterSeriesRenderCache::itemSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#itemSize
    """
    #  float ScatterSeriesRenderCache::itemSize() const
    return self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache8itemSizeEv',
    )

  def selectionIndexOffset(self) -> int:
    """
    Calls Qt's 'int ScatterSeriesRenderCache::selectionIndexOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#selectionIndexOffset
    """
    #  int ScatterSeriesRenderCache::selectionIndexOffset() const
    return self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache20selectionIndexOffsetEv',
    )

  def staticBufferDirty(self) -> bool:
    """
    Calls Qt's 'bool ScatterSeriesRenderCache::staticBufferDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#staticBufferDirty
    """
    #  bool ScatterSeriesRenderCache::staticBufferDirty() const
    return self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache17staticBufferDirtyEv',
    )

  def oldArraySize(self) -> int:
    """
    Calls Qt's 'int ScatterSeriesRenderCache::oldArraySize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#oldArraySize
    """
    #  int ScatterSeriesRenderCache::oldArraySize() const
    return self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache12oldArraySizeEv',
    )

  def oldMeshFileName(self) -> str:
    """
    Calls Qt's 'const QString &ScatterSeriesRenderCache::oldMeshFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#oldMeshFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &ScatterSeriesRenderCache::oldMeshFileName() const
    return self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache15oldMeshFileNameEv',
    )

  def bufferObject(self) -> Optional[ScatterObjectBufferHelper]:
    """
    Calls Qt's 'ScatterObjectBufferHelper
    *ScatterSeriesRenderCache::bufferObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#bufferObject

    Returns
    -------

    Optional[ScatterObjectBufferHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ScatterObjectBufferHelper *ScatterSeriesRenderCache::bufferObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache12bufferObjectEv',
    )
    from . import ScatterObjectBufferHelper
    return ScatterObjectBufferHelper._cuteAt(address)

  def bufferPoints(self) -> Optional[ScatterPointBufferHelper]:
    """
    Calls Qt's 'ScatterPointBufferHelper
    *ScatterSeriesRenderCache::bufferPoints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#bufferPoints

    Returns
    -------

    Optional[ScatterPointBufferHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ScatterPointBufferHelper *ScatterSeriesRenderCache::bufferPoints()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache12bufferPointsEv',
    )
    from . import ScatterPointBufferHelper
    return ScatterPointBufferHelper._cuteAt(address)

  def visibilityChanged(self) -> bool:
    """
    Calls Qt's 'bool ScatterSeriesRenderCache::visibilityChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#visibilityChanged
    """
    #  bool ScatterSeriesRenderCache::visibilityChanged() const
    return self.uglySide.call(
        'ritual_ZNK24ScatterSeriesRenderCache17visibilityChangedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setItemSize(self, size: float) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::setItemSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setItemSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void ScatterSeriesRenderCache::setItemSize(float size)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache11setItemSizeEf', size,
    )

  @overload(int)
  def setSelectionIndexOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::setSelectionIndexOffset(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void ScatterSeriesRenderCache::setSelectionIndexOffset(int offset)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache23setSelectionIndexOffsetEi',
        offset,
    )

  @overload(bool)
  def setStaticBufferDirty(self, state: bool) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::setStaticBufferDirty(bool
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setStaticBufferDirty

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void ScatterSeriesRenderCache::setStaticBufferDirty(bool state)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache20setStaticBufferDirtyEb', state,
    )

  @overload(int)
  def setOldArraySize(self, size: int) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::setOldArraySize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setOldArraySize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void ScatterSeriesRenderCache::setOldArraySize(int size)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache15setOldArraySizeEi', size,
    )

  @overload(str)
  def setOldMeshFileName(self, meshFileName: str) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::setOldMeshFileName(const
    QString &meshFileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setOldMeshFileName

    Parameters
    ----------

    meshFileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ScatterSeriesRenderCache::setOldMeshFileName(const QString
    #      &meshFileName)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache18setOldMeshFileNameERK7QString',
        meshFileName,
    )

  @overload(ScatterObjectBufferHelper)
  @overload(NoneType)
  def setBufferObject(
      self,
      object: Optional[ScatterObjectBufferHelper],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterSeriesRenderCache::setBufferObject(ScatterObjectBufferHelper
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setBufferObject

    Parameters
    ----------

    object : Optional[ScatterObjectBufferHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterSeriesRenderCache::setBufferObject(
    #      ScatterObjectBufferHelper *object)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache15setBufferObjectEP25ScatterObj'
        'ectBufferHelper',
        self._addressOf(object),
    )

  @overload(ScatterPointBufferHelper)
  @overload(NoneType)
  def setBufferPoints(
      self,
      object: Optional[ScatterPointBufferHelper],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterSeriesRenderCache::setBufferPoints(ScatterPointBufferHelper
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setBufferPoints

    Parameters
    ----------

    object : Optional[ScatterPointBufferHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      ScatterSeriesRenderCache::setBufferPoints(ScatterPointBufferHelper
    #      *object)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache15setBufferPointsEP24ScatterPoi'
        'ntBufferHelper',
        self._addressOf(object),
    )

  @overload(bool)
  def setVisibilityChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::setVisibilityChanged(bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#setVisibilityChanged

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void ScatterSeriesRenderCache::setVisibilityChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache20setVisibilityChangedEb',
        changed,
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
    'ScatterSeriesRenderCache::ScatterSeriesRenderCache(QAbstract3DSeries
    *series, Abstract3DRenderer *renderer)': leans on
    'SeriesRenderCache::populate(bool)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ScatterSeriesRenderCache.__init__' has no cute function yet. Qt's "
        "'ScatterSeriesRenderCache::ScatterSeriesRenderCache(QAbstract3DSeri"
        "es *series, Abstract3DRenderer *renderer)': leans on "
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

  @overload(TextureHelper)
  @overload(NoneType)
  def cleanup(self, texHelper: Optional[TextureHelper]) -> None:
    """
    Calls Qt's 'void ScatterSeriesRenderCache::cleanup(TextureHelper
    *texHelper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterseriesrendercache.html#cleanup

    Parameters
    ----------

    texHelper : Optional[TextureHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterSeriesRenderCache::cleanup(TextureHelper *texHelper)
    self.uglySide.call(
        'ritual_ZN24ScatterSeriesRenderCache7cleanupEP13TextureHelper',
        self._addressOf(texHelper),
    )

  @staticmethod
  def bufferIndices(*__, **_) -> Never:
    """
    Qt's 'QList<int> &ScatterSeriesRenderCache::bufferIndices()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ScatterSeriesRenderCache.bufferIndices' has no cute function yet. "
        "Qt's 'QList<int> &ScatterSeriesRenderCache::bufferIndices()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def renderArray(*__, **_) -> Never:
    """
    Qt's 'ScatterRenderItemArray &ScatterSeriesRenderCache::renderArray()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ScatterSeriesRenderCache.renderArray' has no cute function yet. "
        "Qt's 'ScatterRenderItemArray "
        "&ScatterSeriesRenderCache::renderArray()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def updateIndices(*__, **_) -> Never:
    """
    Qt's 'QList<int> &ScatterSeriesRenderCache::updateIndices()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ScatterSeriesRenderCache.updateIndices' has no cute function yet. "
        "Qt's 'QList<int> &ScatterSeriesRenderCache::updateIndices()': "
        "gives a type Python has no way to take yet.")
