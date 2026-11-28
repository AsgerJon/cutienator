"""
QSslDiffieHellmanParametersPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qssldiffiehellmanparameters_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSslDiffieHellmanParametersPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSslDiffieHellmanParametersPrivate(QSharedData):
  """
  The cute side of Qt's QSslDiffieHellmanParametersPrivate: a plain Python
  object standing in front of one C++ QSslDiffieHellmanParametersPrivate.

  It is built on the cute 'QSharedData', as Qt's
  QSslDiffieHellmanParametersPrivate is built on Qt's QSharedData, and has
  everything that class has.

  C++ hands a QSslDiffieHellmanParametersPrivate around as a copy, so every
  C++ QSslDiffieHellmanParametersPrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QSslDiffieHellmanParametersPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'initFromDer',
  'initFromPem'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSslDiffieHellmanParametersPrivate::~QSslDiffieHellmanParametersPrivate(
    )': the destructor: Python removes its C++
    QSslDiffieHellmanParametersPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSslDiffieHellmanParametersPrivate is created at the first use,
    not by 'QSslDiffieHellmanParametersPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslDiffieHellmanParametersPrivate back gives a copy
    the ritual made for Python, in a new cute
    QSslDiffieHellmanParametersPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslDiffieHellmanParametersPrivate'

  #  Qt's '~QSslDiffieHellmanParametersPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QSslDiffieHellmanParametersPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN34QSslDiffieHellmanParametersPrivateD1Ev'

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

  @overload(QByteArray)
  def initFromDer(self, der: QByteArray) -> None:
    """
    Calls Qt's 'void QSslDiffieHellmanParametersPrivate::initFromDer(const
    QByteArray &der)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparametersprivate.html

    Parameters
    ----------

    der : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSslDiffieHellmanParametersPrivate::initFromDer(const QByteArray
    #      &der)
    self.uglySide.call(
        'ritual_ZN34QSslDiffieHellmanParametersPrivate11initFromDerERK10QBy'
        'teArray',
        self._valueOf(der),
    )

  @overload(QByteArray)
  def initFromPem(self, pem: QByteArray) -> None:
    """
    Calls Qt's 'void QSslDiffieHellmanParametersPrivate::initFromPem(const
    QByteArray &pem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparametersprivate.html

    Parameters
    ----------

    pem : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSslDiffieHellmanParametersPrivate::initFromPem(const QByteArray
    #      &pem)
    self.uglySide.call(
        'ritual_ZN34QSslDiffieHellmanParametersPrivate11initFromPemERK10QBy'
        'teArray',
        self._valueOf(pem),
    )
