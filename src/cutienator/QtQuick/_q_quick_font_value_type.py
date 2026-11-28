"""
QQuickFontValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickFontValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap
from ..QtGui import QFont
from . import QQuickFontEnums

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QVariant = WAIT['QVariant']


class QQuickFontValueType(QFont):
  """
  The cute side of Qt's QQuickFontValueType: a plain Python object standing
  in front of one C++ QQuickFontValueType.

  It is built on the cute 'QFont', as Qt's QQuickFontValueType is built on
  Qt's QFont, and has everything that class has.

  C++ hands a QQuickFontValueType around as a copy, so every C++
  QQuickFontValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickFontValueType that has a ritual and that
  Python can call so far, 42 names in all: 'create', 'toString', 'family',
  'setFamily', 'styleName', 'setStyleName', 'bold', 'setBold', 'weight',
  'setWeight', 'italic', 'setItalic', 'underline', 'setUnderline',
  'overline', 'setOverline', 'strikeout', 'setStrikeout', 'pointSize',
  'setPointSize', 'pixelSize', 'setPixelSize', 'capitalization',
  'setCapitalization', 'letterSpacing', 'setLetterSpacing', 'wordSpacing',
  'setWordSpacing', 'hintingPreference', 'setHintingPreference', 'kerning',
  'setKerning', 'preferShaping', 'setPreferShaping', 'features',
  'setFeatures', 'variableAxes', 'setVariableAxes', 'contextFontMerging',
  'setContextFontMerging', 'preferTypoLineMetrics',
  'setPreferTypoLineMetrics'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickFontValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickFontValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQuickFontValueType::~QQuickFontValueType()': the destructor:
    Python removes its C++ QQuickFontValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 50 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickFontValueType is created at the first use, not by
    'QQuickFontValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickFontValueType back gives a copy the ritual made
    for Python, in a new cute QQuickFontValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(value: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickFontValueType::create(const QJSValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#create

    Parameters
    ----------

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickFontValueType::create(const QJSValue &value)
    address = Rituals.call(
        'ritual_ZN19QQuickFontValueType6createERK8QJSValue',
        CuteMixin._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontValueType'

  #  Qt's '~QQuickFontValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickFontValueType behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQuickFontValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQuickFontValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontValueType::toString() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType8toStringEv')

  def family(self) -> str:
    """
    Calls Qt's 'QString QQuickFontValueType::family() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#family

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontValueType::family() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType6familyEv')

  def styleName(self) -> str:
    """
    Calls Qt's 'QString QQuickFontValueType::styleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontValueType::styleName() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType9styleNameEv')

  def bold(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::bold() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#bold
    """
    #  bool QQuickFontValueType::bold() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType4boldEv')

  def weight(self) -> int:
    """
    Calls Qt's 'int QQuickFontValueType::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#weight
    """
    #  int QQuickFontValueType::weight() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType6weightEv')

  def italic(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::italic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#italic
    """
    #  bool QQuickFontValueType::italic() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType6italicEv')

  def underline(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::underline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#underline
    """
    #  bool QQuickFontValueType::underline() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType9underlineEv')

  def overline(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::overline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#overline
    """
    #  bool QQuickFontValueType::overline() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType8overlineEv')

  def strikeout(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::strikeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#strikeout
    """
    #  bool QQuickFontValueType::strikeout() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType9strikeoutEv')

  def pointSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontValueType::pointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#pointSize
    """
    #  qreal QQuickFontValueType::pointSize() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType9pointSizeEv')

  def pixelSize(self) -> int:
    """
    Calls Qt's 'int QQuickFontValueType::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#pixelSize
    """
    #  int QQuickFontValueType::pixelSize() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType9pixelSizeEv')

  def capitalization(self) -> QQuickFontEnums.Capitalization:
    """
    Calls Qt's 'QQuickFontEnums::Capitalization
    QQuickFontValueType::capitalization() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#capitalization

    Returns
    -------

    QQuickFontEnums.Capitalization
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickFontEnums.Capitalization(number)' gives.
    """
    #  QQuickFontEnums::Capitalization QQuickFontValueType::capitalization()
    #      const
    return QQuickFontEnums.Capitalization(self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType14capitalizationEv',
    ))

  def letterSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontValueType::letterSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#letterSpacing
    """
    #  qreal QQuickFontValueType::letterSpacing() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType13letterSpacingEv',
    )

  def wordSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontValueType::wordSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#wordSpacing
    """
    #  qreal QQuickFontValueType::wordSpacing() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType11wordSpacingEv',
    )

  def hintingPreference(self) -> QQuickFontEnums.HintingPreference:
    """
    Calls Qt's 'QQuickFontEnums::HintingPreference
    QQuickFontValueType::hintingPreference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#hintingPreference

    Returns
    -------

    QQuickFontEnums.HintingPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickFontEnums.HintingPreference(number)' gives.
    """
    #  QQuickFontEnums::HintingPreference
    #      QQuickFontValueType::hintingPreference() const
    return QQuickFontEnums.HintingPreference(self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType17hintingPreferenceEv',
    ))

  def kerning(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::kerning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#kerning
    """
    #  bool QQuickFontValueType::kerning() const
    return self.uglySide.call('ritual_ZNK19QQuickFontValueType7kerningEv')

  def preferShaping(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::preferShaping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#preferShaping
    """
    #  bool QQuickFontValueType::preferShaping() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType13preferShapingEv',
    )

  def features(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QQuickFontValueType::features() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#features

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QQuickFontValueType::features() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType8featuresEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def variableAxes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QQuickFontValueType::variableAxes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#variableAxes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QQuickFontValueType::variableAxes() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType12variableAxesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def contextFontMerging(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::contextFontMerging() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#contextFontMerging
    """
    #  bool QQuickFontValueType::contextFontMerging() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType18contextFontMergingEv',
    )

  def preferTypoLineMetrics(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontValueType::preferTypoLineMetrics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#preferTypoLineMetrics
    """
    #  bool QQuickFontValueType::preferTypoLineMetrics() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickFontValueType21preferTypoLineMetricsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFamily(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setFamily(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#setFamily

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFontValueType::setFamily(const QString &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType9setFamilyERK7QString', a0,
    )

  @overload(str)
  def setStyleName(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setStyleName(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setStyleName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFontValueType::setStyleName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType12setStyleNameERK7QString', a0,
    )

  @overload(bool)
  def setBold(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setBold(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#setBold

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setBold(bool b)
    self.uglySide.call('ritual_ZN19QQuickFontValueType7setBoldEb', b)

  @overload(int)
  def setWeight(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setWeight(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#setWeight

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickFontValueType::setWeight(int a0)
    self.uglySide.call('ritual_ZN19QQuickFontValueType9setWeightEi', a0)

  @overload(bool)
  def setItalic(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setItalic(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontvaluetype.html#setItalic

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setItalic(bool b)
    self.uglySide.call('ritual_ZN19QQuickFontValueType9setItalicEb', b)

  @overload(bool)
  def setUnderline(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setUnderline(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setUnderline

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setUnderline(bool b)
    self.uglySide.call('ritual_ZN19QQuickFontValueType12setUnderlineEb', b)

  @overload(bool)
  def setOverline(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setOverline(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setOverline

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setOverline(bool b)
    self.uglySide.call('ritual_ZN19QQuickFontValueType11setOverlineEb', b)

  @overload(bool)
  def setStrikeout(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setStrikeout(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setStrikeout

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setStrikeout(bool b)
    self.uglySide.call('ritual_ZN19QQuickFontValueType12setStrikeoutEb', b)

  @overload(float)
  def setPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setPointSize(qreal size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuickFontValueType::setPointSize(qreal size)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType12setPointSizeEd', size,
    )

  @overload(int)
  def setPixelSize(self, size: int) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setPixelSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setPixelSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQuickFontValueType::setPixelSize(int size)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType12setPixelSizeEi', size,
    )

  @overload(QQuickFontEnums.Capitalization)
  def setCapitalization(self, a0: QQuickFontEnums.Capitalization) -> None:
    """
    Calls Qt's 'void
    QQuickFontValueType::setCapitalization(QQuickFontEnums::Capitalization
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setCapitalization

    Parameters
    ----------

    a0 : QQuickFontEnums.Capitalization
      Passed on as its number.
    """
    #  void QQuickFontValueType::setCapitalization(QQuickFontEnums::
    #      Capitalization a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType17setCapitalizationEN15QQuickFontEnu'
        'ms14CapitalizationE',
        a0.value,
    )

  @overload(float)
  def setLetterSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setLetterSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setLetterSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickFontValueType::setLetterSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType16setLetterSpacingEd', spacing,
    )

  @overload(float)
  def setWordSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setWordSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setWordSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickFontValueType::setWordSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType14setWordSpacingEd', spacing,
    )

  @overload(QQuickFontEnums.HintingPreference)
  def setHintingPreference(
      self,
      a0: QQuickFontEnums.HintingPreference,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontValueType::setHintingPreference(QQuickFontEnums::
    HintingPreference a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setHintingPreference

    Parameters
    ----------

    a0 : QQuickFontEnums.HintingPreference
      Passed on as its number.
    """
    #  void QQuickFontValueType::setHintingPreference(QQuickFontEnums::
    #      HintingPreference a0)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType20setHintingPreferenceEN15QQuickFont'
        'Enums17HintingPreferenceE',
        a0.value,
    )

  @overload(bool)
  def setKerning(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setKerning(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setKerning

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setKerning(bool b)
    self.uglySide.call('ritual_ZN19QQuickFontValueType10setKerningEb', b)

  @overload(bool)
  def setPreferShaping(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setPreferShaping(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setPreferShaping

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setPreferShaping(bool b)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType16setPreferShapingEb', b,
    )

  @overload(QMap[str, QVariant])
  def setFeatures(self, features: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setFeatures(const QVariantMap
    &features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setFeatures

    Parameters
    ----------

    features : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickFontValueType::setFeatures(const QVariantMap &features)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType11setFeaturesERK4QMapI7QString8QVari'
        'antE',
        self._valueOf(features),
    )

  @overload(QMap[str, QVariant])
  def setVariableAxes(self, variableAxes: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setVariableAxes(const QVariantMap
    &variableAxes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setVariableAxes

    Parameters
    ----------

    variableAxes : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickFontValueType::setVariableAxes(const QVariantMap
    #      &variableAxes)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType15setVariableAxesERK4QMapI7QString8Q'
        'VariantE',
        self._valueOf(variableAxes),
    )

  @overload(bool)
  def setContextFontMerging(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setContextFontMerging(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setContextFontMerging

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setContextFontMerging(bool b)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType21setContextFontMergingEb', b,
    )

  @overload(bool)
  def setPreferTypoLineMetrics(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickFontValueType::setPreferTypoLineMetrics(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#setPreferTypoLineMetrics

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickFontValueType::setPreferTypoLineMetrics(bool b)
    self.uglySide.call(
        'ritual_ZN19QQuickFontValueType24setPreferTypoLineMetricsEb', b,
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
    Notes what was given, for Qt's
    'QQuickFontValueType::QQuickFontValueType()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#QQuickFontValueType
    """
    #  QQuickFontValueType::QQuickFontValueType()
    self._noteCreation(QQuickFontValueType, lambda: Rituals.call(
        'ritual_ZN19QQuickFontValueTypeC1Ev',
    ))

  @overload(QFont)
  def __init__(self, font: QFont) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFontValueType::QQuickFontValueType(const QFont &font)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontvaluetype.html#QQuickFontValueType

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QQuickFontValueType::QQuickFontValueType(const QFont &font)
    self._noteCreation(QQuickFontValueType, lambda: Rituals.call(
        'ritual_ZN19QQuickFontValueTypeC1ERK5QFont', self._valueOf(font),
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
