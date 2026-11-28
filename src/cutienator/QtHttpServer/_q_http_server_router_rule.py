"""
QHttpServerRouterRule binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverrouterrule.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QHttpServerRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRegularExpressionMatch
  from . import QHttpServerRouterRulePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttpServerRouterRulePrivate = WAIT['QHttpServerRouterRulePrivate']
  QRegularExpressionMatch = WAIT['QRegularExpressionMatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerRouterRule(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerRouterRule: a plain Python object standing
  in front of one C++ QHttpServerRouterRule.

  What exists
  -----------

  Every function of Qt's QHttpServerRouterRule that has a ritual and that
  Python can call so far, 4 names in all: 'd_func', 'contextObject',
  'hasValidMethods', 'matches'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHttpServerRouterRulePrivate *QHttpServerRouterRule::d_func()
    const': takes in Python what 'QHttpServerRouterRulePrivate
    *QHttpServerRouterRule::d_func()' takes.
  - Qt's 'QHttpServerRouterRule::QHttpServerRouterRule(const QString
    &pathPattern, const QHttpServerRequest::Methods methods, const QObject
    *context, QtPrivate::QSlotObjectBase *slotObjRaw)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QHttpServerRouterRule::~QHttpServerRouterRule()': the destructor:
    Python never removes a C++ QHttpServerRouterRule.
  - Qt's 'bool QHttpServerRouterRule::exec(const QHttpServerRequest &request,
    QHttpServerResponder &responder) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'bool
    QHttpServerRouterRule::createPathRegexp(std::initializer_list<QMetaType>
    metaTypes, const QHash<QMetaType, QString> &converters)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 19 functions Qt declares: 5 a template; 4 forbidden.

  What to expect
  --------------

  - The C++ QHttpServerRouterRule is created at the first use, not by
    'QHttpServerRouterRule(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerRouterRule.
  - Each name of Qt's QHttpServerRouterRule that has no cute function yet,
    'bindCaptured', 'bindCapturedImpl', 'bind_front', 'createPathRegexp',
    'exec', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerRouterRule'

  #  A C++ QHttpServerRouterRule Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpServerRouterRule'

  #  The functions Qt calls itself that QHttpServerRouterRule is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'matches': (
          ('_ZNK21QHttpServerRouterRule7matchesERK18QHttpServerRequestP23QR'
           'egularExpressionMatch',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtHttpServer:QHttpServerRequest'),
               ('address', 'address', 'QtCore:QRegularExpressionMatch'),
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

  def contextObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'const QObject *QHttpServerRouterRule::contextObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouterrule.html#contextObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QObject *QHttpServerRouterRule::contextObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QHttpServerRouterRule13contextObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def hasValidMethods(self) -> bool:
    """
    Calls Qt's 'bool QHttpServerRouterRule::hasValidMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouterrule.html#hasValidMethods
    """
    #  bool QHttpServerRouterRule::hasValidMethods() const
    return self.uglySide.call(
        'ritual_ZNK21QHttpServerRouterRule15hasValidMethodsEv',
    )

  @overload(QHttpServerRequest, QRegularExpressionMatch)
  @overload(QHttpServerRequest, NoneType)
  def matches(
      self,
      request: QHttpServerRequest,
      match: Optional[QRegularExpressionMatch],
  ) -> bool:
    """
    Calls Qt's 'bool QHttpServerRouterRule::matches(const QHttpServerRequest
    &request, QRegularExpressionMatch *match) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrouterrule.html#matches

    Parameters
    ----------

    request : QHttpServerRequest
      Passed on as a value: Qt reads the C++ QHttpServerRequest, which stays
      Python's own.

    match : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHttpServerRouterRule::matches(const QHttpServerRequest &request,
    #      QRegularExpressionMatch *match) const
    ritual = (
        'ritual_ZNK21QHttpServerRouterRule7matchesERK18QHttpServerRequestP2'
        '3QRegularExpressionMatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QHttpServerRouterRule7matchesERK18QHttpServerReq'
          'uestP23QRegularExpressionMatch')
    return self.uglySide.call(
        ritual, self._valueOf(request), self._addressOf(match),
    )

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

  @overload(QHttpServerRouterRulePrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QHttpServerRouterRulePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRouterRule::QHttpServerRouterRule(
    QHttpServerRouterRulePrivate *d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouterrule.html#QHttpServerRouterRule

    Parameters
    ----------

    d : Optional[QHttpServerRouterRulePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttpServerRouterRule::QHttpServerRouterRule(
    #      QHttpServerRouterRulePrivate *d)
    self._noteCreation(QHttpServerRouterRule, lambda: Rituals.call(
        'ritual_ZN21QHttpServerRouterRuleC1EP28QHttpServerRouterRulePrivate',
        self._addressOf(d),
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

  def d_func(self) -> Optional[QHttpServerRouterRulePrivate]:
    """
    Calls Qt's 'QHttpServerRouterRulePrivate
    *QHttpServerRouterRule::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverrouterrule.html#d_func

    Returns
    -------

    Optional[QHttpServerRouterRulePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpServerRouterRulePrivate *QHttpServerRouterRule::d_func()
    address = self.uglySide.call('ritual_ZN21QHttpServerRouterRule6d_funcEv')
    from . import QHttpServerRouterRulePrivate
    return QHttpServerRouterRulePrivate._cuteAt(address)

  @staticmethod
  def bindCaptured(*__, **_) -> Never:
    """
    Qt's 'QHttpServerRouterRule::bindCaptured': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QHttpServerRouterRule.bindCaptured' has no cute function yet. "
        "Qt's 'QHttpServerRouterRule::bindCaptured': a template: a pattern "
        "and no single function.")

  @staticmethod
  def bindCapturedImpl(*__, **_) -> Never:
    """
    Qt's 'QHttpServerRouterRule::bindCapturedImpl': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QHttpServerRouterRule.bindCapturedImpl' has no cute function yet. "
        "Qt's 'QHttpServerRouterRule::bindCapturedImpl': a template: a "
        "pattern and no single function.")

  @staticmethod
  def bind_front(*__, **_) -> Never:
    """
    Qt's 'QHttpServerRouterRule::bind_front': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QHttpServerRouterRule.bind_front' has no cute function yet. Qt's "
        "'QHttpServerRouterRule::bind_front': a template: a pattern and no "
        "single function.")

  @staticmethod
  def createPathRegexp(*__, **_) -> Never:
    """
    Qt's 'bool
    QHttpServerRouterRule::createPathRegexp(std::initializer_list<QMetaType>
    metaTypes, const QHash<QMetaType, QString> &converters)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerRouterRule.createPathRegexp' has no cute function yet. "
        "Qt's 'bool "
        "QHttpServerRouterRule::createPathRegexp(std::initializer_list<QMeta"
        "Type> metaTypes, const QHash<QMetaType, QString> &converters)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def exec(*__, **_) -> Never:
    """
    Qt's 'bool QHttpServerRouterRule::exec(const QHttpServerRequest &request,
    QHttpServerResponder &responder) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerRouterRule.exec' has no cute function yet. Qt's 'bool "
        "QHttpServerRouterRule::exec(const QHttpServerRequest &request, "
        "QHttpServerResponder &responder) const': takes a type Python has "
        "no way to hand over yet.")
