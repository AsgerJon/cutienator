"""
QQuickShapeGenericStrokeFillNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeGenericStrokeFillNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeGenericStrokeFillNode(QObject):
  """
  The cute side of Qt's QQuickShapeGenericStrokeFillNode: a plain Python
  object standing in front of one C++ QQuickShapeGenericStrokeFillNode.

  It is built on the cute 'QObject', as Qt's QQuickShapeGenericStrokeFillNode
  is built on Qt's QObject, and has everything that class has. Qt's
  QQuickShapeGenericStrokeFillNode is built on Qt's QSGGeometryNode as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickShapeGenericStrokeFillNode that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject',
  'activateMaterial', 'preprocess', 'handleTextureChanged',
  'handleTextureProviderDestroyed'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShapeGenericStrokeFillNode::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickShapeGenericStrokeFillNode::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickShapeGenericStrokeFillNode; 1 leans on 'vtable for
  QQuickShapeGenericStrokeFillNode', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickShapeGenericStrokeFillNode is created at the first use, not
    by 'QQuickShapeGenericStrokeFillNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeGenericStrokeFillNode.
  - Qt tells when it has removed the C++ QQuickShapeGenericStrokeFillNode.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickShapeGenericStrokeFillNode that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickShapeGenericStrokeFillNode, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Material(CuteNum):
    """
    The enum 'QQuickShapeGenericStrokeFillNode::Material' of Qt, with the 5
    names Qt gives in it.
    """

    MatSolidColor = Kee[int](0)
    MatLinearGradient = Kee[int](1)
    MatRadialGradient = Kee[int](2)
    MatConicalGradient = Kee[int](3)
    MatTextureFill = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeGenericStrokeFillNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickShapeGenericStrokeFillNode::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericstrokefillnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShapeGenericStrokeFillNode::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickShapeGenericStrokeFillNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QQuickShapeGenericStrokeFillNode::QQuickShapeGenericStrokeFillNode(
    QQuickWindow *window)': leans on 'vtable for
    QQuickShapeGenericStrokeFillNode', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShapeGenericStrokeFillNode.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickShapeGenericStrokeFillNode::QQuickShapeGenericStrokeFillNode"
        "(QQuickWindow *window)': leans on 'vtable for "
        "QQuickShapeGenericStrokeFillNode', which Qt's source does not mark "
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

  @overload(QQuickWindow, Material)
  @overload(NoneType, Material)
  def activateMaterial(
      self,
      window: Optional[QQuickWindow],
      m: Material,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickShapeGenericStrokeFillNode::activateMaterial(QQuickWindow *window,
    Material m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericstrokefillnode.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : Material
      Passed on as its number.
    """
    #  void QQuickShapeGenericStrokeFillNode::activateMaterial(QQuickWindow
    #      *window, Material m)
    self.uglySide.call(
        'ritual_ZN32QQuickShapeGenericStrokeFillNode16activateMaterialEP12Q'
        'QuickWindowNS_8MaterialE',
        self._addressOf(window), m.value,
    )

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QQuickShapeGenericStrokeFillNode::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericstrokefillnode.html#preprocess
    """
    #  void QQuickShapeGenericStrokeFillNode::preprocess()
    ritual = 'ritual_ZN32QQuickShapeGenericStrokeFillNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickShapeGenericStrokeFillNode10preprocessEv')
    self.uglySide.call(ritual)

  def handleTextureChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickShapeGenericStrokeFillNode::handleTextureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericstrokefillnode.html
    """
    #  void QQuickShapeGenericStrokeFillNode::handleTextureChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickShapeGenericStrokeFillNode20handleTextureChangedE'
        'v',
    )

  def handleTextureProviderDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericstrokefillnode.html
    """
    #  void
    #      QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed()
    self.uglySide.call(
        'ritual_ZN32QQuickShapeGenericStrokeFillNode30handleTextureProvider'
        'DestroyedEv',
    )
