"""
QInputMethodQueryEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QInputMethodQueryEvent(QEvent):
  """
  The cute side of Qt's QInputMethodQueryEvent: a plain Python object
  standing in front of one C++ QInputMethodQueryEvent.

  It is built on the cute 'QEvent', as Qt's QInputMethodQueryEvent is built
  on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputMethodQueryEvent that has a ritual and that
  Python can call so far, 4 names in all: 'clone', 'queries', 'setValue',
  'value'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputMethodQueryEvent::QInputMethodQueryEvent(const
    QInputMethodQueryEvent &a0)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QInputMethodQueryEvent &QInputMethodQueryEvent::operator=(const
    QInputMethodQueryEvent &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QInputMethodQueryEvent::~QInputMethodQueryEvent()': the destructor:
    Python never removes a C++ QInputMethodQueryEvent.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QInputMethodQueryEvent is created at the first use, not by
    'QInputMethodQueryEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputMethodQueryEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputMethodQueryEvent'

  #  A C++ QInputMethodQueryEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInputMethodQueryEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QInputMethodQueryEvent]:
    """
    Calls Qt's 'QInputMethodQueryEvent *QInputMethodQueryEvent::clone()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethodqueryevent.html#clone

    Returns
    -------

    Optional[QInputMethodQueryEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputMethodQueryEvent *QInputMethodQueryEvent::clone() const
    ritual = 'ritual_ZNK22QInputMethodQueryEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QInputMethodQueryEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QInputMethodQueryEvent._cuteAt(address)

  def queries(self) -> Qt.InputMethodQueries:
    """
    Calls Qt's 'Qt::InputMethodQueries QInputMethodQueryEvent::queries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodqueryevent.html#queries

    Returns
    -------

    Qt.InputMethodQueries
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodQueries QInputMethodQueryEvent::queries() const
    return Qt.InputMethodQueries(self.uglySide.call(
        'ritual_ZNK22QInputMethodQueryEvent7queriesEv',
    ))

  @overload(Qt.InputMethodQuery)
  def value(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QInputMethodQueryEvent::value(Qt::InputMethodQuery
    query) const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethodqueryevent.html#value

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QInputMethodQueryEvent::value(Qt::InputMethodQuery query)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QInputMethodQueryEvent5valueEN2Qt16InputMethodQueryE',
        query.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.InputMethodQuery, QVariant)
  def setValue(self, query: Qt.InputMethodQuery, value: QVariant) -> None:
    """
    Calls Qt's 'void QInputMethodQueryEvent::setValue(Qt::InputMethodQuery
    query, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodqueryevent.html#setValue

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QInputMethodQueryEvent::setValue(Qt::InputMethodQuery query,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN22QInputMethodQueryEvent8setValueEN2Qt16InputMethodQueryE'
        'RK8QVariant',
        query.value, self._valueOf(value),
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

  @overload(Qt.InputMethodQueries)
  def __init__(self, queries: Qt.InputMethodQueries) -> None:
    """
    Notes what was given, for Qt's
    'QInputMethodQueryEvent::QInputMethodQueryEvent(Qt::InputMethodQueries
    queries)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodqueryevent.html#QInputMethodQueryEvent

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  QInputMethodQueryEvent::QInputMethodQueryEvent(Qt::InputMethodQueries
    #      queries)
    self._noteCreation(QInputMethodQueryEvent, lambda: Rituals.call(
        'ritual_ZN22QInputMethodQueryEventC1E6QFlagsIN2Qt16InputMethodQuery'
        'EE',
        queries.value,
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
