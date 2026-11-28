"""
PlaneGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/planegeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means PlaneGeometry to be private: it declares the class in a header it
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

  from ..QtCore import QMetaObject, QSize
  from ..QtQuick3D import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DObject = WAIT['QQuick3DObject']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PlaneGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's PlaneGeometry: a plain Python object standing in
  front of one C++ PlaneGeometry.

  What exists
  -----------

  Every function of Qt's PlaneGeometry that has a ritual and that Python can
  call so far, 28 names in all: 'metaObject', 'tr', 'width', 'setWidth',
  'height', 'setHeight', 'meshResolution', 'setMeshResolution', 'plane',
  'setPlane', 'mirrored', 'setMirrored', 'asynchronous', 'setAsynchronous',
  'status', 'reversed', 'setReversed', 'doUpdateGeometry', 'requestFinished',
  'widthChanged', 'heightChanged', 'meshResolutionChanged', 'planeChanged',
  'mirroredChanged', 'asynchronousChanged', 'statusChanged',
  'reversedChanged', 'scheduleGeometryUpdate'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PlaneGeometry::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PlaneGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PlaneGeometry::~PlaneGeometry()': the destructor: Python never
    removes a C++ PlaneGeometry.
  - Qt's 'void PlaneGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'PlaneGeometry::GeometryData
    PlaneGeometry::generatePlaneGeometry(float width, float height, QSize
    meshResolution, Plane plane, bool reversed, bool mirrored)': gives a type
    Python has no way to take yet.
  - Qt's 'void
    PlaneGeometry::generatePlaneGeometryAsync(QPromise<PlaneGeometry::
    GeometryData> &promise, float width, float height, QSize meshResolution,
    Plane plane, bool reversed, bool mirrored)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PlaneGeometry is created at the first use, not by
    'PlaneGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PlaneGeometry.
  - Qt tells when it has removed the C++ PlaneGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's PlaneGeometry that has no cute function yet,
    'generatePlaneGeometry', 'generatePlaneGeometryAsync', 'updateGeometry',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside PlaneGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Plane(CuteNum):
    """
    The enum 'PlaneGeometry::Plane' of Qt, with the 3 names Qt gives in it.
    """

    XY = Kee[int](0)
    XZ = Kee[int](1)
    ZY = Kee[int](2)

  class Status(CuteNum):
    """
    The enum 'PlaneGeometry::Status' of Qt, with the 4 names Qt gives in it.
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
    Calls Qt's 'QString PlaneGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#tr

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
    #  QString PlaneGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13PlaneGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PlaneGeometry'

  #  A C++ PlaneGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PlaneGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PlaneGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PlaneGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK13PlaneGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'float PlaneGeometry::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#width
    """
    #  float PlaneGeometry::width() const
    return self.uglySide.call('ritual_ZNK13PlaneGeometry5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'float PlaneGeometry::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#height
    """
    #  float PlaneGeometry::height() const
    return self.uglySide.call('ritual_ZNK13PlaneGeometry6heightEv')

  def meshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize PlaneGeometry::meshResolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#meshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize PlaneGeometry::meshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK13PlaneGeometry14meshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def plane(self) -> Plane:
    """
    Calls Qt's 'Plane PlaneGeometry::plane() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#plane

    Returns
    -------

    Plane
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Plane(number)' gives.
    """
    #  Plane PlaneGeometry::plane() const
    return PlaneGeometry.Plane(self.uglySide.call(
        'ritual_ZNK13PlaneGeometry5planeEv',
    ))

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool PlaneGeometry::mirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#mirrored
    """
    #  bool PlaneGeometry::mirrored() const
    return self.uglySide.call('ritual_ZNK13PlaneGeometry8mirroredEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool PlaneGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#asynchronous
    """
    #  bool PlaneGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK13PlaneGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status PlaneGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status PlaneGeometry::status() const
    return PlaneGeometry.Status(self.uglySide.call(
        'ritual_ZNK13PlaneGeometry6statusEv',
    ))

  def reversed(self) -> bool:
    """
    Calls Qt's 'bool PlaneGeometry::reversed() const'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#reversed
    """
    #  bool PlaneGeometry::reversed() const
    return self.uglySide.call('ritual_ZNK13PlaneGeometry8reversedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, newWidth: float) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setWidth(float newWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#setWidth

    Parameters
    ----------

    newWidth : float
      Passed on as it is.
    """
    #  void PlaneGeometry::setWidth(float newWidth)
    self.uglySide.call('ritual_ZN13PlaneGeometry8setWidthEf', newWidth)

  @overload(float)
  def setHeight(self, newHeight: float) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setHeight(float newHeight)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#setHeight

    Parameters
    ----------

    newHeight : float
      Passed on as it is.
    """
    #  void PlaneGeometry::setHeight(float newHeight)
    self.uglySide.call('ritual_ZN13PlaneGeometry9setHeightEf', newHeight)

  @overload(QSize)
  def setMeshResolution(self, newMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setMeshResolution(const QSize
    &newMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/planegeometry.html#setMeshResolution

    Parameters
    ----------

    newMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void PlaneGeometry::setMeshResolution(const QSize &newMeshResolution)
    self.uglySide.call(
        'ritual_ZN13PlaneGeometry17setMeshResolutionERK5QSize',
        self._valueOf(newMeshResolution),
    )

  @overload(Plane)
  def setPlane(self, newPlane: Plane) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setPlane(Plane newPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#setPlane

    Parameters
    ----------

    newPlane : Plane
      Passed on as its number.
    """
    #  void PlaneGeometry::setPlane(Plane newPlane)
    self.uglySide.call(
        'ritual_ZN13PlaneGeometry8setPlaneENS_5PlaneE', newPlane.value,
    )

  @overload(bool)
  def setMirrored(self, newMirrored: bool) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setMirrored(bool newMirrored)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#setMirrored

    Parameters
    ----------

    newMirrored : bool
      Passed on as it is.
    """
    #  void PlaneGeometry::setMirrored(bool newMirrored)
    self.uglySide.call(
        'ritual_ZN13PlaneGeometry11setMirroredEb', newMirrored,
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setAsynchronous(bool newAsynchronous)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void PlaneGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN13PlaneGeometry15setAsynchronousEb', newAsynchronous,
    )

  @overload(bool)
  def setReversed(self, newReversed: bool) -> None:
    """
    Calls Qt's 'void PlaneGeometry::setReversed(bool newReversed)'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#setReversed

    Parameters
    ----------

    newReversed : bool
      Passed on as it is.
    """
    #  void PlaneGeometry::setReversed(bool newReversed)
    self.uglySide.call(
        'ritual_ZN13PlaneGeometry11setReversedEb', newReversed,
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
    'PlaneGeometry::PlaneGeometry(QQuick3DObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#PlaneGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  PlaneGeometry::PlaneGeometry(QQuick3DObject *parent)
    self._noteCreation(PlaneGeometry, lambda: Rituals.call(
        'ritual_ZN13PlaneGeometryC1EP14QQuick3DObject',
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
    Calls Qt's 'void PlaneGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/planegeometry.html#doUpdateGeometry
    """
    #  void PlaneGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN13PlaneGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::requestFinished()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#requestFinished
    """
    #  void PlaneGeometry::requestFinished()
    self.uglySide.call('ritual_ZN13PlaneGeometry15requestFinishedEv')

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#widthChanged
    """
    #  void PlaneGeometry::widthChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::heightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#heightChanged
    """
    #  void PlaneGeometry::heightChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry13heightChangedEv')

  def meshResolutionChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::meshResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/planegeometry.html#meshResolutionChanged
    """
    #  void PlaneGeometry::meshResolutionChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry21meshResolutionChangedEv')

  def planeChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::planeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#planeChanged
    """
    #  void PlaneGeometry::planeChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry12planeChangedEv')

  def mirroredChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::mirroredChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#mirroredChanged
    """
    #  void PlaneGeometry::mirroredChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry15mirroredChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/planegeometry.html#asynchronousChanged
    """
    #  void PlaneGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#statusChanged
    """
    #  void PlaneGeometry::statusChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry13statusChangedEv')

  def reversedChanged(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::reversedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/planegeometry.html#reversedChanged
    """
    #  void PlaneGeometry::reversedChanged()
    self.uglySide.call('ritual_ZN13PlaneGeometry15reversedChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void PlaneGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/planegeometry.html#scheduleGeometryUpdate
    """
    #  void PlaneGeometry::scheduleGeometryUpdate()
    self.uglySide.call('ritual_ZN13PlaneGeometry22scheduleGeometryUpdateEv')

  @staticmethod
  def generatePlaneGeometry(*__, **_) -> Never:
    """
    Qt's 'PlaneGeometry::GeometryData
    PlaneGeometry::generatePlaneGeometry(float width, float height, QSize
    meshResolution, Plane plane, bool reversed, bool mirrored)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'PlaneGeometry.generatePlaneGeometry' has no cute function yet. "
        "Qt's 'PlaneGeometry::GeometryData "
        "PlaneGeometry::generatePlaneGeometry(float width, float height, "
        "QSize meshResolution, Plane plane, bool reversed, bool mirrored)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def generatePlaneGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void
    PlaneGeometry::generatePlaneGeometryAsync(QPromise<PlaneGeometry::
    GeometryData> &promise, float width, float height, QSize meshResolution,
    Plane plane, bool reversed, bool mirrored)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'PlaneGeometry.generatePlaneGeometryAsync' has no cute function "
        "yet. Qt's 'void "
        "PlaneGeometry::generatePlaneGeometryAsync(QPromise<PlaneGeometry::G"
        "eometryData> &promise, float width, float height, QSize "
        "meshResolution, Plane plane, bool reversed, bool mirrored)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void PlaneGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'PlaneGeometry.updateGeometry' has no cute function yet. Qt's "
        "'void PlaneGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
