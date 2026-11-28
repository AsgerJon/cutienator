"""
QQuickPanePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPanePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtQuick import QQuickItem
  from . import QQuickPane
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPanePrivate(QQuickControlPrivate):
  """
  The cute side of Qt's QQuickPanePrivate: a plain Python object standing in
  front of one C++ QQuickPanePrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's QQuickPanePrivate
  is built on Qt's QQuickControlPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPanePrivate that has a ritual and that Python
  can call so far, 14 names in all: 'q_func', 'init', 'contentChildItems',
  'getFirstChild', 'getContentItem', 'getContentWidth', 'getContentHeight',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged', 'itemDestroyed',
  'contentChildrenChange', 'updateContentWidth', 'updateContentHeight',
  'handlePress'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPane *QQuickPanePrivate::q_func() const': takes in
    Python what 'QQuickPane *QQuickPanePrivate::q_func()' takes.
  - Qt's 'QQmlListProperty<QObject> QQuickPanePrivate::contentData()': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickPanePrivate::contentChildren()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QQuickPanePrivate is created at the first use, not by
    'QQuickPanePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPanePrivate.
  - Each name of Qt's QQuickPanePrivate that has no cute function yet,
    'contentChildren', 'contentData', holds a function that raises
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
  __qt_class__ = 'QQuickPanePrivate'

  #  A C++ QQuickPanePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPanePrivate'

  #  The functions Qt calls itself that QQuickPanePrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'contentData': (
          'QQmlListProperty<QObject> QQuickPanePrivate::contentData()',
      ),
      'contentChildren': (
          'QQmlListProperty<QQuickItem> '
          'QQuickPanePrivate::contentChildren()',
      ),
      'contentChildItems': (
          'QList<QQuickItem *> QQuickPanePrivate::contentChildItems() const',
      ),
  }

  #  The functions Qt calls itself that QQuickPanePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'getFirstChild': (
          ('_ZNK17QQuickPanePrivate13getFirstChildEv',
           ('address', 'address', 'QtQuick:QQuickItem'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentChildItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QQuickPanePrivate::contentChildItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#contentChildItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QQuickPanePrivate::contentChildItems() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPanePrivate17contentChildItemsEv',
    )
    from ..QtQuick import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  def getFirstChild(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPanePrivate::getFirstChild() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#getFirstChild

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPanePrivate::getFirstChild() const
    ritual = 'ritual_ZNK17QQuickPanePrivate13getFirstChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickPanePrivate13getFirstChildEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPanePrivate::getContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#getContentWidth
    """
    #  qreal QQuickPanePrivate::getContentWidth() const
    ritual = 'ritual_ZNK17QQuickPanePrivate15getContentWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickPanePrivate15getContentWidthEv'
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPanePrivate::getContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#getContentHeight
    """
    #  qreal QQuickPanePrivate::getContentHeight() const
    ritual = 'ritual_ZNK17QQuickPanePrivate16getContentHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickPanePrivate16getContentHeightEv'
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

  def q_func(self) -> Optional[QQuickPane]:
    """
    Calls Qt's 'QQuickPane *QQuickPanePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpaneprivate.html#q_func

    Returns
    -------

    Optional[QQuickPane]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPane *QQuickPanePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickPanePrivate6q_funcEv')
    from . import QQuickPane
    return QQuickPane._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpaneprivate.html#init
    """
    #  void QQuickPanePrivate::init()
    self.uglySide.call('ritual_ZN17QQuickPanePrivate4initEv')

  def getContentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPanePrivate::getContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#getContentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPanePrivate::getContentItem()
    ritual = 'ritual_ZN17QQuickPanePrivate14getContentItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPanePrivate14getContentItemEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPanePrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickPanePrivate24itemImplicitWidthChangedEP10QQuickIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPanePrivate24itemImplicitWidthChangedEP10QQ'
          'uickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#itemImplicitHeightChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPanePrivate::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickPanePrivate25itemImplicitHeightChangedEP10QQuickI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPanePrivate25itemImplicitHeightChangedEP10Q'
          'QuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPanePrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN17QQuickPanePrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPanePrivate13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def contentChildrenChange(self) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::contentChildrenChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#contentChildrenChange
    """
    #  void QQuickPanePrivate::contentChildrenChange()
    self.uglySide.call(
        'ritual_ZN17QQuickPanePrivate21contentChildrenChangeEv',
    )

  def updateContentWidth(self) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::updateContentWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#updateContentWidth
    """
    #  void QQuickPanePrivate::updateContentWidth()
    self.uglySide.call('ritual_ZN17QQuickPanePrivate18updateContentWidthEv')

  def updateContentHeight(self) -> None:
    """
    Calls Qt's 'void QQuickPanePrivate::updateContentHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaneprivate.html#updateContentHeight
    """
    #  void QQuickPanePrivate::updateContentHeight()
    self.uglySide.call('ritual_ZN17QQuickPanePrivate19updateContentHeightEv')

  @overload(QPointF, int)
  def handlePress(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickPanePrivate::handlePress(const QPointF &point,
    ulong timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpaneprivate.html#handlePress

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickPanePrivate::handlePress(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN17QQuickPanePrivate11handlePressERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPanePrivate11handlePressERK7QPointFm'
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @staticmethod
  def contentChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem> QQuickPanePrivate::contentChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPanePrivate.contentChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickItem> "
        "QQuickPanePrivate::contentChildren()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def contentData(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPanePrivate::contentData()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPanePrivate.contentData' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPanePrivate::contentData()': "
        "gives a type Python has no way to take yet.")
