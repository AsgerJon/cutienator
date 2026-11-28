"""
QtVirtualKeyboard::AppInputPanel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/appinputpanel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::AppInputPanel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AppInputPanel(QtVirtualKeyboard.AbstractInputPanel):
  """
  The cute side of Qt's QtVirtualKeyboard::AppInputPanel: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::AppInputPanel.

  It is built on the cute 'QtVirtualKeyboard::AbstractInputPanel', as Qt's
  QtVirtualKeyboard::AppInputPanel is built on Qt's
  QtVirtualKeyboard::AbstractInputPanel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::AppInputPanel that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'd_func', 'show', 'hide', 'isVisible'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::AppInputPanel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::AppInputPanel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const AppInputPanelPrivate
    *QtVirtualKeyboard::AppInputPanel::d_func() const': takes in Python what
    'AppInputPanelPrivate *QtVirtualKeyboard::AppInputPanel::d_func()' takes.
  - Qt's
    'QtVirtualKeyboard::AppInputPanel::AppInputPanel(AppInputPanelPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QtVirtualKeyboard::AppInputPanel::~AppInputPanel()': the
    destructor: Python never removes a C++ QtVirtualKeyboard::AppInputPanel.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::AppInputPanel is created at the first use, not
    by 'QtVirtualKeyboard::AppInputPanel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::AppInputPanel.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::AppInputPanel.
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
    Calls Qt's 'QString QtVirtualKeyboard::AppInputPanel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#tr

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
    #  QString QtVirtualKeyboard::AppInputPanel::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard13AppInputPanel2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::AppInputPanel'

  #  A C++ QtVirtualKeyboard::AppInputPanel Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_AppInputPanel'

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
    *QtVirtualKeyboard::AppInputPanel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::AppInputPanel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard13AppInputPanel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::AppInputPanel::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#isVisible
    """
    #  bool QtVirtualKeyboard::AppInputPanel::isVisible() const
    ritual = 'ritual_ZNK17QtVirtualKeyboard13AppInputPanel9isVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QtVirtualKeyboard13AppInputPanel9isVisibleEv'
    return self.uglySide.call(ritual)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::AppInputPanel::AppInputPanel(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#AppInputPanel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::AppInputPanel::AppInputPanel(QObject *parent)
    self._noteCreation(AppInputPanel, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard13AppInputPanelC1EP7QObject',
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

  def d_func(self) -> Optional[QtVirtualKeyboard.AppInputPanelPrivate]:
    """
    Calls Qt's 'AppInputPanelPrivate
    *QtVirtualKeyboard::AppInputPanel::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#d_func

    Returns
    -------

    Optional[QtVirtualKeyboard.AppInputPanelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AppInputPanelPrivate *QtVirtualKeyboard::AppInputPanel::d_func()
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard13AppInputPanel6d_funcEv',
    )
    return QtVirtualKeyboard.AppInputPanelPrivate._cuteAt(address)

  def show(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::AppInputPanel::show()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#show
    """
    #  void QtVirtualKeyboard::AppInputPanel::show()
    ritual = 'ritual_ZN17QtVirtualKeyboard13AppInputPanel4showEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard13AppInputPanel4showEv'
    self.uglySide.call(ritual)

  def hide(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::AppInputPanel::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-appinputpanel.html#hide
    """
    #  void QtVirtualKeyboard::AppInputPanel::hide()
    ritual = 'ritual_ZN17QtVirtualKeyboard13AppInputPanel4hideEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard13AppInputPanel4hideEv'
    self.uglySide.call(ritual)
