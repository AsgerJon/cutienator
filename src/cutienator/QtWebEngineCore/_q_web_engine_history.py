"""
QWebEngineHistory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginehistory.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWebEngineHistoryItem, QWebEngineHistoryModel
  from . import QWebEngineHistoryPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineHistoryItem = WAIT['QWebEngineHistoryItem']
  QWebEngineHistoryPrivate = WAIT['QWebEngineHistoryPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineHistory(QObject):
  """
  The cute side of Qt's QWebEngineHistory: a plain Python object standing in
  front of one C++ QWebEngineHistory.

  It is built on the cute 'QObject', as Qt's QWebEngineHistory is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineHistory that has a ritual and that Python
  can call so far, 22 names in all: 'metaObject', 'tr', 'clear', 'items',
  'backItems', 'forwardItems', 'canGoBack', 'canGoForward', 'back',
  'forward', 'goToItem', 'backItem', 'currentItem', 'forwardItem', 'itemAt',
  'currentItemIndex', 'count', 'itemsModel', 'backItemsModel',
  'forwardItemsModel', 'd_func', 'reset'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineHistory::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWebEngineHistory::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineHistory::~QWebEngineHistory()': the destructor: Python
    never removes a C++ QWebEngineHistory.
  - Qt's 'const QWebEngineHistoryPrivate *QWebEngineHistory::d_func() const':
    takes in Python what 'QWebEngineHistoryPrivate
    *QWebEngineHistory::d_func()' takes.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QWebEngineHistory &a1)':
    an operator between other classes, written inside this one.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QWebEngineHistory
    &a1)': an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineHistory is created at the first use, not by
    'QWebEngineHistory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineHistory.
  - Qt tells when it has removed the C++ QWebEngineHistory. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QWebEngineHistory::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#tr

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
    #  QString QWebEngineHistory::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QWebEngineHistory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineHistory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineHistory::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineHistory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def items(self) -> QList[QWebEngineHistoryItem]:
    """
    Calls Qt's 'QList<QWebEngineHistoryItem> QWebEngineHistory::items()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#items

    Returns
    -------

    QList[QWebEngineHistoryItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineHistoryItem> QWebEngineHistory::items() const
    address = self.uglySide.call('ritual_ZNK17QWebEngineHistory5itemsEv')
    from . import QWebEngineHistoryItem
    return QList[QWebEngineHistoryItem]._cuteOwning(address)

  @overload(int)
  def backItems(self, maxItems: int) -> QList[QWebEngineHistoryItem]:
    """
    Calls Qt's 'QList<QWebEngineHistoryItem> QWebEngineHistory::backItems(int
    maxItems) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#backItems

    Parameters
    ----------

    maxItems : int
      Passed on as it is.

    Returns
    -------

    QList[QWebEngineHistoryItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineHistoryItem> QWebEngineHistory::backItems(int
    #      maxItems) const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory9backItemsEi', maxItems,
    )
    from . import QWebEngineHistoryItem
    return QList[QWebEngineHistoryItem]._cuteOwning(address)

  @overload(int)
  def forwardItems(self, maxItems: int) -> QList[QWebEngineHistoryItem]:
    """
    Calls Qt's 'QList<QWebEngineHistoryItem>
    QWebEngineHistory::forwardItems(int maxItems) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistory.html#forwardItems

    Parameters
    ----------

    maxItems : int
      Passed on as it is.

    Returns
    -------

    QList[QWebEngineHistoryItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineHistoryItem> QWebEngineHistory::forwardItems(int
    #      maxItems) const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory12forwardItemsEi', maxItems,
    )
    from . import QWebEngineHistoryItem
    return QList[QWebEngineHistoryItem]._cuteOwning(address)

  def canGoBack(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineHistory::canGoBack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#canGoBack
    """
    #  bool QWebEngineHistory::canGoBack() const
    return self.uglySide.call('ritual_ZNK17QWebEngineHistory9canGoBackEv')

  def canGoForward(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineHistory::canGoForward() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistory.html#canGoForward
    """
    #  bool QWebEngineHistory::canGoForward() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory12canGoForwardEv',
    )

  def backItem(self) -> QWebEngineHistoryItem:
    """
    Calls Qt's 'QWebEngineHistoryItem QWebEngineHistory::backItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#backItem

    Returns
    -------

    QWebEngineHistoryItem
      A new cute QWebEngineHistoryItem around the copy Qt gave back. Python
      owns it.
    """
    #  QWebEngineHistoryItem QWebEngineHistory::backItem() const
    address = self.uglySide.call('ritual_ZNK17QWebEngineHistory8backItemEv')
    from . import QWebEngineHistoryItem
    return QWebEngineHistoryItem._cuteOwning(address)

  def currentItem(self) -> QWebEngineHistoryItem:
    """
    Calls Qt's 'QWebEngineHistoryItem QWebEngineHistory::currentItem()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#currentItem

    Returns
    -------

    QWebEngineHistoryItem
      A new cute QWebEngineHistoryItem around the copy Qt gave back. Python
      owns it.
    """
    #  QWebEngineHistoryItem QWebEngineHistory::currentItem() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory11currentItemEv',
    )
    from . import QWebEngineHistoryItem
    return QWebEngineHistoryItem._cuteOwning(address)

  def forwardItem(self) -> QWebEngineHistoryItem:
    """
    Calls Qt's 'QWebEngineHistoryItem QWebEngineHistory::forwardItem()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#forwardItem

    Returns
    -------

    QWebEngineHistoryItem
      A new cute QWebEngineHistoryItem around the copy Qt gave back. Python
      owns it.
    """
    #  QWebEngineHistoryItem QWebEngineHistory::forwardItem() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory11forwardItemEv',
    )
    from . import QWebEngineHistoryItem
    return QWebEngineHistoryItem._cuteOwning(address)

  @overload(int)
  def itemAt(self, i: int) -> QWebEngineHistoryItem:
    """
    Calls Qt's 'QWebEngineHistoryItem QWebEngineHistory::itemAt(int i)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#itemAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QWebEngineHistoryItem
      A new cute QWebEngineHistoryItem around the copy Qt gave back. Python
      owns it.
    """
    #  QWebEngineHistoryItem QWebEngineHistory::itemAt(int i) const
    address = self.uglySide.call('ritual_ZNK17QWebEngineHistory6itemAtEi', i)
    from . import QWebEngineHistoryItem
    return QWebEngineHistoryItem._cuteOwning(address)

  def currentItemIndex(self) -> int:
    """
    Calls Qt's 'int QWebEngineHistory::currentItemIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistory.html#currentItemIndex
    """
    #  int QWebEngineHistory::currentItemIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory16currentItemIndexEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QWebEngineHistory::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#count
    """
    #  int QWebEngineHistory::count() const
    return self.uglySide.call('ritual_ZNK17QWebEngineHistory5countEv')

  def itemsModel(self) -> Optional[QWebEngineHistoryModel]:
    """
    Calls Qt's 'QWebEngineHistoryModel *QWebEngineHistory::itemsModel()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#itemsModel

    Returns
    -------

    Optional[QWebEngineHistoryModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistoryModel *QWebEngineHistory::itemsModel() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory10itemsModelEv',
    )
    from . import QWebEngineHistoryModel
    return QWebEngineHistoryModel._cuteAt(address)

  def backItemsModel(self) -> Optional[QWebEngineHistoryModel]:
    """
    Calls Qt's 'QWebEngineHistoryModel *QWebEngineHistory::backItemsModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistory.html#backItemsModel

    Returns
    -------

    Optional[QWebEngineHistoryModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistoryModel *QWebEngineHistory::backItemsModel() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory14backItemsModelEv',
    )
    from . import QWebEngineHistoryModel
    return QWebEngineHistoryModel._cuteAt(address)

  def forwardItemsModel(self) -> Optional[QWebEngineHistoryModel]:
    """
    Calls Qt's 'QWebEngineHistoryModel
    *QWebEngineHistory::forwardItemsModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistory.html#forwardItemsModel

    Returns
    -------

    Optional[QWebEngineHistoryModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistoryModel *QWebEngineHistory::forwardItemsModel() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineHistory17forwardItemsModelEv',
    )
    from . import QWebEngineHistoryModel
    return QWebEngineHistoryModel._cuteAt(address)

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

  @overload(QWebEngineHistoryPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QWebEngineHistoryPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineHistory::QWebEngineHistory(QWebEngineHistoryPrivate *d)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistory.html#QWebEngineHistory

    Parameters
    ----------

    d : Optional[QWebEngineHistoryPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineHistory::QWebEngineHistory(QWebEngineHistoryPrivate *d)
    self._noteCreation(QWebEngineHistory, lambda: Rituals.call(
        'ritual_ZN17QWebEngineHistoryC1EP24QWebEngineHistoryPrivate',
        self._addressOf(d),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QWebEngineHistory::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#clear
    """
    #  void QWebEngineHistory::clear()
    self.uglySide.call('ritual_ZN17QWebEngineHistory5clearEv')

  def back(self) -> None:
    """
    Calls Qt's 'void QWebEngineHistory::back()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#back
    """
    #  void QWebEngineHistory::back()
    self.uglySide.call('ritual_ZN17QWebEngineHistory4backEv')

  def forward(self) -> None:
    """
    Calls Qt's 'void QWebEngineHistory::forward()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#forward
    """
    #  void QWebEngineHistory::forward()
    self.uglySide.call('ritual_ZN17QWebEngineHistory7forwardEv')

  @overload(QWebEngineHistoryItem)
  def goToItem(self, item: QWebEngineHistoryItem) -> None:
    """
    Calls Qt's 'void QWebEngineHistory::goToItem(const QWebEngineHistoryItem
    &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#goToItem

    Parameters
    ----------

    item : QWebEngineHistoryItem
      Passed on as a value: Qt reads the C++ QWebEngineHistoryItem, which
      stays Python's own.
    """
    #  void QWebEngineHistory::goToItem(const QWebEngineHistoryItem &item)
    self.uglySide.call(
        'ritual_ZN17QWebEngineHistory8goToItemERK21QWebEngineHistoryItem',
        self._valueOf(item),
    )

  def d_func(self) -> Optional[QWebEngineHistoryPrivate]:
    """
    Calls Qt's 'QWebEngineHistoryPrivate *QWebEngineHistory::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#d_func

    Returns
    -------

    Optional[QWebEngineHistoryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistoryPrivate *QWebEngineHistory::d_func()
    address = self.uglySide.call('ritual_ZN17QWebEngineHistory6d_funcEv')
    from . import QWebEngineHistoryPrivate
    return QWebEngineHistoryPrivate._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QWebEngineHistory::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistory.html#reset
    """
    #  void QWebEngineHistory::reset()
    self.uglySide.call('ritual_ZN17QWebEngineHistory5resetEv')
