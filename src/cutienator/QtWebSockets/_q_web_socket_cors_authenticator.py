"""
QWebSocketCorsAuthenticator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/qwebsocketcorsauthenticator.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QWebSocketCorsAuthenticatorPrivate


class QWebSocketCorsAuthenticator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebSocketCorsAuthenticator: a plain Python object
  standing in front of one C++ QWebSocketCorsAuthenticator.

  C++ hands a QWebSocketCorsAuthenticator around as a copy, so every C++
  QWebSocketCorsAuthenticator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebSocketCorsAuthenticator that has a ritual and
  that Python can call so far, 4 names in all: 'd_func', 'origin',
  'setAllowed', 'allowed'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWebSocketCorsAuthenticatorPrivate
    *QWebSocketCorsAuthenticator::d_func() const': takes in Python what
    'QWebSocketCorsAuthenticatorPrivate
    *QWebSocketCorsAuthenticator::d_func()' takes.
  - Qt's 'QWebSocketCorsAuthenticator::~QWebSocketCorsAuthenticator()': the
    destructor: Python removes its C++ QWebSocketCorsAuthenticator by it, and
    has no other use for it.
  - Qt's 'QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(
    QWebSocketCorsAuthenticator &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QWebSocketCorsAuthenticator
    &QWebSocketCorsAuthenticator::operator=(QWebSocketCorsAuthenticator
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QWebSocketCorsAuthenticator::swap(QWebSocketCorsAuthenticator
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebSocketCorsAuthenticator
    &QWebSocketCorsAuthenticator::operator=(const QWebSocketCorsAuthenticator
    &other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QWebSocketCorsAuthenticator is created at the first use, not by
    'QWebSocketCorsAuthenticator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebSocketCorsAuthenticator back gives a copy the
    ritual made for Python, in a new cute QWebSocketCorsAuthenticator.
  - Each name of Qt's QWebSocketCorsAuthenticator that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QWebSocketCorsAuthenticator'

  #  Qt's '~QWebSocketCorsAuthenticator()'. Naming it makes this a value
  #  class: Python owns every C++ QWebSocketCorsAuthenticator behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QWebSocketCorsAuthenticatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def origin(self) -> str:
    """
    Calls Qt's 'QString QWebSocketCorsAuthenticator::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketcorsauthenticator.html#origin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketCorsAuthenticator::origin() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketCorsAuthenticator6originEv',
    )

  def allowed(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketCorsAuthenticator::allowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketcorsauthenticator.html#allowed
    """
    #  bool QWebSocketCorsAuthenticator::allowed() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketCorsAuthenticator7allowedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAllowed(self, allowed: bool) -> None:
    """
    Calls Qt's 'void QWebSocketCorsAuthenticator::setAllowed(bool allowed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketcorsauthenticator.html#setAllowed

    Parameters
    ----------

    allowed : bool
      Passed on as it is.
    """
    #  void QWebSocketCorsAuthenticator::setAllowed(bool allowed)
    self.uglySide.call(
        'ritual_ZN27QWebSocketCorsAuthenticator10setAllowedEb', allowed,
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

  @overload(str)
  def __init__(self, origin: str) -> None:
    """
    Notes what was given, for Qt's
    'QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(const QString
    &origin)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketcorsauthenticator.html

    Parameters
    ----------

    origin : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(const QString
    #      &origin)
    self._noteCreation(QWebSocketCorsAuthenticator, lambda: Rituals.call(
        'ritual_ZN27QWebSocketCorsAuthenticatorC1ERK7QString', origin,
    ))

  @overload(THIS)
  def __init__(self, other: QWebSocketCorsAuthenticator) -> None:
    """
    Notes what was given, for Qt's
    'QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(const
    QWebSocketCorsAuthenticator &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketcorsauthenticator.html

    Parameters
    ----------

    other : QWebSocketCorsAuthenticator
      Passed on as a value: Qt reads the C++ QWebSocketCorsAuthenticator,
      which stays Python's own.
    """
    #  QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(const
    #      QWebSocketCorsAuthenticator &other)
    self._noteCreation(QWebSocketCorsAuthenticator, lambda: Rituals.call(
        'ritual_ZN27QWebSocketCorsAuthenticatorC1ERKS_',
        self._valueOf(other),
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

  def d_func(self) -> Optional[QWebSocketCorsAuthenticatorPrivate]:
    """
    Calls Qt's 'QWebSocketCorsAuthenticatorPrivate
    *QWebSocketCorsAuthenticator::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketcorsauthenticator.html#d_func

    Returns
    -------

    Optional[QWebSocketCorsAuthenticatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocketCorsAuthenticatorPrivate
    #      *QWebSocketCorsAuthenticator::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QWebSocketCorsAuthenticator6d_funcEv',
    )
    from . import QWebSocketCorsAuthenticatorPrivate
    return QWebSocketCorsAuthenticatorPrivate._cuteAt(address)

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketCorsAuthenticator::swap(QWebSocketCorsAuthenticator
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebSocketCorsAuthenticator.swap' has no cute function yet. Qt's "
        "'void "
        "QWebSocketCorsAuthenticator::swap(QWebSocketCorsAuthenticator "
        "&other)': takes a type Python has no way to hand over yet.")
