"""
AbstractDomain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/abstractdomain_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means AbstractDomain to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF
  from . import QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractDomain(QObject):
  """
  The cute side of Qt's AbstractDomain: a plain Python object standing in
  front of one C++ AbstractDomain.

  It is built on the cute 'QObject', as Qt's AbstractDomain is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AbstractDomain that has a ritual and that Python can
  call so far, 44 names in all: 'metaObject', 'tr', 'setSize', 'size',
  'type', 'setRange', 'setRangeX', 'setRangeY', 'setMinX', 'setMaxX',
  'setMinY', 'setMaxY', 'minX', 'maxX', 'minY', 'maxY', 'spanX', 'spanY',
  'isEmpty', 'blockRangeSignals', 'rangeSignalsBlocked', 'zoomReset',
  'storeZoomReset', 'isZoomed', 'zoomIn', 'zoomOut', 'move',
  'calculateDomainPoint', 'calculateGeometryPoints', 'attachAxis',
  'detachAxis', 'niceNumber', 'setReverseX', 'setReverseY', 'isReverseX',
  'isReverseY', 'updated', 'rangeHorizontalChanged', 'rangeVerticalChanged',
  'handleVerticalAxisRangeChanged', 'handleHorizontalAxisRangeChanged',
  'handleReverseXChanged', 'handleReverseYChanged', 'fixZoomRect'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AbstractDomain::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int AbstractDomain::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AbstractDomain::~AbstractDomain()': the destructor: Python never
    removes a C++ AbstractDomain.
  - Qt's 'QPointF AbstractDomain::calculateGeometryPoint(const QPointF
    &point, bool &ok) const': takes a number to change where it is.
  - Qt's 'void AbstractDomain::looseNiceNumbers(qreal &min, qreal &max, int
    &ticksCount)': takes a number to change where it is.
  - Qt's 'void AbstractDomain::adjustLogDomainRanges(qreal &min, qreal
    &max)': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 56 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 leans on 'operator==(AbstractDomain const&,
  AbstractDomain const&)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'operator!=(AbstractDomain const&, AbstractDomain const&)', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken; 1 leans on 'operator<<(QDebug, AbstractDomain const&)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ AbstractDomain is created at the first use, not by
    'AbstractDomain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AbstractDomain.
  - Qt tells when it has removed the C++ AbstractDomain. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's AbstractDomain that has no cute function yet,
    '__init__', 'adjustLogDomainRanges', 'calculateGeometryPoint',
    'looseNiceNumbers', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside AbstractDomain, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DomainType(CuteNum):
    """
    The enum 'AbstractDomain::DomainType' of Qt, with the 9 names Qt gives in
    it.
    """

    UndefinedDomain = Kee[int](0)
    XYDomain = Kee[int](1)
    XLogYDomain = Kee[int](2)
    LogXYDomain = Kee[int](3)
    LogXLogYDomain = Kee[int](4)
    XYPolarDomain = Kee[int](5)
    XLogYPolarDomain = Kee[int](6)
    LogXYPolarDomain = Kee[int](7)
    LogXLogYPolarDomain = Kee[int](8)

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
    Calls Qt's 'QString AbstractDomain::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#tr

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
    #  QString AbstractDomain::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14AbstractDomain2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(float, bool)
  def niceNumber(x: float, ceiling: bool) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::niceNumber(qreal x, bool ceiling)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#niceNumber

    Parameters
    ----------

    x : float
      Passed on as it is.

    ceiling : bool
      Passed on as it is.
    """
    #  qreal AbstractDomain::niceNumber(qreal x, bool ceiling)
    return Rituals.call(
        'ritual_ZN14AbstractDomain10niceNumberEdb', x, ceiling,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AbstractDomain'

  #  A C++ AbstractDomain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AbstractDomain'

  #  The functions Qt calls itself that AbstractDomain is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'calculateGeometryPoint': (
          'QPointF AbstractDomain::calculateGeometryPoint(const QPointF &, '
          'bool &) const',
      ),
      'calculateGeometryPoints': (
          'QList<QPointF> AbstractDomain::calculateGeometryPoints(const '
          'QList<QPointF> &) const',
      ),
  }

  #  The functions Qt calls itself that AbstractDomain is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setSize': (
          ('_ZN14AbstractDomain7setSizeERK6QSizeF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
      'type': (
          ('_ZN14AbstractDomain4typeEv',
           ('int', 'enum', 'QtCharts:AbstractDomain.DomainType'),
           ()),
      ),
      'setRange': (
          ('_ZN14AbstractDomain8setRangeEdddd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'zoomIn': (
          ('_ZN14AbstractDomain6zoomInERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'zoomOut': (
          ('_ZN14AbstractDomain7zoomOutERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'move': (
          ('_ZN14AbstractDomain4moveEdd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'calculateDomainPoint': (
          ('_ZNK14AbstractDomain20calculateDomainPointERK7QPointF',
           ('address', 'value', 'QtCore:QPointF'),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'attachAxis': (
          ('_ZN14AbstractDomain10attachAxisEP13QAbstractAxis',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCharts:QAbstractAxis'),
           )),
      ),
      'detachAxis': (
          ('_ZN14AbstractDomain10detachAxisEP13QAbstractAxis',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCharts:QAbstractAxis'),
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
    Calls Qt's 'const QMetaObject *AbstractDomain::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AbstractDomain::metaObject() const
    address = self.uglySide.call('ritual_ZNK14AbstractDomain10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF AbstractDomain::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF AbstractDomain::size() const
    address = self.uglySide.call('ritual_ZNK14AbstractDomain4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def minX(self) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::minX() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#minX
    """
    #  qreal AbstractDomain::minX() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain4minXEv')

  def maxX(self) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::maxX() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#maxX
    """
    #  qreal AbstractDomain::maxX() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain4maxXEv')

  def minY(self) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::minY() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#minY
    """
    #  qreal AbstractDomain::minY() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain4minYEv')

  def maxY(self) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::maxY() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#maxY
    """
    #  qreal AbstractDomain::maxY() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain4maxYEv')

  def spanX(self) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::spanX() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#spanX
    """
    #  qreal AbstractDomain::spanX() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain5spanXEv')

  def spanY(self) -> float:
    """
    Calls Qt's 'qreal AbstractDomain::spanY() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#spanY
    """
    #  qreal AbstractDomain::spanY() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain5spanYEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#isEmpty
    """
    #  bool AbstractDomain::isEmpty() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain7isEmptyEv')

  def rangeSignalsBlocked(self) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::rangeSignalsBlocked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#rangeSignalsBlocked
    """
    #  bool AbstractDomain::rangeSignalsBlocked() const
    return self.uglySide.call(
        'ritual_ZNK14AbstractDomain19rangeSignalsBlockedEv',
    )

  @overload(QPointF)
  def calculateDomainPoint(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF AbstractDomain::calculateDomainPoint(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#calculateDomainPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF AbstractDomain::calculateDomainPoint(const QPointF &point)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14AbstractDomain20calculateDomainPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QList[QPointF])
  def calculateGeometryPoints(self, list: QList[QPointF]) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> AbstractDomain::calculateGeometryPoints(const
    QList<QPointF> &list) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#calculateGeometryPoints

    Parameters
    ----------

    list : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> AbstractDomain::calculateGeometryPoints(const
    #      QList<QPointF> &list) const
    address = self.uglySide.call(
        'ritual_ZNK14AbstractDomain23calculateGeometryPointsERK5QListI7QPoi'
        'ntFE',
        self._valueOf(list),
    )
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  def isReverseX(self) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::isReverseX() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#isReverseX
    """
    #  bool AbstractDomain::isReverseX() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain10isReverseXEv')

  def isReverseY(self) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::isReverseY() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#isReverseY
    """
    #  bool AbstractDomain::isReverseY() const
    return self.uglySide.call('ritual_ZNK14AbstractDomain10isReverseYEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void AbstractDomain::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void AbstractDomain::setSize(const QSizeF &size)
    ritual = 'ritual_ZN14AbstractDomain7setSizeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14AbstractDomain7setSizeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(float, float, float, float)
  def setRange(
      self,
      minX: float,
      maxX: float,
      minY: float,
      maxY: float,
  ) -> None:
    """
    Calls Qt's 'void AbstractDomain::setRange(qreal minX, qreal maxX, qreal
    minY, qreal maxY)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setRange

    Parameters
    ----------

    minX : float
      Passed on as it is.

    maxX : float
      Passed on as it is.

    minY : float
      Passed on as it is.

    maxY : float
      Passed on as it is.
    """
    #  void AbstractDomain::setRange(qreal minX, qreal maxX, qreal minY,
    #      qreal maxY)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain8setRangeEdddd', minX, maxX, minY, maxY,
    )

  @overload(float, float)
  def setRangeX(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::setRangeX(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setRangeX

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::setRangeX(qreal min, qreal max)
    self.uglySide.call('ritual_ZN14AbstractDomain9setRangeXEdd', min, max)

  @overload(float, float)
  def setRangeY(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::setRangeY(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setRangeY

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::setRangeY(qreal min, qreal max)
    self.uglySide.call('ritual_ZN14AbstractDomain9setRangeYEdd', min, max)

  @overload(float)
  def setMinX(self, min: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::setMinX(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setMinX

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void AbstractDomain::setMinX(qreal min)
    self.uglySide.call('ritual_ZN14AbstractDomain7setMinXEd', min)

  @overload(float)
  def setMaxX(self, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::setMaxX(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setMaxX

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::setMaxX(qreal max)
    self.uglySide.call('ritual_ZN14AbstractDomain7setMaxXEd', max)

  @overload(float)
  def setMinY(self, min: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::setMinY(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setMinY

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void AbstractDomain::setMinY(qreal min)
    self.uglySide.call('ritual_ZN14AbstractDomain7setMinYEd', min)

  @overload(float)
  def setMaxY(self, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::setMaxY(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setMaxY

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::setMaxY(qreal max)
    self.uglySide.call('ritual_ZN14AbstractDomain7setMaxYEd', max)

  @overload(bool)
  def setReverseX(self, reverse: bool) -> None:
    """
    Calls Qt's 'void AbstractDomain::setReverseX(bool reverse)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setReverseX

    Parameters
    ----------

    reverse : bool
      Passed on as it is.
    """
    #  void AbstractDomain::setReverseX(bool reverse)
    self.uglySide.call('ritual_ZN14AbstractDomain11setReverseXEb', reverse)

  @overload(bool)
  def setReverseY(self, reverse: bool) -> None:
    """
    Calls Qt's 'void AbstractDomain::setReverseY(bool reverse)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#setReverseY

    Parameters
    ----------

    reverse : bool
      Passed on as it is.
    """
    #  void AbstractDomain::setReverseY(bool reverse)
    self.uglySide.call('ritual_ZN14AbstractDomain11setReverseYEb', reverse)

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
    Qt's 'AbstractDomain::AbstractDomain(QObject *object)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'AbstractDomain.__init__' has no cute function yet. Qt's "
        "'AbstractDomain::AbstractDomain(QObject *object)': the class is "
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

  def type(self) -> DomainType:
    """
    Calls Qt's 'DomainType AbstractDomain::type()'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#type

    Returns
    -------

    DomainType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DomainType(number)'
      gives.
    """
    #  DomainType AbstractDomain::type()
    return AbstractDomain.DomainType(self.uglySide.call(
        'ritual_ZN14AbstractDomain4typeEv',
    ))

  @overload(bool)
  def blockRangeSignals(self, block: bool) -> None:
    """
    Calls Qt's 'void AbstractDomain::blockRangeSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#blockRangeSignals

    Parameters
    ----------

    block : bool
      Passed on as it is.
    """
    #  void AbstractDomain::blockRangeSignals(bool block)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain17blockRangeSignalsEb', block,
    )

  def zoomReset(self) -> None:
    """
    Calls Qt's 'void AbstractDomain::zoomReset()'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#zoomReset
    """
    #  void AbstractDomain::zoomReset()
    self.uglySide.call('ritual_ZN14AbstractDomain9zoomResetEv')

  def storeZoomReset(self) -> None:
    """
    Calls Qt's 'void AbstractDomain::storeZoomReset()'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#storeZoomReset
    """
    #  void AbstractDomain::storeZoomReset()
    self.uglySide.call('ritual_ZN14AbstractDomain14storeZoomResetEv')

  def isZoomed(self) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::isZoomed()'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#isZoomed
    """
    #  bool AbstractDomain::isZoomed()
    return self.uglySide.call('ritual_ZN14AbstractDomain8isZoomedEv')

  @overload(QRectF)
  def zoomIn(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void AbstractDomain::zoomIn(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#zoomIn

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void AbstractDomain::zoomIn(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain6zoomInERK6QRectF', self._valueOf(rect),
    )

  @overload(QRectF)
  def zoomOut(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void AbstractDomain::zoomOut(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#zoomOut

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void AbstractDomain::zoomOut(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain7zoomOutERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float)
  def move(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::move(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#move

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void AbstractDomain::move(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN14AbstractDomain4moveEdd', dx, dy)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def attachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::attachAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#attachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
    ritual = 'ritual_ZN14AbstractDomain10attachAxisEP13QAbstractAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14AbstractDomain10attachAxisEP13QAbstractAxis'
    return self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstractAxis)
  @overload(NoneType)
  def detachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool AbstractDomain::detachAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#detachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
    ritual = 'ritual_ZN14AbstractDomain10detachAxisEP13QAbstractAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14AbstractDomain10detachAxisEP13QAbstractAxis'
    return self.uglySide.call(ritual, self._addressOf(axis))

  def updated(self) -> None:
    """
    Calls Qt's 'void AbstractDomain::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#updated
    """
    #  void AbstractDomain::updated()
    self.uglySide.call('ritual_ZN14AbstractDomain7updatedEv')

  @overload(float, float)
  def rangeHorizontalChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::rangeHorizontalChanged(qreal min, qreal
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#rangeHorizontalChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::rangeHorizontalChanged(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain22rangeHorizontalChangedEdd', min, max,
    )

  @overload(float, float)
  def rangeVerticalChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::rangeVerticalChanged(qreal min, qreal
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#rangeVerticalChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::rangeVerticalChanged(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain20rangeVerticalChangedEdd', min, max,
    )

  @overload(float, float)
  def handleVerticalAxisRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::handleVerticalAxisRangeChanged(qreal
    min, qreal max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#handleVerticalAxisRangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::handleVerticalAxisRangeChanged(qreal min, qreal
    #      max)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain30handleVerticalAxisRangeChangedEdd',
        min, max,
    )

  @overload(float, float)
  def handleHorizontalAxisRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void AbstractDomain::handleHorizontalAxisRangeChanged(qreal
    min, qreal max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void AbstractDomain::handleHorizontalAxisRangeChanged(qreal min, qreal
    #      max)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain32handleHorizontalAxisRangeChangedEdd',
        min, max,
    )

  @overload(bool)
  def handleReverseXChanged(self, reverse: bool) -> None:
    """
    Calls Qt's 'void AbstractDomain::handleReverseXChanged(bool reverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#handleReverseXChanged

    Parameters
    ----------

    reverse : bool
      Passed on as it is.
    """
    #  void AbstractDomain::handleReverseXChanged(bool reverse)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain21handleReverseXChangedEb', reverse,
    )

  @overload(bool)
  def handleReverseYChanged(self, reverse: bool) -> None:
    """
    Calls Qt's 'void AbstractDomain::handleReverseYChanged(bool reverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractdomain.html#handleReverseYChanged

    Parameters
    ----------

    reverse : bool
      Passed on as it is.
    """
    #  void AbstractDomain::handleReverseYChanged(bool reverse)
    self.uglySide.call(
        'ritual_ZN14AbstractDomain21handleReverseYChangedEb', reverse,
    )

  @overload(QRectF)
  def fixZoomRect(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractDomain::fixZoomRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractdomain.html#fixZoomRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractDomain::fixZoomRect(const QRectF &rect)
    address = self.uglySide.call(
        'ritual_ZN14AbstractDomain11fixZoomRectERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  def adjustLogDomainRanges(*__, **_) -> Never:
    """
    Qt's 'void AbstractDomain::adjustLogDomainRanges(qreal &min, qreal
    &max)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'AbstractDomain.adjustLogDomainRanges' has no cute function yet. "
        "Qt's 'void AbstractDomain::adjustLogDomainRanges(qreal &min, qreal "
        "&max)': takes a number to change where it is.")

  @staticmethod
  def calculateGeometryPoint(*__, **_) -> Never:
    """
    Qt's 'QPointF AbstractDomain::calculateGeometryPoint(const QPointF
    &point, bool &ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'AbstractDomain.calculateGeometryPoint' has no cute function yet. "
        "Qt's 'QPointF AbstractDomain::calculateGeometryPoint(const QPointF "
        "&point, bool &ok) const': takes a number to change where it is.")

  @staticmethod
  def looseNiceNumbers(*__, **_) -> Never:
    """
    Qt's 'void AbstractDomain::looseNiceNumbers(qreal &min, qreal &max, int
    &ticksCount)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'AbstractDomain.looseNiceNumbers' has no cute function yet. Qt's "
        "'void AbstractDomain::looseNiceNumbers(qreal &min, qreal &max, int "
        "&ticksCount)': takes a number to change where it is.")
