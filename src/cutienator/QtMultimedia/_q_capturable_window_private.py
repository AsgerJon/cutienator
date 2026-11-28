"""
QCapturableWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qcapturablewindow_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCapturableWindowPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCapturableWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCapturableWindow = WAIT['QCapturableWindow']


class QCapturableWindowPrivate(QSharedData):
  """
  The cute side of Qt's QCapturableWindowPrivate: a plain Python object
  standing in front of one C++ QCapturableWindowPrivate.

  It is built on the cute 'QSharedData', as Qt's QCapturableWindowPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QCapturableWindowPrivate around as a copy, so every C++
  QCapturableWindowPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCapturableWindowPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'handle'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCapturableWindowPrivate::QCapturableWindowPrivate(Id id, QString
    &&description)': takes a type Python has no way to hand over yet.
  - Qt's 'QCapturableWindow QCapturableWindowPrivate::create(Id id, QString
    &&description)': takes a type Python has no way to hand over yet.
  - Qt's 'QCapturableWindowPrivate::~QCapturableWindowPrivate()': the
    destructor: Python removes its C++ QCapturableWindowPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QCapturableWindowPrivate is created at the first use, not by
    'QCapturableWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCapturableWindowPrivate back gives a copy the ritual
    made for Python, in a new cute QCapturableWindowPrivate.
  - Each name of Qt's QCapturableWindowPrivate that has no cute function yet,
    '__init__', 'create', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCapturableWindow)
  def handle(
      window: QCapturableWindow,
  ) -> Optional[QCapturableWindowPrivate]:
    """
    Calls Qt's 'const QCapturableWindowPrivate
    *QCapturableWindowPrivate::handle(const QCapturableWindow &window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcapturablewindowprivate.html#handle

    Parameters
    ----------

    window : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.

    Returns
    -------

    Optional[QCapturableWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCapturableWindowPrivate *QCapturableWindowPrivate::handle(const
    #      QCapturableWindow &window)
    address = Rituals.call(
        'ritual_ZN24QCapturableWindowPrivate6handleERK17QCapturableWindow',
        CuteMixin._valueOf(window),
    )
    return QCapturableWindowPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCapturableWindowPrivate'

  #  Qt's '~QCapturableWindowPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCapturableWindowPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QCapturableWindowPrivateD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QCapturableWindowPrivate::QCapturableWindowPrivate(Id id, QString
    &&description)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCapturableWindowPrivate.__init__' has no cute function yet. Qt's "
        "'QCapturableWindowPrivate::QCapturableWindowPrivate(Id id, QString "
        "&&description)': takes a type Python has no way to hand over yet.")

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
  def create(*__, **_) -> Never:
    """
    Qt's 'QCapturableWindow QCapturableWindowPrivate::create(Id id, QString
    &&description)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCapturableWindowPrivate.create' has no cute function yet. Qt's "
        "'QCapturableWindow QCapturableWindowPrivate::create(Id id, QString "
        "&&description)': takes a type Python has no way to hand over yet.")
