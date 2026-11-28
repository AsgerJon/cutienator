"""
QPdfEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPdfEnginePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPaintEnginePrivate, QPdfEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QDateTime, QIODevice
  from ..QtCore import QPointF
  from . import QColor, QFontSubset, QGradient, QLinearGradient
  from . import QRadialGradient, QTextItemInt, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QColor = WAIT['QColor']
  QDateTime = WAIT['QDateTime']
  QFontSubset = WAIT['QFontSubset']
  QGradient = WAIT['QGradient']
  QIODevice = WAIT['QIODevice']
  QLinearGradient = WAIT['QLinearGradient']
  QPointF = WAIT['QPointF']
  QRadialGradient = WAIT['QRadialGradient']
  QTextItemInt = WAIT['QTextItemInt']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfEnginePrivate(QPaintEnginePrivate):
  """
  The cute side of Qt's QPdfEnginePrivate: a plain Python object standing in
  front of one C++ QPdfEnginePrivate.

  It is built on the cute 'QPaintEnginePrivate', as Qt's QPdfEnginePrivate is
  built on Qt's QPaintEnginePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfEnginePrivate that has a ritual and that Python
  can call so far, 27 names in all: 'q_func', 'requestObject', 'writeHeader',
  'writeTail', 'addConstantAlphaObject', 'drawTextItem', 'pageMatrix',
  'newPage', 'generateGradientShader', 'generateLinearGradientShader',
  'generateRadialGradientShader', 'colorModelForColor', 'writeInfo',
  'writeXmpDocumentMetaData', 'writeOutputIntent', 'writePageRoot',
  'writeDestsRoot', 'writeAttachmentRoot', 'writeNamesRoot', 'writeFonts',
  'embedFont', 'calcUserUnit', 'writePage', 'addXrefEntry', 'printString',
  'write', 'writeCompressed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPdfEngine *QPdfEnginePrivate::q_func() const': takes in
    Python what 'QPdfEngine *QPdfEnginePrivate::q_func()' takes.
  - Qt's 'QPdfEnginePrivate::~QPdfEnginePrivate()': the destructor: Python
    never removes a C++ QPdfEnginePrivate.
  - Qt's 'int QPdfEnginePrivate::addImage(const QImage &image, bool *bitmap,
    bool lossless, qint64 serial_no)': takes a number to change where it is.
  - Qt's 'int QPdfEnginePrivate::addBrushPattern(const QTransform &matrix,
    bool *specifyColor, int *gStateObject)': takes a number to change where
    it is.
  - Qt's 'int QPdfEnginePrivate::gradientBrush(const QBrush &b, const
    QTransform &matrix, int *gStateObject)': takes a number to change where
    it is.
  - Qt's 'ShadingFunctionResult
    QPdfEnginePrivate::createShadingFunction(const QGradient *gradient, int
    from, int to, bool reflect, bool alpha)': gives a type Python has no way
    to take yet.
  - Qt's 'void QPdfEnginePrivate::writeColor(ColorDomain domain, const QColor
    &color)': names the enum 'QPdfEnginePrivate::ColorDomain', whose class
    cannot be named here.
  - Qt's 'int QPdfEnginePrivate::writeImage(const QByteArray &data, int
    width, int height, WriteImageOption option, int maskObject, int
    softMaskObject, bool dct, bool isMono)': names the enum
    'QPdfEnginePrivate::WriteImageOption', whose class cannot be named here.

  What has no ritual
  ------------------

  1 of the 39 functions Qt declares: 1 takes any number of arguments.

  What to expect
  --------------

  - The C++ QPdfEnginePrivate is created at the first use, not by
    'QPdfEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfEnginePrivate.
  - Each name of Qt's QPdfEnginePrivate that has no cute function yet,
    'addBrushPattern', 'addImage', 'createShadingFunction', 'gradientBrush',
    'writeColor', 'writeImage', 'xprintf', holds a function that raises
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
  __qt_class__ = 'QPdfEnginePrivate'

  #  A C++ QPdfEnginePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfEnginePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pageMatrix(self) -> QTransform:
    """
    Calls Qt's 'QTransform QPdfEnginePrivate::pageMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#pageMatrix

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPdfEnginePrivate::pageMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK17QPdfEnginePrivate10pageMatrixEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  @overload(QColor)
  def colorModelForColor(self, color: QColor) -> QPdfEngine.ColorModel:
    """
    Calls Qt's 'QPdfEngine::ColorModel
    QPdfEnginePrivate::colorModelForColor(const QColor &color) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#colorModelForColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QPdfEngine.ColorModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPdfEngine.ColorModel(number)' gives.
    """
    #  QPdfEngine::ColorModel QPdfEnginePrivate::colorModelForColor(const
    #      QColor &color) const
    return QPdfEngine.ColorModel(self.uglySide.call(
        'ritual_ZNK17QPdfEnginePrivate18colorModelForColorERK6QColor',
        self._valueOf(color),
    ))

  def calcUserUnit(self) -> float:
    """
    Calls Qt's 'qreal QPdfEnginePrivate::calcUserUnit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#calcUserUnit
    """
    #  qreal QPdfEnginePrivate::calcUserUnit() const
    return self.uglySide.call(
        'ritual_ZNK17QPdfEnginePrivate12calcUserUnitEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfEnginePrivate::QPdfEnginePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#QPdfEnginePrivate
    """
    #  QPdfEnginePrivate::QPdfEnginePrivate()
    self._noteCreation(QPdfEnginePrivate, lambda: Rituals.call(
        'ritual_ZN17QPdfEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QPdfEngine]:
    """
    Calls Qt's 'QPdfEngine *QPdfEnginePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#q_func

    Returns
    -------

    Optional[QPdfEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfEngine *QPdfEnginePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QPdfEnginePrivate6q_funcEv')
    return QPdfEngine._cuteAt(address)

  def requestObject(self) -> int:
    """
    Calls Qt's 'uint QPdfEnginePrivate::requestObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#requestObject
    """
    #  uint QPdfEnginePrivate::requestObject()
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate13requestObjectEv',
    )

  def writeHeader(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeHeader()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#writeHeader
    """
    #  void QPdfEnginePrivate::writeHeader()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate11writeHeaderEv')

  def writeTail(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeTail()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#writeTail
    """
    #  void QPdfEnginePrivate::writeTail()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate9writeTailEv')

  @overload(int)
  @overload(int, int)
  def addConstantAlphaObject(
      self,
      brushAlpha: int,
      penAlpha: int = 255,
  ) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::addConstantAlphaObject(int brushAlpha,
    int penAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#addConstantAlphaObject

    Parameters
    ----------

    brushAlpha : int
      Passed on as it is.

    penAlpha : int
      Passed on as it is. May be left out, as in Qt: it is then 255.
    """
    #  int QPdfEnginePrivate::addConstantAlphaObject(int brushAlpha, int
    #      penAlpha)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate22addConstantAlphaObjectEii',
        brushAlpha, penAlpha,
    )

  @overload(QPointF, QTextItemInt)
  def drawTextItem(self, p: QPointF, ti: QTextItemInt) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::drawTextItem(const QPointF &p, const
    QTextItemInt &ti)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ti : QTextItemInt
      Passed on as a value: Qt reads the C++ QTextItemInt, which stays
      Python's own.
    """
    #  void QPdfEnginePrivate::drawTextItem(const QPointF &p, const
    #      QTextItemInt &ti)
    self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate12drawTextItemERK7QPointFRK12QTextItem'
        'Int',
        self._valueOf(p, 'QPointF'), self._valueOf(ti),
    )

  def newPage(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#newPage
    """
    #  void QPdfEnginePrivate::newPage()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate7newPageEv')

  @overload(QGradient, QTransform)
  @overload(NoneType, QTransform)
  @overload(QGradient, QTransform, bool)
  @overload(NoneType, QTransform, bool)
  def generateGradientShader(
      self,
      gradient: Optional[QGradient],
      matrix: QTransform,
      alpha: bool = False,
  ) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::generateGradientShader(const QGradient
    *gradient, const QTransform &matrix, bool alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#generateGradientShader

    Parameters
    ----------

    gradient : Optional[QGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    alpha : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  int QPdfEnginePrivate::generateGradientShader(const QGradient
    #      *gradient, const QTransform &matrix, bool alpha)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate22generateGradientShaderEPK9QGradientR'
        'K10QTransformb',
        self._addressOf(gradient), self._valueOf(matrix), alpha,
    )

  @overload(QLinearGradient, QTransform, bool)
  @overload(NoneType, QTransform, bool)
  def generateLinearGradientShader(
      self,
      lg: Optional[QLinearGradient],
      matrix: QTransform,
      alpha: bool,
  ) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::generateLinearGradientShader(const
    QLinearGradient *lg, const QTransform &matrix, bool alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html

    Parameters
    ----------

    lg : Optional[QLinearGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    alpha : bool
      Passed on as it is.
    """
    #  int QPdfEnginePrivate::generateLinearGradientShader(const
    #      QLinearGradient *lg, const QTransform &matrix, bool alpha)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate28generateLinearGradientShaderEPK15QLi'
        'nearGradientRK10QTransformb',
        self._addressOf(lg), self._valueOf(matrix), alpha,
    )

  @overload(QRadialGradient, QTransform, bool)
  @overload(NoneType, QTransform, bool)
  def generateRadialGradientShader(
      self,
      gradient: Optional[QRadialGradient],
      matrix: QTransform,
      alpha: bool,
  ) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::generateRadialGradientShader(const
    QRadialGradient *gradient, const QTransform &matrix, bool alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html

    Parameters
    ----------

    gradient : Optional[QRadialGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    alpha : bool
      Passed on as it is.
    """
    #  int QPdfEnginePrivate::generateRadialGradientShader(const
    #      QRadialGradient *gradient, const QTransform &matrix, bool alpha)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate28generateRadialGradientShaderEPK15QRa'
        'dialGradientRK10QTransformb',
        self._addressOf(gradient), self._valueOf(matrix), alpha,
    )

  @overload(QDateTime)
  def writeInfo(self, date: QDateTime) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeInfo(const QDateTime &date)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#writeInfo

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QPdfEnginePrivate::writeInfo(const QDateTime &date)
    self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate9writeInfoERK9QDateTime',
        self._valueOf(date),
    )

  @overload(QDateTime)
  def writeXmpDocumentMetaData(self, date: QDateTime) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::writeXmpDocumentMetaData(const
    QDateTime &date)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeXmpDocumentMetaData

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  int QPdfEnginePrivate::writeXmpDocumentMetaData(const QDateTime &date)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate24writeXmpDocumentMetaDataERK9QDateTim'
        'e',
        self._valueOf(date),
    )

  def writeOutputIntent(self) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::writeOutputIntent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeOutputIntent
    """
    #  int QPdfEnginePrivate::writeOutputIntent()
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate17writeOutputIntentEv',
    )

  def writePageRoot(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writePageRoot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writePageRoot
    """
    #  void QPdfEnginePrivate::writePageRoot()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate13writePageRootEv')

  def writeDestsRoot(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeDestsRoot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeDestsRoot
    """
    #  void QPdfEnginePrivate::writeDestsRoot()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate14writeDestsRootEv')

  def writeAttachmentRoot(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeAttachmentRoot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeAttachmentRoot
    """
    #  void QPdfEnginePrivate::writeAttachmentRoot()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate19writeAttachmentRootEv')

  def writeNamesRoot(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeNamesRoot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeNamesRoot
    """
    #  void QPdfEnginePrivate::writeNamesRoot()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate14writeNamesRootEv')

  def writeFonts(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writeFonts()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#writeFonts
    """
    #  void QPdfEnginePrivate::writeFonts()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate10writeFontsEv')

  @overload(QFontSubset)
  @overload(NoneType)
  def embedFont(self, font: Optional[QFontSubset]) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::embedFont(QFontSubset *font)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#embedFont

    Parameters
    ----------

    font : Optional[QFontSubset]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfEnginePrivate::embedFont(QFontSubset *font)
    self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate9embedFontEP11QFontSubset',
        self._addressOf(font),
    )

  def writePage(self) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::writePage()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#writePage
    """
    #  void QPdfEnginePrivate::writePage()
    self.uglySide.call('ritual_ZN17QPdfEnginePrivate9writePageEv')

  @overload(int)
  @overload(int, bool)
  def addXrefEntry(self, object: int, printostr: bool = True) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::addXrefEntry(int object, bool
    printostr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#addXrefEntry

    Parameters
    ----------

    object : int
      Passed on as it is.

    printostr : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int QPdfEnginePrivate::addXrefEntry(int object, bool printostr)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate12addXrefEntryEib', object, printostr,
    )

  @overload(str)
  def printString(self, string: str) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::printString(QStringView string)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#printString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfEnginePrivate::printString(QStringView string)
    self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate11printStringE11QStringView', string,
    )

  @overload(QByteArrayView)
  def write(self, data: QByteArrayView) -> None:
    """
    Calls Qt's 'void QPdfEnginePrivate::write(QByteArrayView data)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengineprivate.html#write

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QPdfEnginePrivate::write(QByteArrayView data)
    self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate5writeE14QByteArrayView',
        self._valueOf(data),
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeCompressed(self, src: Optional[str], len: int) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::writeCompressed(const char *src, int
    len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeCompressed

    Parameters
    ----------

    src : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  int QPdfEnginePrivate::writeCompressed(const char *src, int len)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate15writeCompressedEPKci',
        self._bytesOf(src), len,
    )

  @overload(QByteArray)
  def writeCompressed(self, data: QByteArray) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::writeCompressed(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeCompressed

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QPdfEnginePrivate::writeCompressed(const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate15writeCompressedERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def writeCompressed(self, dev: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'int QPdfEnginePrivate::writeCompressed(QIODevice *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengineprivate.html#writeCompressed

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QPdfEnginePrivate::writeCompressed(QIODevice *dev)
    return self.uglySide.call(
        'ritual_ZN17QPdfEnginePrivate15writeCompressedEP9QIODevice',
        self._addressOf(dev),
    )

  @staticmethod
  def addBrushPattern(*__, **_) -> Never:
    """
    Qt's 'int QPdfEnginePrivate::addBrushPattern(const QTransform &matrix,
    bool *specifyColor, int *gStateObject)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.addBrushPattern' has no cute function yet. Qt's "
        "'int QPdfEnginePrivate::addBrushPattern(const QTransform &matrix, "
        "bool *specifyColor, int *gStateObject)': takes a number to change "
        "where it is.")

  @staticmethod
  def addImage(*__, **_) -> Never:
    """
    Qt's 'int QPdfEnginePrivate::addImage(const QImage &image, bool *bitmap,
    bool lossless, qint64 serial_no)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.addImage' has no cute function yet. Qt's 'int "
        "QPdfEnginePrivate::addImage(const QImage &image, bool *bitmap, "
        "bool lossless, qint64 serial_no)': takes a number to change where "
        "it is.")

  @staticmethod
  def createShadingFunction(*__, **_) -> Never:
    """
    Qt's 'ShadingFunctionResult
    QPdfEnginePrivate::createShadingFunction(const QGradient *gradient, int
    from, int to, bool reflect, bool alpha)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.createShadingFunction' has no cute function "
        "yet. Qt's 'ShadingFunctionResult "
        "QPdfEnginePrivate::createShadingFunction(const QGradient "
        "*gradient, int from, int to, bool reflect, bool alpha)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def gradientBrush(*__, **_) -> Never:
    """
    Qt's 'int QPdfEnginePrivate::gradientBrush(const QBrush &b, const
    QTransform &matrix, int *gStateObject)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.gradientBrush' has no cute function yet. Qt's "
        "'int QPdfEnginePrivate::gradientBrush(const QBrush &b, const "
        "QTransform &matrix, int *gStateObject)': takes a number to change "
        "where it is.")

  @staticmethod
  def writeColor(*__, **_) -> Never:
    """
    Qt's 'void QPdfEnginePrivate::writeColor(ColorDomain domain, const QColor
    &color)': names the enum 'QPdfEnginePrivate::ColorDomain', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.writeColor' has no cute function yet. Qt's "
        "'void QPdfEnginePrivate::writeColor(ColorDomain domain, const "
        "QColor &color)': names the enum 'QPdfEnginePrivate::ColorDomain', "
        "whose class cannot be named here.")

  @staticmethod
  def writeImage(*__, **_) -> Never:
    """
    Qt's 'int QPdfEnginePrivate::writeImage(const QByteArray &data, int
    width, int height, WriteImageOption option, int maskObject, int
    softMaskObject, bool dct, bool isMono)': names the enum
    'QPdfEnginePrivate::WriteImageOption', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.writeImage' has no cute function yet. Qt's 'int "
        "QPdfEnginePrivate::writeImage(const QByteArray &data, int width, "
        "int height, WriteImageOption option, int maskObject, int "
        "softMaskObject, bool dct, bool isMono)': names the enum "
        "'QPdfEnginePrivate::WriteImageOption', whose class cannot be named "
        "here.")

  @staticmethod
  def xprintf(*__, **_) -> Never:
    """
    Qt's 'void QPdfEnginePrivate::xprintf(const char *fmt)': takes any number
    of arguments.
    """
    raise NotImplementedError(
        "'QPdfEnginePrivate.xprintf' has no cute function yet. Qt's 'void "
        "QPdfEnginePrivate::xprintf(const char *fmt)': takes any number of "
        "arguments.")
