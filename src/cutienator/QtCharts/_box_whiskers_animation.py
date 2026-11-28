"""
BoxWhiskersAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/boxwhiskersanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means BoxWhiskersAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import ChartAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import BoxWhiskersData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BoxWhiskersData = WAIT['BoxWhiskersData']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoxWhiskersAnimation(ChartAnimation):
  """
  The cute side of Qt's BoxWhiskersAnimation: a plain Python object standing
  in front of one C++ BoxWhiskersAnimation.

  It is built on the cute 'ChartAnimation', as Qt's BoxWhiskersAnimation is
  built on Qt's ChartAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's BoxWhiskersAnimation that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'interpolated',
  'updateCurrentValue', 'setup', 'setEndData', 'setStartData'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BoxWhiskersAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int BoxWhiskersAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'BoxWhiskersAnimation::BoxWhiskersAnimation(BoxWhiskers *box,
    BoxPlotAnimation *boxPlotAnimation, int duration, QEasingCurve &curve)':
    takes a type Python has no way to hand over yet.
  - Qt's 'BoxWhiskersAnimation::~BoxWhiskersAnimation()': the destructor:
    Python never removes a C++ BoxWhiskersAnimation.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ BoxWhiskersAnimation is created at the first use, not by
    'BoxWhiskersAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BoxWhiskersAnimation.
  - Qt tells when it has removed the C++ BoxWhiskersAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's BoxWhiskersAnimation that has no cute function yet,
    '__init__', 'moveMedianLine', holds a function that raises
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
    Calls Qt's 'QString BoxWhiskersAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskersanimation.html#tr

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
    #  QString BoxWhiskersAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20BoxWhiskersAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BoxWhiskersAnimation'

  #  A C++ BoxWhiskersAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BoxWhiskersAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *BoxWhiskersAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxwhiskersanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BoxWhiskersAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20BoxWhiskersAnimation10metaObjectEv',
    )
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
    Calls Qt's 'QVariant BoxWhiskersAnimation::interpolated(const QVariant
    &from, const QVariant &to, qreal progress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxwhiskersanimation.html#interpolated

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
    #  QVariant BoxWhiskersAnimation::interpolated(const QVariant &from,
    #      const QVariant &to, qreal progress) const
    ritual = 'ritual_ZNK20BoxWhiskersAnimation12interpolatedERK8QVariantS2_d'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20BoxWhiskersAnimation12interpolatedERK8QVariantS2'
          '_d')
    address = self.uglySide.call(
        ritual, self._valueOf(from_), self._valueOf(to), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BoxWhiskersData)
  def setEndData(self, endData: BoxWhiskersData) -> None:
    """
    Calls Qt's 'void BoxWhiskersAnimation::setEndData(const BoxWhiskersData
    &endData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxwhiskersanimation.html#setEndData

    Parameters
    ----------

    endData : BoxWhiskersData
      Passed on as a value: Qt reads the C++ BoxWhiskersData, which stays
      Python's own.
    """
    #  void BoxWhiskersAnimation::setEndData(const BoxWhiskersData &endData)
    self.uglySide.call(
        'ritual_ZN20BoxWhiskersAnimation10setEndDataERK15BoxWhiskersData',
        self._valueOf(endData),
    )

  @overload(BoxWhiskersData)
  def setStartData(self, endData: BoxWhiskersData) -> None:
    """
    Calls Qt's 'void BoxWhiskersAnimation::setStartData(const BoxWhiskersData
    &endData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxwhiskersanimation.html#setStartData

    Parameters
    ----------

    endData : BoxWhiskersData
      Passed on as a value: Qt reads the C++ BoxWhiskersData, which stays
      Python's own.
    """
    #  void BoxWhiskersAnimation::setStartData(const BoxWhiskersData
    #      &endData)
    self.uglySide.call(
        'ritual_ZN20BoxWhiskersAnimation12setStartDataERK15BoxWhiskersData',
        self._valueOf(endData),
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
    Qt's 'BoxWhiskersAnimation::BoxWhiskersAnimation(BoxWhiskers *box,
    BoxPlotAnimation *boxPlotAnimation, int duration, QEasingCurve &curve)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'BoxWhiskersAnimation.__init__' has no cute function yet. Qt's "
        "'BoxWhiskersAnimation::BoxWhiskersAnimation(BoxWhiskers *box, "
        "BoxPlotAnimation *boxPlotAnimation, int duration, QEasingCurve "
        "&curve)': takes a type Python has no way to hand over yet.")

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
    Calls Qt's 'void BoxWhiskersAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxwhiskersanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void BoxWhiskersAnimation::updateCurrentValue(const QVariant &value)
    ritual = (
        'ritual_ZN20BoxWhiskersAnimation18updateCurrentValueERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20BoxWhiskersAnimation18updateCurrentValueERK8QVari'
          'ant')
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(BoxWhiskersData, BoxWhiskersData)
  def setup(
      self,
      startData: BoxWhiskersData,
      endData: BoxWhiskersData,
  ) -> None:
    """
    Calls Qt's 'void BoxWhiskersAnimation::setup(const BoxWhiskersData
    &startData, const BoxWhiskersData &endData)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskersanimation.html#setup

    Parameters
    ----------

    startData : BoxWhiskersData
      Passed on as a value: Qt reads the C++ BoxWhiskersData, which stays
      Python's own.

    endData : BoxWhiskersData
      Passed on as a value: Qt reads the C++ BoxWhiskersData, which stays
      Python's own.
    """
    #  void BoxWhiskersAnimation::setup(const BoxWhiskersData &startData,
    #      const BoxWhiskersData &endData)
    self.uglySide.call(
        'ritual_ZN20BoxWhiskersAnimation5setupERK15BoxWhiskersDataS2_',
        self._valueOf(startData), self._valueOf(endData),
    )

  @staticmethod
  def moveMedianLine(*__, **_) -> Never:
    """
    Qt's 'void BoxWhiskersAnimation::moveMedianLine(bool move)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'BoxWhiskersAnimation.moveMedianLine' has no cute function yet. "
        "Qt's 'void BoxWhiskersAnimation::moveMedianLine(bool move)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
