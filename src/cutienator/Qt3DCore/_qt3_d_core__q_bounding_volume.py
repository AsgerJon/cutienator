"""
Qt3DCore::QBoundingVolume binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qboundingvolume.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

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


class QBoundingVolume(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DCore::QBoundingVolume: a plain Python object
  standing in front of one C++ Qt3DCore::QBoundingVolume.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DCore::QBoundingVolume is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QBoundingVolume that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr', 'view',
  'implicitMinPoint', 'implicitMaxPoint', 'areImplicitPointsValid',
  'minPoint', 'maxPoint', 'setView', 'setMinPoint', 'setMaxPoint',
  'updateImplicitBounds', 'viewChanged', 'implicitMinPointChanged',
  'implicitMaxPointChanged', 'implicitPointsValidChanged', 'minPointChanged',
  'maxPointChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QBoundingVolume::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QBoundingVolume::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QBoundingVolume::~QBoundingVolume()': the destructor:
    Python never removes a C++ Qt3DCore::QBoundingVolume.
  - Qt's 'Qt3DCore::QBoundingVolume::QBoundingVolume(QBoundingVolumePrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QBoundingVolumePrivate *Qt3DCore::QBoundingVolume::d_func()
    const': takes in Python what 'QBoundingVolumePrivate
    *Qt3DCore::QBoundingVolume::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QBoundingVolume is created at the first use, not by
    'Qt3DCore::QBoundingVolume(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QBoundingVolume.
  - Qt tells when it has removed the C++ Qt3DCore::QBoundingVolume. Every
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
    Calls Qt's 'QString Qt3DCore::QBoundingVolume::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#tr

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
    #  QString Qt3DCore::QBoundingVolume::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QBoundingVolume'

  #  A C++ Qt3DCore::QBoundingVolume Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QBoundingVolume'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QBoundingVolume::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QBoundingVolume::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[Qt3DCore.QGeometryView]:
    """
    Calls Qt's 'QGeometryView *Qt3DCore::QBoundingVolume::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#view

    Returns
    -------

    Optional[Qt3DCore.QGeometryView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometryView *Qt3DCore::QBoundingVolume::view() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume4viewEv',
    )
    return Qt3DCore.QGeometryView._cuteAt(address)

  def implicitMinPoint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QBoundingVolume::implicitMinPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#implicitMinPoint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QBoundingVolume::implicitMinPoint() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume16implicitMinPointEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def implicitMaxPoint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QBoundingVolume::implicitMaxPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#implicitMaxPoint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QBoundingVolume::implicitMaxPoint() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume16implicitMaxPointEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def areImplicitPointsValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QBoundingVolume::areImplicitPointsValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html
    """
    #  bool Qt3DCore::QBoundingVolume::areImplicitPointsValid() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume22areImplicitPointsValidEv',
    )

  def minPoint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QBoundingVolume::minPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#minPoint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QBoundingVolume::minPoint() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume8minPointEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def maxPoint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QBoundingVolume::maxPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#maxPoint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QBoundingVolume::maxPoint() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QBoundingVolume8maxPointEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QGeometryView'])
  @overload(NoneType)
  def setView(self, view: Optional[Qt3DCore.QGeometryView]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::setView(QGeometryView
    *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#setView

    Parameters
    ----------

    view : Optional[Qt3DCore.QGeometryView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBoundingVolume::setView(QGeometryView *view)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume7setViewEPNS_13QGeometryViewE',
        self._addressOf(view),
    )

  @overload(QVector3D)
  def setMinPoint(self, minPoint: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::setMinPoint(const QVector3D
    &minPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#setMinPoint

    Parameters
    ----------

    minPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QBoundingVolume::setMinPoint(const QVector3D &minPoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume11setMinPointERK9QVector3D',
        self._valueOf(minPoint),
    )

  @overload(QVector3D)
  def setMaxPoint(self, maxPoint: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::setMaxPoint(const QVector3D
    &maxPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#setMaxPoint

    Parameters
    ----------

    maxPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QBoundingVolume::setMaxPoint(const QVector3D &maxPoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume11setMaxPointERK9QVector3D',
        self._valueOf(maxPoint),
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
    'Qt3DCore::QBoundingVolume::QBoundingVolume(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#QBoundingVolume

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QBoundingVolume::QBoundingVolume(Qt3DCore::QNode *parent)
    self._noteCreation(QBoundingVolume, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QBoundingVolumeC1EPNS_5QNodeE',
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

  def updateImplicitBounds(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QBoundingVolume::updateImplicitBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#updateImplicitBounds
    """
    #  bool Qt3DCore::QBoundingVolume::updateImplicitBounds()
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume20updateImplicitBoundsEv',
    )

  @overload(WAIT['Qt3DCore.QGeometryView'])
  @overload(NoneType)
  def viewChanged(self, view: Optional[Qt3DCore.QGeometryView]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::viewChanged(QGeometryView
    *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#viewChanged

    Parameters
    ----------

    view : Optional[Qt3DCore.QGeometryView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBoundingVolume::viewChanged(QGeometryView *view)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume11viewChangedEPNS_13QGeometryVi'
        'ewE',
        self._addressOf(view),
    )

  @overload(QVector3D)
  def implicitMinPointChanged(self, implicitMinPoint: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::implicitMinPointChanged(const
    QVector3D &implicitMinPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html

    Parameters
    ----------

    implicitMinPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QBoundingVolume::implicitMinPointChanged(const
    #      QVector3D &implicitMinPoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume23implicitMinPointChangedERK9QV'
        'ector3D',
        self._valueOf(implicitMinPoint),
    )

  @overload(QVector3D)
  def implicitMaxPointChanged(self, implicitMaxPoint: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::implicitMaxPointChanged(const
    QVector3D &implicitMaxPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html

    Parameters
    ----------

    implicitMaxPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QBoundingVolume::implicitMaxPointChanged(const
    #      QVector3D &implicitMaxPoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume23implicitMaxPointChangedERK9QV'
        'ector3D',
        self._valueOf(implicitMaxPoint),
    )

  @overload(bool)
  def implicitPointsValidChanged(self, implicitPointsValid: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QBoundingVolume::implicitPointsValidChanged(bool
    implicitPointsValid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html

    Parameters
    ----------

    implicitPointsValid : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QBoundingVolume::implicitPointsValidChanged(bool
    #      implicitPointsValid)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume26implicitPointsValidChangedEb',
        implicitPointsValid,
    )

  @overload(QVector3D)
  def minPointChanged(self, minPoint: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::minPointChanged(QVector3D
    minPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#minPointChanged

    Parameters
    ----------

    minPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QBoundingVolume::minPointChanged(QVector3D minPoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume15minPointChangedE9QVector3D',
        self._valueOf(minPoint),
    )

  @overload(QVector3D)
  def maxPointChanged(self, maxPoint: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolume::maxPointChanged(QVector3D
    maxPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#maxPointChanged

    Parameters
    ----------

    maxPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QBoundingVolume::maxPointChanged(QVector3D maxPoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume15maxPointChangedE9QVector3D',
        self._valueOf(maxPoint),
    )

  def d_func(self) -> Optional[Qt3DCore.QBoundingVolumePrivate]:
    """
    Calls Qt's 'QBoundingVolumePrivate *Qt3DCore::QBoundingVolume::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolume.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QBoundingVolumePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoundingVolumePrivate *Qt3DCore::QBoundingVolume::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QBoundingVolume6d_funcEv',
    )
    return Qt3DCore.QBoundingVolumePrivate._cuteAt(address)
