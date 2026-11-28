"""
QValue3DAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qvalue3daxis_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QValue3DAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QAbstract3DAxisPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QValue3DAxis


class QValue3DAxisPrivate(QAbstract3DAxisPrivate):
  """
  The cute side of Qt's QValue3DAxisPrivate: a plain Python object standing
  in front of one C++ QValue3DAxisPrivate.

  It is built on the cute 'QAbstract3DAxisPrivate', as Qt's
  QValue3DAxisPrivate is built on Qt's QAbstract3DAxisPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QValue3DAxisPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'q_func', 'setRange', 'setMin',
  'setMax', 'emitLabelsChanged', 'emitFormatterDirty', 'updateLabels',
  'allowZero', 'allowNegatives', 'allowMinMaxSame'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QValue3DAxis *QValue3DAxisPrivate::q_func() const': takes in
    Python what 'QValue3DAxis *QValue3DAxisPrivate::q_func()' takes.
  - Qt's 'QValue3DAxisPrivate::~QValue3DAxisPrivate()': the destructor:
    Python never removes a C++ QValue3DAxisPrivate.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QValue3DAxisPrivate is created at the first use, not by
    'QValue3DAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QValue3DAxisPrivate.
  - Each name of Qt's QValue3DAxisPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QValue3DAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QValue3DAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QValue3DAxisPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  @overload(float, float, bool)
  def setRange(
      self,
      min: float,
      max: float,
      suppressWarnings: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::setRange(float min, float max, bool
    suppressWarnings)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.

    suppressWarnings : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QValue3DAxisPrivate::setRange(float min, float max, bool
    #      suppressWarnings)
    ritual = 'ritual_ZN19QValue3DAxisPrivate8setRangeEffb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate8setRangeEffb'
    self.uglySide.call(ritual, min, max, suppressWarnings)

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::setMin(float min)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisprivate.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QValue3DAxisPrivate::setMin(float min)
    ritual = 'ritual_ZN19QValue3DAxisPrivate6setMinEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate6setMinEf'
    self.uglySide.call(ritual, min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::setMax(float max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisprivate.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QValue3DAxisPrivate::setMax(float max)
    ritual = 'ritual_ZN19QValue3DAxisPrivate6setMaxEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate6setMaxEf'
    self.uglySide.call(ritual, max)

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
    Qt's 'QValue3DAxisPrivate::QValue3DAxisPrivate()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'Utils'.
    """
    raise NotImplementedError(
        "'QValue3DAxisPrivate.__init__' has no cute function yet. Qt's "
        "'QValue3DAxisPrivate::QValue3DAxisPrivate()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'Utils'.")

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

  def q_func(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QValue3DAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisprivate.html#q_func

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QValue3DAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QValue3DAxisPrivate6q_funcEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def emitLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::emitLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#emitLabelsChanged
    """
    #  void QValue3DAxisPrivate::emitLabelsChanged()
    self.uglySide.call('ritual_ZN19QValue3DAxisPrivate17emitLabelsChangedEv')

  def emitFormatterDirty(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::emitFormatterDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#emitFormatterDirty
    """
    #  void QValue3DAxisPrivate::emitFormatterDirty()
    self.uglySide.call(
        'ritual_ZN19QValue3DAxisPrivate18emitFormatterDirtyEv',
    )

  def updateLabels(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::updateLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#updateLabels
    """
    #  void QValue3DAxisPrivate::updateLabels()
    self.uglySide.call('ritual_ZN19QValue3DAxisPrivate12updateLabelsEv')

  def allowZero(self) -> bool:
    """
    Calls Qt's 'bool QValue3DAxisPrivate::allowZero()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisprivate.html#allowZero
    """
    #  bool QValue3DAxisPrivate::allowZero()
    ritual = 'ritual_ZN19QValue3DAxisPrivate9allowZeroEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate9allowZeroEv'
    return self.uglySide.call(ritual)

  def allowNegatives(self) -> bool:
    """
    Calls Qt's 'bool QValue3DAxisPrivate::allowNegatives()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#allowNegatives
    """
    #  bool QValue3DAxisPrivate::allowNegatives()
    ritual = 'ritual_ZN19QValue3DAxisPrivate14allowNegativesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate14allowNegativesEv'
    return self.uglySide.call(ritual)

  def allowMinMaxSame(self) -> bool:
    """
    Calls Qt's 'bool QValue3DAxisPrivate::allowMinMaxSame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#allowMinMaxSame
    """
    #  bool QValue3DAxisPrivate::allowMinMaxSame()
    ritual = 'ritual_ZN19QValue3DAxisPrivate15allowMinMaxSameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate15allowMinMaxSameEv'
    return self.uglySide.call(ritual)
