"""
QScxmlCppDataModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlcppdatamodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap
from . import QScxmlDataModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QScxmlCppDataModelPrivate, QScxmlEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlEvent = WAIT['QScxmlEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlCppDataModel(QScxmlDataModel):
  """
  The cute side of Qt's QScxmlCppDataModel: a plain Python object standing in
  front of one C++ QScxmlCppDataModel.

  It is built on the cute 'QScxmlDataModel', as Qt's QScxmlCppDataModel is
  built on Qt's QScxmlDataModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlCppDataModel that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'd_func', 'setup',
  'setScxmlEvent', 'scxmlEvent', 'scxmlProperty', 'hasScxmlProperty',
  'setScxmlProperty', 'inState'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlCppDataModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScxmlCppDataModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScxmlCppDataModelPrivate *QScxmlCppDataModel::d_func()
    const': takes in Python what 'QScxmlCppDataModelPrivate
    *QScxmlCppDataModel::d_func()' takes.
  - Qt's 'void
    QScxmlCppDataModel::evaluateAssignment(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlCppDataModel::evaluateInitialization(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlCppDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId
    id, bool *ok, ForeachLoopBody *body)': takes a number to change where it
    is.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QScxmlCppDataModel is created at the first use, not by
    'QScxmlCppDataModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlCppDataModel.
  - Qt tells when it has removed the C++ QScxmlCppDataModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlCppDataModel that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QScxmlCppDataModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#tr

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
    #  QString QScxmlCppDataModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QScxmlCppDataModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlCppDataModel'

  #  A C++ QScxmlCppDataModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlCppDataModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlCppDataModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlCppDataModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlCppDataModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scxmlEvent(self) -> QScxmlEvent:
    """
    Calls Qt's 'const QScxmlEvent &QScxmlCppDataModel::scxmlEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#scxmlEvent

    Returns
    -------

    QScxmlEvent
      A new cute QScxmlEvent around the copy Qt gave back. Python owns it.
    """
    #  const QScxmlEvent &QScxmlCppDataModel::scxmlEvent() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlCppDataModel10scxmlEventEv',
    )
    from . import QScxmlEvent
    return QScxmlEvent._cuteOwning(address)

  @overload(str)
  def scxmlProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QScxmlCppDataModel::scxmlProperty(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#scxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QScxmlCppDataModel::scxmlProperty(const QString &name) const
    ritual = 'ritual_ZNK18QScxmlCppDataModel13scxmlPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QScxmlCppDataModel13scxmlPropertyERK7QString'
    address = self.uglySide.call(ritual, name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def hasScxmlProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QScxmlCppDataModel::hasScxmlProperty(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#hasScxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlCppDataModel::hasScxmlProperty(const QString &name) const
    ritual = 'ritual_ZNK18QScxmlCppDataModel16hasScxmlPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QScxmlCppDataModel16hasScxmlPropertyERK7QString')
    return self.uglySide.call(ritual, name)

  @overload(str)
  def inState(self, stateName: str) -> bool:
    """
    Calls Qt's 'bool QScxmlCppDataModel::inState(const QString &stateName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#inState

    Parameters
    ----------

    stateName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlCppDataModel::inState(const QString &stateName) const
    return self.uglySide.call(
        'ritual_ZNK18QScxmlCppDataModel7inStateERK7QString', stateName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScxmlEvent)
  def setScxmlEvent(self, scxmlEvent: QScxmlEvent) -> None:
    """
    Calls Qt's 'void QScxmlCppDataModel::setScxmlEvent(const QScxmlEvent
    &scxmlEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#setScxmlEvent

    Parameters
    ----------

    scxmlEvent : QScxmlEvent
      Passed on as a value: Qt reads the C++ QScxmlEvent, which stays
      Python's own.
    """
    #  void QScxmlCppDataModel::setScxmlEvent(const QScxmlEvent &scxmlEvent)
    self.uglySide.call(
        'ritual_ZN18QScxmlCppDataModel13setScxmlEventERK11QScxmlEvent',
        self._valueOf(scxmlEvent),
    )

  @overload(str, QVariant, str)
  def setScxmlProperty(
      self,
      name: str,
      value: QVariant,
      context: str,
  ) -> bool:
    """
    Calls Qt's 'bool QScxmlCppDataModel::setScxmlProperty(const QString
    &name, const QVariant &value, const QString &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#setScxmlProperty

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
    #  bool QScxmlCppDataModel::setScxmlProperty(const QString &name, const
    #      QVariant &value, const QString &context)
    ritual = (
        'ritual_ZN18QScxmlCppDataModel16setScxmlPropertyERK7QStringRK8QVari'
        'antS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QScxmlCppDataModel16setScxmlPropertyERK7QStringRK'
          '8QVariantS2_')
    return self.uglySide.call(ritual, name, self._valueOf(value), context)

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
    Qt's 'QScxmlCppDataModel::QScxmlCppDataModel(QObject *parent)': the class
    is abstract, so C++ cannot make one, and the C++ class of ours does not
    fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QScxmlCppDataModel.__init__' has no cute function yet. Qt's "
        "'QScxmlCppDataModel::QScxmlCppDataModel(QObject *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QScxmlCppDataModelPrivate]:
    """
    Calls Qt's 'QScxmlCppDataModelPrivate *QScxmlCppDataModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#d_func

    Returns
    -------

    Optional[QScxmlCppDataModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlCppDataModelPrivate *QScxmlCppDataModel::d_func()
    address = self.uglySide.call('ritual_ZN18QScxmlCppDataModel6d_funcEv')
    from . import QScxmlCppDataModelPrivate
    return QScxmlCppDataModelPrivate._cuteAt(address)

  @overload(QMap[str, QVariant])
  def setup(self, initialDataValues: QMap[str, QVariant]) -> bool:
    """
    Calls Qt's 'bool QScxmlCppDataModel::setup(const QVariantMap
    &initialDataValues)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#setup

    Parameters
    ----------

    initialDataValues : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QScxmlCppDataModel::setup(const QVariantMap &initialDataValues)
    return self.uglySide.call(
        'ritual_ZN18QScxmlCppDataModel5setupERK4QMapI7QString8QVariantE',
        self._valueOf(initialDataValues),
    )
