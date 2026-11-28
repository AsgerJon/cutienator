"""
QSidebar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSidebar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QListView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QSize, QUrl
  from ..QtGui import QDragEnterEvent, QFocusEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QPoint = WAIT['QPoint']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSidebar(QListView):
  """
  The cute side of Qt's QSidebar: a plain Python object standing in front of
  one C++ QSidebar.

  It is built on the cute 'QListView', as Qt's QSidebar is built on Qt's
  QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSidebar that has a ritual and that Python can call
  so far, 11 names in all: 'metaObject', 'goToUrl', 'sizeHint', 'setUrls',
  'addUrls', 'urls', 'event', 'focusInEvent', 'dragEnterEvent',
  'showContextMenu', 'removeEntry'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSidebar::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QSidebar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSidebar::~QSidebar()': the destructor: Python never removes a C++
    QSidebar.

  What has no ritual
  ------------------

  7 of the 21 functions Qt declares: 4 leans on 'QSidebar; 2 not a gap; 1 the
  compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QSidebar is created at the first use, not by 'QSidebar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSidebar.
  - Qt tells when it has removed the C++ QSidebar. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSidebar that has no cute function yet, '__init__',
    'selectUrl', 'setModelAndUrls', holds a function that raises
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
  __qt_class__ = 'QSidebar'

  #  A C++ QSidebar Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSidebar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSidebar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSidebar::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QSidebar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSidebar::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSidebar::sizeHint() const
    ritual = 'ritual_ZNK8QSidebar8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSidebar8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def urls(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QSidebar::urls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#urls

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QSidebar::urls() const
    address = self.uglySide.call('ritual_ZNK8QSidebar4urlsEv')
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QUrl])
  def setUrls(self, list: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QSidebar::setUrls(const QList<QUrl> &list)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#setUrls

    Parameters
    ----------

    list : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSidebar::setUrls(const QList<QUrl> &list)
    self.uglySide.call(
        'ritual_ZN8QSidebar7setUrlsERK5QListI4QUrlE', self._valueOf(list),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSidebar::QSidebar(QWidget *parent)': leans on
    'QSidebar::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSidebar.__init__' has no cute function yet. Qt's "
        "'QSidebar::QSidebar(QWidget *parent)': leans on "
        "'QSidebar::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(QUrl)
  def goToUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QSidebar::goToUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#goToUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QSidebar::goToUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN8QSidebar7goToUrlERK4QUrl', self._valueOf(url),
    )

  @overload(QList[QUrl], int)
  def addUrls(self, list: QList[QUrl], row: int) -> None:
    """
    Calls Qt's 'void QSidebar::addUrls(const QList<QUrl> &list, int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#addUrls

    Parameters
    ----------

    list : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    row : int
      Passed on as it is.
    """
    #  void QSidebar::addUrls(const QList<QUrl> &list, int row)
    self.uglySide.call(
        'ritual_ZN8QSidebar7addUrlsERK5QListI4QUrlEi',
        self._valueOf(list), row,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSidebar::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSidebar::event(QEvent *e)
    ritual = 'ritual_ZN8QSidebar5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QSidebar5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QSidebar::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSidebar::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN8QSidebar12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QSidebar12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QSidebar::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSidebar::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN8QSidebar14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QSidebar14dragEnterEventEP15QDragEnterEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPoint)
  def showContextMenu(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QSidebar::showContextMenu(const QPoint &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#showContextMenu

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSidebar::showContextMenu(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN8QSidebar15showContextMenuERK6QPoint',
        self._valueOf(position),
    )

  def removeEntry(self) -> None:
    """
    Calls Qt's 'void QSidebar::removeEntry()'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#removeEntry
    """
    #  void QSidebar::removeEntry()
    self.uglySide.call('ritual_ZN8QSidebar11removeEntryEv')

  @staticmethod
  def selectUrl(*__, **_) -> Never:
    """
    Qt's 'void QSidebar::selectUrl(const QUrl &url)': leans on
    'QSidebar::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSidebar.selectUrl' has no cute function yet. Qt's 'void "
        "QSidebar::selectUrl(const QUrl &url)': leans on "
        "'QSidebar::staticMetaObject', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setModelAndUrls(*__, **_) -> Never:
    """
    Qt's 'void QSidebar::setModelAndUrls(QFileSystemModel *model, const
    QList<QUrl> &newUrls)': leans on 'QSidebar::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSidebar.setModelAndUrls' has no cute function yet. Qt's 'void "
        "QSidebar::setModelAndUrls(QFileSystemModel *model, const "
        "QList<QUrl> &newUrls)': leans on 'QSidebar::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
