"""
QQmlJavaScriptExpressionGuard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlJavaScriptExpressionGuard to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQmlNotifierEndpoint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlEngine, QQmlJavaScriptExpression
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngine = WAIT['QQmlEngine']
  QQmlJavaScriptExpression = WAIT['QQmlJavaScriptExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJavaScriptExpressionGuard(QQmlNotifierEndpoint):
  """
  The cute side of Qt's QQmlJavaScriptExpressionGuard: a plain Python object
  standing in front of one C++ QQmlJavaScriptExpressionGuard.

  It is built on the cute 'QQmlNotifierEndpoint', as Qt's
  QQmlJavaScriptExpressionGuard is built on Qt's QQmlNotifierEndpoint, and
  has everything that class has.

  C++ hands a QQmlJavaScriptExpressionGuard around as a copy, so every C++
  QQmlJavaScriptExpressionGuard behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlJavaScriptExpressionGuard that has a ritual and
  that Python can call so far, 2 names in all: 'New', 'Delete'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJavaScriptExpressionGuard::~QQmlJavaScriptExpressionGuard()':
    the destructor: Python removes its C++ QQmlJavaScriptExpressionGuard by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJavaScriptExpressionGuard is created at the first use, not by
    'QQmlJavaScriptExpressionGuard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJavaScriptExpressionGuard back gives a copy the
    ritual made for Python, in a new cute QQmlJavaScriptExpressionGuard.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlJavaScriptExpression, QQmlEngine)
  @overload(QQmlJavaScriptExpression, NoneType)
  @overload(NoneType, QQmlEngine)
  @overload(NoneType, NoneType)
  def New(
      e: Optional[QQmlJavaScriptExpression],
      engine: Optional[QQmlEngine],
  ) -> Optional[QQmlJavaScriptExpressionGuard]:
    """
    Calls Qt's 'QQmlJavaScriptExpressionGuard
    *QQmlJavaScriptExpressionGuard::New(QQmlJavaScriptExpression *e,
    QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpressionguard.html#New

    Parameters
    ----------

    e : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlJavaScriptExpressionGuard]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJavaScriptExpressionGuard
    #      *QQmlJavaScriptExpressionGuard::New(QQmlJavaScriptExpression *e,
    #      QQmlEngine *engine)
    address = Rituals.call(
        'ritual_ZN29QQmlJavaScriptExpressionGuard3NewEP24QQmlJavaScriptExpr'
        'essionP10QQmlEngine',
        CuteMixin._addressOf(e, 'QQmlJavaScriptExpression'),
        CuteMixin._addressOf(engine),
    )
    return QQmlJavaScriptExpressionGuard._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJavaScriptExpressionGuard'

  #  Qt's '~QQmlJavaScriptExpressionGuard()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlJavaScriptExpressionGuard behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QQmlJavaScriptExpressionGuardD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlJavaScriptExpression)
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlJavaScriptExpression]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJavaScriptExpressionGuard::QQmlJavaScriptExpressionGuard(
    QQmlJavaScriptExpression *a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpressionguard.html

    Parameters
    ----------

    a0 : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJavaScriptExpressionGuard::QQmlJavaScriptExpressionGuard(
    #      QQmlJavaScriptExpression *a0)
    self._noteCreation(QQmlJavaScriptExpressionGuard, lambda: Rituals.call(
        'ritual_ZN29QQmlJavaScriptExpressionGuardC1EP24QQmlJavaScriptExpres'
        'sion',
        self._addressOf(a0, 'QQmlJavaScriptExpression'),
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

  def Delete(self) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpressionGuard::Delete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpressionguard.html#Delete
    """
    #  void QQmlJavaScriptExpressionGuard::Delete()
    self.uglySide.call('ritual_ZN29QQmlJavaScriptExpressionGuard6DeleteEv')
