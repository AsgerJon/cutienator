"""
QGraphicsSceneIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsSceneIndex to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QList, QObject
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QPainterPath, QPolygonF, QTransform
  from . import QGraphicsScene, QGraphicsSceneIndexPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QPointF = WAIT['QPointF']
  QPolygonF = WAIT['QPolygonF']
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSceneIndex(QObject):
  """
  The cute side of Qt's QGraphicsSceneIndex: a plain Python object standing
  in front of one C++ QGraphicsSceneIndex.

  It is built on the cute 'QObject', as Qt's QGraphicsSceneIndex is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneIndex that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'scene', 'items',
  'estimateItems', 'estimateTopLevelItems', 'updateSceneRect', 'clear',
  'addItem', 'removeItem', 'deleteItem', 'prepareBoundingRectChange',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsSceneIndex::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGraphicsSceneIndex::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsSceneIndex::~QGraphicsSceneIndex()': the destructor:
    Python never removes a C++ QGraphicsSceneIndex.
  - Qt's 'void QGraphicsSceneIndex::itemChange(const QGraphicsItem *item,
    QGraphicsItem::GraphicsItemChange a1, const void *const value)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QGraphicsSceneIndexPrivate *QGraphicsSceneIndex::d_func()
    const': takes in Python what 'QGraphicsSceneIndexPrivate
    *QGraphicsSceneIndex::d_func()' takes.

  What has no ritual
  ------------------

  9 of the 31 functions Qt declares: 4 forbidden; 2 not a gap; 2 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open; 1 leans on 'QGraphicsSceneIndex.

  What to expect
  --------------

  - The C++ QGraphicsSceneIndex is created at the first use, not by
    'QGraphicsSceneIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneIndex.
  - Qt tells when it has removed the C++ QGraphicsSceneIndex. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphicsSceneIndex that has no cute function yet,
    '__init__', 'itemChange', holds a function that raises
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
  __qt_class__ = 'QGraphicsSceneIndex'

  #  A C++ QGraphicsSceneIndex Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneIndex'

  #  The functions Qt calls itself that QGraphicsSceneIndex is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'items': (
          'QList<QGraphicsItem *> '
          'QGraphicsSceneIndex::items(Qt::SortOrder) const',
          'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPointF '
          '&, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform &) '
          'const',
          'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QRectF '
          '&, Qt::ItemSelectionMode, Qt::SortOrder, const QTransform &) '
          'const',
          'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const '
          'QPolygonF &, Qt::ItemSelectionMode, Qt::SortOrder, const '
          'QTransform &) const',
          'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const '
          'QPainterPath &, Qt::ItemSelectionMode, Qt::SortOrder, const '
          'QTransform &) const',
      ),
      'estimateItems': (
          'QList<QGraphicsItem *> QGraphicsSceneIndex::estimateItems(const '
          'QPointF &, Qt::SortOrder) const',
          'QList<QGraphicsItem *> QGraphicsSceneIndex::estimateItems(const '
          'QRectF &, Qt::SortOrder) const',
      ),
      'estimateTopLevelItems': (
          'QList<QGraphicsItem *> '
          'QGraphicsSceneIndex::estimateTopLevelItems(const QRectF &, '
          'Qt::SortOrder) const',
      ),
      'itemChange': (
          'void QGraphicsSceneIndex::itemChange(const QGraphicsItem *, '
          'QGraphicsItem::GraphicsItemChange, const void *const)',
      ),
  }

  #  The functions Qt calls itself that QGraphicsSceneIndex is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateSceneRect': (
          ('_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'clear': (
          ('_ZN19QGraphicsSceneIndex5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addItem': (
          ('_ZN19QGraphicsSceneIndex7addItemEP13QGraphicsItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
           )),
      ),
      'removeItem': (
          ('_ZN19QGraphicsSceneIndex10removeItemEP13QGraphicsItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
           )),
      ),
      'deleteItem': (
          ('_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
           )),
      ),
      'prepareBoundingRectChange': (
          ('_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGraphi'
           'csItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsSceneIndex::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsSceneIndex::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scene(self) -> Optional[QGraphicsScene]:
    """
    Calls Qt's 'QGraphicsScene *QGraphicsSceneIndex::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#scene

    Returns
    -------

    Optional[QGraphicsScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsScene *QGraphicsSceneIndex::scene() const
    address = self.uglySide.call('ritual_ZNK19QGraphicsSceneIndex5sceneEv')
    from . import QGraphicsScene
    return QGraphicsScene._cuteAt(address)

  @overload()
  @overload(Qt.SortOrder)
  def items(
      self,
      order: Qt.SortOrder = Qt.SortOrder.DescendingOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneIndex::items(Qt::SortOrder order) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#items

    Parameters
    ----------

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.DescendingOrder.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::items(Qt::SortOrder order)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex5itemsEN2Qt9SortOrderE', order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPointF, Qt.ItemSelectionMode, Qt.SortOrder)
  @overload(QPointF, Qt.ItemSelectionMode, Qt.SortOrder, QTransform)
  def items(
      self,
      pos: QPointF,
      mode: Qt.ItemSelectionMode,
      order: Qt.SortOrder,
      deviceTransform: Optional[QTransform] = None,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const
    QPointF &pos, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
    QTransform &deviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#items

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    mode : Qt.ItemSelectionMode
      Passed on as its number.

    order : Qt.SortOrder
      Passed on as its number.

    deviceTransform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPointF &pos,
    #      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
    #      &deviceTransform) const
    if deviceTransform is None:
      from ..QtGui import QTransform
      deviceTransform = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex5itemsERK7QPointFN2Qt17ItemSelectio'
        'nModeENS3_9SortOrderERK10QTransform',
        self._valueOf(pos, 'QPointF'), mode.value, order.value,
        self._valueOf(deviceTransform),
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QRectF, Qt.ItemSelectionMode, Qt.SortOrder)
  @overload(QRectF, Qt.ItemSelectionMode, Qt.SortOrder, QTransform)
  def items(
      self,
      rect: QRectF,
      mode: Qt.ItemSelectionMode,
      order: Qt.SortOrder,
      deviceTransform: Optional[QTransform] = None,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const
    QRectF &rect, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
    QTransform &deviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#items

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    mode : Qt.ItemSelectionMode
      Passed on as its number.

    order : Qt.SortOrder
      Passed on as its number.

    deviceTransform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QRectF &rect,
    #      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
    #      &deviceTransform) const
    if deviceTransform is None:
      from ..QtGui import QTransform
      deviceTransform = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex5itemsERK6QRectFN2Qt17ItemSelection'
        'ModeENS3_9SortOrderERK10QTransform',
        self._valueOf(rect), mode.value, order.value,
        self._valueOf(deviceTransform),
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPolygonF, Qt.ItemSelectionMode, Qt.SortOrder)
  @overload(QPolygonF, Qt.ItemSelectionMode, Qt.SortOrder, QTransform)
  def items(
      self,
      polygon: QPolygonF,
      mode: Qt.ItemSelectionMode,
      order: Qt.SortOrder,
      deviceTransform: Optional[QTransform] = None,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const
    QPolygonF &polygon, Qt::ItemSelectionMode mode, Qt::SortOrder order,
    const QTransform &deviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#items

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    mode : Qt.ItemSelectionMode
      Passed on as its number.

    order : Qt.SortOrder
      Passed on as its number.

    deviceTransform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPolygonF
    #      &polygon, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
    #      QTransform &deviceTransform) const
    if deviceTransform is None:
      from ..QtGui import QTransform
      deviceTransform = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex5itemsERK9QPolygonFN2Qt17ItemSelect'
        'ionModeENS3_9SortOrderERK10QTransform',
        self._valueOf(polygon), mode.value, order.value,
        self._valueOf(deviceTransform),
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPainterPath, Qt.ItemSelectionMode, Qt.SortOrder)
  @overload(QPainterPath, Qt.ItemSelectionMode, Qt.SortOrder, QTransform)
  def items(
      self,
      path: QPainterPath,
      mode: Qt.ItemSelectionMode,
      order: Qt.SortOrder,
      deviceTransform: Optional[QTransform] = None,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsSceneIndex::items(const
    QPainterPath &path, Qt::ItemSelectionMode mode, Qt::SortOrder order,
    const QTransform &deviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#items

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    mode : Qt.ItemSelectionMode
      Passed on as its number.

    order : Qt.SortOrder
      Passed on as its number.

    deviceTransform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPainterPath
    #      &path, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
    #      QTransform &deviceTransform) const
    if deviceTransform is None:
      from ..QtGui import QTransform
      deviceTransform = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex5itemsERK12QPainterPathN2Qt17ItemSe'
        'lectionModeENS3_9SortOrderERK10QTransform',
        self._valueOf(path), mode.value, order.value,
        self._valueOf(deviceTransform),
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPointF, Qt.SortOrder)
  def estimateItems(
      self,
      point: QPointF,
      order: Qt.SortOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneIndex::estimateItems(const QPointF &point, Qt::SortOrder
    order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#estimateItems

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    order : Qt.SortOrder
      Passed on as its number.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::estimateItems(const
    #      QPointF &point, Qt::SortOrder order) const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex13estimateItemsERK7QPointFN2Qt9Sort'
        'OrderE',
        self._valueOf(point, 'QPointF'), order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QRectF, Qt.SortOrder)
  def estimateItems(
      self,
      rect: QRectF,
      order: Qt.SortOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneIndex::estimateItems(const QRectF &rect, Qt::SortOrder
    order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#estimateItems

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    order : Qt.SortOrder
      Passed on as its number.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsSceneIndex::estimateItems(const QRectF
    #      &rect, Qt::SortOrder order) const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex13estimateItemsERK6QRectFN2Qt9SortO'
        'rderE',
        self._valueOf(rect), order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QRectF, Qt.SortOrder)
  def estimateTopLevelItems(
      self,
      a0: QRectF,
      order: Qt.SortOrder,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsSceneIndex::estimateTopLevelItems(const QRectF &a0,
    Qt::SortOrder order) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#estimateTopLevelItems

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    order : Qt.SortOrder
      Passed on as its number.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *>
    #      QGraphicsSceneIndex::estimateTopLevelItems(const QRectF &a0,
    #      Qt::SortOrder order) const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsSceneIndex21estimateTopLevelItemsERK6QRectFN2'
        'Qt9SortOrderE',
        self._valueOf(a0), order.value,
    )
    return QList[QGraphicsItem]._cuteOwning(address)

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
    - Qt's 'QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsScene *scene)':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
    - Qt's
      'QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsSceneIndexPrivate
      &dd, QGraphicsScene *scene)': the class is abstract, so C++ cannot make
      one, and the C++ class of ours does not fill in every function it
      leaves open.
    """
    raise NotImplementedError(
        "'QGraphicsSceneIndex.__init__' has no cute function yet. Qt's "
        "'QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsScene *scene)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open. Qt's "
        "'QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsSceneIndexPrivat"
        "e &dd, QGraphicsScene *scene)': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(QRectF)
  def updateSceneRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndex::updateSceneRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#updateSceneRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsSceneIndex::updateSceneRect(const QRectF &rect)
    ritual = 'ritual_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  def clear(self) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndex::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#clear
    """
    #  void QGraphicsSceneIndex::clear()
    ritual = 'ritual_ZN19QGraphicsSceneIndex5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsSceneIndex5clearEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndex::addItem(QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneIndex::addItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN19QGraphicsSceneIndex7addItemEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndex::removeItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#removeItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneIndex::removeItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN19QGraphicsSceneIndex10removeItemEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def deleteItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#deleteItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
    ritual = 'ritual_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem')
    self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def prepareBoundingRectChange(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsSceneIndex::prepareBoundingRectChange(const
    QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneindex.html#prepareBoundingRectChange

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSceneIndex::prepareBoundingRectChange(const
    #      QGraphicsItem *item)
    ritual = (
        'ritual_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGra'
        'phicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK'
          '13QGraphicsItem')
    self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def d_func(self) -> Optional[QGraphicsSceneIndexPrivate]:
    """
    Calls Qt's 'QGraphicsSceneIndexPrivate *QGraphicsSceneIndex::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneindex.html#d_func

    Returns
    -------

    Optional[QGraphicsSceneIndexPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsSceneIndexPrivate *QGraphicsSceneIndex::d_func()
    address = self.uglySide.call('ritual_ZN19QGraphicsSceneIndex6d_funcEv')
    from . import QGraphicsSceneIndexPrivate
    return QGraphicsSceneIndexPrivate._cuteAt(address)

  @staticmethod
  def itemChange(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneIndex::itemChange(const QGraphicsItem *item,
    QGraphicsItem::GraphicsItemChange a1, const void *const value)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsSceneIndex.itemChange' has no cute function yet. Qt's "
        "'void QGraphicsSceneIndex::itemChange(const QGraphicsItem *item, "
        "QGraphicsItem::GraphicsItemChange a1, const void *const value)': "
        "takes a type Python has no way to hand over yet.")
