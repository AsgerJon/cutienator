"""
Qt3DExtras::QTorusGeometryView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qtorusgeometryview.h, Qt 6.12.0. Changes made here are lost.
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


class QTorusGeometryView(Qt3DCore.QGeometryView):
  """
  The cute side of Qt's Qt3DExtras::QTorusGeometryView: a plain Python object
  standing in front of one C++ Qt3DExtras::QTorusGeometryView.

  It is built on the cute 'Qt3DCore::QGeometryView', as Qt's
  Qt3DExtras::QTorusGeometryView is built on Qt's Qt3DCore::QGeometryView,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QTorusGeometryView that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr', 'rings',
  'slices', 'radius', 'minorRadius', 'setRings', 'setSlices', 'setRadius',
  'setMinorRadius', 'radiusChanged', 'ringsChanged', 'slicesChanged',
  'minorRadiusChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QTorusGeometryView::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QTorusGeometryView::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QTorusGeometryView::~QTorusGeometryView()': the
    destructor: Python never removes a C++ Qt3DExtras::QTorusGeometryView.

  What has no ritual
  ------------------

  10 of the 28 functions Qt declares: 10 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QTorusGeometryView is created at the first use, not
    by 'Qt3DExtras::QTorusGeometryView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QTorusGeometryView.
  - Qt tells when it has removed the C++ Qt3DExtras::QTorusGeometryView.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DExtras::QTorusGeometryView::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#tr

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
    #  QString Qt3DExtras::QTorusGeometryView::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QTorusGeometryView'

  #  A C++ Qt3DExtras::QTorusGeometryView Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QTorusGeometryView'

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
    *Qt3DExtras::QTorusGeometryView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QTorusGeometryView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QTorusGeometryView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QTorusGeometryView::rings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#rings
    """
    #  int Qt3DExtras::QTorusGeometryView::rings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QTorusGeometryView5ringsEv',
    )

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QTorusGeometryView::slices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#slices
    """
    #  int Qt3DExtras::QTorusGeometryView::slices() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QTorusGeometryView6slicesEv',
    )

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QTorusGeometryView::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#radius
    """
    #  float Qt3DExtras::QTorusGeometryView::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QTorusGeometryView6radiusEv',
    )

  def minorRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QTorusGeometryView::minorRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#minorRadius
    """
    #  float Qt3DExtras::QTorusGeometryView::minorRadius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QTorusGeometryView11minorRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::setRings(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::setRings(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView8setRingsEi', rings,
    )

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::setSlices(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView9setSlicesEi', slices,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::setRadius(float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::setRadius(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView9setRadiusEf', radius,
    )

  @overload(float)
  def setMinorRadius(self, minorRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::setMinorRadius(float
    minorRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#setMinorRadius

    Parameters
    ----------

    minorRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::setMinorRadius(float minorRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView14setMinorRadiusEf',
        minorRadius,
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
    'Qt3DExtras::QTorusGeometryView::QTorusGeometryView(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QTorusGeometryView::QTorusGeometryView(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QTorusGeometryView, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryViewC1EPN8Qt3DCore5QNodeE',
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

  @overload(float)
  def radiusChanged(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::radiusChanged(float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#radiusChanged

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::radiusChanged(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView13radiusChangedEf', radius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::ringsChanged(int
    rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::slicesChanged(int
    slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView13slicesChangedEi', slices,
    )

  @overload(float)
  def minorRadiusChanged(self, minorRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTorusGeometryView::minorRadiusChanged(float
    minorRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtorusgeometryview.html

    Parameters
    ----------

    minorRadius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QTorusGeometryView::minorRadiusChanged(float
    #      minorRadius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QTorusGeometryView18minorRadiusChangedEf',
        minorRadius,
    )
