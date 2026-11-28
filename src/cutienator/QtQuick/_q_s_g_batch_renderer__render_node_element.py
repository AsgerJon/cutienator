"""
QSGBatchRenderer::RenderNodeElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::RenderNodeElement to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGBatchRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGRenderNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGRenderNode = WAIT['QSGRenderNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderNodeElement(QSGBatchRenderer.Element):
  """
  The cute side of Qt's QSGBatchRenderer::RenderNodeElement: a plain Python
  object standing in front of one C++ QSGBatchRenderer::RenderNodeElement.

  It is built on the cute 'QSGBatchRenderer::Element', as Qt's
  QSGBatchRenderer::RenderNodeElement is built on Qt's
  QSGBatchRenderer::Element, and has everything that class has.

  C++ hands a QSGBatchRenderer::RenderNodeElement around as a copy, so every
  C++ QSGBatchRenderer::RenderNodeElement behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QSGBatchRenderer::RenderNodeElement yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::RenderNodeElement::~RenderNodeElement()': the
    destructor: Python removes its C++ QSGBatchRenderer::RenderNodeElement by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::RenderNodeElement is created at the first use,
    not by 'QSGBatchRenderer::RenderNodeElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::RenderNodeElement back gives a copy
    the ritual made for Python, in a new cute
    QSGBatchRenderer::RenderNodeElement.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::RenderNodeElement'

  #  Qt's '~QSGBatchRenderer::RenderNodeElement()'. Naming it makes this a
  #  value class: Python owns every C++ QSGBatchRenderer::RenderNodeElement
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGBatchRenderer17RenderNodeElementD1Ev'

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

  @overload(QSGRenderNode)
  @overload(NoneType)
  def __init__(self, rn: Optional[QSGRenderNode]) -> None:
    """
    Notes what was given, for Qt's
    'QSGBatchRenderer::RenderNodeElement::RenderNodeElement(QSGRenderNode
    *rn)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-rendernodeelement.html

    Parameters
    ----------

    rn : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGBatchRenderer::RenderNodeElement::RenderNodeElement(QSGRenderNode
    #      *rn)
    self._noteCreation(RenderNodeElement, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer17RenderNodeElementC1EP13QSGRenderNode',
        self._addressOf(rn),
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
