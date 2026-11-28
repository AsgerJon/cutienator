"""
QValue3DAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qvalue3daxis_p.h,
#  Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QMetaObject
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
  Python can call so far, 11 names in all: 'metaObject', 'setRange',
  'setMin', 'setMax', 'emitLabelsChanged', 'formatterDirty', 'updateLabels',
  'allowZero', 'allowNegatives', 'allowMinMaxSame', 'qptr'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QValue3DAxisPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QValue3DAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QValue3DAxisPrivate::~QValue3DAxisPrivate()': the destructor:
    Python never removes a C++ QValue3DAxisPrivate.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QValue3DAxisPrivate.

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
  - Qt tells when it has removed the C++ QValue3DAxisPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
  __qt_part__ = 'QtDataVisualization'

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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QValue3DAxisPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QValue3DAxisPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QValue3DAxisPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QValue3DAxisPrivate::QValue3DAxisPrivate(QValue3DAxis *q)': leans
    on 'QValue3DAxisPrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QValue3DAxisPrivate.__init__' has no cute function yet. Qt's "
        "'QValue3DAxisPrivate::QValue3DAxisPrivate(QValue3DAxis *q)': leans "
        "on 'QValue3DAxisPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def emitLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::emitLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#emitLabelsChanged
    """
    #  void QValue3DAxisPrivate::emitLabelsChanged()
    self.uglySide.call('ritual_ZN19QValue3DAxisPrivate17emitLabelsChangedEv')

  def formatterDirty(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::formatterDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#formatterDirty
    """
    #  void QValue3DAxisPrivate::formatterDirty()
    self.uglySide.call('ritual_ZN19QValue3DAxisPrivate14formatterDirtyEv')

  def updateLabels(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisPrivate::updateLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisprivate.html#updateLabels
    """
    #  void QValue3DAxisPrivate::updateLabels()
    ritual = 'ritual_ZN19QValue3DAxisPrivate12updateLabelsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QValue3DAxisPrivate12updateLabelsEv'
    self.uglySide.call(ritual)

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

  def qptr(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QValue3DAxisPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisprivate.html#qptr

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QValue3DAxisPrivate::qptr()
    address = self.uglySide.call('ritual_ZN19QValue3DAxisPrivate4qptrEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)
