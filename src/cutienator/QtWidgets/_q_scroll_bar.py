"""
QScrollBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qscrollbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractSlider, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QSize
  from ..QtGui import QContextMenuEvent, QHideEvent, QMouseEvent, QPaintEvent
  from ..QtGui import QWheelEvent
  from . import QMenu, QScrollBarPrivate, QStyleOptionSlider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QStyleOptionSlider = WAIT['QStyleOptionSlider']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScrollBar(QAbstractSlider):
  """
  The cute side of Qt's QScrollBar: a plain Python object standing in front
  of one C++ QScrollBar.

  It is built on the cute 'QAbstractSlider', as Qt's QScrollBar is built on
  Qt's QAbstractSlider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollBar that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'sizeHint', 'event',
  'createStandardContextMenu', 'wheelEvent', 'paintEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseMoveEvent', 'hideEvent', 'contextMenuEvent',
  'initStyleOption', 'd_func'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScrollBar::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QScrollBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QScrollBar::~QScrollBar()': the destructor: Python never removes a
    C++ QScrollBar.
  - Qt's 'void QScrollBar::sliderChange(SliderChange change)': names the enum
    'QAbstractSlider::SliderChange', whose class cannot be named here.
  - Qt's 'const QScrollBarPrivate *QScrollBar::d_func() const': takes in
    Python what 'QScrollBarPrivate *QScrollBar::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QScrollBar is created at the first use, not by 'QScrollBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollBar.
  - Qt tells when it has removed the C++ QScrollBar. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QScrollBar::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#tr

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
    #  QString QScrollBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QScrollBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollBar'

  #  A C++ QScrollBar Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScrollBar'

  #  The functions Qt calls itself that QScrollBar is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK10QScrollBar15initStyleOptionEP18QStyleOptionSlider',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionSlider'),
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
    Calls Qt's 'const QMetaObject *QScrollBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScrollBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QScrollBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QScrollBar::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScrollBar::sizeHint() const
    ritual = 'ritual_ZNK10QScrollBar8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QScrollBar8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QScrollBar::QScrollBar(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#QScrollBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScrollBar::QScrollBar(QWidget *parent)
    self._noteCreation(QScrollBar, lambda: Rituals.call(
        'ritual_ZN10QScrollBarC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QWidget)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      a0: Qt.Orientation,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QScrollBar::QScrollBar(Qt::Orientation
    a0, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#QScrollBar

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScrollBar::QScrollBar(Qt::Orientation a0, QWidget *parent)
    self._noteCreation(QScrollBar, lambda: Rituals.call(
        'ritual_ZN10QScrollBarC1EN2Qt11OrientationEP7QWidget',
        a0.value, self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QScrollBar::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QScrollBar::event(QEvent *event)
    ritual = 'ritual_ZN10QScrollBar5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPoint)
  def createStandardContextMenu(self, position: QPoint) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QScrollBar::createStandardContextMenu(QPoint
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbar.html#createStandardContextMenu

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QScrollBar::createStandardContextMenu(QPoint position)
    address = self.uglySide.call(
        'ritual_ZN10QScrollBar25createStandardContextMenuE6QPoint',
        self._valueOf(position),
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, a0: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::wheelEvent(QWheelEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#wheelEvent

    Parameters
    ----------

    a0 : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::wheelEvent(QWheelEvent *a0)
    ritual = 'ritual_ZN10QScrollBar10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN10QScrollBar10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QScrollBar15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QScrollBar17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN10QScrollBar14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::hideEvent(QHideEvent *a0)
    ritual = 'ritual_ZN10QScrollBar9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QScrollBar9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, a0: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QScrollBar::contextMenuEvent(QContextMenuEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#contextMenuEvent

    Parameters
    ----------

    a0 : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::contextMenuEvent(QContextMenuEvent *a0)
    ritual = 'ritual_ZN10QScrollBar16contextMenuEventEP17QContextMenuEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QScrollBar16contextMenuEventEP17QContextMenuEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QStyleOptionSlider)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionSlider]) -> None:
    """
    Calls Qt's 'void QScrollBar::initStyleOption(QStyleOptionSlider *option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionSlider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollBar::initStyleOption(QStyleOptionSlider *option) const
    ritual = 'ritual_ZNK10QScrollBar15initStyleOptionEP18QStyleOptionSlider'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QScrollBar15initStyleOptionEP18QStyleOptionSlide'
          'r')
    self.uglySide.call(ritual, self._addressOf(option))

  def d_func(self) -> Optional[QScrollBarPrivate]:
    """
    Calls Qt's 'QScrollBarPrivate *QScrollBar::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbar.html#d_func

    Returns
    -------

    Optional[QScrollBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBarPrivate *QScrollBar::d_func()
    address = self.uglySide.call('ritual_ZN10QScrollBar6d_funcEv')
    from . import QScrollBarPrivate
    return QScrollBarPrivate._cuteAt(address)
