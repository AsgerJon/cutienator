"""
QQuickRhiItemNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrhiitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickRhiItemNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGSimpleTextureNode, QSGTextureProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QRhiCommandBuffer
  from . import QQuickRhiItemRenderer, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickRhiItemRenderer = WAIT['QQuickRhiItemRenderer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRhiItemNode(QSGTextureProvider, QSGSimpleTextureNode):
  """
  The cute side of Qt's QQuickRhiItemNode: a plain Python object standing in
  front of one C++ QQuickRhiItemNode.

  It is built on the cute 'QSGTextureProvider', as Qt's QQuickRhiItemNode is
  built on Qt's QSGTextureProvider, and has everything that class has. It is
  built on the cute 'QSGSimpleTextureNode' as well, as Qt's QQuickRhiItemNode
  is built on Qt's QSGSimpleTextureNode too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQuickRhiItemNode that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'texture', 'sync',
  'queryCommandBuffer', 'resetColorBufferObjects',
  'resetRenderTargetObjects', 'isValid', 'scheduleUpdate', 'hasRenderer',
  'setRenderer', 'render'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRhiItemNode::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickRhiItemNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickRhiItemNode.

  What to expect
  --------------

  - The C++ QQuickRhiItemNode is created at the first use, not by
    'QQuickRhiItemNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRhiItemNode.
  - Qt tells when it has removed the C++ QQuickRhiItemNode. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickRhiItemNode that has no cute function yet,
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
  __qt_class__ = 'QQuickRhiItemNode'

  #  Qt's QQuickRhiItemNode is built on more than one class. The part of a
  #  C++ QQuickRhiItemNode that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGSimpleTextureNode':
          'ritual_cast_QQuickRhiItemNode_QSGSimpleTextureNode',
  }

  #  A C++ QQuickRhiItemNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRhiItemNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRhiItemNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRhiItemNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickRhiItemNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QQuickRhiItemNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickRhiItemNode::texture() const
    ritual = 'ritual_ZNK17QQuickRhiItemNode7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickRhiItemNode7textureEv'
    address = self.uglySide.call(ritual)
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItemNode::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#isValid
    """
    #  bool QQuickRhiItemNode::isValid() const
    return self.uglySide.call('ritual_ZNK17QQuickRhiItemNode7isValidEv')

  def hasRenderer(self) -> bool:
    """
    Calls Qt's 'bool QQuickRhiItemNode::hasRenderer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#hasRenderer
    """
    #  bool QQuickRhiItemNode::hasRenderer() const
    return self.uglySide.call('ritual_ZNK17QQuickRhiItemNode11hasRendererEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickRhiItemRenderer)
  @overload(NoneType)
  def setRenderer(self, r: Optional[QQuickRhiItemRenderer]) -> None:
    """
    Calls Qt's 'void QQuickRhiItemNode::setRenderer(QQuickRhiItemRenderer
    *r)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#setRenderer

    Parameters
    ----------

    r : Optional[QQuickRhiItemRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRhiItemNode::setRenderer(QQuickRhiItemRenderer *r)
    self.uglySide.call(
        'ritual_ZN17QQuickRhiItemNode11setRendererEP21QQuickRhiItemRenderer',
        self._addressOf(r),
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
    Qt's 'QQuickRhiItemNode::QQuickRhiItemNode(QQuickRhiItem *item)': leans
    on 'QQuickRhiItemNode::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickRhiItemNode.__init__' has no cute function yet. Qt's "
        "'QQuickRhiItemNode::QQuickRhiItemNode(QQuickRhiItem *item)': leans "
        "on 'QQuickRhiItemNode::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
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

  def sync(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItemNode::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#sync
    """
    #  void QQuickRhiItemNode::sync()
    self.uglySide.call('ritual_ZN17QQuickRhiItemNode4syncEv')

  def queryCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer *QQuickRhiItemNode::queryCommandBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemnode.html#queryCommandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QQuickRhiItemNode::queryCommandBuffer()
    address = self.uglySide.call(
        'ritual_ZN17QQuickRhiItemNode18queryCommandBufferEv',
    )
    from ..QtGui import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  def resetColorBufferObjects(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItemNode::resetColorBufferObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemnode.html#resetColorBufferObjects
    """
    #  void QQuickRhiItemNode::resetColorBufferObjects()
    self.uglySide.call(
        'ritual_ZN17QQuickRhiItemNode23resetColorBufferObjectsEv',
    )

  def resetRenderTargetObjects(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItemNode::resetRenderTargetObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemnode.html#resetRenderTargetObjects
    """
    #  void QQuickRhiItemNode::resetRenderTargetObjects()
    self.uglySide.call(
        'ritual_ZN17QQuickRhiItemNode24resetRenderTargetObjectsEv',
    )

  def scheduleUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItemNode::scheduleUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemnode.html#scheduleUpdate
    """
    #  void QQuickRhiItemNode::scheduleUpdate()
    self.uglySide.call('ritual_ZN17QQuickRhiItemNode14scheduleUpdateEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItemNode::render()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemnode.html#render
    """
    #  void QQuickRhiItemNode::render()
    self.uglySide.call('ritual_ZN17QQuickRhiItemNode6renderEv')
