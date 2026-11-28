"""
Qt3DExtras::QSphereGeometryView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qspheregeometryview.h, Qt 6.12.0. Changes made here are lost.
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


class QSphereGeometryView(Qt3DCore.QGeometryView):
  """
  The cute side of Qt's Qt3DExtras::QSphereGeometryView: a plain Python
  object standing in front of one C++ Qt3DExtras::QSphereGeometryView.

  It is built on the cute 'Qt3DCore::QGeometryView', as Qt's
  Qt3DExtras::QSphereGeometryView is built on Qt's Qt3DCore::QGeometryView,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSphereGeometryView that has a ritual
  and that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'rings', 'slices', 'radius', 'generateTangents', 'setRings', 'setSlices',
  'setRadius', 'setGenerateTangents', 'radiusChanged', 'ringsChanged',
  'slicesChanged', 'generateTangentsChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QSphereGeometryView::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QSphereGeometryView::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QSphereGeometryView::~QSphereGeometryView()': the
    destructor: Python never removes a C++ Qt3DExtras::QSphereGeometryView.

  What has no ritual
  ------------------

  9 of the 27 functions Qt declares: 9 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSphereGeometryView is created at the first use, not
    by 'Qt3DExtras::QSphereGeometryView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSphereGeometryView.
  - Qt tells when it has removed the C++ Qt3DExtras::QSphereGeometryView.
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
    Calls Qt's 'QString Qt3DExtras::QSphereGeometryView::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#tr

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
    #  QString Qt3DExtras::QSphereGeometryView::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSphereGeometryView'

  #  A C++ Qt3DExtras::QSphereGeometryView Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QSphereGeometryView'

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
    *Qt3DExtras::QSphereGeometryView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QSphereGeometryView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QSphereGeometryView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rings(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSphereGeometryView::rings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#rings
    """
    #  int Qt3DExtras::QSphereGeometryView::rings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QSphereGeometryView5ringsEv',
    )

  def slices(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSphereGeometryView::slices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#slices
    """
    #  int Qt3DExtras::QSphereGeometryView::slices() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QSphereGeometryView6slicesEv',
    )

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QSphereGeometryView::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#radius
    """
    #  float Qt3DExtras::QSphereGeometryView::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QSphereGeometryView6radiusEv',
    )

  def generateTangents(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QSphereGeometryView::generateTangents()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html
    """
    #  bool Qt3DExtras::QSphereGeometryView::generateTangents() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QSphereGeometryView16generateTangentsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRings(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometryView::setRings(int rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#setRings

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::setRings(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView8setRingsEi', rings,
    )

  @overload(int)
  def setSlices(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometryView::setSlices(int slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#setSlices

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::setSlices(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView9setSlicesEi', slices,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometryView::setRadius(float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::setRadius(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView9setRadiusEf', radius,
    )

  @overload(bool)
  def setGenerateTangents(self, gen: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QSphereGeometryView::setGenerateTangents(bool gen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html

    Parameters
    ----------

    gen : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::setGenerateTangents(bool gen)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView19setGenerateTangentsEb',
        gen,
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
    'Qt3DExtras::QSphereGeometryView::QSphereGeometryView(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QSphereGeometryView::QSphereGeometryView(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QSphereGeometryView, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryViewC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QSphereGeometryView::radiusChanged(float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#radiusChanged

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::radiusChanged(float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView13radiusChangedEf',
        radius,
    )

  @overload(int)
  def ringsChanged(self, rings: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometryView::ringsChanged(int
    rings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#ringsChanged

    Parameters
    ----------

    rings : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::ringsChanged(int rings)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView12ringsChangedEi', rings,
    )

  @overload(int)
  def slicesChanged(self, slices: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometryView::slicesChanged(int
    slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html#slicesChanged

    Parameters
    ----------

    slices : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::slicesChanged(int slices)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView13slicesChangedEi',
        slices,
    )

  @overload(bool)
  def generateTangentsChanged(self, generateTangents: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QSphereGeometryView::generateTangentsChanged(bool
    generateTangents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryview.html

    Parameters
    ----------

    generateTangents : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QSphereGeometryView::generateTangentsChanged(bool
    #      generateTangents)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QSphereGeometryView23generateTangentsChange'
        'dEb',
        generateTangents,
    )
