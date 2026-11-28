"""
QWebSocketHandshakeOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/qwebsockethandshakeoptions.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWebSocketHandshakeOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebSocketHandshakeOptions: a plain Python object
  standing in front of one C++ QWebSocketHandshakeOptions.

  C++ hands a QWebSocketHandshakeOptions around as a copy, so every C++
  QWebSocketHandshakeOptions behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebSocketHandshakeOptions that has a ritual and
  that Python can call so far, 5 names in all: 'subprotocols',
  'setSubprotocols', 'equals', '__eq__', '__ne__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebSocketHandshakeOptions::QWebSocketHandshakeOptions(
    QWebSocketHandshakeOptions &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QWebSocketHandshakeOptions::~QWebSocketHandshakeOptions()': the
    destructor: Python removes its C++ QWebSocketHandshakeOptions by it, and
    has no other use for it.
  - Qt's 'QWebSocketHandshakeOptions
    &QWebSocketHandshakeOptions::operator=(QWebSocketHandshakeOptions
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebSocketHandshakeOptions
    &QWebSocketHandshakeOptions::operator=(const QWebSocketHandshakeOptions
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QWebSocketHandshakeOptions::swap(QWebSocketHandshakeOptions
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QWebSocketHandshakeOptions is created at the first use, not by
    'QWebSocketHandshakeOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebSocketHandshakeOptions back gives a copy the
    ritual made for Python, in a new cute QWebSocketHandshakeOptions.
  - Each name of Qt's QWebSocketHandshakeOptions that has no cute function
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
  __qt_class__ = 'QWebSocketHandshakeOptions'

  #  Qt's '~QWebSocketHandshakeOptions()'. Naming it makes this a value
  #  class: Python owns every C++ QWebSocketHandshakeOptions behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QWebSocketHandshakeOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def subprotocols(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebSocketHandshakeOptions::subprotocols()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html#subprotocols

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebSocketHandshakeOptions::subprotocols() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeOptions12subprotocolsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(THIS)
  def equals(self, other: QWebSocketHandshakeOptions) -> bool:
    """
    Calls Qt's 'bool QWebSocketHandshakeOptions::equals(const
    QWebSocketHandshakeOptions &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html#equals

    Parameters
    ----------

    other : QWebSocketHandshakeOptions
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own.
    """
    #  bool QWebSocketHandshakeOptions::equals(const
    #      QWebSocketHandshakeOptions &other) const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeOptions6equalsERKS_',
        self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setSubprotocols(self, protocols: QStringList) -> None:
    """
    Calls Qt's 'void QWebSocketHandshakeOptions::setSubprotocols(const
    QStringList &protocols)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html#setSubprotocols

    Parameters
    ----------

    protocols : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocketHandshakeOptions::setSubprotocols(const QStringList
    #      &protocols)
    self.uglySide.call(
        'ritual_ZN26QWebSocketHandshakeOptions15setSubprotocolsERK5QListI7Q'
        'StringE',
        self._valueOf(protocols),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QWebSocketHandshakeOptions) -> bool:
    """
    Calls Qt's 'bool operator==(const QWebSocketHandshakeOptions &lhs, const
    QWebSocketHandshakeOptions &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html#operator==

    Parameters
    ----------

    rhs : QWebSocketHandshakeOptions
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own.
    """
    #  bool operator==(const QWebSocketHandshakeOptions &lhs, const
    #      QWebSocketHandshakeOptions &rhs)
    return Rituals.call(
        'ritual_ZeqRK26QWebSocketHandshakeOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QWebSocketHandshakeOptions) -> bool:
    """
    Calls Qt's 'bool operator!=(const QWebSocketHandshakeOptions &lhs, const
    QWebSocketHandshakeOptions &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html#operator!=

    Parameters
    ----------

    rhs : QWebSocketHandshakeOptions
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own.
    """
    #  bool operator!=(const QWebSocketHandshakeOptions &lhs, const
    #      QWebSocketHandshakeOptions &rhs)
    return Rituals.call(
        'ritual_ZneRK26QWebSocketHandshakeOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWebSocketHandshakeOptions::QWebSocketHandshakeOptions()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html
    """
    #  QWebSocketHandshakeOptions::QWebSocketHandshakeOptions()
    self._noteCreation(QWebSocketHandshakeOptions, lambda: Rituals.call(
        'ritual_ZN26QWebSocketHandshakeOptionsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebSocketHandshakeOptions) -> None:
    """
    Notes what was given, for Qt's
    'QWebSocketHandshakeOptions::QWebSocketHandshakeOptions(const
    QWebSocketHandshakeOptions &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeoptions.html

    Parameters
    ----------

    other : QWebSocketHandshakeOptions
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own.
    """
    #  QWebSocketHandshakeOptions::QWebSocketHandshakeOptions(const
    #      QWebSocketHandshakeOptions &other)
    self._noteCreation(QWebSocketHandshakeOptions, lambda: Rituals.call(
        'ritual_ZN26QWebSocketHandshakeOptionsC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketHandshakeOptions::swap(QWebSocketHandshakeOptions
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebSocketHandshakeOptions.swap' has no cute function yet. Qt's "
        "'void QWebSocketHandshakeOptions::swap(QWebSocketHandshakeOptions "
        "&other)': takes a type Python has no way to hand over yet.")
