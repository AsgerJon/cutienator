"""
QScxmlDataModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmldatamodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QScxmlDataModelPrivate, QScxmlEvent, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlEvent = WAIT['QScxmlEvent']
  QScxmlStateMachine = WAIT['QScxmlStateMachine']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlDataModel(QObject):
  """
  The cute side of Qt's QScxmlDataModel: a plain Python object standing in
  front of one C++ QScxmlDataModel.

  It is built on the cute 'QObject', as Qt's QScxmlDataModel is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlDataModel that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'd_func',
  'createScxmlDataModel', 'setStateMachine', 'stateMachine', 'setup',
  'setScxmlEvent', 'scxmlProperty', 'hasScxmlProperty', 'setScxmlProperty',
  'stateMachineChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlDataModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScxmlDataModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QScxmlDataModelPrivate *QScxmlDataModel::d_func() const':
    takes in Python what 'QScxmlDataModelPrivate *QScxmlDataModel::d_func()'
    takes.
  - Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlDataModel::bindableStateMachine()': gives a type Python has no way
    to take yet.
  - Qt's 'QString
    QScxmlDataModel::evaluateToString(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
  - Qt's 'bool
    QScxmlDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId id,
    bool *ok)': takes a number to change where it is.
  - Qt's 'QVariant
    QScxmlDataModel::evaluateToVariant(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId id,
    bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlDataModel::evaluateAssignment(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlDataModel::evaluateInitialization(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId id,
    bool *ok, ForeachLoopBody *body)': takes a number to change where it is.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QScxmlDataModel is created at the first use, not by
    'QScxmlDataModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlDataModel.
  - Qt tells when it has removed the C++ QScxmlDataModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlDataModel that has no cute function yet,
    '__init__', 'bindableStateMachine', 'evaluateAssignment',
    'evaluateForeach', 'evaluateInitialization', 'evaluateToBool',
    'evaluateToString', 'evaluateToVariant', 'evaluateToVoid', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QScxmlDataModel, each a class in here as in
  #  C++.

  class ForeachLoopBody(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlDataModel::ForeachLoopBody: a plain Python
    object standing in front of one C++ QScxmlDataModel::ForeachLoopBody.

    What exists
    -----------

    No function of Qt's QScxmlDataModel::ForeachLoopBody yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlDataModel::ForeachLoopBody::~ForeachLoopBody()': the
      destructor: Python never removes a C++
      QScxmlDataModel::ForeachLoopBody.
    - Qt's 'void QScxmlDataModel::ForeachLoopBody::run(bool *ok)': takes a
      number to change where it is.

    What has no ritual
    ------------------

    3 of the 5 functions Qt declares: 2 forbidden; 1 the class is abstract,
    so C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.

    What to expect
    --------------

    - The C++ QScxmlDataModel::ForeachLoopBody is created at the first use,
      not by 'QScxmlDataModel::ForeachLoopBody(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QScxmlDataModel::ForeachLoopBody.
    - Each name of Qt's QScxmlDataModel::ForeachLoopBody that has no cute
      function yet, '__init__', 'run', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlDataModel::ForeachLoopBody'

    #  The functions Qt calls itself that QScxmlDataModel::ForeachLoopBody is
    #  the first to declare and that cannot be handed to Python yet, each as
    #  Qt declares it. A class of a program that writes one of them anew is
    #  refused, since Qt would never call what it wrote; see
    #  'CuteMixin._refuseLeftOut'.
    __virtual_left_out__ = {
        'run': (
            'void QScxmlDataModel::ForeachLoopBody::run(bool *)',
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QScxmlDataModel::ForeachLoopBody::ForeachLoopBody()': the class
      is abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
      """
      raise NotImplementedError(
          "'QScxmlDataModel.ForeachLoopBody.__init__' has no cute function "
          "yet. Qt's 'QScxmlDataModel::ForeachLoopBody::ForeachLoopBody()': "
          "the class is abstract, so C++ cannot make one, and the C++ class "
          "of ours does not fill in every function it leaves open.")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def run(*__, **_) -> Never:
      """
      Qt's 'void QScxmlDataModel::ForeachLoopBody::run(bool *ok)': takes a
      number to change where it is.
      """
      raise NotImplementedError(
          "'QScxmlDataModel.ForeachLoopBody.run' has no cute function yet. "
          "Qt's 'void QScxmlDataModel::ForeachLoopBody::run(bool *ok)': "
          "takes a number to change where it is.")

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
    Calls Qt's 'QString QScxmlDataModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#tr

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
    #  QString QScxmlDataModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QScxmlDataModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def createScxmlDataModel(pluginKey: str) -> Optional[QScxmlDataModel]:
    """
    Calls Qt's 'QScxmlDataModel *QScxmlDataModel::createScxmlDataModel(const
    QString &pluginKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodel.html#createScxmlDataModel

    Parameters
    ----------

    pluginKey : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QScxmlDataModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlDataModel *QScxmlDataModel::createScxmlDataModel(const QString
    #      &pluginKey)
    address = Rituals.call(
        'ritual_ZN15QScxmlDataModel20createScxmlDataModelERK7QString',
        pluginKey,
    )
    return QScxmlDataModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlDataModel'

  #  A C++ QScxmlDataModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlDataModel'

  #  The functions Qt calls itself that QScxmlDataModel is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setup': (
          'bool QScxmlDataModel::setup(const QVariantMap &)',
      ),
      'evaluateToString': (
          'QString '
          'QScxmlDataModel::evaluateToString(QScxmlExecutableContent::Evalu'
          'atorId, bool *)',
      ),
      'evaluateToBool': (
          'bool '
          'QScxmlDataModel::evaluateToBool(QScxmlExecutableContent::Evaluat'
          'orId, bool *)',
      ),
      'evaluateToVariant': (
          'QVariant '
          'QScxmlDataModel::evaluateToVariant(QScxmlExecutableContent::Eval'
          'uatorId, bool *)',
      ),
      'evaluateToVoid': (
          'void '
          'QScxmlDataModel::evaluateToVoid(QScxmlExecutableContent::Evaluat'
          'orId, bool *)',
      ),
      'evaluateAssignment': (
          'void '
          'QScxmlDataModel::evaluateAssignment(QScxmlExecutableContent::Eva'
          'luatorId, bool *)',
      ),
      'evaluateInitialization': (
          'void '
          'QScxmlDataModel::evaluateInitialization(QScxmlExecutableContent:'
          ':EvaluatorId, bool *)',
      ),
      'evaluateForeach': (
          'void '
          'QScxmlDataModel::evaluateForeach(QScxmlExecutableContent::Evalua'
          'torId, bool *, ForeachLoopBody *)',
      ),
  }

  #  The functions Qt calls itself that QScxmlDataModel is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setScxmlEvent': (
          ('_ZN15QScxmlDataModel13setScxmlEventERK11QScxmlEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtScxml:QScxmlEvent'),
           )),
      ),
      'scxmlProperty': (
          ('_ZNK15QScxmlDataModel13scxmlPropertyERK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
           )),
      ),
      'hasScxmlProperty': (
          ('_ZNK15QScxmlDataModel16hasScxmlPropertyERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setScxmlProperty': (
          ('_ZN15QScxmlDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'text', ''),
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
    Calls Qt's 'const QMetaObject *QScxmlDataModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlDataModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QScxmlDataModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlDataModel::stateMachine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#stateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlDataModel::stateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK15QScxmlDataModel12stateMachineEv',
    )
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  @overload(str)
  def scxmlProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QScxmlDataModel::scxmlProperty(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#scxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QScxmlDataModel::scxmlProperty(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK15QScxmlDataModel13scxmlPropertyERK7QString', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def hasScxmlProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QScxmlDataModel::hasScxmlProperty(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodel.html#hasScxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlDataModel::hasScxmlProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK15QScxmlDataModel16hasScxmlPropertyERK7QString', name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def setStateMachine(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void QScxmlDataModel::setStateMachine(QScxmlStateMachine
    *stateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodel.html#setStateMachine

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlDataModel::setStateMachine(QScxmlStateMachine
    #      *stateMachine)
    self.uglySide.call(
        'ritual_ZN15QScxmlDataModel15setStateMachineEP18QScxmlStateMachine',
        self._addressOf(stateMachine),
    )

  @overload(QScxmlEvent)
  def setScxmlEvent(self, event: QScxmlEvent) -> None:
    """
    Calls Qt's 'void QScxmlDataModel::setScxmlEvent(const QScxmlEvent
    &event)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#setScxmlEvent

    Parameters
    ----------

    event : QScxmlEvent
      Passed on as a value: Qt reads the C++ QScxmlEvent, which stays
      Python's own.
    """
    #  void QScxmlDataModel::setScxmlEvent(const QScxmlEvent &event)
    self.uglySide.call(
        'ritual_ZN15QScxmlDataModel13setScxmlEventERK11QScxmlEvent',
        self._valueOf(event),
    )

  @overload(str, QVariant, str)
  def setScxmlProperty(
      self,
      name: str,
      value: QVariant,
      context: str,
  ) -> bool:
    """
    Calls Qt's 'bool QScxmlDataModel::setScxmlProperty(const QString &name,
    const QVariant &value, const QString &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodel.html#setScxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    context : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlDataModel::setScxmlProperty(const QString &name, const
    #      QVariant &value, const QString &context)
    return self.uglySide.call(
        'ritual_ZN15QScxmlDataModel16setScxmlPropertyERK7QStringRK8QVariant'
        'S2_',
        name, self._valueOf(value), context,
    )

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
    - Qt's 'QScxmlDataModel::QScxmlDataModel(QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's 'QScxmlDataModel::QScxmlDataModel(QScxmlDataModelPrivate &dd,
      QObject *parent)': the class is abstract, so C++ cannot make one, and
      the C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.__init__' has no cute function yet. Qt's "
        "'QScxmlDataModel::QScxmlDataModel(QObject *parent)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open. Qt's "
        "'QScxmlDataModel::QScxmlDataModel(QScxmlDataModelPrivate &dd, "
        "QObject *parent)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  def d_func(self) -> Optional[QScxmlDataModelPrivate]:
    """
    Calls Qt's 'QScxmlDataModelPrivate *QScxmlDataModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#d_func

    Returns
    -------

    Optional[QScxmlDataModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlDataModelPrivate *QScxmlDataModel::d_func()
    address = self.uglySide.call('ritual_ZN15QScxmlDataModel6d_funcEv')
    from . import QScxmlDataModelPrivate
    return QScxmlDataModelPrivate._cuteAt(address)

  @overload(QMap[str, QVariant])
  def setup(self, initialDataValues: QMap[str, QVariant]) -> bool:
    """
    Calls Qt's 'bool QScxmlDataModel::setup(const QVariantMap
    &initialDataValues)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodel.html#setup

    Parameters
    ----------

    initialDataValues : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QScxmlDataModel::setup(const QVariantMap &initialDataValues)
    return self.uglySide.call(
        'ritual_ZN15QScxmlDataModel5setupERK4QMapI7QString8QVariantE',
        self._valueOf(initialDataValues),
    )

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def stateMachineChanged(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void QScxmlDataModel::stateMachineChanged(QScxmlStateMachine
    *stateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodel.html#stateMachineChanged

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlDataModel::stateMachineChanged(QScxmlStateMachine
    #      *stateMachine)
    self.uglySide.call(
        'ritual_ZN15QScxmlDataModel19stateMachineChangedEP18QScxmlStateMach'
        'ine',
        self._addressOf(stateMachine),
    )

  @staticmethod
  def bindableStateMachine(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlDataModel::bindableStateMachine()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.bindableStateMachine' has no cute function yet. "
        "Qt's 'QBindable<QScxmlStateMachine *> "
        "QScxmlDataModel::bindableStateMachine()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def evaluateAssignment(*__, **_) -> Never:
    """
    Qt's 'void
    QScxmlDataModel::evaluateAssignment(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateAssignment' has no cute function yet. "
        "Qt's 'void "
        "QScxmlDataModel::evaluateAssignment(QScxmlExecutableContent::Evalua"
        "torId id, bool *ok)': takes a number to change where it is.")

  @staticmethod
  def evaluateForeach(*__, **_) -> Never:
    """
    Qt's 'void
    QScxmlDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId id,
    bool *ok, ForeachLoopBody *body)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateForeach' has no cute function yet. Qt's "
        "'void "
        "QScxmlDataModel::evaluateForeach(QScxmlExecutableContent::Evaluator"
        "Id id, bool *ok, ForeachLoopBody *body)': takes a number to change "
        "where it is.")

  @staticmethod
  def evaluateInitialization(*__, **_) -> Never:
    """
    Qt's 'void
    QScxmlDataModel::evaluateInitialization(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateInitialization' has no cute function yet. "
        "Qt's 'void "
        "QScxmlDataModel::evaluateInitialization(QScxmlExecutableContent::Ev"
        "aluatorId id, bool *ok)': takes a number to change where it is.")

  @staticmethod
  def evaluateToBool(*__, **_) -> Never:
    """
    Qt's 'bool
    QScxmlDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId id,
    bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateToBool' has no cute function yet. Qt's "
        "'bool "
        "QScxmlDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorI"
        "d id, bool *ok)': takes a number to change where it is.")

  @staticmethod
  def evaluateToString(*__, **_) -> Never:
    """
    Qt's 'QString
    QScxmlDataModel::evaluateToString(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateToString' has no cute function yet. Qt's "
        "'QString "
        "QScxmlDataModel::evaluateToString(QScxmlExecutableContent::Evaluato"
        "rId id, bool *ok)': takes a number to change where it is.")

  @staticmethod
  def evaluateToVariant(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QScxmlDataModel::evaluateToVariant(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateToVariant' has no cute function yet. Qt's "
        "'QVariant "
        "QScxmlDataModel::evaluateToVariant(QScxmlExecutableContent::Evaluat"
        "orId id, bool *ok)': takes a number to change where it is.")

  @staticmethod
  def evaluateToVoid(*__, **_) -> Never:
    """
    Qt's 'void
    QScxmlDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId id,
    bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlDataModel.evaluateToVoid' has no cute function yet. Qt's "
        "'void "
        "QScxmlDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorI"
        "d id, bool *ok)': takes a number to change where it is.")
