"""
Surface3DController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/surface3dcontroller_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Surface3DController to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import Abstract3DController, QAbstract3DAxis, QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect
  from . import Q3DScene, QAbstract3DSeries, QSurface3DSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSurface3DSeries = WAIT['QtDataVisualization:QSurface3DSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Surface3DController(Abstract3DController):
  """
  The cute side of Qt's Surface3DController: a plain Python object standing
  in front of one C++ Surface3DController.

  It is built on the cute 'Abstract3DController', as Qt's Surface3DController
  is built on Qt's Abstract3DController, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Surface3DController that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr',
  'initializeOpenGL', 'synchDataToRenderer', 'setSelectionMode',
  'setSelectedPoint', 'clearSelection', 'selectedSeries',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleAxisRangeChangedBySender', 'handleSeriesVisibilityChangedBySender',
  'handlePendingClick', 'adjustAxisRanges', 'invalidSelectionPosition',
  'isFlatShadingSupported', 'addSeries', 'removeSeries', 'surfaceSeriesList',
  'setFlipHorizontalGrid', 'flipHorizontalGrid', 'updateSurfaceTexture',
  'handleArrayReset', 'handleRowsAdded', 'handleRowsChanged',
  'handleRowsRemoved', 'handleRowsInserted', 'handleItemChanged',
  'handleFlatShadingSupportedChange', 'selectedSeriesChanged',
  'flipHorizontalGridChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Surface3DController::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Surface3DController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Surface3DController::~Surface3DController()': the destructor:
    Python never removes a C++ Surface3DController.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Surface3DController is created at the first use, not by
    'Surface3DController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Surface3DController.
  - Qt tells when it has removed the C++ Surface3DController. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside Surface3DController, each a class in here
  #  as in C++.

  class ChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Surface3DController::ChangeItem: a plain Python
    object standing in front of one C++ Surface3DController::ChangeItem.

    C++ hands a Surface3DController::ChangeItem around as a copy, so every
    C++ Surface3DController::ChangeItem behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's Surface3DController::ChangeItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Surface3DController::ChangeItem::~ChangeItem()': the destructor:
      Python removes its C++ Surface3DController::ChangeItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ Surface3DController::ChangeItem is created at the first use,
      not by 'Surface3DController::ChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Surface3DController::ChangeItem back gives a copy
      the ritual made for Python, in a new cute
      Surface3DController::ChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Surface3DController::ChangeItem'

    #  Qt's '~Surface3DController::ChangeItem()'. Naming it makes this a
    #  value class: Python owns every C++ Surface3DController::ChangeItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19Surface3DController10ChangeItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class ChangeRow(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Surface3DController::ChangeRow: a plain Python
    object standing in front of one C++ Surface3DController::ChangeRow.

    C++ hands a Surface3DController::ChangeRow around as a copy, so every C++
    Surface3DController::ChangeRow behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's Surface3DController::ChangeRow yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Surface3DController::ChangeRow::~ChangeRow()': the destructor:
      Python removes its C++ Surface3DController::ChangeRow by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Surface3DController::ChangeRow is created at the first use, not
      by 'Surface3DController::ChangeRow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Surface3DController::ChangeRow back gives a copy
      the ritual made for Python, in a new cute
      Surface3DController::ChangeRow.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Surface3DController::ChangeRow'

    #  Qt's '~Surface3DController::ChangeRow()'. Naming it makes this a value
    #  class: Python owns every C++ Surface3DController::ChangeRow behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19Surface3DController9ChangeRowD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString Surface3DController::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3dcontroller.html#tr

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
    #  QString Surface3DController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19Surface3DController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint Surface3DController::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Surface3DController::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN19Surface3DController24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Surface3DController'

  #  A C++ Surface3DController Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Surface3DController'

  #  The functions Qt calls itself that Surface3DController is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'surfaceSeriesList': (
          'QList<QSurface3DSeries *> '
          'Surface3DController::surfaceSeriesList()',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Surface3DController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Surface3DController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19Surface3DController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectedSeries(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *Surface3DController::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#selectedSeries

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *Surface3DController::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK19Surface3DController14selectedSeriesEv',
    )
    from . import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def flipHorizontalGrid(self) -> bool:
    """
    Calls Qt's 'bool Surface3DController::flipHorizontalGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#flipHorizontalGrid
    """
    #  bool Surface3DController::flipHorizontalGrid() const
    return self.uglySide.call(
        'ritual_ZNK19Surface3DController18flipHorizontalGridEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DGraph.SelectionFlags)
  def setSelectionMode(self, mode: QAbstract3DGraph.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    Surface3DController::setSelectionMode(QAbstract3DGraph::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#setSelectionMode

    Parameters
    ----------

    mode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Surface3DController::setSelectionMode(QAbstract3DGraph::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN19Surface3DController16setSelectionModeE6QFlagsIN16QAbstr'
        'act3DGraph13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Surface3DController16setSelectionModeE6QFlagsIN16'
          'QAbstract3DGraph13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QPoint, QSurface3DSeries, bool)
  @overload(QPoint, NoneType, bool)
  def setSelectedPoint(
      self,
      position: QPoint,
      series: Optional[QSurface3DSeries],
      enterSlice: bool,
  ) -> None:
    """
    Calls Qt's 'void Surface3DController::setSelectedPoint(const QPoint
    &position, QSurface3DSeries *series, bool enterSlice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#setSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enterSlice : bool
      Passed on as it is.
    """
    #  void Surface3DController::setSelectedPoint(const QPoint &position,
    #      QSurface3DSeries *series, bool enterSlice)
    self.uglySide.call(
        'ritual_ZN19Surface3DController16setSelectedPointERK6QPointP16QSurf'
        'ace3DSeriesb',
        self._valueOf(position), self._addressOf(series), enterSlice,
    )

  @overload(bool)
  def setFlipHorizontalGrid(self, flip: bool) -> None:
    """
    Calls Qt's 'void Surface3DController::setFlipHorizontalGrid(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#setFlipHorizontalGrid

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Surface3DController::setFlipHorizontalGrid(bool flip)
    self.uglySide.call(
        'ritual_ZN19Surface3DController21setFlipHorizontalGridEb', flip,
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

  @overload(QRect)
  @overload(QRect, Q3DScene)
  @overload(QRect, NoneType)
  def __init__(self, rect: QRect, scene: Optional[Q3DScene] = None) -> None:
    """
    Notes what was given, for Qt's
    'Surface3DController::Surface3DController(QRect rect, Q3DScene *scene)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#Surface3DController

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Surface3DController::Surface3DController(QRect rect, Q3DScene *scene)
    self._noteCreation(Surface3DController, lambda: Rituals.call(
        'ritual_ZN19Surface3DControllerC1E5QRectP8Q3DScene',
        self._valueOf(rect), self._addressOf(scene),
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

  def initializeOpenGL(self) -> None:
    """
    Calls Qt's 'void Surface3DController::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#initializeOpenGL
    """
    #  void Surface3DController::initializeOpenGL()
    ritual = 'ritual_ZN19Surface3DController16initializeOpenGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Surface3DController16initializeOpenGLEv'
    self.uglySide.call(ritual)

  def synchDataToRenderer(self) -> None:
    """
    Calls Qt's 'void Surface3DController::synchDataToRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#synchDataToRenderer
    """
    #  void Surface3DController::synchDataToRenderer()
    ritual = 'ritual_ZN19Surface3DController19synchDataToRendererEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Surface3DController19synchDataToRendererEv'
    self.uglySide.call(ritual)

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void Surface3DController::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#clearSelection
    """
    #  void Surface3DController::clearSelection()
    ritual = 'ritual_ZN19Surface3DController14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Surface3DController14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DController::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void Surface3DController::
    #      handleAxisAutoAdjustRangeChangedInOrientation(QAbstract3DAxis::
    #      AxisOrientation orientation, bool autoAdjust)
    ritual = (
        'ritual_ZN19Surface3DController45handleAxisAutoAdjustRangeChangedIn'
        'OrientationEN15QAbstract3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Surface3DController45handleAxisAutoAdjustRangeCha'
          'ngedInOrientationEN15QAbstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, autoAdjust)

  @overload(QObject)
  @overload(NoneType)
  def handleAxisRangeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DController::handleAxisRangeChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DController::handleAxisRangeChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19Surface3DController30handleAxisRangeChangedBySenderEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Surface3DController30handleAxisRangeChangedBySend'
          'erEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DController::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Surface3DController::handleSeriesVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19Surface3DController37handleSeriesVisibilityChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Surface3DController37handleSeriesVisibilityChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def handlePendingClick(self) -> None:
    """
    Calls Qt's 'void Surface3DController::handlePendingClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handlePendingClick
    """
    #  void Surface3DController::handlePendingClick()
    ritual = 'ritual_ZN19Surface3DController18handlePendingClickEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Surface3DController18handlePendingClickEv'
    self.uglySide.call(ritual)

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void Surface3DController::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#adjustAxisRanges
    """
    #  void Surface3DController::adjustAxisRanges()
    ritual = 'ritual_ZN19Surface3DController16adjustAxisRangesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Surface3DController16adjustAxisRangesEv'
    self.uglySide.call(ritual)

  def isFlatShadingSupported(self) -> bool:
    """
    Calls Qt's 'bool Surface3DController::isFlatShadingSupported()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#isFlatShadingSupported
    """
    #  bool Surface3DController::isFlatShadingSupported()
    return self.uglySide.call(
        'ritual_ZN19Surface3DController22isFlatShadingSupportedEv',
    )

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Surface3DController::addSeries(QAbstract3DSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3dcontroller.html#addSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DController::addSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN19Surface3DController9addSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Surface3DController9addSeriesEP17QAbstract3DSerie'
          's')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Surface3DController::removeSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DController::removeSeries(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN19Surface3DController12removeSeriesEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Surface3DController12removeSeriesEP17QAbstract3DS'
          'eries')
    self.uglySide.call(ritual, self._addressOf(series))

  def surfaceSeriesList(self) -> QList[QSurface3DSeries]:
    """
    Calls Qt's 'QList<QSurface3DSeries *>
    Surface3DController::surfaceSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#surfaceSeriesList

    Returns
    -------

    QList[QSurface3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSurface3DSeries *> Surface3DController::surfaceSeriesList()
    address = self.uglySide.call(
        'ritual_ZN19Surface3DController17surfaceSeriesListEv',
    )
    from . import QSurface3DSeries
    return QList[QSurface3DSeries]._cuteOwning(address)

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def updateSurfaceTexture(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void
    Surface3DController::updateSurfaceTexture(QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#updateSurfaceTexture

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DController::updateSurfaceTexture(QSurface3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19Surface3DController20updateSurfaceTextureEP16QSurface3D'
        'Series',
        self._addressOf(series),
    )

  def handleArrayReset(self) -> None:
    """
    Calls Qt's 'void Surface3DController::handleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handleArrayReset
    """
    #  void Surface3DController::handleArrayReset()
    self.uglySide.call('ritual_ZN19Surface3DController16handleArrayResetEv')

  @overload(int, int)
  def handleRowsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Surface3DController::handleRowsAdded(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handleRowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Surface3DController::handleRowsAdded(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN19Surface3DController15handleRowsAddedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Surface3DController::handleRowsChanged(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handleRowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Surface3DController::handleRowsChanged(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN19Surface3DController17handleRowsChangedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Surface3DController::handleRowsRemoved(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handleRowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Surface3DController::handleRowsRemoved(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN19Surface3DController17handleRowsRemovedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Surface3DController::handleRowsInserted(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handleRowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Surface3DController::handleRowsInserted(int startIndex, int
    #      count)
    self.uglySide.call(
        'ritual_ZN19Surface3DController18handleRowsInsertedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void Surface3DController::handleItemChanged(int rowIndex, int
    columnIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#handleItemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void Surface3DController::handleItemChanged(int rowIndex, int
    #      columnIndex)
    self.uglySide.call(
        'ritual_ZN19Surface3DController17handleItemChangedEii',
        rowIndex, columnIndex,
    )

  @overload(bool)
  def handleFlatShadingSupportedChange(self, supported: bool) -> None:
    """
    Calls Qt's 'void
    Surface3DController::handleFlatShadingSupportedChange(bool supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html

    Parameters
    ----------

    supported : bool
      Passed on as it is.
    """
    #  void Surface3DController::handleFlatShadingSupportedChange(bool
    #      supported)
    self.uglySide.call(
        'ritual_ZN19Surface3DController32handleFlatShadingSupportedChangeEb',
        supported,
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DController::selectedSeriesChanged(QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DController::selectedSeriesChanged(QSurface3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19Surface3DController21selectedSeriesChangedEP16QSurface3'
        'DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def flipHorizontalGridChanged(self, flip: bool) -> None:
    """
    Calls Qt's 'void Surface3DController::flipHorizontalGridChanged(bool
    flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3dcontroller.html#flipHorizontalGridChanged

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Surface3DController::flipHorizontalGridChanged(bool flip)
    self.uglySide.call(
        'ritual_ZN19Surface3DController25flipHorizontalGridChangedEb', flip,
    )
