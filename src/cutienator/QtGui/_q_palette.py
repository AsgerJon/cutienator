"""
QPalette binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpalette.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QBrush, QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']


class QPalette(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPalette: a plain Python object standing in front of
  one C++ QPalette.

  C++ hands a QPalette around as a copy, so every C++ QPalette behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPalette that has a ritual and that Python can call
  so far, 37 names in all: 'currentColorGroup', 'setCurrentColorGroup',
  'color', 'brush', 'setColor', 'setBrush', 'isBrushSet', 'setColorGroup',
  'isEqual', 'windowText', 'button', 'light', 'dark', 'mid', 'text', 'base',
  'alternateBase', 'toolTipBase', 'toolTipText', 'window', 'midlight',
  'brightText', 'buttonText', 'shadow', 'highlight', 'highlightedText',
  'link', 'linkVisited', 'placeholderText', 'accent', '__eq__', '__ne__',
  'isCopyOf', 'cacheKey', 'resolve', 'resolveMask', 'setResolveMask'. It can
  be made from Python, in 7 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPalette::~QPalette()': the destructor: Python removes its C++
    QPalette by it, and has no other use for it.
  - Qt's 'QVariant QPalette::operator QVariant() const': an operator Python
    has no name for.

  What has no ritual
  ------------------

  12 of the 62 functions Qt declares: 5 private; 5 takes or gives a type that
  cannot be passed yet; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QPalette is created at the first use, not by 'QPalette(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPalette back gives a copy the ritual made for
    Python, in a new cute QPalette.
  """

  #  The enums Qt writes inside QPalette, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ColorGroup(CuteNum):
    """
    The enum 'QPalette::ColorGroup' of Qt, with the 7 names Qt gives in it.
    """

    Active = Kee[int](0)
    Disabled = Kee[int](1)
    Inactive = Kee[int](2)
    NColorGroups = Kee[int](3)
    Current = Kee[int](4)
    All = Kee[int](5)
    Normal = Kee[int](0)

  class ColorRole(CuteNum):
    """
    The enum 'QPalette::ColorRole' of Qt, with the 23 names Qt gives in it.
    """

    WindowText = Kee[int](0)
    Button = Kee[int](1)
    Light = Kee[int](2)
    Midlight = Kee[int](3)
    Dark = Kee[int](4)
    Mid = Kee[int](5)
    Text = Kee[int](6)
    BrightText = Kee[int](7)
    ButtonText = Kee[int](8)
    Base = Kee[int](9)
    Window = Kee[int](10)
    Shadow = Kee[int](11)
    Highlight = Kee[int](12)
    HighlightedText = Kee[int](13)
    Link = Kee[int](14)
    LinkVisited = Kee[int](15)
    AlternateBase = Kee[int](16)
    NoRole = Kee[int](17)
    ToolTipBase = Kee[int](18)
    ToolTipText = Kee[int](19)
    PlaceholderText = Kee[int](20)
    Accent = Kee[int](21)
    NColorRoles = Kee[int](22)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPalette'

  #  Qt's '~QPalette()'. Naming it makes this a value class: Python owns
  #  every C++ QPalette behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QPaletteD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentColorGroup(self) -> ColorGroup:
    """
    Calls Qt's 'ColorGroup QPalette::currentColorGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#currentColorGroup

    Returns
    -------

    ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorGroup(number)'
      gives.
    """
    #  ColorGroup QPalette::currentColorGroup() const
    return QPalette.ColorGroup(self.uglySide.call(
        'ritual_ZNK8QPalette17currentColorGroupEv',
    ))

  @overload(ColorGroup, ColorRole)
  def color(self, cg: ColorGroup, cr: ColorRole) -> QColor:
    """
    Calls Qt's 'const QColor &QPalette::color(ColorGroup cg, ColorRole cr)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#color

    Parameters
    ----------

    cg : ColorGroup
      Passed on as its number.

    cr : ColorRole
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QPalette::color(ColorGroup cg, ColorRole cr) const
    address = self.uglySide.call(
        'ritual_ZNK8QPalette5colorENS_10ColorGroupENS_9ColorRoleE',
        cg.value, cr.value,
    )
    from . import QColor
    return QColor._cuteOwning(address)

  @overload(ColorRole)
  def color(self, cr: ColorRole) -> QColor:
    """
    Calls Qt's 'const QColor &QPalette::color(ColorRole cr) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#color

    Parameters
    ----------

    cr : ColorRole
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QPalette::color(ColorRole cr) const
    address = self.uglySide.call(
        'ritual_ZNK8QPalette5colorENS_9ColorRoleE', cr.value,
    )
    from . import QColor
    return QColor._cuteOwning(address)

  @overload(ColorGroup, ColorRole)
  def brush(self, cg: ColorGroup, cr: ColorRole) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::brush(ColorGroup cg, ColorRole cr)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#brush

    Parameters
    ----------

    cg : ColorGroup
      Passed on as its number.

    cr : ColorRole
      Passed on as its number.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::brush(ColorGroup cg, ColorRole cr) const
    address = self.uglySide.call(
        'ritual_ZNK8QPalette5brushENS_10ColorGroupENS_9ColorRoleE',
        cg.value, cr.value,
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  @overload(ColorRole)
  def brush(self, cr: ColorRole) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::brush(ColorRole cr) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#brush

    Parameters
    ----------

    cr : ColorRole
      Passed on as its number.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::brush(ColorRole cr) const
    address = self.uglySide.call(
        'ritual_ZNK8QPalette5brushENS_9ColorRoleE', cr.value,
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  @overload(ColorGroup, ColorRole)
  def isBrushSet(self, cg: ColorGroup, cr: ColorRole) -> bool:
    """
    Calls Qt's 'bool QPalette::isBrushSet(ColorGroup cg, ColorRole cr)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#isBrushSet

    Parameters
    ----------

    cg : ColorGroup
      Passed on as its number.

    cr : ColorRole
      Passed on as its number.
    """
    #  bool QPalette::isBrushSet(ColorGroup cg, ColorRole cr) const
    return self.uglySide.call(
        'ritual_ZNK8QPalette10isBrushSetENS_10ColorGroupENS_9ColorRoleE',
        cg.value, cr.value,
    )

  @overload(ColorGroup, ColorGroup)
  def isEqual(self, cr1: ColorGroup, cr2: ColorGroup) -> bool:
    """
    Calls Qt's 'bool QPalette::isEqual(ColorGroup cr1, ColorGroup cr2)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#isEqual

    Parameters
    ----------

    cr1 : ColorGroup
      Passed on as its number.

    cr2 : ColorGroup
      Passed on as its number.
    """
    #  bool QPalette::isEqual(ColorGroup cr1, ColorGroup cr2) const
    return self.uglySide.call(
        'ritual_ZNK8QPalette7isEqualENS_10ColorGroupES0_',
        cr1.value, cr2.value,
    )

  def windowText(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::windowText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#windowText

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::windowText() const
    address = self.uglySide.call('ritual_ZNK8QPalette10windowTextEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def button(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#button

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::button() const
    address = self.uglySide.call('ritual_ZNK8QPalette6buttonEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def light(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::light() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#light

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::light() const
    address = self.uglySide.call('ritual_ZNK8QPalette5lightEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def dark(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::dark() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#dark

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::dark() const
    address = self.uglySide.call('ritual_ZNK8QPalette4darkEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def mid(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::mid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#mid

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::mid() const
    address = self.uglySide.call('ritual_ZNK8QPalette3midEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def text(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#text

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::text() const
    address = self.uglySide.call('ritual_ZNK8QPalette4textEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def base(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#base

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::base() const
    address = self.uglySide.call('ritual_ZNK8QPalette4baseEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def alternateBase(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::alternateBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#alternateBase

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::alternateBase() const
    address = self.uglySide.call('ritual_ZNK8QPalette13alternateBaseEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def toolTipBase(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::toolTipBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#toolTipBase

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::toolTipBase() const
    address = self.uglySide.call('ritual_ZNK8QPalette11toolTipBaseEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def toolTipText(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::toolTipText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#toolTipText

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::toolTipText() const
    address = self.uglySide.call('ritual_ZNK8QPalette11toolTipTextEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def window(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#window

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::window() const
    address = self.uglySide.call('ritual_ZNK8QPalette6windowEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def midlight(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::midlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#midlight

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::midlight() const
    address = self.uglySide.call('ritual_ZNK8QPalette8midlightEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def brightText(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::brightText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#brightText

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::brightText() const
    address = self.uglySide.call('ritual_ZNK8QPalette10brightTextEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def buttonText(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::buttonText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#buttonText

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::buttonText() const
    address = self.uglySide.call('ritual_ZNK8QPalette10buttonTextEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def shadow(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::shadow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#shadow

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::shadow() const
    address = self.uglySide.call('ritual_ZNK8QPalette6shadowEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def highlight(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::highlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#highlight

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::highlight() const
    address = self.uglySide.call('ritual_ZNK8QPalette9highlightEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def highlightedText(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::highlightedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#highlightedText

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::highlightedText() const
    address = self.uglySide.call('ritual_ZNK8QPalette15highlightedTextEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def link(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::link() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#link

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::link() const
    address = self.uglySide.call('ritual_ZNK8QPalette4linkEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def linkVisited(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::linkVisited() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#linkVisited

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::linkVisited() const
    address = self.uglySide.call('ritual_ZNK8QPalette11linkVisitedEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def placeholderText(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::placeholderText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#placeholderText

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::placeholderText() const
    address = self.uglySide.call('ritual_ZNK8QPalette15placeholderTextEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def accent(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPalette::accent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#accent

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPalette::accent() const
    address = self.uglySide.call('ritual_ZNK8QPalette6accentEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  @overload(THIS)
  def isCopyOf(self, p: QPalette) -> bool:
    """
    Calls Qt's 'bool QPalette::isCopyOf(const QPalette &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#isCopyOf

    Parameters
    ----------

    p : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QPalette::isCopyOf(const QPalette &p) const
    return self.uglySide.call(
        'ritual_ZNK8QPalette8isCopyOfERKS_', self._valueOf(p),
    )

  def cacheKey(self) -> int:
    """
    Calls Qt's 'qint64 QPalette::cacheKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#cacheKey
    """
    #  qint64 QPalette::cacheKey() const
    return self.uglySide.call('ritual_ZNK8QPalette8cacheKeyEv')

  @overload(THIS)
  def resolve(self, other: QPalette) -> QPalette:
    """
    Calls Qt's 'QPalette QPalette::resolve(const QPalette &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#resolve

    Parameters
    ----------

    other : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QPalette::resolve(const QPalette &other) const
    address = self.uglySide.call(
        'ritual_ZNK8QPalette7resolveERKS_', self._valueOf(other),
    )
    return QPalette._cuteOwning(address)

  def resolveMask(self) -> int:
    """
    Calls Qt's 'ResolveMask QPalette::resolveMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#resolveMask
    """
    #  ResolveMask QPalette::resolveMask() const
    return self.uglySide.call('ritual_ZNK8QPalette11resolveMaskEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ColorGroup)
  def setCurrentColorGroup(self, cg: ColorGroup) -> None:
    """
    Calls Qt's 'void QPalette::setCurrentColorGroup(ColorGroup cg)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setCurrentColorGroup

    Parameters
    ----------

    cg : ColorGroup
      Passed on as its number.
    """
    #  void QPalette::setCurrentColorGroup(ColorGroup cg)
    self.uglySide.call(
        'ritual_ZN8QPalette20setCurrentColorGroupENS_10ColorGroupE',
        cg.value,
    )

  @overload(ColorGroup, ColorRole, QColor)
  def setColor(self, cg: ColorGroup, cr: ColorRole, color: QColor) -> None:
    """
    Calls Qt's 'void QPalette::setColor(ColorGroup cg, ColorRole cr, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setColor

    Parameters
    ----------

    cg : ColorGroup
      Passed on as its number.

    cr : ColorRole
      Passed on as its number.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPalette::setColor(ColorGroup cg, ColorRole cr, const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN8QPalette8setColorENS_10ColorGroupENS_9ColorRoleERK6QColo'
        'r',
        cg.value, cr.value, self._valueOf(color),
    )

  @overload(ColorRole, QColor)
  def setColor(self, cr: ColorRole, color: QColor) -> None:
    """
    Calls Qt's 'void QPalette::setColor(ColorRole cr, const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setColor

    Parameters
    ----------

    cr : ColorRole
      Passed on as its number.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPalette::setColor(ColorRole cr, const QColor &color)
    self.uglySide.call(
        'ritual_ZN8QPalette8setColorENS_9ColorRoleERK6QColor',
        cr.value, self._valueOf(color),
    )

  @overload(ColorRole, QBrush)
  def setBrush(self, cr: ColorRole, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPalette::setBrush(ColorRole cr, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setBrush

    Parameters
    ----------

    cr : ColorRole
      Passed on as its number.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPalette::setBrush(ColorRole cr, const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN8QPalette8setBrushENS_9ColorRoleERK6QBrush',
        cr.value, self._valueOf(brush),
    )

  @overload(ColorGroup, ColorRole, QBrush)
  def setBrush(self, cg: ColorGroup, cr: ColorRole, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPalette::setBrush(ColorGroup cg, ColorRole cr, const
    QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setBrush

    Parameters
    ----------

    cg : ColorGroup
      Passed on as its number.

    cr : ColorRole
      Passed on as its number.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPalette::setBrush(ColorGroup cg, ColorRole cr, const QBrush
    #      &brush)
    self.uglySide.call(
        'ritual_ZN8QPalette8setBrushENS_10ColorGroupENS_9ColorRoleERK6QBrus'
        'h',
        cg.value, cr.value, self._valueOf(brush),
    )

  @overload(
      ColorGroup, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush,
      QBrush, QBrush,
  )
  def setColorGroup(
      self,
      cr: ColorGroup,
      windowText: QBrush,
      button: QBrush,
      light: QBrush,
      dark: QBrush,
      mid: QBrush,
      text: QBrush,
      bright_text: QBrush,
      base: QBrush,
      window: QBrush,
  ) -> None:
    """
    Calls Qt's 'void QPalette::setColorGroup(ColorGroup cr, const QBrush
    &windowText, const QBrush &button, const QBrush &light, const QBrush
    &dark, const QBrush &mid, const QBrush &text, const QBrush &bright_text,
    const QBrush &base, const QBrush &window)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setColorGroup

    Parameters
    ----------

    cr : ColorGroup
      Passed on as its number.

    windowText : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    button : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    light : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    dark : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    mid : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    text : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    bright_text : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    base : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    window : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPalette::setColorGroup(ColorGroup cr, const QBrush &windowText,
    #      const QBrush &button, const QBrush &light, const QBrush &dark,
    #      const QBrush &mid, const QBrush &text, const QBrush &bright_text,
    #      const QBrush &base, const QBrush &window)
    self.uglySide.call(
        'ritual_ZN8QPalette13setColorGroupENS_10ColorGroupERK6QBrushS3_S3_S'
        '3_S3_S3_S3_S3_S3_',
        cr.value, self._valueOf(windowText), self._valueOf(button),
        self._valueOf(light), self._valueOf(dark), self._valueOf(mid),
        self._valueOf(text), self._valueOf(bright_text), self._valueOf(base),
        self._valueOf(window),
    )

  @overload(int)
  def setResolveMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QPalette::setResolveMask(ResolveMask mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#setResolveMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QPalette::setResolveMask(ResolveMask mask)
    self.uglySide.call('ritual_ZN8QPalette14setResolveMaskEy', mask)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, p: QPalette) -> bool:
    """
    Calls Qt's 'bool QPalette::operator==(const QPalette &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#operator==

    Parameters
    ----------

    p : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QPalette::operator==(const QPalette &p) const
    return self.uglySide.call('ritual_ZNK8QPaletteeqERKS_', self._valueOf(p))

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, p: QPalette) -> bool:
    """
    Calls Qt's 'bool QPalette::operator!=(const QPalette &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#operator!=

    Parameters
    ----------

    p : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QPalette::operator!=(const QPalette &p) const
    return self.uglySide.call('ritual_ZNK8QPaletteneERKS_', self._valueOf(p))

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette
    """
    #  QPalette::QPalette()
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1Ev',
    ))

  @overload(QColor)
  def __init__(self, button: QColor) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette(const QColor
    &button)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette

    Parameters
    ----------

    button : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QPalette::QPalette(const QColor &button)
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1ERK6QColor', self._valueOf(button),
    ))

  @overload(Qt.GlobalColor)
  def __init__(self, button: Qt.GlobalColor) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette(Qt::GlobalColor
    button)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette

    Parameters
    ----------

    button : Qt.GlobalColor
      Passed on as its number.
    """
    #  QPalette::QPalette(Qt::GlobalColor button)
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1EN2Qt11GlobalColorE', button.value,
    ))

  @overload(QColor, QColor)
  def __init__(self, button: QColor, window: QColor) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette(const QColor &button,
    const QColor &window)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette

    Parameters
    ----------

    button : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    window : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QPalette::QPalette(const QColor &button, const QColor &window)
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1ERK6QColorS2_',
        self._valueOf(button), self._valueOf(window),
    ))

  @overload(
      QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush,
  )
  def __init__(
      self,
      windowText: QBrush,
      button: QBrush,
      light: QBrush,
      dark: QBrush,
      mid: QBrush,
      text: QBrush,
      bright_text: QBrush,
      base: QBrush,
      window: QBrush,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette(const QBrush
    &windowText, const QBrush &button, const QBrush &light, const QBrush
    &dark, const QBrush &mid, const QBrush &text, const QBrush &bright_text,
    const QBrush &base, const QBrush &window)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette

    Parameters
    ----------

    windowText : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    button : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    light : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    dark : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    mid : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    text : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    bright_text : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    base : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    window : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  QPalette::QPalette(const QBrush &windowText, const QBrush &button,
    #      const QBrush &light, const QBrush &dark, const QBrush &mid, const
    #      QBrush &text, const QBrush &bright_text, const QBrush &base, const
    #      QBrush &window)
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1ERK6QBrushS2_S2_S2_S2_S2_S2_S2_S2_',
        self._valueOf(windowText), self._valueOf(button),
        self._valueOf(light), self._valueOf(dark), self._valueOf(mid),
        self._valueOf(text), self._valueOf(bright_text), self._valueOf(base),
        self._valueOf(window),
    ))

  @overload(QColor, QColor, QColor, QColor, QColor, QColor, QColor)
  def __init__(
      self,
      windowText: QColor,
      window: QColor,
      light: QColor,
      dark: QColor,
      mid: QColor,
      text: QColor,
      base: QColor,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette(const QColor
    &windowText, const QColor &window, const QColor &light, const QColor
    &dark, const QColor &mid, const QColor &text, const QColor &base)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette

    Parameters
    ----------

    windowText : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    window : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    light : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    dark : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    mid : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    text : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    base : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QPalette::QPalette(const QColor &windowText, const QColor &window,
    #      const QColor &light, const QColor &dark, const QColor &mid, const
    #      QColor &text, const QColor &base)
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1ERK6QColorS2_S2_S2_S2_S2_S2_',
        self._valueOf(windowText), self._valueOf(window),
        self._valueOf(light), self._valueOf(dark), self._valueOf(mid),
        self._valueOf(text), self._valueOf(base),
    ))

  @overload(THIS)
  def __init__(self, palette: QPalette) -> None:
    """
    Notes what was given, for Qt's 'QPalette::QPalette(const QPalette
    &palette)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpalette.html#QPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  QPalette::QPalette(const QPalette &palette)
    self._noteCreation(QPalette, lambda: Rituals.call(
        'ritual_ZN8QPaletteC1ERKS_', self._valueOf(palette),
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
