"""
QScxmlNullDataModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlnulldatamodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from . import QScxmlDataModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QScxmlEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlEvent = WAIT['QScxmlEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlNullDataModel(QScxmlDataModel):
  """
  The cute side of Qt's QScxmlNullDataModel: a plain Python object standing
  in front of one C++ QScxmlNullDataModel.

  It is built on the cute 'QScxmlDataModel', as Qt's QScxmlNullDataModel is
  built on Qt's QScxmlDataModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlNullDataModel that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'setup',
  'setScxmlEvent', 'scxmlProperty', 'hasScxmlProperty', 'setScxmlProperty'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlNullDataModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QScxmlNullDataModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QScxmlNullDataModelPrivate *QScxmlNullDataModel::d_func()': gives
    'QScxmlNullDataModelPrivate', which has no cute class yet.
  - Qt's 'const QScxmlNullDataModelPrivate *QScxmlNullDataModel::d_func()
    const': gives 'QScxmlNullDataModelPrivate', which has no cute class yet.
  - Qt's 'QScxmlNullDataModel::~QScxmlNullDataModel()': the destructor:
    Python never removes a C++ QScxmlNullDataModel.
  - Qt's 'QString
    QScxmlNullDataModel::evaluateToString(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'bool
    QScxmlNullDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
  - Qt's 'QVariant
    QScxmlNullDataModel::evaluateToVariant(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlNullDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId
    id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlNullDataModel::evaluateAssignment(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlNullDataModel::evaluateInitialization(QScxmlExecutableContent::
    EvaluatorId id, bool *ok)': takes a number to change where it is.
  - Qt's 'void
    QScxmlNullDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId
    id, bool *ok, ForeachLoopBody *body)': takes a number to change where it
    is.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlNullDataModel is created at the first use, not by
    'QScxmlNullDataModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlNullDataModel.
  - Qt tells when it has removed the C++ QScxmlNullDataModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QScxmlNullDataModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#tr

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
    #  QString QScxmlNullDataModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QScxmlNullDataModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlNullDataModel'

  #  A C++ QScxmlNullDataModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlNullDataModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlNullDataModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlNullDataModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QScxmlNullDataModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def scxmlProperty(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QScxmlNullDataModel::scxmlProperty(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#scxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QScxmlNullDataModel::scxmlProperty(const QString &name) const
    ritual = 'ritual_ZNK19QScxmlNullDataModel13scxmlPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QScxmlNullDataModel13scxmlPropertyERK7QString')
    address = self.uglySide.call(ritual, name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def hasScxmlProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QScxmlNullDataModel::hasScxmlProperty(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#hasScxmlProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlNullDataModel::hasScxmlProperty(const QString &name) const
    ritual = 'ritual_ZNK19QScxmlNullDataModel16hasScxmlPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QScxmlNullDataModel16hasScxmlPropertyERK7QString')
    return self.uglySide.call(ritual, name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScxmlEvent)
  def setScxmlEvent(self, event: QScxmlEvent) -> None:
    """
    Calls Qt's 'void QScxmlNullDataModel::setScxmlEvent(const QScxmlEvent
    &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#setScxmlEvent

    Parameters
    ----------

    event : QScxmlEvent
      Passed on as a value: Qt reads the C++ QScxmlEvent, which stays
      Python's own.
    """
    #  void QScxmlNullDataModel::setScxmlEvent(const QScxmlEvent &event)
    ritual = 'ritual_ZN19QScxmlNullDataModel13setScxmlEventERK11QScxmlEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QScxmlNullDataModel13setScxmlEventERK11QScxmlEven'
          't')
    self.uglySide.call(ritual, self._valueOf(event))

  @overload(str, QVariant, str)
  def setScxmlProperty(
      self,
      name: str,
      value: QVariant,
      context: str,
  ) -> bool:
    """
    Calls Qt's 'bool QScxmlNullDataModel::setScxmlProperty(const QString
    &name, const QVariant &value, const QString &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#setScxmlProperty

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
    #  bool QScxmlNullDataModel::setScxmlProperty(const QString &name, const
    #      QVariant &value, const QString &context)
    ritual = (
        'ritual_ZN19QScxmlNullDataModel16setScxmlPropertyERK7QStringRK8QVar'
        'iantS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QScxmlNullDataModel16setScxmlPropertyERK7QStringR'
          'K8QVariantS2_')
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlNullDataModel::QScxmlNullDataModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#QScxmlNullDataModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScxmlNullDataModel::QScxmlNullDataModel(QObject *parent)
    self._noteCreation(QScxmlNullDataModel, lambda: Rituals.call(
        'ritual_ZN19QScxmlNullDataModelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QMap[str, QVariant])
  def setup(self, initialDataValues: QMap[str, QVariant]) -> bool:
    """
    Calls Qt's 'bool QScxmlNullDataModel::setup(const QVariantMap
    &initialDataValues)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#setup

    Parameters
    ----------

    initialDataValues : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QScxmlNullDataModel::setup(const QVariantMap &initialDataValues)
    return self.uglySide.call(
        'ritual_ZN19QScxmlNullDataModel5setupERK4QMapI7QString8QVariantE',
        self._valueOf(initialDataValues),
    )
