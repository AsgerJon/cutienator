"""
QSpanData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdrawhelper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSpanData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRasterBuffer, QRasterPaintEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRasterBuffer = WAIT['QRasterBuffer']
  QRasterPaintEngine = WAIT['QRasterPaintEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpanData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSpanData: a plain Python object standing in front of
  one C++ QSpanData.

  C++ hands a QSpanData around as a copy, so every C++ QSpanData behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSpanData that has a ritual and that Python can call
  so far, 1 name in all: 'init'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSpanData::~QSpanData()': the destructor: Python removes its C++
    QSpanData by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QSpanData.

  What to expect
  --------------

  - The C++ QSpanData is created at the first use, not by 'QSpanData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSpanData back gives a copy the ritual made for
    Python, in a new cute QSpanData.
  - Each name of Qt's QSpanData that has no cute function yet,
    'adjustSpanMethods', 'initTexture', 'setup', 'setupMatrix', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSpanData, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """The enum 'QSpanData::Type' of Qt, with the 6 names Qt gives in it."""

    NULL = Kee[int](0)
    Solid = Kee[int](1)
    LinearGradient = Kee[int](2)
    RadialGradient = Kee[int](3)
    ConicalGradient = Kee[int](4)
    Texture = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpanData'

  #  Qt's '~QSpanData()'. Naming it makes this a value class: Python owns
  #  every C++ QSpanData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSpanDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QSpanData::QSpanData()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qspandata.html#QSpanData
    """
    #  QSpanData::QSpanData()
    self._noteCreation(QSpanData, lambda: Rituals.call(
        'ritual_ZN9QSpanDataC1Ev',
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

  @overload(QRasterBuffer, QRasterPaintEngine)
  @overload(QRasterBuffer, NoneType)
  @overload(NoneType, QRasterPaintEngine)
  @overload(NoneType, NoneType)
  def init(
      self,
      rb: Optional[QRasterBuffer],
      pe: Optional[QRasterPaintEngine],
  ) -> None:
    """
    Calls Qt's 'void QSpanData::init(QRasterBuffer *rb, const
    QRasterPaintEngine *pe)'.

    Qt's own words: https://doc.qt.io/qt-6/qspandata.html#init

    Parameters
    ----------

    rb : Optional[QRasterBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pe : Optional[QRasterPaintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSpanData::init(QRasterBuffer *rb, const QRasterPaintEngine *pe)
    self.uglySide.call(
        'ritual_ZN9QSpanData4initEP13QRasterBufferPK18QRasterPaintEngine',
        self._addressOf(rb), self._addressOf(pe),
    )

  @staticmethod
  def adjustSpanMethods(*__, **_) -> Never:
    """
    Qt's 'void QSpanData::adjustSpanMethods()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qt_span_fill_clipRect'; did you mean
    'qt_span_fill_clipped'?.
    """
    raise NotImplementedError(
        "'QSpanData.adjustSpanMethods' has no cute function yet. Qt's 'void "
        "QSpanData::adjustSpanMethods()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qt_span_fill_clipRect'; did you mean "
        "'qt_span_fill_clipped'?.")

  @staticmethod
  def initTexture(*__, **_) -> Never:
    """
    Qt's 'void QSpanData::initTexture(const QImage *image, int alpha,
    QTextureData::Type a2, const QRect &sourceRect)': leans on
    'QSpanData::adjustSpanMethods()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSpanData.initTexture' has no cute function yet. Qt's 'void "
        "QSpanData::initTexture(const QImage *image, int alpha, "
        "QTextureData::Type a2, const QRect &sourceRect)': leans on "
        "'QSpanData::adjustSpanMethods()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setup(*__, **_) -> Never:
    """
    Qt's 'void QSpanData::setup(const QBrush &brush, int alpha,
    QPainter::CompositionMode compositionMode, bool isCosmetic)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qt_gradient_cache'.
    """
    raise NotImplementedError(
        "'QSpanData.setup' has no cute function yet. Qt's 'void "
        "QSpanData::setup(const QBrush &brush, int alpha, "
        "QPainter::CompositionMode compositionMode, bool isCosmetic)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_gradient_cache'.")

  @staticmethod
  def setupMatrix(*__, **_) -> Never:
    """
    Qt's 'void QSpanData::setupMatrix(const QTransform &matrix, int
    bilinear)': leans on 'QSpanData::adjustSpanMethods()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QSpanData.setupMatrix' has no cute function yet. Qt's 'void "
        "QSpanData::setupMatrix(const QTransform &matrix, int bilinear)': "
        "leans on 'QSpanData::adjustSpanMethods()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
