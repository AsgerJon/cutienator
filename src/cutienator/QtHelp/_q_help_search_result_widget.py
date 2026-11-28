"""
QHelpSearchResultWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpsearchresultwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QUrl
  from . import QHelpSearchEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHelpSearchEngine = WAIT['QHelpSearchEngine']
  QPoint = WAIT['QPoint']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpSearchResultWidget(QWidget):
  """
  The cute side of Qt's QHelpSearchResultWidget: a plain Python object
  standing in front of one C++ QHelpSearchResultWidget.

  It is built on the cute 'QWidget', as Qt's QHelpSearchResultWidget is built
  on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpSearchResultWidget that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'linkAt',
  'requestShowLink', 'changeEvent'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpSearchResultWidget::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHelpSearchResultWidget::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpSearchResultWidget::~QHelpSearchResultWidget()': the
    destructor: Python never removes a C++ QHelpSearchResultWidget.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpSearchResultWidget is created at the first use, not by
    'QHelpSearchResultWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpSearchResultWidget.
  - Qt tells when it has removed the C++ QHelpSearchResultWidget. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QHelpSearchResultWidget::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchresultwidget.html#tr

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
    #  QString QHelpSearchResultWidget::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QHelpSearchResultWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpSearchResultWidget'

  #  A C++ QHelpSearchResultWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpSearchResultWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpSearchResultWidget::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresultwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpSearchResultWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QHelpSearchResultWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QHelpSearchEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QHelpSearchEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QHelpSearchResultWidget::QHelpSearchResultWidget(QHelpSearchEngine
    *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresultwidget.html

    Parameters
    ----------

    engine : Optional[QHelpSearchEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHelpSearchResultWidget::QHelpSearchResultWidget(QHelpSearchEngine
    #      *engine)
    self._noteCreation(QHelpSearchResultWidget, lambda: Rituals.call(
        'ritual_ZN23QHelpSearchResultWidgetC1EP17QHelpSearchEngine',
        self._addressOf(engine),
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

  @overload(QPoint)
  def linkAt(self, point: QPoint) -> QUrl:
    """
    Calls Qt's 'QUrl QHelpSearchResultWidget::linkAt(const QPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresultwidget.html#linkAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHelpSearchResultWidget::linkAt(const QPoint &point)
    address = self.uglySide.call(
        'ritual_ZN23QHelpSearchResultWidget6linkAtERK6QPoint',
        self._valueOf(point),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QUrl)
  def requestShowLink(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QHelpSearchResultWidget::requestShowLink(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresultwidget.html#requestShowLink

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHelpSearchResultWidget::requestShowLink(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN23QHelpSearchResultWidget15requestShowLinkERK4QUrl',
        self._valueOf(url),
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QHelpSearchResultWidget::changeEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresultwidget.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHelpSearchResultWidget::changeEvent(QEvent *event)
    ritual = 'ritual_ZN23QHelpSearchResultWidget11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QHelpSearchResultWidget11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))
