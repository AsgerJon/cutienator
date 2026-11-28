"""
Qt3DRender::QClipPlane binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qclipplane.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QClipPlane(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QClipPlane: a plain Python object
  standing in front of one C++ Qt3DRender::QClipPlane.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QClipPlane is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QClipPlane that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'planeIndex',
  'normal', 'distance', 'setPlaneIndex', 'setNormal', 'setDistance',
  'planeIndexChanged', 'normalChanged', 'distanceChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QClipPlane::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QClipPlane::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QClipPlane::~QClipPlane()': the destructor: Python
    never removes a C++ Qt3DRender::QClipPlane.
  - Qt's 'const QClipPlanePrivate *Qt3DRender::QClipPlane::d_func() const':
    takes in Python what 'QClipPlanePrivate
    *Qt3DRender::QClipPlane::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QClipPlane is created at the first use, not by
    'Qt3DRender::QClipPlane(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QClipPlane.
  - Qt tells when it has removed the C++ Qt3DRender::QClipPlane. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QClipPlane::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qclipplane.html#tr

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
    #  QString Qt3DRender::QClipPlane::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QClipPlane2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QClipPlane'

  #  A C++ Qt3DRender::QClipPlane Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QClipPlane'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QClipPlane::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QClipPlane::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QClipPlane10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def planeIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QClipPlane::planeIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#planeIndex
    """
    #  int Qt3DRender::QClipPlane::planeIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QClipPlane10planeIndexEv',
    )

  def normal(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QClipPlane::normal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qclipplane.html#normal

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QClipPlane::normal() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QClipPlane6normalEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def distance(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QClipPlane::distance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#distance
    """
    #  float Qt3DRender::QClipPlane::distance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QClipPlane8distanceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPlaneIndex(self, a0: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClipPlane::setPlaneIndex(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#setPlaneIndex

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void Qt3DRender::QClipPlane::setPlaneIndex(int a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane13setPlaneIndexEi', a0,
    )

  @overload(QVector3D)
  def setNormal(self, a0: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClipPlane::setNormal(QVector3D a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#setNormal

    Parameters
    ----------

    a0 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QClipPlane::setNormal(QVector3D a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane9setNormalE9QVector3D',
        self._valueOf(a0),
    )

  @overload(float)
  def setDistance(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClipPlane::setDistance(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#setDistance

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DRender::QClipPlane::setDistance(float a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane11setDistanceEf', a0,
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
    'Qt3DRender::QClipPlane::QClipPlane(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#QClipPlane

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QClipPlane::QClipPlane(Qt3DCore::QNode *parent)
    self._noteCreation(QClipPlane, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QClipPlaneC1EPN8Qt3DCore5QNodeE',
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

  @overload(int)
  def planeIndexChanged(self, planeIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClipPlane::planeIndexChanged(int
    planeIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#planeIndexChanged

    Parameters
    ----------

    planeIndex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QClipPlane::planeIndexChanged(int planeIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane17planeIndexChangedEi', planeIndex,
    )

  @overload(QVector3D)
  def normalChanged(self, normal: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClipPlane::normalChanged(QVector3D
    normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#normalChanged

    Parameters
    ----------

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QClipPlane::normalChanged(QVector3D normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane13normalChangedE9QVector3D',
        self._valueOf(normal),
    )

  @overload(float)
  def distanceChanged(self, distance: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClipPlane::distanceChanged(float
    distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclipplane.html#distanceChanged

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void Qt3DRender::QClipPlane::distanceChanged(float distance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane15distanceChangedEf', distance,
    )

  def d_func(self) -> Optional[Qt3DRender.QClipPlanePrivate]:
    """
    Calls Qt's 'QClipPlanePrivate *Qt3DRender::QClipPlane::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qclipplane.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QClipPlanePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QClipPlanePrivate *Qt3DRender::QClipPlane::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QClipPlane6d_funcEv',
    )
    return Qt3DRender.QClipPlanePrivate._cuteAt(address)
