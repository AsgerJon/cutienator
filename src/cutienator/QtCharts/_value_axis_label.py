"""
ValueAxisLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/valueaxislabel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ValueAxisLabel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import EditableAxisLabel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ValueAxisLabel(EditableAxisLabel):
  """
  The cute side of Qt's ValueAxisLabel: a plain Python object standing in
  front of one C++ ValueAxisLabel.

  It is built on the cute 'EditableAxisLabel', as Qt's ValueAxisLabel is
  built on Qt's EditableAxisLabel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ValueAxisLabel that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'keyPressEvent', 'value',
  'setValue', 'setInitialEditValue', 'finishEditing', 'resetBeforeEditValue',
  'valueChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ValueAxisLabel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ValueAxisLabel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ValueAxisLabel is created at the first use, not by
    'ValueAxisLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ValueAxisLabel.
  - Qt tells when it has removed the C++ ValueAxisLabel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString ValueAxisLabel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#tr

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
    #  QString ValueAxisLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14ValueAxisLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ValueAxisLabel'

  #  A C++ ValueAxisLabel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ValueAxisLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ValueAxisLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ValueAxisLabel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14ValueAxisLabel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> float:
    """
    Calls Qt's 'qreal ValueAxisLabel::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#value
    """
    #  qreal ValueAxisLabel::value() const
    return self.uglySide.call('ritual_ZNK14ValueAxisLabel5valueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void ValueAxisLabel::setValue(const qreal &value)'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void ValueAxisLabel::setValue(const qreal &value)
    self.uglySide.call('ritual_ZN14ValueAxisLabel8setValueERKd', value)

  def setInitialEditValue(self) -> None:
    """
    Calls Qt's 'void ValueAxisLabel::setInitialEditValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/valueaxislabel.html#setInitialEditValue
    """
    #  void ValueAxisLabel::setInitialEditValue()
    ritual = 'ritual_ZN14ValueAxisLabel19setInitialEditValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14ValueAxisLabel19setInitialEditValueEv'
    self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'ValueAxisLabel::ValueAxisLabel(QGraphicsItem *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#ValueAxisLabel

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ValueAxisLabel::ValueAxisLabel(QGraphicsItem *parent)
    self._noteCreation(ValueAxisLabel, lambda: Rituals.call(
        'ritual_ZN14ValueAxisLabelC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void ValueAxisLabel::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ValueAxisLabel::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN14ValueAxisLabel13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14ValueAxisLabel13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def finishEditing(self) -> None:
    """
    Calls Qt's 'void ValueAxisLabel::finishEditing()'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#finishEditing
    """
    #  void ValueAxisLabel::finishEditing()
    ritual = 'ritual_ZN14ValueAxisLabel13finishEditingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14ValueAxisLabel13finishEditingEv'
    self.uglySide.call(ritual)

  def resetBeforeEditValue(self) -> None:
    """
    Calls Qt's 'void ValueAxisLabel::resetBeforeEditValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/valueaxislabel.html#resetBeforeEditValue
    """
    #  void ValueAxisLabel::resetBeforeEditValue()
    ritual = 'ritual_ZN14ValueAxisLabel20resetBeforeEditValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14ValueAxisLabel20resetBeforeEditValueEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def valueChanged(self, oldValue: float, newValue: float) -> None:
    """
    Calls Qt's 'void ValueAxisLabel::valueChanged(qreal oldValue, qreal
    newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/valueaxislabel.html#valueChanged

    Parameters
    ----------

    oldValue : float
      Passed on as it is.

    newValue : float
      Passed on as it is.
    """
    #  void ValueAxisLabel::valueChanged(qreal oldValue, qreal newValue)
    self.uglySide.call(
        'ritual_ZN14ValueAxisLabel12valueChangedEdd', oldValue, newValue,
    )
