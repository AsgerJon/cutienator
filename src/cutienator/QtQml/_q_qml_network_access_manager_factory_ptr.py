"""
QQmlNetworkAccessManagerFactoryPtr binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlNetworkAccessManagerFactoryPtr to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlNetworkAccessManagerFactory, QQmlTypeLoaderLockedData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlNetworkAccessManagerFactory = WAIT['QQmlNetworkAccessManagerFactory']
  QQmlTypeLoaderLockedData = WAIT['QQmlTypeLoaderLockedData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlNetworkAccessManagerFactoryPtr(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlNetworkAccessManagerFactoryPtr: a plain Python
  object standing in front of one C++ QQmlNetworkAccessManagerFactoryPtr.

  What exists
  -----------

  Every function of Qt's QQmlNetworkAccessManagerFactoryPtr that has a ritual
  and that Python can call so far, 1 name in all: 'reset'. It can be made
  from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlNetworkAccessManagerFactoryPtr is created at the first use,
    not by 'QQmlNetworkAccessManagerFactoryPtr(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlNetworkAccessManagerFactoryPtr.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlNetworkAccessManagerFactoryPtr'

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

  @overload(QQmlTypeLoaderLockedData)
  @overload(NoneType)
  def __init__(self, lockedData: Optional[QQmlTypeLoaderLockedData]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlNetworkAccessManagerFactoryPtr::QQmlNetworkAccessManagerFactoryPtr(
    QQmlTypeLoaderLockedData *lockedData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnetworkaccessmanagerfactoryptr.html

    Parameters
    ----------

    lockedData : Optional[QQmlTypeLoaderLockedData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlNetworkAccessManagerFactoryPtr::
    #      QQmlNetworkAccessManagerFactoryPtr(QQmlTypeLoaderLockedData
    #      *lockedData)
    self._noteCreation(
        QQmlNetworkAccessManagerFactoryPtr, lambda: Rituals.call(
            'ritual_ZN34QQmlNetworkAccessManagerFactoryPtrC1EP24QQmlTypeLoa'
            'derLockedData',
            self._addressOf(lockedData),
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

  @overload(QQmlNetworkAccessManagerFactory)
  @overload(NoneType)
  def reset(
      self,
      factory: Optional[QQmlNetworkAccessManagerFactory],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlNetworkAccessManagerFactoryPtr::reset(QQmlNetworkAccessManagerFactory
    *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnetworkaccessmanagerfactoryptr.html#reset

    Parameters
    ----------

    factory : Optional[QQmlNetworkAccessManagerFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlNetworkAccessManagerFactoryPtr::reset(
    #      QQmlNetworkAccessManagerFactory *factory)
    self.uglySide.call(
        'ritual_ZN34QQmlNetworkAccessManagerFactoryPtr5resetEP31QQmlNetwork'
        'AccessManagerFactory',
        self._addressOf(factory),
    )
