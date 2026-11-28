"""
QQmlScriptStringPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlscriptstring_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlScriptStringPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlContext, QQmlScriptString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlScriptString = WAIT['QQmlScriptString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlScriptStringPrivate(QSharedData):
  """
  The cute side of Qt's QQmlScriptStringPrivate: a plain Python object
  standing in front of one C++ QQmlScriptStringPrivate.

  It is built on the cute 'QSharedData', as Qt's QQmlScriptStringPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QQmlScriptStringPrivate around as a copy, so every C++
  QQmlScriptStringPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlScriptStringPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'get', 'create'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlScriptStringPrivate::~QQmlScriptStringPrivate()': the
    destructor: Python removes its C++ QQmlScriptStringPrivate by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QQmlScriptStringPrivate is created at the first use, not by
    'QQmlScriptStringPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlScriptStringPrivate back gives a copy the ritual
    made for Python, in a new cute QQmlScriptStringPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlScriptString)
  def get(script: QQmlScriptString) -> Optional[QQmlScriptStringPrivate]:
    """
    Calls Qt's 'const QQmlScriptStringPrivate
    *QQmlScriptStringPrivate::get(const QQmlScriptString &script)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptstringprivate.html#get

    Parameters
    ----------

    script : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlScriptStringPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlScriptStringPrivate *QQmlScriptStringPrivate::get(const
    #      QQmlScriptString &script)
    address = Rituals.call(
        'ritual_ZN23QQmlScriptStringPrivate3getERK16QQmlScriptString',
        CuteMixin._valueOf(script),
    )
    return QQmlScriptStringPrivate._cuteAt(address)

  @staticmethod
  @overload(str, QQmlContext, QObject)
  @overload(str, QQmlContext, NoneType)
  @overload(str, NoneType, QObject)
  @overload(str, NoneType, NoneType)
  def create(
      script: str,
      context: Optional[QQmlContext],
      scope: Optional[QObject],
  ) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQmlScriptStringPrivate::create(const
    QString &script, QQmlContext *context, QObject *scope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstringprivate.html#create

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scope : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQmlScriptStringPrivate::create(const QString
    #      &script, QQmlContext *context, QObject *scope)
    address = Rituals.call(
        'ritual_ZN23QQmlScriptStringPrivate6createERK7QStringP11QQmlContext'
        'P7QObject',
        script, CuteMixin._addressOf(context), CuteMixin._addressOf(scope,
        'QObject'),
    )
    from . import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlScriptStringPrivate'

  #  Qt's '~QQmlScriptStringPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlScriptStringPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQmlScriptStringPrivateD1Ev'

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
    'QQmlScriptStringPrivate::QQmlScriptStringPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstringprivate.html
    """
    #  QQmlScriptStringPrivate::QQmlScriptStringPrivate()
    self._noteCreation(QQmlScriptStringPrivate, lambda: Rituals.call(
        'ritual_ZN23QQmlScriptStringPrivateC1Ev',
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
