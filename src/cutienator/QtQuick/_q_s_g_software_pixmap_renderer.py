"""
QSGSoftwarePixmapRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaprenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwarePixmapRenderer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGAbstractSoftwareRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from . import QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSGRenderContext = WAIT['QSGRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwarePixmapRenderer(QSGAbstractSoftwareRenderer):
  """
  The cute side of Qt's QSGSoftwarePixmapRenderer: a plain Python object
  standing in front of one C++ QSGSoftwarePixmapRenderer.

  It is built on the cute 'QSGAbstractSoftwareRenderer', as Qt's
  QSGSoftwarePixmapRenderer is built on Qt's QSGAbstractSoftwareRenderer, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwarePixmapRenderer that has a ritual and that
  Python can call so far, 3 names in all: 'renderScene', 'render',
  'setProjectionRect'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwarePixmapRenderer::~QSGSoftwarePixmapRenderer()': the
    destructor: Python never removes a C++ QSGSoftwarePixmapRenderer.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSGSoftwarePixmapRenderer is created at the first use, not by
    'QSGSoftwarePixmapRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwarePixmapRenderer.
  - Qt tells when it has removed the C++ QSGSoftwarePixmapRenderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwarePixmapRenderer'

  #  A C++ QSGSoftwarePixmapRenderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwarePixmapRenderer'

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

  @overload(QRect)
  def setProjectionRect(self, projectionRect: QRect) -> None:
    """
    Calls Qt's 'void QSGSoftwarePixmapRenderer::setProjectionRect(const QRect
    &projectionRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaprenderer.html#setProjectionRect

    Parameters
    ----------

    projectionRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSGSoftwarePixmapRenderer::setProjectionRect(const QRect
    #      &projectionRect)
    self.uglySide.call(
        'ritual_ZN25QSGSoftwarePixmapRenderer17setProjectionRectERK5QRect',
        self._valueOf(projectionRect),
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

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGSoftwarePixmapRenderer::QSGSoftwarePixmapRenderer(QSGRenderContext
    *context)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaprenderer.html

    Parameters
    ----------

    context : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGSoftwarePixmapRenderer::QSGSoftwarePixmapRenderer(QSGRenderContext
    #      *context)
    self._noteCreation(QSGSoftwarePixmapRenderer, lambda: Rituals.call(
        'ritual_ZN25QSGSoftwarePixmapRendererC1EP16QSGRenderContext',
        self._addressOf(context),
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

  def renderScene(self) -> None:
    """
    Calls Qt's 'void QSGSoftwarePixmapRenderer::renderScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaprenderer.html#renderScene
    """
    #  void QSGSoftwarePixmapRenderer::renderScene()
    self.uglySide.call('ritual_ZN25QSGSoftwarePixmapRenderer11renderSceneEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QSGSoftwarePixmapRenderer::render()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaprenderer.html#render
    """
    #  void QSGSoftwarePixmapRenderer::render()
    self.uglySide.call('ritual_ZN25QSGSoftwarePixmapRenderer6renderEv')
