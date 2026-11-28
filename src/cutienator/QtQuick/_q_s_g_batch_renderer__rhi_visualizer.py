"""
QSGBatchRenderer::RhiVisualizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhivisualizer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::RhiVisualizer to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from . import QSGBatchRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class RhiVisualizer(QSGBatchRenderer.Visualizer):
  """
  The cute side of Qt's QSGBatchRenderer::RhiVisualizer: a plain Python
  object standing in front of one C++ QSGBatchRenderer::RhiVisualizer.

  It is built on the cute 'QSGBatchRenderer::Visualizer', as Qt's
  QSGBatchRenderer::RhiVisualizer is built on Qt's
  QSGBatchRenderer::Visualizer, and has everything that class has.

  C++ hands a QSGBatchRenderer::RhiVisualizer around as a copy, so every C++
  QSGBatchRenderer::RhiVisualizer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::RhiVisualizer that has a ritual
  and that Python can call so far, 3 names in all: 'prepareVisualize',
  'visualize', 'releaseResources'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::RhiVisualizer::~RhiVisualizer()': the destructor:
    Python removes its C++ QSGBatchRenderer::RhiVisualizer by it, and has no
    other use for it.
  - Qt's 'void QSGBatchRenderer::RhiVisualizer::recordDrawCalls(const
    QList<DrawCall> &drawCalls, QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, bool blendOneOne)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'QSGBatchRenderer.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::RhiVisualizer is created at the first use, not
    by 'QSGBatchRenderer::RhiVisualizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::RhiVisualizer back gives a copy the
    ritual made for Python, in a new cute QSGBatchRenderer::RhiVisualizer.
  - Each name of Qt's QSGBatchRenderer::RhiVisualizer that has no cute
    function yet, '__init__', 'recordDrawCalls', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGBatchRenderer::RhiVisualizer, each a
  #  class in here as in C++.

  class DrawCall(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGBatchRenderer::RhiVisualizer::DrawCall: a plain
    Python object standing in front of one C++
    QSGBatchRenderer::RhiVisualizer::DrawCall.

    C++ hands a QSGBatchRenderer::RhiVisualizer::DrawCall around as a copy,
    so every C++ QSGBatchRenderer::RhiVisualizer::DrawCall behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSGBatchRenderer::RhiVisualizer::DrawCall yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGBatchRenderer::RhiVisualizer::DrawCall::~DrawCall()': the
      destructor: Python removes its C++
      QSGBatchRenderer::RhiVisualizer::DrawCall by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSGBatchRenderer::RhiVisualizer::DrawCall is created at the
      first use, not by 'QSGBatchRenderer::RhiVisualizer::DrawCall(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGBatchRenderer::RhiVisualizer::DrawCall back
      gives a copy the ritual made for Python, in a new cute
      QSGBatchRenderer::RhiVisualizer::DrawCall.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGBatchRenderer::RhiVisualizer::DrawCall'

    #  Qt's '~QSGBatchRenderer::RhiVisualizer::DrawCall()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSGBatchRenderer::RhiVisualizer::DrawCall behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN16QSGBatchRenderer13RhiVisualizer8DrawCallD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::RhiVisualizer'

  #  A C++ QSGBatchRenderer::RhiVisualizer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBatchRenderer_RhiVisualizer'

  #  Qt's '~QSGBatchRenderer::RhiVisualizer()'. Naming it makes this a value
  #  class: Python owns every C++ QSGBatchRenderer::RhiVisualizer behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGBatchRenderer13RhiVisualizerD1Ev'

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
    Qt's 'QSGBatchRenderer::RhiVisualizer::RhiVisualizer(Renderer
    *renderer)': leans on
    'QSGBatchRenderer::Visualizer::visualizeChangesPrepare(
    QSGBatchRenderer::Node*, unsigned int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.RhiVisualizer.__init__' has no cute function "
        "yet. Qt's 'QSGBatchRenderer::RhiVisualizer::RhiVisualizer(Renderer "
        "*renderer)': leans on "
        "'QSGBatchRenderer::Visualizer::visualizeChangesPrepare(QSGBatchRend"
        "erer::Node*, unsigned int)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  def prepareVisualize(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::RhiVisualizer::prepareVisualize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-rhivisualizer.html
    """
    #  void QSGBatchRenderer::RhiVisualizer::prepareVisualize()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer13RhiVisualizer16prepareVisualizeEv',
    )

  def visualize(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::RhiVisualizer::visualize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-rhivisualizer.html#visualize
    """
    #  void QSGBatchRenderer::RhiVisualizer::visualize()
    ritual = 'ritual_ZN16QSGBatchRenderer13RhiVisualizer9visualizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGBatchRenderer13RhiVisualizer9visualizeEv'
    self.uglySide.call(ritual)

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::RhiVisualizer::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-rhivisualizer.html
    """
    #  void QSGBatchRenderer::RhiVisualizer::releaseResources()
    ritual = 'ritual_ZN16QSGBatchRenderer13RhiVisualizer16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGBatchRenderer13RhiVisualizer16releaseResources'
          'Ev')
    self.uglySide.call(ritual)

  @staticmethod
  def recordDrawCalls(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::RhiVisualizer::recordDrawCalls(const
    QList<DrawCall> &drawCalls, QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, bool blendOneOne)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.RhiVisualizer.recordDrawCalls' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::RhiVisualizer::recordDrawCalls(const "
        "QList<DrawCall> &drawCalls, QRhiCommandBuffer *cb, "
        "QRhiShaderResourceBindings *srb, bool blendOneOne)': takes a type "
        "Python has no way to hand over yet.")
