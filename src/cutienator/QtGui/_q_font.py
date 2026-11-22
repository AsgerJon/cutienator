"""
QFont binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QDebug
  from . import QPaintDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QPaintDevice = WAIT['QPaintDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFont(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFont: a plain Python object standing in front of one
  C++ QFont.

  C++ hands a QFont around as a copy, so every C++ QFont behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFont that has a ritual and that Python can call so
  far, 74 names in all: 'family', 'setFamily', 'styleName', 'setStyleName',
  'pointSize', 'setPointSize', 'pointSizeF', 'setPointSizeF', 'pixelSize',
  'setPixelSize', 'weight', 'setWeight', 'bold', 'setBold', 'setStyle',
  'style', 'italic', 'setItalic', 'underline', 'setUnderline', 'overline',
  'setOverline', 'strikeOut', 'setStrikeOut', 'fixedPitch', 'setFixedPitch',
  'kerning', 'setKerning', 'styleHint', 'styleStrategy', 'setStyleHint',
  'setStyleStrategy', 'stretch', 'setStretch', 'letterSpacing',
  'letterSpacingType', 'setLetterSpacing', 'wordSpacing', 'setWordSpacing',
  'setCapitalization', 'capitalization', 'setHintingPreference',
  'hintingPreference', 'setFeature', 'unsetFeature', 'featureValue',
  'isFeatureSet', 'clearFeatures', 'setVariableAxis', 'unsetVariableAxis',
  'isVariableAxisSet', 'variableAxisValue', 'clearVariableAxes',
  'exactMatch', '__eq__', '__ne__', '__lt__', 'isCopyOf', 'key', 'toString',
  'fromString', 'substitute', 'insertSubstitution', 'removeSubstitutions',
  'initialize', 'cleanup', 'cacheStatistics', 'defaultFamily', 'resolve',
  'resolveMask', 'setResolveMask', 'setLegacyWeight', 'legacyWeight',
  '__rlshift__'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFont::~QFont()': the destructor: Python removes its C++ QFont by
    it, and has no other use for it.
  - Qt's 'QVariant QFont::operator QVariant() const': an operator Python has
    no name for.

  What has no ritual
  ------------------

  19 of the 99 functions Qt declares: 14 takes or gives a type that cannot be
  passed yet; 3 private; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QFont is created at the first use, not by 'QFont(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFont back gives a copy the ritual made for Python,
    in a new cute QFont.
  """

  #  The enums Qt writes inside QFont, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Capitalization(CuteNum):
    """
    The enum 'QFont::Capitalization' of Qt, with the 5 names Qt gives in it.
    """

    MixedCase = Kee[int](0)
    AllUppercase = Kee[int](1)
    AllLowercase = Kee[int](2)
    SmallCaps = Kee[int](3)
    Capitalize = Kee[int](4)

  class HintingPreference(CuteNum):
    """
    The enum 'QFont::HintingPreference' of Qt, with the 4 names Qt gives in
    it.
    """

    PreferDefaultHinting = Kee[int](0)
    PreferNoHinting = Kee[int](1)
    PreferVerticalHinting = Kee[int](2)
    PreferFullHinting = Kee[int](3)

  class ResolveProperties(CuteNum):
    """
    The enum 'QFont::ResolveProperties' of Qt, with the 22 names Qt gives in
    it.
    """

    NoPropertiesResolved = Kee[int](0)
    FamilyResolved = Kee[int](1)
    SizeResolved = Kee[int](2)
    StyleHintResolved = Kee[int](4)
    StyleStrategyResolved = Kee[int](8)
    WeightResolved = Kee[int](16)
    StyleResolved = Kee[int](32)
    UnderlineResolved = Kee[int](64)
    OverlineResolved = Kee[int](128)
    StrikeOutResolved = Kee[int](256)
    FixedPitchResolved = Kee[int](512)
    StretchResolved = Kee[int](1024)
    KerningResolved = Kee[int](2048)
    CapitalizationResolved = Kee[int](4096)
    LetterSpacingResolved = Kee[int](8192)
    WordSpacingResolved = Kee[int](16384)
    HintingPreferenceResolved = Kee[int](32768)
    StyleNameResolved = Kee[int](65536)
    FamiliesResolved = Kee[int](131072)
    FeaturesResolved = Kee[int](262144)
    VariableAxesResolved = Kee[int](524288)
    AllPropertiesResolved = Kee[int](1048575)

  class SpacingType(CuteNum):
    """
    The enum 'QFont::SpacingType' of Qt, with the 2 names Qt gives in it.
    """

    PercentageSpacing = Kee[int](0)
    AbsoluteSpacing = Kee[int](1)

  class Stretch(CuteNum):
    """The enum 'QFont::Stretch' of Qt, with the 10 names Qt gives in it."""

    AnyStretch = Kee[int](0)
    UltraCondensed = Kee[int](50)
    ExtraCondensed = Kee[int](62)
    Condensed = Kee[int](75)
    SemiCondensed = Kee[int](87)
    Unstretched = Kee[int](100)
    SemiExpanded = Kee[int](112)
    Expanded = Kee[int](125)
    ExtraExpanded = Kee[int](150)
    UltraExpanded = Kee[int](200)

  class Style(CuteNum):
    """The enum 'QFont::Style' of Qt, with the 3 names Qt gives in it."""

    StyleNormal = Kee[int](0)
    StyleItalic = Kee[int](1)
    StyleOblique = Kee[int](2)

  class StyleHint(CuteNum):
    """
    The enum 'QFont::StyleHint' of Qt, with the 13 names Qt gives in it.
    """

    Helvetica = Kee[int](0)
    SansSerif = Kee[int](0)
    Times = Kee[int](1)
    Serif = Kee[int](1)
    Courier = Kee[int](2)
    TypeWriter = Kee[int](2)
    OldEnglish = Kee[int](3)
    Decorative = Kee[int](3)
    System = Kee[int](4)
    AnyStyle = Kee[int](5)
    Cursive = Kee[int](6)
    Monospace = Kee[int](7)
    Fantasy = Kee[int](8)

  class StyleStrategy(CuteNum):
    """
    The enum 'QFont::StyleStrategy' of Qt, with the 14 names Qt gives in it.
    """

    PreferDefault = Kee[int](1)
    PreferBitmap = Kee[int](2)
    PreferDevice = Kee[int](4)
    PreferOutline = Kee[int](8)
    ForceOutline = Kee[int](16)
    PreferMatch = Kee[int](32)
    PreferQuality = Kee[int](64)
    PreferAntialias = Kee[int](128)
    NoAntialias = Kee[int](256)
    NoSubpixelAntialias = Kee[int](2048)
    PreferNoShaping = Kee[int](4096)
    ContextFontMerging = Kee[int](8192)
    PreferTypoLineMetrics = Kee[int](16384)
    NoFontMerging = Kee[int](32768)

  class Weight(CuteNum):
    """The enum 'QFont::Weight' of Qt, with the 9 names Qt gives in it."""

    Thin = Kee[int](100)
    ExtraLight = Kee[int](200)
    Light = Kee[int](300)
    Normal = Kee[int](400)
    Medium = Kee[int](500)
    DemiBold = Kee[int](600)
    Bold = Kee[int](700)
    ExtraBold = Kee[int](800)
    Black = Kee[int](900)

  #  The classes Qt writes inside QFont, each a class in here as in C++.

  class Tag(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFont::Tag: a plain Python object standing in front
    of one C++ QFont::Tag.

    C++ hands a QFont::Tag around as a copy, so every C++ QFont::Tag behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QFont::Tag that has a ritual and that Python can
    call so far, 10 names in all: 'isValid', 'value', 'toString',
    '__rlshift__', '__eq__', '__ne__', '__lt__', '__gt__', '__le__',
    '__ge__'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFont::Tag::~Tag()': the destructor: Python removes its C++
      QFont::Tag by it, and has no other use for it.

    What has no ritual
    ------------------

    5 of the 17 functions Qt declares: 4 takes or gives a type that cannot be
    passed yet; 1 a template.

    What to expect
    --------------

    - The C++ QFont::Tag is created at the first use, not by
      'QFont::Tag(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFont::Tag back gives a copy the ritual made for
      Python, in a new cute QFont::Tag.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDebug = WAIT['QDebug']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFont::Tag'

    #  Qt's '~QFont::Tag()'. Naming it makes this a value class: Python owns
    #  every C++ QFont::Tag behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN5QFont3TagD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QFont::Tag::isValid() const'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#isValid
      """
      #  bool QFont::Tag::isValid() const
      return self.uglySide.call('ritual_ZNK5QFont3Tag7isValidEv')

    def value(self) -> int:
      """
      Calls Qt's 'quint32 QFont::Tag::value() const'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#value
      """
      #  quint32 QFont::Tag::value() const
      return self.uglySide.call('ritual_ZNK5QFont3Tag5valueEv')

    def toString(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QFont::Tag::toString() const'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#toString

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QFont::Tag::toString() const
      address = self.uglySide.call('ritual_ZNK5QFont3Tag8toStringEv')
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QDebug)
    def __rlshift__(self, debug: QDebug) -> QDebug:
      """
      Calls Qt's 'QDebug operator<<(QDebug debug, Tag tag)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator<<

      Parameters
      ----------

      debug : QDebug
        Passed on as a value: Qt reads the C++ QDebug, which stays Python's
        own.

      Returns
      -------

      QDebug
        A new cute QDebug around the copy Qt gave back. Python owns it.
      """
      #  QDebug operator<<(QDebug debug, Tag tag)
      address = Rituals.call(
          'ritual_Zls6QDebugN5QFont3TagE',
          CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
      )
      from ..QtCore import QDebug
      return QDebug._cuteOwning(address)

    @overload.fallback
    def __rlshift__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __eq__(self, rhs: QFont.Tag) -> bool:
      """
      Calls Qt's 'bool operator==(const QFont::Tag &lhs, const QFont::Tag
      &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator==

      Parameters
      ----------

      rhs : QFont.Tag
        Passed on as a value: Qt reads the C++ QFont::Tag, which stays
        Python's own.
      """
      #  bool operator==(const QFont::Tag &lhs, const QFont::Tag &rhs)
      return Rituals.call(
          'ritual_ZeqRKN5QFont3TagES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    def __ne__(self, rhs: QFont.Tag) -> bool:
      """
      Calls Qt's 'bool operator!=(const QFont::Tag &lhs, const QFont::Tag
      &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator!=

      Parameters
      ----------

      rhs : QFont.Tag
        Passed on as a value: Qt reads the C++ QFont::Tag, which stays
        Python's own.
      """
      #  bool operator!=(const QFont::Tag &lhs, const QFont::Tag &rhs)
      return Rituals.call(
          'ritual_ZneRKN5QFont3TagES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __lt__(self, rhs: QFont.Tag) -> bool:
      """
      Calls Qt's 'bool operator<(const QFont::Tag &lhs, const QFont::Tag
      &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator<

      Parameters
      ----------

      rhs : QFont.Tag
        Passed on as a value: Qt reads the C++ QFont::Tag, which stays
        Python's own.
      """
      #  bool operator<(const QFont::Tag &lhs, const QFont::Tag &rhs)
      return Rituals.call(
          'ritual_ZltRKN5QFont3TagES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __gt__(self, rhs: QFont.Tag) -> bool:
      """
      Calls Qt's 'bool operator>(const QFont::Tag &lhs, const QFont::Tag
      &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator>

      Parameters
      ----------

      rhs : QFont.Tag
        Passed on as a value: Qt reads the C++ QFont::Tag, which stays
        Python's own.
      """
      #  bool operator>(const QFont::Tag &lhs, const QFont::Tag &rhs)
      return Rituals.call(
          'ritual_ZgtRKN5QFont3TagES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __gt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __le__(self, rhs: QFont.Tag) -> bool:
      """
      Calls Qt's 'bool operator<=(const QFont::Tag &lhs, const QFont::Tag
      &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator<=

      Parameters
      ----------

      rhs : QFont.Tag
        Passed on as a value: Qt reads the C++ QFont::Tag, which stays
        Python's own.
      """
      #  bool operator<=(const QFont::Tag &lhs, const QFont::Tag &rhs)
      return Rituals.call(
          'ritual_ZleRKN5QFont3TagES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __le__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __ge__(self, rhs: QFont.Tag) -> bool:
      """
      Calls Qt's 'bool operator>=(const QFont::Tag &lhs, const QFont::Tag
      &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#operator>=

      Parameters
      ----------

      rhs : QFont.Tag
        Passed on as a value: Qt reads the C++ QFont::Tag, which stays
        Python's own.
      """
      #  bool operator>=(const QFont::Tag &lhs, const QFont::Tag &rhs)
      return Rituals.call(
          'ritual_ZgeRKN5QFont3TagES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __ge__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QFont::Tag::Tag()', which is called at
      the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#Tag
      """
      #  QFont::Tag::Tag()
      self._noteCreation(QFont.Tag, lambda: Rituals.call(
          'ritual_ZN5QFont3TagC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def substitute(a0: str) -> str:
    """
    Calls Qt's 'QString QFont::substitute(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#substitute

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFont::substitute(const QString &a0)
    return Rituals.call('ritual_ZN5QFont10substituteERK7QString', a0)

  @staticmethod
  @overload(str, str)
  def insertSubstitution(a0: str, a1: str) -> None:
    """
    Calls Qt's 'void QFont::insertSubstitution(const QString &a0, const
    QString &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#insertSubstitution

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFont::insertSubstitution(const QString &a0, const QString &a1)
    Rituals.call('ritual_ZN5QFont18insertSubstitutionERK7QStringS2_', a0, a1)

  @staticmethod
  @overload(str)
  def removeSubstitutions(a0: str) -> None:
    """
    Calls Qt's 'void QFont::removeSubstitutions(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#removeSubstitutions

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFont::removeSubstitutions(const QString &a0)
    Rituals.call('ritual_ZN5QFont19removeSubstitutionsERK7QString', a0)

  @staticmethod
  def initialize() -> None:
    """
    Calls Qt's 'void QFont::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#initialize
    """
    #  void QFont::initialize()
    Rituals.call('ritual_ZN5QFont10initializeEv')

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QFont::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#cleanup
    """
    #  void QFont::cleanup()
    Rituals.call('ritual_ZN5QFont7cleanupEv')

  @staticmethod
  def cacheStatistics() -> None:
    """
    Calls Qt's 'void QFont::cacheStatistics()'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#cacheStatistics
    """
    #  void QFont::cacheStatistics()
    Rituals.call('ritual_ZN5QFont15cacheStatisticsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFont'

  #  Qt's '~QFont()'. Naming it makes this a value class: Python owns every
  #  C++ QFont behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QFontD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def family(self) -> str:
    """
    Calls Qt's 'QString QFont::family() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#family

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFont::family() const
    return self.uglySide.call('ritual_ZNK5QFont6familyEv')

  def styleName(self) -> str:
    """
    Calls Qt's 'QString QFont::styleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFont::styleName() const
    return self.uglySide.call('ritual_ZNK5QFont9styleNameEv')

  def pointSize(self) -> int:
    """
    Calls Qt's 'int QFont::pointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#pointSize
    """
    #  int QFont::pointSize() const
    return self.uglySide.call('ritual_ZNK5QFont9pointSizeEv')

  def pointSizeF(self) -> float:
    """
    Calls Qt's 'qreal QFont::pointSizeF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#pointSizeF
    """
    #  qreal QFont::pointSizeF() const
    return self.uglySide.call('ritual_ZNK5QFont10pointSizeFEv')

  def pixelSize(self) -> int:
    """
    Calls Qt's 'int QFont::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#pixelSize
    """
    #  int QFont::pixelSize() const
    return self.uglySide.call('ritual_ZNK5QFont9pixelSizeEv')

  def weight(self) -> Weight:
    """
    Calls Qt's 'Weight QFont::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#weight

    Returns
    -------

    Weight
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Weight(number)' gives.
    """
    #  Weight QFont::weight() const
    return QFont.Weight(self.uglySide.call('ritual_ZNK5QFont6weightEv'))

  def bold(self) -> bool:
    """
    Calls Qt's 'bool QFont::bold() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#bold
    """
    #  bool QFont::bold() const
    return self.uglySide.call('ritual_ZNK5QFont4boldEv')

  def style(self) -> Style:
    """
    Calls Qt's 'Style QFont::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#style

    Returns
    -------

    Style
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Style(number)' gives.
    """
    #  Style QFont::style() const
    return QFont.Style(self.uglySide.call('ritual_ZNK5QFont5styleEv'))

  def italic(self) -> bool:
    """
    Calls Qt's 'bool QFont::italic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#italic
    """
    #  bool QFont::italic() const
    return self.uglySide.call('ritual_ZNK5QFont6italicEv')

  def underline(self) -> bool:
    """
    Calls Qt's 'bool QFont::underline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#underline
    """
    #  bool QFont::underline() const
    return self.uglySide.call('ritual_ZNK5QFont9underlineEv')

  def overline(self) -> bool:
    """
    Calls Qt's 'bool QFont::overline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#overline
    """
    #  bool QFont::overline() const
    return self.uglySide.call('ritual_ZNK5QFont8overlineEv')

  def strikeOut(self) -> bool:
    """
    Calls Qt's 'bool QFont::strikeOut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#strikeOut
    """
    #  bool QFont::strikeOut() const
    return self.uglySide.call('ritual_ZNK5QFont9strikeOutEv')

  def fixedPitch(self) -> bool:
    """
    Calls Qt's 'bool QFont::fixedPitch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#fixedPitch
    """
    #  bool QFont::fixedPitch() const
    return self.uglySide.call('ritual_ZNK5QFont10fixedPitchEv')

  def kerning(self) -> bool:
    """
    Calls Qt's 'bool QFont::kerning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#kerning
    """
    #  bool QFont::kerning() const
    return self.uglySide.call('ritual_ZNK5QFont7kerningEv')

  def styleHint(self) -> StyleHint:
    """
    Calls Qt's 'StyleHint QFont::styleHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#styleHint

    Returns
    -------

    StyleHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StyleHint(number)' gives.
    """
    #  StyleHint QFont::styleHint() const
    return QFont.StyleHint(self.uglySide.call(
        'ritual_ZNK5QFont9styleHintEv',
    ))

  def styleStrategy(self) -> StyleStrategy:
    """
    Calls Qt's 'StyleStrategy QFont::styleStrategy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#styleStrategy

    Returns
    -------

    StyleStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StyleStrategy(number)'
      gives.
    """
    #  StyleStrategy QFont::styleStrategy() const
    return QFont.StyleStrategy(self.uglySide.call(
        'ritual_ZNK5QFont13styleStrategyEv',
    ))

  def stretch(self) -> int:
    """
    Calls Qt's 'int QFont::stretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#stretch
    """
    #  int QFont::stretch() const
    return self.uglySide.call('ritual_ZNK5QFont7stretchEv')

  def letterSpacing(self) -> float:
    """
    Calls Qt's 'qreal QFont::letterSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#letterSpacing
    """
    #  qreal QFont::letterSpacing() const
    return self.uglySide.call('ritual_ZNK5QFont13letterSpacingEv')

  def letterSpacingType(self) -> SpacingType:
    """
    Calls Qt's 'SpacingType QFont::letterSpacingType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#letterSpacingType

    Returns
    -------

    SpacingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SpacingType(number)'
      gives.
    """
    #  SpacingType QFont::letterSpacingType() const
    return QFont.SpacingType(self.uglySide.call(
        'ritual_ZNK5QFont17letterSpacingTypeEv',
    ))

  def wordSpacing(self) -> float:
    """
    Calls Qt's 'qreal QFont::wordSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#wordSpacing
    """
    #  qreal QFont::wordSpacing() const
    return self.uglySide.call('ritual_ZNK5QFont11wordSpacingEv')

  def capitalization(self) -> Capitalization:
    """
    Calls Qt's 'Capitalization QFont::capitalization() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#capitalization

    Returns
    -------

    Capitalization
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Capitalization(number)'
      gives.
    """
    #  Capitalization QFont::capitalization() const
    return QFont.Capitalization(self.uglySide.call(
        'ritual_ZNK5QFont14capitalizationEv',
    ))

  def hintingPreference(self) -> HintingPreference:
    """
    Calls Qt's 'HintingPreference QFont::hintingPreference() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#hintingPreference

    Returns
    -------

    HintingPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'HintingPreference(number)' gives.
    """
    #  HintingPreference QFont::hintingPreference() const
    return QFont.HintingPreference(self.uglySide.call(
        'ritual_ZNK5QFont17hintingPreferenceEv',
    ))

  @overload(Tag)
  def featureValue(self, tag: Tag) -> int:
    """
    Calls Qt's 'quint32 QFont::featureValue(Tag tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#featureValue

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  quint32 QFont::featureValue(Tag tag) const
    return self.uglySide.call(
        'ritual_ZNK5QFont12featureValueENS_3TagE', self._valueOf(tag),
    )

  @overload(Tag)
  def isFeatureSet(self, tag: Tag) -> bool:
    """
    Calls Qt's 'bool QFont::isFeatureSet(Tag tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#isFeatureSet

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  bool QFont::isFeatureSet(Tag tag) const
    return self.uglySide.call(
        'ritual_ZNK5QFont12isFeatureSetENS_3TagE', self._valueOf(tag),
    )

  @overload(Tag)
  def isVariableAxisSet(self, tag: Tag) -> bool:
    """
    Calls Qt's 'bool QFont::isVariableAxisSet(Tag tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#isVariableAxisSet

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  bool QFont::isVariableAxisSet(Tag tag) const
    return self.uglySide.call(
        'ritual_ZNK5QFont17isVariableAxisSetENS_3TagE', self._valueOf(tag),
    )

  @overload(Tag)
  def variableAxisValue(self, tag: Tag) -> float:
    """
    Calls Qt's 'float QFont::variableAxisValue(Tag tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#variableAxisValue

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  float QFont::variableAxisValue(Tag tag) const
    return self.uglySide.call(
        'ritual_ZNK5QFont17variableAxisValueENS_3TagE', self._valueOf(tag),
    )

  def exactMatch(self) -> bool:
    """
    Calls Qt's 'bool QFont::exactMatch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#exactMatch
    """
    #  bool QFont::exactMatch() const
    return self.uglySide.call('ritual_ZNK5QFont10exactMatchEv')

  @overload(THIS)
  def isCopyOf(self, a0: QFont) -> bool:
    """
    Calls Qt's 'bool QFont::isCopyOf(const QFont &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#isCopyOf

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  bool QFont::isCopyOf(const QFont &a0) const
    return self.uglySide.call(
        'ritual_ZNK5QFont8isCopyOfERKS_', self._valueOf(a0),
    )

  def key(self) -> str:
    """
    Calls Qt's 'QString QFont::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFont::key() const
    return self.uglySide.call('ritual_ZNK5QFont3keyEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QFont::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFont::toString() const
    return self.uglySide.call('ritual_ZNK5QFont8toStringEv')

  def defaultFamily(self) -> str:
    """
    Calls Qt's 'QString QFont::defaultFamily() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#defaultFamily

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFont::defaultFamily() const
    return self.uglySide.call('ritual_ZNK5QFont13defaultFamilyEv')

  @overload(THIS)
  def resolve(self, a0: QFont) -> QFont:
    """
    Calls Qt's 'QFont QFont::resolve(const QFont &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#resolve

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFont::resolve(const QFont &a0) const
    address = self.uglySide.call(
        'ritual_ZNK5QFont7resolveERKS_', self._valueOf(a0),
    )
    return QFont._cuteOwning(address)

  def resolveMask(self) -> int:
    """
    Calls Qt's 'uint QFont::resolveMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#resolveMask
    """
    #  uint QFont::resolveMask() const
    return self.uglySide.call('ritual_ZNK5QFont11resolveMaskEv')

  def legacyWeight(self) -> int:
    """
    Calls Qt's 'int QFont::legacyWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#legacyWeight
    """
    #  int QFont::legacyWeight() const
    return self.uglySide.call('ritual_ZNK5QFont12legacyWeightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFamily(self, a0: str) -> None:
    """
    Calls Qt's 'void QFont::setFamily(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setFamily

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFont::setFamily(const QString &a0)
    self.uglySide.call('ritual_ZN5QFont9setFamilyERK7QString', a0)

  @overload(str)
  def setStyleName(self, a0: str) -> None:
    """
    Calls Qt's 'void QFont::setStyleName(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setStyleName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFont::setStyleName(const QString &a0)
    self.uglySide.call('ritual_ZN5QFont12setStyleNameERK7QString', a0)

  @overload(int)
  def setPointSize(self, a0: int) -> None:
    """
    Calls Qt's 'void QFont::setPointSize(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setPointSize

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFont::setPointSize(int a0)
    self.uglySide.call('ritual_ZN5QFont12setPointSizeEi', a0)

  @overload(float)
  def setPointSizeF(self, a0: float) -> None:
    """
    Calls Qt's 'void QFont::setPointSizeF(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setPointSizeF

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QFont::setPointSizeF(qreal a0)
    self.uglySide.call('ritual_ZN5QFont13setPointSizeFEd', a0)

  @overload(int)
  def setPixelSize(self, a0: int) -> None:
    """
    Calls Qt's 'void QFont::setPixelSize(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setPixelSize

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFont::setPixelSize(int a0)
    self.uglySide.call('ritual_ZN5QFont12setPixelSizeEi', a0)

  @overload(Weight)
  def setWeight(self, weight: Weight) -> None:
    """
    Calls Qt's 'void QFont::setWeight(Weight weight)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setWeight

    Parameters
    ----------

    weight : Weight
      Passed on as its number.
    """
    #  void QFont::setWeight(Weight weight)
    self.uglySide.call('ritual_ZN5QFont9setWeightENS_6WeightE', weight.value)

  @overload(bool)
  def setBold(self, a0: bool) -> None:
    """
    Calls Qt's 'void QFont::setBold(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setBold

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QFont::setBold(bool a0)
    self.uglySide.call('ritual_ZN5QFont7setBoldEb', a0)

  @overload(Style)
  def setStyle(self, style: Style) -> None:
    """
    Calls Qt's 'void QFont::setStyle(Style style)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setStyle

    Parameters
    ----------

    style : Style
      Passed on as its number.
    """
    #  void QFont::setStyle(Style style)
    self.uglySide.call('ritual_ZN5QFont8setStyleENS_5StyleE', style.value)

  @overload(bool)
  def setItalic(self, b: bool) -> None:
    """
    Calls Qt's 'void QFont::setItalic(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setItalic

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QFont::setItalic(bool b)
    self.uglySide.call('ritual_ZN5QFont9setItalicEb', b)

  @overload(bool)
  def setUnderline(self, a0: bool) -> None:
    """
    Calls Qt's 'void QFont::setUnderline(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setUnderline

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QFont::setUnderline(bool a0)
    self.uglySide.call('ritual_ZN5QFont12setUnderlineEb', a0)

  @overload(bool)
  def setOverline(self, a0: bool) -> None:
    """
    Calls Qt's 'void QFont::setOverline(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setOverline

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QFont::setOverline(bool a0)
    self.uglySide.call('ritual_ZN5QFont11setOverlineEb', a0)

  @overload(bool)
  def setStrikeOut(self, a0: bool) -> None:
    """
    Calls Qt's 'void QFont::setStrikeOut(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setStrikeOut

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QFont::setStrikeOut(bool a0)
    self.uglySide.call('ritual_ZN5QFont12setStrikeOutEb', a0)

  @overload(bool)
  def setFixedPitch(self, a0: bool) -> None:
    """
    Calls Qt's 'void QFont::setFixedPitch(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setFixedPitch

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QFont::setFixedPitch(bool a0)
    self.uglySide.call('ritual_ZN5QFont13setFixedPitchEb', a0)

  @overload(bool)
  def setKerning(self, a0: bool) -> None:
    """
    Calls Qt's 'void QFont::setKerning(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setKerning

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QFont::setKerning(bool a0)
    self.uglySide.call('ritual_ZN5QFont10setKerningEb', a0)

  @overload(StyleHint)
  @overload(StyleHint, StyleStrategy)
  def setStyleHint(
      self,
      a0: StyleHint,
      a1: StyleStrategy = StyleStrategy.PreferDefault,
  ) -> None:
    """
    Calls Qt's 'void QFont::setStyleHint(StyleHint a0, StyleStrategy a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setStyleHint

    Parameters
    ----------

    a0 : StyleHint
      Passed on as its number.

    a1 : StyleStrategy
      Passed on as its number. May be left out, as in Qt: it is then
      StyleStrategy.PreferDefault.
    """
    #  void QFont::setStyleHint(StyleHint a0, StyleStrategy a1)
    self.uglySide.call(
        'ritual_ZN5QFont12setStyleHintENS_9StyleHintENS_13StyleStrategyE',
        a0.value, a1.value,
    )

  @overload(StyleStrategy)
  def setStyleStrategy(self, s: StyleStrategy) -> None:
    """
    Calls Qt's 'void QFont::setStyleStrategy(StyleStrategy s)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setStyleStrategy

    Parameters
    ----------

    s : StyleStrategy
      Passed on as its number.
    """
    #  void QFont::setStyleStrategy(StyleStrategy s)
    self.uglySide.call(
        'ritual_ZN5QFont16setStyleStrategyENS_13StyleStrategyE', s.value,
    )

  @overload(int)
  def setStretch(self, a0: int) -> None:
    """
    Calls Qt's 'void QFont::setStretch(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setStretch

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFont::setStretch(int a0)
    self.uglySide.call('ritual_ZN5QFont10setStretchEi', a0)

  @overload(SpacingType, float)
  def setLetterSpacing(self, type: SpacingType, spacing: float) -> None:
    """
    Calls Qt's 'void QFont::setLetterSpacing(SpacingType type, qreal
    spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setLetterSpacing

    Parameters
    ----------

    type : SpacingType
      Passed on as its number.

    spacing : float
      Passed on as it is.
    """
    #  void QFont::setLetterSpacing(SpacingType type, qreal spacing)
    self.uglySide.call(
        'ritual_ZN5QFont16setLetterSpacingENS_11SpacingTypeEd',
        type.value, spacing,
    )

  @overload(float)
  def setWordSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QFont::setWordSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setWordSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QFont::setWordSpacing(qreal spacing)
    self.uglySide.call('ritual_ZN5QFont14setWordSpacingEd', spacing)

  @overload(Capitalization)
  def setCapitalization(self, a0: Capitalization) -> None:
    """
    Calls Qt's 'void QFont::setCapitalization(Capitalization a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setCapitalization

    Parameters
    ----------

    a0 : Capitalization
      Passed on as its number.
    """
    #  void QFont::setCapitalization(Capitalization a0)
    self.uglySide.call(
        'ritual_ZN5QFont17setCapitalizationENS_14CapitalizationE', a0.value,
    )

  @overload(HintingPreference)
  def setHintingPreference(
      self,
      hintingPreference: HintingPreference,
  ) -> None:
    """
    Calls Qt's 'void QFont::setHintingPreference(HintingPreference
    hintingPreference)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setHintingPreference

    Parameters
    ----------

    hintingPreference : HintingPreference
      Passed on as its number.
    """
    #  void QFont::setHintingPreference(HintingPreference hintingPreference)
    self.uglySide.call(
        'ritual_ZN5QFont20setHintingPreferenceENS_17HintingPreferenceE',
        hintingPreference.value,
    )

  @overload(Tag, int)
  def setFeature(self, tag: Tag, value: int) -> None:
    """
    Calls Qt's 'void QFont::setFeature(Tag tag, quint32 value)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setFeature

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.

    value : int
      Passed on as it is.
    """
    #  void QFont::setFeature(Tag tag, quint32 value)
    self.uglySide.call(
        'ritual_ZN5QFont10setFeatureENS_3TagEj', self._valueOf(tag), value,
    )

  @overload(Tag, float)
  def setVariableAxis(self, tag: Tag, value: float) -> None:
    """
    Calls Qt's 'void QFont::setVariableAxis(Tag tag, float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setVariableAxis

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.

    value : float
      Passed on as it is.
    """
    #  void QFont::setVariableAxis(Tag tag, float value)
    self.uglySide.call(
        'ritual_ZN5QFont15setVariableAxisENS_3TagEf',
        self._valueOf(tag), value,
    )

  @overload(int)
  def setResolveMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QFont::setResolveMask(uint mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setResolveMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QFont::setResolveMask(uint mask)
    self.uglySide.call('ritual_ZN5QFont14setResolveMaskEj', mask)

  @overload(int)
  def setLegacyWeight(self, legacyWeight: int) -> None:
    """
    Calls Qt's 'void QFont::setLegacyWeight(int legacyWeight)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#setLegacyWeight

    Parameters
    ----------

    legacyWeight : int
      Passed on as it is.
    """
    #  void QFont::setLegacyWeight(int legacyWeight)
    self.uglySide.call('ritual_ZN5QFont15setLegacyWeightEi', legacyWeight)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QFont) -> bool:
    """
    Calls Qt's 'bool QFont::operator==(const QFont &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#operator==

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  bool QFont::operator==(const QFont &a0) const
    return self.uglySide.call('ritual_ZNK5QFonteqERKS_', self._valueOf(a0))

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, a0: QFont) -> bool:
    """
    Calls Qt's 'bool QFont::operator!=(const QFont &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#operator!=

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  bool QFont::operator!=(const QFont &a0) const
    return self.uglySide.call('ritual_ZNK5QFontneERKS_', self._valueOf(a0))

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, a0: QFont) -> bool:
    """
    Calls Qt's 'bool QFont::operator<(const QFont &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#operator<

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  bool QFont::operator<(const QFont &a0) const
    return self.uglySide.call('ritual_ZNK5QFontltERKS_', self._valueOf(a0))

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QFont &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QFont &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK5QFont',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QFont::QFont()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#QFont
    """
    #  QFont::QFont()
    self._noteCreation(QFont, lambda: Rituals.call('ritual_ZN5QFontC1Ev'))

  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  @overload(str, int, int, bool)
  def __init__(
      self,
      family: str,
      pointSize: int = -1,
      weight: int = -1,
      italic: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QFont::QFont(const QString &family, int
    pointSize, int weight, bool italic)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#QFont

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    pointSize : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    weight : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    italic : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QFont::QFont(const QString &family, int pointSize, int weight, bool
    #      italic)
    self._noteCreation(QFont, lambda: Rituals.call(
        'ritual_ZN5QFontC1ERK7QStringiib', family, pointSize, weight, italic,
    ))

  @overload(THIS, QPaintDevice)
  @overload(THIS, NoneType)
  def __init__(self, font: QFont, pd: Optional[QPaintDevice]) -> None:
    """
    Notes what was given, for Qt's 'QFont::QFont(const QFont &font, const
    QPaintDevice *pd)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#QFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    pd : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFont::QFont(const QFont &font, const QPaintDevice *pd)
    self._noteCreation(QFont, lambda: Rituals.call(
        'ritual_ZN5QFontC1ERKS_PK12QPaintDevice',
        self._valueOf(font), self._addressOf(pd, 'QPaintDevice'),
    ))

  @overload(THIS)
  def __init__(self, font: QFont) -> None:
    """
    Notes what was given, for Qt's 'QFont::QFont(const QFont &font)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#QFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QFont::QFont(const QFont &font)
    self._noteCreation(QFont, lambda: Rituals.call(
        'ritual_ZN5QFontC1ERKS_', self._valueOf(font),
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

  @overload(Tag)
  def unsetFeature(self, tag: Tag) -> None:
    """
    Calls Qt's 'void QFont::unsetFeature(Tag tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#unsetFeature

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  void QFont::unsetFeature(Tag tag)
    self.uglySide.call(
        'ritual_ZN5QFont12unsetFeatureENS_3TagE', self._valueOf(tag),
    )

  def clearFeatures(self) -> None:
    """
    Calls Qt's 'void QFont::clearFeatures()'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#clearFeatures
    """
    #  void QFont::clearFeatures()
    self.uglySide.call('ritual_ZN5QFont13clearFeaturesEv')

  @overload(Tag)
  def unsetVariableAxis(self, tag: Tag) -> None:
    """
    Calls Qt's 'void QFont::unsetVariableAxis(Tag tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#unsetVariableAxis

    Parameters
    ----------

    tag : Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  void QFont::unsetVariableAxis(Tag tag)
    self.uglySide.call(
        'ritual_ZN5QFont17unsetVariableAxisENS_3TagE', self._valueOf(tag),
    )

  def clearVariableAxes(self) -> None:
    """
    Calls Qt's 'void QFont::clearVariableAxes()'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#clearVariableAxes
    """
    #  void QFont::clearVariableAxes()
    self.uglySide.call('ritual_ZN5QFont17clearVariableAxesEv')

  @overload(str)
  def fromString(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QFont::fromString(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfont.html#fromString

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFont::fromString(const QString &a0)
    return self.uglySide.call('ritual_ZN5QFont10fromStringERK7QString', a0)
