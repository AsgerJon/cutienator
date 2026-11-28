"""
Bars3DController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/bars3dcontroller_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Bars3DController to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import Abstract3DController, QAbstract3DAxis, QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSizeF
  from . import Q3DScene, QAbstract3DSeries, QBar3DSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QBar3DSeries = WAIT['QtDataVisualization:QBar3DSeries']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Bars3DController(Abstract3DController):
  """
  The cute side of Qt's Bars3DController: a plain Python object standing in
  front of one C++ Bars3DController.

  It is built on the cute 'Abstract3DController', as Qt's Bars3DController is
  built on Qt's Abstract3DController, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Bars3DController that has a ritual and that Python
  can call so far, 44 names in all: 'metaObject', 'tr', 'initializeOpenGL',
  'synchDataToRenderer', 'setMultiSeriesScaling', 'multiSeriesScaling',
  'setBarSpecs', 'setBarSeriesMargin', 'barSeriesMargin', 'barThickness',
  'barSpacing', 'isBarSpecRelative', 'setFloorLevel', 'floorLevel',
  'selectedSeries', 'setSelectionMode', 'setSelectedBar', 'clearSelection',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleSeriesVisibilityChangedBySender', 'handlePendingClick',
  'invalidSelectionPosition', 'setAxisX', 'setAxisZ', 'setPrimarySeries',
  'primarySeries', 'addSeries', 'removeSeries', 'insertSeries',
  'barSeriesList', 'handleAxisRangeChangedBySender', 'adjustAxisRanges',
  'handleArrayReset', 'handleRowsAdded', 'handleRowsChanged',
  'handleRowsRemoved', 'handleRowsInserted', 'handleItemChanged',
  'handleDataRowLabelsChanged', 'handleDataColumnLabelsChanged',
  'handleRowColorsChanged', 'primarySeriesChanged', 'selectedSeriesChanged',
  'createDefaultAxis'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Bars3DController::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Bars3DController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Bars3DController::~Bars3DController()': the destructor: Python
    never removes a C++ Bars3DController.
  - Qt's 'void Bars3DController::adjustSelectionPosition(QPoint &pos, const
    QBar3DSeries *series)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 53 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Bars3DController is created at the first use, not by
    'Bars3DController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Bars3DController.
  - Qt tells when it has removed the C++ Bars3DController. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Bars3DController that has no cute function yet,
    'adjustSelectionPosition', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside Bars3DController, each a class in here as
  #  in C++.

  class ChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Bars3DController::ChangeItem: a plain Python object
    standing in front of one C++ Bars3DController::ChangeItem.

    C++ hands a Bars3DController::ChangeItem around as a copy, so every C++
    Bars3DController::ChangeItem behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's Bars3DController::ChangeItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Bars3DController::ChangeItem::~ChangeItem()': the destructor:
      Python removes its C++ Bars3DController::ChangeItem by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Bars3DController::ChangeItem is created at the first use, not
      by 'Bars3DController::ChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Bars3DController::ChangeItem back gives a copy the
      ritual made for Python, in a new cute Bars3DController::ChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Bars3DController::ChangeItem'

    #  Qt's '~Bars3DController::ChangeItem()'. Naming it makes this a value
    #  class: Python owns every C++ Bars3DController::ChangeItem behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16Bars3DController10ChangeItemD1Ev'

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
    The cute side of Qt's Bars3DController::ChangeRow: a plain Python object
    standing in front of one C++ Bars3DController::ChangeRow.

    C++ hands a Bars3DController::ChangeRow around as a copy, so every C++
    Bars3DController::ChangeRow behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's Bars3DController::ChangeRow yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Bars3DController::ChangeRow::~ChangeRow()': the destructor:
      Python removes its C++ Bars3DController::ChangeRow by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Bars3DController::ChangeRow is created at the first use, not by
      'Bars3DController::ChangeRow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Bars3DController::ChangeRow back gives a copy the
      ritual made for Python, in a new cute Bars3DController::ChangeRow.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Bars3DController::ChangeRow'

    #  Qt's '~Bars3DController::ChangeRow()'. Naming it makes this a value
    #  class: Python owns every C++ Bars3DController::ChangeRow behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16Bars3DController9ChangeRowD1Ev'

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
    Calls Qt's 'QString Bars3DController::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#tr

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
    #  QString Bars3DController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16Bars3DController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint Bars3DController::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Bars3DController::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN16Bars3DController24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Bars3DController'

  #  A C++ Bars3DController Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Bars3DController'

  #  The functions Qt calls itself that Bars3DController is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'barSeriesList': (
          'QList<QBar3DSeries *> Bars3DController::barSeriesList()',
      ),
  }

  #  The functions Qt calls itself that Bars3DController is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setPrimarySeries': (
          ('_ZN16Bars3DController16setPrimarySeriesEP12QBar3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QBar3DSeries'),
           )),
      ),
      'primarySeries': (
          ('_ZNK16Bars3DController13primarySeriesEv',
           ('address', 'address', 'QtDataVisualization:QBar3DSeries'),
           ()),
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
    Calls Qt's 'const QMetaObject *Bars3DController::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Bars3DController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16Bars3DController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def multiSeriesScaling(self) -> bool:
    """
    Calls Qt's 'bool Bars3DController::multiSeriesScaling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#multiSeriesScaling
    """
    #  bool Bars3DController::multiSeriesScaling() const
    return self.uglySide.call(
        'ritual_ZNK16Bars3DController18multiSeriesScalingEv',
    )

  def floorLevel(self) -> float:
    """
    Calls Qt's 'float Bars3DController::floorLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#floorLevel
    """
    #  float Bars3DController::floorLevel() const
    return self.uglySide.call('ritual_ZNK16Bars3DController10floorLevelEv')

  def selectedSeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Bars3DController::selectedSeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#selectedSeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Bars3DController::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK16Bars3DController14selectedSeriesEv',
    )
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def primarySeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Bars3DController::primarySeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#primarySeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Bars3DController::primarySeries() const
    ritual = 'ritual_ZNK16Bars3DController13primarySeriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16Bars3DController13primarySeriesEv'
    address = self.uglySide.call(ritual)
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setMultiSeriesScaling(self, uniform: bool) -> None:
    """
    Calls Qt's 'void Bars3DController::setMultiSeriesScaling(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#setMultiSeriesScaling

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void Bars3DController::setMultiSeriesScaling(bool uniform)
    self.uglySide.call(
        'ritual_ZN16Bars3DController21setMultiSeriesScalingEb', uniform,
    )

  @overload()
  @overload(float)
  @overload(float, QSizeF)
  @overload(float, QSizeF, bool)
  def setBarSpecs(
      self,
      thicknessRatio: float = 1.0,
      spacing: Optional[QSizeF] = None,
      relative: bool = True,
  ) -> None:
    """
    Calls Qt's 'void Bars3DController::setBarSpecs(GLfloat thicknessRatio,
    const QSizeF &spacing, bool relative)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#setBarSpecs

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    spacing : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF(1.0, 1.0)' is then passed
      on.

    relative : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void Bars3DController::setBarSpecs(GLfloat thicknessRatio, const
    #      QSizeF &spacing, bool relative)
    if spacing is None:
      from ..QtCore import QSizeF
      spacing = QSizeF(1.0, 1.0)
    self.uglySide.call(
        'ritual_ZN16Bars3DController11setBarSpecsEfRK6QSizeFb',
        thicknessRatio, self._valueOf(spacing), relative,
    )

  @overload(QSizeF)
  def setBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void Bars3DController::setBarSeriesMargin(const QSizeF
    &margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#setBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Bars3DController::setBarSeriesMargin(const QSizeF &margin)
    self.uglySide.call(
        'ritual_ZN16Bars3DController18setBarSeriesMarginERK6QSizeF',
        self._valueOf(margin),
    )

  @overload(float)
  def setFloorLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Bars3DController::setFloorLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#setFloorLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Bars3DController::setFloorLevel(float level)
    self.uglySide.call('ritual_ZN16Bars3DController13setFloorLevelEf', level)

  @overload(QAbstract3DGraph.SelectionFlags)
  def setSelectionMode(self, mode: QAbstract3DGraph.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    Bars3DController::setSelectionMode(QAbstract3DGraph::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#setSelectionMode

    Parameters
    ----------

    mode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Bars3DController::setSelectionMode(QAbstract3DGraph::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN16Bars3DController16setSelectionModeE6QFlagsIN16QAbstract'
        '3DGraph13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController16setSelectionModeE6QFlagsIN16QAb'
          'stract3DGraph13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QPoint, QBar3DSeries, bool)
  @overload(QPoint, NoneType, bool)
  def setSelectedBar(
      self,
      position: QPoint,
      series: Optional[QBar3DSeries],
      enterSlice: bool,
  ) -> None:
    """
    Calls Qt's 'void Bars3DController::setSelectedBar(const QPoint &position,
    QBar3DSeries *series, bool enterSlice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#setSelectedBar

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enterSlice : bool
      Passed on as it is.
    """
    #  void Bars3DController::setSelectedBar(const QPoint &position,
    #      QBar3DSeries *series, bool enterSlice)
    self.uglySide.call(
        'ritual_ZN16Bars3DController14setSelectedBarERK6QPointP12QBar3DSeri'
        'esb',
        self._valueOf(position), self._addressOf(series), enterSlice,
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Bars3DController::setAxisX(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::setAxisX(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN16Bars3DController8setAxisXEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController8setAxisXEP15QAbstract3DAxis'
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Bars3DController::setAxisZ(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::setAxisZ(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN16Bars3DController8setAxisZEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController8setAxisZEP15QAbstract3DAxis'
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QBar3DSeries)
  @overload(NoneType)
  def setPrimarySeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Bars3DController::setPrimarySeries(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#setPrimarySeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::setPrimarySeries(QBar3DSeries *series)
    ritual = 'ritual_ZN16Bars3DController16setPrimarySeriesEP12QBar3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController16setPrimarySeriesEP12QBar3DSerie'
          's')
    self.uglySide.call(ritual, self._addressOf(series))

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
    Notes what was given, for Qt's 'Bars3DController::Bars3DController(QRect
    rect, Q3DScene *scene)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#Bars3DController

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Bars3DController::Bars3DController(QRect rect, Q3DScene *scene)
    self._noteCreation(Bars3DController, lambda: Rituals.call(
        'ritual_ZN16Bars3DControllerC1E5QRectP8Q3DScene',
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
    Calls Qt's 'void Bars3DController::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#initializeOpenGL
    """
    #  void Bars3DController::initializeOpenGL()
    ritual = 'ritual_ZN16Bars3DController16initializeOpenGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController16initializeOpenGLEv'
    self.uglySide.call(ritual)

  def synchDataToRenderer(self) -> None:
    """
    Calls Qt's 'void Bars3DController::synchDataToRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#synchDataToRenderer
    """
    #  void Bars3DController::synchDataToRenderer()
    ritual = 'ritual_ZN16Bars3DController19synchDataToRendererEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController19synchDataToRendererEv'
    self.uglySide.call(ritual)

  def barSeriesMargin(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF Bars3DController::barSeriesMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#barSeriesMargin

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF Bars3DController::barSeriesMargin()
    address = self.uglySide.call(
        'ritual_ZN16Bars3DController15barSeriesMarginEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def barThickness(self) -> float:
    """
    Calls Qt's 'GLfloat Bars3DController::barThickness()'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#barThickness
    """
    #  GLfloat Bars3DController::barThickness()
    return self.uglySide.call('ritual_ZN16Bars3DController12barThicknessEv')

  def barSpacing(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF Bars3DController::barSpacing()'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#barSpacing

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF Bars3DController::barSpacing()
    address = self.uglySide.call('ritual_ZN16Bars3DController10barSpacingEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isBarSpecRelative(self) -> bool:
    """
    Calls Qt's 'bool Bars3DController::isBarSpecRelative()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#isBarSpecRelative
    """
    #  bool Bars3DController::isBarSpecRelative()
    return self.uglySide.call(
        'ritual_ZN16Bars3DController17isBarSpecRelativeEv',
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void Bars3DController::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#clearSelection
    """
    #  void Bars3DController::clearSelection()
    ritual = 'ritual_ZN16Bars3DController14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(
    #      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
    ritual = (
        'ritual_ZN16Bars3DController45handleAxisAutoAdjustRangeChangedInOri'
        'entationEN15QAbstract3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController45handleAxisAutoAdjustRangeChange'
          'dInOrientationEN15QAbstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, autoAdjust)

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Bars3DController::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::handleSeriesVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16Bars3DController37handleSeriesVisibilityChangedBySender'
        'EP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController37handleSeriesVisibilityChangedBy'
          'SenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def handlePendingClick(self) -> None:
    """
    Calls Qt's 'void Bars3DController::handlePendingClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handlePendingClick
    """
    #  void Bars3DController::handlePendingClick()
    ritual = 'ritual_ZN16Bars3DController18handlePendingClickEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController18handlePendingClickEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Bars3DController::addSeries(QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#addSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::addSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN16Bars3DController9addSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController9addSeriesEP17QAbstract3DSeries')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Bars3DController::removeSeries(QAbstract3DSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::removeSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN16Bars3DController12removeSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController12removeSeriesEP17QAbstract3DSeri'
          'es')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(int, QAbstract3DSeries)
  @overload(int, NoneType)
  def insertSeries(
      self,
      index: int,
      series: Optional[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Bars3DController::insertSeries(int index,
    QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3dcontroller.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::insertSeries(int index, QAbstract3DSeries
    #      *series)
    ritual = (
        'ritual_ZN16Bars3DController12insertSeriesEiP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController12insertSeriesEiP17QAbstract3DSer'
          'ies')
    self.uglySide.call(ritual, index, self._addressOf(series))

  def barSeriesList(self) -> QList[QBar3DSeries]:
    """
    Calls Qt's 'QList<QBar3DSeries *> Bars3DController::barSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#barSeriesList

    Returns
    -------

    QList[QBar3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBar3DSeries *> Bars3DController::barSeriesList()
    address = self.uglySide.call(
        'ritual_ZN16Bars3DController13barSeriesListEv',
    )
    from . import QBar3DSeries
    return QList[QBar3DSeries]._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def handleAxisRangeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void Bars3DController::handleAxisRangeChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::handleAxisRangeChangedBySender(QObject *sender)
    ritual = (
        'ritual_ZN16Bars3DController30handleAxisRangeChangedBySenderEP7QObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController30handleAxisRangeChangedBySenderE'
          'P7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void Bars3DController::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#adjustAxisRanges
    """
    #  void Bars3DController::adjustAxisRanges()
    ritual = 'ritual_ZN16Bars3DController16adjustAxisRangesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16Bars3DController16adjustAxisRangesEv'
    self.uglySide.call(ritual)

  def handleArrayReset(self) -> None:
    """
    Calls Qt's 'void Bars3DController::handleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleArrayReset
    """
    #  void Bars3DController::handleArrayReset()
    self.uglySide.call('ritual_ZN16Bars3DController16handleArrayResetEv')

  @overload(int, int)
  def handleRowsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Bars3DController::handleRowsAdded(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleRowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Bars3DController::handleRowsAdded(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN16Bars3DController15handleRowsAddedEii', startIndex, count,
    )

  @overload(int, int)
  def handleRowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Bars3DController::handleRowsChanged(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleRowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Bars3DController::handleRowsChanged(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN16Bars3DController17handleRowsChangedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Bars3DController::handleRowsRemoved(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleRowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Bars3DController::handleRowsRemoved(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN16Bars3DController17handleRowsRemovedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Bars3DController::handleRowsInserted(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleRowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Bars3DController::handleRowsInserted(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN16Bars3DController18handleRowsInsertedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void Bars3DController::handleItemChanged(int rowIndex, int
    columnIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleItemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void Bars3DController::handleItemChanged(int rowIndex, int
    #      columnIndex)
    self.uglySide.call(
        'ritual_ZN16Bars3DController17handleItemChangedEii',
        rowIndex, columnIndex,
    )

  def handleDataRowLabelsChanged(self) -> None:
    """
    Calls Qt's 'void Bars3DController::handleDataRowLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleDataRowLabelsChanged
    """
    #  void Bars3DController::handleDataRowLabelsChanged()
    self.uglySide.call(
        'ritual_ZN16Bars3DController26handleDataRowLabelsChangedEv',
    )

  def handleDataColumnLabelsChanged(self) -> None:
    """
    Calls Qt's 'void Bars3DController::handleDataColumnLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html
    """
    #  void Bars3DController::handleDataColumnLabelsChanged()
    self.uglySide.call(
        'ritual_ZN16Bars3DController29handleDataColumnLabelsChangedEv',
    )

  def handleRowColorsChanged(self) -> None:
    """
    Calls Qt's 'void Bars3DController::handleRowColorsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#handleRowColorsChanged
    """
    #  void Bars3DController::handleRowColorsChanged()
    self.uglySide.call(
        'ritual_ZN16Bars3DController22handleRowColorsChangedEv',
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def primarySeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Bars3DController::primarySeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#primarySeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::primarySeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16Bars3DController20primarySeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Bars3DController::selectedSeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DController::selectedSeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16Bars3DController21selectedSeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QAbstract3DAxis.AxisOrientation)
  def createDefaultAxis(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *Bars3DController::createDefaultAxis(QAbstract3DAxis::AxisOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3dcontroller.html#createDefaultAxis

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *Bars3DController::createDefaultAxis(QAbstract3DAxis::
    #      AxisOrientation orientation)
    ritual = (
        'ritual_ZN16Bars3DController17createDefaultAxisEN15QAbstract3DAxis1'
        '5AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16Bars3DController17createDefaultAxisEN15QAbstract3'
          'DAxis15AxisOrientationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstract3DAxis._cuteAt(address)

  @staticmethod
  def adjustSelectionPosition(*__, **_) -> Never:
    """
    Qt's 'void Bars3DController::adjustSelectionPosition(QPoint &pos, const
    QBar3DSeries *series)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Bars3DController.adjustSelectionPosition' has no cute function "
        "yet. Qt's 'void Bars3DController::adjustSelectionPosition(QPoint "
        "&pos, const QBar3DSeries *series)': takes a type Python has no way "
        "to hand over yet.")
