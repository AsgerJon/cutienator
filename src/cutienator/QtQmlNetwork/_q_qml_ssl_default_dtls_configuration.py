"""
QQmlSslDefaultDtlsConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSslDefaultDtlsConfiguration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQmlSslConfiguration


class QQmlSslDefaultDtlsConfiguration(QQmlSslConfiguration):
  """
  The cute side of Qt's QQmlSslDefaultDtlsConfiguration: a plain Python
  object standing in front of one C++ QQmlSslDefaultDtlsConfiguration.

  It is built on the cute 'QQmlSslConfiguration', as Qt's
  QQmlSslDefaultDtlsConfiguration is built on Qt's QQmlSslConfiguration, and
  has everything that class has.

  C++ hands a QQmlSslDefaultDtlsConfiguration around as a copy, so every C++
  QQmlSslDefaultDtlsConfiguration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQmlSslDefaultDtlsConfiguration yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQmlSslDefaultDtlsConfiguration::~QQmlSslDefaultDtlsConfiguration()':
    the destructor: Python removes its C++ QQmlSslDefaultDtlsConfiguration by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 5 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlSslDefaultDtlsConfiguration is created at the first use, not
    by 'QQmlSslDefaultDtlsConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSslDefaultDtlsConfiguration back gives a copy the
    ritual made for Python, in a new cute QQmlSslDefaultDtlsConfiguration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSslDefaultDtlsConfiguration'

  #  Qt's '~QQmlSslDefaultDtlsConfiguration()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlSslDefaultDtlsConfiguration behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QQmlSslDefaultDtlsConfigurationD1Ev'

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
    'QQmlSslDefaultDtlsConfiguration::QQmlSslDefaultDtlsConfiguration()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlssldefaultdtlsconfiguration.html
    """
    #  QQmlSslDefaultDtlsConfiguration::QQmlSslDefaultDtlsConfiguration()
    self._noteCreation(QQmlSslDefaultDtlsConfiguration, lambda: Rituals.call(
        'ritual_ZN31QQmlSslDefaultDtlsConfigurationC1Ev',
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
