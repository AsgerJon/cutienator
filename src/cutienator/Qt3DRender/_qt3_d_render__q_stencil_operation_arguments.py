"""
Qt3DRender::QStencilOperationArguments binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qstenciloperationarguments.h, Qt 6.12.0. Changes made here are
#  lost.
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


class QStencilOperationArguments(QObject):
  """
  The cute side of Qt's Qt3DRender::QStencilOperationArguments: a plain
  Python object standing in front of one C++
  Qt3DRender::QStencilOperationArguments.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::QStencilOperationArguments is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QStencilOperationArguments that has a
  ritual and that Python can call so far, 14 names in all: 'metaObject',
  'tr', 'faceMode', 'stencilTestFailureOperation',
  'depthTestFailureOperation', 'allTestsPassOperation',
  'setStencilTestFailureOperation', 'setDepthTestFailureOperation',
  'setAllTestsPassOperation', 'stencilTestFailureOperationChanged',
  'depthTestFailureOperationChanged', 'allTestsPassOperationChanged',
  'faceModeChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QStencilOperationArguments::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QStencilOperationArguments::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DRender::QStencilOperationArguments::~QStencilOperationArguments()':
    the destructor: Python never removes a C++
    Qt3DRender::QStencilOperationArguments.
  - Qt's 'const QStencilOperationArgumentsPrivate
    *Qt3DRender::QStencilOperationArguments::d_func() const': takes in Python
    what 'QStencilOperationArgumentsPrivate
    *Qt3DRender::QStencilOperationArguments::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QStencilOperationArguments is created at the first
    use, not by 'Qt3DRender::QStencilOperationArguments(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QStencilOperationArguments.
  - Qt tells when it has removed the C++
    Qt3DRender::QStencilOperationArguments. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QStencilOperationArguments, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class FaceMode(CuteNum):
    """
    The enum 'Qt3DRender::QStencilOperationArguments::FaceMode' of Qt, with
    the 3 names Qt gives in it.
    """

    Front = Kee[int](1028)
    Back = Kee[int](1029)
    FrontAndBack = Kee[int](1032)

  class Operation(CuteNum):
    """
    The enum 'Qt3DRender::QStencilOperationArguments::Operation' of Qt, with
    the 8 names Qt gives in it.
    """

    Zero = Kee[int](0)
    Keep = Kee[int](7680)
    Replace = Kee[int](7681)
    Increment = Kee[int](7682)
    Decrement = Kee[int](7683)
    IncrementWrap = Kee[int](34055)
    DecrementWrap = Kee[int](34056)
    Invert = Kee[int](5386)

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
    Calls Qt's 'QString Qt3DRender::QStencilOperationArguments::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html#tr

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
    #  QString Qt3DRender::QStencilOperationArguments::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QStencilOperationArguments'

  #  A C++ Qt3DRender::QStencilOperationArguments Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QStencilOperationArguments'

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
    *Qt3DRender::QStencilOperationArguments::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DRender::QStencilOperationArguments::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender26QStencilOperationArguments10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def faceMode(self) -> FaceMode:
    """
    Calls Qt's 'FaceMode Qt3DRender::QStencilOperationArguments::faceMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Returns
    -------

    FaceMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FaceMode(number)' gives.
    """
    #  FaceMode Qt3DRender::QStencilOperationArguments::faceMode() const
    return QStencilOperationArguments.FaceMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender26QStencilOperationArguments8faceModeEv',
    ))

  def stencilTestFailureOperation(self) -> Operation:
    """
    Calls Qt's 'Operation
    Qt3DRender::QStencilOperationArguments::stencilTestFailureOperation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation Qt3DRender::QStencilOperationArguments::
    #      stencilTestFailureOperation() const
    return QStencilOperationArguments.Operation(self.uglySide.call(
        'ritual_ZNK10Qt3DRender26QStencilOperationArguments27stencilTestFai'
        'lureOperationEv',
    ))

  def depthTestFailureOperation(self) -> Operation:
    """
    Calls Qt's 'Operation
    Qt3DRender::QStencilOperationArguments::depthTestFailureOperation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation
    #      Qt3DRender::QStencilOperationArguments::depthTestFailureOperation(
    #      ) const
    return QStencilOperationArguments.Operation(self.uglySide.call(
        'ritual_ZNK10Qt3DRender26QStencilOperationArguments25depthTestFailu'
        'reOperationEv',
    ))

  def allTestsPassOperation(self) -> Operation:
    """
    Calls Qt's 'Operation
    Qt3DRender::QStencilOperationArguments::allTestsPassOperation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation
    #      Qt3DRender::QStencilOperationArguments::allTestsPassOperation()
    #      const
    return QStencilOperationArguments.Operation(self.uglySide.call(
        'ritual_ZNK10Qt3DRender26QStencilOperationArguments21allTestsPassOp'
        'erationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Operation)
  def setStencilTestFailureOperation(self, operation: Operation) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilOperationArguments::setStencilTestFailureOperation(
    Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    operation : Operation
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::
    #      setStencilTestFailureOperation(Operation operation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments30setStencilTestF'
        'ailureOperationENS0_9OperationE',
        operation.value,
    )

  @overload(Operation)
  def setDepthTestFailureOperation(self, operation: Operation) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilOperationArguments::setDepthTestFailureOperation(
    Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    operation : Operation
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::
    #      setDepthTestFailureOperation(Operation operation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments28setDepthTestFai'
        'lureOperationENS0_9OperationE',
        operation.value,
    )

  @overload(Operation)
  def setAllTestsPassOperation(self, operation: Operation) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilOperationArguments::setAllTestsPassOperation(
    Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    operation : Operation
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::setAllTestsPassOperation(
    #      Operation operation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments24setAllTestsPass'
        'OperationENS0_9OperationE',
        operation.value,
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

  @overload(FaceMode)
  @overload(FaceMode, QObject)
  @overload(FaceMode, NoneType)
  def __init__(
      self,
      mode: FaceMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QStencilOperationArguments::QStencilOperationArguments(
    FaceMode mode, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    mode : FaceMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QStencilOperationArguments::
    #      QStencilOperationArguments(FaceMode mode, QObject *parent)
    self._noteCreation(QStencilOperationArguments, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArgumentsC1ENS0_8FaceModeE'
        'P7QObject',
        mode.value, self._addressOf(parent, 'QObject'),
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

  @overload(Operation)
  def stencilTestFailureOperationChanged(
      self,
      stencilFail: Operation,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QStencilOperationArguments::
    stencilTestFailureOperationChanged(Operation stencilFail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    stencilFail : Operation
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::
    #      stencilTestFailureOperationChanged(Operation stencilFail)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments34stencilTestFail'
        'ureOperationChangedENS0_9OperationE',
        stencilFail.value,
    )

  @overload(Operation)
  def depthTestFailureOperationChanged(self, depthFail: Operation) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilOperationArguments::depthTestFailureOperationChanged(
    Operation depthFail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    depthFail : Operation
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::
    #      depthTestFailureOperationChanged(Operation depthFail)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments32depthTestFailur'
        'eOperationChangedENS0_9OperationE',
        depthFail.value,
    )

  @overload(Operation)
  def allTestsPassOperationChanged(
      self,
      stencilDepthPass: Operation,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilOperationArguments::allTestsPassOperationChanged(
    Operation stencilDepthPass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    stencilDepthPass : Operation
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::
    #      allTestsPassOperationChanged(Operation stencilDepthPass)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments28allTestsPassOpe'
        'rationChangedENS0_9OperationE',
        stencilDepthPass.value,
    )

  @overload(FaceMode)
  def faceModeChanged(self, faceMode: FaceMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QStencilOperationArguments::faceModeChanged(FaceMode
    faceMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html

    Parameters
    ----------

    faceMode : FaceMode
      Passed on as its number.
    """
    #  void Qt3DRender::QStencilOperationArguments::faceModeChanged(FaceMode
    #      faceMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments15faceModeChanged'
        'ENS0_8FaceModeE',
        faceMode.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QStencilOperationArgumentsPrivate]:
    """
    Calls Qt's 'QStencilOperationArgumentsPrivate
    *Qt3DRender::QStencilOperationArguments::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciloperationarguments.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QStencilOperationArgumentsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStencilOperationArgumentsPrivate
    #      *Qt3DRender::QStencilOperationArguments::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender26QStencilOperationArguments6d_funcEv',
    )
    return Qt3DRender.QStencilOperationArgumentsPrivate._cuteAt(address)
