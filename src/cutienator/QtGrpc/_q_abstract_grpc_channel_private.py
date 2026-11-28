"""
QAbstractGrpcChannelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/6.12.0/QtGrpc/private/qabstractgrpcchannel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractGrpcChannelPrivate to be private: it declares the class
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

  from . import QAbstractGrpcChannel, QGrpcChannelOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractGrpcChannel = WAIT['QAbstractGrpcChannel']
  QGrpcChannelOptions = WAIT['QGrpcChannelOptions']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractGrpcChannelPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractGrpcChannelPrivate: a plain Python object
  standing in front of one C++ QAbstractGrpcChannelPrivate.

  What exists
  -----------

  Every function of Qt's QAbstractGrpcChannelPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'get'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractGrpcChannelPrivate
    *QAbstractGrpcChannelPrivate::get(QAbstractGrpcChannel *ch)': takes in
    Python what 'const QAbstractGrpcChannelPrivate
    *QAbstractGrpcChannelPrivate::get(const QAbstractGrpcChannel *ch)' takes.

  What to expect
  --------------

  - The C++ QAbstractGrpcChannelPrivate is created at the first use, not by
    'QAbstractGrpcChannelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractGrpcChannelPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAbstractGrpcChannel)
  @overload(NoneType)
  def get(
      ch: Optional[QAbstractGrpcChannel],
  ) -> Optional[QAbstractGrpcChannelPrivate]:
    """
    Calls Qt's 'const QAbstractGrpcChannelPrivate
    *QAbstractGrpcChannelPrivate::get(const QAbstractGrpcChannel *ch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgrpcchannelprivate.html#get

    Parameters
    ----------

    ch : Optional[QAbstractGrpcChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractGrpcChannelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractGrpcChannelPrivate
    #      *QAbstractGrpcChannelPrivate::get(const QAbstractGrpcChannel *ch)
    address = Rituals.call(
        'ritual_ZN27QAbstractGrpcChannelPrivate3getEPK20QAbstractGrpcChanne'
        'l',
        CuteMixin._addressOf(ch),
    )
    return QAbstractGrpcChannelPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractGrpcChannelPrivate'

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

  @overload(QGrpcChannelOptions, QAbstractGrpcChannel)
  @overload(QGrpcChannelOptions, NoneType)
  def __init__(
      self,
      options: QGrpcChannelOptions,
      parent: Optional[QAbstractGrpcChannel],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractGrpcChannelPrivate::QAbstractGrpcChannelPrivate(const
    QGrpcChannelOptions &options, QAbstractGrpcChannel *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgrpcchannelprivate.html

    Parameters
    ----------

    options : QGrpcChannelOptions
      Passed on as a value: Qt reads the C++ QGrpcChannelOptions, which stays
      Python's own.

    parent : Optional[QAbstractGrpcChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractGrpcChannelPrivate::QAbstractGrpcChannelPrivate(const
    #      QGrpcChannelOptions &options, QAbstractGrpcChannel *parent)
    self._noteCreation(QAbstractGrpcChannelPrivate, lambda: Rituals.call(
        'ritual_ZN27QAbstractGrpcChannelPrivateC1ERK19QGrpcChannelOptionsP2'
        '0QAbstractGrpcChannel',
        self._valueOf(options), self._addressOf(parent),
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
