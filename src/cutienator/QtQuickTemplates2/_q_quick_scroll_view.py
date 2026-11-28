"""
QQuickScrollView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickScrollView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickPane

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSizeF
  from ..QtGui import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScrollView(QQuickPane):
  """
  The cute side of Qt's QQuickScrollView: a plain Python object standing in
  front of one C++ QQuickScrollView.

  It is built on the cute 'QQuickPane', as Qt's QQuickScrollView is built on
  Qt's QQuickPane, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScrollView that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr',
  'effectiveScrollBarWidth', 'effectiveScrollBarHeight',
  'childMouseEventFilter', 'eventFilter', 'keyPressEvent',
  'componentComplete', 'contentItemChange', 'contentSizeChange',
  'accessibleRole', 'effectiveScrollBarWidthChanged',
  'effectiveScrollBarHeightChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScrollView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickScrollView::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickScrollView::~QQuickScrollView()': the destructor: Python
    never removes a C++ QQuickScrollView.
  - Qt's 'QQuickScrollViewPrivate *QQuickScrollView::d_func()': gives
    'QQuickScrollViewPrivate', which has no cute class yet.
  - Qt's 'const QQuickScrollViewPrivate *QQuickScrollView::d_func() const':
    gives 'QQuickScrollViewPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickScrollView is created at the first use, not by
    'QQuickScrollView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScrollView.
  - Qt tells when it has removed the C++ QQuickScrollView. Every call on the
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
    Calls Qt's 'QString QQuickScrollView::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollview.html#tr

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
    #  QString QQuickScrollView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickScrollView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScrollView'

  #  A C++ QQuickScrollView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScrollView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScrollView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScrollView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickScrollView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickScrollView::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickScrollView::accessibleRole() const
    ritual = 'ritual_ZNK16QQuickScrollView14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickScrollView14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickScrollView::QQuickScrollView(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#QQuickScrollView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScrollView::QQuickScrollView(QQuickItem *parent)
    self._noteCreation(QQuickScrollView, lambda: Rituals.call(
        'ritual_ZN16QQuickScrollViewC1EP10QQuickItem',
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

  def effectiveScrollBarWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollView::effectiveScrollBarWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#effectiveScrollBarWidth
    """
    #  qreal QQuickScrollView::effectiveScrollBarWidth()
    return self.uglySide.call(
        'ritual_ZN16QQuickScrollView23effectiveScrollBarWidthEv',
    )

  def effectiveScrollBarHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollView::effectiveScrollBarHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#effectiveScrollBarHeight
    """
    #  qreal QQuickScrollView::effectiveScrollBarHeight()
    return self.uglySide.call(
        'ritual_ZN16QQuickScrollView24effectiveScrollBarHeightEv',
    )

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      item: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickScrollView::childMouseEventFilter(QQuickItem
    *item, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#childMouseEventFilter

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickScrollView::childMouseEventFilter(QQuickItem *item, QEvent
    #      *event)
    ritual = (
        'ritual_ZN16QQuickScrollView21childMouseEventFilterEP10QQuickItemP6'
        'QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickScrollView21childMouseEventFilterEP10QQuick'
          'ItemP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(event),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickScrollView::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollview.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickScrollView::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN16QQuickScrollView11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickScrollView11eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickScrollView::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollView::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN16QQuickScrollView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickScrollView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickScrollView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#componentComplete
    """
    #  void QQuickScrollView::componentComplete()
    ritual = 'ritual_ZN16QQuickScrollView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickScrollView17componentCompleteEv'
    self.uglySide.call(ritual)

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
    Calls Qt's 'void QQuickScrollView::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollView::contentItemChange(QQuickItem *newItem,
    #      QQuickItem *oldItem)
    ritual = (
        'ritual_ZN16QQuickScrollView17contentItemChangeEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickScrollView17contentItemChangeEP10QQuickItem'
          'S1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QSizeF, QSizeF)
  def contentSizeChange(self, newSize: QSizeF, oldSize: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickScrollView::contentSizeChange(const QSizeF
    &newSize, const QSizeF &oldSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html#contentSizeChange

    Parameters
    ----------

    newSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    oldSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickScrollView::contentSizeChange(const QSizeF &newSize, const
    #      QSizeF &oldSize)
    ritual = 'ritual_ZN16QQuickScrollView17contentSizeChangeERK6QSizeFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickScrollView17contentSizeChangeERK6QSizeFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newSize), self._valueOf(oldSize),
    )

  def effectiveScrollBarWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollView::effectiveScrollBarWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html
    """
    #  void QQuickScrollView::effectiveScrollBarWidthChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickScrollView30effectiveScrollBarWidthChangedEv',
    )

  def effectiveScrollBarHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollView::effectiveScrollBarHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollview.html
    """
    #  void QQuickScrollView::effectiveScrollBarHeightChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickScrollView31effectiveScrollBarHeightChangedEv',
    )
