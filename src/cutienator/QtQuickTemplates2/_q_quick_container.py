"""
QQuickContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickContainer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQuickContainerPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContainer(QQuickControl):
  """
  The cute side of Qt's QQuickContainer: a plain Python object standing in
  front of one C++ QQuickContainer.

  It is built on the cute 'QQuickControl', as Qt's QQuickContainer is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContainer that has a ritual and that Python
  can call so far, 35 names in all: 'metaObject', 'tr', 'count', 'itemAt',
  'addItem', 'insertItem', 'moveItem', 'removeItem', 'takeItem',
  'contentModel', 'currentIndex', 'currentItem', 'contentWidth',
  'setContentWidth', 'resetContentWidth', 'contentHeight',
  'setContentHeight', 'resetContentHeight', 'setCurrentIndex',
  'incrementCurrentIndex', 'decrementCurrentIndex', 'countChanged',
  'contentChildrenChanged', 'currentIndexChanged', 'currentItemChanged',
  'contentWidthChanged', 'contentHeightChanged', 'componentComplete',
  'itemChange', 'contentItemChange', 'isContent', 'itemAdded', 'itemMoved',
  'itemRemoved', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickContainer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickContainer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickContainer::~QQuickContainer()': the destructor: Python never
    removes a C++ QQuickContainer.
  - Qt's 'QQmlListProperty<QObject> QQuickContainer::contentData()': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickContainer::contentChildren()':
    gives a type Python has no way to take yet.
  - Qt's 'QQuickContainer::QQuickContainer(QQuickContainerPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickContainerPrivate *QQuickContainer::d_func() const':
    takes in Python what 'QQuickContainerPrivate *QQuickContainer::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickContainer is created at the first use, not by
    'QQuickContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContainer.
  - Qt tells when it has removed the C++ QQuickContainer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickContainer that has no cute function yet,
    'contentChildren', 'contentData', holds a function that raises
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
    Calls Qt's 'QString QQuickContainer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#tr

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
    #  QString QQuickContainer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickContainer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContainer'

  #  A C++ QQuickContainer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContainer'

  #  The functions Qt calls itself that QQuickContainer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isContent': (
          ('_ZNK15QQuickContainer9isContentEP10QQuickItem',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemAdded': (
          ('_ZN15QQuickContainer9itemAddedEiP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemMoved': (
          ('_ZN15QQuickContainer9itemMovedEiP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemRemoved': (
          ('_ZN15QQuickContainer11itemRemovedEiP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick:QQuickItem'),
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
    Calls Qt's 'const QMetaObject *QQuickContainer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickContainer::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickContainer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickContainer::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#count
    """
    #  int QQuickContainer::count() const
    return self.uglySide.call('ritual_ZNK15QQuickContainer5countEv')

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickContainer::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#itemAt

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
    #  QQuickItem *QQuickContainer::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickContainer6itemAtEi', index,
    )
    return QQuickItem._cuteAt(address)

  def contentModel(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickContainer::contentModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#contentModel

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickContainer::contentModel() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickContainer12contentModelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickContainer::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#currentIndex
    """
    #  int QQuickContainer::currentIndex() const
    return self.uglySide.call('ritual_ZNK15QQuickContainer12currentIndexEv')

  def currentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickContainer::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#currentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickContainer::currentItem() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickContainer11currentItemEv',
    )
    return QQuickItem._cuteAt(address)

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickContainer::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#contentWidth
    """
    #  qreal QQuickContainer::contentWidth() const
    return self.uglySide.call('ritual_ZNK15QQuickContainer12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickContainer::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#contentHeight
    """
    #  qreal QQuickContainer::contentHeight() const
    return self.uglySide.call('ritual_ZNK15QQuickContainer13contentHeightEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def isContent(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickContainer::isContent(QQuickItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#isContent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickContainer::isContent(QQuickItem *item) const
    ritual = 'ritual_ZNK15QQuickContainer9isContentEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickContainer9isContentEP10QQuickItem'
    return self.uglySide.call(ritual, self._addressOf(item))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setContentWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickContainer::setContentWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#setContentWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickContainer::setContentWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN15QQuickContainer15setContentWidthEd', width,
    )

  @overload(float)
  def setContentHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickContainer::setContentHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#setContentHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickContainer::setContentHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN15QQuickContainer16setContentHeightEd', height,
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickContainer::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickContainer::setCurrentIndex(int index)
    self.uglySide.call(
        'ritual_ZN15QQuickContainer15setCurrentIndexEi', index,
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
    'QQuickContainer::QQuickContainer(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#QQuickContainer

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickContainer::QQuickContainer(QQuickItem *parent)
    self._noteCreation(QQuickContainer, lambda: Rituals.call(
        'ritual_ZN15QQuickContainerC1EP10QQuickItem',
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

  @overload(QQuickItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainer::addItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#addItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::addItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN15QQuickContainer7addItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def insertItem(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainer::insertItem(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::insertItem(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN15QQuickContainer10insertItemEiP10QQuickItem',
        index, self._addressOf(item),
    )

  @overload(int, int)
  def moveItem(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QQuickContainer::moveItem(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#moveItem

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QQuickContainer::moveItem(int from, int to)
    self.uglySide.call('ritual_ZN15QQuickContainer8moveItemEii', from_, to)

  @overload(QQuickItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainer::removeItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#removeItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::removeItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN15QQuickContainer10removeItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(int)
  def takeItem(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickContainer::takeItem(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#takeItem

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
    #  QQuickItem *QQuickContainer::takeItem(int index)
    address = self.uglySide.call(
        'ritual_ZN15QQuickContainer8takeItemEi', index,
    )
    return QQuickItem._cuteAt(address)

  def resetContentWidth(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::resetContentWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#resetContentWidth
    """
    #  void QQuickContainer::resetContentWidth()
    self.uglySide.call('ritual_ZN15QQuickContainer17resetContentWidthEv')

  def resetContentHeight(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::resetContentHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#resetContentHeight
    """
    #  void QQuickContainer::resetContentHeight()
    self.uglySide.call('ritual_ZN15QQuickContainer18resetContentHeightEv')

  def incrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::incrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#incrementCurrentIndex
    """
    #  void QQuickContainer::incrementCurrentIndex()
    self.uglySide.call('ritual_ZN15QQuickContainer21incrementCurrentIndexEv')

  def decrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::decrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#decrementCurrentIndex
    """
    #  void QQuickContainer::decrementCurrentIndex()
    self.uglySide.call('ritual_ZN15QQuickContainer21decrementCurrentIndexEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#countChanged
    """
    #  void QQuickContainer::countChanged()
    self.uglySide.call('ritual_ZN15QQuickContainer12countChangedEv')

  def contentChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::contentChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#contentChildrenChanged
    """
    #  void QQuickContainer::contentChildrenChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickContainer22contentChildrenChangedEv',
    )

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#currentIndexChanged
    """
    #  void QQuickContainer::currentIndexChanged()
    self.uglySide.call('ritual_ZN15QQuickContainer19currentIndexChangedEv')

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#currentItemChanged
    """
    #  void QQuickContainer::currentItemChanged()
    self.uglySide.call('ritual_ZN15QQuickContainer18currentItemChangedEv')

  def contentWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::contentWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#contentWidthChanged
    """
    #  void QQuickContainer::contentWidthChanged()
    self.uglySide.call('ritual_ZN15QQuickContainer19contentWidthChangedEv')

  def contentHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::contentHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#contentHeightChanged
    """
    #  void QQuickContainer::contentHeightChanged()
    self.uglySide.call('ritual_ZN15QQuickContainer20contentHeightChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickContainer::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#componentComplete
    """
    #  void QQuickContainer::componentComplete()
    ritual = 'ritual_ZN15QQuickContainer17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickContainer17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickContainer::itemChange(ItemChange change, const
    ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickContainer::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN15QQuickContainer10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickContainer10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickContainer::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainer.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::contentItemChange(QQuickItem *newItem,
    #      QQuickItem *oldItem)
    ritual = 'ritual_ZN15QQuickContainer17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickContainer17contentItemChangeEP10QQuickItemS'
          '1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainer::itemAdded(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::itemAdded(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickContainer9itemAddedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickContainer9itemAddedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemMoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainer::itemMoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#itemMoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::itemMoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickContainer9itemMovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickContainer9itemMovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainer::itemRemoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainer::itemRemoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickContainer11itemRemovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickContainer11itemRemovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  def d_func(self) -> Optional[QQuickContainerPrivate]:
    """
    Calls Qt's 'QQuickContainerPrivate *QQuickContainer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainer.html#d_func

    Returns
    -------

    Optional[QQuickContainerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContainerPrivate *QQuickContainer::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickContainer6d_funcEv')
    from . import QQuickContainerPrivate
    return QQuickContainerPrivate._cuteAt(address)

  @staticmethod
  def contentChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem> QQuickContainer::contentChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickContainer.contentChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickItem> QQuickContainer::contentChildren()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def contentData(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickContainer::contentData()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickContainer.contentData' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickContainer::contentData()': gives "
        "a type Python has no way to take yet.")
