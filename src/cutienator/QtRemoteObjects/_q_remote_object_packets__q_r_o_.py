"""
QRemoteObjectPackets::QRO_ binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectPackets::QRO_ to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QRemoteObjectSourceBase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectSourceBase = WAIT['QRemoteObjectSourceBase']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRO_(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRemoteObjectPackets::QRO_: a plain Python object
  standing in front of one C++ QRemoteObjectPackets::QRO_.

  C++ hands a QRemoteObjectPackets::QRO_ around as a copy, so every C++
  QRemoteObjectPackets::QRO_ behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QRemoteObjectPackets::QRO_ yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectPackets::QRO_::~QRO_()': the destructor: Python
    removes its C++ QRemoteObjectPackets::QRO_ by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRemoteObjectPackets::QRO_ is created at the first use, not by
    'QRemoteObjectPackets::QRO_(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRemoteObjectPackets::QRO_ back gives a copy the
    ritual made for Python, in a new cute QRemoteObjectPackets::QRO_.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectPackets::QRO_'

  #  Qt's '~QRemoteObjectPackets::QRO_()'. Naming it makes this a value
  #  class: Python owns every C++ QRemoteObjectPackets::QRO_ behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QRemoteObjectPackets4QRO_D1Ev'

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
    Notes what was given, for Qt's 'QRemoteObjectPackets::QRO_::QRO_()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qro_.html#QRO_
    """
    #  QRemoteObjectPackets::QRO_::QRO_()
    self._noteCreation(QRO_, lambda: Rituals.call(
        'ritual_ZN20QRemoteObjectPackets4QRO_C1Ev',
    ))

  @overload(QRemoteObjectSourceBase)
  @overload(NoneType)
  def __init__(self, source: Optional[QRemoteObjectSourceBase]) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectPackets::QRO_::QRO_(QRemoteObjectSourceBase *source)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qro_.html#QRO_

    Parameters
    ----------

    source : Optional[QRemoteObjectSourceBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRemoteObjectPackets::QRO_::QRO_(QRemoteObjectSourceBase *source)
    self._noteCreation(QRO_, lambda: Rituals.call(
        'ritual_ZN20QRemoteObjectPackets4QRO_C1EP23QRemoteObjectSourceBase',
        self._addressOf(source),
    ))

  @overload(QVariant)
  def __init__(self, value: QVariant) -> None:
    """
    Notes what was given, for Qt's 'QRemoteObjectPackets::QRO_::QRO_(const
    QVariant &value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpackets-qro_.html#QRO_

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QRemoteObjectPackets::QRO_::QRO_(const QVariant &value)
    self._noteCreation(QRO_, lambda: Rituals.call(
        'ritual_ZN20QRemoteObjectPackets4QRO_C1ERK8QVariant',
        self._valueOf(value),
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
