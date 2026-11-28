"""
QQuickTimeLineValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTimeLineValue to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickTimeLineObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickTimeLine


class QQuickTimeLineValue(QQuickTimeLineObject):
  """
  The cute side of Qt's QQuickTimeLineValue: a plain Python object standing
  in front of one C++ QQuickTimeLineValue.

  It is built on the cute 'QQuickTimeLineObject', as Qt's QQuickTimeLineValue
  is built on Qt's QQuickTimeLineObject, and has everything that class has.

  C++ hands a QQuickTimeLineValue around as a copy, so every C++
  QQuickTimeLineValue behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickTimeLineValue that has a ritual and that
  Python can call so far, 3 names in all: 'value', 'setValue', 'timeLine'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qreal QQuickTimeLineValue::operator double() const': an operator
    Python has no name for.
  - Qt's 'QQuickTimeLineValue &QQuickTimeLineValue::operator=(qreal v)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQuickTimeLineValue::~QQuickTimeLineValue()': the destructor:
    Python removes its C++ QQuickTimeLineValue by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickTimeLineValue is created at the first use, not by
    'QQuickTimeLineValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickTimeLineValue back gives a copy the ritual made
    for Python, in a new cute QQuickTimeLineValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTimeLineValue'

  #  The functions Qt calls itself that QQuickTimeLineValue is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'value': (
          ('_ZNK19QQuickTimeLineValue5valueEv',
           ('double', 'number', ''),
           ()),
      ),
      'setValue': (
          ('_ZN19QQuickTimeLineValue8setValueEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QQuickTimeLineValue()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickTimeLineValue behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQuickTimeLineValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickTimeLineValue::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimelinevalue.html#value
    """
    #  qreal QQuickTimeLineValue::value() const
    ritual = 'ritual_ZNK19QQuickTimeLineValue5valueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickTimeLineValue5valueEv'
    return self.uglySide.call(ritual)

  def timeLine(self) -> Optional[QQuickTimeLine]:
    """
    Calls Qt's 'QQuickTimeLine *QQuickTimeLineValue::timeLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimelinevalue.html#timeLine

    Returns
    -------

    Optional[QQuickTimeLine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTimeLine *QQuickTimeLineValue::timeLine() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickTimeLineValue8timeLineEv',
    )
    from . import QQuickTimeLine
    return QQuickTimeLine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setValue(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickTimeLineValue::setValue(qreal v)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimelinevalue.html#setValue

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickTimeLineValue::setValue(qreal v)
    ritual = 'ritual_ZN19QQuickTimeLineValue8setValueEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickTimeLineValue8setValueEd'
    self.uglySide.call(ritual, v)

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
  @overload(float)
  def __init__(self, v: float = 0.0) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTimeLineValue::QQuickTimeLineValue(qreal v)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelinevalue.html#QQuickTimeLineValue

    Parameters
    ----------

    v : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QQuickTimeLineValue::QQuickTimeLineValue(qreal v)
    self._noteCreation(QQuickTimeLineValue, lambda: Rituals.call(
        'ritual_ZN19QQuickTimeLineValueC1Ed', v,
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
