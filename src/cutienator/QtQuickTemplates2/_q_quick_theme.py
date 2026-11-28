"""
QQuickTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktheme_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTheme to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QFont, QPalette
  from . import QQuickThemePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPalette = WAIT['QPalette']


class QQuickTheme(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickTheme: a plain Python object standing in front
  of one C++ QQuickTheme.

  What exists
  -----------

  Every function of Qt's QQuickTheme that has a ritual and that Python can
  call so far, 8 names in all: 'instance', 'font', 'palette', 'setFont',
  'setPalette', 'setUsePlatformPalette', 'usePlatformPalette', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickTheme::~QQuickTheme()': the destructor: Python never removes
    a C++ QQuickTheme.
  - Qt's 'const QQuickThemePrivate *QQuickTheme::d_func() const': takes in
    Python what 'QQuickThemePrivate *QQuickTheme::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTheme is created at the first use, not by
    'QQuickTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTheme.
  """

  #  The enums Qt writes inside QQuickTheme, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Scope(CuteNum):
    """
    The enum 'QQuickTheme::Scope' of Qt, with the 19 names Qt gives in it.
    """

    System = Kee[int](0)
    Button = Kee[int](1)
    CheckBox = Kee[int](2)
    ComboBox = Kee[int](3)
    GroupBox = Kee[int](4)
    ItemView = Kee[int](5)
    Label = Kee[int](6)
    ListView = Kee[int](7)
    Menu = Kee[int](8)
    MenuBar = Kee[int](9)
    RadioButton = Kee[int](10)
    SpinBox = Kee[int](11)
    Switch = Kee[int](12)
    TabBar = Kee[int](13)
    TextArea = Kee[int](14)
    TextField = Kee[int](15)
    ToolBar = Kee[int](16)
    ToolTip = Kee[int](17)
    Tumbler = Kee[int](18)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QQuickTheme]:
    """
    Calls Qt's 'QQuickTheme *QQuickTheme::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#instance

    Returns
    -------

    Optional[QQuickTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTheme *QQuickTheme::instance()
    address = Rituals.call('ritual_ZN11QQuickTheme8instanceEv')
    return QQuickTheme._cuteAt(address)

  @staticmethod
  @overload(Scope)
  def font(scope: Scope) -> QFont:
    """
    Calls Qt's 'QFont QQuickTheme::font(Scope scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#font

    Parameters
    ----------

    scope : Scope
      Passed on as its number.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTheme::font(Scope scope)
    address = Rituals.call(
        'ritual_ZN11QQuickTheme4fontENS_5ScopeE', scope.value,
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(Scope)
  def palette(scope: Scope) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickTheme::palette(Scope scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#palette

    Parameters
    ----------

    scope : Scope
      Passed on as its number.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickTheme::palette(Scope scope)
    address = Rituals.call(
        'ritual_ZN11QQuickTheme7paletteENS_5ScopeE', scope.value,
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTheme'

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

  @overload(Scope, QFont)
  def setFont(self, scope: Scope, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTheme::setFont(Scope scope, const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#setFont

    Parameters
    ----------

    scope : Scope
      Passed on as its number.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTheme::setFont(Scope scope, const QFont &font)
    self.uglySide.call(
        'ritual_ZN11QQuickTheme7setFontENS_5ScopeERK5QFont',
        scope.value, self._valueOf(font),
    )

  @overload(Scope, QPalette)
  def setPalette(self, scope: Scope, palette: QPalette) -> None:
    """
    Calls Qt's 'void QQuickTheme::setPalette(Scope scope, const QPalette
    &palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#setPalette

    Parameters
    ----------

    scope : Scope
      Passed on as its number.

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickTheme::setPalette(Scope scope, const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN11QQuickTheme10setPaletteENS_5ScopeERK8QPalette',
        scope.value, self._valueOf(palette),
    )

  @overload(bool)
  def setUsePlatformPalette(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickTheme::setUsePlatformPalette(const bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktheme.html#setUsePlatformPalette

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickTheme::setUsePlatformPalette(const bool enable)
    self.uglySide.call(
        'ritual_ZN11QQuickTheme21setUsePlatformPaletteEb', enable,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuickTheme::QQuickTheme()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#QQuickTheme
    """
    #  QQuickTheme::QQuickTheme()
    self._noteCreation(QQuickTheme, lambda: Rituals.call(
        'ritual_ZN11QQuickThemeC1Ev',
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

  def usePlatformPalette(self) -> bool:
    """
    Calls Qt's 'bool QQuickTheme::usePlatformPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktheme.html#usePlatformPalette
    """
    #  bool QQuickTheme::usePlatformPalette()
    return self.uglySide.call('ritual_ZN11QQuickTheme18usePlatformPaletteEv')

  def d_func(self) -> Optional[QQuickThemePrivate]:
    """
    Calls Qt's 'QQuickThemePrivate *QQuickTheme::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktheme.html#d_func

    Returns
    -------

    Optional[QQuickThemePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickThemePrivate *QQuickTheme::d_func()
    address = self.uglySide.call('ritual_ZN11QQuickTheme6d_funcEv')
    from . import QQuickThemePrivate
    return QQuickThemePrivate._cuteAt(address)
