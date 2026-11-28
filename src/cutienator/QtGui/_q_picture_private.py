"""
QPicturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpicture_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPicturePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPicturePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPicturePrivate: a plain Python object standing in
  front of one C++ QPicturePrivate.

  C++ hands a QPicturePrivate around as a copy, so every C++ QPicturePrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QPicturePrivate yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPicturePrivate::~QPicturePrivate()': the destructor: Python
    removes its C++ QPicturePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 2 written with the class 'QPicture',
  which declares it as well and stands first in it; 1 Qt's library has no
  name for it, and its code in Qt's source does not compile apart from its
  file; 1 leans on 'qt_mfhdr_tag', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QPicturePrivate is created at the first use, not by
    'QPicturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPicturePrivate back gives a copy the ritual made for
    Python, in a new cute QPicturePrivate.
  - Each name of Qt's QPicturePrivate that has no cute function yet,
    'checkFormat', 'resetFormat', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPicturePrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PaintCommand(CuteNum):
    """
    The enum 'QPicturePrivate::PaintCommand' of Qt, with the 59 names Qt
    gives in it.
    """

    PdcNOP = Kee[int](0)
    PdcDrawPoint = Kee[int](1)
    PdcDrawFirst = Kee[int](1)
    PdcMoveTo = Kee[int](2)
    PdcLineTo = Kee[int](3)
    PdcDrawLine = Kee[int](4)
    PdcDrawRect = Kee[int](5)
    PdcDrawRoundRect = Kee[int](6)
    PdcDrawEllipse = Kee[int](7)
    PdcDrawArc = Kee[int](8)
    PdcDrawPie = Kee[int](9)
    PdcDrawChord = Kee[int](10)
    PdcDrawLineSegments = Kee[int](11)
    PdcDrawPolyline = Kee[int](12)
    PdcDrawPolygon = Kee[int](13)
    PdcDrawCubicBezier = Kee[int](14)
    PdcDrawText = Kee[int](15)
    PdcDrawTextFormatted = Kee[int](16)
    PdcDrawPixmap = Kee[int](17)
    PdcDrawImage = Kee[int](18)
    PdcDrawText2 = Kee[int](19)
    PdcDrawText2Formatted = Kee[int](20)
    PdcDrawTextItem = Kee[int](21)
    PdcDrawLast = Kee[int](21)
    PdcDrawPoints = Kee[int](22)
    PdcDrawWinFocusRect = Kee[int](23)
    PdcDrawTiledPixmap = Kee[int](24)
    PdcDrawPath = Kee[int](25)
    PdcBegin = Kee[int](30)
    PdcEnd = Kee[int](31)
    PdcSave = Kee[int](32)
    PdcRestore = Kee[int](33)
    PdcSetdev = Kee[int](34)
    PdcSetBkColor = Kee[int](40)
    PdcSetBkMode = Kee[int](41)
    PdcSetROP = Kee[int](42)
    PdcSetBrushOrigin = Kee[int](43)
    PdcSetFont = Kee[int](45)
    PdcSetPen = Kee[int](46)
    PdcSetBrush = Kee[int](47)
    PdcSetTabStops = Kee[int](48)
    PdcSetTabArray = Kee[int](49)
    PdcSetUnit = Kee[int](50)
    PdcSetVXform = Kee[int](51)
    PdcSetWindow = Kee[int](52)
    PdcSetViewport = Kee[int](53)
    PdcSetWXform = Kee[int](54)
    PdcSetWMatrix = Kee[int](55)
    PdcSaveWMatrix = Kee[int](56)
    PdcRestoreWMatrix = Kee[int](57)
    PdcSetClip = Kee[int](60)
    PdcSetClipRegion = Kee[int](61)
    PdcSetClipPath = Kee[int](62)
    PdcSetRenderHint = Kee[int](63)
    PdcSetCompositionMode = Kee[int](64)
    PdcSetClipEnabled = Kee[int](65)
    PdcSetOpacity = Kee[int](66)
    PdcReservedStart = Kee[int](0)
    PdcReservedStop = Kee[int](199)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPicturePrivate'

  #  Qt's '~QPicturePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QPicturePrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QPicturePrivateD1Ev'

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
    Notes what was given, for Qt's 'QPicturePrivate::QPicturePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpictureprivate.html#QPicturePrivate
    """
    #  QPicturePrivate::QPicturePrivate()
    self._noteCreation(QPicturePrivate, lambda: Rituals.call(
        'ritual_ZN15QPicturePrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPicturePrivate) -> None:
    """
    Notes what was given, for Qt's 'QPicturePrivate::QPicturePrivate(const
    QPicturePrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpictureprivate.html#QPicturePrivate

    Parameters
    ----------

    other : QPicturePrivate
      Passed on as a value: Qt reads the C++ QPicturePrivate, which stays
      Python's own.
    """
    #  QPicturePrivate::QPicturePrivate(const QPicturePrivate &other)
    self._noteCreation(QPicturePrivate, lambda: Rituals.call(
        'ritual_ZN15QPicturePrivateC1ERKS_', self._valueOf(other),
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
  def checkFormat(*__, **_) -> Never:
    """
    Qt's 'bool QPicturePrivate::checkFormat()': leans on 'qt_mfhdr_tag',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QPicturePrivate.checkFormat' has no cute function yet. Qt's 'bool "
        "QPicturePrivate::checkFormat()': leans on 'qt_mfhdr_tag', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resetFormat(*__, **_) -> Never:
    """
    Qt's 'void QPicturePrivate::resetFormat()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'mfhdr_maj'.
    """
    raise NotImplementedError(
        "'QPicturePrivate.resetFormat' has no cute function yet. Qt's 'void "
        "QPicturePrivate::resetFormat()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'mfhdr_maj'.")
