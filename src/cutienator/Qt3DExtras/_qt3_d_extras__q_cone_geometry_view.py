"""
Qt3DExtras::QConeGeometryView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qconegeometryview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QConeGeometryView(Qt3DCore.QGeometryView):
  """
  The cute side of Qt's Qt3DExtras::QConeGeometryView: a plain Python object
  standing in front of one C++ Qt3DExtras::QConeGeometryView.

  It is built on the cute 'Qt3DCore::QGeometryView', as Qt's
  Qt3DExtras::QConeGeometryView is built on Qt's Qt3DCore::QGeometryView, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QConeGeometryView that has a ritual and
  that Python can call so far, 23 names in all: 'metaObject', 'tr', 'rings',
  'slices', 'hasTopEndcap', 'hasBottomEndcap', 'topRadius', 'bottomRadius',
  'length', 'setHasTopEndcap', 'setHasBottomEndcap', 'setTopRadius',
  'setBottomRadius', 'setRings', 'setSlices', 'setLength',
  'hasTopEndcapChanged', 'hasBottomEndcapChanged', 'topRadiusChanged',
  'bottomRadiusChanged', 'ringsChanged', 'slicesChanged', 'lengthChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QConeGeometryView::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QConeGeometryView::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QConeGeometryView::~QConeGeometryView()': the
    destructor: Python never removes a C++ Qt3DExtras::QConeGeometryView.

  What has no ritual
  ------------------

  10 of the 37 functions Qt declares: 10 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QConeGeometryView is created at the first use, not by
    'Qt3DExtras::QConeGeometryView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QConeGeometryView.
  - Qt tells when it has removed the C++ Qt3DExtras::QConeGeometryView. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DExtras::QConeGeometryView::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#tr

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
    #  QString Qt3DExtras::QConeGeometryView::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QConeGeometryView'

  #  A C++ Qt3DExtras::QConeGeometryView Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QConeGeometryView'

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
    *Qt3DExtras::QConeGeometryView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QConeGeometryView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QConeGeometryView::rings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#rings
    """
    #  int Qt3DExtras::QConeGeometryView::rings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView5ringsEv',
    )

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QConeGeometryView::slices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#slices
    """
    #  int Qt3DExtras::QConeGeometryView::slices() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView6slicesEv',
    )

  def hasTopEndcap(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QConeGeometryView::hasTopEndcap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#hasTopEndcap
    """
    #  bool Qt3DExtras::QConeGeometryView::hasTopEndcap() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView12hasTopEndcapEv',
    )

  def hasBottomEndcap(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QConeGeometryView::hasBottomEndcap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#hasBottomEndcap
    """
    #  bool Qt3DExtras::QConeGeometryView::hasBottomEndcap() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView15hasBottomEndcapEv',
    )

  def topRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeGeometryView::topRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#topRadius
    """
    #  float Qt3DExtras::QConeGeometryView::topRadius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView9topRadiusEv',
    )

  def bottomRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeGeometryView::bottomRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#bottomRadius
    """
    #  float Qt3DExtras::QConeGeometryView::bottomRadius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView12bottomRadiusEv',
    )

  def length(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QConeGeometryView::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#length
    """
    #  float Qt3DExtras::QConeGeometryView::length() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QConeGeometryView6lengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasTopEndcap(self, hasTopEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setHasTopEndcap(bool
    hasTopEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#setHasTopEndcap

    Parameters
    ----------

    hasTopEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setHasTopEndcap(bool hasTopEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView15setHasTopEndcapEb',
        hasTopEndcap,
    )

  @overload(bool)
  def setHasBottomEndcap(self, hasBottomEndcap: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setHasBottomEndcap(bool
    hasBottomEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html

    Parameters
    ----------

    hasBottomEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setHasBottomEndcap(bool
    #      hasBottomEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView18setHasBottomEndcapEb',
        hasBottomEndcap,
    )

  @overload(float)
  def setTopRadius(self, topRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setTopRadius(float
    topRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#setTopRadius

    Parameters
    ----------

    topRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setTopRadius(float topRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView12setTopRadiusEf',
        topRadius,
    )

  @overload(float)
  def setBottomRadius(self, bottomRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setBottomRadius(float
    bottomRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#setBottomRadius

    Parameters
    ----------

    bottomRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setBottomRadius(float
    #      bottomRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView15setBottomRadiusEf',
        bottomRadius,
    )

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setRings(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setRings(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView8setRingsEi', rings,
    )

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setSlices(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView9setSlicesEi', slices,
    )

  @overload(float)
  def setLength(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::setLength(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#setLength

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::setLength(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView9setLengthEf', length,
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
    'Qt3DExtras::QConeGeometryView::QConeGeometryView(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QConeGeometryView::QConeGeometryView(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QConeGeometryView, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryViewC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::hasTopEndcapChanged(bool
    hasTopEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html

    Parameters
    ----------

    hasTopEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::hasTopEndcapChanged(bool
    #      hasTopEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView19hasTopEndcapChangedEb',
        hasTopEndcap,
    )

  @overload(bool)
  def hasBottomEndcapChanged(self, hasBottomEndcap: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QConeGeometryView::hasBottomEndcapChanged(bool
    hasBottomEndcap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html

    Parameters
    ----------

    hasBottomEndcap : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::hasBottomEndcapChanged(bool
    #      hasBottomEndcap)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView22hasBottomEndcapChangedEb',
        hasBottomEndcap,
    )

  @overload(float)
  def topRadiusChanged(self, topRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::topRadiusChanged(float
    topRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#topRadiusChanged

    Parameters
    ----------

    topRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::topRadiusChanged(float topRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView16topRadiusChangedEf',
        topRadius,
    )

  @overload(float)
  def bottomRadiusChanged(self, bottomRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::bottomRadiusChanged(float
    bottomRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html

    Parameters
    ----------

    bottomRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::bottomRadiusChanged(float
    #      bottomRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView19bottomRadiusChangedEf',
        bottomRadius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::ringsChanged(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::slicesChanged(int
    slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView13slicesChangedEi', slices,
    )

  @overload(float)
  def lengthChanged(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QConeGeometryView::lengthChanged(float
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryview.html#lengthChanged

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QConeGeometryView::lengthChanged(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QConeGeometryView13lengthChangedEf', length,
    )
