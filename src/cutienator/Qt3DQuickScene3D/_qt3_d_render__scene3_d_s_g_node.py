"""
Qt3DRender::Scene3DSGNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Scene3DSGNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QSGGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtQuick import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGTexture = WAIT['QSGTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene3DSGNode(QSGGeometryNode):
  """
  The cute side of Qt's Qt3DRender::Scene3DSGNode: a plain Python object
  standing in front of one C++ Qt3DRender::Scene3DSGNode.

  It is built on the cute 'QSGGeometryNode', as Qt's
  Qt3DRender::Scene3DSGNode is built on Qt's QSGGeometryNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Scene3DSGNode that has a ritual and that
  Python can call so far, 5 names in all: 'setTexture', 'texture', 'setRect',
  'rect', 'show'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Scene3DSGNode::~Scene3DSGNode()': the destructor:
    Python never removes a C++ Qt3DRender::Scene3DSGNode.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 leans on 'vtable for Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Scene3DSGNode is created at the first use, not by
    'Qt3DRender::Scene3DSGNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Scene3DSGNode.
  - Each name of Qt's Qt3DRender::Scene3DSGNode that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Scene3DSGNode'

  #  A C++ Qt3DRender::Scene3DSGNode Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Scene3DSGNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *Qt3DRender::Scene3DSGNode::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgnode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *Qt3DRender::Scene3DSGNode::texture() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13Scene3DSGNode7textureEv',
    )
    from ..QtQuick import QSGTexture
    return QSGTexture._cuteAt(address)

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF Qt3DRender::Scene3DSGNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-scene3dsgnode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DRender::Scene3DSGNode::rect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13Scene3DSGNode4rectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DSGNode::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgnode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Scene3DSGNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13Scene3DSGNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(QRectF)
  @overload(QRectF, bool)
  def setRect(self, rect: QRectF, mirrorVertically: bool = False) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DSGNode::setRect(const QRectF &rect,
    bool mirrorVertically)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3dsgnode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    mirrorVertically : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void Qt3DRender::Scene3DSGNode::setRect(const QRectF &rect, bool
    #      mirrorVertically)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13Scene3DSGNode7setRectERK6QRectFb',
        self._valueOf(rect), mirrorVertically,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Scene3DSGNode::Scene3DSGNode()': leans on 'vtable for
    Qt3DRender::Scene3DSGMaterial', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DSGNode.__init__' has no cute function yet. Qt's "
        "'Qt3DRender::Scene3DSGNode::Scene3DSGNode()': leans on 'vtable for "
        "Qt3DRender::Scene3DSGMaterial', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def show(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DSGNode::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-scene3dsgnode.html#show
    """
    #  void Qt3DRender::Scene3DSGNode::show()
    self.uglySide.call('ritual_ZN10Qt3DRender13Scene3DSGNode4showEv')
