"""
CuboidGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/cuboidgeometry_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means CuboidGeometry to be private: it declares the class in a header
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


class CuboidGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's CuboidGeometry: a plain Python object standing in
  front of one C++ CuboidGeometry.

  What exists
  -----------

  Every function of Qt's CuboidGeometry that has a ritual and that Python can
  call so far, 28 names in all: 'metaObject', 'tr', 'xExtent', 'setXExtent',
  'yExtent', 'setYExtent', 'zExtent', 'setZExtent', 'yzMeshResolution',
  'setYzMeshResolution', 'xzMeshResolution', 'setXzMeshResolution',
  'xyMeshResolution', 'setXyMeshResolution', 'asynchronous',
  'setAsynchronous', 'status', 'doUpdateGeometry', 'requestFinished',
  'xExtentChanged', 'yExtentChanged', 'zExtentChanged',
  'yzMeshResolutionChanged', 'xzMeshResolutionChanged',
  'xyMeshResolutionChanged', 'asynchronousChanged', 'statusChanged',
  'scheduleGeometryUpdate'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CuboidGeometry::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int CuboidGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'CuboidGeometry::~CuboidGeometry()': the destructor: Python never
    removes a C++ CuboidGeometry.
  - Qt's 'void CuboidGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'CuboidGeometry::GeometryData
    CuboidGeometry::generateCuboidGeometry(float xExtent, float yExtent,
    float zExtent, QSize yzMeshResolution, QSize xzMeshResolution, QSize
    xyMeshResolution)': gives a type Python has no way to take yet.
  - Qt's 'void
    CuboidGeometry::generateCuboidGeometryAsync(QPromise<CuboidGeometry::
    GeometryData> &promise, float xExtent, float yExtent, float zExtent,
    QSize yzMeshResolution, QSize xzMeshResolution, QSize xyMeshResolution)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ CuboidGeometry is created at the first use, not by
    'CuboidGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CuboidGeometry.
  - Qt tells when it has removed the C++ CuboidGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's CuboidGeometry that has no cute function yet,
    'generateCuboidGeometry', 'generateCuboidGeometryAsync',
    'updateGeometry', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside CuboidGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'CuboidGeometry::Status' of Qt, with the 4 names Qt gives in it.
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
    Calls Qt's 'QString CuboidGeometry::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#tr

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
    #  QString CuboidGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14CuboidGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CuboidGeometry'

  #  A C++ CuboidGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CuboidGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CuboidGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CuboidGeometry::metaObject() const
    address = self.uglySide.call('ritual_ZNK14CuboidGeometry10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xExtent(self) -> float:
    """
    Calls Qt's 'float CuboidGeometry::xExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#xExtent
    """
    #  float CuboidGeometry::xExtent() const
    return self.uglySide.call('ritual_ZNK14CuboidGeometry7xExtentEv')

  def yExtent(self) -> float:
    """
    Calls Qt's 'float CuboidGeometry::yExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#yExtent
    """
    #  float CuboidGeometry::yExtent() const
    return self.uglySide.call('ritual_ZNK14CuboidGeometry7yExtentEv')

  def zExtent(self) -> float:
    """
    Calls Qt's 'float CuboidGeometry::zExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#zExtent
    """
    #  float CuboidGeometry::zExtent() const
    return self.uglySide.call('ritual_ZNK14CuboidGeometry7zExtentEv')

  def yzMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize CuboidGeometry::yzMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#yzMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize CuboidGeometry::yzMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK14CuboidGeometry16yzMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def xzMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize CuboidGeometry::xzMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#xzMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize CuboidGeometry::xzMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK14CuboidGeometry16xzMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def xyMeshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize CuboidGeometry::xyMeshResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#xyMeshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize CuboidGeometry::xyMeshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK14CuboidGeometry16xyMeshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool CuboidGeometry::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#asynchronous
    """
    #  bool CuboidGeometry::asynchronous() const
    return self.uglySide.call('ritual_ZNK14CuboidGeometry12asynchronousEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status CuboidGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status CuboidGeometry::status() const
    return CuboidGeometry.Status(self.uglySide.call(
        'ritual_ZNK14CuboidGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXExtent(self, newXExtent: float) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setXExtent(float newXExtent)'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#setXExtent

    Parameters
    ----------

    newXExtent : float
      Passed on as it is.
    """
    #  void CuboidGeometry::setXExtent(float newXExtent)
    self.uglySide.call('ritual_ZN14CuboidGeometry10setXExtentEf', newXExtent)

  @overload(float)
  def setYExtent(self, newYExtent: float) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setYExtent(float newYExtent)'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#setYExtent

    Parameters
    ----------

    newYExtent : float
      Passed on as it is.
    """
    #  void CuboidGeometry::setYExtent(float newYExtent)
    self.uglySide.call('ritual_ZN14CuboidGeometry10setYExtentEf', newYExtent)

  @overload(float)
  def setZExtent(self, newZExtent: float) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setZExtent(float newZExtent)'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#setZExtent

    Parameters
    ----------

    newZExtent : float
      Passed on as it is.
    """
    #  void CuboidGeometry::setZExtent(float newZExtent)
    self.uglySide.call('ritual_ZN14CuboidGeometry10setZExtentEf', newZExtent)

  @overload(QSize)
  def setYzMeshResolution(self, newYzMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setYzMeshResolution(const QSize
    &newYzMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#setYzMeshResolution

    Parameters
    ----------

    newYzMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void CuboidGeometry::setYzMeshResolution(const QSize
    #      &newYzMeshResolution)
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry19setYzMeshResolutionERK5QSize',
        self._valueOf(newYzMeshResolution),
    )

  @overload(QSize)
  def setXzMeshResolution(self, newXzMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setXzMeshResolution(const QSize
    &newXzMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#setXzMeshResolution

    Parameters
    ----------

    newXzMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void CuboidGeometry::setXzMeshResolution(const QSize
    #      &newXzMeshResolution)
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry19setXzMeshResolutionERK5QSize',
        self._valueOf(newXzMeshResolution),
    )

  @overload(QSize)
  def setXyMeshResolution(self, newXyMeshResolution: QSize) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setXyMeshResolution(const QSize
    &newXyMeshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#setXyMeshResolution

    Parameters
    ----------

    newXyMeshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void CuboidGeometry::setXyMeshResolution(const QSize
    #      &newXyMeshResolution)
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry19setXyMeshResolutionERK5QSize',
        self._valueOf(newXyMeshResolution),
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void CuboidGeometry::setAsynchronous(bool newAsynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void CuboidGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry15setAsynchronousEb', newAsynchronous,
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
    'CuboidGeometry::CuboidGeometry(QQuick3DObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#CuboidGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  CuboidGeometry::CuboidGeometry(QQuick3DObject *parent)
    self._noteCreation(CuboidGeometry, lambda: Rituals.call(
        'ritual_ZN14CuboidGeometryC1EP14QQuick3DObject',
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
    Calls Qt's 'void CuboidGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#doUpdateGeometry
    """
    #  void CuboidGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN14CuboidGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#requestFinished
    """
    #  void CuboidGeometry::requestFinished()
    self.uglySide.call('ritual_ZN14CuboidGeometry15requestFinishedEv')

  def xExtentChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::xExtentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#xExtentChanged
    """
    #  void CuboidGeometry::xExtentChanged()
    self.uglySide.call('ritual_ZN14CuboidGeometry14xExtentChangedEv')

  def yExtentChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::yExtentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#yExtentChanged
    """
    #  void CuboidGeometry::yExtentChanged()
    self.uglySide.call('ritual_ZN14CuboidGeometry14yExtentChangedEv')

  def zExtentChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::zExtentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#zExtentChanged
    """
    #  void CuboidGeometry::zExtentChanged()
    self.uglySide.call('ritual_ZN14CuboidGeometry14zExtentChangedEv')

  def yzMeshResolutionChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::yzMeshResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#yzMeshResolutionChanged
    """
    #  void CuboidGeometry::yzMeshResolutionChanged()
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry23yzMeshResolutionChangedEv',
    )

  def xzMeshResolutionChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::xzMeshResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#xzMeshResolutionChanged
    """
    #  void CuboidGeometry::xzMeshResolutionChanged()
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry23xzMeshResolutionChangedEv',
    )

  def xyMeshResolutionChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::xyMeshResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#xyMeshResolutionChanged
    """
    #  void CuboidGeometry::xyMeshResolutionChanged()
    self.uglySide.call(
        'ritual_ZN14CuboidGeometry23xyMeshResolutionChangedEv',
    )

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#asynchronousChanged
    """
    #  void CuboidGeometry::asynchronousChanged()
    self.uglySide.call('ritual_ZN14CuboidGeometry19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/cuboidgeometry.html#statusChanged
    """
    #  void CuboidGeometry::statusChanged()
    self.uglySide.call('ritual_ZN14CuboidGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void CuboidGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cuboidgeometry.html#scheduleGeometryUpdate
    """
    #  void CuboidGeometry::scheduleGeometryUpdate()
    self.uglySide.call('ritual_ZN14CuboidGeometry22scheduleGeometryUpdateEv')

  @staticmethod
  def generateCuboidGeometry(*__, **_) -> Never:
    """
    Qt's 'CuboidGeometry::GeometryData
    CuboidGeometry::generateCuboidGeometry(float xExtent, float yExtent,
    float zExtent, QSize yzMeshResolution, QSize xzMeshResolution, QSize
    xyMeshResolution)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'CuboidGeometry.generateCuboidGeometry' has no cute function yet. "
        "Qt's 'CuboidGeometry::GeometryData "
        "CuboidGeometry::generateCuboidGeometry(float xExtent, float "
        "yExtent, float zExtent, QSize yzMeshResolution, QSize "
        "xzMeshResolution, QSize xyMeshResolution)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def generateCuboidGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void
    CuboidGeometry::generateCuboidGeometryAsync(QPromise<CuboidGeometry::
    GeometryData> &promise, float xExtent, float yExtent, float zExtent,
    QSize yzMeshResolution, QSize xzMeshResolution, QSize xyMeshResolution)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'CuboidGeometry.generateCuboidGeometryAsync' has no cute function "
        "yet. Qt's 'void "
        "CuboidGeometry::generateCuboidGeometryAsync(QPromise<CuboidGeometry"
        "::GeometryData> &promise, float xExtent, float yExtent, float "
        "zExtent, QSize yzMeshResolution, QSize xzMeshResolution, QSize "
        "xyMeshResolution)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void CuboidGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'CuboidGeometry.updateGeometry' has no cute function yet. Qt's "
        "'void CuboidGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
