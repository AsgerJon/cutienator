"""
QSGSoftwareRenderableNodeUpdater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenodeupdater_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGSoftwareRenderableNodeUpdater to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGNodeVisitorEx

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QSGSoftwareRenderableNodeUpdater(QSGNodeVisitorEx):
  """
  The cute side of Qt's QSGSoftwareRenderableNodeUpdater: a plain Python
  object standing in front of one C++ QSGSoftwareRenderableNodeUpdater.

  It is built on the cute 'QSGNodeVisitorEx', as Qt's
  QSGSoftwareRenderableNodeUpdater is built on Qt's QSGNodeVisitorEx, and has
  everything that class has.

  C++ hands a QSGSoftwareRenderableNodeUpdater around as a copy, so every C++
  QSGSoftwareRenderableNodeUpdater behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSGSoftwareRenderableNodeUpdater that has a ritual
  and that Python can call so far, 3 names in all: 'visit', 'endVisit',
  'updateNodes'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSGSoftwareRenderableNodeUpdater::~QSGSoftwareRenderableNodeUpdater()':
    the destructor: Python removes its C++ QSGSoftwareRenderableNodeUpdater
    by it, and has no other use for it.
  - Qt's 'NodeState QSGSoftwareRenderableNodeUpdater::currentState(QSGNode
    *node) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 1 a template; 1 leans on
  'QSGSoftwareRenderableNodeUpdater.

  What to expect
  --------------

  - The C++ QSGSoftwareRenderableNodeUpdater is created at the first use, not
    by 'QSGSoftwareRenderableNodeUpdater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGSoftwareRenderableNodeUpdater back gives a copy
    the ritual made for Python, in a new cute
    QSGSoftwareRenderableNodeUpdater.
  - Each name of Qt's QSGSoftwareRenderableNodeUpdater that has no cute
    function yet, '__init__', 'currentState', 'updateRenderableNode', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareRenderableNodeUpdater'

  #  A C++ QSGSoftwareRenderableNodeUpdater Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareRenderableNodeUpdater'

  #  Qt's '~QSGSoftwareRenderableNodeUpdater()'. Naming it makes this a value
  #  class: Python owns every C++ QSGSoftwareRenderableNodeUpdater behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QSGSoftwareRenderableNodeUpdaterD1Ev'

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
    Qt's 'QSGSoftwareRenderableNodeUpdater::QSGSoftwareRenderableNodeUpdater(
    QSGAbstractSoftwareRenderer *renderer)': leans on
    'QSGSoftwareRenderableNodeUpdater::visit(QSGClipNode*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareRenderableNodeUpdater.__init__' has no cute function "
        "yet. Qt's "
        "'QSGSoftwareRenderableNodeUpdater::QSGSoftwareRenderableNodeUpdater"
        "(QSGAbstractSoftwareRenderer *renderer)': leans on "
        "'QSGSoftwareRenderableNodeUpdater::visit(QSGClipNode*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGTransformNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP16QSGTransformN'
        'ode',
        self._addressOf(a0, 'QSGTransformNode'),
    )

  @overload(QSGClipNode)
  def visit(self, a0: Optional[QSGClipNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGClipNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGClipNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP11QSGClipNode',
        self._addressOf(a0),
    )

  @overload(QSGInternalImageNode)
  def visit(self, a0: Optional[QSGInternalImageNode]) -> bool:
    """
    Calls Qt's 'bool
    QSGSoftwareRenderableNodeUpdater::visit(QSGInternalImageNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGInternalImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGInternalImageNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP20QSGInternalIm'
        'ageNode',
        self._addressOf(a0),
    )

  @overload(QSGPainterNode)
  def visit(self, a0: Optional[QSGPainterNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGPainterNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGPainterNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGPainterNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP14QSGPainterNod'
        'e',
        self._addressOf(a0),
    )

  @overload(QSGInternalRectangleNode)
  def visit(self, a0: Optional[QSGInternalRectangleNode]) -> bool:
    """
    Calls Qt's 'bool
    QSGSoftwareRenderableNodeUpdater::visit(QSGInternalRectangleNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGInternalRectangleNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGInternalRectangleNode
    #      *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP24QSGInternalRe'
        'ctangleNode',
        self._addressOf(a0),
    )

  @overload(QSGGlyphNode)
  def visit(self, a0: Optional[QSGGlyphNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGGlyphNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGGlyphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGGlyphNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP12QSGGlyphNode',
        self._addressOf(a0),
    )

  @overload(QSGSpriteNode)
  def visit(self, a0: Optional[QSGSpriteNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGSpriteNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGSpriteNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP13QSGSpriteNode',
        self._addressOf(a0),
    )

  @overload(QSGGeometryNode)
  def visit(self, a0: Optional[QSGGeometryNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGGeometryNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGGeometryNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP15QSGGeometryNo'
        'de',
        self._addressOf(a0, 'QSGGeometryNode'),
    )

  @overload(QSGOpacityNode)
  def visit(self, a0: Optional[QSGOpacityNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGOpacityNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGOpacityNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP14QSGOpacityNod'
        'e',
        self._addressOf(a0),
    )

  @overload(QSGRootNode)
  def visit(self, a0: Optional[QSGRootNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGRootNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGRootNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP11QSGRootNode',
        self._addressOf(a0, 'QSGRootNode'),
    )

  @overload(QSGRenderNode)
  def visit(self, a0: Optional[QSGRenderNode]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNodeUpdater::visit(QSGRenderNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#visit

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareRenderableNodeUpdater::visit(QSGRenderNode *a0)
    return self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP13QSGRenderNode',
        self._addressOf(a0),
    )

  @overload(QSGTransformNode)
  @overload(NoneType)
  def endVisit(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderableNodeUpdater::endVisit(QSGTransformNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGTransformNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP16QSGTransfo'
        'rmNode',
        self._addressOf(a0, 'QSGTransformNode'),
    )

  @overload(QSGClipNode)
  def endVisit(self, a0: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNodeUpdater::endVisit(QSGClipNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGClipNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP11QSGClipNod'
        'e',
        self._addressOf(a0),
    )

  @overload(QSGInternalImageNode)
  def endVisit(self, a0: Optional[QSGInternalImageNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalImageNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGInternalImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalImageNode
    #      *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP20QSGInterna'
        'lImageNode',
        self._addressOf(a0),
    )

  @overload(QSGPainterNode)
  def endVisit(self, a0: Optional[QSGPainterNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderableNodeUpdater::endVisit(QSGPainterNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGPainterNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGPainterNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP14QSGPainter'
        'Node',
        self._addressOf(a0),
    )

  @overload(QSGInternalRectangleNode)
  def endVisit(self, a0: Optional[QSGInternalRectangleNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalRectangleNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGInternalRectangleNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(
    #      QSGInternalRectangleNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP24QSGInterna'
        'lRectangleNode',
        self._addressOf(a0),
    )

  @overload(QSGGlyphNode)
  def endVisit(self, a0: Optional[QSGGlyphNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGlyphNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGGlyphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGlyphNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP12QSGGlyphNo'
        'de',
        self._addressOf(a0),
    )

  @overload(QSGSpriteNode)
  def endVisit(self, a0: Optional[QSGSpriteNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNodeUpdater::endVisit(QSGSpriteNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGSpriteNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP13QSGSpriteN'
        'ode',
        self._addressOf(a0),
    )

  @overload(QSGGeometryNode)
  def endVisit(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderableNodeUpdater::endVisit(QSGGeometryNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGeometryNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP15QSGGeometr'
        'yNode',
        self._addressOf(a0, 'QSGGeometryNode'),
    )

  @overload(QSGOpacityNode)
  def endVisit(self, a0: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareRenderableNodeUpdater::endVisit(QSGOpacityNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGOpacityNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP14QSGOpacity'
        'Node',
        self._addressOf(a0),
    )

  @overload(QSGRootNode)
  def endVisit(self, a0: Optional[QSGRootNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRootNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRootNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP11QSGRootNod'
        'e',
        self._addressOf(a0, 'QSGRootNode'),
    )

  @overload(QSGRenderNode)
  def endVisit(self, a0: Optional[QSGRenderNode]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRenderNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#endVisit

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRenderNode *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP13QSGRenderN'
        'ode',
        self._addressOf(a0),
    )

  @overload(QSGNode)
  @overload(NoneType)
  @overload(QSGNode, bool)
  @overload(NoneType, bool)
  def updateNodes(
      self,
      node: Optional[QSGNode],
      isNodeRemoved: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNodeUpdater::updateNodes(QSGNode
    *node, bool isNodeRemoved)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenodeupdater.html#updateNodes

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isNodeRemoved : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSGSoftwareRenderableNodeUpdater::updateNodes(QSGNode *node, bool
    #      isNodeRemoved)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareRenderableNodeUpdater11updateNodesEP7QSGNode'
        'b',
        self._addressOf(node, 'QSGNode'), isNodeRemoved,
    )

  @staticmethod
  def currentState(*__, **_) -> Never:
    """
    Qt's 'NodeState QSGSoftwareRenderableNodeUpdater::currentState(QSGNode
    *node) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGSoftwareRenderableNodeUpdater.currentState' has no cute "
        "function yet. Qt's 'NodeState "
        "QSGSoftwareRenderableNodeUpdater::currentState(QSGNode *node) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def updateRenderableNode(*__, **_) -> Never:
    """
    Qt's 'QSGSoftwareRenderableNodeUpdater::updateRenderableNode': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QSGSoftwareRenderableNodeUpdater.updateRenderableNode' has no "
        "cute function yet. Qt's "
        "'QSGSoftwareRenderableNodeUpdater::updateRenderableNode': a "
        "template: a pattern and no single function.")
