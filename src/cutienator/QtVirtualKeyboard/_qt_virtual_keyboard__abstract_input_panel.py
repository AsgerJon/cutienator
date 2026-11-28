"""
QtVirtualKeyboard::AbstractInputPanel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/abstractinputpanel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::AbstractInputPanel to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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

  from ..QtCore import QMetaObject, QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractInputPanel(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::AbstractInputPanel: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::AbstractInputPanel.

  It is built on the cute 'QObject', as Qt's
  QtVirtualKeyboard::AbstractInputPanel is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::AbstractInputPanel that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'show', 'hide', 'isVisible', 'setInputRect', 'createView', 'destroyView'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::AbstractInputPanel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::AbstractInputPanel::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QtVirtualKeyboard::AbstractInputPanel::AbstractInputPanel(QObjectPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QtVirtualKeyboard::AbstractInputPanel::~AbstractInputPanel()': the
    destructor: Python never removes a C++
    QtVirtualKeyboard::AbstractInputPanel.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::AbstractInputPanel is created at the first
    use, not by 'QtVirtualKeyboard::AbstractInputPanel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::AbstractInputPanel.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::AbstractInputPanel. Every call on the cute object, and
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
    Calls Qt's 'QString QtVirtualKeyboard::AbstractInputPanel::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html#tr

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
    #  QString QtVirtualKeyboard::AbstractInputPanel::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard18AbstractInputPanel2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::AbstractInputPanel'

  #  A C++ QtVirtualKeyboard::AbstractInputPanel Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_AbstractInputPanel'

  #  The functions Qt calls itself that QtVirtualKeyboard::AbstractInputPanel
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'show': (
          ('_ZN17QtVirtualKeyboard18AbstractInputPanel4showEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'hide': (
          ('_ZN17QtVirtualKeyboard18AbstractInputPanel4hideEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isVisible': (
          ('_ZNK17QtVirtualKeyboard18AbstractInputPanel9isVisibleEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setInputRect': (
          ('_ZN17QtVirtualKeyboard18AbstractInputPanel12setInputRectERK5QRe'
           'ct',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'createView': (
          ('_ZN17QtVirtualKeyboard18AbstractInputPanel10createViewEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'destroyView': (
          ('_ZN17QtVirtualKeyboard18AbstractInputPanel11destroyViewEv',
           ('nothing', 'nothing', ''),
           ()),
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
    *QtVirtualKeyboard::AbstractInputPanel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::AbstractInputPanel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18AbstractInputPanel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::AbstractInputPanel::isVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html
    """
    #  bool QtVirtualKeyboard::AbstractInputPanel::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18AbstractInputPanel9isVisibleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setInputRect(self, inputRect: QRect) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::AbstractInputPanel::setInputRect(const QRect
    &inputRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html

    Parameters
    ----------

    inputRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QtVirtualKeyboard::AbstractInputPanel::setInputRect(const QRect
    #      &inputRect)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard18AbstractInputPanel12setInputRectERK5'
        'QRect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard18AbstractInputPanel12setInputRe'
          'ctERK5QRect')
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
    'QtVirtualKeyboard::AbstractInputPanel::AbstractInputPanel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::AbstractInputPanel::AbstractInputPanel(QObject
    #      *parent)
    self._noteCreation(AbstractInputPanel, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard18AbstractInputPanelC1EP7QObject',
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
    Calls Qt's 'void QtVirtualKeyboard::AbstractInputPanel::show()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html#show
    """
    #  void QtVirtualKeyboard::AbstractInputPanel::show()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18AbstractInputPanel4showEv',
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::AbstractInputPanel::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html#hide
    """
    #  void QtVirtualKeyboard::AbstractInputPanel::hide()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18AbstractInputPanel4hideEv',
    )

  def createView(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::AbstractInputPanel::createView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html
    """
    #  void QtVirtualKeyboard::AbstractInputPanel::createView()
    ritual = 'ritual_ZN17QtVirtualKeyboard18AbstractInputPanel10createViewEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard18AbstractInputPanel10createView'
          'Ev')
    self.uglySide.call(ritual)

  def destroyView(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::AbstractInputPanel::destroyView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-abstractinputpanel.html
    """
    #  void QtVirtualKeyboard::AbstractInputPanel::destroyView()
    ritual = (
        'ritual_ZN17QtVirtualKeyboard18AbstractInputPanel11destroyViewEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard18AbstractInputPanel11destroyVie'
          'wEv')
    self.uglySide.call(ritual)
