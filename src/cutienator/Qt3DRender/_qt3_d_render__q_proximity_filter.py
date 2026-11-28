"""
Qt3DRender::QProximityFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qproximityfilter.h, Qt 6.12.0. Changes made here are lost.
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProximityFilter(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QProximityFilter: a plain Python object
  standing in front of one C++ Qt3DRender::QProximityFilter.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QProximityFilter is built on Qt's Qt3DRender::QFrameGraphNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QProximityFilter that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr', 'entity',
  'distanceThreshold', 'setEntity', 'setDistanceThreshold', 'entityChanged',
  'distanceThresholdChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QProximityFilter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QProximityFilter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QProximityFilter::~QProximityFilter()': the destructor:
    Python never removes a C++ Qt3DRender::QProximityFilter.
  - Qt's
    'Qt3DRender::QProximityFilter::QProximityFilter(QProximityFilterPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QProximityFilterPrivate
    *Qt3DRender::QProximityFilter::d_func() const': takes in Python what
    'QProximityFilterPrivate *Qt3DRender::QProximityFilter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QProximityFilter is created at the first use, not by
    'Qt3DRender::QProximityFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QProximityFilter.
  - Qt tells when it has removed the C++ Qt3DRender::QProximityFilter. Every
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
    Calls Qt's 'QString Qt3DRender::QProximityFilter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#tr

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
    #  QString Qt3DRender::QProximityFilter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QProximityFilter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QProximityFilter'

  #  A C++ Qt3DRender::QProximityFilter Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QProximityFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QProximityFilter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QProximityFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QProximityFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def entity(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::QProximityFilter::entity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#entity

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::QProximityFilter::entity() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QProximityFilter6entityEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  def distanceThreshold(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QProximityFilter::distanceThreshold()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#distanceThreshold
    """
    #  float Qt3DRender::QProximityFilter::distanceThreshold() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QProximityFilter17distanceThresholdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QProximityFilter::setEntity(Qt3DCore::QEntity *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#setEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QProximityFilter::setEntity(Qt3DCore::QEntity
    #      *entity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QProximityFilter9setEntityEPN8Qt3DCore7QEnt'
        'ityE',
        self._addressOf(entity),
    )

  @overload(float)
  def setDistanceThreshold(self, distanceThreshold: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QProximityFilter::setDistanceThreshold(float
    distanceThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html

    Parameters
    ----------

    distanceThreshold : float
      Passed on as it is.
    """
    #  void Qt3DRender::QProximityFilter::setDistanceThreshold(float
    #      distanceThreshold)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QProximityFilter20setDistanceThresholdEf',
        distanceThreshold,
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
    'Qt3DRender::QProximityFilter::QProximityFilter(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#QProximityFilter

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QProximityFilter::QProximityFilter(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QProximityFilter, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QProximityFilterC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def entityChanged(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QProximityFilter::entityChanged(Qt3DCore::QEntity *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#entityChanged

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QProximityFilter::entityChanged(Qt3DCore::QEntity
    #      *entity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QProximityFilter13entityChangedEPN8Qt3DCore'
        '7QEntityE',
        self._addressOf(entity),
    )

  @overload(float)
  def distanceThresholdChanged(self, distanceThreshold: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QProximityFilter::distanceThresholdChanged(float
    distanceThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html

    Parameters
    ----------

    distanceThreshold : float
      Passed on as it is.
    """
    #  void Qt3DRender::QProximityFilter::distanceThresholdChanged(float
    #      distanceThreshold)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QProximityFilter24distanceThresholdChangedE'
        'f',
        distanceThreshold,
    )

  def d_func(self) -> Optional[Qt3DRender.QProximityFilterPrivate]:
    """
    Calls Qt's 'QProximityFilterPrivate
    *Qt3DRender::QProximityFilter::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qproximityfilter.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QProximityFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProximityFilterPrivate *Qt3DRender::QProximityFilter::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender16QProximityFilter6d_funcEv',
    )
    return Qt3DRender.QProximityFilterPrivate._cuteAt(address)
