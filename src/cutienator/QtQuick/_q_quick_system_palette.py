"""
QQuickSystemPalette binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksystempalette_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickSystemPalette to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSystemPalette(QObject):
  """
  The cute side of Qt's QQuickSystemPalette: a plain Python object standing
  in front of one C++ QQuickSystemPalette.

  It is built on the cute 'QObject', as Qt's QQuickSystemPalette is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSystemPalette that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'window',
  'windowText', 'base', 'text', 'alternateBase', 'button', 'buttonText',
  'light', 'midlight', 'dark', 'mid', 'shadow', 'highlight',
  'highlightedText', 'placeholderText', 'accent', 'colorGroup',
  'setColorGroup', 'eventFilter', 'paletteChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSystemPalette::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSystemPalette::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSystemPalettePrivate *QQuickSystemPalette::d_func()': gives
    'QQuickSystemPalettePrivate', which has no cute class yet.
  - Qt's 'const QQuickSystemPalettePrivate *QQuickSystemPalette::d_func()
    const': gives 'QQuickSystemPalettePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSystemPalette is created at the first use, not by
    'QQuickSystemPalette(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSystemPalette.
  - Qt tells when it has removed the C++ QQuickSystemPalette. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickSystemPalette, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ColorGroup(CuteNum):
    """
    The enum 'QQuickSystemPalette::ColorGroup' of Qt, with the 3 names Qt
    gives in it.
    """

    Active = Kee[int](0)
    Inactive = Kee[int](2)
    Disabled = Kee[int](1)

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
    Calls Qt's 'QString QQuickSystemPalette::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#tr

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
    #  QString QQuickSystemPalette::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickSystemPalette2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSystemPalette'

  #  A C++ QQuickSystemPalette Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSystemPalette'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSystemPalette::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSystemPalette::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def window(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#window

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::window() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette6windowEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def windowText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::windowText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#windowText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::windowText() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette10windowTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def base(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#base

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::base() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette4baseEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def text(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#text

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::text() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette4textEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def alternateBase(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::alternateBase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#alternateBase

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::alternateBase() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette13alternateBaseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def button(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#button

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::button() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette6buttonEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def buttonText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::buttonText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#buttonText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::buttonText() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette10buttonTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def light(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::light() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#light

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::light() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette5lightEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def midlight(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::midlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#midlight

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::midlight() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette8midlightEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def dark(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::dark() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#dark

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::dark() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette4darkEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def mid(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::mid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#mid

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::mid() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette3midEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shadow(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::shadow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#shadow

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::shadow() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette6shadowEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def highlight(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::highlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#highlight

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::highlight() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette9highlightEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def highlightedText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::highlightedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#highlightedText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::highlightedText() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette15highlightedTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def placeholderText(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::placeholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#placeholderText

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::placeholderText() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette15placeholderTextEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def accent(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickSystemPalette::accent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksystempalette.html#accent

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickSystemPalette::accent() const
    address = self.uglySide.call('ritual_ZNK19QQuickSystemPalette6accentEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def colorGroup(self) -> ColorGroup:
    """
    Calls Qt's 'QQuickSystemPalette::ColorGroup
    QQuickSystemPalette::colorGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#colorGroup

    Returns
    -------

    ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorGroup(number)'
      gives.
    """
    #  QQuickSystemPalette::ColorGroup QQuickSystemPalette::colorGroup()
    #      const
    return QQuickSystemPalette.ColorGroup(self.uglySide.call(
        'ritual_ZNK19QQuickSystemPalette10colorGroupEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ColorGroup)
  def setColorGroup(self, a0: ColorGroup) -> None:
    """
    Calls Qt's 'void
    QQuickSystemPalette::setColorGroup(QQuickSystemPalette::ColorGroup a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#setColorGroup

    Parameters
    ----------

    a0 : ColorGroup
      Passed on as its number.
    """
    #  void
    #      QQuickSystemPalette::setColorGroup(QQuickSystemPalette::ColorGroup
    #      a0)
    self.uglySide.call(
        'ritual_ZN19QQuickSystemPalette13setColorGroupENS_10ColorGroupE',
        a0.value,
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
    'QQuickSystemPalette::QQuickSystemPalette(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#QQuickSystemPalette

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSystemPalette::QQuickSystemPalette(QObject *parent)
    self._noteCreation(QQuickSystemPalette, lambda: Rituals.call(
        'ritual_ZN19QQuickSystemPaletteC1EP7QObject',
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickSystemPalette::eventFilter(QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickSystemPalette::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN19QQuickSystemPalette11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickSystemPalette11eventFilterEP7QObjectP6QEven'
          't')
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSystemPalette::paletteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksystempalette.html#paletteChanged
    """
    #  void QQuickSystemPalette::paletteChanged()
    self.uglySide.call('ritual_ZN19QQuickSystemPalette14paletteChangedEv')
