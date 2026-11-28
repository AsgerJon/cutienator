"""
QDeclarativePluginParameter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativepluginparameter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePluginParameter to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativePluginParameter(QObject):
  """
  The cute side of Qt's QDeclarativePluginParameter: a plain Python object
  standing in front of one C++ QDeclarativePluginParameter.

  It is built on the cute 'QObject', as Qt's QDeclarativePluginParameter is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePluginParameter that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'tr',
  'setName', 'name', 'setValue', 'value', 'isInitialized', 'nameChanged',
  'valueChanged', 'initialized'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePluginParameter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativePluginParameter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePluginParameter::~QDeclarativePluginParameter()': the
    destructor: Python never removes a C++ QDeclarativePluginParameter.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePluginParameter is created at the first use, not by
    'QDeclarativePluginParameter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePluginParameter.
  - Qt tells when it has removed the C++ QDeclarativePluginParameter. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDeclarativePluginParameter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#tr

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
    #  QString QDeclarativePluginParameter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDeclarativePluginParameter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePluginParameter'

  #  A C++ QDeclarativePluginParameter Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePluginParameter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativePluginParameter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePluginParameter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativePluginParameter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePluginParameter::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePluginParameter::name() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativePluginParameter4nameEv',
    )

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativePluginParameter::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativePluginParameter::value() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativePluginParameter5valueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePluginParameter::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#isInitialized
    """
    #  bool QDeclarativePluginParameter::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativePluginParameter13isInitializedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativePluginParameter::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativePluginParameter::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePluginParameter7setNameERK7QString', name,
    )

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativePluginParameter::setValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativePluginParameter::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePluginParameter8setValueERK8QVariant',
        self._valueOf(value),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativePluginParameter::QDeclarativePluginParameter(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePluginParameter::QDeclarativePluginParameter(QObject
    #      *parent)
    self._noteCreation(QDeclarativePluginParameter, lambda: Rituals.call(
        'ritual_ZN27QDeclarativePluginParameterC1EP7QObject',
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

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativePluginParameter::nameChanged(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativePluginParameter::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePluginParameter11nameChangedERK7QString',
        name,
    )

  @overload(QVariant)
  def valueChanged(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativePluginParameter::valueChanged(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#valueChanged

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativePluginParameter::valueChanged(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePluginParameter12valueChangedERK8QVariant',
        self._valueOf(value),
    )

  def initialized(self) -> None:
    """
    Calls Qt's 'void QDeclarativePluginParameter::initialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepluginparameter.html#initialized
    """
    #  void QDeclarativePluginParameter::initialized()
    self.uglySide.call(
        'ritual_ZN27QDeclarativePluginParameter11initializedEv',
    )
