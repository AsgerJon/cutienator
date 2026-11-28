"""
QQuickStochasticState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickStochasticState to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject

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


class QQuickStochasticState(QObject):
  """
  The cute side of Qt's QQuickStochasticState: a plain Python object standing
  in front of one C++ QQuickStochasticState.

  It is built on the cute 'QObject', as Qt's QQuickStochasticState is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStochasticState that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr', 'duration',
  'name', 'to', 'durationVariation', 'variedDuration', 'randomStart',
  'durationChanged', 'nameChanged', 'toChanged', 'durationVariationChanged',
  'entered', 'randomStartChanged', 'setDuration', 'setName', 'setTo',
  'setDurationVariation', 'setRandomStart'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStochasticState::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickStochasticState::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickStochasticState is created at the first use, not by
    'QQuickStochasticState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStochasticState.
  - Qt tells when it has removed the C++ QQuickStochasticState. Every call on
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
    Calls Qt's 'QString QQuickStochasticState::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticstate.html#tr

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
    #  QString QQuickStochasticState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickStochasticState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStochasticState'

  #  The functions Qt calls itself that QQuickStochasticState is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'variedDuration': (
          ('_ZNK21QQuickStochasticState14variedDurationEv',
           ('int', 'number', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QQuickStochasticState::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStochasticState::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickStochasticState10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickStochasticState::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#duration
    """
    #  int QQuickStochasticState::duration() const
    return self.uglySide.call('ritual_ZNK21QQuickStochasticState8durationEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickStochasticState::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticstate.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStochasticState::name() const
    return self.uglySide.call('ritual_ZNK21QQuickStochasticState4nameEv')

  def to(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QQuickStochasticState::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticstate.html#to

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QQuickStochasticState::to() const
    address = self.uglySide.call('ritual_ZNK21QQuickStochasticState2toEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def durationVariation(self) -> int:
    """
    Calls Qt's 'int QQuickStochasticState::durationVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#durationVariation
    """
    #  int QQuickStochasticState::durationVariation() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickStochasticState17durationVariationEv',
    )

  def variedDuration(self) -> int:
    """
    Calls Qt's 'int QQuickStochasticState::variedDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#variedDuration
    """
    #  int QQuickStochasticState::variedDuration() const
    ritual = 'ritual_ZNK21QQuickStochasticState14variedDurationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickStochasticState14variedDurationEv'
    return self.uglySide.call(ritual)

  def randomStart(self) -> bool:
    """
    Calls Qt's 'bool QQuickStochasticState::randomStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#randomStart
    """
    #  bool QQuickStochasticState::randomStart() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickStochasticState11randomStartEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::setDuration(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#setDuration

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickStochasticState::setDuration(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState11setDurationEi', arg,
    )

  @overload(str)
  def setName(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::setName(const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticstate.html#setName

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStochasticState::setName(const QString &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState7setNameERK7QString', arg,
    )

  @overload(QMap[str, QVariant])
  def setTo(self, arg: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::setTo(const QVariantMap &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticstate.html#setTo

    Parameters
    ----------

    arg : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickStochasticState::setTo(const QVariantMap &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState5setToERK4QMapI7QString8QVariantE',
        self._valueOf(arg),
    )

  @overload(int)
  def setDurationVariation(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::setDurationVariation(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#setDurationVariation

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickStochasticState::setDurationVariation(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState20setDurationVariationEi', arg,
    )

  @overload(bool)
  def setRandomStart(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::setRandomStart(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#setRandomStart

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickStochasticState::setRandomStart(bool arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState14setRandomStartEb', arg,
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
    'QQuickStochasticState::QQuickStochasticState(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#QQuickStochasticState

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStochasticState::QQuickStochasticState(QObject *parent)
    self._noteCreation(QQuickStochasticState, lambda: Rituals.call(
        'ritual_ZN21QQuickStochasticStateC1EP7QObject',
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

  @overload(int)
  def durationChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::durationChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#durationChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickStochasticState::durationChanged(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState15durationChangedEi', arg,
    )

  @overload(str)
  def nameChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::nameChanged(const QString &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#nameChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStochasticState::nameChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState11nameChangedERK7QString', arg,
    )

  @overload(QMap[str, QVariant])
  def toChanged(self, arg: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::toChanged(const QVariantMap
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#toChanged

    Parameters
    ----------

    arg : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickStochasticState::toChanged(const QVariantMap &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState9toChangedERK4QMapI7QString8QVaria'
        'ntE',
        self._valueOf(arg),
    )

  @overload(int)
  def durationVariationChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::durationVariationChanged(int
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickStochasticState::durationVariationChanged(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState24durationVariationChangedEi', arg,
    )

  def entered(self) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::entered()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticstate.html#entered
    """
    #  void QQuickStochasticState::entered()
    self.uglySide.call('ritual_ZN21QQuickStochasticState7enteredEv')

  @overload(bool)
  def randomStartChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickStochasticState::randomStartChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticstate.html#randomStartChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickStochasticState::randomStartChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN21QQuickStochasticState18randomStartChangedEb', arg,
    )


#  Qt's 'QList<QQuickStochasticState *>': the list of QQuickStochasticState,
#  which 'QList[QQuickStochasticState]' gives. It is made here, so that there
#  is one as soon as there can be a QQuickStochasticState.
QList.createKind(
    QQuickStochasticState, 'address',
    make='ritual_list_make_QQuickStochasticState_ptr',
    add='ritual_list_add_QQuickStochasticState_ptr',
    size='ritual_list_size_QQuickStochasticState_ptr',
    at='ritual_list_at_QQuickStochasticState_ptr',
    drop='ritual_list_drop_QQuickStochasticState_ptr',
)
