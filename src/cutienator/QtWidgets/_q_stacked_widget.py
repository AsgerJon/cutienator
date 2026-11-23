"""
QStackedWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstackedwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStackedWidget(QFrame):
  """
  The cute side of Qt's QStackedWidget: a plain Python object standing in
  front of one C++ QStackedWidget.

  It is built on the cute 'QFrame', as Qt's QStackedWidget is built on Qt's
  QFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStackedWidget that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'addWidget',
  'insertWidget', 'removeWidget', 'currentWidget', 'currentIndex', 'indexOf',
  'widget', 'count', 'setCurrentIndex', 'setCurrentWidget', 'event'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStackedWidget::~QStackedWidget()': the destructor: Python never
    removes a C++ QStackedWidget.

  What has no ritual
  ------------------

  11 of the 26 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 3 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QStackedWidget is created at the first use, not by
    'QStackedWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStackedWidget.
  - Qt tells when it has removed the C++ QStackedWidget. Every call on the
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
    Calls Qt's 'QString QStackedWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#tr

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
    #  QString QStackedWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QStackedWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStackedWidget'

  #  A C++ QStackedWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStackedWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStackedWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStackedWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QStackedWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QStackedWidget::currentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#currentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QStackedWidget::currentWidget() const
    address = self.uglySide.call(
        'ritual_ZNK14QStackedWidget13currentWidgetEv',
    )
    return QWidget._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QStackedWidget::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#currentIndex
    """
    #  int QStackedWidget::currentIndex() const
    return self.uglySide.call('ritual_ZNK14QStackedWidget12currentIndexEv')

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, a0: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QStackedWidget::indexOf(const QWidget *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#indexOf

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QStackedWidget::indexOf(const QWidget *a0) const
    return self.uglySide.call(
        'ritual_ZNK14QStackedWidget7indexOfEPK7QWidget', self._addressOf(a0),
    )

  @overload(int)
  def widget(self, a0: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QStackedWidget::widget(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#widget

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QStackedWidget::widget(int a0) const
    address = self.uglySide.call('ritual_ZNK14QStackedWidget6widgetEi', a0)
    return QWidget._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QStackedWidget::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#count
    """
    #  int QStackedWidget::count() const
    return self.uglySide.call('ritual_ZNK14QStackedWidget5countEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QStackedWidget::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidget.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QStackedWidget::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN14QStackedWidget15setCurrentIndexEi', index)

  @overload(QWidget)
  @overload(NoneType)
  def setCurrentWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStackedWidget::setCurrentWidget(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidget.html#setCurrentWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedWidget::setCurrentWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN14QStackedWidget16setCurrentWidgetEP7QWidget',
        self._addressOf(w),
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
    Notes what was given, for Qt's 'QStackedWidget::QStackedWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#QStackedWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStackedWidget::QStackedWidget(QWidget *parent)
    self._noteCreation(QStackedWidget, lambda: Rituals.call(
        'ritual_ZN14QStackedWidgetC1EP7QWidget', self._addressOf(parent),
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

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, w: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QStackedWidget::addWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#addWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QStackedWidget::addWidget(QWidget *w)
    return self.uglySide.call(
        'ritual_ZN14QStackedWidget9addWidgetEP7QWidget', self._addressOf(w),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def insertWidget(self, index: int, w: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QStackedWidget::insertWidget(int index, QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QStackedWidget::insertWidget(int index, QWidget *w)
    return self.uglySide.call(
        'ritual_ZN14QStackedWidget12insertWidgetEiP7QWidget',
        index, self._addressOf(w),
    )

  @overload(QWidget)
  @overload(NoneType)
  def removeWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStackedWidget::removeWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#removeWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedWidget::removeWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN14QStackedWidget12removeWidgetEP7QWidget',
        self._addressOf(w),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QStackedWidget::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidget.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStackedWidget::event(QEvent *e)
    ritual = 'ritual_ZN14QStackedWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStackedWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))
