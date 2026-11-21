"""
QStatusBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstatusbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStatusBar(QWidget):
  """
  The cute side of Qt's QStatusBar: a plain Python object standing in front
  of one C++ QStatusBar.

  It is built on the cute 'QWidget', as Qt's QStatusBar is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStatusBar that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'addWidget',
  'insertWidget', 'addPermanentWidget', 'insertPermanentWidget',
  'removeWidget', 'setSizeGripEnabled', 'isSizeGripEnabled',
  'currentMessage', 'showMessage', 'clearMessage'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStatusBar::~QStatusBar()': the destructor: Python never removes a
    C++ QStatusBar.

  What has no ritual
  ------------------

  15 of the 29 functions Qt declares: 6 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QStatusBar is created at the first use, not by 'QStatusBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStatusBar.
  - Qt tells when it has removed the C++ QStatusBar. Every call on the cute
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
    Calls Qt's 'QString QStatusBar::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#tr

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
    #  QString QStatusBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QStatusBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStatusBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStatusBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStatusBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QStatusBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSizeGripEnabled(self) -> bool:
    """
    Calls Qt's 'bool QStatusBar::isSizeGripEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#isSizeGripEnabled
    """
    #  bool QStatusBar::isSizeGripEnabled() const
    return self.uglySide.call('ritual_ZNK10QStatusBar17isSizeGripEnabledEv')

  def currentMessage(self) -> str:
    """
    Calls Qt's 'QString QStatusBar::currentMessage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#currentMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusBar::currentMessage() const
    return self.uglySide.call('ritual_ZNK10QStatusBar14currentMessageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSizeGripEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QStatusBar::setSizeGripEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#setSizeGripEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QStatusBar::setSizeGripEnabled(bool a0)
    self.uglySide.call('ritual_ZN10QStatusBar18setSizeGripEnabledEb', a0)

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
    Notes what was given, for Qt's 'QStatusBar::QStatusBar(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#QStatusBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStatusBar::QStatusBar(QWidget *parent)
    self._noteCreation(QStatusBar, lambda: Rituals.call(
        'ritual_ZN10QStatusBarC1EP7QWidget', self._addressOf(parent),
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
  @overload(QWidget, int)
  @overload(NoneType, int)
  def addWidget(self, widget: Optional[QWidget], stretch: int = 0) -> None:
    """
    Calls Qt's 'void QStatusBar::addWidget(QWidget *widget, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#addWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QStatusBar::addWidget(QWidget *widget, int stretch)
    self.uglySide.call(
        'ritual_ZN10QStatusBar9addWidgetEP7QWidgeti',
        self._addressOf(widget), stretch,
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  @overload(int, QWidget, int)
  @overload(int, NoneType, int)
  def insertWidget(
      self,
      index: int,
      widget: Optional[QWidget],
      stretch: int = 0,
  ) -> int:
    """
    Calls Qt's 'int QStatusBar::insertWidget(int index, QWidget *widget, int
    stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QStatusBar::insertWidget(int index, QWidget *widget, int stretch)
    return self.uglySide.call(
        'ritual_ZN10QStatusBar12insertWidgetEiP7QWidgeti',
        index, self._addressOf(widget), stretch,
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, int)
  @overload(NoneType, int)
  def addPermanentWidget(
      self,
      widget: Optional[QWidget],
      stretch: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QStatusBar::addPermanentWidget(QWidget *widget, int
    stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#addPermanentWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QStatusBar::addPermanentWidget(QWidget *widget, int stretch)
    self.uglySide.call(
        'ritual_ZN10QStatusBar18addPermanentWidgetEP7QWidgeti',
        self._addressOf(widget), stretch,
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  @overload(int, QWidget, int)
  @overload(int, NoneType, int)
  def insertPermanentWidget(
      self,
      index: int,
      widget: Optional[QWidget],
      stretch: int = 0,
  ) -> int:
    """
    Calls Qt's 'int QStatusBar::insertPermanentWidget(int index, QWidget
    *widget, int stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusbar.html#insertPermanentWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QStatusBar::insertPermanentWidget(int index, QWidget *widget, int
    #      stretch)
    return self.uglySide.call(
        'ritual_ZN10QStatusBar21insertPermanentWidgetEiP7QWidgeti',
        index, self._addressOf(widget), stretch,
    )

  @overload(QWidget)
  @overload(NoneType)
  def removeWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStatusBar::removeWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#removeWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStatusBar::removeWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN10QStatusBar12removeWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(str)
  @overload(str, int)
  def showMessage(self, text: str, timeout: int = 0) -> None:
    """
    Calls Qt's 'void QStatusBar::showMessage(const QString &text, int
    timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#showMessage

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QStatusBar::showMessage(const QString &text, int timeout)
    self.uglySide.call(
        'ritual_ZN10QStatusBar11showMessageERK7QStringi', text, timeout,
    )

  def clearMessage(self) -> None:
    """
    Calls Qt's 'void QStatusBar::clearMessage()'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusbar.html#clearMessage
    """
    #  void QStatusBar::clearMessage()
    self.uglySide.call('ritual_ZN10QStatusBar12clearMessageEv')
