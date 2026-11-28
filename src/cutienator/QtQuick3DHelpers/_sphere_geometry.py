"""
SphereGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/spheregeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means SphereGeometry to be private: it declares the class in a header
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


class SphereGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's SphereGeometry: a plain Python object standing in
  front of one C++ SphereGeometry.

  What exists
  -----------

  Every function of Qt's SphereGeometry that has a ritual and that Python can
  call so far, 19 names in all: 'metaObject', 'tr', 'radius', 'setRadius',
  'rings', 'setRings', 'segments', 'setSegments', 'asynchronous',
  'setAsynchronous', 'status', 'doUpdateGeometry', 'requestFinished',
  'radiusChanged', 'ringsChanged', 'segmentsChanged', 'asynchronousChanged',
  'statusChanged', 'scheduleGeometryUpdate'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *SphereGeometry::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int SphereGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'SphereGeometry::~SphereGeometry()': the destructor: Python never
    removes a C++ SphereGeometry.
  - Qt's 'void SphereGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'SphereGeometry::GeometryData
    SphereGeometry::generateSphereGeometry(float radius, int rings, int
    segments)': gives a type Python has no way to take yet.
  - Qt's 'void
    SphereGeometry::generateSphereGeometryAsync(QPromise<SphereGeometry::
    GeometryData> &promise, float radius, int rings, int segments)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ SphereGeometry is created at the first use, not by
    'SphereGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SphereGeometry.
  - Qt tells when it has removed the C++ SphereGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's SphereGeometry that has no cute function yet,
    'generateSphereGeometry', 'generateSphereGeometryAsync',
    'updateGeometry', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside SphereGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'SphereGeometry::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString SphereGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#tr

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
    #  QString SphereGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14SphereGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SphereGeometry'

  #  A C++ SphereGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SphereGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *SphereGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *SphereGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK14SphereGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'float SphereGeometry::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#radius
    """
    #  float SphereGeometry::radius() const
    return self.uglySide.call('ritual_ZNK14SphereGeometry6radiusEv')

  def rings(self) -> int:
    """
    Calls Qt's 'int SphereGeometry::rings() const'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#rings
    """
    #  int SphereGeometry::rings() const
    return self.uglySide.call('ritual_ZNK14SphereGeometry5ringsEv')

  def segments(self) -> int:
    """
    Calls Qt's 'int SphereGeometry::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#segments
    """
    #  int SphereGeometry::segments() const
    return self.uglySide.call('ritual_ZNK14SphereGeometry8segmentsEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool SphereGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#asynchronous
    """
    #  bool SphereGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK14SphereGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status SphereGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status SphereGeometry::status() const
    return SphereGeometry.Status(self.uglySide.call(
        'ritual_ZNK14SphereGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadius(self, newRadius: float) -> None:
    """
    Calls Qt's 'void SphereGeometry::setRadius(float newRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#setRadius

    Parameters
    ----------

    newRadius : float
      Passed on as it is.
    """
    #  void SphereGeometry::setRadius(float newRadius)
    self.uglySide.call('ritual_ZN14SphereGeometry9setRadiusEf', newRadius)

  @overload(int)
  def setRings(self, newRings: int) -> None:
    """
    Calls Qt's 'void SphereGeometry::setRings(int newRings)'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#setRings

    Parameters
    ----------

    newRings : int
      Passed on as it is.
    """
    #  void SphereGeometry::setRings(int newRings)
    self.uglySide.call('ritual_ZN14SphereGeometry8setRingsEi', newRings)

  @overload(int)
  def setSegments(self, newSegments: int) -> None:
    """
    Calls Qt's 'void SphereGeometry::setSegments(int newSegments)'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#setSegments

    Parameters
    ----------

    newSegments : int
      Passed on as it is.
    """
    #  void SphereGeometry::setSegments(int newSegments)
    self.uglySide.call(
        'ritual_ZN14SphereGeometry11setSegmentsEi', newSegments,
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void SphereGeometry::setAsynchronous(bool newAsynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/spheregeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void SphereGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN14SphereGeometry15setAsynchronousEb', newAsynchronous,
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
    'SphereGeometry::SphereGeometry(QQuick3DObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#SphereGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  SphereGeometry::SphereGeometry(QQuick3DObject *parent)
    self._noteCreation(SphereGeometry, lambda: Rituals.call(
        'ritual_ZN14SphereGeometryC1EP14QQuick3DObject',
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
    Calls Qt's 'void SphereGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/spheregeometry.html#doUpdateGeometry
    """
    #  void SphereGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN14SphereGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/spheregeometry.html#requestFinished
    """
    #  void SphereGeometry::requestFinished()
    self.uglySide.call('ritual_ZN14SphereGeometry15requestFinishedEv')

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::radiusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#radiusChanged
    """
    #  void SphereGeometry::radiusChanged()
    self.uglySide.call('ritual_ZN14SphereGeometry13radiusChangedEv')

  def ringsChanged(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::ringsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#ringsChanged
    """
    #  void SphereGeometry::ringsChanged()
    self.uglySide.call('ritual_ZN14SphereGeometry12ringsChangedEv')

  def segmentsChanged(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::segmentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/spheregeometry.html#segmentsChanged
    """
    #  void SphereGeometry::segmentsChanged()
    self.uglySide.call('ritual_ZN14SphereGeometry15segmentsChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/spheregeometry.html#asynchronousChanged
    """
    #  void SphereGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN14SphereGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/spheregeometry.html#statusChanged
    """
    #  void SphereGeometry::statusChanged()
    self.uglySide.call('ritual_ZN14SphereGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void SphereGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/spheregeometry.html#scheduleGeometryUpdate
    """
    #  void SphereGeometry::scheduleGeometryUpdate()
    self.uglySide.call('ritual_ZN14SphereGeometry22scheduleGeometryUpdateEv')

  @staticmethod
  def generateSphereGeometry(*__, **_) -> Never:
    """
    Qt's 'SphereGeometry::GeometryData
    SphereGeometry::generateSphereGeometry(float radius, int rings, int
    segments)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SphereGeometry.generateSphereGeometry' has no cute function yet. "
        "Qt's 'SphereGeometry::GeometryData "
        "SphereGeometry::generateSphereGeometry(float radius, int rings, "
        "int segments)': gives a type Python has no way to take yet.")

  @staticmethod
  def generateSphereGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void
    SphereGeometry::generateSphereGeometryAsync(QPromise<SphereGeometry::
    GeometryData> &promise, float radius, int rings, int segments)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'SphereGeometry.generateSphereGeometryAsync' has no cute function "
        "yet. Qt's 'void "
        "SphereGeometry::generateSphereGeometryAsync(QPromise<SphereGeometry"
        "::GeometryData> &promise, float radius, int rings, int segments)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void SphereGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'SphereGeometry.updateGeometry' has no cute function yet. Qt's "
        "'void SphereGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
