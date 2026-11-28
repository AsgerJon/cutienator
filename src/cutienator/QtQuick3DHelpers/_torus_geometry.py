"""
TorusGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/torusgeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means TorusGeometry to be private: it declares the class in a header it
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


class TorusGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's TorusGeometry: a plain Python object standing in
  front of one C++ TorusGeometry.

  What exists
  -----------

  Every function of Qt's TorusGeometry that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'rings', 'setRings',
  'segments', 'setSegments', 'radius', 'setRadius', 'tubeRadius',
  'setTubeRadius', 'asynchronous', 'setAsynchronous', 'status',
  'doUpdateGeometry', 'requestFinished', 'ringsChanged', 'segmentsChanged',
  'radiusChanged', 'tubeRadiusChanged', 'asynchronousChanged',
  'statusChanged', 'scheduleGeometryUpdate'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *TorusGeometry::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int TorusGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'TorusGeometry::~TorusGeometry()': the destructor: Python never
    removes a C++ TorusGeometry.
  - Qt's 'void TorusGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'TorusGeometry::GeometryData
    TorusGeometry::generateTorusGeometry(int rings, int segments, float
    radius, float tubeRadius)': gives a type Python has no way to take yet.
  - Qt's 'void
    TorusGeometry::generateTorusGeometryAsync(QPromise<TorusGeometry::
    GeometryData> &promise, int rings, int segments, float radius, float
    tubeRadius)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ TorusGeometry is created at the first use, not by
    'TorusGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ TorusGeometry.
  - Qt tells when it has removed the C++ TorusGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's TorusGeometry that has no cute function yet,
    'generateTorusGeometry', 'generateTorusGeometryAsync', 'updateGeometry',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside TorusGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'TorusGeometry::Status' of Qt, with the 4 names Qt gives in it.
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
    Calls Qt's 'QString TorusGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#tr

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
    #  QString TorusGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13TorusGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'TorusGeometry'

  #  A C++ TorusGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_TorusGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *TorusGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *TorusGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK13TorusGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rings(self) -> int:
    """
    Calls Qt's 'int TorusGeometry::rings() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#rings
    """
    #  int TorusGeometry::rings() const
    return self.uglySide.call('ritual_ZNK13TorusGeometry5ringsEv')

  def segments(self) -> int:
    """
    Calls Qt's 'int TorusGeometry::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#segments
    """
    #  int TorusGeometry::segments() const
    return self.uglySide.call('ritual_ZNK13TorusGeometry8segmentsEv')

  def radius(self) -> float:
    """
    Calls Qt's 'float TorusGeometry::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#radius
    """
    #  float TorusGeometry::radius() const
    return self.uglySide.call('ritual_ZNK13TorusGeometry6radiusEv')

  def tubeRadius(self) -> float:
    """
    Calls Qt's 'float TorusGeometry::tubeRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#tubeRadius
    """
    #  float TorusGeometry::tubeRadius() const
    return self.uglySide.call('ritual_ZNK13TorusGeometry10tubeRadiusEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool TorusGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#asynchronous
    """
    #  bool TorusGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK13TorusGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status TorusGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status TorusGeometry::status() const
    return TorusGeometry.Status(self.uglySide.call(
        'ritual_ZNK13TorusGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRings(self, newRings: int) -> None:
    """
    Calls Qt's 'void TorusGeometry::setRings(int newRings)'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#setRings

    Parameters
    ----------

    newRings : int
      Passed on as it is.
    """
    #  void TorusGeometry::setRings(int newRings)
    self.uglySide.call('ritual_ZN13TorusGeometry8setRingsEi', newRings)

  @overload(int)
  def setSegments(self, newSegments: int) -> None:
    """
    Calls Qt's 'void TorusGeometry::setSegments(int newSegments)'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#setSegments

    Parameters
    ----------

    newSegments : int
      Passed on as it is.
    """
    #  void TorusGeometry::setSegments(int newSegments)
    self.uglySide.call(
        'ritual_ZN13TorusGeometry11setSegmentsEi', newSegments,
    )

  @overload(float)
  def setRadius(self, newRadius: float) -> None:
    """
    Calls Qt's 'void TorusGeometry::setRadius(float newRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#setRadius

    Parameters
    ----------

    newRadius : float
      Passed on as it is.
    """
    #  void TorusGeometry::setRadius(float newRadius)
    self.uglySide.call('ritual_ZN13TorusGeometry9setRadiusEf', newRadius)

  @overload(float)
  def setTubeRadius(self, newTubeRadius: float) -> None:
    """
    Calls Qt's 'void TorusGeometry::setTubeRadius(float newTubeRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#setTubeRadius

    Parameters
    ----------

    newTubeRadius : float
      Passed on as it is.
    """
    #  void TorusGeometry::setTubeRadius(float newTubeRadius)
    self.uglySide.call(
        'ritual_ZN13TorusGeometry13setTubeRadiusEf', newTubeRadius,
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void TorusGeometry::setAsynchronous(bool newAsynchronous)'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void TorusGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN13TorusGeometry15setAsynchronousEb', newAsynchronous,
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
    'TorusGeometry::TorusGeometry(QQuick3DObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#TorusGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  TorusGeometry::TorusGeometry(QQuick3DObject *parent)
    self._noteCreation(TorusGeometry, lambda: Rituals.call(
        'ritual_ZN13TorusGeometryC1EP14QQuick3DObject',
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
    Calls Qt's 'void TorusGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/torusgeometry.html#doUpdateGeometry
    """
    #  void TorusGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN13TorusGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::requestFinished()'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#requestFinished
    """
    #  void TorusGeometry::requestFinished()
    self.uglySide.call('ritual_ZN13TorusGeometry15requestFinishedEv')

  def ringsChanged(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::ringsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#ringsChanged
    """
    #  void TorusGeometry::ringsChanged()
    self.uglySide.call('ritual_ZN13TorusGeometry12ringsChangedEv')

  def segmentsChanged(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::segmentsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#segmentsChanged
    """
    #  void TorusGeometry::segmentsChanged()
    self.uglySide.call('ritual_ZN13TorusGeometry15segmentsChangedEv')

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::radiusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#radiusChanged
    """
    #  void TorusGeometry::radiusChanged()
    self.uglySide.call('ritual_ZN13TorusGeometry13radiusChangedEv')

  def tubeRadiusChanged(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::tubeRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/torusgeometry.html#tubeRadiusChanged
    """
    #  void TorusGeometry::tubeRadiusChanged()
    self.uglySide.call('ritual_ZN13TorusGeometry17tubeRadiusChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/torusgeometry.html#asynchronousChanged
    """
    #  void TorusGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN13TorusGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/torusgeometry.html#statusChanged
    """
    #  void TorusGeometry::statusChanged()
    self.uglySide.call('ritual_ZN13TorusGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void TorusGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/torusgeometry.html#scheduleGeometryUpdate
    """
    #  void TorusGeometry::scheduleGeometryUpdate()
    self.uglySide.call('ritual_ZN13TorusGeometry22scheduleGeometryUpdateEv')

  @staticmethod
  def generateTorusGeometry(*__, **_) -> Never:
    """
    Qt's 'TorusGeometry::GeometryData
    TorusGeometry::generateTorusGeometry(int rings, int segments, float
    radius, float tubeRadius)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'TorusGeometry.generateTorusGeometry' has no cute function yet. "
        "Qt's 'TorusGeometry::GeometryData "
        "TorusGeometry::generateTorusGeometry(int rings, int segments, "
        "float radius, float tubeRadius)': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def generateTorusGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void
    TorusGeometry::generateTorusGeometryAsync(QPromise<TorusGeometry::
    GeometryData> &promise, int rings, int segments, float radius, float
    tubeRadius)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'TorusGeometry.generateTorusGeometryAsync' has no cute function "
        "yet. Qt's 'void "
        "TorusGeometry::generateTorusGeometryAsync(QPromise<TorusGeometry::G"
        "eometryData> &promise, int rings, int segments, float radius, "
        "float tubeRadius)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void TorusGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'TorusGeometry.updateGeometry' has no cute function yet. Qt's "
        "'void TorusGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
