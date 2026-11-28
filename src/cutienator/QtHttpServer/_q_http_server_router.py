"""
QHttpServerRouter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverrouter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType
  from . import QAbstractHttpServer, QHttpServerRouterPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractHttpServer = WAIT['QAbstractHttpServer']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerRouter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerRouter: a plain Python object standing in
  front of one C++ QHttpServerRouter.

  What exists
  -----------

  Every function of Qt's QHttpServerRouter that has a ritual and that Python
  can call so far, 4 names in all: 'd_func', 'addConverter',
  'removeConverter', 'clearConverters'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHttpServerRouterPrivate *QHttpServerRouter::d_func() const':
    takes in Python what 'QHttpServerRouterPrivate
    *QHttpServerRouter::d_func()' takes.
  - Qt's 'QHttpServerRouter::~QHttpServerRouter()': the destructor: Python
    never removes a C++ QHttpServerRouter.
  - Qt's 'const QHash<QMetaType, QString> &QHttpServerRouter::converters()
    const': gives a type Python has no way to take yet.
  - Qt's 'bool QHttpServerRouter::handleRequest(const QHttpServerRequest
    &request, QHttpServerResponder &responder) const': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 4 forbidden; 3 a template; 1 not a gap;
  1 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QHttpServerRouter is created at the first use, not by
    'QHttpServerRouter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerRouter.
  - Each name of Qt's QHttpServerRouter that has no cute function yet,
    'addRule', 'addRuleHelper', 'addRuleImpl', 'converters', 'handleRequest',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerRouter'

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

  @overload(QAbstractHttpServer)
  @overload(NoneType)
  def __init__(self, server: Optional[QAbstractHttpServer]) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRouter::QHttpServerRouter(QAbstractHttpServer *server)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouter.html#QHttpServerRouter

    Parameters
    ----------

    server : Optional[QAbstractHttpServer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttpServerRouter::QHttpServerRouter(QAbstractHttpServer *server)
    self._noteCreation(QHttpServerRouter, lambda: Rituals.call(
        'ritual_ZN17QHttpServerRouterC1EP19QAbstractHttpServer',
        self._addressOf(server),
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

  def d_func(self) -> Optional[QHttpServerRouterPrivate]:
    """
    Calls Qt's 'QHttpServerRouterPrivate *QHttpServerRouter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrouter.html#d_func

    Returns
    -------

    Optional[QHttpServerRouterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpServerRouterPrivate *QHttpServerRouter::d_func()
    address = self.uglySide.call('ritual_ZN17QHttpServerRouter6d_funcEv')
    from . import QHttpServerRouterPrivate
    return QHttpServerRouterPrivate._cuteAt(address)

  @overload(QMetaType, str)
  def addConverter(self, metaType: QMetaType, regexp: str) -> None:
    """
    Calls Qt's 'void QHttpServerRouter::addConverter(QMetaType metaType,
    QAnyStringView regexp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouter.html#addConverter

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    regexp : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpServerRouter::addConverter(QMetaType metaType,
    #      QAnyStringView regexp)
    self.uglySide.call(
        'ritual_ZN17QHttpServerRouter12addConverterE9QMetaType14QAnyStringV'
        'iew',
        self._valueOf(metaType), regexp,
    )

  @overload(QMetaType)
  def removeConverter(self, metaType: QMetaType) -> None:
    """
    Calls Qt's 'void QHttpServerRouter::removeConverter(QMetaType metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouter.html#removeConverter

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QHttpServerRouter::removeConverter(QMetaType metaType)
    self.uglySide.call(
        'ritual_ZN17QHttpServerRouter15removeConverterE9QMetaType',
        self._valueOf(metaType),
    )

  def clearConverters(self) -> None:
    """
    Calls Qt's 'void QHttpServerRouter::clearConverters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouter.html#clearConverters
    """
    #  void QHttpServerRouter::clearConverters()
    self.uglySide.call('ritual_ZN17QHttpServerRouter15clearConvertersEv')

  @staticmethod
  def addRule(*__, **_) -> Never:
    """
    Qt's 'QHttpServerRouter::addRule': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QHttpServerRouter.addRule' has no cute function yet. Qt's "
        "'QHttpServerRouter::addRule': a template: a pattern and no single "
        "function.")

  @staticmethod
  def addRuleHelper(*__, **_) -> Never:
    """
    Qt's 'QHttpServerRouter::addRuleHelper': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QHttpServerRouter.addRuleHelper' has no cute function yet. Qt's "
        "'QHttpServerRouter::addRuleHelper': a template: a pattern and no "
        "single function.")

  @staticmethod
  def addRuleImpl(*__, **_) -> Never:
    """
    Qt's 'QHttpServerRouterRule
    *QHttpServerRouter::addRuleImpl(std::unique_ptr<QHttpServerRouterRule>
    rule, std::initializer_list<QMetaType> metaTypes)': the compiler refuses
    its ritual as it would be written here: call to deleted constructor of
    'std::unique_ptr<QHttpServerRouterRule>'.
    """
    raise NotImplementedError(
        "'QHttpServerRouter.addRuleImpl' has no cute function yet. Qt's "
        "'QHttpServerRouterRule "
        "*QHttpServerRouter::addRuleImpl(std::unique_ptr<QHttpServerRouterRu"
        "le> rule, std::initializer_list<QMetaType> metaTypes)': the "
        "compiler refuses its ritual as it would be written here: call to "
        "deleted constructor of 'std::unique_ptr<QHttpServerRouterRule>'.")

  @staticmethod
  def converters(*__, **_) -> Never:
    """
    Qt's 'const QHash<QMetaType, QString> &QHttpServerRouter::converters()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpServerRouter.converters' has no cute function yet. Qt's "
        "'const QHash<QMetaType, QString> &QHttpServerRouter::converters() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def handleRequest(*__, **_) -> Never:
    """
    Qt's 'bool QHttpServerRouter::handleRequest(const QHttpServerRequest
    &request, QHttpServerResponder &responder) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerRouter.handleRequest' has no cute function yet. Qt's "
        "'bool QHttpServerRouter::handleRequest(const QHttpServerRequest "
        "&request, QHttpServerResponder &responder) const': takes a type "
        "Python has no way to hand over yet.")
