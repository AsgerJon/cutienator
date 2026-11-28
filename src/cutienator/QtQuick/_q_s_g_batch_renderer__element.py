"""
QSGBatchRenderer::Element binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Element to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGGeometryNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGGeometryNode = WAIT['QSGGeometryNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Element(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::Element: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Element.

  C++ hands a QSGBatchRenderer::Element around as a copy, so every C++
  QSGBatchRenderer::Element behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Element that has a ritual and that
  Python can call so far, 3 names in all: 'setNode', 'ensureBoundsValid',
  'computeBounds'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::Element::~Element()': the destructor: Python
    removes its C++ QSGBatchRenderer::Element by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Element is created at the first use, not by
    'QSGBatchRenderer::Element(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::Element back gives a copy the
    ritual made for Python, in a new cute QSGBatchRenderer::Element.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Element'

  #  Qt's '~QSGBatchRenderer::Element()'. Naming it makes this a value class:
  #  Python owns every C++ QSGBatchRenderer::Element behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGBatchRenderer7ElementD1Ev'

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

  @overload(QSGGeometryNode)
  @overload(NoneType)
  def setNode(self, n: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Element::setNode(QSGGeometryNode *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-element.html#setNode

    Parameters
    ----------

    n : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Element::setNode(QSGGeometryNode *n)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer7Element7setNodeEP15QSGGeometryNode',
        self._addressOf(n, 'QSGGeometryNode'),
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
    Notes what was given, for Qt's 'QSGBatchRenderer::Element::Element()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-element.html#Element
    """
    #  QSGBatchRenderer::Element::Element()
    self._noteCreation(Element, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer7ElementC1Ev',
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

  def ensureBoundsValid(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Element::ensureBoundsValid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-element.html#ensureBoundsValid
    """
    #  void QSGBatchRenderer::Element::ensureBoundsValid()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer7Element17ensureBoundsValidEv',
    )

  def computeBounds(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Element::computeBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-element.html#computeBounds
    """
    #  void QSGBatchRenderer::Element::computeBounds()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer7Element13computeBoundsEv',
    )
