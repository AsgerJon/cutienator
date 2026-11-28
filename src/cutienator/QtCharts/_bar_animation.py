"""
BarAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/baranimation_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means BarAnimation to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import ChartAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BarAnimation(ChartAnimation):
  """
  The cute side of Qt's BarAnimation: a plain Python object standing in front
  of one C++ BarAnimation.

  It is built on the cute 'ChartAnimation', as Qt's BarAnimation is built on
  Qt's ChartAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's BarAnimation that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'interpolated',
  'updateCurrentValue', 'setup'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BarAnimation::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int BarAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'BarAnimation::BarAnimation(AbstractBarChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
  - Qt's 'BarAnimation::~BarAnimation()': the destructor: Python never
    removes a C++ BarAnimation.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ BarAnimation is created at the first use, not by
    'BarAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BarAnimation.
  - Qt tells when it has removed the C++ BarAnimation. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's BarAnimation that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString BarAnimation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/baranimation.html#tr

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
    #  QString BarAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12BarAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BarAnimation'

  #  A C++ BarAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BarAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *BarAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/baranimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BarAnimation::metaObject() const
    address = self.uglySide.call('ritual_ZNK12BarAnimation10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QVariant, QVariant, float)
  def interpolated(
      self,
      from_: QVariant,
      to: QVariant,
      progress: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant BarAnimation::interpolated(const QVariant &from,
    const QVariant &to, qreal progress) const'.

    Qt's own words: https://doc.qt.io/qt-6/baranimation.html#interpolated

    Parameters
    ----------

    from_ : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    to : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant BarAnimation::interpolated(const QVariant &from, const
    #      QVariant &to, qreal progress) const
    ritual = 'ritual_ZNK12BarAnimation12interpolatedERK8QVariantS2_d'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12BarAnimation12interpolatedERK8QVariantS2_d'
    address = self.uglySide.call(
        ritual, self._valueOf(from_), self._valueOf(to), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'BarAnimation::BarAnimation(AbstractBarChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'BarAnimation.__init__' has no cute function yet. Qt's "
        "'BarAnimation::BarAnimation(AbstractBarChartItem *item, int "
        "duration, QEasingCurve &curve)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void BarAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/baranimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void BarAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN12BarAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12BarAnimation18updateCurrentValueERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(QList[QRectF], QList[QRectF])
  def setup(
      self,
      oldLayout: QList[QRectF],
      newLayout: QList[QRectF],
  ) -> None:
    """
    Calls Qt's 'void BarAnimation::setup(const QList<QRectF> &oldLayout,
    const QList<QRectF> &newLayout)'.

    Qt's own words: https://doc.qt.io/qt-6/baranimation.html#setup

    Parameters
    ----------

    oldLayout : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    newLayout : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void BarAnimation::setup(const QList<QRectF> &oldLayout, const
    #      QList<QRectF> &newLayout)
    self.uglySide.call(
        'ritual_ZN12BarAnimation5setupERK5QListI6QRectFES4_',
        self._valueOf(oldLayout), self._valueOf(newLayout),
    )
