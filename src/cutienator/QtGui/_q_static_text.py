"""
QStaticText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qstatictext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSizeF
  from . import QFont, QTextOption, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QTextOption = WAIT['QTextOption']
  QTransform = WAIT['QTransform']


class QStaticText(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStaticText: a plain Python object standing in front
  of one C++ QStaticText.

  C++ hands a QStaticText around as a copy, so every C++ QStaticText behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStaticText that has a ritual and that Python can
  call so far, 15 names in all: 'setText', 'text', 'setTextFormat',
  'textFormat', 'setTextWidth', 'textWidth', 'setTextOption', 'textOption',
  'size', 'prepare', 'setPerformanceHint', 'performanceHint', '__eq__',
  '__ne__', 'detach'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStaticText::~QStaticText()': the destructor: Python removes its
    C++ QStaticText by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStaticText is created at the first use, not by
    'QStaticText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStaticText back gives a copy the ritual made for
    Python, in a new cute QStaticText.
  """

  #  The enums Qt writes inside QStaticText, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PerformanceHint(CuteNum):
    """
    The enum 'QStaticText::PerformanceHint' of Qt, with the 2 names Qt gives
    in it.
    """

    ModerateCaching = Kee[int](0)
    AggressiveCaching = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStaticText'

  #  Qt's '~QStaticText()'. Naming it makes this a value class: Python owns
  #  every C++ QStaticText behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QStaticTextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString QStaticText::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStaticText::text() const
    return self.uglySide.call('ritual_ZNK11QStaticText4textEv')

  def textFormat(self) -> Qt.TextFormat:
    """
    Calls Qt's 'Qt::TextFormat QStaticText::textFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#textFormat

    Returns
    -------

    Qt.TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextFormat(number)'
      gives.
    """
    #  Qt::TextFormat QStaticText::textFormat() const
    return Qt.TextFormat(self.uglySide.call(
        'ritual_ZNK11QStaticText10textFormatEv',
    ))

  def textWidth(self) -> float:
    """
    Calls Qt's 'qreal QStaticText::textWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#textWidth
    """
    #  qreal QStaticText::textWidth() const
    return self.uglySide.call('ritual_ZNK11QStaticText9textWidthEv')

  def textOption(self) -> QTextOption:
    """
    Calls Qt's 'QTextOption QStaticText::textOption() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#textOption

    Returns
    -------

    QTextOption
      A new cute QTextOption around the copy Qt gave back. Python owns it.
    """
    #  QTextOption QStaticText::textOption() const
    address = self.uglySide.call('ritual_ZNK11QStaticText10textOptionEv')
    from . import QTextOption
    return QTextOption._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QStaticText::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QStaticText::size() const
    address = self.uglySide.call('ritual_ZNK11QStaticText4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def performanceHint(self) -> PerformanceHint:
    """
    Calls Qt's 'PerformanceHint QStaticText::performanceHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#performanceHint

    Returns
    -------

    PerformanceHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PerformanceHint(number)'
      gives.
    """
    #  PerformanceHint QStaticText::performanceHint() const
    return QStaticText.PerformanceHint(self.uglySide.call(
        'ritual_ZNK11QStaticText15performanceHintEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QStaticText::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStaticText::setText(const QString &text)
    self.uglySide.call('ritual_ZN11QStaticText7setTextERK7QString', text)

  @overload(Qt.TextFormat)
  def setTextFormat(self, textFormat: Qt.TextFormat) -> None:
    """
    Calls Qt's 'void QStaticText::setTextFormat(Qt::TextFormat textFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#setTextFormat

    Parameters
    ----------

    textFormat : Qt.TextFormat
      Passed on as its number.
    """
    #  void QStaticText::setTextFormat(Qt::TextFormat textFormat)
    self.uglySide.call(
        'ritual_ZN11QStaticText13setTextFormatEN2Qt10TextFormatE',
        textFormat.value,
    )

  @overload(float)
  def setTextWidth(self, textWidth: float) -> None:
    """
    Calls Qt's 'void QStaticText::setTextWidth(qreal textWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#setTextWidth

    Parameters
    ----------

    textWidth : float
      Passed on as it is.
    """
    #  void QStaticText::setTextWidth(qreal textWidth)
    self.uglySide.call('ritual_ZN11QStaticText12setTextWidthEd', textWidth)

  @overload(QTextOption)
  def setTextOption(self, textOption: QTextOption) -> None:
    """
    Calls Qt's 'void QStaticText::setTextOption(const QTextOption
    &textOption)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#setTextOption

    Parameters
    ----------

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.
    """
    #  void QStaticText::setTextOption(const QTextOption &textOption)
    self.uglySide.call(
        'ritual_ZN11QStaticText13setTextOptionERK11QTextOption',
        self._valueOf(textOption),
    )

  @overload(PerformanceHint)
  def setPerformanceHint(self, performanceHint: PerformanceHint) -> None:
    """
    Calls Qt's 'void QStaticText::setPerformanceHint(PerformanceHint
    performanceHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatictext.html#setPerformanceHint

    Parameters
    ----------

    performanceHint : PerformanceHint
      Passed on as its number.
    """
    #  void QStaticText::setPerformanceHint(PerformanceHint performanceHint)
    self.uglySide.call(
        'ritual_ZN11QStaticText18setPerformanceHintENS_15PerformanceHintE',
        performanceHint.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QStaticText) -> bool:
    """
    Calls Qt's 'bool QStaticText::operator==(const QStaticText &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#operator==

    Parameters
    ----------

    a0 : QStaticText
      Passed on as a value: Qt reads the C++ QStaticText, which stays
      Python's own.
    """
    #  bool QStaticText::operator==(const QStaticText &a0) const
    return self.uglySide.call(
        'ritual_ZNK11QStaticTexteqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, a0: QStaticText) -> bool:
    """
    Calls Qt's 'bool QStaticText::operator!=(const QStaticText &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#operator!=

    Parameters
    ----------

    a0 : QStaticText
      Passed on as a value: Qt reads the C++ QStaticText, which stays
      Python's own.
    """
    #  bool QStaticText::operator!=(const QStaticText &a0) const
    return self.uglySide.call(
        'ritual_ZNK11QStaticTextneERKS_', self._valueOf(a0),
    )

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
    Notes what was given, for Qt's 'QStaticText::QStaticText()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#QStaticText
    """
    #  QStaticText::QStaticText()
    self._noteCreation(QStaticText, lambda: Rituals.call(
        'ritual_ZN11QStaticTextC1Ev',
    ))

  @overload(str)
  def __init__(self, text: str) -> None:
    """
    Notes what was given, for Qt's 'QStaticText::QStaticText(const QString
    &text)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#QStaticText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QStaticText::QStaticText(const QString &text)
    self._noteCreation(QStaticText, lambda: Rituals.call(
        'ritual_ZN11QStaticTextC1ERK7QString', text,
    ))

  @overload(THIS)
  def __init__(self, other: QStaticText) -> None:
    """
    Notes what was given, for Qt's 'QStaticText::QStaticText(const
    QStaticText &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#QStaticText

    Parameters
    ----------

    other : QStaticText
      Passed on as a value: Qt reads the C++ QStaticText, which stays
      Python's own.
    """
    #  QStaticText::QStaticText(const QStaticText &other)
    self._noteCreation(QStaticText, lambda: Rituals.call(
        'ritual_ZN11QStaticTextC1ERKS_', self._valueOf(other),
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

  @overload()
  @overload(QTransform)
  @overload(QTransform, QFont)
  def prepare(
      self,
      matrix: Optional[QTransform] = None,
      font: Optional[QFont] = None,
  ) -> None:
    """
    Calls Qt's 'void QStaticText::prepare(const QTransform &matrix, const
    QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#prepare

    Parameters
    ----------

    matrix : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    font : Optional[QFont]
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
      May be left out, as in Qt: a new 'QFont()' is then passed on.
    """
    #  void QStaticText::prepare(const QTransform &matrix, const QFont &font)
    if matrix is None:
      from . import QTransform
      matrix = QTransform()
    if font is None:
      from . import QFont
      font = QFont()
    self.uglySide.call(
        'ritual_ZN11QStaticText7prepareERK10QTransformRK5QFont',
        self._valueOf(matrix), self._valueOf(font),
    )

  def detach(self) -> None:
    """
    Calls Qt's 'void QStaticText::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictext.html#detach
    """
    #  void QStaticText::detach()
    self.uglySide.call('ritual_ZN11QStaticText6detachEv')
