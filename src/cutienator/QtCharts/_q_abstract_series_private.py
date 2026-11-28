"""
QAbstractSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qabstractseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QAbstractAxis, QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QGraphicsItem
  from . import AbstractDomain, ChartItem, ChartPresenter, ChartTheme
  from . import QLegend, QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  ChartPresenter = WAIT['ChartPresenter']
  ChartTheme = WAIT['ChartTheme']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSeriesPrivate(QObject):
  """
  The cute side of Qt's QAbstractSeriesPrivate: a plain Python object
  standing in front of one C++ QAbstractSeriesPrivate.

  It is built on the cute 'QObject', as Qt's QAbstractSeriesPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSeriesPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr',
  'initializeDomain', 'initializeAxes', 'initializeTheme',
  'initializeGraphics', 'createLegendMarkers', 'defaultAxisType',
  'createDefaultAxis', 'chartItem', 'setDomain', 'domain', 'setPresenter',
  'presenter', 'chart', 'setBlockOpenGL', 'countChanged'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractSeriesPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractSeriesPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractSeriesPrivate::~QAbstractSeriesPrivate()': the destructor:
    Python never removes a C++ QAbstractSeriesPrivate.
  - Qt's 'void
    QAbstractSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractSeriesPrivate is created at the first use, not by
    'QAbstractSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSeriesPrivate.
  - Qt tells when it has removed the C++ QAbstractSeriesPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractSeriesPrivate that has no cute function yet,
    '__init__', 'initializeAnimations', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QAbstractSeriesPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseriesprivate.html#tr

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
    #  QString QAbstractSeriesPrivate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QAbstractSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSeriesPrivate'

  #  A C++ QAbstractSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSeriesPrivate'

  #  The functions Qt calls itself that QAbstractSeriesPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'initializeAnimations': (
          'void '
          'QAbstractSeriesPrivate::initializeAnimations(QChart::AnimationOp'
          'tions, int, QEasingCurve &)',
      ),
      'createLegendMarkers': (
          'QList<QLegendMarker *> '
          'QAbstractSeriesPrivate::createLegendMarkers(QLegend *)',
      ),
  }

  #  The functions Qt calls itself that QAbstractSeriesPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeDomain': (
          ('_ZN22QAbstractSeriesPrivate16initializeDomainEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initializeAxes': (
          ('_ZN22QAbstractSeriesPrivate14initializeAxesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initializeTheme': (
          ('_ZN22QAbstractSeriesPrivate15initializeThemeEiP10ChartThemeb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCharts:ChartTheme'),
               ('bool', 'number', ''),
           )),
      ),
      'initializeGraphics': (
          ('_ZN22QAbstractSeriesPrivate18initializeGraphicsEP13QGraphicsIte'
           'm',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
           )),
      ),
      'defaultAxisType': (
          ('_ZNK22QAbstractSeriesPrivate15defaultAxisTypeEN2Qt11Orientation'
           'E',
           ('int', 'enum', 'QtCharts:QAbstractAxis.AxisType'),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'createDefaultAxis': (
          ('_ZNK22QAbstractSeriesPrivate17createDefaultAxisEN2Qt11Orientati'
           'onE',
           ('address', 'address', 'QtCharts:QAbstractAxis'),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'setDomain': (
          ('_ZN22QAbstractSeriesPrivate9setDomainEP14AbstractDomain',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:AbstractDomain'),
           )),
      ),
      'setPresenter': (
          ('_ZN22QAbstractSeriesPrivate12setPresenterEP14ChartPresenter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:ChartPresenter'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstractSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.Orientation)
  def defaultAxisType(self, a0: Qt.Orientation) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'QAbstractAxis::AxisType
    QAbstractSeriesPrivate::defaultAxisType(Qt::Orientation a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#defaultAxisType

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  QAbstractAxis::AxisType
    #      QAbstractSeriesPrivate::defaultAxisType(Qt::Orientation a0) const
    return QAbstractAxis.AxisType(self.uglySide.call(
        'ritual_ZNK22QAbstractSeriesPrivate15defaultAxisTypeEN2Qt11Orientat'
        'ionE',
        a0.value,
    ))

  @overload(Qt.Orientation)
  def createDefaultAxis(self, a0: Qt.Orientation) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *QAbstractSeriesPrivate::createDefaultAxis(Qt::Orientation a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#createDefaultAxis

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis
    #      *QAbstractSeriesPrivate::createDefaultAxis(Qt::Orientation a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstractSeriesPrivate17createDefaultAxisEN2Qt11Orient'
        'ationE',
        a0.value,
    )
    return QAbstractAxis._cuteAt(address)

  def presenter(self) -> Optional[ChartPresenter]:
    """
    Calls Qt's 'ChartPresenter *QAbstractSeriesPrivate::presenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#presenter

    Returns
    -------

    Optional[ChartPresenter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartPresenter *QAbstractSeriesPrivate::presenter() const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstractSeriesPrivate9presenterEv',
    )
    from . import ChartPresenter
    return ChartPresenter._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AbstractDomain)
  @overload(NoneType)
  def setDomain(self, domain: Optional[AbstractDomain]) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::setDomain(AbstractDomain
    *domain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#setDomain

    Parameters
    ----------

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
    ritual = 'ritual_ZN22QAbstractSeriesPrivate9setDomainEP14AbstractDomain'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSeriesPrivate9setDomainEP14AbstractDomai'
          'n')
    self.uglySide.call(ritual, self._addressOf(domain))

  @overload(ChartPresenter)
  @overload(NoneType)
  def setPresenter(self, presenter: Optional[ChartPresenter]) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::setPresenter(ChartPresenter
    *presenter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#setPresenter

    Parameters
    ----------

    presenter : Optional[ChartPresenter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
    ritual = (
        'ritual_ZN22QAbstractSeriesPrivate12setPresenterEP14ChartPresenter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSeriesPrivate12setPresenterEP14ChartPres'
          'enter')
    self.uglySide.call(ritual, self._addressOf(presenter))

  @overload(bool)
  def setBlockOpenGL(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::setBlockOpenGL(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#setBlockOpenGL

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractSeriesPrivate::setBlockOpenGL(bool enable)
    self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate14setBlockOpenGLEb', enable,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstractSeriesPrivate::QAbstractSeriesPrivate(QAbstractSeries
    *q)': the class is abstract, so C++ cannot make one, and the C++ class of
    ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractSeriesPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstractSeriesPrivate::QAbstractSeriesPrivate(QAbstractSeries "
        "*q)': the class is abstract, so C++ cannot make one, and the C++ "
        "class of ours does not fill in every function it leaves open.")

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

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#initializeDomain
    """
    #  void QAbstractSeriesPrivate::initializeDomain()
    self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate16initializeDomainEv',
    )

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#initializeAxes
    """
    #  void QAbstractSeriesPrivate::initializeAxes()
    self.uglySide.call('ritual_ZN22QAbstractSeriesPrivate14initializeAxesEv')

  @overload(int, ChartTheme)
  @overload(int, NoneType)
  @overload(int, ChartTheme, bool)
  @overload(int, NoneType, bool)
  def initializeTheme(
      self,
      index: int,
      theme: Optional[ChartTheme],
      forced: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#initializeTheme

    Parameters
    ----------

    index : int
      Passed on as it is.

    theme : Optional[ChartTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forced : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QAbstractSeriesPrivate::initializeTheme(int index, ChartTheme
    #      *theme, bool forced)
    self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate15initializeThemeEiP10ChartThemeb',
        index, self._addressOf(theme), forced,
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate18initializeGraphicsEP13QGraphics'
        'Item',
        self._addressOf(parent, 'QGraphicsItem'),
    )

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QAbstractSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#createLegendMarkers

    Parameters
    ----------

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QLegendMarker]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLegendMarker *>
    #      QAbstractSeriesPrivate::createLegendMarkers(QLegend *legend)
    address = self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate19createLegendMarkersEP7QLegend',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  def chartItem(self) -> Optional[ChartItem]:
    """
    Calls Qt's 'ChartItem *QAbstractSeriesPrivate::chartItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#chartItem

    Returns
    -------

    Optional[ChartItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartItem *QAbstractSeriesPrivate::chartItem()
    address = self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate9chartItemEv',
    )
    from . import ChartItem
    return ChartItem._cuteAt(address)

  def domain(self) -> Optional[AbstractDomain]:
    """
    Calls Qt's 'AbstractDomain *QAbstractSeriesPrivate::domain()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseriesprivate.html#domain

    Returns
    -------

    Optional[AbstractDomain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractDomain *QAbstractSeriesPrivate::domain()
    address = self.uglySide.call(
        'ritual_ZN22QAbstractSeriesPrivate6domainEv',
    )
    from . import AbstractDomain
    return AbstractDomain._cuteAt(address)

  def chart(self) -> Optional[QChart]:
    """
    Calls Qt's 'QChart *QAbstractSeriesPrivate::chart()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseriesprivate.html#chart

    Returns
    -------

    Optional[QChart]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChart *QAbstractSeriesPrivate::chart()
    address = self.uglySide.call('ritual_ZN22QAbstractSeriesPrivate5chartEv')
    return QChart._cuteAt(address)

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeriesPrivate::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseriesprivate.html#countChanged
    """
    #  void QAbstractSeriesPrivate::countChanged()
    self.uglySide.call('ritual_ZN22QAbstractSeriesPrivate12countChangedEv')

  @staticmethod
  def initializeAnimations(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractSeriesPrivate.initializeAnimations' has no cute function "
        "yet. Qt's 'void "
        "QAbstractSeriesPrivate::initializeAnimations(QChart::AnimationOptio"
        "ns options, int duration, QEasingCurve &curve)': takes a type "
        "Python has no way to hand over yet.")
