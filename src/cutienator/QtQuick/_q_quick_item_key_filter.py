"""
QQuickItemKeyFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickItemKeyFilter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from ..QtGui import QInputMethodEvent, QKeyEvent
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemKeyFilter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemKeyFilter: a plain Python object standing
  in front of one C++ QQuickItemKeyFilter.

  C++ hands a QQuickItemKeyFilter around as a copy, so every C++
  QQuickItemKeyFilter behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickItemKeyFilter that has a ritual and that
  Python can call so far, 6 names in all: 'keyPressed', 'keyReleased',
  'inputMethodEvent', 'inputMethodQuery', 'shortcutOverrideEvent',
  'componentComplete'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickItemKeyFilter::~QQuickItemKeyFilter()': the destructor:
    Python removes its C++ QQuickItemKeyFilter by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickItemKeyFilter is created at the first use, not by
    'QQuickItemKeyFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickItemKeyFilter back gives a copy the ritual made
    for Python, in a new cute QQuickItemKeyFilter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemKeyFilter'

  #  A C++ QQuickItemKeyFilter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemKeyFilter'

  #  The functions Qt calls itself that QQuickItemKeyFilter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'keyPressed': (
          ('_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
               ('bool', 'number', ''),
           )),
      ),
      'keyReleased': (
          ('_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
               ('bool', 'number', ''),
           )),
      ),
      'inputMethodEvent': (
          ('_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEvent'
           'b',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QInputMethodEvent'),
               ('bool', 'number', ''),
           )),
      ),
      'inputMethodQuery': (
          ('_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMethodQu'
           'eryE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtCore:Qt.InputMethodQuery'),
           )),
      ),
      'shortcutOverrideEvent': (
          ('_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'componentComplete': (
          ('_ZN19QQuickItemKeyFilter17componentCompleteEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~QQuickItemKeyFilter()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickItemKeyFilter behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQuickItemKeyFilterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickItemKeyFilter::inputMethodQuery(Qt::InputMethodQuery query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickItemKeyFilter::inputMethodQuery(Qt::InputMethodQuery
    #      query) const
    ritual = (
        'ritual_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMetho'
        'dQueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16Inpu'
          'tMethodQueryE')
    address = self._callAs('QQuickItemKeyFilter', ritual, query.value)
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, a0: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemKeyFilter::QQuickItemKeyFilter(QQuickItem *a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#QQuickItemKeyFilter

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickItemKeyFilter::QQuickItemKeyFilter(QQuickItem *a0)
    self._noteCreation(QQuickItemKeyFilter, lambda: Rituals.call(
        'ritual_ZN19QQuickItemKeyFilterC1EP10QQuickItem',
        self._addressOf(a0),
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

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def keyPressed(self, event: Optional[QKeyEvent], post: bool) -> None:
    """
    Calls Qt's 'void QQuickItemKeyFilter::keyPressed(QKeyEvent *event, bool
    post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#keyPressed

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickItemKeyFilter::keyPressed(QKeyEvent *event, bool post)
    ritual = 'ritual_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb'
    self._callAs('QQuickItemKeyFilter', ritual, self._addressOf(event), post)

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def keyReleased(self, event: Optional[QKeyEvent], post: bool) -> None:
    """
    Calls Qt's 'void QQuickItemKeyFilter::keyReleased(QKeyEvent *event, bool
    post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#keyReleased

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickItemKeyFilter::keyReleased(QKeyEvent *event, bool post)
    ritual = 'ritual_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb'
    self._callAs('QQuickItemKeyFilter', ritual, self._addressOf(event), post)

  @overload(QInputMethodEvent, bool)
  @overload(NoneType, bool)
  def inputMethodEvent(
      self,
      event: Optional[QInputMethodEvent],
      post: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemKeyFilter::inputMethodEvent(QInputMethodEvent
    *event, bool post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickItemKeyFilter::inputMethodEvent(QInputMethodEvent *event,
    #      bool post)
    ritual = (
        'ritual_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEv'
        'entb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMe'
          'thodEventb')
    self._callAs('QQuickItemKeyFilter', ritual, self._addressOf(event), post)

  @overload(QKeyEvent)
  @overload(NoneType)
  def shortcutOverrideEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickItemKeyFilter::shortcutOverrideEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#shortcutOverrideEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemKeyFilter::shortcutOverrideEvent(QKeyEvent *event)
    ritual = (
        'ritual_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKey'
          'Event')
    self._callAs('QQuickItemKeyFilter', ritual, self._addressOf(event))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickItemKeyFilter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemkeyfilter.html#componentComplete
    """
    #  void QQuickItemKeyFilter::componentComplete()
    ritual = 'ritual_ZN19QQuickItemKeyFilter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickItemKeyFilter17componentCompleteEv'
    self._callAs('QQuickItemKeyFilter', ritual)
