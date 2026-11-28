"""
SGFramebufferObjectNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means SGFramebufferObjectNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtQuick import QSGSimpleTextureNode, QSGTextureProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick import QSGTexture


class SGFramebufferObjectNode(QSGTextureProvider, QSGSimpleTextureNode):
  """
  The cute side of Qt's SGFramebufferObjectNode: a plain Python object
  standing in front of one C++ SGFramebufferObjectNode.

  It is built on the cute 'QSGTextureProvider', as Qt's
  SGFramebufferObjectNode is built on Qt's QSGTextureProvider, and has
  everything that class has. It is built on the cute 'QSGSimpleTextureNode'
  as well, as Qt's SGFramebufferObjectNode is built on Qt's
  QSGSimpleTextureNode too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's SGFramebufferObjectNode that has a ritual and that
  Python can call so far, 2 names in all: 'scheduleRender', 'texture'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SGFramebufferObjectNode::~SGFramebufferObjectNode()': the
    destructor: Python never removes a C++ SGFramebufferObjectNode.

  What has no ritual
  ------------------

  10 of the 13 functions Qt declares: 6 leans on 'SGFramebufferObjectNode; 2
  not a gap; 1 leans on 'vtable for SGFramebufferObjectNode', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken; 1 leans on 'QQuick3DSceneRenderer.

  What to expect
  --------------

  - The C++ SGFramebufferObjectNode is created at the first use, not by
    'SGFramebufferObjectNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SGFramebufferObjectNode.
  - Qt tells when it has removed the C++ SGFramebufferObjectNode. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's SGFramebufferObjectNode that has no cute function yet,
    '__init__', 'handleScreenChange', 'render', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SGFramebufferObjectNode'

  #  Qt's SGFramebufferObjectNode is built on more than one class. The part
  #  of a C++ SGFramebufferObjectNode that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGSimpleTextureNode':
          'ritual_cast_SGFramebufferObjectNode_QSGSimpleTextureNode',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *SGFramebufferObjectNode::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sgframebufferobjectnode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *SGFramebufferObjectNode::texture() const
    address = self.uglySide.call(
        'ritual_ZNK23SGFramebufferObjectNode7textureEv',
    )
    from ..QtQuick import QSGTexture
    return QSGTexture._cuteAt(address)

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
    Qt's 'SGFramebufferObjectNode::SGFramebufferObjectNode()': leans on
    'vtable for SGFramebufferObjectNode', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SGFramebufferObjectNode.__init__' has no cute function yet. Qt's "
        "'SGFramebufferObjectNode::SGFramebufferObjectNode()': leans on "
        "'vtable for SGFramebufferObjectNode', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def scheduleRender(self) -> None:
    """
    Calls Qt's 'void SGFramebufferObjectNode::scheduleRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/sgframebufferobjectnode.html#scheduleRender
    """
    #  void SGFramebufferObjectNode::scheduleRender()
    self.uglySide.call(
        'ritual_ZN23SGFramebufferObjectNode14scheduleRenderEv',
    )

  @staticmethod
  def handleScreenChange(*__, **_) -> Never:
    """
    Qt's 'void SGFramebufferObjectNode::handleScreenChange()': leans on
    'SGFramebufferObjectNode::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'SGFramebufferObjectNode.handleScreenChange' has no cute function "
        "yet. Qt's 'void SGFramebufferObjectNode::handleScreenChange()': "
        "leans on 'SGFramebufferObjectNode::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void SGFramebufferObjectNode::render()': leans on
    'SGFramebufferObjectNode::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'SGFramebufferObjectNode.render' has no cute function yet. Qt's "
        "'void SGFramebufferObjectNode::render()': leans on "
        "'SGFramebufferObjectNode::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
