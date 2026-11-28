"""
QStackedWidgetPreviewEventFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QStackedWidgetPreviewEventFilter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtWidgets import QStackedWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QStackedWidget = WAIT['QStackedWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStackedWidgetPreviewEventFilter(QObject):
  """
  The cute side of Qt's QStackedWidgetPreviewEventFilter: a plain Python
  object standing in front of one C++ QStackedWidgetPreviewEventFilter.

  It is built on the cute 'QObject', as Qt's QStackedWidgetPreviewEventFilter
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStackedWidgetPreviewEventFilter that has a ritual
  and that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'install', 'eventFilter', 'setButtonToolTipEnabled',
  'buttonToolTipEnabled', 'updateButtons', 'prevPage', 'nextPage',
  'stackedWidget', 'gotoPage', 'updateButtonToolTip'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStackedWidgetPreviewEventFilter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QStackedWidgetPreviewEventFilter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QStackedWidgetPreviewEventFilter is created at the first use, not
    by 'QStackedWidgetPreviewEventFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStackedWidgetPreviewEventFilter.
  - Qt tells when it has removed the C++ QStackedWidgetPreviewEventFilter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QStackedWidgetPreviewEventFilter::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#tr

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
    #  QString QStackedWidgetPreviewEventFilter::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QStackedWidget)
  @overload(NoneType)
  def install(stackedWidget: Optional[QStackedWidget]) -> None:
    """
    Calls Qt's 'void QStackedWidgetPreviewEventFilter::install(QStackedWidget
    *stackedWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#install

    Parameters
    ----------

    stackedWidget : Optional[QStackedWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedWidgetPreviewEventFilter::install(QStackedWidget
    #      *stackedWidget)
    Rituals.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter7installEP14QStackedWid'
        'get',
        CuteMixin._addressOf(stackedWidget),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStackedWidgetPreviewEventFilter'

  #  The functions Qt calls itself that QStackedWidgetPreviewEventFilter is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'gotoPage': (
          ('_ZN32QStackedWidgetPreviewEventFilter8gotoPageEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject
    *QStackedWidgetPreviewEventFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStackedWidgetPreviewEventFilter::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QStackedWidgetPreviewEventFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buttonToolTipEnabled(self) -> bool:
    """
    Calls Qt's 'bool QStackedWidgetPreviewEventFilter::buttonToolTipEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html
    """
    #  bool QStackedWidgetPreviewEventFilter::buttonToolTipEnabled() const
    return self.uglySide.call(
        'ritual_ZNK32QStackedWidgetPreviewEventFilter20buttonToolTipEnabled'
        'Ev',
    )

  def stackedWidget(self) -> Optional[QStackedWidget]:
    """
    Calls Qt's 'QStackedWidget
    *QStackedWidgetPreviewEventFilter::stackedWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html

    Returns
    -------

    Optional[QStackedWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStackedWidget *QStackedWidgetPreviewEventFilter::stackedWidget()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QStackedWidgetPreviewEventFilter13stackedWidgetEv',
    )
    from ..QtWidgets import QStackedWidget
    return QStackedWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setButtonToolTipEnabled(self, v: bool) -> None:
    """
    Calls Qt's 'void
    QStackedWidgetPreviewEventFilter::setButtonToolTipEnabled(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QStackedWidgetPreviewEventFilter::setButtonToolTipEnabled(bool v)
    self.uglySide.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter23setButtonToolTipEnabl'
        'edEb',
        v,
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

  @overload(QStackedWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QStackedWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QStackedWidgetPreviewEventFilter::QStackedWidgetPreviewEventFilter(
    QStackedWidget *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html

    Parameters
    ----------

    parent : Optional[QStackedWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStackedWidgetPreviewEventFilter::
    #      QStackedWidgetPreviewEventFilter(QStackedWidget *parent)
    self._noteCreation(
        QStackedWidgetPreviewEventFilter, lambda: Rituals.call(
            'ritual_ZN32QStackedWidgetPreviewEventFilterC1EP14QStackedWidge'
            't',
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QStackedWidgetPreviewEventFilter::eventFilter(QObject
    *watched, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStackedWidgetPreviewEventFilter::eventFilter(QObject *watched,
    #      QEvent *event)
    ritual = (
        'ritual_ZN32QStackedWidgetPreviewEventFilter11eventFilterEP7QObject'
        'P6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QStackedWidgetPreviewEventFilter11eventFilterEP7Q'
          'ObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def updateButtons(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetPreviewEventFilter::updateButtons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html
    """
    #  void QStackedWidgetPreviewEventFilter::updateButtons()
    self.uglySide.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter13updateButtonsEv',
    )

  def prevPage(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetPreviewEventFilter::prevPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#prevPage
    """
    #  void QStackedWidgetPreviewEventFilter::prevPage()
    self.uglySide.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter8prevPageEv',
    )

  def nextPage(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetPreviewEventFilter::nextPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#nextPage
    """
    #  void QStackedWidgetPreviewEventFilter::nextPage()
    self.uglySide.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter8nextPageEv',
    )

  @overload(int)
  def gotoPage(self, page: int) -> None:
    """
    Calls Qt's 'void QStackedWidgetPreviewEventFilter::gotoPage(int page)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html#gotoPage

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  void QStackedWidgetPreviewEventFilter::gotoPage(int page)
    ritual = 'ritual_ZN32QStackedWidgetPreviewEventFilter8gotoPageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN32QStackedWidgetPreviewEventFilter8gotoPageEi'
    self.uglySide.call(ritual, page)

  @overload(QObject)
  @overload(NoneType)
  def updateButtonToolTip(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QStackedWidgetPreviewEventFilter::updateButtonToolTip(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetprevieweventfilter.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedWidgetPreviewEventFilter::updateButtonToolTip(QObject *o)
    self.uglySide.call(
        'ritual_ZN32QStackedWidgetPreviewEventFilter19updateButtonToolTipEP'
        '7QObject',
        self._addressOf(o, 'QObject'),
    )
