"""
PolarDomain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polardomain_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means PolarDomain to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import AbstractDomain

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarDomain(AbstractDomain):
  """
  The cute side of Qt's PolarDomain: a plain Python object standing in front
  of one C++ PolarDomain.

  It is built on the cute 'AbstractDomain', as Qt's PolarDomain is built on
  Qt's AbstractDomain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarDomain that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'setSize',
  'calculateGeometryPoints', 'polarCoordinateToPoint'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarDomain::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PolarDomain::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PolarDomain::~PolarDomain()': the destructor: Python never removes
    a C++ PolarDomain.
  - Qt's 'QPointF PolarDomain::calculateGeometryPoint(const QPointF &point,
    bool &ok) const': takes a number to change where it is.
  - Qt's 'qreal PolarDomain::toAngularCoordinate(qreal value, bool &ok)
    const': takes a number to change where it is.
  - Qt's 'qreal PolarDomain::toRadialCoordinate(qreal value, bool &ok)
    const': takes a number to change where it is.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ PolarDomain is created at the first use, not by
    'PolarDomain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarDomain.
  - Qt tells when it has removed the C++ PolarDomain. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's PolarDomain that has no cute function yet, '__init__',
    'toAngularCoordinate', 'toRadialCoordinate', holds a function that raises
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
    Calls Qt's 'QString PolarDomain::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/polardomain.html#tr

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
    #  QString PolarDomain::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11PolarDomain2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarDomain'

  #  A C++ PolarDomain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarDomain'

  #  The functions Qt calls itself that PolarDomain is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'toAngularCoordinate': (
          'qreal PolarDomain::toAngularCoordinate(qreal, bool &) const',
      ),
      'toRadialCoordinate': (
          'qreal PolarDomain::toRadialCoordinate(qreal, bool &) const',
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
    Calls Qt's 'const QMetaObject *PolarDomain::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/polardomain.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarDomain::metaObject() const
    address = self.uglySide.call('ritual_ZNK11PolarDomain10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QList[QPointF])
  def calculateGeometryPoints(self, list: QList[QPointF]) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> PolarDomain::calculateGeometryPoints(const
    QList<QPointF> &list) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polardomain.html#calculateGeometryPoints

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
    #  QList<QPointF> PolarDomain::calculateGeometryPoints(const
    #      QList<QPointF> &list) const
    address = self.uglySide.call(
        'ritual_ZNK11PolarDomain23calculateGeometryPointsERK5QListI7QPointF'
        'E',
        self._valueOf(list),
    )
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  @overload(float, float)
  def polarCoordinateToPoint(
      self,
      angularCoordinate: float,
      radialCoordinate: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF PolarDomain::polarCoordinateToPoint(qreal
    angularCoordinate, qreal radialCoordinate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polardomain.html#polarCoordinateToPoint

    Parameters
    ----------

    angularCoordinate : float
      Passed on as it is.

    radialCoordinate : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF PolarDomain::polarCoordinateToPoint(qreal angularCoordinate,
    #      qreal radialCoordinate) const
    address = self.uglySide.call(
        'ritual_ZNK11PolarDomain22polarCoordinateToPointEdd',
        angularCoordinate, radialCoordinate,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void PolarDomain::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/polardomain.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void PolarDomain::setSize(const QSizeF &size)
    ritual = 'ritual_ZN11PolarDomain7setSizeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11PolarDomain7setSizeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(size))

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
    Qt's 'PolarDomain::PolarDomain(QObject *object)': the class is abstract,
    so C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'PolarDomain.__init__' has no cute function yet. Qt's "
        "'PolarDomain::PolarDomain(QObject *object)': the class is "
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

  @staticmethod
  def toAngularCoordinate(*__, **_) -> Never:
    """
    Qt's 'qreal PolarDomain::toAngularCoordinate(qreal value, bool &ok)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'PolarDomain.toAngularCoordinate' has no cute function yet. Qt's "
        "'qreal PolarDomain::toAngularCoordinate(qreal value, bool &ok) "
        "const': takes a number to change where it is.")

  @staticmethod
  def toRadialCoordinate(*__, **_) -> Never:
    """
    Qt's 'qreal PolarDomain::toRadialCoordinate(qreal value, bool &ok)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'PolarDomain.toRadialCoordinate' has no cute function yet. Qt's "
        "'qreal PolarDomain::toRadialCoordinate(qreal value, bool &ok) "
        "const': takes a number to change where it is.")
