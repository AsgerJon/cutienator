"""
ChartElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartelement_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means ChartElement to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtWidgets import QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import ChartAnimation, ChartDataSet, ChartPresenter
  from . import ChartThemeManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartDataSet = WAIT['ChartDataSet']
  ChartPresenter = WAIT['ChartPresenter']
  ChartThemeManager = WAIT['ChartThemeManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartElement(QGraphicsObject):
  """
  The cute side of Qt's ChartElement: a plain Python object standing in front
  of one C++ ChartElement.

  It is built on the cute 'QGraphicsObject', as Qt's ChartElement is built on
  Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartElement that has a ritual and that Python can
  call so far, 7 names in all: 'animation', 'setPresenter', 'presenter',
  'setThemeManager', 'themeManager', 'setDataSet', 'dataSet'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ ChartElement is created at the first use, not by
    'ChartElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartElement.
  - Qt tells when it has removed the C++ ChartElement. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's ChartElement that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartElement'

  #  The functions Qt calls itself that ChartElement is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'animation': (
          ('_ZNK12ChartElement9animationEv',
           ('address', 'address', 'QtCharts:ChartAnimation'),
           ()),
      ),
      'setPresenter': (
          ('_ZN12ChartElement12setPresenterEP14ChartPresenter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:ChartPresenter'),
           )),
      ),
      'setThemeManager': (
          ('_ZN12ChartElement15setThemeManagerEP17ChartThemeManager',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:ChartThemeManager'),
           )),
      ),
      'setDataSet': (
          ('_ZN12ChartElement10setDataSetEP12ChartDataSet',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:ChartDataSet'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def animation(self) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *ChartElement::animation() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#animation

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *ChartElement::animation() const
    ritual = 'ritual_ZNK12ChartElement9animationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12ChartElement9animationEv'
    address = self.uglySide.call(ritual)
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  def presenter(self) -> Optional[ChartPresenter]:
    """
    Calls Qt's 'ChartPresenter *ChartElement::presenter() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#presenter

    Returns
    -------

    Optional[ChartPresenter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartPresenter *ChartElement::presenter() const
    address = self.uglySide.call('ritual_ZNK12ChartElement9presenterEv')
    from . import ChartPresenter
    return ChartPresenter._cuteAt(address)

  def themeManager(self) -> Optional[ChartThemeManager]:
    """
    Calls Qt's 'ChartThemeManager *ChartElement::themeManager() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#themeManager

    Returns
    -------

    Optional[ChartThemeManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartThemeManager *ChartElement::themeManager() const
    address = self.uglySide.call('ritual_ZNK12ChartElement12themeManagerEv')
    from . import ChartThemeManager
    return ChartThemeManager._cuteAt(address)

  def dataSet(self) -> Optional[ChartDataSet]:
    """
    Calls Qt's 'ChartDataSet *ChartElement::dataSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#dataSet

    Returns
    -------

    Optional[ChartDataSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartDataSet *ChartElement::dataSet() const
    address = self.uglySide.call('ritual_ZNK12ChartElement7dataSetEv')
    from . import ChartDataSet
    return ChartDataSet._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ChartPresenter)
  @overload(NoneType)
  def setPresenter(self, presenter: Optional[ChartPresenter]) -> None:
    """
    Calls Qt's 'void ChartElement::setPresenter(ChartPresenter *presenter)'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#setPresenter

    Parameters
    ----------

    presenter : Optional[ChartPresenter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartElement::setPresenter(ChartPresenter *presenter)
    ritual = 'ritual_ZN12ChartElement12setPresenterEP14ChartPresenter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12ChartElement12setPresenterEP14ChartPresenter'
    self.uglySide.call(ritual, self._addressOf(presenter))

  @overload(ChartThemeManager)
  @overload(NoneType)
  def setThemeManager(self, manager: Optional[ChartThemeManager]) -> None:
    """
    Calls Qt's 'void ChartElement::setThemeManager(ChartThemeManager
    *manager)'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#setThemeManager

    Parameters
    ----------

    manager : Optional[ChartThemeManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartElement::setThemeManager(ChartThemeManager *manager)
    ritual = 'ritual_ZN12ChartElement15setThemeManagerEP17ChartThemeManager'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12ChartElement15setThemeManagerEP17ChartThemeManage'
          'r')
    self.uglySide.call(ritual, self._addressOf(manager))

  @overload(ChartDataSet)
  @overload(NoneType)
  def setDataSet(self, dataSet: Optional[ChartDataSet]) -> None:
    """
    Calls Qt's 'void ChartElement::setDataSet(ChartDataSet *dataSet)'.

    Qt's own words: https://doc.qt.io/qt-6/chartelement.html#setDataSet

    Parameters
    ----------

    dataSet : Optional[ChartDataSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartElement::setDataSet(ChartDataSet *dataSet)
    ritual = 'ritual_ZN12ChartElement10setDataSetEP12ChartDataSet'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12ChartElement10setDataSetEP12ChartDataSet'
    self.uglySide.call(ritual, self._addressOf(dataSet))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'ChartElement::ChartElement(QGraphicsItem *item)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'ChartElement.__init__' has no cute function yet. Qt's "
        "'ChartElement::ChartElement(QGraphicsItem *item)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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
