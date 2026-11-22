"""
QScrollArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qscrollarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QAbstractScrollArea, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScrollArea(QAbstractScrollArea):
  """
  The cute side of Qt's QScrollArea: a plain Python object standing in front
  of one C++ QScrollArea.

  It is built on the cute 'QAbstractScrollArea', as Qt's QScrollArea is built
  on Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollArea that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'widget', 'setWidget',
  'takeWidget', 'widgetResizable', 'setWidgetResizable', 'sizeHint',
  'focusNextPrevChild', 'alignment', 'setAlignment', 'ensureVisible',
  'ensureWidgetVisible', 'event', 'eventFilter', 'resizeEvent',
  'scrollContentsBy', 'viewportSizeHint'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScrollArea::~QScrollArea()': the destructor: Python never removes
    a C++ QScrollArea.

  What has no ritual
  ------------------

  9 of the 29 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QScrollArea is created at the first use, not by
    'QScrollArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollArea.
  - Qt tells when it has removed the C++ QScrollArea. Every call on the cute
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
    Calls Qt's 'QString QScrollArea::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#tr

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
    #  QString QScrollArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QScrollArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollArea'

  #  A C++ QScrollArea Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScrollArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScrollArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScrollArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QScrollArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QScrollArea::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QScrollArea::widget() const
    address = self.uglySide.call('ritual_ZNK11QScrollArea6widgetEv')
    return QWidget._cuteAt(address)

  def widgetResizable(self) -> bool:
    """
    Calls Qt's 'bool QScrollArea::widgetResizable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#widgetResizable
    """
    #  bool QScrollArea::widgetResizable() const
    return self.uglySide.call('ritual_ZNK11QScrollArea15widgetResizableEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QScrollArea::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScrollArea::sizeHint() const
    ritual = 'ritual_ZNK11QScrollArea8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QScrollArea8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QScrollArea::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QScrollArea::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK11QScrollArea9alignmentEv',
    ))

  def viewportSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QScrollArea::viewportSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#viewportSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScrollArea::viewportSizeHint() const
    address = self.uglySide.call(
        'ritual_own_ZNK11QScrollArea16viewportSizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QScrollArea::setWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollArea::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QScrollArea9setWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(bool)
  def setWidgetResizable(self, resizable: bool) -> None:
    """
    Calls Qt's 'void QScrollArea::setWidgetResizable(bool resizable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollarea.html#setWidgetResizable

    Parameters
    ----------

    resizable : bool
      Passed on as it is.
    """
    #  void QScrollArea::setWidgetResizable(bool resizable)
    self.uglySide.call(
        'ritual_ZN11QScrollArea18setWidgetResizableEb', resizable,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, a0: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QScrollArea::setAlignment(Qt::Alignment a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#setAlignment

    Parameters
    ----------

    a0 : Qt.Alignment
      Passed on as its number.
    """
    #  void QScrollArea::setAlignment(Qt::Alignment a0)
    self.uglySide.call(
        'ritual_ZN11QScrollArea12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        a0.value,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QScrollArea::QScrollArea(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#QScrollArea

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScrollArea::QScrollArea(QWidget *parent)
    self._noteCreation(QScrollArea, lambda: Rituals.call(
        'ritual_ZN11QScrollAreaC1EP7QWidget', self._addressOf(parent),
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

  def takeWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QScrollArea::takeWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#takeWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QScrollArea::takeWidget()
    address = self.uglySide.call('ritual_ZN11QScrollArea10takeWidgetEv')
    return QWidget._cuteAt(address)

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QScrollArea::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollarea.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QScrollArea::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN11QScrollArea18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QScrollArea18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  def ensureVisible(
      self,
      x: int,
      y: int,
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QScrollArea::ensureVisible(int x, int y, int xmargin,
    int ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#ensureVisible

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QScrollArea::ensureVisible(int x, int y, int xmargin, int
    #      ymargin)
    self.uglySide.call(
        'ritual_ZN11QScrollArea13ensureVisibleEiiii', x, y, xmargin, ymargin,
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, int)
  @overload(NoneType, int)
  @overload(QWidget, int, int)
  @overload(NoneType, int, int)
  def ensureWidgetVisible(
      self,
      childWidget: Optional[QWidget],
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QScrollArea::ensureWidgetVisible(QWidget *childWidget,
    int xmargin, int ymargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollarea.html#ensureWidgetVisible

    Parameters
    ----------

    childWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QScrollArea::ensureWidgetVisible(QWidget *childWidget, int
    #      xmargin, int ymargin)
    self.uglySide.call(
        'ritual_ZN11QScrollArea19ensureWidgetVisibleEP7QWidgetii',
        self._addressOf(childWidget), xmargin, ymargin,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QScrollArea::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QScrollArea::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_own_ZN11QScrollArea5eventEP6QEvent', self._addressOf(a0),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QScrollArea::eventFilter(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QScrollArea::eventFilter(QObject *a0, QEvent *a1)
    return self.uglySide.call(
        'ritual_own_ZN11QScrollArea11eventFilterEP7QObjectP6QEvent',
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QScrollArea::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollArea::resizeEvent(QResizeEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QScrollArea11resizeEventEP12QResizeEvent',
        self._addressOf(a0),
    )

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QScrollArea::scrollContentsBy(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollarea.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QScrollArea::scrollContentsBy(int dx, int dy)
    self.uglySide.call(
        'ritual_own_ZN11QScrollArea16scrollContentsByEii', dx, dy,
    )
