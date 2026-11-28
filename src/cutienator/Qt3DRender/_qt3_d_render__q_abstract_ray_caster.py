"""
Qt3DRender::QAbstractRayCaster binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qabstractraycaster.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractRayCaster(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QAbstractRayCaster: a plain Python object
  standing in front of one C++ Qt3DRender::QAbstractRayCaster.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QAbstractRayCaster is built on Qt's Qt3DCore::QComponent, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractRayCaster that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'runMode', 'filterMode', 'addLayer', 'removeLayer', 'setRunMode',
  'setFilterMode', 'runModeChanged', 'filterModeChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QAbstractRayCaster::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QAbstractRayCaster::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QAbstractRayCaster::~QAbstractRayCaster()': the
    destructor: Python never removes a C++ Qt3DRender::QAbstractRayCaster.
  - Qt's 'Hits Qt3DRender::QAbstractRayCaster::hits() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<QLayer *> Qt3DRender::QAbstractRayCaster::layers() const':
    gives a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::QAbstractRayCaster::hitsChanged(const
    Qt3DRender::QAbstractRayCaster::Hits &hits)': takes a type Python has no
    way to hand over yet.
  - Qt's 'Qt3DRender::QAbstractRayCaster::QAbstractRayCaster(
    QAbstractRayCasterPrivate &dd, QNode *parent)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QAbstractRayCasterPrivate
    *Qt3DRender::QAbstractRayCaster::d_func() const': takes in Python what
    'QAbstractRayCasterPrivate *Qt3DRender::QAbstractRayCaster::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractRayCaster is created at the first use, not
    by 'Qt3DRender::QAbstractRayCaster(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractRayCaster.
  - Qt tells when it has removed the C++ Qt3DRender::QAbstractRayCaster.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QAbstractRayCaster that has no cute
    function yet, 'hits', 'hitsChanged', 'layers', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QAbstractRayCaster, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class FilterMode(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractRayCaster::FilterMode' of Qt, with the 4
    names Qt gives in it.
    """

    AcceptAnyMatchingLayers = Kee[int](0)
    AcceptAllMatchingLayers = Kee[int](1)
    DiscardAnyMatchingLayers = Kee[int](2)
    DiscardAllMatchingLayers = Kee[int](3)

  class RunMode(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractRayCaster::RunMode' of Qt, with the 2
    names Qt gives in it.
    """

    Continuous = Kee[int](0)
    SingleShot = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QAbstractRayCaster::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#tr

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
    #  QString Qt3DRender::QAbstractRayCaster::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractRayCaster'

  #  A C++ Qt3DRender::QAbstractRayCaster Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QAbstractRayCaster'

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
    *Qt3DRender::QAbstractRayCaster::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QAbstractRayCaster::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QAbstractRayCaster10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def runMode(self) -> RunMode:
    """
    Calls Qt's 'RunMode Qt3DRender::QAbstractRayCaster::runMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#runMode

    Returns
    -------

    RunMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RunMode(number)' gives.
    """
    #  RunMode Qt3DRender::QAbstractRayCaster::runMode() const
    return QAbstractRayCaster.RunMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QAbstractRayCaster7runModeEv',
    ))

  def filterMode(self) -> FilterMode:
    """
    Calls Qt's 'FilterMode Qt3DRender::QAbstractRayCaster::filterMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#filterMode

    Returns
    -------

    FilterMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FilterMode(number)'
      gives.
    """
    #  FilterMode Qt3DRender::QAbstractRayCaster::filterMode() const
    return QAbstractRayCaster.FilterMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QAbstractRayCaster10filterModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RunMode)
  def setRunMode(self, runMode: RunMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractRayCaster::setRunMode(RunMode
    runMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#setRunMode

    Parameters
    ----------

    runMode : RunMode
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractRayCaster::setRunMode(RunMode runMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster10setRunModeENS0_7RunMode'
        'E',
        runMode.value,
    )

  @overload(FilterMode)
  def setFilterMode(self, filterMode: FilterMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractRayCaster::setFilterMode(FilterMode
    filterMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#setFilterMode

    Parameters
    ----------

    filterMode : FilterMode
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractRayCaster::setFilterMode(FilterMode
    #      filterMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster13setFilterModeENS0_10Fil'
        'terModeE',
        filterMode.value,
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
    'Qt3DRender::QAbstractRayCaster::QAbstractRayCaster(QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QAbstractRayCaster::QAbstractRayCaster(QNode *parent)
    self._noteCreation(QAbstractRayCaster, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCasterC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DRender.QLayer'])
  @overload(NoneType)
  def addLayer(self, layer: Optional[Qt3DRender.QLayer]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractRayCaster::addLayer(QLayer
    *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#addLayer

    Parameters
    ----------

    layer : Optional[Qt3DRender.QLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QAbstractRayCaster::addLayer(QLayer *layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster8addLayerEPNS_6QLayerE',
        self._addressOf(layer),
    )

  @overload(WAIT['Qt3DRender.QLayer'])
  @overload(NoneType)
  def removeLayer(self, layer: Optional[Qt3DRender.QLayer]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractRayCaster::removeLayer(QLayer
    *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#removeLayer

    Parameters
    ----------

    layer : Optional[Qt3DRender.QLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QAbstractRayCaster::removeLayer(QLayer *layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster11removeLayerEPNS_6QLayer'
        'E',
        self._addressOf(layer),
    )

  @overload(RunMode)
  def runModeChanged(self, runMode: RunMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractRayCaster::runModeChanged(Qt3DRender::
    QAbstractRayCaster::RunMode runMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#runModeChanged

    Parameters
    ----------

    runMode : RunMode
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractRayCaster::runModeChanged(Qt3DRender::
    #      QAbstractRayCaster::RunMode runMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster14runModeChangedENS0_7Run'
        'ModeE',
        runMode.value,
    )

  @overload(FilterMode)
  def filterModeChanged(self, filterMode: FilterMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractRayCaster::filterModeChanged(Qt3DRender::
    QAbstractRayCaster::FilterMode filterMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html

    Parameters
    ----------

    filterMode : FilterMode
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractRayCaster::filterModeChanged(Qt3DRender::
    #      QAbstractRayCaster::FilterMode filterMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster17filterModeChangedENS0_1'
        '0FilterModeE',
        filterMode.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QAbstractRayCasterPrivate]:
    """
    Calls Qt's 'QAbstractRayCasterPrivate
    *Qt3DRender::QAbstractRayCaster::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycaster.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractRayCasterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractRayCasterPrivate *Qt3DRender::QAbstractRayCaster::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender18QAbstractRayCaster6d_funcEv',
    )
    return Qt3DRender.QAbstractRayCasterPrivate._cuteAt(address)

  @staticmethod
  def hits(*__, **_) -> Never:
    """
    Qt's 'Hits Qt3DRender::QAbstractRayCaster::hits() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractRayCaster.hits' has no cute function yet. "
        "Qt's 'Hits Qt3DRender::QAbstractRayCaster::hits() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def hitsChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QAbstractRayCaster::hitsChanged(const
    Qt3DRender::QAbstractRayCaster::Hits &hits)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractRayCaster.hitsChanged' has no cute function "
        "yet. Qt's 'void Qt3DRender::QAbstractRayCaster::hitsChanged(const "
        "Qt3DRender::QAbstractRayCaster::Hits &hits)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def layers(*__, **_) -> Never:
    """
    Qt's 'QList<QLayer *> Qt3DRender::QAbstractRayCaster::layers() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractRayCaster.layers' has no cute function yet. "
        "Qt's 'QList<QLayer *> Qt3DRender::QAbstractRayCaster::layers() "
        "const': gives a type Python has no way to take yet.")
