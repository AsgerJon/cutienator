"""
Scatter3DController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatter3dcontroller_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Scatter3DController to be private: it declares the class in a
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

  from ..QtCore import QMetaObject, QRect
  from . import Q3DScene, QAbstract3DSeries, QScatter3DSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QRect = WAIT['QRect']
  QScatter3DSeries = WAIT['QtDataVisualization:QScatter3DSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scatter3DController(Abstract3DController):
  """
  The cute side of Qt's Scatter3DController: a plain Python object standing
  in front of one C++ Scatter3DController.

  It is built on the cute 'Abstract3DController', as Qt's Scatter3DController
  is built on Qt's Abstract3DController, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Scatter3DController that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr',
  'initializeOpenGL', 'setSelectionMode', 'selectedSeries',
  'setSelectedItem', 'invalidSelectionIndex', 'clearSelection',
  'synchDataToRenderer', 'addSeries', 'removeSeries', 'scatterSeriesList',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleAxisRangeChangedBySender', 'handlePendingClick', 'adjustAxisRanges',
  'handleArrayReset', 'handleItemsAdded', 'handleItemsChanged',
  'handleItemsRemoved', 'handleItemsInserted', 'selectedSeriesChanged',
  'startRecordingRemovesAndInserts'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Scatter3DController::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Scatter3DController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Scatter3DController::~Scatter3DController()': the destructor:
    Python never removes a C++ Scatter3DController.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Scatter3DController is created at the first use, not by
    'Scatter3DController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Scatter3DController.
  - Qt tells when it has removed the C++ Scatter3DController. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside Scatter3DController, each a class in here
  #  as in C++.

  class ChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Scatter3DController::ChangeItem: a plain Python
    object standing in front of one C++ Scatter3DController::ChangeItem.

    C++ hands a Scatter3DController::ChangeItem around as a copy, so every
    C++ Scatter3DController::ChangeItem behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's Scatter3DController::ChangeItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Scatter3DController::ChangeItem::~ChangeItem()': the destructor:
      Python removes its C++ Scatter3DController::ChangeItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ Scatter3DController::ChangeItem is created at the first use,
      not by 'Scatter3DController::ChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Scatter3DController::ChangeItem back gives a copy
      the ritual made for Python, in a new cute
      Scatter3DController::ChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Scatter3DController::ChangeItem'

    #  Qt's '~Scatter3DController::ChangeItem()'. Naming it makes this a
    #  value class: Python owns every C++ Scatter3DController::ChangeItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19Scatter3DController10ChangeItemD1Ev'

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
    Calls Qt's 'QString Scatter3DController::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3dcontroller.html#tr

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
    #  QString Scatter3DController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19Scatter3DController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionIndex() -> int:
    """
    Calls Qt's 'int Scatter3DController::invalidSelectionIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#invalidSelectionIndex
    """
    #  int Scatter3DController::invalidSelectionIndex()
    return Rituals.call(
        'ritual_ZN19Scatter3DController21invalidSelectionIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Scatter3DController'

  #  A C++ Scatter3DController Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Scatter3DController'

  #  The functions Qt calls itself that Scatter3DController is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'scatterSeriesList': (
          'QList<QScatter3DSeries *> '
          'Scatter3DController::scatterSeriesList()',
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
    Calls Qt's 'const QMetaObject *Scatter3DController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Scatter3DController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19Scatter3DController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectedSeries(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *Scatter3DController::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#selectedSeries

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *Scatter3DController::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK19Scatter3DController14selectedSeriesEv',
    )
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DGraph.SelectionFlags)
  def setSelectionMode(self, mode: QAbstract3DGraph.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    Scatter3DController::setSelectionMode(QAbstract3DGraph::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#setSelectionMode

    Parameters
    ----------

    mode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Scatter3DController::setSelectionMode(QAbstract3DGraph::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN19Scatter3DController16setSelectionModeE6QFlagsIN16QAbstr'
        'act3DGraph13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Scatter3DController16setSelectionModeE6QFlagsIN16'
          'QAbstract3DGraph13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(int, QScatter3DSeries)
  @overload(int, NoneType)
  def setSelectedItem(
      self,
      index: int,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Scatter3DController::setSelectedItem(int index,
    QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#setSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DController::setSelectedItem(int index, QScatter3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19Scatter3DController15setSelectedItemEiP16QScatter3DSeri'
        'es',
        index, self._addressOf(series),
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
    'Scatter3DController::Scatter3DController(QRect rect, Q3DScene *scene)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#Scatter3DController

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Scatter3DController::Scatter3DController(QRect rect, Q3DScene *scene)
    self._noteCreation(Scatter3DController, lambda: Rituals.call(
        'ritual_ZN19Scatter3DControllerC1E5QRectP8Q3DScene',
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
    Calls Qt's 'void Scatter3DController::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#initializeOpenGL
    """
    #  void Scatter3DController::initializeOpenGL()
    ritual = 'ritual_ZN19Scatter3DController16initializeOpenGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Scatter3DController16initializeOpenGLEv'
    self.uglySide.call(ritual)

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void Scatter3DController::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#clearSelection
    """
    #  void Scatter3DController::clearSelection()
    ritual = 'ritual_ZN19Scatter3DController14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Scatter3DController14clearSelectionEv'
    self.uglySide.call(ritual)

  def synchDataToRenderer(self) -> None:
    """
    Calls Qt's 'void Scatter3DController::synchDataToRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#synchDataToRenderer
    """
    #  void Scatter3DController::synchDataToRenderer()
    ritual = 'ritual_ZN19Scatter3DController19synchDataToRendererEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Scatter3DController19synchDataToRendererEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Scatter3DController::addSeries(QAbstract3DSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3dcontroller.html#addSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DController::addSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN19Scatter3DController9addSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Scatter3DController9addSeriesEP17QAbstract3DSerie'
          's')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Scatter3DController::removeSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DController::removeSeries(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN19Scatter3DController12removeSeriesEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Scatter3DController12removeSeriesEP17QAbstract3DS'
          'eries')
    self.uglySide.call(ritual, self._addressOf(series))

  def scatterSeriesList(self) -> QList[QScatter3DSeries]:
    """
    Calls Qt's 'QList<QScatter3DSeries *>
    Scatter3DController::scatterSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#scatterSeriesList

    Returns
    -------

    QList[QScatter3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScatter3DSeries *> Scatter3DController::scatterSeriesList()
    address = self.uglySide.call(
        'ritual_ZN19Scatter3DController17scatterSeriesListEv',
    )
    from . import QScatter3DSeries
    return QList[QScatter3DSeries]._cuteOwning(address)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Scatter3DController::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void Scatter3DController::
    #      handleAxisAutoAdjustRangeChangedInOrientation(QAbstract3DAxis::
    #      AxisOrientation orientation, bool autoAdjust)
    ritual = (
        'ritual_ZN19Scatter3DController45handleAxisAutoAdjustRangeChangedIn'
        'OrientationEN15QAbstract3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Scatter3DController45handleAxisAutoAdjustRangeCha'
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
    Scatter3DController::handleAxisRangeChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DController::handleAxisRangeChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19Scatter3DController30handleAxisRangeChangedBySenderEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Scatter3DController30handleAxisRangeChangedBySend'
          'erEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def handlePendingClick(self) -> None:
    """
    Calls Qt's 'void Scatter3DController::handlePendingClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#handlePendingClick
    """
    #  void Scatter3DController::handlePendingClick()
    ritual = 'ritual_ZN19Scatter3DController18handlePendingClickEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Scatter3DController18handlePendingClickEv'
    self.uglySide.call(ritual)

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void Scatter3DController::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#adjustAxisRanges
    """
    #  void Scatter3DController::adjustAxisRanges()
    ritual = 'ritual_ZN19Scatter3DController16adjustAxisRangesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Scatter3DController16adjustAxisRangesEv'
    self.uglySide.call(ritual)

  def handleArrayReset(self) -> None:
    """
    Calls Qt's 'void Scatter3DController::handleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#handleArrayReset
    """
    #  void Scatter3DController::handleArrayReset()
    self.uglySide.call('ritual_ZN19Scatter3DController16handleArrayResetEv')

  @overload(int, int)
  def handleItemsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Scatter3DController::handleItemsAdded(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#handleItemsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Scatter3DController::handleItemsAdded(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN19Scatter3DController16handleItemsAddedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Scatter3DController::handleItemsChanged(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#handleItemsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Scatter3DController::handleItemsChanged(int startIndex, int
    #      count)
    self.uglySide.call(
        'ritual_ZN19Scatter3DController18handleItemsChangedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Scatter3DController::handleItemsRemoved(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#handleItemsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Scatter3DController::handleItemsRemoved(int startIndex, int
    #      count)
    self.uglySide.call(
        'ritual_ZN19Scatter3DController18handleItemsRemovedEii',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void Scatter3DController::handleItemsInserted(int startIndex,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#handleItemsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void Scatter3DController::handleItemsInserted(int startIndex, int
    #      count)
    self.uglySide.call(
        'ritual_ZN19Scatter3DController19handleItemsInsertedEii',
        startIndex, count,
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    Scatter3DController::selectedSeriesChanged(QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DController::selectedSeriesChanged(QScatter3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19Scatter3DController21selectedSeriesChangedEP16QScatter3'
        'DSeries',
        self._addressOf(series),
    )

  def startRecordingRemovesAndInserts(self) -> None:
    """
    Calls Qt's 'void Scatter3DController::startRecordingRemovesAndInserts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3dcontroller.html
    """
    #  void Scatter3DController::startRecordingRemovesAndInserts()
    ritual = (
        'ritual_ZN19Scatter3DController31startRecordingRemovesAndInsertsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Scatter3DController31startRecordingRemovesAndInse'
          'rtsEv')
    self.uglySide.call(ritual)
