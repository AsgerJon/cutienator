"""
QWebEngineHistoryItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginehistory.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QUrl
  from . import QWebEngineHistoryItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineHistoryItemPrivate = WAIT['QWebEngineHistoryItemPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineHistoryItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineHistoryItem: a plain Python object standing
  in front of one C++ QWebEngineHistoryItem.

  C++ hands a QWebEngineHistoryItem around as a copy, so every C++
  QWebEngineHistoryItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineHistoryItem that has a ritual and that
  Python can call so far, 7 names in all: 'originalUrl', 'url', 'title',
  'lastVisited', 'iconUrl', 'isValid', 'd_func'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineHistoryItem::QWebEngineHistoryItem(QWebEngineHistoryItem
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineHistoryItem &QWebEngineHistoryItem::operator=(const
    QWebEngineHistoryItem &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QWebEngineHistoryItem
    &QWebEngineHistoryItem::operator=(QWebEngineHistoryItem &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineHistoryItem::~QWebEngineHistoryItem()': the destructor:
    Python removes its C++ QWebEngineHistoryItem by it, and has no other use
    for it.
  - Qt's 'void QWebEngineHistoryItem::swap(QWebEngineHistoryItem &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QWebEngineHistoryItemPrivate *QWebEngineHistoryItem::d_func()
    const': takes in Python what 'QWebEngineHistoryItemPrivate
    *QWebEngineHistoryItem::d_func()' takes.

  What to expect
  --------------

  - The C++ QWebEngineHistoryItem is created at the first use, not by
    'QWebEngineHistoryItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineHistoryItem back gives a copy the ritual
    made for Python, in a new cute QWebEngineHistoryItem.
  - Each name of Qt's QWebEngineHistoryItem that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineHistoryItem'

  #  Qt's '~QWebEngineHistoryItem()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineHistoryItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QWebEngineHistoryItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def originalUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineHistoryItem::originalUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistoryitem.html#originalUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineHistoryItem::originalUrl() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineHistoryItem11originalUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineHistoryItem::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistoryitem.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineHistoryItem::url() const
    address = self.uglySide.call('ritual_ZNK21QWebEngineHistoryItem3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QWebEngineHistoryItem::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistoryitem.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineHistoryItem::title() const
    return self.uglySide.call('ritual_ZNK21QWebEngineHistoryItem5titleEv')

  def lastVisited(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QWebEngineHistoryItem::lastVisited() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistoryitem.html#lastVisited

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QWebEngineHistoryItem::lastVisited() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineHistoryItem11lastVisitedEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def iconUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineHistoryItem::iconUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistoryitem.html#iconUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineHistoryItem::iconUrl() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineHistoryItem7iconUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineHistoryItem::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistoryitem.html#isValid
    """
    #  bool QWebEngineHistoryItem::isValid() const
    return self.uglySide.call('ritual_ZNK21QWebEngineHistoryItem7isValidEv')

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

  @overload(THIS)
  def __init__(self, other: QWebEngineHistoryItem) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineHistoryItem::QWebEngineHistoryItem(const QWebEngineHistoryItem
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistoryitem.html#QWebEngineHistoryItem

    Parameters
    ----------

    other : QWebEngineHistoryItem
      Passed on as a value: Qt reads the C++ QWebEngineHistoryItem, which
      stays Python's own.
    """
    #  QWebEngineHistoryItem::QWebEngineHistoryItem(const
    #      QWebEngineHistoryItem &other)
    self._noteCreation(QWebEngineHistoryItem, lambda: Rituals.call(
        'ritual_ZN21QWebEngineHistoryItemC1ERKS_', self._valueOf(other),
    ))

  @overload(QWebEngineHistoryItemPrivate)
  @overload(NoneType)
  def __init__(self, priv: Optional[QWebEngineHistoryItemPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineHistoryItem::QWebEngineHistoryItem(
    QWebEngineHistoryItemPrivate *priv)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistoryitem.html#QWebEngineHistoryItem

    Parameters
    ----------

    priv : Optional[QWebEngineHistoryItemPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineHistoryItem::QWebEngineHistoryItem(
    #      QWebEngineHistoryItemPrivate *priv)
    self._noteCreation(QWebEngineHistoryItem, lambda: Rituals.call(
        'ritual_ZN21QWebEngineHistoryItemC1EP28QWebEngineHistoryItemPrivate',
        self._addressOf(priv),
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

  def d_func(self) -> Optional[QWebEngineHistoryItemPrivate]:
    """
    Calls Qt's 'QWebEngineHistoryItemPrivate
    *QWebEngineHistoryItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistoryitem.html#d_func

    Returns
    -------

    Optional[QWebEngineHistoryItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistoryItemPrivate *QWebEngineHistoryItem::d_func()
    address = self.uglySide.call('ritual_ZN21QWebEngineHistoryItem6d_funcEv')
    from . import QWebEngineHistoryItemPrivate
    return QWebEngineHistoryItemPrivate._cuteAt(address)

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineHistoryItem::swap(QWebEngineHistoryItem &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryItem.swap' has no cute function yet. Qt's 'void "
        "QWebEngineHistoryItem::swap(QWebEngineHistoryItem &other)': takes "
        "a type Python has no way to hand over yet.")


#  Qt's 'QList<QWebEngineHistoryItem>': the list of QWebEngineHistoryItem,
#  which 'QList[QWebEngineHistoryItem]' gives. It is made here, so that there
#  is one as soon as there can be a QWebEngineHistoryItem.
QList.createKind(
    QWebEngineHistoryItem, 'value',
    make='ritual_list_make_QWebEngineHistoryItem',
    add='ritual_list_add_QWebEngineHistoryItem',
    size='ritual_list_size_QWebEngineHistoryItem',
    at='ritual_list_at_QWebEngineHistoryItem',
    drop='ritual_list_drop_QWebEngineHistoryItem',
)
