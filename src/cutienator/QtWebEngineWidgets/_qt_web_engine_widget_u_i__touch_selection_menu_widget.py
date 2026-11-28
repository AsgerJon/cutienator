"""
QtWebEngineWidgetUI::TouchSelectionMenuWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/touchselectionmenuwidget_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWebEngineWidgetUI::TouchSelectionMenuWidget to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtWidgets import QPushButton, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TouchSelectionMenuWidget(QWidget):
  """
  The cute side of Qt's QtWebEngineWidgetUI::TouchSelectionMenuWidget: a
  plain Python object standing in front of one C++
  QtWebEngineWidgetUI::TouchSelectionMenuWidget.

  It is built on the cute 'QWidget', as Qt's
  QtWebEngineWidgetUI::TouchSelectionMenuWidget is built on Qt's QWidget, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtWebEngineWidgetUI::TouchSelectionMenuWidget that
  has a ritual and that Python can call so far, 1 name in all: 'eventFilter'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtWebEngineWidgetUI::TouchSelectionMenuWidget::
    ~TouchSelectionMenuWidget()': the destructor: Python never removes a C++
    QtWebEngineWidgetUI::TouchSelectionMenuWidget.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QtWebEngineWidgetUI::TouchSelectionMenuWidget is created at the
    first use, not by 'QtWebEngineWidgetUI::TouchSelectionMenuWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtWebEngineWidgetUI::TouchSelectionMenuWidget.
  - Qt tells when it has removed the C++
    QtWebEngineWidgetUI::TouchSelectionMenuWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtWebEngineWidgetUI::TouchSelectionMenuWidget that has
    no cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside
  #  QtWebEngineWidgetUI::TouchSelectionMenuWidget, each a class in here as
  #  in C++.

  class TouchButton(QPushButton):
    """
    The cute side of Qt's
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton: a plain
    Python object standing in front of one C++
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton.

    It is built on the cute 'QPushButton', as Qt's
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton is built on
    Qt's QPushButton, and has everything that class has.

    What exists
    -----------

    Every function of Qt's
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton that has a
    ritual and that Python can call so far, 1 name in all: 'event'. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::
      ~TouchButton()': the destructor: Python never removes a C++
      QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton.

    What to expect
    --------------

    - The C++ QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton is
      created at the first use, not by
      'QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++
      QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton.
    - Qt tells when it has removed the C++
      QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton. Every call
      on the cute object, and every use of it as an argument, then raises
      'RuntimeError', and nothing reaches C++.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QEvent = WAIT['QEvent']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton'

    #  A C++ QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton
    #  Python makes is of a C++ class of ours, in which Python can take
    #  functions over. This ritual hands one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str, QWidget)
    @overload(str, NoneType)
    def __init__(self, name: str, parent: Optional[QWidget]) -> None:
      """
      Notes what was given, for Qt's
      'QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::
      TouchButton(QString name, QWidget *parent)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtwebenginewidgetui-touchselectionmenuwidget-touchbutton.html

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.

      parent : Optional[QWidget]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::
      #      TouchButton(QString name, QWidget *parent)
      self._noteCreation(
          TouchSelectionMenuWidget.TouchButton, lambda: Rituals.call(
              'ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11To'
              'uchButtonC1E7QStringP7QWidget',
              name, self._addressOf(parent),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QEvent)
    @overload(NoneType)
    def event(self, ev: Optional[QEvent]) -> bool:
      """
      Calls Qt's 'bool
      QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::event(
      QEvent *ev)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtwebenginewidgetui-touchselectionmenuwidget-touchbutton.html

      Parameters
      ----------

      ev : Optional[QEvent]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  bool QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::
      #      event(QEvent *ev)
      ritual = (
          'ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchB'
          'utton5eventEP6QEvent')
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11'
            'TouchButton5eventEP6QEvent')
      return self.uglySide.call(ritual, self._addressOf(ev))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWebEngineWidgetUI::TouchSelectionMenuWidget'

  #  A C++ QtWebEngineWidgetUI::TouchSelectionMenuWidget Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWebEngineWidgetUI_TouchSelectionMenuWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's
    'QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchSelectionMenuWidget(
    QWebEngineView *view, QtWebEngineCore::TouchSelectionMenuController
    *controller)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QtWebEngineCore::TouchSelectionMenuController'.
    """
    raise NotImplementedError(
        "'QtWebEngineWidgetUI.TouchSelectionMenuWidget.__init__' has no "
        "cute function yet. Qt's "
        "'QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchSelectionMenuW"
        "idget(QWebEngineView *view, "
        "QtWebEngineCore::TouchSelectionMenuController *controller)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QtWebEngineCore::TouchSelectionMenuController'.")

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
      obj: Optional[QObject],
      ev: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter(QObject *obj,
    QEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginewidgetui-touchselectionmenuwidget.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ev : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter(QObject
    #      *obj, QEvent *ev)
    ritual = (
        'ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11eventFil'
        'terEP7QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11ev'
          'entFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(obj, 'QObject'), self._addressOf(ev),
    )
