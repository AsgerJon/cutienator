"""
QScxmlInvokableServiceFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlinvokableservice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QScxmlInvokableService, QScxmlInvokableServiceFactoryPrivate
  from . import QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlInvokableServiceFactory(QObject):
  """
  The cute side of Qt's QScxmlInvokableServiceFactory: a plain Python object
  standing in front of one C++ QScxmlInvokableServiceFactory.

  It is built on the cute 'QObject', as Qt's QScxmlInvokableServiceFactory is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlInvokableServiceFactory that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr', 'd_func',
  'invoke', 'invokeInfo'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlInvokableServiceFactory::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QScxmlInvokableServiceFactory::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScxmlInvokableServiceFactoryPrivate
    *QScxmlInvokableServiceFactory::d_func() const': takes in Python what
    'QScxmlInvokableServiceFactoryPrivate
    *QScxmlInvokableServiceFactory::d_func()' takes.
  - Qt's 'QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(const
    QScxmlExecutableContent::InvokeInfo &invokeInfo, const
    QList<QScxmlExecutableContent::StringId> &names, const
    QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QList<QScxmlExecutableContent::ParameterInfo>
    &QScxmlInvokableServiceFactory::parameters() const': gives a type Python
    has no way to take yet.
  - Qt's 'const QList<QScxmlExecutableContent::StringId>
    &QScxmlInvokableServiceFactory::names() const': gives a type Python has
    no way to take yet.
  - Qt's 'QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(
    QScxmlInvokableServiceFactoryPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlInvokableServiceFactory is created at the first use, not by
    'QScxmlInvokableServiceFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlInvokableServiceFactory.
  - Qt tells when it has removed the C++ QScxmlInvokableServiceFactory. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlInvokableServiceFactory that has no cute function
    yet, '__init__', 'names', 'parameters', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QScxmlInvokableServiceFactory::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlInvokableServiceFactory::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QScxmlInvokableServiceFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInvokableServiceFactory'

  #  A C++ QScxmlInvokableServiceFactory Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlInvokableServiceFactory'

  #  The functions Qt calls itself that QScxmlInvokableServiceFactory is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'invoke': (
          ('_ZN29QScxmlInvokableServiceFactory6invokeEP18QScxmlStateMachine',
           ('address', 'address', 'QtScxml:QScxmlInvokableService'),
           (
               ('address', 'address', 'QtScxml:QScxmlStateMachine'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QScxmlInvokableServiceFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlInvokableServiceFactory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QScxmlInvokableServiceFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def invokeInfo(self) -> QScxmlExecutableContent.InvokeInfo:
    """
    Calls Qt's 'const QScxmlExecutableContent::InvokeInfo
    &QScxmlInvokableServiceFactory::invokeInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#invokeInfo

    Returns
    -------

    QScxmlExecutableContent.InvokeInfo
      A new cute QScxmlExecutableContent::InvokeInfo around the copy Qt gave
      back. Python owns it.
    """
    #  const QScxmlExecutableContent::InvokeInfo
    #      &QScxmlInvokableServiceFactory::invokeInfo() const
    address = self.uglySide.call(
        'ritual_ZNK29QScxmlInvokableServiceFactory10invokeInfoEv',
    )
    return QScxmlExecutableContent.InvokeInfo._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's
      'QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(const
      QScxmlExecutableContent::InvokeInfo &invokeInfo, const
      QList<QScxmlExecutableContent::StringId> &names, const
      QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject
      *parent)': takes a type Python has no way to hand over yet.
    - Qt's 'QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(
      QScxmlInvokableServiceFactoryPrivate &dd, QObject *parent)': takes a
      type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokableServiceFactory.__init__' has no cute function yet. "
        "Qt's "
        "'QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(const"
        " QScxmlExecutableContent::InvokeInfo &invokeInfo, const "
        "QList<QScxmlExecutableContent::StringId> &names, const "
        "QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject "
        "*parent)': takes a type Python has no way to hand over yet. Qt's "
        "'QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(QScxm"
        "lInvokableServiceFactoryPrivate &dd, QObject *parent)': takes a "
        "type Python has no way to hand over yet.")

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

  def d_func(self) -> Optional[QScxmlInvokableServiceFactoryPrivate]:
    """
    Calls Qt's 'QScxmlInvokableServiceFactoryPrivate
    *QScxmlInvokableServiceFactory::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#d_func

    Returns
    -------

    Optional[QScxmlInvokableServiceFactoryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlInvokableServiceFactoryPrivate
    #      *QScxmlInvokableServiceFactory::d_func()
    address = self.uglySide.call(
        'ritual_ZN29QScxmlInvokableServiceFactory6d_funcEv',
    )
    from . import QScxmlInvokableServiceFactoryPrivate
    return QScxmlInvokableServiceFactoryPrivate._cuteAt(address)

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def invoke(
      self,
      parentStateMachine: Optional[QScxmlStateMachine],
  ) -> Optional[QScxmlInvokableService]:
    """
    Calls Qt's 'QScxmlInvokableService
    *QScxmlInvokableServiceFactory::invoke(QScxmlStateMachine
    *parentStateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#invoke

    Parameters
    ----------

    parentStateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QScxmlInvokableService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlInvokableService
    #      *QScxmlInvokableServiceFactory::invoke(QScxmlStateMachine
    #      *parentStateMachine)
    address = self.uglySide.call(
        'ritual_ZN29QScxmlInvokableServiceFactory6invokeEP18QScxmlStateMach'
        'ine',
        self._addressOf(parentStateMachine),
    )
    from . import QScxmlInvokableService
    return QScxmlInvokableService._cuteAt(address)

  @staticmethod
  def names(*__, **_) -> Never:
    """
    Qt's 'const QList<QScxmlExecutableContent::StringId>
    &QScxmlInvokableServiceFactory::names() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokableServiceFactory.names' has no cute function yet. "
        "Qt's 'const QList<QScxmlExecutableContent::StringId> "
        "&QScxmlInvokableServiceFactory::names() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'const QList<QScxmlExecutableContent::ParameterInfo>
    &QScxmlInvokableServiceFactory::parameters() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokableServiceFactory.parameters' has no cute function "
        "yet. Qt's 'const QList<QScxmlExecutableContent::ParameterInfo> "
        "&QScxmlInvokableServiceFactory::parameters() const': gives a type "
        "Python has no way to take yet.")
