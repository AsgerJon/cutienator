"""
ScatterPointBufferHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatterpointbufferhelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ScatterPointBufferHelper to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import AbstractObjectHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import ScatterSeriesRenderCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ScatterSeriesRenderCache = WAIT['ScatterSeriesRenderCache']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScatterPointBufferHelper(AbstractObjectHelper):
  """
  The cute side of Qt's ScatterPointBufferHelper: a plain Python object
  standing in front of one C++ ScatterPointBufferHelper.

  It is built on the cute 'AbstractObjectHelper', as Qt's
  ScatterPointBufferHelper is built on Qt's AbstractObjectHelper, and has
  everything that class has.

  C++ hands a ScatterPointBufferHelper around as a copy, so every C++
  ScatterPointBufferHelper behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ScatterPointBufferHelper that has a ritual and that
  Python can call so far, 4 names in all: 'pointBuf', 'popPoint',
  'setScaleY', 'updateUVs'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ScatterPointBufferHelper::~ScatterPointBufferHelper()': the
    destructor: Python removes its C++ ScatterPointBufferHelper by it, and
    has no other use for it.
  - Qt's 'void
    ScatterPointBufferHelper::createRangeGradientUVs(ScatterSeriesRenderCache
    *cache, QList<QVector2D> &buffered_uvs)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ ScatterPointBufferHelper is created at the first use, not by
    'ScatterPointBufferHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ScatterPointBufferHelper back gives a copy the ritual
    made for Python, in a new cute ScatterPointBufferHelper.
  - Each name of Qt's ScatterPointBufferHelper that has no cute function yet,
    'createRangeGradientUVs', 'load', 'pushPoint', 'update', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterPointBufferHelper'

  #  A C++ ScatterPointBufferHelper Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ScatterPointBufferHelper'

  #  Qt's '~ScatterPointBufferHelper()'. Naming it makes this a value class:
  #  Python owns every C++ ScatterPointBufferHelper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24ScatterPointBufferHelperD1Ev'

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

  @overload(float)
  def setScaleY(self, scale: float) -> None:
    """
    Calls Qt's 'void ScatterPointBufferHelper::setScaleY(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterpointbufferhelper.html#setScaleY

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void ScatterPointBufferHelper::setScaleY(float scale)
    self.uglySide.call(
        'ritual_ZN24ScatterPointBufferHelper9setScaleYEf', scale,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'ScatterPointBufferHelper::ScatterPointBufferHelper()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterpointbufferhelper.html
    """
    #  ScatterPointBufferHelper::ScatterPointBufferHelper()
    self._noteCreation(ScatterPointBufferHelper, lambda: Rituals.call(
        'ritual_ZN24ScatterPointBufferHelperC1Ev',
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

  def pointBuf(self) -> int:
    """
    Calls Qt's 'GLuint ScatterPointBufferHelper::pointBuf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterpointbufferhelper.html#pointBuf
    """
    #  GLuint ScatterPointBufferHelper::pointBuf()
    return self.uglySide.call(
        'ritual_ZN24ScatterPointBufferHelper8pointBufEv',
    )

  def popPoint(self) -> None:
    """
    Calls Qt's 'void ScatterPointBufferHelper::popPoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterpointbufferhelper.html#popPoint
    """
    #  void ScatterPointBufferHelper::popPoint()
    self.uglySide.call('ritual_ZN24ScatterPointBufferHelper8popPointEv')

  @overload(ScatterSeriesRenderCache)
  @overload(NoneType)
  def updateUVs(self, cache: Optional[ScatterSeriesRenderCache]) -> None:
    """
    Calls Qt's 'void
    ScatterPointBufferHelper::updateUVs(ScatterSeriesRenderCache *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterpointbufferhelper.html#updateUVs

    Parameters
    ----------

    cache : Optional[ScatterSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterPointBufferHelper::updateUVs(ScatterSeriesRenderCache
    #      *cache)
    self.uglySide.call(
        'ritual_ZN24ScatterPointBufferHelper9updateUVsEP24ScatterSeriesRend'
        'erCache',
        self._addressOf(cache),
    )

  @staticmethod
  def createRangeGradientUVs(*__, **_) -> Never:
    """
    Qt's 'void
    ScatterPointBufferHelper::createRangeGradientUVs(ScatterSeriesRenderCache
    *cache, QList<QVector2D> &buffered_uvs)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'ScatterPointBufferHelper.createRangeGradientUVs' has no cute "
        "function yet. Qt's 'void "
        "ScatterPointBufferHelper::createRangeGradientUVs(ScatterSeriesRende"
        "rCache *cache, QList<QVector2D> &buffered_uvs)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'void ScatterPointBufferHelper::load(ScatterSeriesRenderCache
    *cache)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'hiddenPos'.
    """
    raise NotImplementedError(
        "'ScatterPointBufferHelper.load' has no cute function yet. Qt's "
        "'void ScatterPointBufferHelper::load(ScatterSeriesRenderCache "
        "*cache)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'hiddenPos'.")

  @staticmethod
  def pushPoint(*__, **_) -> Never:
    """
    Qt's 'void ScatterPointBufferHelper::pushPoint(uint pointIndex)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'hiddenPos'.
    """
    raise NotImplementedError(
        "'ScatterPointBufferHelper.pushPoint' has no cute function yet. "
        "Qt's 'void ScatterPointBufferHelper::pushPoint(uint pointIndex)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'hiddenPos'.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void ScatterPointBufferHelper::update(ScatterSeriesRenderCache
    *cache)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'hiddenPos'.
    """
    raise NotImplementedError(
        "'ScatterPointBufferHelper.update' has no cute function yet. Qt's "
        "'void ScatterPointBufferHelper::update(ScatterSeriesRenderCache "
        "*cache)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'hiddenPos'.")
