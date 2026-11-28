"""
QHttp2ConfigurationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttp2configuration_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttp2ConfigurationPrivate to be private: it declares the class
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
  from typing import Optional

  from . import QHttp2Configuration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttp2Configuration = WAIT['QHttp2Configuration']


class QHttp2ConfigurationPrivate(QSharedData):
  """
  The cute side of Qt's QHttp2ConfigurationPrivate: a plain Python object
  standing in front of one C++ QHttp2ConfigurationPrivate.

  It is built on the cute 'QSharedData', as Qt's QHttp2ConfigurationPrivate
  is built on Qt's QSharedData, and has everything that class has.

  C++ hands a QHttp2ConfigurationPrivate around as a copy, so every C++
  QHttp2ConfigurationPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QHttp2ConfigurationPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'get'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttp2ConfigurationPrivate
    *QHttp2ConfigurationPrivate::get(QHttp2Configuration &config)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QHttp2ConfigurationPrivate::~QHttp2ConfigurationPrivate()': the
    destructor: Python removes its C++ QHttp2ConfigurationPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QHttp2ConfigurationPrivate is created at the first use, not by
    'QHttp2ConfigurationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttp2ConfigurationPrivate back gives a copy the
    ritual made for Python, in a new cute QHttp2ConfigurationPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QHttp2Configuration)
  def get(
      config: QHttp2Configuration,
  ) -> Optional[QHttp2ConfigurationPrivate]:
    """
    Calls Qt's 'const QHttp2ConfigurationPrivate
    *QHttp2ConfigurationPrivate::get(const QHttp2Configuration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configurationprivate.html#get

    Parameters
    ----------

    config : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.

    Returns
    -------

    Optional[QHttp2ConfigurationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QHttp2ConfigurationPrivate
    #      *QHttp2ConfigurationPrivate::get(const QHttp2Configuration
    #      &config)
    address = Rituals.call(
        'ritual_ZN26QHttp2ConfigurationPrivate3getERK19QHttp2Configuration',
        CuteMixin._valueOf(config),
    )
    return QHttp2ConfigurationPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttp2ConfigurationPrivate'

  #  Qt's '~QHttp2ConfigurationPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QHttp2ConfigurationPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QHttp2ConfigurationPrivateD1Ev'

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
