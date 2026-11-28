"""
QQStyleKitLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitLayoutItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMarginsF, QMetaObject
  from ..QtQuick import QQuickItem


class QQStyleKitLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQStyleKitLayoutItem: a plain Python object standing
  in front of one C++ QQStyleKitLayoutItem.

  What exists
  -----------

  Every function of Qt's QQStyleKitLayoutItem that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'item', 'x', 'y',
  'width', 'height', 'alignment', 'margins', 'fillWidth', 'fillHeight',
  'itemChanged', 'xChanged', 'yChanged', 'widthChanged', 'heightChanged',
  'alignmentChanged', 'marginsChanged', 'fillWidthChanged',
  'fillHeightChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitLayoutItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQStyleKitLayoutItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  13 of the 34 functions Qt declares: 10 leans on 'QQStyleKitLayoutItem; 2
  not a gap; 1 leans on 'vtable for QQStyleKitLayoutItem', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QQStyleKitLayoutItem is created at the first use, not by
    'QQStyleKitLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitLayoutItem.
  - Qt tells when it has removed the C++ QQStyleKitLayoutItem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitLayoutItem that has no cute function yet,
    '__init__', 'setAlignment', 'setFillHeight', 'setFillWidth', 'setHeight',
    'setItem', 'setMargins', 'setWidth', 'setX', 'setY', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitLayoutItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitLayoutItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitLayoutItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQStyleKitLayoutItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def item(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQStyleKitLayoutItem::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#item

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQStyleKitLayoutItem::item() const
    address = self.uglySide.call('ritual_ZNK20QQStyleKitLayoutItem4itemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayoutItem::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#x
    """
    #  qreal QQStyleKitLayoutItem::x() const
    return self.uglySide.call('ritual_ZNK20QQStyleKitLayoutItem1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayoutItem::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#y
    """
    #  qreal QQStyleKitLayoutItem::y() const
    return self.uglySide.call('ritual_ZNK20QQStyleKitLayoutItem1yEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayoutItem::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#width
    """
    #  qreal QQStyleKitLayoutItem::width() const
    return self.uglySide.call('ritual_ZNK20QQStyleKitLayoutItem5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayoutItem::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#height
    """
    #  qreal QQStyleKitLayoutItem::height() const
    return self.uglySide.call('ritual_ZNK20QQStyleKitLayoutItem6heightEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QQStyleKitLayoutItem::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QQStyleKitLayoutItem::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK20QQStyleKitLayoutItem9alignmentEv',
    ))

  def margins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQStyleKitLayoutItem::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#margins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQStyleKitLayoutItem::margins() const
    address = self.uglySide.call(
        'ritual_ZNK20QQStyleKitLayoutItem7marginsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def fillWidth(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitLayoutItem::fillWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#fillWidth
    """
    #  bool QQStyleKitLayoutItem::fillWidth() const
    return self.uglySide.call('ritual_ZNK20QQStyleKitLayoutItem9fillWidthEv')

  def fillHeight(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitLayoutItem::fillHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#fillHeight
    """
    #  bool QQStyleKitLayoutItem::fillHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQStyleKitLayoutItem10fillHeightEv',
    )

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
    Qt's 'QQStyleKitLayoutItem::QQStyleKitLayoutItem(QObject *parent)': leans
    on 'vtable for QQStyleKitLayoutItem', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.__init__' has no cute function yet. Qt's "
        "'QQStyleKitLayoutItem::QQStyleKitLayoutItem(QObject *parent)': "
        "leans on 'vtable for QQStyleKitLayoutItem', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
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

  def itemChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::itemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#itemChanged
    """
    #  void QQStyleKitLayoutItem::itemChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem11itemChangedEv')

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#xChanged
    """
    #  void QQStyleKitLayoutItem::xChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#yChanged
    """
    #  void QQStyleKitLayoutItem::yChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem8yChangedEv')

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#widthChanged
    """
    #  void QQStyleKitLayoutItem::widthChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#heightChanged
    """
    #  void QQStyleKitLayoutItem::heightChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem13heightChangedEv')

  def alignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::alignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#alignmentChanged
    """
    #  void QQStyleKitLayoutItem::alignmentChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem16alignmentChangedEv')

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::marginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#marginsChanged
    """
    #  void QQStyleKitLayoutItem::marginsChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem14marginsChangedEv')

  def fillWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::fillWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#fillWidthChanged
    """
    #  void QQStyleKitLayoutItem::fillWidthChanged()
    self.uglySide.call('ritual_ZN20QQStyleKitLayoutItem16fillWidthChangedEv')

  def fillHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayoutItem::fillHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayoutitem.html#fillHeightChanged
    """
    #  void QQStyleKitLayoutItem::fillHeightChanged()
    self.uglySide.call(
        'ritual_ZN20QQStyleKitLayoutItem17fillHeightChangedEv',
    )

  @staticmethod
  def setAlignment(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setAlignment(Qt::Alignment alignment)':
    leans on 'QQStyleKitLayoutItem::alignmentChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setAlignment' has no cute function yet. Qt's "
        "'void QQStyleKitLayoutItem::setAlignment(Qt::Alignment "
        "alignment)': leans on 'QQStyleKitLayoutItem::alignmentChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setFillHeight(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setFillHeight(bool fill)': leans on
    'QQStyleKitLayoutItem::fillHeightChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setFillHeight' has no cute function yet. "
        "Qt's 'void QQStyleKitLayoutItem::setFillHeight(bool fill)': leans "
        "on 'QQStyleKitLayoutItem::fillHeightChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setFillWidth(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setFillWidth(bool fill)': leans on
    'QQStyleKitLayoutItem::fillWidthChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setFillWidth' has no cute function yet. Qt's "
        "'void QQStyleKitLayoutItem::setFillWidth(bool fill)': leans on "
        "'QQStyleKitLayoutItem::fillWidthChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setHeight(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setHeight(qreal height)': leans on
    'QQStyleKitLayoutItem::heightChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setHeight' has no cute function yet. Qt's "
        "'void QQStyleKitLayoutItem::setHeight(qreal height)': leans on "
        "'QQStyleKitLayoutItem::heightChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setItem(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setItem(QQuickItem *item)': leans on
    'QQStyleKitLayoutItem::itemChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setItem' has no cute function yet. Qt's "
        "'void QQStyleKitLayoutItem::setItem(QQuickItem *item)': leans on "
        "'QQStyleKitLayoutItem::itemChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setMargins(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setMargins(const QMarginsF &margins)':
    leans on 'QQStyleKitLayoutItem::marginsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setMargins' has no cute function yet. Qt's "
        "'void QQStyleKitLayoutItem::setMargins(const QMarginsF &margins)': "
        "leans on 'QQStyleKitLayoutItem::marginsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setWidth(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setWidth(qreal width)': leans on
    'QQStyleKitLayoutItem::widthChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setWidth' has no cute function yet. Qt's "
        "'void QQStyleKitLayoutItem::setWidth(qreal width)': leans on "
        "'QQStyleKitLayoutItem::widthChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setX(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setX(qreal x)': leans on
    'QQStyleKitLayoutItem::xChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setX' has no cute function yet. Qt's 'void "
        "QQStyleKitLayoutItem::setX(qreal x)': leans on "
        "'QQStyleKitLayoutItem::xChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setY(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayoutItem::setY(qreal y)': leans on
    'QQStyleKitLayoutItem::yChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayoutItem.setY' has no cute function yet. Qt's 'void "
        "QQStyleKitLayoutItem::setY(qreal y)': leans on "
        "'QQStyleKitLayoutItem::yChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
