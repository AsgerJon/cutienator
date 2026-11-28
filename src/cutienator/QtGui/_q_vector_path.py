"""
QVectorPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qvectorpath_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVectorPath to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QPaintEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from . import QPaintEngineEx, QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEngineEx = WAIT['QPaintEngineEx']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVectorPath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVectorPath: a plain Python object standing in front
  of one C++ QVectorPath.

  What exists
  -----------

  Every function of Qt's QVectorPath that has a ritual and that Python can
  call so far, 16 names in all: 'controlPointRect', 'shape', 'isConvex',
  'isCurved', 'isCacheable', 'hasImplicitClose', 'hasExplicitOpen',
  'hasWindingFill', 'makeCacheable', 'hints', 'isEmpty', 'elementCount',
  'convertToPainterPath', 'polygonFlags', 'lookupCacheData', 'isRect'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVectorPath::QVectorPath(const qreal *points, int count, const
    QPainterPath::ElementType *elements, uint hints)': names 'qreal', which
    has no cute class yet.
  - Qt's 'QVectorPath::~QVectorPath()': the destructor: Python never removes
    a C++ QVectorPath.
  - Qt's 'const QPainterPath::ElementType *QVectorPath::elements() const':
    gives 'QPainterPath::ElementType', which has no cute class yet.
  - Qt's 'const qreal *QVectorPath::points() const': gives 'double', which
    has no cute class yet.
  - Qt's 'CacheEntry *QVectorPath::addCacheData(QPaintEngineEx *engine, void
    *data, qvectorpath_cache_cleanup cleanup) const': names 'void', which has
    no cute class yet.

  What has no ritual
  ------------------

  5 of the 26 functions Qt declares: 4 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QVectorPath is created at the first use, not by
    'QVectorPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVectorPath.
  - Each name of Qt's QVectorPath that has no cute function yet, '__init__',
    'addCacheData', 'elements', 'points', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QVectorPath, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Hint(CuteNum):
    """
    The enum 'QVectorPath::Hint' of Qt, with the 20 names Qt gives in it.
    """

    AreaShapeMask = Kee[int](1)
    NonConvexShapeMask = Kee[int](2)
    CurvedShapeMask = Kee[int](4)
    LinesShapeMask = Kee[int](8)
    RectangleShapeMask = Kee[int](16)
    ShapeMask = Kee[int](31)
    LinesHint = Kee[int](8)
    RectangleHint = Kee[int](17)
    EllipseHint = Kee[int](5)
    ConvexPolygonHint = Kee[int](1)
    PolygonHint = Kee[int](3)
    RoundedRectHint = Kee[int](5)
    ArbitraryShapeHint = Kee[int](7)
    IsCachedHint = Kee[int](256)
    ShouldUseCacheHint = Kee[int](512)
    ControlPointRect = Kee[int](1024)
    OddEvenFill = Kee[int](4096)
    WindingFill = Kee[int](8192)
    ImplicitClose = Kee[int](16384)
    ExplicitOpen = Kee[int](32768)

  #  The classes Qt writes inside QVectorPath, each a class in here as in
  #  C++.

  class CacheEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVectorPath::CacheEntry: a plain Python object
    standing in front of one C++ QVectorPath::CacheEntry.

    C++ hands a QVectorPath::CacheEntry around as a copy, so every C++
    QVectorPath::CacheEntry behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QVectorPath::CacheEntry yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVectorPath::CacheEntry::~CacheEntry()': the destructor: Python
      removes its C++ QVectorPath::CacheEntry by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QVectorPath::CacheEntry is created at the first use, not by
      'QVectorPath::CacheEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVectorPath::CacheEntry back gives a copy the
      ritual made for Python, in a new cute QVectorPath::CacheEntry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVectorPath::CacheEntry'

    #  Qt's '~QVectorPath::CacheEntry()'. Naming it makes this a value class:
    #  Python owns every C++ QVectorPath::CacheEntry behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QVectorPath10CacheEntryD1Ev'

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
  @overload(QPaintEngine.PolygonDrawMode)
  def polygonFlags(mode: QPaintEngine.PolygonDrawMode) -> int:
    """
    Calls Qt's 'uint QVectorPath::polygonFlags(QPaintEngine::PolygonDrawMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#polygonFlags

    Parameters
    ----------

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  uint QVectorPath::polygonFlags(QPaintEngine::PolygonDrawMode mode)
    return Rituals.call(
        'ritual_ZN11QVectorPath12polygonFlagsEN12QPaintEngine15PolygonDrawM'
        'odeE',
        mode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVectorPath'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def controlPointRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QVectorPath::controlPointRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#controlPointRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QVectorPath::controlPointRect() const
    address = self.uglySide.call(
        'ritual_ZNK11QVectorPath16controlPointRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> Hint:
    """
    Calls Qt's 'Hint QVectorPath::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#shape

    Returns
    -------

    Hint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Hint(number)' gives.
    """
    #  Hint QVectorPath::shape() const
    return QVectorPath.Hint(self.uglySide.call(
        'ritual_ZNK11QVectorPath5shapeEv',
    ))

  def isConvex(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::isConvex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#isConvex
    """
    #  bool QVectorPath::isConvex() const
    return self.uglySide.call('ritual_ZNK11QVectorPath8isConvexEv')

  def isCurved(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::isCurved() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#isCurved
    """
    #  bool QVectorPath::isCurved() const
    return self.uglySide.call('ritual_ZNK11QVectorPath8isCurvedEv')

  def isCacheable(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::isCacheable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#isCacheable
    """
    #  bool QVectorPath::isCacheable() const
    return self.uglySide.call('ritual_ZNK11QVectorPath11isCacheableEv')

  def hasImplicitClose(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::hasImplicitClose() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#hasImplicitClose
    """
    #  bool QVectorPath::hasImplicitClose() const
    return self.uglySide.call('ritual_ZNK11QVectorPath16hasImplicitCloseEv')

  def hasExplicitOpen(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::hasExplicitOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#hasExplicitOpen
    """
    #  bool QVectorPath::hasExplicitOpen() const
    return self.uglySide.call('ritual_ZNK11QVectorPath15hasExplicitOpenEv')

  def hasWindingFill(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::hasWindingFill() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#hasWindingFill
    """
    #  bool QVectorPath::hasWindingFill() const
    return self.uglySide.call('ritual_ZNK11QVectorPath14hasWindingFillEv')

  def hints(self) -> int:
    """
    Calls Qt's 'uint QVectorPath::hints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#hints
    """
    #  uint QVectorPath::hints() const
    return self.uglySide.call('ritual_ZNK11QVectorPath5hintsEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#isEmpty
    """
    #  bool QVectorPath::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QVectorPath7isEmptyEv')

  def elementCount(self) -> int:
    """
    Calls Qt's 'int QVectorPath::elementCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#elementCount
    """
    #  int QVectorPath::elementCount() const
    return self.uglySide.call('ritual_ZNK11QVectorPath12elementCountEv')

  def convertToPainterPath(self) -> QPainterPath:
    """
    Calls Qt's 'const QPainterPath QVectorPath::convertToPainterPath()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvectorpath.html#convertToPainterPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  const QPainterPath QVectorPath::convertToPainterPath() const
    address = self.uglySide.call(
        'ritual_ZNK11QVectorPath20convertToPainterPathEv',
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPaintEngineEx)
  @overload(NoneType)
  def lookupCacheData(
      self,
      engine: Optional[QPaintEngineEx],
  ) -> Optional[CacheEntry]:
    """
    Calls Qt's 'CacheEntry *QVectorPath::lookupCacheData(QPaintEngineEx
    *engine) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#lookupCacheData

    Parameters
    ----------

    engine : Optional[QPaintEngineEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[CacheEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CacheEntry *QVectorPath::lookupCacheData(QPaintEngineEx *engine) const
    address = self.uglySide.call(
        'ritual_ZNK11QVectorPath15lookupCacheDataEP14QPaintEngineEx',
        self._addressOf(engine),
    )
    return QVectorPath.CacheEntry._cuteAt(address)

  def isRect(self) -> bool:
    """
    Calls Qt's 'bool QVectorPath::isRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#isRect
    """
    #  bool QVectorPath::isRect() const
    return self.uglySide.call('ritual_ZNK11QVectorPath6isRectEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QVectorPath::QVectorPath(const qreal *points, int count, const
    QPainterPath::ElementType *elements, uint hints)': names 'qreal', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QVectorPath.__init__' has no cute function yet. Qt's "
        "'QVectorPath::QVectorPath(const qreal *points, int count, const "
        "QPainterPath::ElementType *elements, uint hints)': names 'qreal', "
        "which has no cute class yet.")

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

  def makeCacheable(self) -> None:
    """
    Calls Qt's 'void QVectorPath::makeCacheable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvectorpath.html#makeCacheable
    """
    #  void QVectorPath::makeCacheable() const
    self.uglySide.call('ritual_ZNK11QVectorPath13makeCacheableEv')

  @staticmethod
  def addCacheData(*__, **_) -> Never:
    """
    Qt's 'CacheEntry *QVectorPath::addCacheData(QPaintEngineEx *engine, void
    *data, qvectorpath_cache_cleanup cleanup) const': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QVectorPath.addCacheData' has no cute function yet. Qt's "
        "'CacheEntry *QVectorPath::addCacheData(QPaintEngineEx *engine, "
        "void *data, qvectorpath_cache_cleanup cleanup) const': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def elements(*__, **_) -> Never:
    """
    Qt's 'const QPainterPath::ElementType *QVectorPath::elements() const':
    gives 'QPainterPath::ElementType', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QVectorPath.elements' has no cute function yet. Qt's 'const "
        "QPainterPath::ElementType *QVectorPath::elements() const': gives "
        "'QPainterPath::ElementType', which has no cute class yet.")

  @staticmethod
  def points(*__, **_) -> Never:
    """
    Qt's 'const qreal *QVectorPath::points() const': gives 'double', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QVectorPath.points' has no cute function yet. Qt's 'const qreal "
        "*QVectorPath::points() const': gives 'double', which has no cute "
        "class yet.")
