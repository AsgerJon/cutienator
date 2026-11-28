"""
QCanSignalDescriptionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qcansignaldescription_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanSignalDescriptionPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCanSignalDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanSignalDescription = WAIT['QCanSignalDescription']


class QCanSignalDescriptionPrivate(QSharedData):
  """
  The cute side of Qt's QCanSignalDescriptionPrivate: a plain Python object
  standing in front of one C++ QCanSignalDescriptionPrivate.

  It is built on the cute 'QSharedData', as Qt's QCanSignalDescriptionPrivate
  is built on Qt's QSharedData, and has everything that class has.

  C++ hands a QCanSignalDescriptionPrivate around as a copy, so every C++
  QCanSignalDescriptionPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QCanSignalDescriptionPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'isShared', 'get'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCanSignalDescriptionPrivate::muxValueInRange(const QVariant
    &value, const QCanSignalDescription::MultiplexValues &ranges) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanSignalDescriptionPrivate::~QCanSignalDescriptionPrivate()': the
    destructor: Python removes its C++ QCanSignalDescriptionPrivate by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QCanSignalDescriptionPrivate is created at the first use, not by
    'QCanSignalDescriptionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanSignalDescriptionPrivate back gives a copy the
    ritual made for Python, in a new cute QCanSignalDescriptionPrivate.
  - Each name of Qt's QCanSignalDescriptionPrivate that has no cute function
    yet, 'muxValueInRange', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanSignalDescription)
  def get(
      desc: QCanSignalDescription,
  ) -> Optional[QCanSignalDescriptionPrivate]:
    """
    Calls Qt's 'QCanSignalDescriptionPrivate
    *QCanSignalDescriptionPrivate::get(const QCanSignalDescription &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescriptionprivate.html#get

    Parameters
    ----------

    desc : QCanSignalDescription
      Passed on as a value: Qt reads the C++ QCanSignalDescription, which
      stays Python's own.

    Returns
    -------

    Optional[QCanSignalDescriptionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanSignalDescriptionPrivate *QCanSignalDescriptionPrivate::get(const
    #      QCanSignalDescription &desc)
    address = Rituals.call(
        'ritual_ZN28QCanSignalDescriptionPrivate3getERK21QCanSignalDescript'
        'ion',
        CuteMixin._valueOf(desc),
    )
    return QCanSignalDescriptionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanSignalDescriptionPrivate'

  #  Qt's '~QCanSignalDescriptionPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QCanSignalDescriptionPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QCanSignalDescriptionPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isShared(self) -> bool:
    """
    Calls Qt's 'bool QCanSignalDescriptionPrivate::isShared() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescriptionprivate.html#isShared
    """
    #  bool QCanSignalDescriptionPrivate::isShared() const
    return self.uglySide.call(
        'ritual_ZNK28QCanSignalDescriptionPrivate8isSharedEv',
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
  def muxValueInRange(*__, **_) -> Never:
    """
    Qt's 'bool QCanSignalDescriptionPrivate::muxValueInRange(const QVariant
    &value, const QCanSignalDescription::MultiplexValues &ranges) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanSignalDescriptionPrivate.muxValueInRange' has no cute "
        "function yet. Qt's 'bool "
        "QCanSignalDescriptionPrivate::muxValueInRange(const QVariant "
        "&value, const QCanSignalDescription::MultiplexValues &ranges) "
        "const': takes a type Python has no way to hand over yet.")
