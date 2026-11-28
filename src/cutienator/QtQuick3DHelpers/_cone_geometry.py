"""
ConeGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/conegeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means ConeGeometry to be private: it declares the class in a header it
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


class ConeGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ConeGeometry: a plain Python object standing in front
  of one C++ ConeGeometry.

  What exists
  -----------

  Every function of Qt's ConeGeometry that has a ritual and that Python can
  call so far, 25 names in all: 'metaObject', 'tr', 'topRadius',
  'setTopRadius', 'bottomRadius', 'setBottomRadius', 'length', 'setLength',
  'rings', 'setRings', 'segments', 'setSegments', 'asynchronous',
  'setAsynchronous', 'status', 'doUpdateGeometry', 'requestFinished',
  'topRadiusChanged', 'bottomRadiusChanged', 'lengthChanged', 'ringsChanged',
  'segmentsChanged', 'asynchronousChanged', 'statusChanged',
  'scheduleGeometryUpdate'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ConeGeometry::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ConeGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'ConeGeometry::~ConeGeometry()': the destructor: Python never
    removes a C++ ConeGeometry.
  - Qt's 'void ConeGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'ConeGeometry::GeometryData ConeGeometry::generateConeGeometry(float
    topRadius, float bottomRadius, float length, int rings, int slices)':
    gives a type Python has no way to take yet.
  - Qt's 'void
    ConeGeometry::generateConeGeometryAsync(QPromise<ConeGeometry::
    GeometryData> &promise, float topRadius, float bottomRadius, float
    length, int rings, int segments)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ConeGeometry is created at the first use, not by
    'ConeGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ConeGeometry.
  - Qt tells when it has removed the C++ ConeGeometry. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's ConeGeometry that has no cute function yet,
    'generateConeGeometry', 'generateConeGeometryAsync', 'updateGeometry',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside ConeGeometry, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'ConeGeometry::Status' of Qt, with the 4 names Qt gives in it.
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
    Calls Qt's 'QString ConeGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#tr

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
    #  QString ConeGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12ConeGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ConeGeometry'

  #  A C++ ConeGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ConeGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ConeGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ConeGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK12ConeGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def topRadius(self) -> float:
    """
    Calls Qt's 'float ConeGeometry::topRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#topRadius
    """
    #  float ConeGeometry::topRadius() const
    return self.uglySide.call('ritual_ZNK12ConeGeometry9topRadiusEv')

  def bottomRadius(self) -> float:
    """
    Calls Qt's 'float ConeGeometry::bottomRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#bottomRadius
    """
    #  float ConeGeometry::bottomRadius() const
    return self.uglySide.call('ritual_ZNK12ConeGeometry12bottomRadiusEv')

  def length(self) -> float:
    """
    Calls Qt's 'float ConeGeometry::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#length
    """
    #  float ConeGeometry::length() const
    return self.uglySide.call('ritual_ZNK12ConeGeometry6lengthEv')

  def rings(self) -> int:
    """
    Calls Qt's 'int ConeGeometry::rings() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#rings
    """
    #  int ConeGeometry::rings() const
    return self.uglySide.call('ritual_ZNK12ConeGeometry5ringsEv')

  def segments(self) -> int:
    """
    Calls Qt's 'int ConeGeometry::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#segments
    """
    #  int ConeGeometry::segments() const
    return self.uglySide.call('ritual_ZNK12ConeGeometry8segmentsEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool ConeGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#asynchronous
    """
    #  bool ConeGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK12ConeGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status ConeGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status ConeGeometry::status() const
    return ConeGeometry.Status(self.uglySide.call(
        'ritual_ZNK12ConeGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTopRadius(self, newTopRadius: float) -> None:
    """
    Calls Qt's 'void ConeGeometry::setTopRadius(float newTopRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#setTopRadius

    Parameters
    ----------

    newTopRadius : float
      Passed on as it is.
    """
    #  void ConeGeometry::setTopRadius(float newTopRadius)
    self.uglySide.call(
        'ritual_ZN12ConeGeometry12setTopRadiusEf', newTopRadius,
    )

  @overload(float)
  def setBottomRadius(self, newBottomRadius: float) -> None:
    """
    Calls Qt's 'void ConeGeometry::setBottomRadius(float newBottomRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#setBottomRadius

    Parameters
    ----------

    newBottomRadius : float
      Passed on as it is.
    """
    #  void ConeGeometry::setBottomRadius(float newBottomRadius)
    self.uglySide.call(
        'ritual_ZN12ConeGeometry15setBottomRadiusEf', newBottomRadius,
    )

  @overload(float)
  def setLength(self, newLength: float) -> None:
    """
    Calls Qt's 'void ConeGeometry::setLength(float newLength)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#setLength

    Parameters
    ----------

    newLength : float
      Passed on as it is.
    """
    #  void ConeGeometry::setLength(float newLength)
    self.uglySide.call('ritual_ZN12ConeGeometry9setLengthEf', newLength)

  @overload(int)
  def setRings(self, newRings: int) -> None:
    """
    Calls Qt's 'void ConeGeometry::setRings(int newRings)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#setRings

    Parameters
    ----------

    newRings : int
      Passed on as it is.
    """
    #  void ConeGeometry::setRings(int newRings)
    self.uglySide.call('ritual_ZN12ConeGeometry8setRingsEi', newRings)

  @overload(int)
  def setSegments(self, newSegments: int) -> None:
    """
    Calls Qt's 'void ConeGeometry::setSegments(int newSegments)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#setSegments

    Parameters
    ----------

    newSegments : int
      Passed on as it is.
    """
    #  void ConeGeometry::setSegments(int newSegments)
    self.uglySide.call('ritual_ZN12ConeGeometry11setSegmentsEi', newSegments)

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void ConeGeometry::setAsynchronous(bool newAsynchronous)'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void ConeGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN12ConeGeometry15setAsynchronousEb', newAsynchronous,
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
    Notes what was given, for Qt's 'ConeGeometry::ConeGeometry(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#ConeGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ConeGeometry::ConeGeometry(QQuick3DObject *parent)
    self._noteCreation(ConeGeometry, lambda: Rituals.call(
        'ritual_ZN12ConeGeometryC1EP14QQuick3DObject',
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
    Calls Qt's 'void ConeGeometry::doUpdateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#doUpdateGeometry
    """
    #  void ConeGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN12ConeGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::requestFinished()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#requestFinished
    """
    #  void ConeGeometry::requestFinished()
    self.uglySide.call('ritual_ZN12ConeGeometry15requestFinishedEv')

  def topRadiusChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::topRadiusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#topRadiusChanged
    """
    #  void ConeGeometry::topRadiusChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry16topRadiusChangedEv')

  def bottomRadiusChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::bottomRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/conegeometry.html#bottomRadiusChanged
    """
    #  void ConeGeometry::bottomRadiusChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry19bottomRadiusChangedEv')

  def lengthChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::lengthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#lengthChanged
    """
    #  void ConeGeometry::lengthChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry13lengthChangedEv')

  def ringsChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::ringsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#ringsChanged
    """
    #  void ConeGeometry::ringsChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry12ringsChangedEv')

  def segmentsChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::segmentsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#segmentsChanged
    """
    #  void ConeGeometry::segmentsChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry15segmentsChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/conegeometry.html#asynchronousChanged
    """
    #  void ConeGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/conegeometry.html#statusChanged
    """
    #  void ConeGeometry::statusChanged()
    self.uglySide.call('ritual_ZN12ConeGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void ConeGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/conegeometry.html#scheduleGeometryUpdate
    """
    #  void ConeGeometry::scheduleGeometryUpdate()
    self.uglySide.call('ritual_ZN12ConeGeometry22scheduleGeometryUpdateEv')

  @staticmethod
  def generateConeGeometry(*__, **_) -> Never:
    """
    Qt's 'ConeGeometry::GeometryData ConeGeometry::generateConeGeometry(float
    topRadius, float bottomRadius, float length, int rings, int slices)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ConeGeometry.generateConeGeometry' has no cute function yet. Qt's "
        "'ConeGeometry::GeometryData "
        "ConeGeometry::generateConeGeometry(float topRadius, float "
        "bottomRadius, float length, int rings, int slices)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def generateConeGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void
    ConeGeometry::generateConeGeometryAsync(QPromise<ConeGeometry::
    GeometryData> &promise, float topRadius, float bottomRadius, float
    length, int rings, int segments)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'ConeGeometry.generateConeGeometryAsync' has no cute function yet. "
        "Qt's 'void "
        "ConeGeometry::generateConeGeometryAsync(QPromise<ConeGeometry::Geom"
        "etryData> &promise, float topRadius, float bottomRadius, float "
        "length, int rings, int segments)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void ConeGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ConeGeometry.updateGeometry' has no cute function yet. Qt's 'void "
        "ConeGeometry::updateGeometry(const GeometryData &geometryData)': "
        "takes a type Python has no way to hand over yet.")
