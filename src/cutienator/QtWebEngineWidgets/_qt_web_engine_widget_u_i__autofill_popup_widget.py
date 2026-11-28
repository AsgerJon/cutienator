"""
QtWebEngineWidgetUI::AutofillPopupWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/autofillpopupwidget_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWebEngineWidgetUI::AutofillPopupWidget to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..QtWidgets import QFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AutofillPopupWidget(QFrame):
  """
  The cute side of Qt's QtWebEngineWidgetUI::AutofillPopupWidget: a plain
  Python object standing in front of one C++
  QtWebEngineWidgetUI::AutofillPopupWidget.

  It is built on the cute 'QFrame', as Qt's
  QtWebEngineWidgetUI::AutofillPopupWidget is built on Qt's QFrame, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtWebEngineWidgetUI::AutofillPopupWidget that has a
  ritual and that Python can call so far, 4 names in all: 'metaObject',
  'eventFilter', 'keyPressEvent', 'keyReleaseEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtWebEngineWidgetUI::AutofillPopupWidget::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtWebEngineWidgetUI::AutofillPopupWidget::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtWebEngineWidgetUI::AutofillPopupWidget::~AutofillPopupWidget()':
    the destructor: Python never removes a C++
    QtWebEngineWidgetUI::AutofillPopupWidget.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QtWebEngineWidgetUI.

  What to expect
  --------------

  - The C++ QtWebEngineWidgetUI::AutofillPopupWidget is created at the first
    use, not by 'QtWebEngineWidgetUI::AutofillPopupWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWebEngineWidgetUI::AutofillPopupWidget.
  - Qt tells when it has removed the C++
    QtWebEngineWidgetUI::AutofillPopupWidget. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QtWebEngineWidgetUI::AutofillPopupWidget that has no
    cute function yet, '__init__', 'showPopup', holds a function that raises
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
  __qt_class__ = 'QtWebEngineWidgetUI::AutofillPopupWidget'

  #  A C++ QtWebEngineWidgetUI::AutofillPopupWidget Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWebEngineWidgetUI_AutofillPopupWidget'

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
    *QtWebEngineWidgetUI::AutofillPopupWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginewidgetui-autofillpopupwidget.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtWebEngineWidgetUI::AutofillPopupWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QtWebEngineWidgetUI19AutofillPopupWidget10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtWebEngineWidgetUI::AutofillPopupWidget::AutofillPopupWidget(
    QtWebEngineCore::AutofillPopupController *controller, QWebEngineView
    *parent)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QtWebEngineCore::AutofillPopupController'.
    """
    raise NotImplementedError(
        "'QtWebEngineWidgetUI.AutofillPopupWidget.__init__' has no cute "
        "function yet. Qt's "
        "'QtWebEngineWidgetUI::AutofillPopupWidget::AutofillPopupWidget(QtWe"
        "bEngineCore::AutofillPopupController *controller, QWebEngineView "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QtWebEngineCore::AutofillPopupController'.")

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
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QtWebEngineWidgetUI::AutofillPopupWidget::eventFilter(QObject *object,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginewidgetui-autofillpopupwidget.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWebEngineWidgetUI::AutofillPopupWidget::eventFilter(QObject
    #      *object, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN19QtWebEngineWidgetUI19AutofillPopupWidget11eventFilterEP'
        '7QObjectP6QEvent',
        self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    QtWebEngineWidgetUI::AutofillPopupWidget::keyPressEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginewidgetui-autofillpopupwidget.html

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWebEngineWidgetUI::AutofillPopupWidget::keyPressEvent(QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN19QtWebEngineWidgetUI19AutofillPopupWidget13keyPressEvent'
        'EP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    QtWebEngineWidgetUI::AutofillPopupWidget::keyReleaseEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginewidgetui-autofillpopupwidget.html

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWebEngineWidgetUI::AutofillPopupWidget::keyReleaseEvent(
    #      QKeyEvent *event)
    ritual = (
        'ritual_ZN19QtWebEngineWidgetUI19AutofillPopupWidget15keyReleaseEve'
        'ntEP9QKeyEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QtWebEngineWidgetUI19AutofillPopupWidget15keyRele'
          'aseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def showPopup(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineWidgetUI::AutofillPopupWidget::showPopup(QPoint
    pos, int width, bool autoselectFirstSuggestion)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type
    'QtWebEngineCore::AutofillPopupController'.
    """
    raise NotImplementedError(
        "'QtWebEngineWidgetUI.AutofillPopupWidget.showPopup' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineWidgetUI::AutofillPopupWidget::showPopup(QPoint pos, "
        "int width, bool autoselectFirstSuggestion)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QtWebEngineCore::AutofillPopupController'.")
