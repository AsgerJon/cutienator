"""
QQC2::QCommonStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qcommonstyle_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QCommonStylePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt
from . import QQC2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRect
  from ..QtGui import QFont, QTextOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QTextOption = WAIT['QTextOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCommonStylePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QCommonStylePrivate: a plain Python object
  standing in front of one C++ QQC2::QCommonStylePrivate.

  What exists
  -----------

  Every function of Qt's QQC2::QCommonStylePrivate that has a ritual and that
  Python can call so far, 5 names in all: 'calculateElidedText',
  'viewItemLayout', 'isViewItemCached', 'toolButtonElideText', 'tabLayout'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCommonStyle *QQC2::QCommonStylePrivate::q_func()': gives
    'QQC2::QCommonStyle', which has no cute class yet.
  - Qt's 'const QCommonStyle *QQC2::QCommonStylePrivate::q_func() const':
    gives 'QQC2::QCommonStyle', which has no cute class yet.
  - Qt's 'QQC2::QCommonStylePrivate::~QCommonStylePrivate()': the destructor:
    Python never removes a C++ QQC2::QCommonStylePrivate.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQC2::QCommonStylePrivate is created at the first use, not by
    'QQC2::QCommonStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQC2::QCommonStylePrivate.
  - Each name of Qt's QQC2::QCommonStylePrivate that has no cute function
    yet, 'viewItemDrawText', 'viewItemSize', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QCommonStylePrivate'

  #  A C++ QQC2::QCommonStylePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQC2_QCommonStylePrivate'

  #  The functions Qt calls itself that QQC2::QCommonStylePrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'tabLayout': (
          ('_ZNK4QQC219QCommonStylePrivate9tabLayoutEPKNS_15QStyleOptionTab'
           'EP5QRectS5_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionTab'),
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
    Calls Qt's 'QString QQC2::QCommonStylePrivate::calculateElidedText(const
    QString &text, const QTextOption &textOption, const QFont &font, const
    QRect &textRect, const Qt::Alignment valign, Qt::TextElideMode
    textElideMode, int flags, bool lastVisibleLineShouldBeElided, QPointF
    *paintStartPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qcommonstyleprivate.html#calculateElidedText

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
    #  QString QQC2::QCommonStylePrivate::calculateElidedText(const QString
    #      &text, const QTextOption &textOption, const QFont &font, const
    #      QRect &textRect, const Qt::Alignment valign, Qt::TextElideMode
    #      textElideMode, int flags, bool lastVisibleLineShouldBeElided,
    #      QPointF *paintStartPosition) const
    return self.uglySide.call(
        'ritual_ZNK4QQC219QCommonStylePrivate19calculateElidedTextERK7QStri'
        'ngRK11QTextOptionRK5QFontRK5QRect6QFlagsIN2Qt13AlignmentFlagEENSE_'
        '13TextElideModeEibP7QPointF',
        text, self._valueOf(textOption), self._valueOf(font),
        self._valueOf(textRect), valign.value, textElideMode.value, flags,
        lastVisibleLineShouldBeElided, self._addressOf(paintStartPosition,
        'QPointF'),
    )

  @overload(WAIT['QQC2.QStyleOptionViewItem'])
  def isViewItemCached(self, option: QQC2.QStyleOptionViewItem) -> bool:
    """
    Calls Qt's 'bool QQC2::QCommonStylePrivate::isViewItemCached(const
    QStyleOptionViewItem &option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qcommonstyleprivate.html#isViewItemCached

    Parameters
    ----------

    option : QQC2.QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionViewItem,
      which stays Python's own.
    """
    #  bool QQC2::QCommonStylePrivate::isViewItemCached(const
    #      QStyleOptionViewItem &option) const
    return self.uglySide.call(
        'ritual_ZNK4QQC219QCommonStylePrivate16isViewItemCachedERKNS_20QSty'
        'leOptionViewItemE',
        self._valueOf(option),
    )

  @overload(WAIT['QQC2.QStyleOptionToolButton'], QRect, int)
  @overload(NoneType, QRect, int)
  def toolButtonElideText(
      self,
      toolbutton: Optional[QQC2.QStyleOptionToolButton],
      textRect: QRect,
      flags: int,
  ) -> str:
    """
    Calls Qt's 'QString QQC2::QCommonStylePrivate::toolButtonElideText(const
    QStyleOptionToolButton *toolbutton, const QRect &textRect, int flags)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qcommonstyleprivate.html#toolButtonElideText

    Parameters
    ----------

    toolbutton : Optional[QQC2.QStyleOptionToolButton]
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
    #  QString QQC2::QCommonStylePrivate::toolButtonElideText(const
    #      QStyleOptionToolButton *toolbutton, const QRect &textRect, int
    #      flags) const
    return self.uglySide.call(
        'ritual_ZNK4QQC219QCommonStylePrivate19toolButtonElideTextEPKNS_22Q'
        'StyleOptionToolButtonERK5QRecti',
        self._addressOf(toolbutton), self._valueOf(textRect), flags,
    )

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

  @overload(WAIT['QQC2.QStyleOptionViewItem'], QRect, QRect, QRect, bool)
  @overload(WAIT['QQC2.QStyleOptionViewItem'], QRect, QRect, NoneType, bool)
  @overload(WAIT['QQC2.QStyleOptionViewItem'], QRect, NoneType, QRect, bool)
  @overload(
      WAIT['QQC2.QStyleOptionViewItem'], QRect, NoneType, NoneType, bool,
  )
  @overload(WAIT['QQC2.QStyleOptionViewItem'], NoneType, QRect, QRect, bool)
  @overload(
      WAIT['QQC2.QStyleOptionViewItem'], NoneType, QRect, NoneType, bool,
  )
  @overload(
      WAIT['QQC2.QStyleOptionViewItem'], NoneType, NoneType, QRect, bool,
  )
  @overload(
      WAIT['QQC2.QStyleOptionViewItem'], NoneType, NoneType, NoneType, bool,
  )
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
      opt: Optional[QQC2.QStyleOptionViewItem],
      checkRect: Optional[QRect],
      pixmapRect: Optional[QRect],
      textRect: Optional[QRect],
      sizehint: bool,
  ) -> None:
    """
    Calls Qt's 'void QQC2::QCommonStylePrivate::viewItemLayout(const
    QStyleOptionViewItem *opt, QRect *checkRect, QRect *pixmapRect, QRect
    *textRect, bool sizehint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qcommonstyleprivate.html#viewItemLayout

    Parameters
    ----------

    opt : Optional[QQC2.QStyleOptionViewItem]
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
    #  void QQC2::QCommonStylePrivate::viewItemLayout(const
    #      QStyleOptionViewItem *opt, QRect *checkRect, QRect *pixmapRect,
    #      QRect *textRect, bool sizehint) const
    self.uglySide.call(
        'ritual_ZNK4QQC219QCommonStylePrivate14viewItemLayoutEPKNS_20QStyle'
        'OptionViewItemEP5QRectS5_S5_b',
        self._addressOf(opt), self._addressOf(checkRect),
        self._addressOf(pixmapRect), self._addressOf(textRect), sizehint,
    )

  @overload(WAIT['QQC2.QStyleOptionTab'], QRect, QRect)
  @overload(WAIT['QQC2.QStyleOptionTab'], QRect, NoneType)
  @overload(WAIT['QQC2.QStyleOptionTab'], NoneType, QRect)
  @overload(WAIT['QQC2.QStyleOptionTab'], NoneType, NoneType)
  @overload(NoneType, QRect, QRect)
  @overload(NoneType, QRect, NoneType)
  @overload(NoneType, NoneType, QRect)
  @overload(NoneType, NoneType, NoneType)
  def tabLayout(
      self,
      opt: Optional[QQC2.QStyleOptionTab],
      textRect: Optional[QRect],
      pixmapRect: Optional[QRect],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QCommonStylePrivate::tabLayout(const
    QStyleOptionTab *opt, QRect *textRect, QRect *pixmapRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qcommonstyleprivate.html#tabLayout

    Parameters
    ----------

    opt : Optional[QQC2.QStyleOptionTab]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    textRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pixmapRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt,
    #      QRect *textRect, QRect *pixmapRect) const
    ritual = (
        'ritual_ZNK4QQC219QCommonStylePrivate9tabLayoutEPKNS_15QStyleOption'
        'TabEP5QRectS5_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC219QCommonStylePrivate9tabLayoutEPKNS_15QStyle'
          'OptionTabEP5QRectS5_')
    self.uglySide.call(
        ritual,
        self._addressOf(opt), self._addressOf(textRect),
        self._addressOf(pixmapRect),
    )

  @staticmethod
  def viewItemDrawText(*__, **_) -> Never:
    """
    Qt's 'void QQC2::QCommonStylePrivate::viewItemDrawText(QPainter *p, const
    QStyleOptionViewItem *option, const QRect &rect) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'viewItemTextLayout'.
    """
    raise NotImplementedError(
        "'QQC2.QCommonStylePrivate.viewItemDrawText' has no cute function "
        "yet. Qt's 'void "
        "QQC2::QCommonStylePrivate::viewItemDrawText(QPainter *p, const "
        "QStyleOptionViewItem *option, const QRect &rect) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'viewItemTextLayout'.")

  @staticmethod
  def viewItemSize(*__, **_) -> Never:
    """
    Qt's 'QSize QQC2::QCommonStylePrivate::viewItemSize(const
    QStyleOptionViewItem *option, int role) const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'viewItemTextLayout'.
    """
    raise NotImplementedError(
        "'QQC2.QCommonStylePrivate.viewItemSize' has no cute function yet. "
        "Qt's 'QSize QQC2::QCommonStylePrivate::viewItemSize(const "
        "QStyleOptionViewItem *option, int role) const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'viewItemTextLayout'.")
