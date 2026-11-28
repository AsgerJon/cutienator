"""
QQuickStackLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickstacklayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickLayout
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QQuickStackLayoutAttached, QQuickStackLayoutPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackLayout(QQuickLayout):
  """
  The cute side of Qt's QQuickStackLayout: a plain Python object standing in
  front of one C++ QQuickStackLayout.

  It is built on the cute 'QQuickLayout', as Qt's QQuickStackLayout is built
  on Qt's QQuickLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStackLayout that has a ritual and that Python
  can call so far, 23 names in all: 'metaObject', 'tr', 'count',
  'currentIndex', 'setCurrentIndex', 'componentComplete', 'itemChange',
  'sizeHint', 'setAlignment', 'invalidate', 'updateLayoutItems', 'rearrange',
  'setStretchFactor', 'itemAt', 'itemCount', 'indexOf',
  'itemSiblingOrderChanged', 'qmlAttachedProperties', 'currentIndexChanged',
  'countChanged', 'collectItemSizeHints', 'shouldIgnoreItem', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStackLayout::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickStackLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickStackLayout::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickStackLayout::childItemsChanged(AdjustCurrentIndexPolicy
    adjustCurrentIndexPolicy)': names the enum
    'QQuickStackLayout::AdjustCurrentIndexPolicy', whose class cannot be
    named here.
  - Qt's 'const QQuickStackLayoutPrivate *QQuickStackLayout::d_func() const':
    takes in Python what 'QQuickStackLayoutPrivate
    *QQuickStackLayout::d_func()' takes.
  - Qt's 'SizeHints &QQuickStackLayout::cachedItemSizeHints(int index)
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickStackLayout is created at the first use, not by
    'QQuickStackLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStackLayout.
  - Qt tells when it has removed the C++ QQuickStackLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickStackLayout that has no cute function yet,
    'cachedItemSizeHints', 'childItemsChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickStackLayout::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStackLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickStackLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickStackLayoutAttached]:
    """
    Calls Qt's 'QQuickStackLayoutAttached
    *QQuickStackLayout::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickStackLayoutAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackLayoutAttached
    #      *QQuickStackLayout::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN17QQuickStackLayout21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickStackLayoutAttached
    return QQuickStackLayoutAttached._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, QSizeF)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QSizeF)
  @overload(NoneType, NoneType)
  def collectItemSizeHints(
      item: Optional[QQuickItem],
      sizeHints: Optional[QSizeF],
  ) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::collectItemSizeHints(QQuickItem
    *item, QSizeF *sizeHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#collectItemSizeHints

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sizeHints : Optional[QSizeF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackLayout::collectItemSizeHints(QQuickItem *item, QSizeF
    #      *sizeHints)
    Rituals.call(
        'ritual_ZN17QQuickStackLayout20collectItemSizeHintsEP10QQuickItemP6'
        'QSizeF',
        CuteMixin._addressOf(item), CuteMixin._addressOf(sizeHints),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStackLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStackLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickStackLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickStackLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#count
    """
    #  int QQuickStackLayout::count() const
    return self.uglySide.call('ritual_ZNK17QQuickStackLayout5countEv')

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickStackLayout::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#currentIndex
    """
    #  int QQuickStackLayout::currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickStackLayout12currentIndexEv',
    )

  @overload(Qt.SizeHint)
  def sizeHint(self, whichSizeHint: Qt.SizeHint) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickStackLayout::sizeHint(Qt::SizeHint
    whichSizeHint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#sizeHint

    Parameters
    ----------

    whichSizeHint : Qt.SizeHint
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickStackLayout::sizeHint(Qt::SizeHint whichSizeHint) const
    ritual = 'ritual_ZNK17QQuickStackLayout8sizeHintEN2Qt8SizeHintE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickStackLayout8sizeHintEN2Qt8SizeHintE'
    address = self.uglySide.call(ritual, whichSizeHint.value)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackLayout::itemAt(int index) const
    ritual = 'ritual_ZNK17QQuickStackLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickStackLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QQuickItem._cuteAt(address)

  def itemCount(self) -> int:
    """
    Calls Qt's 'int QQuickStackLayout::itemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#itemCount
    """
    #  int QQuickStackLayout::itemCount() const
    ritual = 'ritual_ZNK17QQuickStackLayout9itemCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickStackLayout9itemCountEv'
    return self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def indexOf(self, item: Optional[QQuickItem]) -> int:
    """
    Calls Qt's 'int QQuickStackLayout::indexOf(QQuickItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#indexOf

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickStackLayout::indexOf(QQuickItem *item) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickStackLayout7indexOfEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def shouldIgnoreItem(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickStackLayout::shouldIgnoreItem(QQuickItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#shouldIgnoreItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickStackLayout::shouldIgnoreItem(QQuickItem *item) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickStackLayout16shouldIgnoreItemEP10QQuickItem',
        self._addressOf(item),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickStackLayout::setCurrentIndex(int index)
    self.uglySide.call(
        'ritual_ZN17QQuickStackLayout15setCurrentIndexEi', index,
    )

  @overload(QQuickItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      item: Optional[QQuickItem],
      align: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::setAlignment(QQuickItem *item,
    Qt::Alignment align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#setAlignment

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    align : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickStackLayout::setAlignment(QQuickItem *item, Qt::Alignment
    #      align)
    ritual = (
        'ritual_ZN17QQuickStackLayout12setAlignmentEP10QQuickItem6QFlagsIN2'
        'Qt13AlignmentFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickStackLayout12setAlignmentEP10QQuickItem6QFl'
          'agsIN2Qt13AlignmentFlagEE')
    self.uglySide.call(ritual, self._addressOf(item), align.value)

  @overload(QQuickItem, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def setStretchFactor(
      self,
      item: Optional[QQuickItem],
      stretchFactor: int,
      orient: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::setStretchFactor(QQuickItem *item,
    int stretchFactor, Qt::Orientation orient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#setStretchFactor

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretchFactor : int
      Passed on as it is.

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickStackLayout::setStretchFactor(QQuickItem *item, int
    #      stretchFactor, Qt::Orientation orient)
    ritual = (
        'ritual_ZN17QQuickStackLayout16setStretchFactorEP10QQuickItemiN2Qt1'
        '1OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickStackLayout16setStretchFactorEP10QQuickItem'
          'iN2Qt11OrientationE')
    self.uglySide.call(
        ritual, self._addressOf(item), stretchFactor, orient.value,
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackLayout::QQuickStackLayout(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#QQuickStackLayout

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStackLayout::QQuickStackLayout(QQuickItem *parent)
    self._noteCreation(QQuickStackLayout, lambda: Rituals.call(
        'ritual_ZN17QQuickStackLayoutC1EP10QQuickItem',
        self._addressOf(parent),
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#componentComplete
    """
    #  void QQuickStackLayout::componentComplete()
    ritual = 'ritual_ZN17QQuickStackLayout17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickStackLayout17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickStackLayout::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN17QQuickStackLayout10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickStackLayout10itemChangeEN10QQuickItem10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def invalidate(self, childItem: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::invalidate(QQuickItem *childItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#invalidate

    Parameters
    ----------

    childItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickStackLayout::invalidate(QQuickItem *childItem)
    ritual = 'ritual_ZN17QQuickStackLayout10invalidateEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickStackLayout10invalidateEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(childItem))

  def updateLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::updateLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#updateLayoutItems
    """
    #  void QQuickStackLayout::updateLayoutItems()
    ritual = 'ritual_ZN17QQuickStackLayout17updateLayoutItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickStackLayout17updateLayoutItemsEv'
    self.uglySide.call(ritual)

  @overload(QSizeF)
  def rearrange(self, a0: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::rearrange(const QSizeF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#rearrange

    Parameters
    ----------

    a0 : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickStackLayout::rearrange(const QSizeF &a0)
    ritual = 'ritual_ZN17QQuickStackLayout9rearrangeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickStackLayout9rearrangeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::itemSiblingOrderChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#itemSiblingOrderChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackLayout::itemSiblingOrderChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickStackLayout23itemSiblingOrderChangedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickStackLayout23itemSiblingOrderChangedEP10QQu'
          'ickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#currentIndexChanged
    """
    #  void QQuickStackLayout::currentIndexChanged()
    self.uglySide.call('ritual_ZN17QQuickStackLayout19currentIndexChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayout::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayout.html#countChanged
    """
    #  void QQuickStackLayout::countChanged()
    self.uglySide.call('ritual_ZN17QQuickStackLayout12countChangedEv')

  def d_func(self) -> Optional[QQuickStackLayoutPrivate]:
    """
    Calls Qt's 'QQuickStackLayoutPrivate *QQuickStackLayout::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayout.html#d_func

    Returns
    -------

    Optional[QQuickStackLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackLayoutPrivate *QQuickStackLayout::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickStackLayout6d_funcEv')
    from . import QQuickStackLayoutPrivate
    return QQuickStackLayoutPrivate._cuteAt(address)

  @staticmethod
  def cachedItemSizeHints(*__, **_) -> Never:
    """
    Qt's 'SizeHints &QQuickStackLayout::cachedItemSizeHints(int index)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickStackLayout.cachedItemSizeHints' has no cute function yet. "
        "Qt's 'SizeHints &QQuickStackLayout::cachedItemSizeHints(int index) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def childItemsChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackLayout::childItemsChanged(AdjustCurrentIndexPolicy
    adjustCurrentIndexPolicy)': names the enum
    'QQuickStackLayout::AdjustCurrentIndexPolicy', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QQuickStackLayout.childItemsChanged' has no cute function yet. "
        "Qt's 'void "
        "QQuickStackLayout::childItemsChanged(AdjustCurrentIndexPolicy "
        "adjustCurrentIndexPolicy)': names the enum "
        "'QQuickStackLayout::AdjustCurrentIndexPolicy', whose class cannot "
        "be named here.")
