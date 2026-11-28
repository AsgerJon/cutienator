"""
Qt3DExtras::QConeMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qconemesh.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QConeMesh(Qt3DRender.QGeometryRenderer):
  """
  The cute side of Qt's Qt3DExtras::QConeMesh: a plain Python object standing
  in front of one C++ Qt3DExtras::QConeMesh.

  It is built on the cute 'Qt3DRender::QGeometryRenderer', as Qt's
  Qt3DExtras::QConeMesh is built on Qt's Qt3DRender::QGeometryRenderer, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QConeMesh that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'rings',
  'slices', 'hasTopEndcap', 'hasBottomEndcap', 'topRadius', 'bottomRadius',
  'length', 'setHasTopEndcap', 'setHasBottomEndcap', 'setTopRadius',
  'setBottomRadius', 'setRings', 'setSlices', 'setLength',
  'hasTopEndcapChanged', 'hasBottomEndcapChanged', 'topRadiusChanged',
  'bottomRadiusChanged', 'ringsChanged', 'slicesChanged', 'lengthChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QConeMesh::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QConeMesh::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QConeMesh::~QConeMesh()': the destructor: Python never
    removes a C++ Qt3DExtras::QConeMesh.

  What has no ritual
  ------------------

  10 of the 37 functions Qt declares: 10 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QConeMesh is created at the first use, not by
    'Qt3DExtras::QConeMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QConeMesh.
  - Qt tells when it has removed the C++ Qt3DExtras::QConeMesh. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString Qt3DExtras::QConeMesh::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#tr

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
    #  QString Qt3DExtras::QConeMesh::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras9QConeMesh2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QConeMesh'

  #  A C++ Qt3DExtras::QConeMesh Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QConeMesh'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QConeMesh::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QConeMesh::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras9QConeMesh10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QConeMesh::rings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#rings
    """
    #  int Qt3DExtras::QConeMesh::rings() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras9QConeMesh5ringsEv')

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QConeMesh::slices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#slices
    """
    #  int Qt3DExtras::QConeMesh::slices() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras9QConeMesh6slicesEv')

  def hasTopEndcap(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QConeMesh::hasTopEndcap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#hasTopEndcap
    """
    #  bool Qt3DExtras::QConeMesh::hasTopEndcap() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras9QConeMesh12hasTopEndcapEv',
    )

  def hasBottomEndcap(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QConeMesh::hasBottomEndcap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#hasBottomEndcap
    """
    #  bool Qt3DExtras::QConeMesh::hasBottomEndcap() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras9QConeMesh15hasBottomEndcapEv',
    )

  def topRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeMesh::topRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#topRadius
    """
    #  float Qt3DExtras::QConeMesh::topRadius() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras9QConeMesh9topRadiusEv')

  def bottomRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeMesh::bottomRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#bottomRadius
    """
    #  float Qt3DExtras::QConeMesh::bottomRadius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras9QConeMesh12bottomRadiusEv',
    )

  def length(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeMesh::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#length
    """
    #  float Qt3DExtras::QConeMesh::length() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras9QConeMesh6lengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasTopEndcap(self, hasTopEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setHasTopEndcap(bool
    hasTopEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setHasTopEndcap

    Parameters
    ----------

    hasTopEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setHasTopEndcap(bool hasTopEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh15setHasTopEndcapEb', hasTopEndcap,
    )

  @overload(bool)
  def setHasBottomEndcap(self, hasBottomEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setHasBottomEndcap(bool
    hasBottomEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setHasBottomEndcap

    Parameters
    ----------

    hasBottomEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setHasBottomEndcap(bool hasBottomEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh18setHasBottomEndcapEb',
        hasBottomEndcap,
    )

  @overload(float)
  def setTopRadius(self, topRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setTopRadius(float topRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setTopRadius

    Parameters
    ----------

    topRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setTopRadius(float topRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh12setTopRadiusEf', topRadius,
    )

  @overload(float)
  def setBottomRadius(self, bottomRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setBottomRadius(float
    bottomRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setBottomRadius

    Parameters
    ----------

    bottomRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setBottomRadius(float bottomRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh15setBottomRadiusEf', bottomRadius,
    )

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setRings(int rings)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setRings(int rings)
    self.uglySide.call('ritual_ZN10Qt3DExtras9QConeMesh8setRingsEi', rings)

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setSlices(int slices)
    self.uglySide.call('ritual_ZN10Qt3DExtras9QConeMesh9setSlicesEi', slices)

  @overload(float)
  def setLength(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::setLength(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#setLength

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::setLength(float length)
    self.uglySide.call('ritual_ZN10Qt3DExtras9QConeMesh9setLengthEf', length)

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
    'Qt3DExtras::QConeMesh::QConeMesh(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#QConeMesh

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QConeMesh::QConeMesh(Qt3DCore::QNode *parent)
    self._noteCreation(QConeMesh, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras9QConeMeshC1EPN8Qt3DCore5QNodeE',
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

  @overload(bool)
  def hasTopEndcapChanged(self, hasTopEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::hasTopEndcapChanged(bool
    hasTopEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#hasTopEndcapChanged

    Parameters
    ----------

    hasTopEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::hasTopEndcapChanged(bool hasTopEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh19hasTopEndcapChangedEb',
        hasTopEndcap,
    )

  @overload(bool)
  def hasBottomEndcapChanged(self, hasBottomEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::hasBottomEndcapChanged(bool
    hasBottomEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#hasBottomEndcapChanged

    Parameters
    ----------

    hasBottomEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::hasBottomEndcapChanged(bool
    #      hasBottomEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh22hasBottomEndcapChangedEb',
        hasBottomEndcap,
    )

  @overload(float)
  def topRadiusChanged(self, topRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::topRadiusChanged(float
    topRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#topRadiusChanged

    Parameters
    ----------

    topRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::topRadiusChanged(float topRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh16topRadiusChangedEf', topRadius,
    )

  @overload(float)
  def bottomRadiusChanged(self, bottomRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::bottomRadiusChanged(float
    bottomRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#bottomRadiusChanged

    Parameters
    ----------

    bottomRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::bottomRadiusChanged(float bottomRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh19bottomRadiusChangedEf',
        bottomRadius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::ringsChanged(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::slicesChanged(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh13slicesChangedEi', slices,
    )

  @overload(float)
  def lengthChanged(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeMesh::lengthChanged(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconemesh.html#lengthChanged

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeMesh::lengthChanged(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras9QConeMesh13lengthChangedEf', length,
    )
