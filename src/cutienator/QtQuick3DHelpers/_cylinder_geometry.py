"""
CylinderGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/cylindergeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means CylinderGeometry to be private: it declares the class in a header
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


class CylinderGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's CylinderGeometry: a plain Python object standing in
  front of one C++ CylinderGeometry.

  What exists
  -----------

  Every function of Qt's CylinderGeometry that has a ritual and that Python
  can call so far, 22 names in all: 'metaObject', 'tr', 'radius',
  'setRadius', 'length', 'setLength', 'rings', 'setRings', 'segments',
  'setSegments', 'asynchronous', 'setAsynchronous', 'status',
  'doUpdateGeometry', 'requestFinished', 'radiusChanged', 'lengthChanged',
  'ringsChanged', 'segmentsChanged', 'asynchronousChanged', 'statusChanged',
  'scheduleGeometryUpdate'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CylinderGeometry::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int CylinderGeometry::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'CylinderGeometry::~CylinderGeometry()': the destructor: Python
    never removes a C++ CylinderGeometry.
  - Qt's 'void CylinderGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'CylinderGeometry::GeometryData
    CylinderGeometry::generateCylinderGeometry(float radius, float length,
    int rings, int slices)': gives a type Python has no way to take yet.
  - Qt's 'void CylinderGeometry::generateCylinderGeometryAsync(
    QPromise<CylinderGeometry::GeometryData> &promise, float radius, float
    length, int rings, int segments)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ CylinderGeometry is created at the first use, not by
    'CylinderGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CylinderGeometry.
  - Qt tells when it has removed the C++ CylinderGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's CylinderGeometry that has no cute function yet,
    'generateCylinderGeometry', 'generateCylinderGeometryAsync',
    'updateGeometry', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside CylinderGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'CylinderGeometry::Status' of Qt, with the 4 names Qt gives in
    it.
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
    Calls Qt's 'QString CylinderGeometry::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#tr

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
    #  QString CylinderGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16CylinderGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CylinderGeometry'

  #  A C++ CylinderGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CylinderGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CylinderGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CylinderGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16CylinderGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'float CylinderGeometry::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#radius
    """
    #  float CylinderGeometry::radius() const
    return self.uglySide.call('ritual_ZNK16CylinderGeometry6radiusEv')

  def length(self) -> float:
    """
    Calls Qt's 'float CylinderGeometry::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#length
    """
    #  float CylinderGeometry::length() const
    return self.uglySide.call('ritual_ZNK16CylinderGeometry6lengthEv')

  def rings(self) -> int:
    """
    Calls Qt's 'int CylinderGeometry::rings() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#rings
    """
    #  int CylinderGeometry::rings() const
    return self.uglySide.call('ritual_ZNK16CylinderGeometry5ringsEv')

  def segments(self) -> int:
    """
    Calls Qt's 'int CylinderGeometry::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#segments
    """
    #  int CylinderGeometry::segments() const
    return self.uglySide.call('ritual_ZNK16CylinderGeometry8segmentsEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool CylinderGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#asynchronous
    """
    #  bool CylinderGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK16CylinderGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status CylinderGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status CylinderGeometry::status() const
    return CylinderGeometry.Status(self.uglySide.call(
        'ritual_ZNK16CylinderGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadius(self, newRadius: float) -> None:
    """
    Calls Qt's 'void CylinderGeometry::setRadius(float newRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#setRadius

    Parameters
    ----------

    newRadius : float
      Passed on as it is.
    """
    #  void CylinderGeometry::setRadius(float newRadius)
    self.uglySide.call('ritual_ZN16CylinderGeometry9setRadiusEf', newRadius)

  @overload(float)
  def setLength(self, newLength: float) -> None:
    """
    Calls Qt's 'void CylinderGeometry::setLength(float newLength)'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#setLength

    Parameters
    ----------

    newLength : float
      Passed on as it is.
    """
    #  void CylinderGeometry::setLength(float newLength)
    self.uglySide.call('ritual_ZN16CylinderGeometry9setLengthEf', newLength)

  @overload(int)
  def setRings(self, newRings: int) -> None:
    """
    Calls Qt's 'void CylinderGeometry::setRings(int newRings)'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#setRings

    Parameters
    ----------

    newRings : int
      Passed on as it is.
    """
    #  void CylinderGeometry::setRings(int newRings)
    self.uglySide.call('ritual_ZN16CylinderGeometry8setRingsEi', newRings)

  @overload(int)
  def setSegments(self, newSegments: int) -> None:
    """
    Calls Qt's 'void CylinderGeometry::setSegments(int newSegments)'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#setSegments

    Parameters
    ----------

    newSegments : int
      Passed on as it is.
    """
    #  void CylinderGeometry::setSegments(int newSegments)
    self.uglySide.call(
        'ritual_ZN16CylinderGeometry11setSegmentsEi', newSegments,
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void CylinderGeometry::setAsynchronous(bool
    newAsynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void CylinderGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN16CylinderGeometry15setAsynchronousEb', newAsynchronous,
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
    'CylinderGeometry::CylinderGeometry(QQuick3DObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#CylinderGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  CylinderGeometry::CylinderGeometry(QQuick3DObject *parent)
    self._noteCreation(CylinderGeometry, lambda: Rituals.call(
        'ritual_ZN16CylinderGeometryC1EP14QQuick3DObject',
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
    Calls Qt's 'void CylinderGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#doUpdateGeometry
    """
    #  void CylinderGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN16CylinderGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#requestFinished
    """
    #  void CylinderGeometry::requestFinished()
    self.uglySide.call('ritual_ZN16CylinderGeometry15requestFinishedEv')

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#radiusChanged
    """
    #  void CylinderGeometry::radiusChanged()
    self.uglySide.call('ritual_ZN16CylinderGeometry13radiusChangedEv')

  def lengthChanged(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::lengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#lengthChanged
    """
    #  void CylinderGeometry::lengthChanged()
    self.uglySide.call('ritual_ZN16CylinderGeometry13lengthChangedEv')

  def ringsChanged(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::ringsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/cylindergeometry.html#ringsChanged
    """
    #  void CylinderGeometry::ringsChanged()
    self.uglySide.call('ritual_ZN16CylinderGeometry12ringsChangedEv')

  def segmentsChanged(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::segmentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#segmentsChanged
    """
    #  void CylinderGeometry::segmentsChanged()
    self.uglySide.call('ritual_ZN16CylinderGeometry15segmentsChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#asynchronousChanged
    """
    #  void CylinderGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN16CylinderGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#statusChanged
    """
    #  void CylinderGeometry::statusChanged()
    self.uglySide.call('ritual_ZN16CylinderGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void CylinderGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cylindergeometry.html#scheduleGeometryUpdate
    """
    #  void CylinderGeometry::scheduleGeometryUpdate()
    self.uglySide.call(
        'ritual_ZN16CylinderGeometry22scheduleGeometryUpdateEv',
    )

  @staticmethod
  def generateCylinderGeometry(*__, **_) -> Never:
    """
    Qt's 'CylinderGeometry::GeometryData
    CylinderGeometry::generateCylinderGeometry(float radius, float length,
    int rings, int slices)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'CylinderGeometry.generateCylinderGeometry' has no cute function "
        "yet. Qt's 'CylinderGeometry::GeometryData "
        "CylinderGeometry::generateCylinderGeometry(float radius, float "
        "length, int rings, int slices)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def generateCylinderGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void CylinderGeometry::generateCylinderGeometryAsync(
    QPromise<CylinderGeometry::GeometryData> &promise, float radius, float
    length, int rings, int segments)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'CylinderGeometry.generateCylinderGeometryAsync' has no cute "
        "function yet. Qt's 'void "
        "CylinderGeometry::generateCylinderGeometryAsync(QPromise<CylinderGe"
        "ometry::GeometryData> &promise, float radius, float length, int "
        "rings, int segments)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void CylinderGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'CylinderGeometry.updateGeometry' has no cute function yet. Qt's "
        "'void CylinderGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
