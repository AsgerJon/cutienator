"""
QAbstractAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qabstractaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtWidgets import QGraphicsItem
  from . import AbstractDomain, ChartAxisElement, ChartTheme, QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  ChartTheme = WAIT['ChartTheme']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QGraphicsItem = WAIT['QGraphicsItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAxisPrivate(QObject):
  """
  The cute side of Qt's QAbstractAxisPrivate: a plain Python object standing
  in front of one C++ QAbstractAxisPrivate.

  It is built on the cute 'QObject', as Qt's QAbstractAxisPrivate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAxisPrivate that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'alignment',
  'orientation', 'setAlignment', 'setLabelsTruncated', 'initializeDomain',
  'initializeGraphics', 'initializeTheme', 'setMin', 'setMax', 'setRange',
  'min', 'max', 'axisItem', 'handleRangeChanged', 'rangeChanged', 'q_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractAxisPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractAxisPrivate::~QAbstractAxisPrivate()': the destructor:
    Python never removes a C++ QAbstractAxisPrivate.
  - Qt's 'void
    QAbstractAxisPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAbstractAxis *QAbstractAxisPrivate::q_func() const': takes
    in Python what 'QAbstractAxis *QAbstractAxisPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractAxisPrivate is created at the first use, not by
    'QAbstractAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAxisPrivate.
  - Qt tells when it has removed the C++ QAbstractAxisPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractAxisPrivate that has no cute function yet,
    'initializeAnimations', holds a function that raises
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
    Calls Qt's 'QString QAbstractAxisPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#tr

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
    #  QString QAbstractAxisPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QAbstractAxisPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QAbstractAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractAxisPrivate'

  #  The functions Qt calls itself that QAbstractAxisPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'initializeAnimations': (
          'void '
          'QAbstractAxisPrivate::initializeAnimations(QChart::AnimationOpti'
          'ons, int, QEasingCurve &)',
      ),
  }

  #  The functions Qt calls itself that QAbstractAxisPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeDomain': (
          ('_ZN20QAbstractAxisPrivate16initializeDomainEP14AbstractDomain',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:AbstractDomain'),
           )),
      ),
      'initializeGraphics': (
          ('_ZN20QAbstractAxisPrivate18initializeGraphicsEP13QGraphicsItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
           )),
      ),
      'initializeTheme': (
          ('_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:ChartTheme'),
               ('bool', 'number', ''),
           )),
      ),
      'setMin': (
          ('_ZN20QAbstractAxisPrivate6setMinERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'setMax': (
          ('_ZN20QAbstractAxisPrivate6setMaxERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'setRange': (
          ('_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
          ('_ZN20QAbstractAxisPrivate8setRangeEdd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'min': (
          ('_ZN20QAbstractAxisPrivate3minEv',
           ('double', 'number', ''),
           ()),
      ),
      'max': (
          ('_ZN20QAbstractAxisPrivate3maxEv',
           ('double', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QAbstractAxisPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractAxisPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractAxisPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QAbstractAxisPrivate::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QAbstractAxisPrivate::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK20QAbstractAxisPrivate9alignmentEv',
    ))

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QAbstractAxisPrivate::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QAbstractAxisPrivate::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK20QAbstractAxisPrivate11orientationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QAbstractAxisPrivate::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate12setAlignmentE6QFlagsIN2Qt13Alignm'
        'entFlagEE',
        alignment.value,
    )

  @overload(bool)
  def setLabelsTruncated(self, labelsTruncated: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setLabelsTruncated(bool
    labelsTruncated)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#setLabelsTruncated

    Parameters
    ----------

    labelsTruncated : bool
      Passed on as it is.
    """
    #  void QAbstractAxisPrivate::setLabelsTruncated(bool labelsTruncated)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate18setLabelsTruncatedEb',
        labelsTruncated,
    )

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setMin(const QVariant &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxisPrivate::setMin(const QVariant &min)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate6setMinERK8QVariant',
        self._valueOf(min),
    )

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setMax(const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxisPrivate::setMax(const QVariant &max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate6setMaxERK8QVariant',
        self._valueOf(max),
    )

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxisPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstractAxisPrivate::setRange(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate8setRangeEdd', min, max,
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

  @overload(QAbstractAxis)
  @overload(NoneType)
  def __init__(self, q: Optional[QAbstractAxis]) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractAxisPrivate::QAbstractAxisPrivate(QAbstractAxis *q)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#QAbstractAxisPrivate

    Parameters
    ----------

    q : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractAxisPrivate::QAbstractAxisPrivate(QAbstractAxis *q)
    self._noteCreation(QAbstractAxisPrivate, lambda: Rituals.call(
        'ritual_ZN20QAbstractAxisPrivateC1EP13QAbstractAxis',
        self._addressOf(q),
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

  @overload(AbstractDomain)
  @overload(NoneType)
  def initializeDomain(self, domain: Optional[AbstractDomain]) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::initializeDomain(AbstractDomain
    *domain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#initializeDomain

    Parameters
    ----------

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractAxisPrivate::initializeDomain(AbstractDomain *domain)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate16initializeDomainEP14AbstractDomai'
        'n',
        self._addressOf(domain),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractAxisPrivate::initializeGraphics(QGraphicsItem *parent)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate18initializeGraphicsEP13QGraphicsIt'
        'em',
        self._addressOf(parent, 'QGraphicsItem'),
    )

  @overload(ChartTheme)
  @overload(NoneType)
  @overload(ChartTheme, bool)
  @overload(NoneType, bool)
  def initializeTheme(
      self,
      theme: Optional[ChartTheme],
      forced: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme,
    bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#initializeTheme

    Parameters
    ----------

    theme : Optional[ChartTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forced : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
    #      forced)
    ritual = (
        'ritual_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThe'
          'meb')
    self.uglySide.call(ritual, self._addressOf(theme), forced)

  def min(self) -> float:
    """
    Calls Qt's 'qreal QAbstractAxisPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#min
    """
    #  qreal QAbstractAxisPrivate::min()
    return self.uglySide.call('ritual_ZN20QAbstractAxisPrivate3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal QAbstractAxisPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#max
    """
    #  qreal QAbstractAxisPrivate::max()
    return self.uglySide.call('ritual_ZN20QAbstractAxisPrivate3maxEv')

  def axisItem(self) -> Optional[ChartAxisElement]:
    """
    Calls Qt's 'ChartAxisElement *QAbstractAxisPrivate::axisItem()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#axisItem

    Returns
    -------

    Optional[ChartAxisElement]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAxisElement *QAbstractAxisPrivate::axisItem()
    address = self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate8axisItemEv',
    )
    from . import ChartAxisElement
    return ChartAxisElement._cuteAt(address)

  @overload(float, float)
  def handleRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::handleRangeChanged(qreal min,
    qreal max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#handleRangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstractAxisPrivate::handleRangeChanged(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate18handleRangeChangedEdd', min, max,
    )

  @overload(float, float)
  def rangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstractAxisPrivate::rangeChanged(qreal min, qreal
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxisprivate.html#rangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstractAxisPrivate::rangeChanged(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN20QAbstractAxisPrivate12rangeChangedEdd', min, max,
    )

  def q_func(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QAbstractAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxisprivate.html#q_func

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QAbstractAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QAbstractAxisPrivate6q_funcEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @staticmethod
  def initializeAnimations(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractAxisPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractAxisPrivate.initializeAnimations' has no cute function "
        "yet. Qt's 'void "
        "QAbstractAxisPrivate::initializeAnimations(QChart::AnimationOptions"
        " options, int duration, QEasingCurve &curve)': takes a type Python "
        "has no way to hand over yet.")
