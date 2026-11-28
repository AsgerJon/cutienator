"""
CapsuleGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/capsulegeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means CapsuleGeometry to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3D import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DObject = WAIT['QQuick3DObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CapsuleGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's CapsuleGeometry: a plain Python object standing in
  front of one C++ CapsuleGeometry.

  What exists
  -----------

  Every function of Qt's CapsuleGeometry that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'enableNormals',
  'setEnableNormals', 'enableUV', 'setEnableUV', 'longitudes',
  'setLongitudes', 'latitudes', 'setLatitudes', 'rings', 'setRings',
  'height', 'setHeight', 'diameter', 'setDiameter', 'uvProfile',
  'setUVProfile', 'asynchronous', 'setAsynchronous', 'status',
  'doUpdateGeometry', 'requestFinished', 'enableNormalsChanged',
  'enableUVChanged', 'longitudesChanged', 'latitudesChanged', 'ringsChanged',
  'heightChanged', 'diameterChanged', 'uvProfileChanged',
  'asynchronousChanged', 'statusChanged', 'scheduleGeometryUpdate'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CapsuleGeometry::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int CapsuleGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'CapsuleGeometry::~CapsuleGeometry()': the destructor: Python never
    removes a C++ CapsuleGeometry.
  - Qt's 'void CapsuleGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'CapsuleGeometry::GeometryData
    CapsuleGeometry::generateCapsuleGeometry(bool enableNormals, bool
    enableUV, int longitudes, int latitudes, int rings, float height, float
    diameter, UVProfile uvProfile)': gives a type Python has no way to take
    yet.
  - Qt's 'void
    CapsuleGeometry::generateCapsuleGeometryAsync(QPromise<CapsuleGeometry::
    GeometryData> &promise, bool enableNormals, bool enableUV, int
    longitudes, int latitudes, int rings, float height, float diameter,
    UVProfile uvProfile)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 44 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ CapsuleGeometry is created at the first use, not by
    'CapsuleGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CapsuleGeometry.
  - Qt tells when it has removed the C++ CapsuleGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's CapsuleGeometry that has no cute function yet,
    'generateCapsuleGeometry', 'generateCapsuleGeometryAsync',
    'updateGeometry', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside CapsuleGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'CapsuleGeometry::Status' of Qt, with the 4 names Qt gives in
    it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

  class UVProfile(CuteNum):
    """
    The enum 'CapsuleGeometry::UVProfile' of Qt, with the 3 names Qt gives in
    it.
    """

    Fixed = Kee[int](0)
    Aspect = Kee[int](1)
    Uniform = Kee[int](2)

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
    Calls Qt's 'QString CapsuleGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#tr

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
    #  QString CapsuleGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15CapsuleGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CapsuleGeometry'

  #  A C++ CapsuleGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CapsuleGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CapsuleGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CapsuleGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK15CapsuleGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enableNormals(self) -> bool:
    """
    Calls Qt's 'bool CapsuleGeometry::enableNormals() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#enableNormals
    """
    #  bool CapsuleGeometry::enableNormals() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry13enableNormalsEv')

  def enableUV(self) -> bool:
    """
    Calls Qt's 'bool CapsuleGeometry::enableUV() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#enableUV
    """
    #  bool CapsuleGeometry::enableUV() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry8enableUVEv')

  def longitudes(self) -> int:
    """
    Calls Qt's 'int CapsuleGeometry::longitudes() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#longitudes
    """
    #  int CapsuleGeometry::longitudes() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry10longitudesEv')

  def latitudes(self) -> int:
    """
    Calls Qt's 'int CapsuleGeometry::latitudes() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#latitudes
    """
    #  int CapsuleGeometry::latitudes() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry9latitudesEv')

  def rings(self) -> int:
    """
    Calls Qt's 'int CapsuleGeometry::rings() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#rings
    """
    #  int CapsuleGeometry::rings() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry5ringsEv')

  def height(self) -> float:
    """
    Calls Qt's 'float CapsuleGeometry::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#height
    """
    #  float CapsuleGeometry::height() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry6heightEv')

  def diameter(self) -> float:
    """
    Calls Qt's 'float CapsuleGeometry::diameter() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#diameter
    """
    #  float CapsuleGeometry::diameter() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry8diameterEv')

  def uvProfile(self) -> UVProfile:
    """
    Calls Qt's 'UVProfile CapsuleGeometry::uvProfile() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#uvProfile

    Returns
    -------

    UVProfile
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UVProfile(number)' gives.
    """
    #  UVProfile CapsuleGeometry::uvProfile() const
    return CapsuleGeometry.UVProfile(self.uglySide.call(
        'ritual_ZNK15CapsuleGeometry9uvProfileEv',
    ))

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool CapsuleGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#asynchronous
    """
    #  bool CapsuleGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK15CapsuleGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status CapsuleGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status CapsuleGeometry::status() const
    return CapsuleGeometry.Status(self.uglySide.call(
        'ritual_ZNK15CapsuleGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnableNormals(self, enable: bool) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setEnableNormals(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#setEnableNormals

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void CapsuleGeometry::setEnableNormals(bool enable)
    self.uglySide.call(
        'ritual_ZN15CapsuleGeometry16setEnableNormalsEb', enable,
    )

  @overload(bool)
  def setEnableUV(self, enable: bool) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setEnableUV(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setEnableUV

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void CapsuleGeometry::setEnableUV(bool enable)
    self.uglySide.call('ritual_ZN15CapsuleGeometry11setEnableUVEb', enable)

  @overload(int)
  def setLongitudes(self, longitudes: int) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setLongitudes(int longitudes)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setLongitudes

    Parameters
    ----------

    longitudes : int
      Passed on as it is.
    """
    #  void CapsuleGeometry::setLongitudes(int longitudes)
    self.uglySide.call(
        'ritual_ZN15CapsuleGeometry13setLongitudesEi', longitudes,
    )

  @overload(int)
  def setLatitudes(self, latitudes: int) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setLatitudes(int latitudes)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setLatitudes

    Parameters
    ----------

    latitudes : int
      Passed on as it is.
    """
    #  void CapsuleGeometry::setLatitudes(int latitudes)
    self.uglySide.call(
        'ritual_ZN15CapsuleGeometry12setLatitudesEi', latitudes,
    )

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setRings(int rings)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void CapsuleGeometry::setRings(int rings)
    self.uglySide.call('ritual_ZN15CapsuleGeometry8setRingsEi', rings)

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setHeight(float height)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void CapsuleGeometry::setHeight(float height)
    self.uglySide.call('ritual_ZN15CapsuleGeometry9setHeightEf', height)

  @overload(float)
  def setDiameter(self, diameter: float) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setDiameter(float diameter)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setDiameter

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void CapsuleGeometry::setDiameter(float diameter)
    self.uglySide.call('ritual_ZN15CapsuleGeometry11setDiameterEf', diameter)

  @overload(UVProfile)
  def setUVProfile(self, newUVProfile: UVProfile) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setUVProfile(UVProfile newUVProfile)'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#setUVProfile

    Parameters
    ----------

    newUVProfile : UVProfile
      Passed on as its number.
    """
    #  void CapsuleGeometry::setUVProfile(UVProfile newUVProfile)
    self.uglySide.call(
        'ritual_ZN15CapsuleGeometry12setUVProfileENS_9UVProfileE',
        newUVProfile.value,
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::setAsynchronous(bool newAsynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void CapsuleGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN15CapsuleGeometry15setAsynchronousEb', newAsynchronous,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'CapsuleGeometry::CapsuleGeometry(QQuick3DObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#CapsuleGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  CapsuleGeometry::CapsuleGeometry(QQuick3DObject *parent)
    self._noteCreation(CapsuleGeometry, lambda: Rituals.call(
        'ritual_ZN15CapsuleGeometryC1EP14QQuick3DObject',
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

  def doUpdateGeometry(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#doUpdateGeometry
    """
    #  void CapsuleGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN15CapsuleGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#requestFinished
    """
    #  void CapsuleGeometry::requestFinished()
    self.uglySide.call('ritual_ZN15CapsuleGeometry15requestFinishedEv')

  def enableNormalsChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::enableNormalsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#enableNormalsChanged
    """
    #  void CapsuleGeometry::enableNormalsChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry20enableNormalsChangedEv')

  def enableUVChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::enableUVChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#enableUVChanged
    """
    #  void CapsuleGeometry::enableUVChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry15enableUVChangedEv')

  def longitudesChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::longitudesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#longitudesChanged
    """
    #  void CapsuleGeometry::longitudesChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry17longitudesChangedEv')

  def latitudesChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::latitudesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#latitudesChanged
    """
    #  void CapsuleGeometry::latitudesChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry16latitudesChangedEv')

  def ringsChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::ringsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#ringsChanged
    """
    #  void CapsuleGeometry::ringsChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry12ringsChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::heightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#heightChanged
    """
    #  void CapsuleGeometry::heightChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry13heightChangedEv')

  def diameterChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::diameterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#diameterChanged
    """
    #  void CapsuleGeometry::diameterChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry15diameterChangedEv')

  def uvProfileChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::uvProfileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#uvProfileChanged
    """
    #  void CapsuleGeometry::uvProfileChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry16uvProfileChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#asynchronousChanged
    """
    #  void CapsuleGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/capsulegeometry.html#statusChanged
    """
    #  void CapsuleGeometry::statusChanged()
    self.uglySide.call('ritual_ZN15CapsuleGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void CapsuleGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/capsulegeometry.html#scheduleGeometryUpdate
    """
    #  void CapsuleGeometry::scheduleGeometryUpdate()
    self.uglySide.call(
        'ritual_ZN15CapsuleGeometry22scheduleGeometryUpdateEv',
    )

  @staticmethod
  def generateCapsuleGeometry(*__, **_) -> Never:
    """
    Qt's 'CapsuleGeometry::GeometryData
    CapsuleGeometry::generateCapsuleGeometry(bool enableNormals, bool
    enableUV, int longitudes, int latitudes, int rings, float height, float
    diameter, UVProfile uvProfile)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'CapsuleGeometry.generateCapsuleGeometry' has no cute function "
        "yet. Qt's 'CapsuleGeometry::GeometryData "
        "CapsuleGeometry::generateCapsuleGeometry(bool enableNormals, bool "
        "enableUV, int longitudes, int latitudes, int rings, float height, "
        "float diameter, UVProfile uvProfile)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def generateCapsuleGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void
    CapsuleGeometry::generateCapsuleGeometryAsync(QPromise<CapsuleGeometry::
    GeometryData> &promise, bool enableNormals, bool enableUV, int
    longitudes, int latitudes, int rings, float height, float diameter,
    UVProfile uvProfile)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'CapsuleGeometry.generateCapsuleGeometryAsync' has no cute "
        "function yet. Qt's 'void "
        "CapsuleGeometry::generateCapsuleGeometryAsync(QPromise<CapsuleGeome"
        "try::GeometryData> &promise, bool enableNormals, bool enableUV, "
        "int longitudes, int latitudes, int rings, float height, float "
        "diameter, UVProfile uvProfile)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void CapsuleGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'CapsuleGeometry.updateGeometry' has no cute function yet. Qt's "
        "'void CapsuleGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
