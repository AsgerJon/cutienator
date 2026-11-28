"""
QProcessEnvironmentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QProcessEnvironmentPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOrderedMutexLocker, QSharedData, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QProcEnvValue, QProcessEnvironment
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QProcEnvValue = WAIT['QProcEnvValue']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProcessEnvironmentPrivate(QSharedData):
  """
  The cute side of Qt's QProcessEnvironmentPrivate: a plain Python object
  standing in front of one C++ QProcessEnvironmentPrivate.

  It is built on the cute 'QSharedData', as Qt's QProcessEnvironmentPrivate
  is built on Qt's QSharedData, and has everything that class has.

  C++ hands a QProcessEnvironmentPrivate around as a copy, so every C++
  QProcessEnvironmentPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QProcessEnvironmentPrivate that has a ritual and
  that Python can call so far, 8 names in all: 'prepareName', 'nameToString',
  'prepareValue', 'valueToString', 'fromList', 'toList', 'keys', 'insert'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProcessEnvironmentPrivate::~QProcessEnvironmentPrivate()': the
    destructor: Python removes its C++ QProcessEnvironmentPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QProcessEnvironmentPrivate is created at the first use, not by
    'QProcessEnvironmentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QProcessEnvironmentPrivate back gives a copy the
    ritual made for Python, in a new cute QProcessEnvironmentPrivate.
  """

  #  The classes Qt writes inside QProcessEnvironmentPrivate, each a class in
  #  here as in C++.

  class MutexLocker(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QProcessEnvironmentPrivate::MutexLocker: a plain
    Python object standing in front of one C++
    QProcessEnvironmentPrivate::MutexLocker.

    What exists
    -----------

    No function of Qt's QProcessEnvironmentPrivate::MutexLocker yet. It can
    be made from Python, in 1 way; see '__init__'.

    What to expect
    --------------

    - The C++ QProcessEnvironmentPrivate::MutexLocker is created at the first
      use, not by 'QProcessEnvironmentPrivate::MutexLocker(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QProcessEnvironmentPrivate::MutexLocker.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QProcessEnvironmentPrivate = WAIT['QProcessEnvironmentPrivate']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QProcessEnvironmentPrivate::MutexLocker'

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

    @overload(QProcessEnvironmentPrivate)
    @overload(NoneType)
    def __init__(self, d: Optional[QProcessEnvironmentPrivate]) -> None:
      """
      Notes what was given, for Qt's
      'QProcessEnvironmentPrivate::MutexLocker::MutexLocker(const
      QProcessEnvironmentPrivate *d)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qprocessenvironmentprivate-mutexlocker.html

      Parameters
      ----------

      d : Optional[QProcessEnvironmentPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QProcessEnvironmentPrivate::MutexLocker::MutexLocker(const
      #      QProcessEnvironmentPrivate *d)
      self._noteCreation(
          QProcessEnvironmentPrivate.MutexLocker, lambda: Rituals.call(
              'ritual_ZN26QProcessEnvironmentPrivate11MutexLockerC1EPKS_',
              self._addressOf(d),
          ))

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

  class OrderedMutexLocker(QOrderedMutexLocker):
    """
    The cute side of Qt's QProcessEnvironmentPrivate::OrderedMutexLocker: a
    plain Python object standing in front of one C++
    QProcessEnvironmentPrivate::OrderedMutexLocker.

    It is built on the cute 'QOrderedMutexLocker', as Qt's
    QProcessEnvironmentPrivate::OrderedMutexLocker is built on Qt's
    QOrderedMutexLocker, and has everything that class has.

    What exists
    -----------

    No function of Qt's QProcessEnvironmentPrivate::OrderedMutexLocker yet.
    It can be made from Python, in 1 way; see '__init__'.

    What to expect
    --------------

    - The C++ QProcessEnvironmentPrivate::OrderedMutexLocker is created at
      the first use, not by
      'QProcessEnvironmentPrivate::OrderedMutexLocker(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++
      QProcessEnvironmentPrivate::OrderedMutexLocker.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QProcessEnvironmentPrivate = WAIT['QProcessEnvironmentPrivate']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QProcessEnvironmentPrivate::OrderedMutexLocker'

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

    @overload(QProcessEnvironmentPrivate, QProcessEnvironmentPrivate)
    @overload(QProcessEnvironmentPrivate, NoneType)
    @overload(NoneType, QProcessEnvironmentPrivate)
    @overload(NoneType, NoneType)
    def __init__(
        self,
        d1: Optional[QProcessEnvironmentPrivate],
        d2: Optional[QProcessEnvironmentPrivate],
    ) -> None:
      """
      Notes what was given, for Qt's
      'QProcessEnvironmentPrivate::OrderedMutexLocker::OrderedMutexLocker(
      const QProcessEnvironmentPrivate *d1, const QProcessEnvironmentPrivate
      *d2)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qprocessenvironmentprivate-orderedmutexlocker.html

      Parameters
      ----------

      d1 : Optional[QProcessEnvironmentPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      d2 : Optional[QProcessEnvironmentPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QProcessEnvironmentPrivate::OrderedMutexLocker::
      #      OrderedMutexLocker(const QProcessEnvironmentPrivate *d1, const
      #      QProcessEnvironmentPrivate *d2)
      self._noteCreation(
          QProcessEnvironmentPrivate.OrderedMutexLocker, lambda: Rituals.call(
              'ritual_ZN26QProcessEnvironmentPrivate18OrderedMutexLockerC1E'
              'PKS_S2_',
              self._addressOf(d1), self._addressOf(d2),
          ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStringList)
  def fromList(list: QStringList) -> QProcessEnvironment:
    """
    Calls Qt's 'QProcessEnvironment
    QProcessEnvironmentPrivate::fromList(const QStringList &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#fromList

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QProcessEnvironment
      A new cute QProcessEnvironment around the copy Qt gave back. Python
      owns it.
    """
    #  QProcessEnvironment QProcessEnvironmentPrivate::fromList(const
    #      QStringList &list)
    address = Rituals.call(
        'ritual_ZN26QProcessEnvironmentPrivate8fromListERK5QListI7QStringE',
        CuteMixin._valueOf(list),
    )
    from . import QProcessEnvironment
    return QProcessEnvironment._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProcessEnvironmentPrivate'

  #  Qt's '~QProcessEnvironmentPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QProcessEnvironmentPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QProcessEnvironmentPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def prepareName(self, name: str) -> QByteArray:
    """
    Calls Qt's 'Key QProcessEnvironmentPrivate::prepareName(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#prepareName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  Key QProcessEnvironmentPrivate::prepareName(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK26QProcessEnvironmentPrivate11prepareNameERK7QString',
        name,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray)
  def nameToString(self, name: QByteArray) -> str:
    """
    Calls Qt's 'QString QProcessEnvironmentPrivate::nameToString(const Key
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#nameToString

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcessEnvironmentPrivate::nameToString(const Key &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QProcessEnvironmentPrivate12nameToStringERK10QByteArra'
        'y',
        self._valueOf(name),
    )

  @overload(str)
  def prepareValue(self, value: str) -> QProcEnvValue:
    """
    Calls Qt's 'Value QProcessEnvironmentPrivate::prepareValue(const QString
    &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#prepareValue

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QProcEnvValue
      A new cute QProcEnvValue around the copy Qt gave back. Python owns it.
    """
    #  Value QProcessEnvironmentPrivate::prepareValue(const QString &value)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QProcessEnvironmentPrivate12prepareValueERK7QString',
        value,
    )
    from . import QProcEnvValue
    return QProcEnvValue._cuteOwning(address)

  @overload(QProcEnvValue)
  def valueToString(self, value: QProcEnvValue) -> str:
    """
    Calls Qt's 'QString QProcessEnvironmentPrivate::valueToString(const Value
    &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#valueToString

    Parameters
    ----------

    value : QProcEnvValue
      Passed on as a value: Qt reads the C++ QProcEnvValue, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcessEnvironmentPrivate::valueToString(const Value &value)
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QProcessEnvironmentPrivate13valueToStringERK13QProcEnv'
        'Value',
        self._valueOf(value),
    )

  def toList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QProcessEnvironmentPrivate::toList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#toList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QProcessEnvironmentPrivate::toList() const
    address = self.uglySide.call(
        'ritual_ZNK26QProcessEnvironmentPrivate6toListEv',
    )
    return QStringList._cuteOwning(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QProcessEnvironmentPrivate::keys() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QProcessEnvironmentPrivate::keys() const
    address = self.uglySide.call(
        'ritual_ZNK26QProcessEnvironmentPrivate4keysEv',
    )
    return QStringList._cuteOwning(address)

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
    'QProcessEnvironmentPrivate::QProcessEnvironmentPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html
    """
    #  QProcessEnvironmentPrivate::QProcessEnvironmentPrivate()
    self._noteCreation(QProcessEnvironmentPrivate, lambda: Rituals.call(
        'ritual_ZN26QProcessEnvironmentPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QProcessEnvironmentPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QProcessEnvironmentPrivate::QProcessEnvironmentPrivate(const
    QProcessEnvironmentPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html

    Parameters
    ----------

    other : QProcessEnvironmentPrivate
      Passed on as a value: Qt reads the C++ QProcessEnvironmentPrivate,
      which stays Python's own.
    """
    #  QProcessEnvironmentPrivate::QProcessEnvironmentPrivate(const
    #      QProcessEnvironmentPrivate &other)
    self._noteCreation(QProcessEnvironmentPrivate, lambda: Rituals.call(
        'ritual_ZN26QProcessEnvironmentPrivateC1ERKS_', self._valueOf(other),
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

  @overload(THIS)
  def insert(self, other: QProcessEnvironmentPrivate) -> None:
    """
    Calls Qt's 'void QProcessEnvironmentPrivate::insert(const
    QProcessEnvironmentPrivate &other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironmentprivate.html#insert

    Parameters
    ----------

    other : QProcessEnvironmentPrivate
      Passed on as a value: Qt reads the C++ QProcessEnvironmentPrivate,
      which stays Python's own.
    """
    #  void QProcessEnvironmentPrivate::insert(const
    #      QProcessEnvironmentPrivate &other)
    self.uglySide.call(
        'ritual_ZN26QProcessEnvironmentPrivate6insertERKS_',
        self._valueOf(other),
    )
