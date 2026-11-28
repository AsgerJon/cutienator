"""
QQuickColorGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcolorgroup_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickColorGroup to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QPalette

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorGroup(QObject):
  """
  The cute side of Qt's QQuickColorGroup: a plain Python object standing in
  front of one C++ QQuickColorGroup.

  It is built on the cute 'QObject', as Qt's QQuickColorGroup is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickColorGroup that has a ritual and that Python
  can call so far, 92 names in all: 'metaObject', 'tr', 'alternateBase',
  'setAlternateBase', 'resetAlternateBase', 'base', 'setBase', 'resetBase',
  'brightText', 'setBrightText', 'resetBrightText', 'button', 'setButton',
  'resetButton', 'buttonText', 'setButtonText', 'resetButtonText', 'dark',
  'setDark', 'resetDark', 'highlight', 'setHighlight', 'resetHighlight',
  'highlightedText', 'setHighlightedText', 'resetHighlightedText', 'light',
  'setLight', 'resetLight', 'link', 'setLink', 'resetLink', 'linkVisited',
  'setLinkVisited', 'resetLinkVisited', 'mid', 'setMid', 'resetMid',
  'midlight', 'setMidlight', 'resetMidlight', 'shadow', 'setShadow',
  'resetShadow', 'text', 'setText', 'resetText', 'toolTipBase',
  'setToolTipBase', 'resetToolTipBase', 'toolTipText', 'setToolTipText',
  'resetToolTipText', 'window', 'setWindow', 'resetWindow', 'windowText',
  'setWindowText', 'resetWindowText', 'placeholderText',
  'setPlaceholderText', 'resetPlaceholderText', 'accent', 'setAccent',
  'resetAccent', 'groupTag', 'setGroupTag', 'alternateBaseChanged',
  'baseChanged', 'brightTextChanged', 'buttonChanged', 'buttonTextChanged',
  'darkChanged', 'highlightChanged', 'highlightedTextChanged',
  'lightChanged', 'linkChanged', 'linkVisitedChanged', 'midChanged',
  'midlightChanged', 'shadowChanged', 'textChanged', 'toolTipBaseChanged',
  'toolTipTextChanged', 'windowChanged', 'windowTextChanged',
  'placeholderTextChanged', 'accentChanged', 'changed', 'defaultGroupTag',
  'currentColorGroup', 'color'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorGroup::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickColorGroup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPaletteColorProvider &QQuickColorGroup::colorProvider()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQuickPaletteColorProvider &QQuickColorGroup::colorProvider()':
    gives a type Python has no way to take yet.
  - Qt's 'QQuickColorGroup *QQuickColorGroup::createWithParent(QQuickPalette
    &parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickColorGroup::QQuickColorGroup(QQuickPalette &parent)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 107 functions Qt declares: 4 forbidden; 2 not a gap; 2 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QQuickColorGroup is created at the first use, not by
    'QQuickColorGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorGroup.
  - Qt tells when it has removed the C++ QQuickColorGroup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickColorGroup that has no cute function yet,
    'colorProvider', 'createWithParent', 'resetColor', 'setColor', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickColorGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#tr

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
    #  QString QQuickColorGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickColorGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultGroupTag() -> QPalette.ColorGroup:
    """
    Calls Qt's 'QPalette::ColorGroup QQuickColorGroup::defaultGroupTag()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#defaultGroupTag

    Returns
    -------

    QPalette.ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorGroup(number)' gives.
    """
    #  QPalette::ColorGroup QQuickColorGroup::defaultGroupTag()
    return QPalette.ColorGroup(Rituals.call(
        'ritual_ZN16QQuickColorGroup15defaultGroupTagEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorGroup'

  #  The functions Qt calls itself that QQuickColorGroup is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'currentColorGroup': (
          ('_ZNK16QQuickColorGroup17currentColorGroupEv',
           ('int', 'enum', 'QtGui:QPalette.ColorGroup'),
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
    Calls Qt's 'const QMetaObject *QQuickColorGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def alternateBase(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::alternateBase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#alternateBase

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::alternateBase() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup13alternateBaseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def base(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#base

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::base() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup4baseEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def brightText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::brightText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#brightText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::brightText() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup10brightTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def button(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#button

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::button() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup6buttonEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def buttonText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::buttonText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#buttonText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::buttonText() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup10buttonTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def dark(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::dark() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#dark

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::dark() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup4darkEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def highlight(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::highlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#highlight

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::highlight() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup9highlightEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def highlightedText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::highlightedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#highlightedText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::highlightedText() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup15highlightedTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def light(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::light() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#light

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::light() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup5lightEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def link(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::link() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#link

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::link() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup4linkEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def linkVisited(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::linkVisited() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#linkVisited

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::linkVisited() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup11linkVisitedEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def mid(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::mid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#mid

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::mid() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup3midEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def midlight(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::midlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#midlight

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::midlight() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup8midlightEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shadow(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::shadow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#shadow

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::shadow() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup6shadowEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def text(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#text

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::text() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup4textEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def toolTipBase(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::toolTipBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#toolTipBase

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::toolTipBase() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup11toolTipBaseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def toolTipText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::toolTipText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#toolTipText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::toolTipText() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup11toolTipTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def window(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#window

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::window() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup6windowEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def windowText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::windowText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#windowText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::windowText() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup10windowTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def placeholderText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::placeholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#placeholderText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::placeholderText() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup15placeholderTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def accent(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::accent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#accent

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::accent() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorGroup6accentEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def groupTag(self) -> QPalette.ColorGroup:
    """
    Calls Qt's 'QPalette::ColorGroup QQuickColorGroup::groupTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#groupTag

    Returns
    -------

    QPalette.ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorGroup(number)' gives.
    """
    #  QPalette::ColorGroup QQuickColorGroup::groupTag() const
    return QPalette.ColorGroup(self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup8groupTagEv',
    ))

  def currentColorGroup(self) -> QPalette.ColorGroup:
    """
    Calls Qt's 'QPalette::ColorGroup QQuickColorGroup::currentColorGroup()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#currentColorGroup

    Returns
    -------

    QPalette.ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorGroup(number)' gives.
    """
    #  QPalette::ColorGroup QQuickColorGroup::currentColorGroup() const
    ritual = 'ritual_ZNK16QQuickColorGroup17currentColorGroupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickColorGroup17currentColorGroupEv'
    return QPalette.ColorGroup(self.uglySide.call(ritual))

  @overload(QPalette.ColorRole)
  def color(self, role: QPalette.ColorRole) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorGroup::color(QPalette::ColorRole role)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#color

    Parameters
    ----------

    role : QPalette.ColorRole
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorGroup::color(QPalette::ColorRole role) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorGroup5colorEN8QPalette9ColorRoleE',
        role.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAlternateBase(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setAlternateBase(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setAlternateBase

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setAlternateBase(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup16setAlternateBaseERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setBase(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setBase(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setBase

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setBase(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup7setBaseERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setBrightText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setBrightText(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setBrightText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setBrightText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup13setBrightTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setButton(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setButton(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setButton

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setButton(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup9setButtonERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setButtonText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setButtonText(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setButtonText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setButtonText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup13setButtonTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setDark(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setDark(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setDark

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setDark(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup7setDarkERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setHighlight(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setHighlight(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setHighlight

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setHighlight(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup12setHighlightERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setHighlightedText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setHighlightedText(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setHighlightedText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setHighlightedText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup18setHighlightedTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setLight(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setLight(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setLight

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setLight(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup8setLightERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setLink(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setLink(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setLink

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setLink(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup7setLinkERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setLinkVisited(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setLinkVisited(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setLinkVisited

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setLinkVisited(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup14setLinkVisitedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setMid(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setMid(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setMid

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setMid(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup6setMidERK6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def setMidlight(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setMidlight(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setMidlight

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setMidlight(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup11setMidlightERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setShadow(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setShadow(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setShadow

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setShadow(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup9setShadowERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setText(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup7setTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setToolTipBase(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setToolTipBase(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setToolTipBase

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setToolTipBase(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup14setToolTipBaseERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setToolTipText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setToolTipText(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setToolTipText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setToolTipText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup14setToolTipTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setWindow(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setWindow(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setWindow

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setWindow(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup9setWindowERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setWindowText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setWindowText(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setWindowText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setWindowText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup13setWindowTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setPlaceholderText(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setPlaceholderText(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#setPlaceholderText

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setPlaceholderText(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup18setPlaceholderTextERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setAccent(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setAccent(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setAccent

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorGroup::setAccent(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup9setAccentERK6QColor',
        self._valueOf(color),
    )

  @overload(QPalette.ColorGroup)
  def setGroupTag(self, tag: QPalette.ColorGroup) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::setGroupTag(QPalette::ColorGroup
    tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#setGroupTag

    Parameters
    ----------

    tag : QPalette.ColorGroup
      Passed on as its number.
    """
    #  void QQuickColorGroup::setGroupTag(QPalette::ColorGroup tag)
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup11setGroupTagEN8QPalette10ColorGroupE',
        tag.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickColorGroup::QQuickColorGroup(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#QQuickColorGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorGroup::QQuickColorGroup(QObject *parent)
    self._noteCreation(QQuickColorGroup, lambda: Rituals.call(
        'ritual_ZN16QQuickColorGroupC1EP7QObject',
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

  def resetAlternateBase(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetAlternateBase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetAlternateBase
    """
    #  void QQuickColorGroup::resetAlternateBase()
    self.uglySide.call('ritual_ZN16QQuickColorGroup18resetAlternateBaseEv')

  def resetBase(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetBase()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetBase
    """
    #  void QQuickColorGroup::resetBase()
    self.uglySide.call('ritual_ZN16QQuickColorGroup9resetBaseEv')

  def resetBrightText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetBrightText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetBrightText
    """
    #  void QQuickColorGroup::resetBrightText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup15resetBrightTextEv')

  def resetButton(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetButton()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetButton
    """
    #  void QQuickColorGroup::resetButton()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11resetButtonEv')

  def resetButtonText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetButtonText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetButtonText
    """
    #  void QQuickColorGroup::resetButtonText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup15resetButtonTextEv')

  def resetDark(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetDark()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetDark
    """
    #  void QQuickColorGroup::resetDark()
    self.uglySide.call('ritual_ZN16QQuickColorGroup9resetDarkEv')

  def resetHighlight(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetHighlight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetHighlight
    """
    #  void QQuickColorGroup::resetHighlight()
    self.uglySide.call('ritual_ZN16QQuickColorGroup14resetHighlightEv')

  def resetHighlightedText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetHighlightedText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetHighlightedText
    """
    #  void QQuickColorGroup::resetHighlightedText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup20resetHighlightedTextEv')

  def resetLight(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetLight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetLight
    """
    #  void QQuickColorGroup::resetLight()
    self.uglySide.call('ritual_ZN16QQuickColorGroup10resetLightEv')

  def resetLink(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetLink()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetLink
    """
    #  void QQuickColorGroup::resetLink()
    self.uglySide.call('ritual_ZN16QQuickColorGroup9resetLinkEv')

  def resetLinkVisited(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetLinkVisited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetLinkVisited
    """
    #  void QQuickColorGroup::resetLinkVisited()
    self.uglySide.call('ritual_ZN16QQuickColorGroup16resetLinkVisitedEv')

  def resetMid(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetMid()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetMid
    """
    #  void QQuickColorGroup::resetMid()
    self.uglySide.call('ritual_ZN16QQuickColorGroup8resetMidEv')

  def resetMidlight(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetMidlight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetMidlight
    """
    #  void QQuickColorGroup::resetMidlight()
    self.uglySide.call('ritual_ZN16QQuickColorGroup13resetMidlightEv')

  def resetShadow(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetShadow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetShadow
    """
    #  void QQuickColorGroup::resetShadow()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11resetShadowEv')

  def resetText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetText()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetText
    """
    #  void QQuickColorGroup::resetText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup9resetTextEv')

  def resetToolTipBase(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetToolTipBase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetToolTipBase
    """
    #  void QQuickColorGroup::resetToolTipBase()
    self.uglySide.call('ritual_ZN16QQuickColorGroup16resetToolTipBaseEv')

  def resetToolTipText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetToolTipText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetToolTipText
    """
    #  void QQuickColorGroup::resetToolTipText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup16resetToolTipTextEv')

  def resetWindow(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetWindow
    """
    #  void QQuickColorGroup::resetWindow()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11resetWindowEv')

  def resetWindowText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetWindowText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetWindowText
    """
    #  void QQuickColorGroup::resetWindowText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup15resetWindowTextEv')

  def resetPlaceholderText(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetPlaceholderText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#resetPlaceholderText
    """
    #  void QQuickColorGroup::resetPlaceholderText()
    self.uglySide.call('ritual_ZN16QQuickColorGroup20resetPlaceholderTextEv')

  def resetAccent(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::resetAccent()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#resetAccent
    """
    #  void QQuickColorGroup::resetAccent()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11resetAccentEv')

  def alternateBaseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::alternateBaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#alternateBaseChanged
    """
    #  void QQuickColorGroup::alternateBaseChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup20alternateBaseChangedEv')

  def baseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::baseChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#baseChanged
    """
    #  void QQuickColorGroup::baseChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11baseChangedEv')

  def brightTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::brightTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#brightTextChanged
    """
    #  void QQuickColorGroup::brightTextChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup17brightTextChangedEv')

  def buttonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::buttonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#buttonChanged
    """
    #  void QQuickColorGroup::buttonChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup13buttonChangedEv')

  def buttonTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::buttonTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#buttonTextChanged
    """
    #  void QQuickColorGroup::buttonTextChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup17buttonTextChangedEv')

  def darkChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::darkChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#darkChanged
    """
    #  void QQuickColorGroup::darkChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11darkChangedEv')

  def highlightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::highlightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#highlightChanged
    """
    #  void QQuickColorGroup::highlightChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup16highlightChangedEv')

  def highlightedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::highlightedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#highlightedTextChanged
    """
    #  void QQuickColorGroup::highlightedTextChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup22highlightedTextChangedEv',
    )

  def lightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::lightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#lightChanged
    """
    #  void QQuickColorGroup::lightChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup12lightChangedEv')

  def linkChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::linkChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#linkChanged
    """
    #  void QQuickColorGroup::linkChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11linkChangedEv')

  def linkVisitedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::linkVisitedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#linkVisitedChanged
    """
    #  void QQuickColorGroup::linkVisitedChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup18linkVisitedChangedEv')

  def midChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::midChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#midChanged
    """
    #  void QQuickColorGroup::midChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup10midChangedEv')

  def midlightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::midlightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#midlightChanged
    """
    #  void QQuickColorGroup::midlightChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup15midlightChangedEv')

  def shadowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::shadowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#shadowChanged
    """
    #  void QQuickColorGroup::shadowChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup13shadowChangedEv')

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#textChanged
    """
    #  void QQuickColorGroup::textChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup11textChangedEv')

  def toolTipBaseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::toolTipBaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#toolTipBaseChanged
    """
    #  void QQuickColorGroup::toolTipBaseChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup18toolTipBaseChangedEv')

  def toolTipTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::toolTipTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#toolTipTextChanged
    """
    #  void QQuickColorGroup::toolTipTextChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup18toolTipTextChangedEv')

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::windowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#windowChanged
    """
    #  void QQuickColorGroup::windowChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup13windowChangedEv')

  def windowTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::windowTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#windowTextChanged
    """
    #  void QQuickColorGroup::windowTextChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup17windowTextChangedEv')

  def placeholderTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::placeholderTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#placeholderTextChanged
    """
    #  void QQuickColorGroup::placeholderTextChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickColorGroup22placeholderTextChangedEv',
    )

  def accentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::accentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorgroup.html#accentChanged
    """
    #  void QQuickColorGroup::accentChanged()
    self.uglySide.call('ritual_ZN16QQuickColorGroup13accentChangedEv')

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuickColorGroup::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorgroup.html#changed
    """
    #  void QQuickColorGroup::changed()
    self.uglySide.call('ritual_ZN16QQuickColorGroup7changedEv')

  @staticmethod
  def colorProvider(*__, **_) -> Never:
    """
    - Qt's 'const QQuickPaletteColorProvider
      &QQuickColorGroup::colorProvider() const': gives a type Python has no
      way to take yet.
    - Qt's 'QQuickPaletteColorProvider &QQuickColorGroup::colorProvider()':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickColorGroup.colorProvider' has no cute function yet. Qt's "
        "'const QQuickPaletteColorProvider "
        "&QQuickColorGroup::colorProvider() const': gives a type Python has "
        "no way to take yet. Qt's 'QQuickPaletteColorProvider "
        "&QQuickColorGroup::colorProvider()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def createWithParent(*__, **_) -> Never:
    """
    Qt's 'QQuickColorGroup *QQuickColorGroup::createWithParent(QQuickPalette
    &parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickColorGroup.createWithParent' has no cute function yet. Qt's "
        "'QQuickColorGroup "
        "*QQuickColorGroup::createWithParent(QQuickPalette &parent)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def resetColor(*__, **_) -> Never:
    """
    Qt's 'void QQuickColorGroup::resetColor(QPalette::ColorRole role,
    Notifier notifier)': takes or gives a type that cannot be passed yet:
    void (QQuickColorGroup::*)().
    """
    raise NotImplementedError(
        "'QQuickColorGroup.resetColor' has no cute function yet. Qt's 'void "
        "QQuickColorGroup::resetColor(QPalette::ColorRole role, Notifier "
        "notifier)': takes or gives a type that cannot be passed yet: void "
        "(QQuickColorGroup::*)().")

  @staticmethod
  def setColor(*__, **_) -> Never:
    """
    Qt's 'void QQuickColorGroup::setColor(QPalette::ColorRole role, QColor
    color, Notifier notifier)': takes or gives a type that cannot be passed
    yet: void (QQuickColorGroup::*)().
    """
    raise NotImplementedError(
        "'QQuickColorGroup.setColor' has no cute function yet. Qt's 'void "
        "QQuickColorGroup::setColor(QPalette::ColorRole role, QColor color, "
        "Notifier notifier)': takes or gives a type that cannot be passed "
        "yet: void (QQuickColorGroup::*)().")
