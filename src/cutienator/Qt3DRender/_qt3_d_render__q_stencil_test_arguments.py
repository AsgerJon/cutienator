"""
Qt3DRender::QStencilTestArguments binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qstenciltestarguments.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStencilTestArguments(QObject):
  """
  The cute side of Qt's Qt3DRender::QStencilTestArguments: a plain Python
  object standing in front of one C++ Qt3DRender::QStencilTestArguments.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::QStencilTestArguments is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QStencilTestArguments that has a ritual
  and that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'comparisonMask', 'referenceValue', 'stencilFunction', 'faceMode',
  'setComparisonMask', 'setReferenceValue', 'setStencilFunction',
  'comparisonMaskChanged', 'stencilFunctionChanged', 'referenceValueChanged',
  'faceModeChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QStencilTestArguments::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QStencilTestArguments::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QStencilTestArguments::~QStencilTestArguments()': the
    destructor: Python never removes a C++ Qt3DRender::QStencilTestArguments.
  - Qt's 'const QStencilTestArgumentsPrivate
    *Qt3DRender::QStencilTestArguments::d_func() const': takes in Python what
    'QStencilTestArgumentsPrivate
    *Qt3DRender::QStencilTestArguments::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QStencilTestArguments is created at the first use,
    not by 'Qt3DRender::QStencilTestArguments(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QStencilTestArguments.
  - Qt tells when it has removed the C++ Qt3DRender::QStencilTestArguments.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QStencilTestArguments, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class StencilFaceMode(CuteNum):
    """
    The enum 'Qt3DRender::QStencilTestArguments::StencilFaceMode' of Qt, with
    the 3 names Qt gives in it.
    """

    Front = Kee[int](1028)
    Back = Kee[int](1029)
    FrontAndBack = Kee[int](1032)

  class StencilFunction(CuteNum):
    """
    The enum 'Qt3DRender::QStencilTestArguments::StencilFunction' of Qt, with
    the 8 names Qt gives in it.
    """

    Never = Kee[int](512)
    Always = Kee[int](519)
    Less = Kee[int](513)
    LessOrEqual = Kee[int](515)
    Equal = Kee[int](514)
    GreaterOrEqual = Kee[int](518)
    Greater = Kee[int](516)
    NotEqual = Kee[int](517)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QStencilTestArguments::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QStencilTestArguments::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QStencilTestArguments'

  #  A C++ Qt3DRender::QStencilTestArguments Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QStencilTestArguments'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::QStencilTestArguments::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QStencilTestArguments::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QStencilTestArguments10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def comparisonMask(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QStencilTestArguments::comparisonMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html
    """
    #  uint Qt3DRender::QStencilTestArguments::comparisonMask() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QStencilTestArguments14comparisonMaskEv',
    )

  def referenceValue(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QStencilTestArguments::referenceValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html
    """
    #  int Qt3DRender::QStencilTestArguments::referenceValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QStencilTestArguments14referenceValueEv',
    )

  def stencilFunction(self) -> StencilFunction:
    """
    Calls Qt's 'StencilFunction
    Qt3DRender::QStencilTestArguments::stencilFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Returns
    -------

    StencilFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StencilFunction(number)'
      gives.
    """
    #  StencilFunction Qt3DRender::QStencilTestArguments::stencilFunction()
    #      const
    return QStencilTestArguments.StencilFunction(self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QStencilTestArguments15stencilFunctionEv',
    ))

  def faceMode(self) -> StencilFaceMode:
    """
    Calls Qt's 'StencilFaceMode Qt3DRender::QStencilTestArguments::faceMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html#faceMode

    Returns
    -------

    StencilFaceMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StencilFaceMode(number)'
      gives.
    """
    #  StencilFaceMode Qt3DRender::QStencilTestArguments::faceMode() const
    return QStencilTestArguments.StencilFaceMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QStencilTestArguments8faceModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setComparisonMask(self, comparisonMask: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilTestArguments::setComparisonMask(uint
    comparisonMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    comparisonMask : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilTestArguments::setComparisonMask(uint
    #      comparisonMask)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments17setComparisonMaskEj',
        comparisonMask,
    )

  @overload(int)
  def setReferenceValue(self, referenceValue: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QStencilTestArguments::setReferenceValue(int
    referenceValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    referenceValue : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilTestArguments::setReferenceValue(int
    #      referenceValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments17setReferenceValueEi',
        referenceValue,
    )

  @overload(StencilFunction)
  def setStencilFunction(self, stencilFunction: StencilFunction) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilTestArguments::setStencilFunction(StencilFunction
    stencilFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    stencilFunction : StencilFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilTestArguments::setStencilFunction(
    #      StencilFunction stencilFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments18setStencilFunctionEN'
        'S0_15StencilFunctionE',
        stencilFunction.value,
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

  @overload(StencilFaceMode)
  @overload(StencilFaceMode, QObject)
  @overload(StencilFaceMode, NoneType)
  def __init__(
      self,
      face: StencilFaceMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QStencilTestArguments::QStencilTestArguments(StencilFaceMode
    face, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    face : StencilFaceMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QStencilTestArguments::QStencilTestArguments(
    #      StencilFaceMode face, QObject *parent)
    self._noteCreation(QStencilTestArguments, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21QStencilTestArgumentsC1ENS0_15StencilFaceMo'
        'deEP7QObject',
        face.value, self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def comparisonMaskChanged(self, comparisonMask: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilTestArguments::comparisonMaskChanged(uint
    comparisonMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    comparisonMask : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilTestArguments::comparisonMaskChanged(uint
    #      comparisonMask)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments21comparisonMaskChange'
        'dEj',
        comparisonMask,
    )

  @overload(StencilFunction)
  def stencilFunctionChanged(self, stencilFunction: StencilFunction) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilTestArguments::stencilFunctionChanged(StencilFunction
    stencilFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    stencilFunction : StencilFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilTestArguments::stencilFunctionChanged(
    #      StencilFunction stencilFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments22stencilFunctionChang'
        'edENS0_15StencilFunctionE',
        stencilFunction.value,
    )

  @overload(int)
  def referenceValueChanged(self, referenceValue: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilTestArguments::referenceValueChanged(int
    referenceValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    referenceValue : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilTestArguments::referenceValueChanged(int
    #      referenceValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments21referenceValueChange'
        'dEi',
        referenceValue,
    )

  @overload(StencilFaceMode)
  def faceModeChanged(self, faceMode: StencilFaceMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilTestArguments::faceModeChanged(StencilFaceMode
    faceMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html

    Parameters
    ----------

    faceMode : StencilFaceMode
      Passed on as its number.
    """
    #  void
    #      Qt3DRender::QStencilTestArguments::faceModeChanged(StencilFaceMode
    #      faceMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments15faceModeChangedENS0_'
        '15StencilFaceModeE',
        faceMode.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QStencilTestArgumentsPrivate]:
    """
    Calls Qt's 'QStencilTestArgumentsPrivate
    *Qt3DRender::QStencilTestArguments::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestarguments.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QStencilTestArgumentsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStencilTestArgumentsPrivate
    #      *Qt3DRender::QStencilTestArguments::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QStencilTestArguments6d_funcEv',
    )
    return Qt3DRender.QStencilTestArgumentsPrivate._cuteAt(address)
