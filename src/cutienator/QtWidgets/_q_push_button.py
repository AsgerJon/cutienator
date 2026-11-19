"""
QPushButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qpushbutton.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ._q_abstract_button import QAbstractButton
from ..QtGui import QIcon
from ._q_menu import QMenu
from ..QtCore import QMetaObject
from ..QtCore import QSize
from ._q_widget import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPushButton(QAbstractButton):
  """
  The cute side of Qt's QPushButton: a plain Python object standing in front
  of one C++ QPushButton.

  It is built on the cute 'QAbstractButton', as Qt's QPushButton is built on
  Qt's QAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPushButton that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSizeHint', 'autoDefault', 'setAutoDefault', 'isDefault',
  'setDefault', 'setMenu', 'menu', 'setFlat', 'isFlat', 'showMenu'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPushButton::~QPushButton()': the destructor: Python never removes
    a C++ QPushButton.

  What has no ritual
  ------------------

  17 of the 34 functions Qt declares: 9 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QPushButton is created at the first use, not by
    'QPushButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPushButton.
  - Qt tells when it has removed the C++ QPushButton. Every call on the cute
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
    Calls Qt's 'QString QPushButton::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#tr

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
    #  QString QPushButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QPushButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPushButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPushButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPushButton::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QPushButton10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QPushButton::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPushButton::sizeHint() const
    address = self.uglySide.call('ritual_ZNK11QPushButton8sizeHintEv')
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QPushButton::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPushButton::minimumSizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK11QPushButton15minimumSizeHintEv',
    )
    return QSize._cuteOwning(address)

  def autoDefault(self) -> bool:
    """
    Calls Qt's 'bool QPushButton::autoDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#autoDefault
    """
    #  bool QPushButton::autoDefault() const
    return self.uglySide.call('ritual_ZNK11QPushButton11autoDefaultEv')

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QPushButton::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#isDefault
    """
    #  bool QPushButton::isDefault() const
    return self.uglySide.call('ritual_ZNK11QPushButton9isDefaultEv')

  def menu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QPushButton::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#menu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QPushButton::menu() const
    address = self.uglySide.call('ritual_ZNK11QPushButton4menuEv')
    return QMenu._cuteAt(address)

  def isFlat(self) -> bool:
    """
    Calls Qt's 'bool QPushButton::isFlat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#isFlat
    """
    #  bool QPushButton::isFlat() const
    return self.uglySide.call('ritual_ZNK11QPushButton6isFlatEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoDefault(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPushButton::setAutoDefault(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#setAutoDefault

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPushButton::setAutoDefault(bool a0)
    self.uglySide.call('ritual_ZN11QPushButton14setAutoDefaultEb', a0)

  @overload(bool)
  def setDefault(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPushButton::setDefault(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#setDefault

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPushButton::setDefault(bool a0)
    self.uglySide.call('ritual_ZN11QPushButton10setDefaultEb', a0)

  @overload(QMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QPushButton::setMenu(QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#setMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPushButton::setMenu(QMenu *menu)
    self.uglySide.call(
        'ritual_ZN11QPushButton7setMenuEP5QMenu', self._addressOf(menu),
    )

  @overload(bool)
  def setFlat(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPushButton::setFlat(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#setFlat

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPushButton::setFlat(bool a0)
    self.uglySide.call('ritual_ZN11QPushButton7setFlatEb', a0)

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
    Notes what was given, for Qt's 'QPushButton::QPushButton(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#QPushButton

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPushButton::QPushButton(QWidget *parent)
    self._noteCreation(QPushButton, lambda: Rituals.call(
        'ritual_ZN11QPushButtonC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QPushButton::QPushButton(const QString
    &text, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#QPushButton

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPushButton::QPushButton(const QString &text, QWidget *parent)
    self._noteCreation(QPushButton, lambda: Rituals.call(
        'ritual_ZN11QPushButtonC1ERK7QStringP7QWidget',
        text, self._addressOf(parent),
    ))

  @overload(QIcon, str)
  @overload(QIcon, str, QWidget)
  @overload(QIcon, str, NoneType)
  def __init__(
      self,
      icon: QIcon,
      text: str,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPushButton::QPushButton(const QIcon
    &icon, const QString &text, QWidget *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#QPushButton

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPushButton::QPushButton(const QIcon &icon, const QString &text,
    #      QWidget *parent)
    self._noteCreation(QPushButton, lambda: Rituals.call(
        'ritual_ZN11QPushButtonC1ERK5QIconRK7QStringP7QWidget',
        self._valueOf(icon), text, self._addressOf(parent),
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

  def showMenu(self) -> None:
    """
    Calls Qt's 'void QPushButton::showMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbutton.html#showMenu
    """
    #  void QPushButton::showMenu()
    self.uglySide.call('ritual_ZN11QPushButton8showMenuEv')
