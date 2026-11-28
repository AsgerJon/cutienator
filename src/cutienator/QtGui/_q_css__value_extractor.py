"""
QCss::ValueExtractor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::ValueExtractor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QCss

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QBrush, QIcon, QTextLength
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QIcon = WAIT['QIcon']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ValueExtractor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::ValueExtractor: a plain Python object standing
  in front of one C++ QCss::ValueExtractor.

  C++ hands a QCss::ValueExtractor around as a copy, so every C++
  QCss::ValueExtractor behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCss::ValueExtractor that has a ritual and that
  Python can call so far, 8 names in all: 'extractPalette',
  'extractStyleFeatures', 'extractIcon', 'textLength', 'extractFont',
  'lengthValue', 'sizeValue', 'sizeValues'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCss::ValueExtractor::ValueExtractor(const QList<Declaration>
    &declarations, const QPalette &a1)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QCss::ValueExtractor::extractFont(QFont *font, int
    *fontSizeAdjustment)': takes a number to change where it is.
  - Qt's 'bool QCss::ValueExtractor::extractBackground(QBrush *a0, QString
    *a1, Repeat *a2, Qt::Alignment *a3, QCss::Origin *a4, QCss::Attachment
    *a5, QCss::Origin *a6) const': names 'QCss::Repeat', which has no cute
    class yet.
  - Qt's 'bool QCss::ValueExtractor::extractGeometry(int *w, int *h, int
    *minw, int *minh, int *maxw, int *maxh)': takes a number to change where
    it is.
  - Qt's 'bool QCss::ValueExtractor::extractPosition(int *l, int *t, int *r,
    int *b, QCss::Origin *a4, Qt::Alignment *a5, QCss::PositionMode *a6,
    Qt::Alignment *a7)': takes a number to change where it is.
  - Qt's 'bool QCss::ValueExtractor::extractBox(int *margins, int *paddings,
    int *spacing)': takes a number to change where it is.
  - Qt's 'bool QCss::ValueExtractor::extractBorder(int *borders, QBrush
    *colors, BorderStyle *Styles, QSize *radii)': takes a number to change
    where it is.
  - Qt's 'bool QCss::ValueExtractor::extractOutline(int *borders, QBrush
    *colors, BorderStyle *Styles, QSize *radii, int *offsets)': takes a
    number to change where it is.
  - Qt's 'bool QCss::ValueExtractor::extractImage(QIcon *icon, Qt::Alignment
    *a, QSize *size) const': names 'Qt::Alignment', which has no cute class
    yet.
  - Qt's 'void QCss::ValueExtractor::lengthValues(const Declaration &decl,
    int *m)': takes a number to change where it is.
  - Qt's 'void QCss::ValueExtractor::borderValue(const Declaration &decl, int
    *width, QCss::BorderStyle *style, QBrush *color)': takes a number to
    change where it is.
  - Qt's 'QCss::ValueExtractor::~ValueExtractor()': the destructor: Python
    removes its C++ QCss::ValueExtractor by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::ValueExtractor is created at the first use, not by
    'QCss::ValueExtractor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::ValueExtractor back gives a copy the ritual
    made for Python, in a new cute QCss::ValueExtractor.
  - Each name of Qt's QCss::ValueExtractor that has no cute function yet,
    '__init__', 'borderValue', 'extractBackground', 'extractBorder',
    'extractBox', 'extractGeometry', 'extractImage', 'extractOutline',
    'extractPosition', 'lengthValues', holds a function that raises
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
  __qt_class__ = 'QCss::ValueExtractor'

  #  Qt's '~QCss::ValueExtractor()'. Naming it makes this a value class:
  #  Python owns every C++ QCss::ValueExtractor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QCss14ValueExtractorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBrush, QBrush, QBrush, QBrush, QBrush, QBrush)
  @overload(QBrush, QBrush, QBrush, QBrush, QBrush, NoneType)
  @overload(QBrush, QBrush, QBrush, QBrush, NoneType, QBrush)
  @overload(QBrush, QBrush, QBrush, QBrush, NoneType, NoneType)
  @overload(QBrush, QBrush, QBrush, NoneType, QBrush, QBrush)
  @overload(QBrush, QBrush, QBrush, NoneType, QBrush, NoneType)
  @overload(QBrush, QBrush, QBrush, NoneType, NoneType, QBrush)
  @overload(QBrush, QBrush, QBrush, NoneType, NoneType, NoneType)
  @overload(QBrush, QBrush, NoneType, QBrush, QBrush, QBrush)
  @overload(QBrush, QBrush, NoneType, QBrush, QBrush, NoneType)
  @overload(QBrush, QBrush, NoneType, QBrush, NoneType, QBrush)
  @overload(QBrush, QBrush, NoneType, QBrush, NoneType, NoneType)
  @overload(QBrush, QBrush, NoneType, NoneType, QBrush, QBrush)
  @overload(QBrush, QBrush, NoneType, NoneType, QBrush, NoneType)
  @overload(QBrush, QBrush, NoneType, NoneType, NoneType, QBrush)
  @overload(QBrush, QBrush, NoneType, NoneType, NoneType, NoneType)
  @overload(QBrush, NoneType, QBrush, QBrush, QBrush, QBrush)
  @overload(QBrush, NoneType, QBrush, QBrush, QBrush, NoneType)
  @overload(QBrush, NoneType, QBrush, QBrush, NoneType, QBrush)
  @overload(QBrush, NoneType, QBrush, QBrush, NoneType, NoneType)
  @overload(QBrush, NoneType, QBrush, NoneType, QBrush, QBrush)
  @overload(QBrush, NoneType, QBrush, NoneType, QBrush, NoneType)
  @overload(QBrush, NoneType, QBrush, NoneType, NoneType, QBrush)
  @overload(QBrush, NoneType, QBrush, NoneType, NoneType, NoneType)
  @overload(QBrush, NoneType, NoneType, QBrush, QBrush, QBrush)
  @overload(QBrush, NoneType, NoneType, QBrush, QBrush, NoneType)
  @overload(QBrush, NoneType, NoneType, QBrush, NoneType, QBrush)
  @overload(QBrush, NoneType, NoneType, QBrush, NoneType, NoneType)
  @overload(QBrush, NoneType, NoneType, NoneType, QBrush, QBrush)
  @overload(QBrush, NoneType, NoneType, NoneType, QBrush, NoneType)
  @overload(QBrush, NoneType, NoneType, NoneType, NoneType, QBrush)
  @overload(QBrush, NoneType, NoneType, NoneType, NoneType, NoneType)
  @overload(NoneType, QBrush, QBrush, QBrush, QBrush, QBrush)
  @overload(NoneType, QBrush, QBrush, QBrush, QBrush, NoneType)
  @overload(NoneType, QBrush, QBrush, QBrush, NoneType, QBrush)
  @overload(NoneType, QBrush, QBrush, QBrush, NoneType, NoneType)
  @overload(NoneType, QBrush, QBrush, NoneType, QBrush, QBrush)
  @overload(NoneType, QBrush, QBrush, NoneType, QBrush, NoneType)
  @overload(NoneType, QBrush, QBrush, NoneType, NoneType, QBrush)
  @overload(NoneType, QBrush, QBrush, NoneType, NoneType, NoneType)
  @overload(NoneType, QBrush, NoneType, QBrush, QBrush, QBrush)
  @overload(NoneType, QBrush, NoneType, QBrush, QBrush, NoneType)
  @overload(NoneType, QBrush, NoneType, QBrush, NoneType, QBrush)
  @overload(NoneType, QBrush, NoneType, QBrush, NoneType, NoneType)
  @overload(NoneType, QBrush, NoneType, NoneType, QBrush, QBrush)
  @overload(NoneType, QBrush, NoneType, NoneType, QBrush, NoneType)
  @overload(NoneType, QBrush, NoneType, NoneType, NoneType, QBrush)
  @overload(NoneType, QBrush, NoneType, NoneType, NoneType, NoneType)
  @overload(NoneType, NoneType, QBrush, QBrush, QBrush, QBrush)
  @overload(NoneType, NoneType, QBrush, QBrush, QBrush, NoneType)
  @overload(NoneType, NoneType, QBrush, QBrush, NoneType, QBrush)
  @overload(NoneType, NoneType, QBrush, QBrush, NoneType, NoneType)
  @overload(NoneType, NoneType, QBrush, NoneType, QBrush, QBrush)
  @overload(NoneType, NoneType, QBrush, NoneType, QBrush, NoneType)
  @overload(NoneType, NoneType, QBrush, NoneType, NoneType, QBrush)
  @overload(NoneType, NoneType, QBrush, NoneType, NoneType, NoneType)
  @overload(NoneType, NoneType, NoneType, QBrush, QBrush, QBrush)
  @overload(NoneType, NoneType, NoneType, QBrush, QBrush, NoneType)
  @overload(NoneType, NoneType, NoneType, QBrush, NoneType, QBrush)
  @overload(NoneType, NoneType, NoneType, QBrush, NoneType, NoneType)
  @overload(NoneType, NoneType, NoneType, NoneType, QBrush, QBrush)
  @overload(NoneType, NoneType, NoneType, NoneType, QBrush, NoneType)
  @overload(NoneType, NoneType, NoneType, NoneType, NoneType, QBrush)
  @overload(NoneType, NoneType, NoneType, NoneType, NoneType, NoneType)
  def extractPalette(
      self,
      foreground: Optional[QBrush],
      selectedForeground: Optional[QBrush],
      selectedBackground: Optional[QBrush],
      alternateBackground: Optional[QBrush],
      placeHolderTextForeground: Optional[QBrush],
      accent: Optional[QBrush],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::ValueExtractor::extractPalette(QBrush *foreground,
    QBrush *selectedForeground, QBrush *selectedBackground, QBrush
    *alternateBackground, QBrush *placeHolderTextForeground, QBrush *accent)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#extractPalette

    Parameters
    ----------

    foreground : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectedForeground : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectedBackground : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alternateBackground : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    placeHolderTextForeground : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    accent : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::ValueExtractor::extractPalette(QBrush *foreground, QBrush
    #      *selectedForeground, QBrush *selectedBackground, QBrush
    #      *alternateBackground, QBrush *placeHolderTextForeground, QBrush
    #      *accent) const
    return self.uglySide.call(
        'ritual_ZNK4QCss14ValueExtractor14extractPaletteEP6QBrushS2_S2_S2_S'
        '2_S2_',
        self._addressOf(foreground), self._addressOf(selectedForeground),
        self._addressOf(selectedBackground),
        self._addressOf(alternateBackground),
        self._addressOf(placeHolderTextForeground), self._addressOf(accent),
    )

  def extractStyleFeatures(self) -> int:
    """
    Calls Qt's 'int QCss::ValueExtractor::extractStyleFeatures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#extractStyleFeatures
    """
    #  int QCss::ValueExtractor::extractStyleFeatures() const
    return self.uglySide.call(
        'ritual_ZNK4QCss14ValueExtractor20extractStyleFeaturesEv',
    )

  @overload(QIcon, QSize)
  @overload(QIcon, NoneType)
  @overload(NoneType, QSize)
  @overload(NoneType, NoneType)
  def extractIcon(
      self,
      icon: Optional[QIcon],
      size: Optional[QSize],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::ValueExtractor::extractIcon(QIcon *icon, QSize
    *size) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#extractIcon

    Parameters
    ----------

    icon : Optional[QIcon]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::ValueExtractor::extractIcon(QIcon *icon, QSize *size) const
    return self.uglySide.call(
        'ritual_ZNK4QCss14ValueExtractor11extractIconEP5QIconP5QSize',
        self._addressOf(icon), self._addressOf(size),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QCss::ValueExtractor::ValueExtractor(const QList<Declaration>
    &declarations, const QPalette &a1)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.__init__' has no cute function yet. Qt's "
        "'QCss::ValueExtractor::ValueExtractor(const QList<Declaration> "
        "&declarations, const QPalette &a1)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload(WAIT['QCss.Declaration'])
  def textLength(self, decl: QCss.Declaration) -> QTextLength:
    """
    Calls Qt's 'QTextLength QCss::ValueExtractor::textLength(const
    Declaration &decl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#textLength

    Parameters
    ----------

    decl : QCss.Declaration
      Passed on as a value: Qt reads the C++ QCss::Declaration, which stays
      Python's own.

    Returns
    -------

    QTextLength
      A new cute QTextLength around the copy Qt gave back. Python owns it.
    """
    #  QTextLength QCss::ValueExtractor::textLength(const Declaration &decl)
    address = self.uglySide.call(
        'ritual_ZN4QCss14ValueExtractor10textLengthERKNS_11DeclarationE',
        self._valueOf(decl),
    )
    from . import QTextLength
    return QTextLength._cuteOwning(address)

  def extractFont(self) -> None:
    """
    Calls Qt's 'void QCss::ValueExtractor::extractFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#extractFont
    """
    #  void QCss::ValueExtractor::extractFont()
    self.uglySide.call('ritual_ZN4QCss14ValueExtractor11extractFontEv')

  @overload(WAIT['QCss.Value'])
  def lengthValue(self, v: QCss.Value) -> QCss.LengthData:
    """
    Calls Qt's 'LengthData QCss::ValueExtractor::lengthValue(const Value
    &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#lengthValue

    Parameters
    ----------

    v : QCss.Value
      Passed on as a value: Qt reads the C++ QCss::Value, which stays
      Python's own.

    Returns
    -------

    QCss.LengthData
      A new cute QCss::LengthData around the copy Qt gave back. Python owns
      it.
    """
    #  LengthData QCss::ValueExtractor::lengthValue(const Value &v)
    address = self.uglySide.call(
        'ritual_ZN4QCss14ValueExtractor11lengthValueERKNS_5ValueE',
        self._valueOf(v),
    )
    return QCss.LengthData._cuteOwning(address)

  @overload(WAIT['QCss.Declaration'])
  def lengthValue(self, decl: QCss.Declaration) -> int:
    """
    Calls Qt's 'int QCss::ValueExtractor::lengthValue(const Declaration
    &decl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#lengthValue

    Parameters
    ----------

    decl : QCss.Declaration
      Passed on as a value: Qt reads the C++ QCss::Declaration, which stays
      Python's own.
    """
    #  int QCss::ValueExtractor::lengthValue(const Declaration &decl)
    return self.uglySide.call(
        'ritual_ZN4QCss14ValueExtractor11lengthValueERKNS_11DeclarationE',
        self._valueOf(decl),
    )

  @overload(WAIT['QCss.Declaration'])
  def sizeValue(self, decl: QCss.Declaration) -> QSize:
    """
    Calls Qt's 'QSize QCss::ValueExtractor::sizeValue(const Declaration
    &decl)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-valueextractor.html#sizeValue

    Parameters
    ----------

    decl : QCss.Declaration
      Passed on as a value: Qt reads the C++ QCss::Declaration, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCss::ValueExtractor::sizeValue(const Declaration &decl)
    address = self.uglySide.call(
        'ritual_ZN4QCss14ValueExtractor9sizeValueERKNS_11DeclarationE',
        self._valueOf(decl),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(WAIT['QCss.Declaration'], QSize)
  @overload(WAIT['QCss.Declaration'], NoneType)
  def sizeValues(
      self,
      decl: QCss.Declaration,
      radii: Optional[QSize],
  ) -> None:
    """
    Calls Qt's 'void QCss::ValueExtractor::sizeValues(const Declaration
    &decl, QSize *radii)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-valueextractor.html#sizeValues

    Parameters
    ----------

    decl : QCss.Declaration
      Passed on as a value: Qt reads the C++ QCss::Declaration, which stays
      Python's own.

    radii : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCss::ValueExtractor::sizeValues(const Declaration &decl, QSize
    #      *radii)
    self.uglySide.call(
        'ritual_ZN4QCss14ValueExtractor10sizeValuesERKNS_11DeclarationEP5QS'
        'ize',
        self._valueOf(decl), self._addressOf(radii),
    )

  @staticmethod
  def borderValue(*__, **_) -> Never:
    """
    Qt's 'void QCss::ValueExtractor::borderValue(const Declaration &decl, int
    *width, QCss::BorderStyle *style, QBrush *color)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.borderValue' has no cute function yet. Qt's "
        "'void QCss::ValueExtractor::borderValue(const Declaration &decl, "
        "int *width, QCss::BorderStyle *style, QBrush *color)': takes a "
        "number to change where it is.")

  @staticmethod
  def extractBackground(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractBackground(QBrush *a0, QString
    *a1, Repeat *a2, Qt::Alignment *a3, QCss::Origin *a4, QCss::Attachment
    *a5, QCss::Origin *a6) const': names 'QCss::Repeat', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractBackground' has no cute function yet. "
        "Qt's 'bool QCss::ValueExtractor::extractBackground(QBrush *a0, "
        "QString *a1, Repeat *a2, Qt::Alignment *a3, QCss::Origin *a4, "
        "QCss::Attachment *a5, QCss::Origin *a6) const': names "
        "'QCss::Repeat', which has no cute class yet.")

  @staticmethod
  def extractBorder(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractBorder(int *borders, QBrush
    *colors, BorderStyle *Styles, QSize *radii)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractBorder' has no cute function yet. Qt's "
        "'bool QCss::ValueExtractor::extractBorder(int *borders, QBrush "
        "*colors, BorderStyle *Styles, QSize *radii)': takes a number to "
        "change where it is.")

  @staticmethod
  def extractBox(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractBox(int *margins, int *paddings,
    int *spacing)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractBox' has no cute function yet. Qt's "
        "'bool QCss::ValueExtractor::extractBox(int *margins, int "
        "*paddings, int *spacing)': takes a number to change where it is.")

  @staticmethod
  def extractGeometry(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractGeometry(int *w, int *h, int
    *minw, int *minh, int *maxw, int *maxh)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractGeometry' has no cute function yet. "
        "Qt's 'bool QCss::ValueExtractor::extractGeometry(int *w, int *h, "
        "int *minw, int *minh, int *maxw, int *maxh)': takes a number to "
        "change where it is.")

  @staticmethod
  def extractImage(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractImage(QIcon *icon, Qt::Alignment
    *a, QSize *size) const': names 'Qt::Alignment', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractImage' has no cute function yet. Qt's "
        "'bool QCss::ValueExtractor::extractImage(QIcon *icon, "
        "Qt::Alignment *a, QSize *size) const': names 'Qt::Alignment', "
        "which has no cute class yet.")

  @staticmethod
  def extractOutline(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractOutline(int *borders, QBrush
    *colors, BorderStyle *Styles, QSize *radii, int *offsets)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractOutline' has no cute function yet. "
        "Qt's 'bool QCss::ValueExtractor::extractOutline(int *borders, "
        "QBrush *colors, BorderStyle *Styles, QSize *radii, int *offsets)': "
        "takes a number to change where it is.")

  @staticmethod
  def extractPosition(*__, **_) -> Never:
    """
    Qt's 'bool QCss::ValueExtractor::extractPosition(int *l, int *t, int *r,
    int *b, QCss::Origin *a4, Qt::Alignment *a5, QCss::PositionMode *a6,
    Qt::Alignment *a7)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.extractPosition' has no cute function yet. "
        "Qt's 'bool QCss::ValueExtractor::extractPosition(int *l, int *t, "
        "int *r, int *b, QCss::Origin *a4, Qt::Alignment *a5, "
        "QCss::PositionMode *a6, Qt::Alignment *a7)': takes a number to "
        "change where it is.")

  @staticmethod
  def lengthValues(*__, **_) -> Never:
    """
    Qt's 'void QCss::ValueExtractor::lengthValues(const Declaration &decl,
    int *m)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.ValueExtractor.lengthValues' has no cute function yet. Qt's "
        "'void QCss::ValueExtractor::lengthValues(const Declaration &decl, "
        "int *m)': takes a number to change where it is.")
