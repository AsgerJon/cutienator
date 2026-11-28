"""
QQStyleKitControlState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolstate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitControlState to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQSK, QQStyleKitControlProperties

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitControlState(QQStyleKitControlProperties):
  """
  The cute side of Qt's QQStyleKitControlState: a plain Python object
  standing in front of one C++ QQStyleKitControlState.

  It is built on the cute 'QQStyleKitControlProperties', as Qt's
  QQStyleKitControlState is built on Qt's QQStyleKitControlProperties, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitControlState that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'nestedState',
  'pressedChanged', 'hoveredChanged', 'focusedChanged', 'checkedChanged',
  'disabledChanged', 'highlightedChanged', 'verticalChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitControlState::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQStyleKitControlState::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  15 of the 26 functions Qt declares: 9 leans on 'QQStyleKitControl; 2 not a
  gap; 2 forbidden; 1 leans on 'QQStyleKitControlState; 1 leans on 'vtable
  for QQStyleKitControlState', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitControlState is created at the first use, not by
    'QQStyleKitControlState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitControlState.
  - Qt tells when it has removed the C++ QQStyleKitControlState. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitControlState that has no cute function yet,
    '__init__', 'checked', 'control', 'disabled', 'focused', 'highlighted',
    'hovered', 'lazyCreateState', 'pressed', 'vertical', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitControlState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitControlState::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitControlState::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQStyleKitControlState10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def nestedState(self) -> QQSK.State:
    """
    Calls Qt's 'QQSK::State QQStyleKitControlState::nestedState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#nestedState

    Returns
    -------

    QQSK.State
      The value standing for the combination Qt gave back.
    """
    #  QQSK::State QQStyleKitControlState::nestedState() const
    return QQSK.State(self.uglySide.call(
        'ritual_ZNK22QQStyleKitControlState11nestedStateEv',
    ))

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
    Qt's 'QQStyleKitControlState::QQStyleKitControlState(QObject *parent)':
    leans on 'vtable for QQStyleKitControlState', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.__init__' has no cute function yet. Qt's "
        "'QQStyleKitControlState::QQStyleKitControlState(QObject *parent)': "
        "leans on 'vtable for QQStyleKitControlState', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#pressedChanged
    """
    #  void QQStyleKitControlState::pressedChanged()
    self.uglySide.call('ritual_ZN22QQStyleKitControlState14pressedChangedEv')

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#hoveredChanged
    """
    #  void QQStyleKitControlState::hoveredChanged()
    self.uglySide.call('ritual_ZN22QQStyleKitControlState14hoveredChangedEv')

  def focusedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::focusedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#focusedChanged
    """
    #  void QQStyleKitControlState::focusedChanged()
    self.uglySide.call('ritual_ZN22QQStyleKitControlState14focusedChangedEv')

  def checkedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::checkedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#checkedChanged
    """
    #  void QQStyleKitControlState::checkedChanged()
    self.uglySide.call('ritual_ZN22QQStyleKitControlState14checkedChangedEv')

  def disabledChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::disabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#disabledChanged
    """
    #  void QQStyleKitControlState::disabledChanged()
    self.uglySide.call(
        'ritual_ZN22QQStyleKitControlState15disabledChangedEv',
    )

  def highlightedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::highlightedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#highlightedChanged
    """
    #  void QQStyleKitControlState::highlightedChanged()
    self.uglySide.call(
        'ritual_ZN22QQStyleKitControlState18highlightedChangedEv',
    )

  def verticalChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlState::verticalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolstate.html#verticalChanged
    """
    #  void QQStyleKitControlState::verticalChanged()
    self.uglySide.call(
        'ritual_ZN22QQStyleKitControlState15verticalChangedEv',
    )

  @staticmethod
  def checked(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::checked() const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.checked' has no cute function yet. Qt's "
        "'QQStyleKitControlState *QQStyleKitControlState::checked() const': "
        "leans on 'QQStyleKitControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def control(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControlState::control() const': leans
    on 'QQStyleKitControl::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.control' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControlState::control() const': "
        "leans on 'QQStyleKitControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def disabled(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::disabled() const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.disabled' has no cute function yet. Qt's "
        "'QQStyleKitControlState *QQStyleKitControlState::disabled() "
        "const': leans on 'QQStyleKitControl::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def focused(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::focused() const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.focused' has no cute function yet. Qt's "
        "'QQStyleKitControlState *QQStyleKitControlState::focused() const': "
        "leans on 'QQStyleKitControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def highlighted(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::highlighted()
    const': leans on 'QQStyleKitControl::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.highlighted' has no cute function yet. "
        "Qt's 'QQStyleKitControlState "
        "*QQStyleKitControlState::highlighted() const': leans on "
        "'QQStyleKitControl::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def hovered(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::hovered() const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.hovered' has no cute function yet. Qt's "
        "'QQStyleKitControlState *QQStyleKitControlState::hovered() const': "
        "leans on 'QQStyleKitControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def lazyCreateState(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState
    *QQStyleKitControlState::lazyCreateState(QQSK::StateFlag state) const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.lazyCreateState' has no cute function yet. "
        "Qt's 'QQStyleKitControlState "
        "*QQStyleKitControlState::lazyCreateState(QQSK::StateFlag state) "
        "const': leans on 'QQStyleKitControl::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def pressed(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::pressed() const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.pressed' has no cute function yet. Qt's "
        "'QQStyleKitControlState *QQStyleKitControlState::pressed() const': "
        "leans on 'QQStyleKitControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def vertical(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlState *QQStyleKitControlState::vertical() const':
    leans on 'QQStyleKitControl::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControlState.vertical' has no cute function yet. Qt's "
        "'QQStyleKitControlState *QQStyleKitControlState::vertical() "
        "const': leans on 'QQStyleKitControl::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
