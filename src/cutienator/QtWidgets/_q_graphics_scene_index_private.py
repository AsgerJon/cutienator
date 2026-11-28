"""
QGraphicsSceneIndexPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsSceneIndexPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QPainterPath
  from . import QGraphicsItem, QGraphicsScene, QGraphicsSceneIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsScene = WAIT['QGraphicsScene']
  QPainterPath = WAIT['QPainterPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneIndexPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGraphicsSceneIndexPrivate: a plain Python object
  standing in front of one C++ QGraphicsSceneIndexPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QGraphicsSceneIndexPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneIndexPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'q_func', 'init',
  'itemCollidesWithPath'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsSceneIndex *QGraphicsSceneIndexPrivate::q_func()
    const': takes in Python what 'QGraphicsSceneIndex
    *QGraphicsSceneIndexPrivate::q_func()' takes.
  - Qt's 'QGraphicsSceneIndexPrivate::~QGraphicsSceneIndexPrivate()': the
    destructor: Python never removes a C++ QGraphicsSceneIndexPrivate.
  - Qt's 'void
    QGraphicsSceneIndexPrivate::recursive_items_helper(QGraphicsItem *item,
    QRectF exposeRect, QGraphicsSceneIndexIntersector intersect,
    QList<QGraphicsItem *> *items, const QTransform &viewTransform,
    Qt::ItemSelectionMode mode, qreal parentOpacity, const void
    *intersectData) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QGraphicsSceneIndexPrivate::items_helper(const QRectF &rect,
    QGraphicsSceneIndexIntersector intersect, QList<QGraphicsItem *> *items,
    const QTransform &viewTransform, Qt::ItemSelectionMode mode,
    Qt::SortOrder order, const void *intersectData) const': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGraphicsSceneIndexPrivate is created at the first use, not by
    'QGraphicsSceneIndexPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneIndexPrivate.
  - Each name of Qt's QGraphicsSceneIndexPrivate that has no cute function
    yet, 'items_helper', 'recursive_items_helper', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsItem, QPainterPath, Qt.ItemSelectionMode)
  @overload(NoneType, QPainterPath, Qt.ItemSelectionMode)
  def itemCollidesWithPath(
      item: Optional[QGraphicsItem],
      path: QPainterPath,
      mode: Qt.ItemSelectionMode,
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsSceneIndexPrivate::itemCollidesWithPath(const
    QGraphicsItem *item, const QPainterPath &path, Qt::ItemSelectionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindexprivate.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    mode : Qt.ItemSelectionMode
      Passed on as its number.
    """
    #  bool QGraphicsSceneIndexPrivate::itemCollidesWithPath(const
    #      QGraphicsItem *item, const QPainterPath &path,
    #      Qt::ItemSelectionMode mode)
    return Rituals.call(
        'ritual_ZN26QGraphicsSceneIndexPrivate20itemCollidesWithPathEPK13QG'
        'raphicsItemRK12QPainterPathN2Qt17ItemSelectionModeE',
        CuteMixin._addressOf(item, 'QGraphicsItem'),
        CuteMixin._valueOf(path), mode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneIndexPrivate'

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

  @overload(QGraphicsScene)
  @overload(NoneType)
  def __init__(self, scene: Optional[QGraphicsScene]) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSceneIndexPrivate::QGraphicsSceneIndexPrivate(QGraphicsScene
    *scene)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindexprivate.html

    Parameters
    ----------

    scene : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGraphicsSceneIndexPrivate::QGraphicsSceneIndexPrivate(QGraphicsScene
    #      *scene)
    self._noteCreation(QGraphicsSceneIndexPrivate, lambda: Rituals.call(
        'ritual_ZN26QGraphicsSceneIndexPrivateC1EP14QGraphicsScene',
        self._addressOf(scene),
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

  def q_func(self) -> Optional[QGraphicsSceneIndex]:
    """
    Calls Qt's 'QGraphicsSceneIndex *QGraphicsSceneIndexPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindexprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsSceneIndex]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsSceneIndex *QGraphicsSceneIndexPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QGraphicsSceneIndexPrivate6q_funcEv',
    )
    from . import QGraphicsSceneIndex
    return QGraphicsSceneIndex._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndexPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindexprivate.html#init
    """
    #  void QGraphicsSceneIndexPrivate::init()
    self.uglySide.call('ritual_ZN26QGraphicsSceneIndexPrivate4initEv')

  @staticmethod
  def items_helper(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneIndexPrivate::items_helper(const QRectF &rect,
    QGraphicsSceneIndexIntersector intersect, QList<QGraphicsItem *> *items,
    const QTransform &viewTransform, Qt::ItemSelectionMode mode,
    Qt::SortOrder order, const void *intersectData) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsSceneIndexPrivate.items_helper' has no cute function "
        "yet. Qt's 'void QGraphicsSceneIndexPrivate::items_helper(const "
        "QRectF &rect, QGraphicsSceneIndexIntersector intersect, "
        "QList<QGraphicsItem *> *items, const QTransform &viewTransform, "
        "Qt::ItemSelectionMode mode, Qt::SortOrder order, const void "
        "*intersectData) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def recursive_items_helper(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsSceneIndexPrivate::recursive_items_helper(QGraphicsItem *item,
    QRectF exposeRect, QGraphicsSceneIndexIntersector intersect,
    QList<QGraphicsItem *> *items, const QTransform &viewTransform,
    Qt::ItemSelectionMode mode, qreal parentOpacity, const void
    *intersectData) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsSceneIndexPrivate.recursive_items_helper' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsSceneIndexPrivate::recursive_items_helper(QGraphicsItem "
        "*item, QRectF exposeRect, QGraphicsSceneIndexIntersector "
        "intersect, QList<QGraphicsItem *> *items, const QTransform "
        "&viewTransform, Qt::ItemSelectionMode mode, qreal parentOpacity, "
        "const void *intersectData) const': takes a type Python has no way "
        "to hand over yet.")
