"""
QLottieRasterRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottierasterrenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieRasterRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QLottieRenderer
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QLottieBase, QLottieBasicTransform, QLottieEllipse
  from . import QLottieFill, QLottieFillEffect, QLottieFreeFormShape
  from . import QLottieGFill, QLottieImage, QLottieLayer, QLottiePolyStar
  from . import QLottiePrecomposition, QLottieRect, QLottieRepeater
  from . import QLottieRound, QLottieShapeTransform, QLottieSolidLayer
  from . import QLottieStroke, QLottieTextLayer, QLottieTrimPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLottieBase = WAIT['QLottieBase']
  QLottieBasicTransform = WAIT['QLottieBasicTransform']
  QLottieEllipse = WAIT['QLottieEllipse']
  QLottieFill = WAIT['QLottieFill']
  QLottieFillEffect = WAIT['QLottieFillEffect']
  QLottieFreeFormShape = WAIT['QLottieFreeFormShape']
  QLottieGFill = WAIT['QLottieGFill']
  QLottieImage = WAIT['QLottieImage']
  QLottieLayer = WAIT['QLottieLayer']
  QLottiePolyStar = WAIT['QLottiePolyStar']
  QLottiePrecomposition = WAIT['QLottiePrecomposition']
  QLottieRect = WAIT['QLottieRect']
  QLottieRepeater = WAIT['QLottieRepeater']
  QLottieRound = WAIT['QLottieRound']
  QLottieShapeTransform = WAIT['QLottieShapeTransform']
  QLottieSolidLayer = WAIT['QLottieSolidLayer']
  QLottieStroke = WAIT['QLottieStroke']
  QLottieTextLayer = WAIT['QLottieTextLayer']
  QLottieTrimPath = WAIT['QLottieTrimPath']


class QLottieRasterRenderer(QLottieRenderer):
  """
  The cute side of Qt's QLottieRasterRenderer: a plain Python object standing
  in front of one C++ QLottieRasterRenderer.

  It is built on the cute 'QLottieRenderer', as Qt's QLottieRasterRenderer is
  built on Qt's QLottieRenderer, and has everything that class has.

  C++ hands a QLottieRasterRenderer around as a copy, so every C++
  QLottieRasterRenderer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieRasterRenderer that has a ritual and that
  Python can call so far, 5 names in all: 'saveState', 'restoreState',
  'render', 'renderPathElements', 'applyRepeaterTransform'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieRasterRenderer::~QLottieRasterRenderer()': the destructor:
    Python removes its C++ QLottieRasterRenderer by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 24 functions Qt declares: 1 leans on 'QLottieRasterRenderer.

  What to expect
  --------------

  - The C++ QLottieRasterRenderer is created at the first use, not by
    'QLottieRasterRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieRasterRenderer back gives a copy the ritual
    made for Python, in a new cute QLottieRasterRenderer.
  - Each name of Qt's QLottieRasterRenderer that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QLottieRasterRenderer'

  #  A C++ QLottieRasterRenderer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRasterRenderer'

  #  Qt's '~QLottieRasterRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QLottieRasterRenderer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QLottieRasterRendererD1Ev'

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
    Qt's 'QLottieRasterRenderer::QLottieRasterRenderer(QPainter *m_painter)':
    leans on 'QLottieRasterRenderer::render(QLottieFill const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QLottieRasterRenderer.__init__' has no cute function yet. Qt's "
        "'QLottieRasterRenderer::QLottieRasterRenderer(QPainter "
        "*m_painter)': leans on 'QLottieRasterRenderer::render(QLottieFill "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def saveState(self) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::saveState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierasterrenderer.html#saveState
    """
    #  void QLottieRasterRenderer::saveState()
    self.uglySide.call('ritual_ZN21QLottieRasterRenderer9saveStateEv')

  def restoreState(self) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::restoreState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierasterrenderer.html#restoreState
    """
    #  void QLottieRasterRenderer::restoreState()
    self.uglySide.call('ritual_ZN21QLottieRasterRenderer12restoreStateEv')

  @overload(QLottiePrecomposition)
  def render(self, precomp: QLottiePrecomposition) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const
    QLottiePrecomposition &precomp)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    precomp : QLottiePrecomposition
      Passed on as a value: Qt reads the C++ QLottiePrecomposition, which
      stays Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottiePrecomposition
    #      &precomp)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK21QLottiePrecomposition',
        self._valueOf(precomp),
    )

  @overload(QLottieSolidLayer)
  def render(self, layer: QLottieSolidLayer) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieSolidLayer
    &layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    layer : QLottieSolidLayer
      Passed on as a value: Qt reads the C++ QLottieSolidLayer, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieSolidLayer &layer)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK17QLottieSolidLayer',
        self._valueOf(layer),
    )

  @overload(QLottieTextLayer)
  def render(self, layer: QLottieTextLayer) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieTextLayer
    &layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    layer : QLottieTextLayer
      Passed on as a value: Qt reads the C++ QLottieTextLayer, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieTextLayer &layer)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK16QLottieTextLayer',
        self._valueOf(layer),
    )

  @overload(QLottieLayer)
  def render(self, layer: QLottieLayer) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieLayer
    &layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    layer : QLottieLayer
      Passed on as a value: Qt reads the C++ QLottieLayer, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieLayer &layer)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK12QLottieLayer',
        self._valueOf(layer),
    )

  @overload(QLottieRect)
  def render(self, rect: QLottieRect) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    rect : QLottieRect
      Passed on as a value: Qt reads the C++ QLottieRect, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieRect &rect)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK11QLottieRect',
        self._valueOf(rect),
    )

  @overload(QLottieEllipse)
  def render(self, ellipse: QLottieEllipse) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieEllipse
    &ellipse)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    ellipse : QLottieEllipse
      Passed on as a value: Qt reads the C++ QLottieEllipse, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieEllipse &ellipse)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK14QLottieEllipse',
        self._valueOf(ellipse),
    )

  @overload(QLottiePolyStar)
  def render(self, star: QLottiePolyStar) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottiePolyStar
    &star)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    star : QLottiePolyStar
      Passed on as a value: Qt reads the C++ QLottiePolyStar, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottiePolyStar &star)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK15QLottiePolyStar',
        self._valueOf(star),
    )

  @overload(QLottieRound)
  def render(self, round: QLottieRound) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieRound
    &round)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    round : QLottieRound
      Passed on as a value: Qt reads the C++ QLottieRound, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieRound &round)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK12QLottieRound',
        self._valueOf(round),
    )

  @overload(QLottieFill)
  def render(self, fill: QLottieFill) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieFill &fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    fill : QLottieFill
      Passed on as a value: Qt reads the C++ QLottieFill, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieFill &fill)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK11QLottieFill',
        self._valueOf(fill),
    )

  @overload(QLottieGFill)
  def render(self, shape: QLottieGFill) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieGFill
    &shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    shape : QLottieGFill
      Passed on as a value: Qt reads the C++ QLottieGFill, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieGFill &shape)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK12QLottieGFill',
        self._valueOf(shape),
    )

  @overload(QLottieImage)
  def render(self, image: QLottieImage) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    image : QLottieImage
      Passed on as a value: Qt reads the C++ QLottieImage, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieImage &image)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK12QLottieImage',
        self._valueOf(image),
    )

  @overload(QLottieStroke)
  def render(self, stroke: QLottieStroke) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieStroke
    &stroke)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    stroke : QLottieStroke
      Passed on as a value: Qt reads the C++ QLottieStroke, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieStroke &stroke)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK13QLottieStroke',
        self._valueOf(stroke),
    )

  @overload(QLottieShapeTransform)
  def render(self, transform: QLottieShapeTransform) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const
    QLottieShapeTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    transform : QLottieShapeTransform
      Passed on as a value: Qt reads the C++ QLottieShapeTransform, which
      stays Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieShapeTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK21QLottieShapeTransform',
        self._valueOf(transform),
    )

  @overload(QLottieBasicTransform)
  def render(self, transform: QLottieBasicTransform) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const
    QLottieBasicTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    transform : QLottieBasicTransform
      Passed on as a value: Qt reads the C++ QLottieBasicTransform, which
      stays Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieBasicTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK21QLottieBasicTransform',
        self._valueOf(transform),
    )

  @overload(QLottieFreeFormShape)
  def render(self, shape: QLottieFreeFormShape) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieFreeFormShape
    &shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    shape : QLottieFreeFormShape
      Passed on as a value: Qt reads the C++ QLottieFreeFormShape, which
      stays Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieFreeFormShape &shape)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK20QLottieFreeFormShape',
        self._valueOf(shape),
    )

  @overload(QLottieTrimPath)
  def render(self, trans: QLottieTrimPath) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieTrimPath
    &trans)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    trans : QLottieTrimPath
      Passed on as a value: Qt reads the C++ QLottieTrimPath, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieTrimPath &trans)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK15QLottieTrimPath',
        self._valueOf(trans),
    )

  @overload(QLottieFillEffect)
  def render(self, effect: QLottieFillEffect) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieFillEffect
    &effect)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    effect : QLottieFillEffect
      Passed on as a value: Qt reads the C++ QLottieFillEffect, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieFillEffect &effect)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK17QLottieFillEffect',
        self._valueOf(effect),
    )

  @overload(QLottieRepeater)
  def render(self, repeater: QLottieRepeater) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::render(const QLottieRepeater
    &repeater)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierasterrenderer.html#render

    Parameters
    ----------

    repeater : QLottieRepeater
      Passed on as a value: Qt reads the C++ QLottieRepeater, which stays
      Python's own.
    """
    #  void QLottieRasterRenderer::render(const QLottieRepeater &repeater)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer6renderERK15QLottieRepeater',
        self._valueOf(repeater),
    )

  @overload(QList[QLottieBase])
  def renderPathElements(self, pathElements: QList[QLottieBase]) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::renderPathElements(const
    QList<QLottieBase *> &pathElements)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierasterrenderer.html#renderPathElements

    Parameters
    ----------

    pathElements : QList[QLottieBase]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLottieRasterRenderer::renderPathElements(const QList<QLottieBase
    #      *> &pathElements)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer18renderPathElementsERK5QListIP11Q'
        'LottieBaseE',
        self._valueOf(pathElements),
    )

  @overload(int)
  def applyRepeaterTransform(self, instance: int) -> None:
    """
    Calls Qt's 'void QLottieRasterRenderer::applyRepeaterTransform(int
    instance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierasterrenderer.html#applyRepeaterTransform

    Parameters
    ----------

    instance : int
      Passed on as it is.
    """
    #  void QLottieRasterRenderer::applyRepeaterTransform(int instance)
    self.uglySide.call(
        'ritual_ZN21QLottieRasterRenderer22applyRepeaterTransformEi',
        instance,
    )
