"""
ScatterObjectBufferHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatterobjectbufferhelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ScatterObjectBufferHelper to be private: it declares the class in
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


class ScatterObjectBufferHelper(AbstractObjectHelper):
  """
  The cute side of Qt's ScatterObjectBufferHelper: a plain Python object
  standing in front of one C++ ScatterObjectBufferHelper.

  It is built on the cute 'AbstractObjectHelper', as Qt's
  ScatterObjectBufferHelper is built on Qt's AbstractObjectHelper, and has
  everything that class has.

  C++ hands a ScatterObjectBufferHelper around as a copy, so every C++
  ScatterObjectBufferHelper behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ScatterObjectBufferHelper that has a ritual and that
  Python can call so far, 2 names in all: 'updateUVs', 'setScaleY'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ScatterObjectBufferHelper::~ScatterObjectBufferHelper()': the
    destructor: Python removes its C++ ScatterObjectBufferHelper by it, and
    has no other use for it.
  - Qt's 'uint ScatterObjectBufferHelper::createRangeGradientUVs(
    ScatterSeriesRenderCache *cache, QList<QVector2D> &buffered_uvs)': takes
    a type Python has no way to hand over yet.
  - Qt's 'uint ScatterObjectBufferHelper::createObjectGradientUVs(
    ScatterSeriesRenderCache *cache, QList<QVector2D> &buffered_uvs, const
    QList<QVector3D> &indexed_vertices)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 leans on 'ScatterObjectBufferHelper.

  What to expect
  --------------

  - The C++ ScatterObjectBufferHelper is created at the first use, not by
    'ScatterObjectBufferHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ScatterObjectBufferHelper back gives a copy the
    ritual made for Python, in a new cute ScatterObjectBufferHelper.
  - Each name of Qt's ScatterObjectBufferHelper that has no cute function
    yet, 'createObjectGradientUVs', 'createRangeGradientUVs', 'fullLoad',
    'update', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterObjectBufferHelper'

  #  A C++ ScatterObjectBufferHelper Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ScatterObjectBufferHelper'

  #  Qt's '~ScatterObjectBufferHelper()'. Naming it makes this a value class:
  #  Python owns every C++ ScatterObjectBufferHelper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25ScatterObjectBufferHelperD1Ev'

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
    Calls Qt's 'void ScatterObjectBufferHelper::setScaleY(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterobjectbufferhelper.html#setScaleY

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void ScatterObjectBufferHelper::setScaleY(float scale)
    self.uglySide.call(
        'ritual_ZN25ScatterObjectBufferHelper9setScaleYEf', scale,
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
    'ScatterObjectBufferHelper::ScatterObjectBufferHelper()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterobjectbufferhelper.html
    """
    #  ScatterObjectBufferHelper::ScatterObjectBufferHelper()
    self._noteCreation(ScatterObjectBufferHelper, lambda: Rituals.call(
        'ritual_ZN25ScatterObjectBufferHelperC1Ev',
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

  @overload(ScatterSeriesRenderCache)
  @overload(NoneType)
  def updateUVs(self, cache: Optional[ScatterSeriesRenderCache]) -> None:
    """
    Calls Qt's 'void
    ScatterObjectBufferHelper::updateUVs(ScatterSeriesRenderCache *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterobjectbufferhelper.html#updateUVs

    Parameters
    ----------

    cache : Optional[ScatterSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterObjectBufferHelper::updateUVs(ScatterSeriesRenderCache
    #      *cache)
    self.uglySide.call(
        'ritual_ZN25ScatterObjectBufferHelper9updateUVsEP24ScatterSeriesRen'
        'derCache',
        self._addressOf(cache),
    )

  @staticmethod
  def createObjectGradientUVs(*__, **_) -> Never:
    """
    Qt's 'uint ScatterObjectBufferHelper::createObjectGradientUVs(
    ScatterSeriesRenderCache *cache, QList<QVector2D> &buffered_uvs, const
    QList<QVector3D> &indexed_vertices)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'ScatterObjectBufferHelper.createObjectGradientUVs' has no cute "
        "function yet. Qt's 'uint "
        "ScatterObjectBufferHelper::createObjectGradientUVs(ScatterSeriesRen"
        "derCache *cache, QList<QVector2D> &buffered_uvs, const "
        "QList<QVector3D> &indexed_vertices)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def createRangeGradientUVs(*__, **_) -> Never:
    """
    Qt's 'uint ScatterObjectBufferHelper::createRangeGradientUVs(
    ScatterSeriesRenderCache *cache, QList<QVector2D> &buffered_uvs)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ScatterObjectBufferHelper.createRangeGradientUVs' has no cute "
        "function yet. Qt's 'uint "
        "ScatterObjectBufferHelper::createRangeGradientUVs(ScatterSeriesRend"
        "erCache *cache, QList<QVector2D> &buffered_uvs)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fullLoad(*__, **_) -> Never:
    """
    Qt's 'void ScatterObjectBufferHelper::fullLoad(ScatterSeriesRenderCache
    *cache, qreal dotScale)': leans on
    'ScatterObjectBufferHelper::itemScaler', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ScatterObjectBufferHelper.fullLoad' has no cute function yet. "
        "Qt's 'void "
        "ScatterObjectBufferHelper::fullLoad(ScatterSeriesRenderCache "
        "*cache, qreal dotScale)': leans on "
        "'ScatterObjectBufferHelper::itemScaler', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void ScatterObjectBufferHelper::update(ScatterSeriesRenderCache
    *cache, qreal dotScale)': leans on
    'ScatterObjectBufferHelper::itemScaler', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ScatterObjectBufferHelper.update' has no cute function yet. Qt's "
        "'void ScatterObjectBufferHelper::update(ScatterSeriesRenderCache "
        "*cache, qreal dotScale)': leans on "
        "'ScatterObjectBufferHelper::itemScaler', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
