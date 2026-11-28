"""
QDistanceField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdistancefield_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDistanceField to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from . import QDistanceFieldData, QFontEngine, QPainterPath, QRawFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDistanceFieldData = WAIT['QDistanceFieldData']
  QFontEngine = WAIT['QFontEngine']
  QPainterPath = WAIT['QPainterPath']
  QRawFont = WAIT['QRawFont']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDistanceField(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDistanceField: a plain Python object standing in
  front of one C++ QDistanceField.

  C++ hands a QDistanceField around as a copy, so every C++ QDistanceField
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDistanceField that has a ritual and that Python can
  call so far, 7 names in all: 'isNull', 'glyph', 'setGlyph', 'width',
  'height', 'copy', 'toImage'. It can be made from Python, in 7 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const uchar *QDistanceField::bits() const': gives 'unsigned char',
    which has no cute class yet.
  - Qt's 'const uchar *QDistanceField::constBits() const': gives 'unsigned
    char', which has no cute class yet.
  - Qt's 'const uchar *QDistanceField::scanLine(int a0) const': gives
    'unsigned char', which has no cute class yet.
  - Qt's 'const uchar *QDistanceField::constScanLine(int a0) const': gives
    'unsigned char', which has no cute class yet.
  - Qt's 'QDistanceField::~QDistanceField()': the destructor: Python removes
    its C++ QDistanceField by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QDistanceField is created at the first use, not by
    'QDistanceField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDistanceField back gives a copy the ritual made for
    Python, in a new cute QDistanceField.
  - Each name of Qt's QDistanceField that has no cute function yet, 'bits',
    'constBits', 'constScanLine', 'scanLine', holds a function that raises
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
  __qt_class__ = 'QDistanceField'

  #  Qt's '~QDistanceField()'. Naming it makes this a value class: Python
  #  owns every C++ QDistanceField behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QDistanceFieldD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDistanceField::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#isNull
    """
    #  bool QDistanceField::isNull() const
    return self.uglySide.call('ritual_ZNK14QDistanceField6isNullEv')

  def glyph(self) -> int:
    """
    Calls Qt's 'glyph_t QDistanceField::glyph() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#glyph
    """
    #  glyph_t QDistanceField::glyph() const
    return self.uglySide.call('ritual_ZNK14QDistanceField5glyphEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QDistanceField::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#width
    """
    #  int QDistanceField::width() const
    return self.uglySide.call('ritual_ZNK14QDistanceField5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QDistanceField::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#height
    """
    #  int QDistanceField::height() const
    return self.uglySide.call('ritual_ZNK14QDistanceField6heightEv')

  @overload()
  @overload(QRect)
  def copy(self, rect: Optional[QRect] = None) -> QDistanceField:
    """
    Calls Qt's 'QDistanceField QDistanceField::copy(const QRect &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#copy

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.

    Returns
    -------

    QDistanceField
      A new cute QDistanceField around the copy Qt gave back. Python owns it.
    """
    #  QDistanceField QDistanceField::copy(const QRect &rect) const
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    address = self.uglySide.call(
        'ritual_ZNK14QDistanceField4copyERK5QRect', self._valueOf(rect),
    )
    return QDistanceField._cuteOwning(address)

  @overload(int, int, int, int)
  def copy(self, x: int, y: int, w: int, h: int) -> QDistanceField:
    """
    Calls Qt's 'QDistanceField QDistanceField::copy(int x, int y, int w, int
    h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#copy

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    Returns
    -------

    QDistanceField
      A new cute QDistanceField around the copy Qt gave back. Python owns it.
    """
    #  QDistanceField QDistanceField::copy(int x, int y, int w, int h) const
    address = self.uglySide.call(
        'ritual_ZNK14QDistanceField4copyEiiii', x, y, w, h,
    )
    return QDistanceField._cuteOwning(address)

  @overload()
  @overload(QImage.Format)
  def toImage(
      self,
      format: QImage.Format = QImage.Format.Format_ARGB32_Premultiplied,
  ) -> QImage:
    """
    Calls Qt's 'QImage QDistanceField::toImage(QImage::Format format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#toImage

    Parameters
    ----------

    format : QImage.Format
      Passed on as its number. May be left out, as in Qt: it is then
      QImage.Format.Format_ARGB32_Premultiplied.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QDistanceField::toImage(QImage::Format format) const
    address = self.uglySide.call(
        'ritual_ZNK14QDistanceField7toImageEN6QImage6FormatE', format.value,
    )
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRawFont, int)
  @overload(QRawFont, int, bool)
  def setGlyph(
      self,
      font: QRawFont,
      glyph: int,
      doubleResolution: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QDistanceField::setGlyph(const QRawFont &font, glyph_t
    glyph, bool doubleResolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#setGlyph

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    glyph : int
      Passed on as it is.

    doubleResolution : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDistanceField::setGlyph(const QRawFont &font, glyph_t glyph,
    #      bool doubleResolution)
    self.uglySide.call(
        'ritual_ZN14QDistanceField8setGlyphERK8QRawFontjb',
        self._valueOf(font), glyph, doubleResolution,
    )

  @overload(QFontEngine, int)
  @overload(NoneType, int)
  @overload(QFontEngine, int, bool)
  @overload(NoneType, int, bool)
  def setGlyph(
      self,
      fontEngine: Optional[QFontEngine],
      glyph: int,
      doubleResolution: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QDistanceField::setGlyph(QFontEngine *fontEngine,
    glyph_t glyph, bool doubleResolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#setGlyph

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    glyph : int
      Passed on as it is.

    doubleResolution : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDistanceField::setGlyph(QFontEngine *fontEngine, glyph_t glyph,
    #      bool doubleResolution)
    self.uglySide.call(
        'ritual_ZN14QDistanceField8setGlyphEP11QFontEnginejb',
        self._addressOf(fontEngine), glyph, doubleResolution,
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
    Notes what was given, for Qt's 'QDistanceField::QDistanceField()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField
    """
    #  QDistanceField::QDistanceField()
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1Ev',
    ))

  @overload(int, int)
  def __init__(self, width: int, height: int) -> None:
    """
    Notes what was given, for Qt's 'QDistanceField::QDistanceField(int width,
    int height)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  QDistanceField::QDistanceField(int width, int height)
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1Eii', width, height,
    ))

  @overload(QRawFont, int)
  @overload(QRawFont, int, bool)
  def __init__(
      self,
      font: QRawFont,
      glyph: int,
      doubleResolution: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDistanceField::QDistanceField(const
    QRawFont &font, glyph_t glyph, bool doubleResolution)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    glyph : int
      Passed on as it is.

    doubleResolution : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QDistanceField::QDistanceField(const QRawFont &font, glyph_t glyph,
    #      bool doubleResolution)
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1ERK8QRawFontjb',
        self._valueOf(font), glyph, doubleResolution,
    ))

  @overload(QFontEngine, int)
  @overload(NoneType, int)
  @overload(QFontEngine, int, bool)
  @overload(NoneType, int, bool)
  def __init__(
      self,
      fontEngine: Optional[QFontEngine],
      glyph: int,
      doubleResolution: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDistanceField::QDistanceField(QFontEngine *fontEngine, glyph_t glyph,
    bool doubleResolution)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    glyph : int
      Passed on as it is.

    doubleResolution : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QDistanceField::QDistanceField(QFontEngine *fontEngine, glyph_t glyph,
    #      bool doubleResolution)
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1EP11QFontEnginejb',
        self._addressOf(fontEngine), glyph, doubleResolution,
    ))

  @overload(QPainterPath, int)
  @overload(QPainterPath, int, bool)
  def __init__(
      self,
      path: QPainterPath,
      glyph: int,
      doubleResolution: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDistanceField::QDistanceField(const
    QPainterPath &path, glyph_t glyph, bool doubleResolution)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    glyph : int
      Passed on as it is.

    doubleResolution : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QDistanceField::QDistanceField(const QPainterPath &path, glyph_t
    #      glyph, bool doubleResolution)
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1ERK12QPainterPathjb',
        self._valueOf(path), glyph, doubleResolution,
    ))

  @overload(QSize, QPainterPath, int)
  @overload(QSize, QPainterPath, int, bool)
  def __init__(
      self,
      size: QSize,
      path: QPainterPath,
      glyph: int,
      doubleResolution: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDistanceField::QDistanceField(QSize
    size, const QPainterPath &path, glyph_t glyph, bool doubleResolution)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    glyph : int
      Passed on as it is.

    doubleResolution : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QDistanceField::QDistanceField(QSize size, const QPainterPath &path,
    #      glyph_t glyph, bool doubleResolution)
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1E5QSizeRK12QPainterPathjb',
        self._valueOf(size), self._valueOf(path), glyph, doubleResolution,
    ))

  @overload(QDistanceFieldData)
  @overload(NoneType)
  def __init__(self, data: Optional[QDistanceFieldData]) -> None:
    """
    Notes what was given, for Qt's
    'QDistanceField::QDistanceField(QDistanceFieldData *data)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdistancefield.html#QDistanceField

    Parameters
    ----------

    data : Optional[QDistanceFieldData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDistanceField::QDistanceField(QDistanceFieldData *data)
    self._noteCreation(QDistanceField, lambda: Rituals.call(
        'ritual_ZN14QDistanceFieldC1EP18QDistanceFieldData',
        self._addressOf(data),
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

  @staticmethod
  def bits(*__, **_) -> Never:
    """
    - Qt's 'const uchar *QDistanceField::bits() const': gives 'unsigned
      char', which has no cute class yet.
    - Qt's 'uchar *QDistanceField::bits()': takes or gives a type that cannot
      be passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QDistanceField.bits' has no cute function yet. Qt's 'const uchar "
        "*QDistanceField::bits() const': gives 'unsigned char', which has "
        "no cute class yet. Qt's 'uchar *QDistanceField::bits()': takes or "
        "gives a type that cannot be passed yet: uchar *.")

  @staticmethod
  def constBits(*__, **_) -> Never:
    """
    Qt's 'const uchar *QDistanceField::constBits() const': gives 'unsigned
    char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDistanceField.constBits' has no cute function yet. Qt's 'const "
        "uchar *QDistanceField::constBits() const': gives 'unsigned char', "
        "which has no cute class yet.")

  @staticmethod
  def constScanLine(*__, **_) -> Never:
    """
    Qt's 'const uchar *QDistanceField::constScanLine(int a0) const': gives
    'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDistanceField.constScanLine' has no cute function yet. Qt's "
        "'const uchar *QDistanceField::constScanLine(int a0) const': gives "
        "'unsigned char', which has no cute class yet.")

  @staticmethod
  def scanLine(*__, **_) -> Never:
    """
    - Qt's 'const uchar *QDistanceField::scanLine(int a0) const': gives
      'unsigned char', which has no cute class yet.
    - Qt's 'uchar *QDistanceField::scanLine(int a0)': takes or gives a type
      that cannot be passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QDistanceField.scanLine' has no cute function yet. Qt's 'const "
        "uchar *QDistanceField::scanLine(int a0) const': gives 'unsigned "
        "char', which has no cute class yet. Qt's 'uchar "
        "*QDistanceField::scanLine(int a0)': takes or gives a type that "
        "cannot be passed yet: uchar *.")


#  Qt's 'QList<QDistanceField>': the list of QDistanceField, which
#  'QList[QDistanceField]' gives. It is made here, so that there is one as
#  soon as there can be a QDistanceField.
QList.createKind(
    QDistanceField, 'value',
    make='ritual_list_make_QDistanceField',
    add='ritual_list_add_QDistanceField',
    size='ritual_list_size_QDistanceField',
    at='ritual_list_at_QDistanceField',
    drop='ritual_list_drop_QDistanceField',
)
