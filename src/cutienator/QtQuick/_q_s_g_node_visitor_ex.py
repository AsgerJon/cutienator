"""
QSGNodeVisitorEx binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGNodeVisitorEx to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGClipNode, QSGGeometryNode, QSGGlyphNode
  from . import QSGInternalImageNode, QSGInternalRectangleNode, QSGNode
  from . import QSGOpacityNode, QSGPainterNode, QSGRenderNode, QSGRootNode
  from . import QSGSpriteNode, QSGTransformNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGClipNode = WAIT['QSGClipNode']
  QSGGeometryNode = WAIT['QSGGeometryNode']
  QSGGlyphNode = WAIT['QSGGlyphNode']
  QSGInternalImageNode = WAIT['QSGInternalImageNode']
  QSGInternalRectangleNode = WAIT['QSGInternalRectangleNode']
  QSGNode = WAIT['QSGNode']
  QSGOpacityNode = WAIT['QSGOpacityNode']
  QSGPainterNode = WAIT['QSGPainterNode']
  QSGRenderNode = WAIT['QSGRenderNode']
  QSGRootNode = WAIT['QSGRootNode']
  QSGSpriteNode = WAIT['QSGSpriteNode']
  QSGTransformNode = WAIT['QSGTransformNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGNodeVisitorEx(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGNodeVisitorEx: a plain Python object standing in
  front of one C++ QSGNodeVisitorEx.

  What exists
  -----------

  Every function of Qt's QSGNodeVisitorEx that has a ritual and that Python
  can call so far, 3 names in all: 'visit', 'endVisit', 'visitChildren'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGNodeVisitorEx::~QSGNodeVisitorEx()': the destructor: Python
    never removes a C++ QSGNodeVisitorEx.

  What to expect
  --------------

  - The C++ QSGNodeVisitorEx is created at the first use, not by
    'QSGNodeVisitorEx(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGNodeVisitorEx.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGNodeVisitorEx'

  #  A C++ QSGNodeVisitorEx Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGNodeVisitorEx'

  #  The functions Qt calls itself that QSGNodeVisitorEx is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'visit': (
          ('_ZN16QSGNodeVisitorEx5visitEP16QSGTransformNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGTransformNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP11QSGClipNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGClipNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP15QSGGeometryNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGGeometryNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP14QSGOpacityNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGOpacityNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP20QSGInternalImageNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGInternalImageNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP14QSGPainterNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGPainterNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP24QSGInternalRectangleNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGInternalRectangleNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP12QSGGlyphNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGGlyphNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP11QSGRootNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGRootNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP13QSGSpriteNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGSpriteNode'),
           )),
          ('_ZN16QSGNodeVisitorEx5visitEP13QSGRenderNode',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderNode'),
           )),
      ),
      'endVisit': (
          ('_ZN16QSGNodeVisitorEx8endVisitEP16QSGTransformNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTransformNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP11QSGClipNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGClipNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP15QSGGeometryNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGGeometryNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP14QSGOpacityNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGOpacityNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP20QSGInternalImageNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGInternalImageNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP14QSGPainterNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGPainterNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP24QSGInternalRectangleNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGInternalRectangleNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP12QSGGlyphNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGGlyphNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP11QSGRootNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRootNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP13QSGSpriteNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGSpriteNode'),
           )),
          ('_ZN16QSGNodeVisitorEx8endVisitEP13QSGRenderNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGRenderNode'),
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

  @overload(QSGTransformNode)
  @overload(NoneType)
  def visit(self, a0: Optional[QSGTransformNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGTransformNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGTransformNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP16QSGTransformNode',
        self._addressOf(a0, 'QSGTransformNode'),
    )

  @overload(QSGClipNode)
  def visit(self, a0: Optional[QSGClipNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGClipNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGClipNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP11QSGClipNode',
        self._addressOf(a0),
    )

  @overload(QSGInternalImageNode)
  def visit(self, a0: Optional[QSGInternalImageNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGInternalImageNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGInternalImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGInternalImageNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP20QSGInternalImageNode',
        self._addressOf(a0),
    )

  @overload(QSGPainterNode)
  def visit(self, a0: Optional[QSGPainterNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGPainterNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGPainterNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGPainterNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP14QSGPainterNode',
        self._addressOf(a0),
    )

  @overload(QSGInternalRectangleNode)
  def visit(self, a0: Optional[QSGInternalRectangleNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGInternalRectangleNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGInternalRectangleNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGInternalRectangleNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP24QSGInternalRectangleNode',
        self._addressOf(a0),
    )

  @overload(QSGGlyphNode)
  def visit(self, a0: Optional[QSGGlyphNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGGlyphNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGGlyphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGGlyphNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP12QSGGlyphNode',
        self._addressOf(a0),
    )

  @overload(QSGSpriteNode)
  def visit(self, a0: Optional[QSGSpriteNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGSpriteNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGSpriteNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP13QSGSpriteNode',
        self._addressOf(a0),
    )

  @overload(QSGGeometryNode)
  def visit(self, a0: Optional[QSGGeometryNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGGeometryNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGGeometryNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP15QSGGeometryNode',
        self._addressOf(a0, 'QSGGeometryNode'),
    )

  @overload(QSGOpacityNode)
  def visit(self, a0: Optional[QSGOpacityNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGOpacityNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGOpacityNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP14QSGOpacityNode',
        self._addressOf(a0),
    )

  @overload(QSGRootNode)
  def visit(self, a0: Optional[QSGRootNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGRootNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGRootNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP11QSGRootNode',
        self._addressOf(a0, 'QSGRootNode'),
    )

  @overload(QSGRenderNode)
  def visit(self, a0: Optional[QSGRenderNode]) -> bool:
    """
    Calls Qt's 'bool QSGNodeVisitorEx::visit(QSGRenderNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#visit

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeVisitorEx::visit(QSGRenderNode *a0)
    return self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx5visitEP13QSGRenderNode',
        self._addressOf(a0),
    )

  @overload(QSGTransformNode)
  @overload(NoneType)
  def endVisit(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGTransformNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGTransformNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP16QSGTransformNode',
        self._addressOf(a0, 'QSGTransformNode'),
    )

  @overload(QSGClipNode)
  def endVisit(self, a0: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGClipNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGClipNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP11QSGClipNode',
        self._addressOf(a0),
    )

  @overload(QSGInternalImageNode)
  def endVisit(self, a0: Optional[QSGInternalImageNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGInternalImageNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGInternalImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGInternalImageNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP20QSGInternalImageNode',
        self._addressOf(a0),
    )

  @overload(QSGPainterNode)
  def endVisit(self, a0: Optional[QSGPainterNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGPainterNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGPainterNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGPainterNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP14QSGPainterNode',
        self._addressOf(a0),
    )

  @overload(QSGInternalRectangleNode)
  def endVisit(self, a0: Optional[QSGInternalRectangleNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGInternalRectangleNode
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGInternalRectangleNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGInternalRectangleNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP24QSGInternalRectangleNode',
        self._addressOf(a0),
    )

  @overload(QSGGlyphNode)
  def endVisit(self, a0: Optional[QSGGlyphNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGGlyphNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGGlyphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGGlyphNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP12QSGGlyphNode',
        self._addressOf(a0),
    )

  @overload(QSGSpriteNode)
  def endVisit(self, a0: Optional[QSGSpriteNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGSpriteNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGSpriteNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP13QSGSpriteNode',
        self._addressOf(a0),
    )

  @overload(QSGGeometryNode)
  def endVisit(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGGeometryNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGGeometryNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP15QSGGeometryNode',
        self._addressOf(a0, 'QSGGeometryNode'),
    )

  @overload(QSGOpacityNode)
  def endVisit(self, a0: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGOpacityNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGOpacityNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP14QSGOpacityNode',
        self._addressOf(a0),
    )

  @overload(QSGRootNode)
  def endVisit(self, a0: Optional[QSGRootNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGRootNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGRootNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP11QSGRootNode',
        self._addressOf(a0, 'QSGRootNode'),
    )

  @overload(QSGRenderNode)
  def endVisit(self, a0: Optional[QSGRenderNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::endVisit(QSGRenderNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitorex.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::endVisit(QSGRenderNode *a0)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx8endVisitEP13QSGRenderNode',
        self._addressOf(a0),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def visitChildren(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitorEx::visitChildren(QSGNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitorex.html#visitChildren

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitorEx::visitChildren(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN16QSGNodeVisitorEx13visitChildrenEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )
