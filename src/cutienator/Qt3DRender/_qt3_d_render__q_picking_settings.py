"""
Qt3DRender::QPickingSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qpickingsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPickingSettings(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QPickingSettings: a plain Python object
  standing in front of one C++ Qt3DRender::QPickingSettings.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::QPickingSettings is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPickingSettings that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'pickMethod', 'pickResultMode', 'faceOrientationPickingMode',
  'worldSpaceTolerance', 'setPickMethod', 'setPickResultMode',
  'setFaceOrientationPickingMode', 'setWorldSpaceTolerance',
  'pickMethodChanged', 'pickResultModeChanged',
  'faceOrientationPickingModeChanged', 'worldSpaceToleranceChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QPickingSettings::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QPickingSettings::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QPickingSettings::~QPickingSettings()': the destructor:
    Python never removes a C++ Qt3DRender::QPickingSettings.
  - Qt's 'const QPickingSettingsPrivate
    *Qt3DRender::QPickingSettings::d_func() const': takes in Python what
    'QPickingSettingsPrivate *Qt3DRender::QPickingSettings::d_func()' takes.
  - Qt's
    'Qt3DRender::QPickingSettings::QPickingSettings(QPickingSettingsPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QPickingSettings is created at the first use, not by
    'Qt3DRender::QPickingSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPickingSettings.
  - Qt tells when it has removed the C++ Qt3DRender::QPickingSettings. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QPickingSettings, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FaceOrientationPickingMode(CuteNum):
    """
    The enum 'Qt3DRender::QPickingSettings::FaceOrientationPickingMode' of
    Qt, with the 3 names Qt gives in it.
    """

    FrontFace = Kee[int](1)
    BackFace = Kee[int](2)
    FrontAndBackFace = Kee[int](3)

  class PickMethod(CuteNum):
    """
    The enum 'Qt3DRender::QPickingSettings::PickMethod' of Qt, with the 5
    names Qt gives in it.
    """

    BoundingVolumePicking = Kee[int](0)
    TrianglePicking = Kee[int](1)
    LinePicking = Kee[int](2)
    PointPicking = Kee[int](4)
    PrimitivePicking = Kee[int](7)

  class PickResultMode(CuteNum):
    """
    The enum 'Qt3DRender::QPickingSettings::PickResultMode' of Qt, with the 3
    names Qt gives in it.
    """

    NearestPick = Kee[int](0)
    AllPicks = Kee[int](1)
    NearestPriorityPick = Kee[int](2)

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
    Calls Qt's 'QString Qt3DRender::QPickingSettings::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#tr

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
    #  QString Qt3DRender::QPickingSettings::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QPickingSettings2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPickingSettings'

  #  A C++ Qt3DRender::QPickingSettings Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPickingSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QPickingSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QPickingSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QPickingSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pickMethod(self) -> PickMethod:
    """
    Calls Qt's 'PickMethod Qt3DRender::QPickingSettings::pickMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#pickMethod

    Returns
    -------

    PickMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PickMethod(number)'
      gives.
    """
    #  PickMethod Qt3DRender::QPickingSettings::pickMethod() const
    return QPickingSettings.PickMethod(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QPickingSettings10pickMethodEv',
    ))

  def pickResultMode(self) -> PickResultMode:
    """
    Calls Qt's 'PickResultMode Qt3DRender::QPickingSettings::pickResultMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#pickResultMode

    Returns
    -------

    PickResultMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PickResultMode(number)'
      gives.
    """
    #  PickResultMode Qt3DRender::QPickingSettings::pickResultMode() const
    return QPickingSettings.PickResultMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QPickingSettings14pickResultModeEv',
    ))

  def faceOrientationPickingMode(self) -> FaceOrientationPickingMode:
    """
    Calls Qt's 'FaceOrientationPickingMode
    Qt3DRender::QPickingSettings::faceOrientationPickingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html

    Returns
    -------

    FaceOrientationPickingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FaceOrientationPickingMode(number)' gives.
    """
    #  FaceOrientationPickingMode
    #      Qt3DRender::QPickingSettings::faceOrientationPickingMode() const
    return QPickingSettings.FaceOrientationPickingMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QPickingSettings26faceOrientationPickingMo'
        'deEv',
    ))

  def worldSpaceTolerance(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QPickingSettings::worldSpaceTolerance()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html
    """
    #  float Qt3DRender::QPickingSettings::worldSpaceTolerance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QPickingSettings19worldSpaceToleranceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PickMethod)
  def setPickMethod(self, pickMethod: PickMethod) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPickingSettings::setPickMethod(PickMethod
    pickMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#setPickMethod

    Parameters
    ----------

    pickMethod : PickMethod
      Passed on as its number.
    """
    #  void Qt3DRender::QPickingSettings::setPickMethod(PickMethod
    #      pickMethod)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings13setPickMethodENS0_10PickM'
        'ethodE',
        pickMethod.value,
    )

  @overload(PickResultMode)
  def setPickResultMode(self, pickResultMode: PickResultMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::setPickResultMode(PickResultMode
    pickResultMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#setPickResultMode

    Parameters
    ----------

    pickResultMode : PickResultMode
      Passed on as its number.
    """
    #  void Qt3DRender::QPickingSettings::setPickResultMode(PickResultMode
    #      pickResultMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings17setPickResultModeENS0_14P'
        'ickResultModeE',
        pickResultMode.value,
    )

  @overload(FaceOrientationPickingMode)
  def setFaceOrientationPickingMode(
      self,
      faceOrientationPickingMode: FaceOrientationPickingMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::setFaceOrientationPickingMode(
    FaceOrientationPickingMode faceOrientationPickingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html

    Parameters
    ----------

    faceOrientationPickingMode : FaceOrientationPickingMode
      Passed on as its number.
    """
    #  void Qt3DRender::QPickingSettings::setFaceOrientationPickingMode(
    #      FaceOrientationPickingMode faceOrientationPickingMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings29setFaceOrientationPicking'
        'ModeENS0_26FaceOrientationPickingModeE',
        faceOrientationPickingMode.value,
    )

  @overload(float)
  def setWorldSpaceTolerance(self, worldSpaceTolerance: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::setWorldSpaceTolerance(float
    worldSpaceTolerance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html

    Parameters
    ----------

    worldSpaceTolerance : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPickingSettings::setWorldSpaceTolerance(float
    #      worldSpaceTolerance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings22setWorldSpaceToleranceEf',
        worldSpaceTolerance,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QPickingSettings::QPickingSettings(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#QPickingSettings

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QPickingSettings::QPickingSettings(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QPickingSettings, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QPickingSettingsC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(PickMethod)
  def pickMethodChanged(self, pickMethod: PickMethod) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::pickMethodChanged(QPickingSettings::
    PickMethod pickMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#pickMethodChanged

    Parameters
    ----------

    pickMethod : PickMethod
      Passed on as its number.
    """
    #  void Qt3DRender::QPickingSettings::pickMethodChanged(
    #      QPickingSettings::PickMethod pickMethod)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings17pickMethodChangedENS0_10P'
        'ickMethodE',
        pickMethod.value,
    )

  @overload(PickResultMode)
  def pickResultModeChanged(self, pickResult: PickResultMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::pickResultModeChanged(QPickingSettings::
    PickResultMode pickResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html

    Parameters
    ----------

    pickResult : PickResultMode
      Passed on as its number.
    """
    #  void Qt3DRender::QPickingSettings::pickResultModeChanged(
    #      QPickingSettings::PickResultMode pickResult)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings21pickResultModeChangedENS0'
        '_14PickResultModeE',
        pickResult.value,
    )

  @overload(FaceOrientationPickingMode)
  def faceOrientationPickingModeChanged(
      self,
      faceOrientationPickingMode: FaceOrientationPickingMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::faceOrientationPickingModeChanged(
    QPickingSettings::FaceOrientationPickingMode
    faceOrientationPickingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html

    Parameters
    ----------

    faceOrientationPickingMode : FaceOrientationPickingMode
      Passed on as its number.
    """
    #  void Qt3DRender::QPickingSettings::faceOrientationPickingModeChanged(
    #      QPickingSettings::FaceOrientationPickingMode
    #      faceOrientationPickingMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings33faceOrientationPickingMod'
        'eChangedENS0_26FaceOrientationPickingModeE',
        faceOrientationPickingMode.value,
    )

  @overload(float)
  def worldSpaceToleranceChanged(self, worldSpaceTolerance: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPickingSettings::worldSpaceToleranceChanged(float
    worldSpaceTolerance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html

    Parameters
    ----------

    worldSpaceTolerance : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPickingSettings::worldSpaceToleranceChanged(float
    #      worldSpaceTolerance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings26worldSpaceToleranceChange'
        'dEf',
        worldSpaceTolerance,
    )

  def d_func(self) -> Optional[Qt3DRender.QPickingSettingsPrivate]:
    """
    Calls Qt's 'QPickingSettingsPrivate
    *Qt3DRender::QPickingSettings::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickingsettings.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QPickingSettingsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPickingSettingsPrivate *Qt3DRender::QPickingSettings::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender16QPickingSettings6d_funcEv',
    )
    return Qt3DRender.QPickingSettingsPrivate._cuteAt(address)
