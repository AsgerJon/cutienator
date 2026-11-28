"""
QQmlNotifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlnotifier_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlNotifier to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlData, QQmlNotifierEndpoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlData = WAIT['QQmlData']
  QQmlNotifierEndpoint = WAIT['QQmlNotifierEndpoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlNotifier(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlNotifier: a plain Python object standing in front
  of one C++ QQmlNotifier.

  C++ hands a QQmlNotifier around as a copy, so every C++ QQmlNotifier behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlNotifier that has a ritual and that Python can
  call so far, 2 names in all: 'notify', 'connect'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlNotifier::~QQmlNotifier()': the destructor: Python removes its
    C++ QQmlNotifier by it, and has no other use for it.
  - Qt's 'void QQmlNotifier::emitNotify(QQmlNotifierEndpoint *a0, void **a)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlNotifier is created at the first use, not by
    'QQmlNotifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlNotifier back gives a copy the ritual made for
    Python, in a new cute QQmlNotifier.
  - Each name of Qt's QQmlNotifier that has no cute function yet,
    'emitNotify', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQmlNotifier'

  #  Qt's '~QQmlNotifier()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlNotifier behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QQmlNotifierD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlNotifier::QQmlNotifier()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnotifier.html#QQmlNotifier
    """
    #  QQmlNotifier::QQmlNotifier()
    self._noteCreation(QQmlNotifier, lambda: Rituals.call(
        'ritual_ZN12QQmlNotifierC1Ev',
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

  @overload()
  def notify(self) -> None:
    """
    Calls Qt's 'void QQmlNotifier::notify()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnotifier.html#notify
    """
    #  void QQmlNotifier::notify()
    self.uglySide.call('ritual_ZN12QQmlNotifier6notifyEv')

  @staticmethod
  @overload(QQmlData, int)
  @overload(NoneType, int)
  def notify(ddata: Optional[QQmlData], notifierIndex: int) -> None:
    """
    Calls Qt's 'void QQmlNotifier::notify(QQmlData *ddata, int
    notifierIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnotifier.html#notify

    Parameters
    ----------

    ddata : Optional[QQmlData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    notifierIndex : int
      Passed on as it is.
    """
    #  void QQmlNotifier::notify(QQmlData *ddata, int notifierIndex)
    Rituals.call(
        'ritual_ZN12QQmlNotifier6notifyEP8QQmlDatai',
        CuteMixin._addressOf(ddata), notifierIndex,
    )

  @overload(QQmlNotifierEndpoint)
  @overload(NoneType)
  def connect(self, endpoint: Optional[QQmlNotifierEndpoint]) -> None:
    """
    Calls Qt's 'void QQmlNotifier::connect(QQmlNotifierEndpoint *endpoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnotifier.html#connect

    Parameters
    ----------

    endpoint : Optional[QQmlNotifierEndpoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlNotifier::connect(QQmlNotifierEndpoint *endpoint)
    self.uglySide.call(
        'ritual_ZN12QQmlNotifier7connectEP20QQmlNotifierEndpoint',
        self._addressOf(endpoint, 'QQmlNotifierEndpoint'),
    )

  @staticmethod
  def emitNotify(*__, **_) -> Never:
    """
    Qt's 'void QQmlNotifier::emitNotify(QQmlNotifierEndpoint *a0, void **a)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlNotifier.emitNotify' has no cute function yet. Qt's 'void "
        "QQmlNotifier::emitNotify(QQmlNotifierEndpoint *a0, void **a)': "
        "takes a type Python has no way to hand over yet.")
