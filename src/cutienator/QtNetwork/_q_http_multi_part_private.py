"""
QHttpMultiPartPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QHttpMultiPartPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QHttpMultiPart
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttpMultiPart = WAIT['QHttpMultiPart']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpMultiPartPrivate(QObjectPrivate):
  """
  The cute side of Qt's QHttpMultiPartPrivate: a plain Python object standing
  in front of one C++ QHttpMultiPartPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QHttpMultiPartPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpMultiPartPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'get'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpMultiPartPrivate::~QHttpMultiPartPrivate()': the destructor:
    Python never removes a C++ QHttpMultiPartPrivate.
  - Qt's 'const QHttpMultiPartPrivate *QHttpMultiPartPrivate::get(const
    QHttpMultiPart *message)': takes in Python what 'QHttpMultiPartPrivate
    *QHttpMultiPartPrivate::get(QHttpMultiPart *message)' takes.

  What to expect
  --------------

  - The C++ QHttpMultiPartPrivate is created at the first use, not by
    'QHttpMultiPartPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpMultiPartPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QHttpMultiPart)
  @overload(NoneType)
  def get(
      message: Optional[QHttpMultiPart],
  ) -> Optional[QHttpMultiPartPrivate]:
    """
    Calls Qt's 'QHttpMultiPartPrivate
    *QHttpMultiPartPrivate::get(QHttpMultiPart *message)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipartprivate.html#get

    Parameters
    ----------

    message : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QHttpMultiPartPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpMultiPartPrivate *QHttpMultiPartPrivate::get(QHttpMultiPart
    #      *message)
    address = Rituals.call(
        'ritual_ZN21QHttpMultiPartPrivate3getEP14QHttpMultiPart',
        CuteMixin._addressOf(message),
    )
    return QHttpMultiPartPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpMultiPartPrivate'

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
    Notes what was given, for Qt's
    'QHttpMultiPartPrivate::QHttpMultiPartPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpmultipartprivate.html#QHttpMultiPartPrivate
    """
    #  QHttpMultiPartPrivate::QHttpMultiPartPrivate()
    self._noteCreation(QHttpMultiPartPrivate, lambda: Rituals.call(
        'ritual_ZN21QHttpMultiPartPrivateC1Ev',
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
