"""
QQuick3DItem2D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ditem2d_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DItem2D to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..QtQuick import QQuickItemChangeListener
from . import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickItem
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DItem2D(QQuick3DNode, QQuickItemChangeListener):
  """
  The cute side of Qt's QQuick3DItem2D: a plain Python object standing in
  front of one C++ QQuick3DItem2D.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DItem2D is built on
  Qt's QQuick3DNode, and has everything that class has. It is built on the
  cute 'QQuickItemChangeListener' as well, as Qt's QQuick3DItem2D is built on
  Qt's QQuickItemChangeListener too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DItem2D that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'contentItem', 'itemDestroyed',
  'updatePicking', 'derefWindow', 'allChildrenRemoved', 'preSync',
  'updateSpatialNode', 'markAllDirty'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DItem2D::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DItem2D::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DItem2D::~QQuick3DItem2D()': the destructor: Python never
    removes a C++ QQuick3DItem2D.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 4 leans on 'QQuick3DItem2D; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DItem2D is created at the first use, not by
    'QQuick3DItem2D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DItem2D.
  - Qt tells when it has removed the C++ QQuick3DItem2D. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DItem2D that has no cute function yet,
    '__init__', 'addChildItem', 'removeChildItem', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DItem2D'

  #  Qt's QQuick3DItem2D is built on more than one class. The part of a C++
  #  QQuick3DItem2D that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemChangeListener':
          'ritual_cast_QQuick3DItem2D_QQuickItemChangeListener',
  }

  #  A C++ QQuick3DItem2D Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DItem2D'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DItem2D::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DItem2D::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DItem2D10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuick3DItem2D::contentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuick3DItem2D::contentItem() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DItem2D11contentItemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

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
    Qt's 'QQuick3DItem2D::QQuick3DItem2D(QQuickItem *item, QQuick3DNode
    *parent)': leans on 'QQuick3DItem2D::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DItem2D.__init__' has no cute function yet. Qt's "
        "'QQuick3DItem2D::QQuick3DItem2D(QQuickItem *item, QQuick3DNode "
        "*parent)': leans on "
        "'QQuick3DItem2D::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuick3DItem2D::itemDestroyed(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DItem2D::itemDestroyed(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN14QQuick3DItem2D13itemDestroyedEP10QQuickItem',
        self._addressOf(item),
    )

  def updatePicking(self) -> None:
    """
    Calls Qt's 'void QQuick3DItem2D::updatePicking()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#updatePicking
    """
    #  void QQuick3DItem2D::updatePicking()
    self.uglySide.call('ritual_ZN14QQuick3DItem2D13updatePickingEv')

  @overload(QObject)
  @overload(NoneType)
  def derefWindow(self, win: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DItem2D::derefWindow(QObject *win)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#derefWindow

    Parameters
    ----------

    win : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DItem2D::derefWindow(QObject *win)
    self.uglySide.call(
        'ritual_ZN14QQuick3DItem2D11derefWindowEP7QObject',
        self._addressOf(win, 'QObject'),
    )

  def allChildrenRemoved(self) -> None:
    """
    Calls Qt's 'void QQuick3DItem2D::allChildrenRemoved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ditem2d.html#allChildrenRemoved
    """
    #  void QQuick3DItem2D::allChildrenRemoved()
    self.uglySide.call('ritual_ZN14QQuick3DItem2D18allChildrenRemovedEv')

  def preSync(self) -> None:
    """
    Calls Qt's 'void QQuick3DItem2D::preSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#preSync
    """
    #  void QQuick3DItem2D::preSync()
    ritual = 'ritual_ZN14QQuick3DItem2D7preSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DItem2D7preSyncEv'
    self.uglySide.call(ritual)

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DItem2D::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ditem2d.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DItem2D::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN14QQuick3DItem2D17updateSpatialNodeEP21QSSGRenderGraphObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuick3DItem2D17updateSpatialNodeEP21QSSGRenderGr'
          'aphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DItem2D::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ditem2d.html#markAllDirty
    """
    #  void QQuick3DItem2D::markAllDirty()
    ritual = 'ritual_ZN14QQuick3DItem2D12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DItem2D12markAllDirtyEv'
    self.uglySide.call(ritual)

  @staticmethod
  def addChildItem(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DItem2D::addChildItem(QQuickItem *item)': leans on
    'QQuick3DItem2D::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DItem2D.addChildItem' has no cute function yet. Qt's 'void "
        "QQuick3DItem2D::addChildItem(QQuickItem *item)': leans on "
        "'QQuick3DItem2D::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def removeChildItem(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DItem2D::removeChildItem(QQuickItem *item)': leans on
    'QQuick3DItem2D::allChildrenRemoved()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DItem2D.removeChildItem' has no cute function yet. Qt's "
        "'void QQuick3DItem2D::removeChildItem(QQuickItem *item)': leans on "
        "'QQuick3DItem2D::allChildrenRemoved()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
