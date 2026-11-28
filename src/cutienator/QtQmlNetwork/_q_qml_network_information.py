"""
QQmlNetworkInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlnetworkinformation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlNetworkInformation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtNetwork import QNetworkInformation
  from ..QtQml import QJSEngine, QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSEngine = WAIT['QJSEngine']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlNetworkInformation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlNetworkInformation: a plain Python object
  standing in front of one C++ QQmlNetworkInformation.

  C++ hands a QQmlNetworkInformation around as a copy, so every C++
  QQmlNetworkInformation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlNetworkInformation that has a ritual and that
  Python can call so far, 1 name in all: 'create'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlNetworkInformation::qt_qmlMarker_foreign()': one of Qt's
    own inner workings.
  - Qt's 'void QQmlNetworkInformation::qt_qmlMarker_singleton()': one of Qt's
    own inner workings.
  - Qt's 'QQmlNetworkInformation::~QQmlNetworkInformation()': the destructor:
    Python removes its C++ QQmlNetworkInformation by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlNetworkInformation is created at the first use, not by
    'QQmlNetworkInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlNetworkInformation back gives a copy the ritual
    made for Python, in a new cute QQmlNetworkInformation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlEngine, QJSEngine)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QJSEngine)
  @overload(NoneType, NoneType)
  def create(
      a0: Optional[QQmlEngine],
      a1: Optional[QJSEngine],
  ) -> Optional[QNetworkInformation]:
    """
    Calls Qt's 'QNetworkInformation
    *QQmlNetworkInformation::create(QQmlEngine *a0, QJSEngine *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnetworkinformation.html#create

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkInformation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkInformation *QQmlNetworkInformation::create(QQmlEngine *a0,
    #      QJSEngine *a1)
    address = Rituals.call(
        'ritual_ZN22QQmlNetworkInformation6createEP10QQmlEngineP9QJSEngine',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )
    from ..QtNetwork import QNetworkInformation
    return QNetworkInformation._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlNetworkInformation'

  #  Qt's '~QQmlNetworkInformation()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlNetworkInformation behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QQmlNetworkInformationD1Ev'

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
