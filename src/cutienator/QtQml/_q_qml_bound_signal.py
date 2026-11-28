"""
QQmlBoundSignal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlBoundSignal to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlNotifierEndpoint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlBoundSignalExpression, QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlBoundSignalExpression = WAIT['QQmlBoundSignalExpression']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBoundSignal(QQmlNotifierEndpoint):
  """
  The cute side of Qt's QQmlBoundSignal: a plain Python object standing in
  front of one C++ QQmlBoundSignal.

  It is built on the cute 'QQmlNotifierEndpoint', as Qt's QQmlBoundSignal is
  built on Qt's QQmlNotifierEndpoint, and has everything that class has.

  C++ hands a QQmlBoundSignal around as a copy, so every C++ QQmlBoundSignal
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlBoundSignal that has a ritual and that Python
  can call so far, 5 names in all: 'removeFromObject', 'expression',
  'takeExpression', 'setEnabled', 'addToObject'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlBoundSignal::~QQmlBoundSignal()': the destructor: Python
    removes its C++ QQmlBoundSignal by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlBoundSignal is created at the first use, not by
    'QQmlBoundSignal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlBoundSignal back gives a copy the ritual made for
    Python, in a new cute QQmlBoundSignal.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBoundSignal'

  #  Qt's '~QQmlBoundSignal()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlBoundSignal behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QQmlBoundSignalD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def expression(self) -> Optional[QQmlBoundSignalExpression]:
    """
    Calls Qt's 'QQmlBoundSignalExpression *QQmlBoundSignal::expression()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlboundsignal.html#expression

    Returns
    -------

    Optional[QQmlBoundSignalExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlBoundSignalExpression *QQmlBoundSignal::expression() const
    address = self.uglySide.call('ritual_ZNK15QQmlBoundSignal10expressionEv')
    from . import QQmlBoundSignalExpression
    return QQmlBoundSignalExpression._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQmlBoundSignal::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlboundsignal.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQmlBoundSignal::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN15QQmlBoundSignal10setEnabledEb', enabled)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject, int, QObject, QQmlEngine)
  @overload(QObject, int, QObject, NoneType)
  @overload(QObject, int, NoneType, QQmlEngine)
  @overload(QObject, int, NoneType, NoneType)
  @overload(NoneType, int, QObject, QQmlEngine)
  @overload(NoneType, int, QObject, NoneType)
  @overload(NoneType, int, NoneType, QQmlEngine)
  @overload(NoneType, int, NoneType, NoneType)
  def __init__(
      self,
      target: Optional[QObject],
      signal: int,
      owner: Optional[QObject],
      engine: Optional[QQmlEngine],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlBoundSignal::QQmlBoundSignal(QObject
    *target, int signal, QObject *owner, QQmlEngine *engine)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignal.html#QQmlBoundSignal

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : int
      Passed on as it is.

    owner : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlBoundSignal::QQmlBoundSignal(QObject *target, int signal, QObject
    #      *owner, QQmlEngine *engine)
    self._noteCreation(QQmlBoundSignal, lambda: Rituals.call(
        'ritual_ZN15QQmlBoundSignalC1EP7QObjectiS1_P10QQmlEngine',
        self._addressOf(target, 'QObject'), signal, self._addressOf(owner,
        'QObject'), self._addressOf(engine),
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

  def removeFromObject(self) -> None:
    """
    Calls Qt's 'void QQmlBoundSignal::removeFromObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignal.html#removeFromObject
    """
    #  void QQmlBoundSignal::removeFromObject()
    self.uglySide.call('ritual_ZN15QQmlBoundSignal16removeFromObjectEv')

  @overload(QQmlBoundSignalExpression)
  @overload(NoneType)
  def takeExpression(self, a0: Optional[QQmlBoundSignalExpression]) -> None:
    """
    Calls Qt's 'void
    QQmlBoundSignal::takeExpression(QQmlBoundSignalExpression *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignal.html#takeExpression

    Parameters
    ----------

    a0 : Optional[QQmlBoundSignalExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlBoundSignal::takeExpression(QQmlBoundSignalExpression *a0)
    self.uglySide.call(
        'ritual_ZN15QQmlBoundSignal14takeExpressionEP25QQmlBoundSignalExpre'
        'ssion',
        self._addressOf(a0),
    )

  @overload(QObject)
  @overload(NoneType)
  def addToObject(self, owner: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlBoundSignal::addToObject(QObject *owner)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlboundsignal.html#addToObject

    Parameters
    ----------

    owner : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlBoundSignal::addToObject(QObject *owner)
    self.uglySide.call(
        'ritual_ZN15QQmlBoundSignal11addToObjectEP7QObject',
        self._addressOf(owner, 'QObject'),
    )
