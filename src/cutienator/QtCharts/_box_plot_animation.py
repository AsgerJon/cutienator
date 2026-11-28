"""
BoxPlotAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/boxplotanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means BoxPlotAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import BoxWhiskers, ChartAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BoxWhiskers = WAIT['BoxWhiskers']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoxPlotAnimation(QObject):
  """
  The cute side of Qt's BoxPlotAnimation: a plain Python object standing in
  front of one C++ BoxPlotAnimation.

  It is built on the cute 'QObject', as Qt's BoxPlotAnimation is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's BoxPlotAnimation that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'addBox',
  'boxAnimation', 'boxChangeAnimation', 'setAnimationStart', 'stopAll',
  'removeBoxAnimation'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BoxPlotAnimation::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int BoxPlotAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'BoxPlotAnimation::BoxPlotAnimation(BoxPlotChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
  - Qt's 'BoxPlotAnimation::~BoxPlotAnimation()': the destructor: Python
    never removes a C++ BoxPlotAnimation.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ BoxPlotAnimation is created at the first use, not by
    'BoxPlotAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BoxPlotAnimation.
  - Qt tells when it has removed the C++ BoxPlotAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's BoxPlotAnimation that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString BoxPlotAnimation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotanimation.html#tr

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
    #  QString BoxPlotAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16BoxPlotAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BoxPlotAnimation'

  #  A C++ BoxPlotAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BoxPlotAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *BoxPlotAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BoxPlotAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16BoxPlotAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BoxWhiskers)
  @overload(NoneType)
  def setAnimationStart(self, box: Optional[BoxWhiskers]) -> None:
    """
    Calls Qt's 'void BoxPlotAnimation::setAnimationStart(BoxWhiskers *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotanimation.html#setAnimationStart

    Parameters
    ----------

    box : Optional[BoxWhiskers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxPlotAnimation::setAnimationStart(BoxWhiskers *box)
    self.uglySide.call(
        'ritual_ZN16BoxPlotAnimation17setAnimationStartEP11BoxWhiskers',
        self._addressOf(box),
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
    Qt's 'BoxPlotAnimation::BoxPlotAnimation(BoxPlotChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'BoxPlotAnimation.__init__' has no cute function yet. Qt's "
        "'BoxPlotAnimation::BoxPlotAnimation(BoxPlotChartItem *item, int "
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

  @overload(BoxWhiskers)
  @overload(NoneType)
  def addBox(self, box: Optional[BoxWhiskers]) -> None:
    """
    Calls Qt's 'void BoxPlotAnimation::addBox(BoxWhiskers *box)'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotanimation.html#addBox

    Parameters
    ----------

    box : Optional[BoxWhiskers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxPlotAnimation::addBox(BoxWhiskers *box)
    self.uglySide.call(
        'ritual_ZN16BoxPlotAnimation6addBoxEP11BoxWhiskers',
        self._addressOf(box),
    )

  @overload(BoxWhiskers)
  @overload(NoneType)
  def boxAnimation(
      self,
      box: Optional[BoxWhiskers],
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *BoxPlotAnimation::boxAnimation(BoxWhiskers
    *box)'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotanimation.html#boxAnimation

    Parameters
    ----------

    box : Optional[BoxWhiskers]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *BoxPlotAnimation::boxAnimation(BoxWhiskers *box)
    address = self.uglySide.call(
        'ritual_ZN16BoxPlotAnimation12boxAnimationEP11BoxWhiskers',
        self._addressOf(box),
    )
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  @overload(BoxWhiskers)
  @overload(NoneType)
  def boxChangeAnimation(
      self,
      box: Optional[BoxWhiskers],
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation
    *BoxPlotAnimation::boxChangeAnimation(BoxWhiskers *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotanimation.html#boxChangeAnimation

    Parameters
    ----------

    box : Optional[BoxWhiskers]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *BoxPlotAnimation::boxChangeAnimation(BoxWhiskers *box)
    address = self.uglySide.call(
        'ritual_ZN16BoxPlotAnimation18boxChangeAnimationEP11BoxWhiskers',
        self._addressOf(box),
    )
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  def stopAll(self) -> None:
    """
    Calls Qt's 'void BoxPlotAnimation::stopAll()'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotanimation.html#stopAll
    """
    #  void BoxPlotAnimation::stopAll()
    self.uglySide.call('ritual_ZN16BoxPlotAnimation7stopAllEv')

  @overload(BoxWhiskers)
  @overload(NoneType)
  def removeBoxAnimation(self, box: Optional[BoxWhiskers]) -> None:
    """
    Calls Qt's 'void BoxPlotAnimation::removeBoxAnimation(BoxWhiskers *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotanimation.html#removeBoxAnimation

    Parameters
    ----------

    box : Optional[BoxWhiskers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxPlotAnimation::removeBoxAnimation(BoxWhiskers *box)
    self.uglySide.call(
        'ritual_ZN16BoxPlotAnimation18removeBoxAnimationEP11BoxWhiskers',
        self._addressOf(box),
    )
