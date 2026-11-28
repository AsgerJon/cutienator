"""
QQuickContainerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickContainerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick import QQuickItem
  from . import QQuickContainer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickContainer = WAIT['QQuickContainer']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContainerPrivate(QQuickControlPrivate):
  """
  The cute side of Qt's QQuickContainerPrivate: a plain Python object
  standing in front of one C++ QQuickContainerPrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's
  QQuickContainerPrivate is built on Qt's QQuickControlPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContainerPrivate that has a ritual and that
  Python can call so far, 20 names in all: 'q_func', 'get', 'init',
  'cleanup', 'itemAt', 'insertItem', 'moveItem', 'removeItem',
  'reorderItems', 'maybeCullItem', 'maybeCullItems',
  '_q_currentIndexChanged', 'itemChildAdded', 'itemSiblingOrderChanged',
  'itemParentChanged', 'itemDestroyed', 'updateContentWidth',
  'updateContentHeight', 'getContentWidth', 'getContentHeight'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickContainer *QQuickContainerPrivate::q_func() const':
    takes in Python what 'QQuickContainer *QQuickContainerPrivate::q_func()'
    takes.
  - Qt's 'void
    QQuickContainerPrivate::contentData_append(QQmlListProperty<QObject>
    *prop, QObject *obj)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QQuickContainerPrivate::contentData_count(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QQuickContainerPrivate::contentData_at(QQmlListProperty<QObject> *prop,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void
    QQuickContainerPrivate::contentData_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQuickContainerPrivate::contentChildren_append(
    QQmlListProperty<QQuickItem> *prop, QQuickItem *obj)': names
    'QQmlListProperty<QQuickItem>', which has no cute class yet.
  - Qt's 'qsizetype QQuickContainerPrivate::contentChildren_count(
    QQmlListProperty<QQuickItem> *prop)': names
    'QQmlListProperty<QQuickItem>', which has no cute class yet.
  - Qt's 'QQuickItem
    *QQuickContainerPrivate::contentChildren_at(QQmlListProperty<QQuickItem>
    *prop, qsizetype index)': names 'QQmlListProperty<QQuickItem>', which has
    no cute class yet.
  - Qt's 'void QQuickContainerPrivate::contentChildren_clear(
    QQmlListProperty<QQuickItem> *prop)': names
    'QQmlListProperty<QQuickItem>', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickContainerPrivate is created at the first use, not by
    'QQuickContainerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContainerPrivate.
  - Each name of Qt's QQuickContainerPrivate that has no cute function yet,
    'contentChildren_append', 'contentChildren_at', 'contentChildren_clear',
    'contentChildren_count', 'contentData_append', 'contentData_at',
    'contentData_clear', 'contentData_count', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickContainer)
  @overload(NoneType)
  def get(
      container: Optional[QQuickContainer],
  ) -> Optional[QQuickContainerPrivate]:
    """
    Calls Qt's 'QQuickContainerPrivate
    *QQuickContainerPrivate::get(QQuickContainer *container)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainerprivate.html#get

    Parameters
    ----------

    container : Optional[QQuickContainer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickContainerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContainerPrivate *QQuickContainerPrivate::get(QQuickContainer
    #      *container)
    address = Rituals.call(
        'ritual_ZN22QQuickContainerPrivate3getEP15QQuickContainer',
        CuteMixin._addressOf(container),
    )
    return QQuickContainerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContainerPrivate'

  #  A C++ QQuickContainerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContainerPrivate'

  #  The functions Qt calls itself that QQuickContainerPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemChildAdded': (
          ('_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemSiblingOrderChanged': (
          ('_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP10QQuickI'
           'tem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemParentChanged': (
          ('_ZN22QQuickContainerPrivate17itemParentChangedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
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

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickContainerPrivate::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainerprivate.html#itemAt

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
    #  QQuickItem *QQuickContainerPrivate::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickContainerPrivate6itemAtEi', index,
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickContainerPrivate::getContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#getContentWidth
    """
    #  qreal QQuickContainerPrivate::getContentWidth() const
    ritual = 'ritual_ZNK22QQuickContainerPrivate15getContentWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickContainerPrivate15getContentWidthEv'
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickContainerPrivate::getContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#getContentHeight
    """
    #  qreal QQuickContainerPrivate::getContentHeight() const
    ritual = 'ritual_ZNK22QQuickContainerPrivate16getContentHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickContainerPrivate16getContentHeightEv'
    return self.uglySide.call(ritual)

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

  def q_func(self) -> Optional[QQuickContainer]:
    """
    Calls Qt's 'QQuickContainer *QQuickContainerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainerprivate.html#q_func

    Returns
    -------

    Optional[QQuickContainer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContainer *QQuickContainerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate6q_funcEv',
    )
    from . import QQuickContainer
    return QQuickContainer._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontainerprivate.html#init
    """
    #  void QQuickContainerPrivate::init()
    self.uglySide.call('ritual_ZN22QQuickContainerPrivate4initEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#cleanup
    """
    #  void QQuickContainerPrivate::cleanup()
    self.uglySide.call('ritual_ZN22QQuickContainerPrivate7cleanupEv')

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def insertItem(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::insertItem(int index, QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::insertItem(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate10insertItemEiP10QQuickItem',
        index, self._addressOf(item),
    )

  @overload(int, int, QQuickItem)
  @overload(int, int, NoneType)
  def moveItem(
      self,
      from_: int,
      to: int,
      item: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::moveItem(int from, int to,
    QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#moveItem

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::moveItem(int from, int to, QQuickItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate8moveItemEiiP10QQuickItem',
        from_, to, self._addressOf(item),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def removeItem(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::removeItem(int index, QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#removeItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::removeItem(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate10removeItemEiP10QQuickItem',
        index, self._addressOf(item),
    )

  def reorderItems(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::reorderItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#reorderItems
    """
    #  void QQuickContainerPrivate::reorderItems()
    self.uglySide.call('ritual_ZN22QQuickContainerPrivate12reorderItemsEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def maybeCullItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::maybeCullItem(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#maybeCullItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::maybeCullItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate13maybeCullItemEP10QQuickItem',
        self._addressOf(item),
    )

  def maybeCullItems(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::maybeCullItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#maybeCullItems
    """
    #  void QQuickContainerPrivate::maybeCullItems()
    self.uglySide.call('ritual_ZN22QQuickContainerPrivate14maybeCullItemsEv')

  def _q_currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::_q_currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#_q_currentIndexChanged
    """
    #  void QQuickContainerPrivate::_q_currentIndexChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate22_q_currentIndexChangedEv',
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildAdded(
      self,
      item: Optional[QQuickItem],
      child: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::itemChildAdded(QQuickItem *item,
    QQuickItem *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#itemChildAdded

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::itemChildAdded(QQuickItem *item,
    #      QQuickItem *child)
    ritual = (
        'ritual_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickI'
          'temS1_')
    self.uglySide.call(ritual, self._addressOf(item), self._addressOf(child))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickContainerPrivate::itemSiblingOrderChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::itemSiblingOrderChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP'
          '10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      item: Optional[QQuickItem],
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::itemParentChanged(QQuickItem
    *item, QQuickItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#itemParentChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::itemParentChanged(QQuickItem *item,
    #      QQuickItem *parent)
    ritual = (
        'ritual_ZN22QQuickContainerPrivate17itemParentChangedEP10QQuickItem'
        'S1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickContainerPrivate17itemParentChangedEP10QQui'
          'ckItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(parent),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContainerPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN22QQuickContainerPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickContainerPrivate13itemDestroyedEP10QQuickIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(item))

  def updateContentWidth(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::updateContentWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#updateContentWidth
    """
    #  void QQuickContainerPrivate::updateContentWidth()
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate18updateContentWidthEv',
    )

  def updateContentHeight(self) -> None:
    """
    Calls Qt's 'void QQuickContainerPrivate::updateContentHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontainerprivate.html#updateContentHeight
    """
    #  void QQuickContainerPrivate::updateContentHeight()
    self.uglySide.call(
        'ritual_ZN22QQuickContainerPrivate19updateContentHeightEv',
    )

  @staticmethod
  def contentChildren_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickContainerPrivate::contentChildren_append(
    QQmlListProperty<QQuickItem> *prop, QQuickItem *obj)': names
    'QQmlListProperty<QQuickItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentChildren_append' has no cute "
        "function yet. Qt's 'void "
        "QQuickContainerPrivate::contentChildren_append(QQmlListProperty<QQu"
        "ickItem> *prop, QQuickItem *obj)': names "
        "'QQmlListProperty<QQuickItem>', which has no cute class yet.")

  @staticmethod
  def contentChildren_at(*__, **_) -> Never:
    """
    Qt's 'QQuickItem
    *QQuickContainerPrivate::contentChildren_at(QQmlListProperty<QQuickItem>
    *prop, qsizetype index)': names 'QQmlListProperty<QQuickItem>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentChildren_at' has no cute function "
        "yet. Qt's 'QQuickItem "
        "*QQuickContainerPrivate::contentChildren_at(QQmlListProperty<QQuick"
        "Item> *prop, qsizetype index)': names "
        "'QQmlListProperty<QQuickItem>', which has no cute class yet.")

  @staticmethod
  def contentChildren_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickContainerPrivate::contentChildren_clear(
    QQmlListProperty<QQuickItem> *prop)': names
    'QQmlListProperty<QQuickItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentChildren_clear' has no cute "
        "function yet. Qt's 'void "
        "QQuickContainerPrivate::contentChildren_clear(QQmlListProperty<QQui"
        "ckItem> *prop)': names 'QQmlListProperty<QQuickItem>', which has "
        "no cute class yet.")

  @staticmethod
  def contentChildren_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickContainerPrivate::contentChildren_count(
    QQmlListProperty<QQuickItem> *prop)': names
    'QQmlListProperty<QQuickItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentChildren_count' has no cute "
        "function yet. Qt's 'qsizetype "
        "QQuickContainerPrivate::contentChildren_count(QQmlListProperty<QQui"
        "ckItem> *prop)': names 'QQmlListProperty<QQuickItem>', which has "
        "no cute class yet.")

  @staticmethod
  def contentData_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickContainerPrivate::contentData_append(QQmlListProperty<QObject>
    *prop, QObject *obj)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentData_append' has no cute function "
        "yet. Qt's 'void "
        "QQuickContainerPrivate::contentData_append(QQmlListProperty<QObject"
        "> *prop, QObject *obj)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def contentData_at(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QQuickContainerPrivate::contentData_at(QQmlListProperty<QObject> *prop,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentData_at' has no cute function yet. "
        "Qt's 'QObject "
        "*QQuickContainerPrivate::contentData_at(QQmlListProperty<QObject> "
        "*prop, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def contentData_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickContainerPrivate::contentData_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentData_clear' has no cute function "
        "yet. Qt's 'void "
        "QQuickContainerPrivate::contentData_clear(QQmlListProperty<QObject>"
        " *prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def contentData_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickContainerPrivate::contentData_count(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickContainerPrivate.contentData_count' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickContainerPrivate::contentData_count(QQmlListProperty<QObject>"
        " *prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")
