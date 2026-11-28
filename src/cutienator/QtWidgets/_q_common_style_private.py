"""
QCommonStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcommonstyle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCommonStylePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QStylePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QPointF, QRect, QSize
  from ..QtGui import QFont, QPainter, QTextOption
  from . import QCommonStyle, QStyleAnimation, QStyleOption, QStyleOptionTab
  from . import QStyleOptionToolButton, QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QObject = WAIT['QObject']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QStyleAnimation = WAIT['QStyleAnimation']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionTab = WAIT['QStyleOptionTab']
  QStyleOptionToolButton = WAIT['QStyleOptionToolButton']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QTextOption = WAIT['QTextOption']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCommonStylePrivate(QStylePrivate):
  """
  The cute side of Qt's QCommonStylePrivate: a plain Python object standing
  in front of one C++ QCommonStylePrivate.

  It is built on the cute 'QStylePrivate', as Qt's QCommonStylePrivate is
  built on Qt's QStylePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCommonStylePrivate that has a ritual and that
  Python can call so far, 13 names in all: 'q_func', 'calculateElidedText',
  'viewItemDrawText', 'viewItemLayout', 'viewItemSize', 'isViewItemCached',
  'toolButtonElideText', 'tabLayout', 'animation', 'startAnimation',
  'stopAnimation', 'removeAnimation', 'rtl'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCommonStyle *QCommonStylePrivate::q_func() const': takes in
    Python what 'QCommonStyle *QCommonStylePrivate::q_func()' takes.
  - Qt's 'QCommonStylePrivate::~QCommonStylePrivate()': the destructor:
    Python never removes a C++ QCommonStylePrivate.
  - Qt's 'QIcon
    QCommonStylePrivate::iconFromWindowsTheme(QCommonStyle::StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QIcon
    QCommonStylePrivate::iconFromMacTheme(QCommonStyle::StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QIcon QCommonStylePrivate::iconFromApplicationTheme(QCommonStyle::
    StandardPixmap standardIcon, const QStyleOption *option, const QWidget
    *widget) const': takes a type Python has no way to hand over yet.
  - Qt's 'QIcon
    QCommonStylePrivate::iconFromResourceTheme(QCommonStyle::StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCommonStylePrivate is created at the first use, not by
    'QCommonStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCommonStylePrivate.
  - Each name of Qt's QCommonStylePrivate that has no cute function yet,
    'iconFromApplicationTheme', 'iconFromMacTheme', 'iconFromResourceTheme',
    'iconFromWindowsTheme', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStyleOption)
  @overload(NoneType)
  def rtl(option: Optional[QStyleOption]) -> bool:
    """
    Calls Qt's 'bool QCommonStylePrivate::rtl(const QStyleOption *option)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyleprivate.html#rtl

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCommonStylePrivate::rtl(const QStyleOption *option)
    return Rituals.call(
        'ritual_ZN19QCommonStylePrivate3rtlEPK12QStyleOption',
        CuteMixin._addressOf(option),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCommonStylePrivate'

  #  A C++ QCommonStylePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCommonStylePrivate'

  #  The functions Qt calls itself that QCommonStylePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'tabLayout': (
          ('_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTabPK7QWidg'
           'etP5QRectS7_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionTab'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtCore:QRect'),
               ('address', 'address', 'QtCore:QRect'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      str, QTextOption, QFont, QRect, Qt.Alignment, Qt.TextElideMode, int,
      bool, QPointF,
  )
  @overload(
      str, QTextOption, QFont, QRect, Qt.Alignment, Qt.TextElideMode, int,
      bool, NoneType,
  )
  def calculateElidedText(
      self,
      text: str,
      textOption: QTextOption,
      font: QFont,
      textRect: QRect,
      valign: Qt.Alignment,
      textElideMode: Qt.TextElideMode,
      flags: int,
      lastVisibleLineShouldBeElided: bool,
      paintStartPosition: Optional[QPointF],
  ) -> str:
    """
    Calls Qt's 'QString QCommonStylePrivate::calculateElidedText(const
    QString &text, const QTextOption &textOption, const QFont &font, const
    QRect &textRect, const Qt::Alignment valign, Qt::TextElideMode
    textElideMode, int flags, bool lastVisibleLineShouldBeElided, QPointF
    *paintStartPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#calculateElidedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    textRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    valign : Qt.Alignment
      Passed on as its number.

    textElideMode : Qt.TextElideMode
      Passed on as its number.

    flags : int
      Passed on as it is.

    lastVisibleLineShouldBeElided : bool
      Passed on as it is.

    paintStartPosition : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommonStylePrivate::calculateElidedText(const QString &text,
    #      const QTextOption &textOption, const QFont &font, const QRect
    #      &textRect, const Qt::Alignment valign, Qt::TextElideMode
    #      textElideMode, int flags, bool lastVisibleLineShouldBeElided,
    #      QPointF *paintStartPosition) const
    return self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate19calculateElidedTextERK7QStringRK1'
        '1QTextOptionRK5QFontRK5QRect6QFlagsIN2Qt13AlignmentFlagEENSD_13Tex'
        'tElideModeEibP7QPointF',
        text, self._valueOf(textOption), self._valueOf(font),
        self._valueOf(textRect), valign.value, textElideMode.value, flags,
        lastVisibleLineShouldBeElided, self._addressOf(paintStartPosition,
        'QPointF'),
    )

  @overload(QStyleOptionViewItem, int)
  @overload(NoneType, int)
  def viewItemSize(
      self,
      option: Optional[QStyleOptionViewItem],
      role: int,
  ) -> QSize:
    """
    Calls Qt's 'QSize QCommonStylePrivate::viewItemSize(const
    QStyleOptionViewItem *option, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#viewItemSize

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : int
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCommonStylePrivate::viewItemSize(const QStyleOptionViewItem
    #      *option, int role) const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate12viewItemSizeEPK20QStyleOptionView'
        'Itemi',
        self._addressOf(option), role,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyleOptionViewItem)
  def isViewItemCached(self, option: QStyleOptionViewItem) -> bool:
    """
    Calls Qt's 'bool QCommonStylePrivate::isViewItemCached(const
    QStyleOptionViewItem &option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#isViewItemCached

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.
    """
    #  bool QCommonStylePrivate::isViewItemCached(const QStyleOptionViewItem
    #      &option) const
    return self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate16isViewItemCachedERK20QStyleOption'
        'ViewItem',
        self._valueOf(option),
    )

  @overload(QStyleOptionToolButton, QRect, int)
  @overload(NoneType, QRect, int)
  def toolButtonElideText(
      self,
      toolbutton: Optional[QStyleOptionToolButton],
      textRect: QRect,
      flags: int,
  ) -> str:
    """
    Calls Qt's 'QString QCommonStylePrivate::toolButtonElideText(const
    QStyleOptionToolButton *toolbutton, const QRect &textRect, int flags)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#toolButtonElideText

    Parameters
    ----------

    toolbutton : Optional[QStyleOptionToolButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    textRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommonStylePrivate::toolButtonElideText(const
    #      QStyleOptionToolButton *toolbutton, const QRect &textRect, int
    #      flags) const
    return self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate19toolButtonElideTextEPK22QStyleOpt'
        'ionToolButtonRK5QRecti',
        self._addressOf(toolbutton), self._valueOf(textRect), flags,
    )

  @overload(QObject)
  @overload(NoneType)
  def animation(
      self,
      target: Optional[QObject],
  ) -> Optional[QStyleAnimation]:
    """
    Calls Qt's 'QStyleAnimation *QCommonStylePrivate::animation(const QObject
    *target) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyleprivate.html#animation

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QStyleAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleAnimation *QCommonStylePrivate::animation(const QObject *target)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate9animationEPK7QObject',
        self._addressOf(target, 'QObject'),
    )
    from . import QStyleAnimation
    return QStyleAnimation._cuteAt(address)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCommonStylePrivate::QCommonStylePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#QCommonStylePrivate
    """
    #  QCommonStylePrivate::QCommonStylePrivate()
    self._noteCreation(QCommonStylePrivate, lambda: Rituals.call(
        'ritual_ZN19QCommonStylePrivateC1Ev',
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

  def q_func(self) -> Optional[QCommonStyle]:
    """
    Calls Qt's 'QCommonStyle *QCommonStylePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyleprivate.html#q_func

    Returns
    -------

    Optional[QCommonStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCommonStyle *QCommonStylePrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QCommonStylePrivate6q_funcEv')
    from . import QCommonStyle
    return QCommonStyle._cuteAt(address)

  @overload(QPainter, QStyleOptionViewItem, QRect)
  @overload(QPainter, NoneType, QRect)
  @overload(NoneType, QStyleOptionViewItem, QRect)
  @overload(NoneType, NoneType, QRect)
  def viewItemDrawText(
      self,
      p: Optional[QPainter],
      option: Optional[QStyleOptionViewItem],
      rect: QRect,
  ) -> None:
    """
    Calls Qt's 'void QCommonStylePrivate::viewItemDrawText(QPainter *p, const
    QStyleOptionViewItem *option, const QRect &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#viewItemDrawText

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QCommonStylePrivate::viewItemDrawText(QPainter *p, const
    #      QStyleOptionViewItem *option, const QRect &rect) const
    self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate16viewItemDrawTextEP8QPainterPK20QS'
        'tyleOptionViewItemRK5QRect',
        self._addressOf(p), self._addressOf(option), self._valueOf(rect),
    )

  @overload(QStyleOptionViewItem, QRect, QRect, QRect, bool)
  @overload(QStyleOptionViewItem, QRect, QRect, NoneType, bool)
  @overload(QStyleOptionViewItem, QRect, NoneType, QRect, bool)
  @overload(QStyleOptionViewItem, QRect, NoneType, NoneType, bool)
  @overload(QStyleOptionViewItem, NoneType, QRect, QRect, bool)
  @overload(QStyleOptionViewItem, NoneType, QRect, NoneType, bool)
  @overload(QStyleOptionViewItem, NoneType, NoneType, QRect, bool)
  @overload(QStyleOptionViewItem, NoneType, NoneType, NoneType, bool)
  @overload(NoneType, QRect, QRect, QRect, bool)
  @overload(NoneType, QRect, QRect, NoneType, bool)
  @overload(NoneType, QRect, NoneType, QRect, bool)
  @overload(NoneType, QRect, NoneType, NoneType, bool)
  @overload(NoneType, NoneType, QRect, QRect, bool)
  @overload(NoneType, NoneType, QRect, NoneType, bool)
  @overload(NoneType, NoneType, NoneType, QRect, bool)
  @overload(NoneType, NoneType, NoneType, NoneType, bool)
  def viewItemLayout(
      self,
      opt: Optional[QStyleOptionViewItem],
      checkRect: Optional[QRect],
      pixmapRect: Optional[QRect],
      textRect: Optional[QRect],
      sizehint: bool,
  ) -> None:
    """
    Calls Qt's 'void QCommonStylePrivate::viewItemLayout(const
    QStyleOptionViewItem *opt, QRect *checkRect, QRect *pixmapRect, QRect
    *textRect, bool sizehint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#viewItemLayout

    Parameters
    ----------

    opt : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    checkRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pixmapRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    textRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sizehint : bool
      Passed on as it is.
    """
    #  void QCommonStylePrivate::viewItemLayout(const QStyleOptionViewItem
    #      *opt, QRect *checkRect, QRect *pixmapRect, QRect *textRect, bool
    #      sizehint) const
    self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate14viewItemLayoutEPK20QStyleOptionVi'
        'ewItemP5QRectS4_S4_b',
        self._addressOf(opt), self._addressOf(checkRect),
        self._addressOf(pixmapRect), self._addressOf(textRect), sizehint,
    )

  @overload(QStyleOptionTab, QWidget, QRect, QRect)
  @overload(QStyleOptionTab, QWidget, QRect, NoneType)
  @overload(QStyleOptionTab, QWidget, NoneType, QRect)
  @overload(QStyleOptionTab, QWidget, NoneType, NoneType)
  @overload(QStyleOptionTab, NoneType, QRect, QRect)
  @overload(QStyleOptionTab, NoneType, QRect, NoneType)
  @overload(QStyleOptionTab, NoneType, NoneType, QRect)
  @overload(QStyleOptionTab, NoneType, NoneType, NoneType)
  @overload(NoneType, QWidget, QRect, QRect)
  @overload(NoneType, QWidget, QRect, NoneType)
  @overload(NoneType, QWidget, NoneType, QRect)
  @overload(NoneType, QWidget, NoneType, NoneType)
  @overload(NoneType, NoneType, QRect, QRect)
  @overload(NoneType, NoneType, QRect, NoneType)
  @overload(NoneType, NoneType, NoneType, QRect)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def tabLayout(
      self,
      opt: Optional[QStyleOptionTab],
      widget: Optional[QWidget],
      textRect: Optional[QRect],
      pixmapRect: Optional[QRect],
  ) -> None:
    """
    Calls Qt's 'void QCommonStylePrivate::tabLayout(const QStyleOptionTab
    *opt, const QWidget *widget, QRect *textRect, QRect *pixmapRect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyleprivate.html#tabLayout

    Parameters
    ----------

    opt : Optional[QStyleOptionTab]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    textRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pixmapRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt, const
    #      QWidget *widget, QRect *textRect, QRect *pixmapRect) const
    ritual = (
        'ritual_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTabPK7QW'
        'idgetP5QRectS7_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTa'
          'bPK7QWidgetP5QRectS7_')
    self.uglySide.call(
        ritual,
        self._addressOf(opt), self._addressOf(widget),
        self._addressOf(textRect), self._addressOf(pixmapRect),
    )

  @overload(QStyleAnimation)
  @overload(NoneType)
  def startAnimation(self, animation: Optional[QStyleAnimation]) -> None:
    """
    Calls Qt's 'void QCommonStylePrivate::startAnimation(QStyleAnimation
    *animation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#startAnimation

    Parameters
    ----------

    animation : Optional[QStyleAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStylePrivate::startAnimation(QStyleAnimation *animation)
    #      const
    self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate14startAnimationEP15QStyleAnimation',
        self._addressOf(animation),
    )

  @overload(QObject)
  @overload(NoneType)
  def stopAnimation(self, target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QCommonStylePrivate::stopAnimation(const QObject
    *target) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#stopAnimation

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStylePrivate::stopAnimation(const QObject *target) const
    self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate13stopAnimationEPK7QObject',
        self._addressOf(target, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def removeAnimation(self, target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QCommonStylePrivate::removeAnimation(const QObject
    *target) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyleprivate.html#removeAnimation

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStylePrivate::removeAnimation(const QObject *target) const
    self.uglySide.call(
        'ritual_ZNK19QCommonStylePrivate15removeAnimationEPK7QObject',
        self._addressOf(target, 'QObject'),
    )

  @staticmethod
  def iconFromApplicationTheme(*__, **_) -> Never:
    """
    Qt's 'QIcon QCommonStylePrivate::iconFromApplicationTheme(QCommonStyle::
    StandardPixmap standardIcon, const QStyleOption *option, const QWidget
    *widget) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCommonStylePrivate.iconFromApplicationTheme' has no cute "
        "function yet. Qt's 'QIcon "
        "QCommonStylePrivate::iconFromApplicationTheme(QCommonStyle::Standar"
        "dPixmap standardIcon, const QStyleOption *option, const QWidget "
        "*widget) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def iconFromMacTheme(*__, **_) -> Never:
    """
    Qt's 'QIcon
    QCommonStylePrivate::iconFromMacTheme(QCommonStyle::StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCommonStylePrivate.iconFromMacTheme' has no cute function yet. "
        "Qt's 'QIcon "
        "QCommonStylePrivate::iconFromMacTheme(QCommonStyle::StandardPixmap "
        "standardIcon, const QStyleOption *option, const QWidget *widget) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def iconFromResourceTheme(*__, **_) -> Never:
    """
    Qt's 'QIcon
    QCommonStylePrivate::iconFromResourceTheme(QCommonStyle::StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCommonStylePrivate.iconFromResourceTheme' has no cute function "
        "yet. Qt's 'QIcon "
        "QCommonStylePrivate::iconFromResourceTheme(QCommonStyle::StandardPi"
        "xmap standardIcon, const QStyleOption *option, const QWidget "
        "*widget) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def iconFromWindowsTheme(*__, **_) -> Never:
    """
    Qt's 'QIcon
    QCommonStylePrivate::iconFromWindowsTheme(QCommonStyle::StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCommonStylePrivate.iconFromWindowsTheme' has no cute function "
        "yet. Qt's 'QIcon "
        "QCommonStylePrivate::iconFromWindowsTheme(QCommonStyle::StandardPix"
        "map standardIcon, const QStyleOption *option, const QWidget "
        "*widget) const': takes a type Python has no way to hand over yet.")
