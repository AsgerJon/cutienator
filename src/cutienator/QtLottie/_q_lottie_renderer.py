"""
QLottieRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottierenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieRenderer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QLottieBase, QLottieBasicTransform, QLottieEllipse
  from . import QLottieFill, QLottieFillEffect, QLottieFreeFormShape
  from . import QLottieGFill, QLottieGroup, QLottieImage, QLottieLayer
  from . import QLottiePolyStar, QLottiePrecomposition, QLottieRect
  from . import QLottieRepeater, QLottieRound, QLottieShapeTransform
  from . import QLottieSolidLayer, QLottieStroke, QLottieTextLayer
  from . import QLottieTrimPath
  from ..QtGui import QTransform
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
  QLottieGroup = WAIT['QLottieGroup']
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
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieRenderer: a plain Python object standing in
  front of one C++ QLottieRenderer.

  What exists
  -----------

  Every function of Qt's QLottieRenderer that has a ritual and that Python
  can call so far, 10 names in all: 'saveState', 'restoreState',
  'setTrimmingState', 'trimmingState', 'render', 'renderPathElements',
  'finish', 'saveTrimmingState', 'restoreTrimmingState', 'applyTransform'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieRenderer::~QLottieRenderer()': the destructor: Python never
    removes a C++ QLottieRenderer.

  What to expect
  --------------

  - The C++ QLottieRenderer is created at the first use, not by
    'QLottieRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLottieRenderer.
  """

  #  The enums Qt writes inside QLottieRenderer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TrimmingState(CuteNum):
    """
    The enum 'QLottieRenderer::TrimmingState' of Qt, with the 3 names Qt
    gives in it.
    """

    Off = Kee[int](0)
    Parallel = Kee[int](1)
    Sequential = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTransform, QLottieBasicTransform)
  @overload(NoneType, QLottieBasicTransform)
  @overload(QTransform, QLottieBasicTransform, bool)
  @overload(NoneType, QLottieBasicTransform, bool)
  def applyTransform(
      xf: Optional[QTransform],
      lottieXf: QLottieBasicTransform,
      isShapeTransform: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QLottieRenderer::applyTransform(QTransform *xf, const
    QLottieBasicTransform &lottieXf, bool isShapeTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierenderer.html#applyTransform

    Parameters
    ----------

    xf : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lottieXf : QLottieBasicTransform
      Passed on as a value: Qt reads the C++ QLottieBasicTransform, which
      stays Python's own.

    isShapeTransform : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QLottieRenderer::applyTransform(QTransform *xf, const
    #      QLottieBasicTransform &lottieXf, bool isShapeTransform)
    Rituals.call(
        'ritual_ZN15QLottieRenderer14applyTransformEP10QTransformRK21QLotti'
        'eBasicTransformb',
        CuteMixin._addressOf(xf), CuteMixin._valueOf(lottieXf),
        isShapeTransform,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieRenderer'

  #  A C++ QLottieRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRenderer'

  #  The functions Qt calls itself that QLottieRenderer is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'renderPathElements': (
          'void QLottieRenderer::renderPathElements(const '
          'QList<QLottieBase *> &)',
      ),
  }

  #  The functions Qt calls itself that QLottieRenderer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'saveState': (
          ('_ZN15QLottieRenderer9saveStateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'restoreState': (
          ('_ZN15QLottieRenderer12restoreStateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setTrimmingState': (
          ('_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingStateE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtLottie:QLottieRenderer.TrimmingState'),
           )),
      ),
      'trimmingState': (
          ('_ZNK15QLottieRenderer13trimmingStateEv',
           ('int', 'enum', 'QtLottie:QLottieRenderer.TrimmingState'),
           ()),
      ),
      'render': (
          ('_ZN15QLottieRenderer6renderERK21QLottiePrecomposition',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottiePrecomposition'),
           )),
          ('_ZN15QLottieRenderer6renderERK12QLottieLayer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieLayer'),
           )),
          ('_ZN15QLottieRenderer6renderERK17QLottieSolidLayer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieSolidLayer'),
           )),
          ('_ZN15QLottieRenderer6renderERK16QLottieTextLayer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieTextLayer'),
           )),
          ('_ZN15QLottieRenderer6renderERK12QLottieGroup',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieGroup'),
           )),
          ('_ZN15QLottieRenderer6renderERK11QLottieRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieRect'),
           )),
          ('_ZN15QLottieRenderer6renderERK14QLottieEllipse',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieEllipse'),
           )),
          ('_ZN15QLottieRenderer6renderERK15QLottiePolyStar',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottiePolyStar'),
           )),
          ('_ZN15QLottieRenderer6renderERK12QLottieRound',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieRound'),
           )),
          ('_ZN15QLottieRenderer6renderERK11QLottieFill',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieFill'),
           )),
          ('_ZN15QLottieRenderer6renderERK12QLottieGFill',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieGFill'),
           )),
          ('_ZN15QLottieRenderer6renderERK12QLottieImage',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieImage'),
           )),
          ('_ZN15QLottieRenderer6renderERK13QLottieStroke',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieStroke'),
           )),
          ('_ZN15QLottieRenderer6renderERK21QLottieBasicTransform',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieBasicTransform'),
           )),
          ('_ZN15QLottieRenderer6renderERK21QLottieShapeTransform',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieShapeTransform'),
           )),
          ('_ZN15QLottieRenderer6renderERK20QLottieFreeFormShape',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieFreeFormShape'),
           )),
          ('_ZN15QLottieRenderer6renderERK15QLottieTrimPath',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieTrimPath'),
           )),
          ('_ZN15QLottieRenderer6renderERK17QLottieFillEffect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieFillEffect'),
           )),
          ('_ZN15QLottieRenderer6renderERK15QLottieRepeater',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieRepeater'),
           )),
      ),
      'finish': (
          ('_ZN15QLottieRenderer6finishERK12QLottieLayer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieLayer'),
           )),
          ('_ZN15QLottieRenderer6finishERK12QLottieGroup',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieGroup'),
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

  def trimmingState(self) -> TrimmingState:
    """
    Calls Qt's 'TrimmingState QLottieRenderer::trimmingState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#trimmingState

    Returns
    -------

    TrimmingState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TrimmingState(number)'
      gives.
    """
    #  TrimmingState QLottieRenderer::trimmingState() const
    ritual = 'ritual_ZNK15QLottieRenderer13trimmingStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottieRenderer13trimmingStateEv'
    return QLottieRenderer.TrimmingState(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TrimmingState)
  def setTrimmingState(self, state: TrimmingState) -> None:
    """
    Calls Qt's 'void QLottieRenderer::setTrimmingState(TrimmingState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierenderer.html#setTrimmingState

    Parameters
    ----------

    state : TrimmingState
      Passed on as its number.
    """
    #  void QLottieRenderer::setTrimmingState(TrimmingState state)
    ritual = (
        'ritual_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingSt'
          'ateE')
    self.uglySide.call(ritual, state.value)

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

  def saveState(self) -> None:
    """
    Calls Qt's 'void QLottieRenderer::saveState()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#saveState
    """
    #  void QLottieRenderer::saveState()
    self.uglySide.call('ritual_ZN15QLottieRenderer9saveStateEv')

  def restoreState(self) -> None:
    """
    Calls Qt's 'void QLottieRenderer::restoreState()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#restoreState
    """
    #  void QLottieRenderer::restoreState()
    self.uglySide.call('ritual_ZN15QLottieRenderer12restoreStateEv')

  @overload(QLottiePrecomposition)
  def render(self, precomp: QLottiePrecomposition) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottiePrecomposition
    &precomp)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    precomp : QLottiePrecomposition
      Passed on as a value: Qt reads the C++ QLottiePrecomposition, which
      stays Python's own.
    """
    #  void QLottieRenderer::render(const QLottiePrecomposition &precomp)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK21QLottiePrecomposition',
        self._valueOf(precomp),
    )

  @overload(QLottieSolidLayer)
  def render(self, layer: QLottieSolidLayer) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieSolidLayer
    &layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    layer : QLottieSolidLayer
      Passed on as a value: Qt reads the C++ QLottieSolidLayer, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieSolidLayer &layer)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK17QLottieSolidLayer',
        self._valueOf(layer),
    )

  @overload(QLottieTextLayer)
  def render(self, a0: QLottieTextLayer) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieTextLayer &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    a0 : QLottieTextLayer
      Passed on as a value: Qt reads the C++ QLottieTextLayer, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieTextLayer &a0)
    ritual = 'ritual_ZN15QLottieRenderer6renderERK16QLottieTextLayer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieRenderer6renderERK16QLottieTextLayer'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QLottieLayer)
  def render(self, layer: QLottieLayer) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieLayer &layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    layer : QLottieLayer
      Passed on as a value: Qt reads the C++ QLottieLayer, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieLayer &layer)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK12QLottieLayer',
        self._valueOf(layer),
    )

  @overload(QLottieGroup)
  def render(self, a0: QLottieGroup) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieGroup &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    a0 : QLottieGroup
      Passed on as a value: Qt reads the C++ QLottieGroup, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieGroup &a0)
    ritual = 'ritual_ZN15QLottieRenderer6renderERK12QLottieGroup'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieRenderer6renderERK12QLottieGroup'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QLottieRect)
  def render(self, rect: QLottieRect) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    rect : QLottieRect
      Passed on as a value: Qt reads the C++ QLottieRect, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieRect &rect)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK11QLottieRect',
        self._valueOf(rect),
    )

  @overload(QLottieEllipse)
  def render(self, ellipse: QLottieEllipse) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieEllipse &ellipse)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    ellipse : QLottieEllipse
      Passed on as a value: Qt reads the C++ QLottieEllipse, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieEllipse &ellipse)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK14QLottieEllipse',
        self._valueOf(ellipse),
    )

  @overload(QLottiePolyStar)
  def render(self, star: QLottiePolyStar) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottiePolyStar &star)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    star : QLottiePolyStar
      Passed on as a value: Qt reads the C++ QLottiePolyStar, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottiePolyStar &star)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK15QLottiePolyStar',
        self._valueOf(star),
    )

  @overload(QLottieRound)
  def render(self, round: QLottieRound) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieRound &round)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    round : QLottieRound
      Passed on as a value: Qt reads the C++ QLottieRound, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieRound &round)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK12QLottieRound',
        self._valueOf(round),
    )

  @overload(QLottieFill)
  def render(self, fill: QLottieFill) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieFill &fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    fill : QLottieFill
      Passed on as a value: Qt reads the C++ QLottieFill, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieFill &fill)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK11QLottieFill',
        self._valueOf(fill),
    )

  @overload(QLottieGFill)
  def render(self, fill: QLottieGFill) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieGFill &fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    fill : QLottieGFill
      Passed on as a value: Qt reads the C++ QLottieGFill, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieGFill &fill)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK12QLottieGFill',
        self._valueOf(fill),
    )

  @overload(QLottieImage)
  def render(self, image: QLottieImage) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    image : QLottieImage
      Passed on as a value: Qt reads the C++ QLottieImage, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieImage &image)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK12QLottieImage',
        self._valueOf(image),
    )

  @overload(QLottieStroke)
  def render(self, stroke: QLottieStroke) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieStroke &stroke)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    stroke : QLottieStroke
      Passed on as a value: Qt reads the C++ QLottieStroke, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieStroke &stroke)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK13QLottieStroke',
        self._valueOf(stroke),
    )

  @overload(QLottieShapeTransform)
  def render(self, trans: QLottieShapeTransform) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieShapeTransform
    &trans)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    trans : QLottieShapeTransform
      Passed on as a value: Qt reads the C++ QLottieShapeTransform, which
      stays Python's own.
    """
    #  void QLottieRenderer::render(const QLottieShapeTransform &trans)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK21QLottieShapeTransform',
        self._valueOf(trans),
    )

  @overload(QLottieBasicTransform)
  def render(self, trans: QLottieBasicTransform) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieBasicTransform
    &trans)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    trans : QLottieBasicTransform
      Passed on as a value: Qt reads the C++ QLottieBasicTransform, which
      stays Python's own.
    """
    #  void QLottieRenderer::render(const QLottieBasicTransform &trans)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK21QLottieBasicTransform',
        self._valueOf(trans),
    )

  @overload(QLottieFreeFormShape)
  def render(self, shape: QLottieFreeFormShape) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieFreeFormShape
    &shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    shape : QLottieFreeFormShape
      Passed on as a value: Qt reads the C++ QLottieFreeFormShape, which
      stays Python's own.
    """
    #  void QLottieRenderer::render(const QLottieFreeFormShape &shape)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK20QLottieFreeFormShape',
        self._valueOf(shape),
    )

  @overload(QLottieTrimPath)
  def render(self, trans: QLottieTrimPath) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieTrimPath &trans)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    trans : QLottieTrimPath
      Passed on as a value: Qt reads the C++ QLottieTrimPath, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieTrimPath &trans)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK15QLottieTrimPath',
        self._valueOf(trans),
    )

  @overload(QLottieFillEffect)
  def render(self, effect: QLottieFillEffect) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieFillEffect
    &effect)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    effect : QLottieFillEffect
      Passed on as a value: Qt reads the C++ QLottieFillEffect, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieFillEffect &effect)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK17QLottieFillEffect',
        self._valueOf(effect),
    )

  @overload(QLottieRepeater)
  def render(self, repeater: QLottieRepeater) -> None:
    """
    Calls Qt's 'void QLottieRenderer::render(const QLottieRepeater
    &repeater)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#render

    Parameters
    ----------

    repeater : QLottieRepeater
      Passed on as a value: Qt reads the C++ QLottieRepeater, which stays
      Python's own.
    """
    #  void QLottieRenderer::render(const QLottieRepeater &repeater)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer6renderERK15QLottieRepeater',
        self._valueOf(repeater),
    )

  @overload(QList[QLottieBase])
  def renderPathElements(self, pathElements: QList[QLottieBase]) -> None:
    """
    Calls Qt's 'void QLottieRenderer::renderPathElements(const
    QList<QLottieBase *> &pathElements)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierenderer.html#renderPathElements

    Parameters
    ----------

    pathElements : QList[QLottieBase]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLottieRenderer::renderPathElements(const QList<QLottieBase *>
    #      &pathElements)
    self.uglySide.call(
        'ritual_ZN15QLottieRenderer18renderPathElementsERK5QListIP11QLottie'
        'BaseE',
        self._valueOf(pathElements),
    )

  @overload(QLottieLayer)
  def finish(self, a0: QLottieLayer) -> None:
    """
    Calls Qt's 'void QLottieRenderer::finish(const QLottieLayer &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#finish

    Parameters
    ----------

    a0 : QLottieLayer
      Passed on as a value: Qt reads the C++ QLottieLayer, which stays
      Python's own.
    """
    #  void QLottieRenderer::finish(const QLottieLayer &a0)
    ritual = 'ritual_ZN15QLottieRenderer6finishERK12QLottieLayer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieRenderer6finishERK12QLottieLayer'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QLottieGroup)
  def finish(self, a0: QLottieGroup) -> None:
    """
    Calls Qt's 'void QLottieRenderer::finish(const QLottieGroup &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottierenderer.html#finish

    Parameters
    ----------

    a0 : QLottieGroup
      Passed on as a value: Qt reads the C++ QLottieGroup, which stays
      Python's own.
    """
    #  void QLottieRenderer::finish(const QLottieGroup &a0)
    ritual = 'ritual_ZN15QLottieRenderer6finishERK12QLottieGroup'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieRenderer6finishERK12QLottieGroup'
    self.uglySide.call(ritual, self._valueOf(a0))

  def saveTrimmingState(self) -> None:
    """
    Calls Qt's 'void QLottieRenderer::saveTrimmingState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierenderer.html#saveTrimmingState
    """
    #  void QLottieRenderer::saveTrimmingState()
    self.uglySide.call('ritual_ZN15QLottieRenderer17saveTrimmingStateEv')

  def restoreTrimmingState(self) -> None:
    """
    Calls Qt's 'void QLottieRenderer::restoreTrimmingState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierenderer.html#restoreTrimmingState
    """
    #  void QLottieRenderer::restoreTrimmingState()
    self.uglySide.call('ritual_ZN15QLottieRenderer20restoreTrimmingStateEv')
