"""
QtVirtualKeyboard::DesktopInputPanel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/desktopinputpanel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::DesktopInputPanel to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect
  from ..QtGui import QScreen, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QScreen = WAIT['QScreen']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DesktopInputPanel(QtVirtualKeyboard.AppInputPanel):
  """
  The cute side of Qt's QtVirtualKeyboard::DesktopInputPanel: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::DesktopInputPanel.

  It is built on the cute 'QtVirtualKeyboard::AppInputPanel', as Qt's
  QtVirtualKeyboard::DesktopInputPanel is built on Qt's
  QtVirtualKeyboard::AppInputPanel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::DesktopInputPanel that has a
  ritual and that Python can call so far, 15 names in all: 'metaObject',
  'tr', 'show', 'hide', 'isVisible', 'setInputRect', 'createView',
  'destroyView', 'repositionView', 'focusWindowChanged',
  'focusWindowVisibleChanged', 'previewRectangleChanged',
  'previewVisibleChanged', 'screenChanged', 'updateInputRegion'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::DesktopInputPanel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::DesktopInputPanel::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtVirtualKeyboard::DesktopInputPanel::~DesktopInputPanel()': the
    destructor: Python never removes a C++
    QtVirtualKeyboard::DesktopInputPanel.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::DesktopInputPanel is created at the first use,
    not by 'QtVirtualKeyboard::DesktopInputPanel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::DesktopInputPanel.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::DesktopInputPanel. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::DesktopInputPanel::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html#tr

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
    #  QString QtVirtualKeyboard::DesktopInputPanel::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::DesktopInputPanel'

  #  A C++ QtVirtualKeyboard::DesktopInputPanel Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_DesktopInputPanel'

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
    *QtVirtualKeyboard::DesktopInputPanel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::DesktopInputPanel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard17DesktopInputPanel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::DesktopInputPanel::isVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html#isVisible
    """
    #  bool QtVirtualKeyboard::DesktopInputPanel::isVisible() const
    ritual = 'ritual_ZNK17QtVirtualKeyboard17DesktopInputPanel9isVisibleEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard17DesktopInputPanel9isVisibleEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setInputRect(self, inputRect: QRect) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputPanel::setInputRect(const
    QRect &inputRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Parameters
    ----------

    inputRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::setInputRect(const QRect
    #      &inputRect)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel12setInputRectERK5Q'
        'Rect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel12setInputRec'
          'tERK5QRect')
    self.uglySide.call(ritual, self._valueOf(inputRect))

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::DesktopInputPanel::DesktopInputPanel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::DesktopInputPanel::DesktopInputPanel(QObject
    #      *parent)
    self._noteCreation(DesktopInputPanel, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def show(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputPanel::show()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html#show
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::show()
    ritual = 'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel4showEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel4showEv'
    self.uglySide.call(ritual)

  def hide(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputPanel::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html#hide
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::hide()
    ritual = 'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel4hideEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel4hideEv'
    self.uglySide.call(ritual)

  def createView(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputPanel::createView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::createView()
    ritual = 'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel10createViewEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel10createViewE'
          'v')
    self.uglySide.call(ritual)

  def destroyView(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputPanel::destroyView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::destroyView()
    ritual = 'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel11destroyViewEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel11destroyView'
          'Ev')
    self.uglySide.call(ritual)

  @overload(QRect)
  def repositionView(self, rect: QRect) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::repositionView(const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::repositionView(const QRect
    #      &rect)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel14repositionViewERK'
        '5QRect',
        self._valueOf(rect),
    )

  @overload(QWindow)
  @overload(NoneType)
  def focusWindowChanged(self, focusWindow: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::focusWindowChanged(QWindow
    *focusWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Parameters
    ----------

    focusWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::focusWindowChanged(QWindow
    #      *focusWindow)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel18focusWindowChange'
        'dEP7QWindow',
        self._addressOf(focusWindow),
    )

  @overload(bool)
  def focusWindowVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::focusWindowVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::focusWindowVisibleChanged(
    #      bool visible)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel25focusWindowVisibl'
        'eChangedEb',
        visible,
    )

  def previewRectangleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::previewRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::previewRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel23previewRectangleC'
        'hangedEv',
    )

  def previewVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::previewVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::previewVisibleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel21previewVisibleCha'
        'ngedEv',
    )

  @overload(QScreen)
  @overload(NoneType)
  def screenChanged(self, a0: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::screenChanged(QScreen *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html

    Parameters
    ----------

    a0 : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::screenChanged(QScreen *a0)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel13screenChangedEP7Q'
        'Screen',
        self._addressOf(a0),
    )

  def updateInputRegion(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputPanel::updateInputRegion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputpanel.html
    """
    #  void QtVirtualKeyboard::DesktopInputPanel::updateInputRegion()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard17DesktopInputPanel17updateInputRegion'
        'Ev',
    )
