"""
QScxmlDynamicScxmlServiceFactory binding of the Qt C++
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
from . import QScxmlInvokableServiceFactory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QScxmlInvokableService, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlDynamicScxmlServiceFactory(QScxmlInvokableServiceFactory):
  """
  The cute side of Qt's QScxmlDynamicScxmlServiceFactory: a plain Python
  object standing in front of one C++ QScxmlDynamicScxmlServiceFactory.

  It is built on the cute 'QScxmlInvokableServiceFactory', as Qt's
  QScxmlDynamicScxmlServiceFactory is built on Qt's
  QScxmlInvokableServiceFactory, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlDynamicScxmlServiceFactory that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'invoke'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlDynamicScxmlServiceFactory::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QScxmlDynamicScxmlServiceFactory::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QScxmlDynamicScxmlServiceFactory::QScxmlDynamicScxmlServiceFactory(const
    QScxmlExecutableContent::InvokeInfo &invokeInfo, const
    QList<QScxmlExecutableContent::StringId> &names, const
    QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlDynamicScxmlServiceFactory is created at the first use, not
    by 'QScxmlDynamicScxmlServiceFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlDynamicScxmlServiceFactory.
  - Qt tells when it has removed the C++ QScxmlDynamicScxmlServiceFactory.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlDynamicScxmlServiceFactory that has no cute
    function yet, '__init__', holds a function that raises
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
    Calls Qt's 'QString QScxmlDynamicScxmlServiceFactory::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldynamicscxmlservicefactory.html#tr

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
    #  QString QScxmlDynamicScxmlServiceFactory::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QScxmlDynamicScxmlServiceFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlDynamicScxmlServiceFactory'

  #  A C++ QScxmlDynamicScxmlServiceFactory Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlDynamicScxmlServiceFactory'

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
    *QScxmlDynamicScxmlServiceFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldynamicscxmlservicefactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlDynamicScxmlServiceFactory::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QScxmlDynamicScxmlServiceFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's
    'QScxmlDynamicScxmlServiceFactory::QScxmlDynamicScxmlServiceFactory(const
    QScxmlExecutableContent::InvokeInfo &invokeInfo, const
    QList<QScxmlExecutableContent::StringId> &names, const
    QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlDynamicScxmlServiceFactory.__init__' has no cute function "
        "yet. Qt's "
        "'QScxmlDynamicScxmlServiceFactory::QScxmlDynamicScxmlServiceFactory"
        "(const QScxmlExecutableContent::InvokeInfo &invokeInfo, const "
        "QList<QScxmlExecutableContent::StringId> &names, const "
        "QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject "
        "*parent)': takes a type Python has no way to hand over yet.")

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

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def invoke(
      self,
      parentStateMachine: Optional[QScxmlStateMachine],
  ) -> Optional[QScxmlInvokableService]:
    """
    Calls Qt's 'QScxmlInvokableService
    *QScxmlDynamicScxmlServiceFactory::invoke(QScxmlStateMachine
    *parentStateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldynamicscxmlservicefactory.html#invoke

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
    #      *QScxmlDynamicScxmlServiceFactory::invoke(QScxmlStateMachine
    #      *parentStateMachine)
    ritual = (
        'ritual_ZN32QScxmlDynamicScxmlServiceFactory6invokeEP18QScxmlStateM'
        'achine')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QScxmlDynamicScxmlServiceFactory6invokeEP18QScxml'
          'StateMachine')
    address = self.uglySide.call(ritual, self._addressOf(parentStateMachine))
    from . import QScxmlInvokableService
    return QScxmlInvokableService._cuteAt(address)
