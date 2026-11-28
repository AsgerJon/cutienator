"""
QWaylandInputMethodControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandinputmethodcontrol.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWaylandInputMethodControlPrivate


class QWaylandInputMethodControl(QObject):
  """
  The cute side of Qt's QWaylandInputMethodControl: a plain Python object
  standing in front of one C++ QWaylandInputMethodControl.

  It is built on the cute 'QObject', as Qt's QWaylandInputMethodControl is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandInputMethodControl that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'd_func',
  'enabled', 'enabledChanged', 'updateInputMethod'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandInputMethodControl::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWaylandInputMethodControl::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandInputMethodControlPrivate
    *QWaylandInputMethodControl::d_func() const': takes in Python what
    'QWaylandInputMethodControlPrivate *QWaylandInputMethodControl::d_func()'
    takes.

  What has no ritual
  ------------------

  14 of the 22 functions Qt declares: 5 leans on 'QWaylandInputMethodControl;
  5 leans on 'QWaylandTextInput; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWaylandInputMethodControl is created at the first use, not by
    'QWaylandInputMethodControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandInputMethodControl.
  - Qt tells when it has removed the C++ QWaylandInputMethodControl. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandInputMethodControl that has no cute function
    yet, '__init__', 'defaultSeatChanged', 'inputMethodEvent',
    'inputMethodQuery', 'setEnabled', 'setSurface', 'surfaceDisabled',
    'surfaceEnabled', 'updateTextInput', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandInputMethodControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandInputMethodControl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandInputMethodControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QWaylandInputMethodControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QWaylandInputMethodControl::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrol.html#enabled
    """
    #  bool QWaylandInputMethodControl::enabled() const
    return self.uglySide.call(
        'ritual_ZNK26QWaylandInputMethodControl7enabledEv',
    )

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
    Qt's
    'QWaylandInputMethodControl::QWaylandInputMethodControl(QWaylandSurface
    *surface)': leans on
    'QWaylandTextInput::surfaceEnabled(QWaylandSurface*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.__init__' has no cute function yet. "
        "Qt's "
        "'QWaylandInputMethodControl::QWaylandInputMethodControl(QWaylandSur"
        "face *surface)': leans on "
        "'QWaylandTextInput::surfaceEnabled(QWaylandSurface*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def d_func(self) -> Optional[QWaylandInputMethodControlPrivate]:
    """
    Calls Qt's 'QWaylandInputMethodControlPrivate
    *QWaylandInputMethodControl::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrol.html#d_func

    Returns
    -------

    Optional[QWaylandInputMethodControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandInputMethodControlPrivate
    #      *QWaylandInputMethodControl::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QWaylandInputMethodControl6d_funcEv',
    )
    from . import QWaylandInputMethodControlPrivate
    return QWaylandInputMethodControlPrivate._cuteAt(address)

  @overload(bool)
  def enabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWaylandInputMethodControl::enabledChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrol.html#enabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWaylandInputMethodControl::enabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN26QWaylandInputMethodControl14enabledChangedEb', enabled,
    )

  @overload(Qt.InputMethodQueries)
  def updateInputMethod(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void
    QWaylandInputMethodControl::updateInputMethod(Qt::InputMethodQueries
    queries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrol.html#updateInputMethod

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QWaylandInputMethodControl::updateInputMethod(Qt::
    #      InputMethodQueries queries)
    self.uglySide.call(
        'ritual_ZN26QWaylandInputMethodControl17updateInputMethodE6QFlagsIN'
        '2Qt16InputMethodQueryEE',
        queries.value,
    )

  @staticmethod
  def defaultSeatChanged(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::defaultSeatChanged()': leans on
    'QWaylandTextInput::surfaceEnabled(QWaylandSurface*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.defaultSeatChanged' has no cute "
        "function yet. Qt's 'void "
        "QWaylandInputMethodControl::defaultSeatChanged()': leans on "
        "'QWaylandTextInput::surfaceEnabled(QWaylandSurface*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def inputMethodEvent(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::inputMethodEvent(QInputMethodEvent
    *event)': leans on
    'QWaylandTextInput::sendInputMethodEvent(QInputMethodEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.inputMethodEvent' has no cute function "
        "yet. Qt's 'void "
        "QWaylandInputMethodControl::inputMethodEvent(QInputMethodEvent "
        "*event)': leans on "
        "'QWaylandTextInput::sendInputMethodEvent(QInputMethodEvent*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def inputMethodQuery(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QWaylandInputMethodControl::inputMethodQuery(Qt::InputMethodQuery query,
    QVariant argument) const': leans on
    'QWaylandTextInput::inputMethodQuery(Qt::InputMethodQuery, QVariant)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.inputMethodQuery' has no cute function "
        "yet. Qt's 'QVariant "
        "QWaylandInputMethodControl::inputMethodQuery(Qt::InputMethodQuery "
        "query, QVariant argument) const': leans on "
        "'QWaylandTextInput::inputMethodQuery(Qt::InputMethodQuery, "
        "QVariant) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def setEnabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::setEnabled(bool enabled)': leans
    on 'QWaylandInputMethodControl::enabledChanged(bool)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.setEnabled' has no cute function yet. "
        "Qt's 'void QWaylandInputMethodControl::setEnabled(bool enabled)': "
        "leans on 'QWaylandInputMethodControl::enabledChanged(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setSurface(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::setSurface(QWaylandSurface
    *surface)': leans on 'QWaylandInputMethodControl::enabledChanged(bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.setSurface' has no cute function yet. "
        "Qt's 'void QWaylandInputMethodControl::setSurface(QWaylandSurface "
        "*surface)': leans on "
        "'QWaylandInputMethodControl::enabledChanged(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def surfaceDisabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::surfaceDisabled(QWaylandSurface
    *surface)': leans on 'QWaylandInputMethodControl::enabledChanged(bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.surfaceDisabled' has no cute function "
        "yet. Qt's 'void "
        "QWaylandInputMethodControl::surfaceDisabled(QWaylandSurface "
        "*surface)': leans on "
        "'QWaylandInputMethodControl::enabledChanged(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def surfaceEnabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::surfaceEnabled(QWaylandSurface
    *surface)': leans on 'QWaylandInputMethodControl::enabledChanged(bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.surfaceEnabled' has no cute function "
        "yet. Qt's 'void "
        "QWaylandInputMethodControl::surfaceEnabled(QWaylandSurface "
        "*surface)': leans on "
        "'QWaylandInputMethodControl::enabledChanged(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateTextInput(*__, **_) -> Never:
    """
    Qt's 'void QWaylandInputMethodControl::updateTextInput()': leans on
    'QWaylandTextInput::surfaceEnabled(QWaylandSurface*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWaylandInputMethodControl.updateTextInput' has no cute function "
        "yet. Qt's 'void QWaylandInputMethodControl::updateTextInput()': "
        "leans on 'QWaylandTextInput::surfaceEnabled(QWaylandSurface*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
