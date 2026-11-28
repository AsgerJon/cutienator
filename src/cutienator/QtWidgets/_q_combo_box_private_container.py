"""
QComboBoxPrivateContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QComboBoxPrivateContainer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QModelIndex, QTimerEvent
  from ..QtGui import QHideEvent, QMouseEvent, QPaintEvent, QResizeEvent
  from ..QtGui import QShowEvent
  from . import QAbstractItemView, QComboBox, QStyleOptionComboBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemView = WAIT['QAbstractItemView']
  QComboBox = WAIT['QComboBox']
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QModelIndex = WAIT['QModelIndex']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboBoxPrivateContainer(QFrame):
  """
  The cute side of Qt's QComboBoxPrivateContainer: a plain Python object
  standing in front of one C++ QComboBoxPrivateContainer.

  It is built on the cute 'QFrame', as Qt's QComboBoxPrivateContainer is
  built on Qt's QFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboBoxPrivateContainer that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'itemView',
  'setItemView', 'spacing', 'topMargin', 'bottomMargin',
  'updateTopBottomMargin', 'updateStyleSettings', 'scrollItemView',
  'hideScrollers', 'updateScrollers', 'viewDestroyed', 'changeEvent',
  'eventFilter', 'mousePressEvent', 'mouseReleaseEvent', 'showEvent',
  'hideEvent', 'timerEvent', 'resizeEvent', 'paintEvent', 'comboStyleOption',
  'itemSelected', 'resetButton'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QComboBoxPrivateContainer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QComboBoxPrivateContainer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QComboBoxPrivateContainer::~QComboBoxPrivateContainer()': the
    destructor: Python never removes a C++ QComboBoxPrivateContainer.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QComboBoxPrivateContainer is created at the first use, not by
    'QComboBoxPrivateContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboBoxPrivateContainer.
  - Qt tells when it has removed the C++ QComboBoxPrivateContainer. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QComboBoxPrivateContainer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#tr

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
    #  QString QComboBoxPrivateContainer::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QComboBoxPrivateContainer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QComboBoxPrivateContainer'

  #  A C++ QComboBoxPrivateContainer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QComboBoxPrivateContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QComboBoxPrivateContainer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QComboBoxPrivateContainer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QComboBoxPrivateContainer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def itemView(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QComboBoxPrivateContainer::itemView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#itemView

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QComboBoxPrivateContainer::itemView() const
    address = self.uglySide.call(
        'ritual_ZNK25QComboBoxPrivateContainer8itemViewEv',
    )
    from . import QAbstractItemView
    return QAbstractItemView._cuteAt(address)

  def spacing(self) -> int:
    """
    Calls Qt's 'int QComboBoxPrivateContainer::spacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#spacing
    """
    #  int QComboBoxPrivateContainer::spacing() const
    return self.uglySide.call(
        'ritual_ZNK25QComboBoxPrivateContainer7spacingEv',
    )

  def topMargin(self) -> int:
    """
    Calls Qt's 'int QComboBoxPrivateContainer::topMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#topMargin
    """
    #  int QComboBoxPrivateContainer::topMargin() const
    return self.uglySide.call(
        'ritual_ZNK25QComboBoxPrivateContainer9topMarginEv',
    )

  def bottomMargin(self) -> int:
    """
    Calls Qt's 'int QComboBoxPrivateContainer::bottomMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#bottomMargin
    """
    #  int QComboBoxPrivateContainer::bottomMargin() const
    return self.uglySide.call(
        'ritual_ZNK25QComboBoxPrivateContainer12bottomMarginEv',
    )

  def comboStyleOption(self) -> QStyleOptionComboBox:
    """
    Calls Qt's 'QStyleOptionComboBox
    QComboBoxPrivateContainer::comboStyleOption() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#comboStyleOption

    Returns
    -------

    QStyleOptionComboBox
      A new cute QStyleOptionComboBox around the copy Qt gave back. Python
      owns it.
    """
    #  QStyleOptionComboBox QComboBoxPrivateContainer::comboStyleOption()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QComboBoxPrivateContainer16comboStyleOptionEv',
    )
    from . import QStyleOptionComboBox
    return QStyleOptionComboBox._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemView)
  @overload(NoneType)
  def setItemView(self, itemView: Optional[QAbstractItemView]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::setItemView(QAbstractItemView
    *itemView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#setItemView

    Parameters
    ----------

    itemView : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::setItemView(QAbstractItemView
    #      *itemView)
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer11setItemViewEP17QAbstractItem'
        'View',
        self._addressOf(itemView),
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

  @overload(QAbstractItemView, QComboBox)
  @overload(QAbstractItemView, NoneType)
  @overload(NoneType, QComboBox)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      itemView: Optional[QAbstractItemView],
      parent: Optional[QComboBox],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QComboBoxPrivateContainer::QComboBoxPrivateContainer(QAbstractItemView
    *itemView, QComboBox *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html

    Parameters
    ----------

    itemView : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QComboBoxPrivateContainer::QComboBoxPrivateContainer(QAbstractItemView
    #      *itemView, QComboBox *parent)
    self._noteCreation(QComboBoxPrivateContainer, lambda: Rituals.call(
        'ritual_ZN25QComboBoxPrivateContainerC1EP17QAbstractItemViewP9QComb'
        'oBox',
        self._addressOf(itemView), self._addressOf(parent),
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

  def updateTopBottomMargin(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::updateTopBottomMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html
    """
    #  void QComboBoxPrivateContainer::updateTopBottomMargin()
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer21updateTopBottomMarginEv',
    )

  def updateStyleSettings(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::updateStyleSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#updateStyleSettings
    """
    #  void QComboBoxPrivateContainer::updateStyleSettings()
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer19updateStyleSettingsEv',
    )

  @overload(int)
  def scrollItemView(self, action: int) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::scrollItemView(int action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#scrollItemView

    Parameters
    ----------

    action : int
      Passed on as it is.
    """
    #  void QComboBoxPrivateContainer::scrollItemView(int action)
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer14scrollItemViewEi', action,
    )

  def hideScrollers(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::hideScrollers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#hideScrollers
    """
    #  void QComboBoxPrivateContainer::hideScrollers()
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer13hideScrollersEv',
    )

  def updateScrollers(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::updateScrollers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#updateScrollers
    """
    #  void QComboBoxPrivateContainer::updateScrollers()
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer15updateScrollersEv',
    )

  def viewDestroyed(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::viewDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#viewDestroyed
    """
    #  void QComboBoxPrivateContainer::viewDestroyed()
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer13viewDestroyedEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::changeEvent(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::changeEvent(QEvent *e)
    ritual = 'ritual_ZN25QComboBoxPrivateContainer11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer11changeEventEP6QEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QComboBoxPrivateContainer::eventFilter(QObject *o,
    QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#eventFilter

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QComboBoxPrivateContainer::eventFilter(QObject *o, QEvent *e)
    ritual = (
        'ritual_ZN25QComboBoxPrivateContainer11eventFilterEP7QObjectP6QEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer11eventFilterEP7QObjectP'
          '6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(o, 'QObject'), self._addressOf(e),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::mousePressEvent(QMouseEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::mousePressEvent(QMouseEvent *e)
    ritual = (
        'ritual_ZN25QComboBoxPrivateContainer15mousePressEventEP11QMouseEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer15mousePressEventEP11QMo'
          'useEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::mouseReleaseEvent(QMouseEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#mouseReleaseEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::mouseReleaseEvent(QMouseEvent *e)
    ritual = (
        'ritual_ZN25QComboBoxPrivateContainer17mouseReleaseEventEP11QMouseE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer17mouseReleaseEventEP11Q'
          'MouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, e: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::showEvent(QShowEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#showEvent

    Parameters
    ----------

    e : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::showEvent(QShowEvent *e)
    ritual = 'ritual_ZN25QComboBoxPrivateContainer9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer9showEventEP10QShowEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, e: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::hideEvent(QHideEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#hideEvent

    Parameters
    ----------

    e : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::hideEvent(QHideEvent *e)
    ritual = 'ritual_ZN25QComboBoxPrivateContainer9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer9hideEventEP10QHideEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, timerEvent: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::timerEvent(QTimerEvent
    *timerEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#timerEvent

    Parameters
    ----------

    timerEvent : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::timerEvent(QTimerEvent *timerEvent)
    ritual = (
        'ritual_ZN25QComboBoxPrivateContainer10timerEventEP11QTimerEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer10timerEventEP11QTimerEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(timerEvent))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::resizeEvent(QResizeEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::resizeEvent(QResizeEvent *e)
    ritual = (
        'ritual_ZN25QComboBoxPrivateContainer11resizeEventEP12QResizeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer11resizeEventEP12QResize'
          'Event')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::paintEvent(QPaintEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateContainer::paintEvent(QPaintEvent *e)
    ritual = (
        'ritual_ZN25QComboBoxPrivateContainer10paintEventEP11QPaintEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QComboBoxPrivateContainer10paintEventEP11QPaintEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QModelIndex)
  def itemSelected(self, a0: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::itemSelected(const
    QModelIndex &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#itemSelected

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivateContainer::itemSelected(const QModelIndex &a0)
    self.uglySide.call(
        'ritual_ZN25QComboBoxPrivateContainer12itemSelectedERK11QModelIndex',
        self._valueOf(a0),
    )

  def resetButton(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateContainer::resetButton()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatecontainer.html#resetButton
    """
    #  void QComboBoxPrivateContainer::resetButton()
    self.uglySide.call('ritual_ZN25QComboBoxPrivateContainer11resetButtonEv')
