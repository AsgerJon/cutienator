"""
QDBusAbstractAdaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusabstractadaptor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDBusAbstractAdaptorPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusAbstractAdaptor(QObject):
  """
  The cute side of Qt's QDBusAbstractAdaptor: a plain Python object standing
  in front of one C++ QDBusAbstractAdaptor.

  It is built on the cute 'QObject', as Qt's QDBusAbstractAdaptor is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusAbstractAdaptor that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'setAutoRelaySignals', 'autoRelaySignals', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusAbstractAdaptor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusAbstractAdaptor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusAbstractAdaptor::~QDBusAbstractAdaptor()': the destructor:
    Python never removes a C++ QDBusAbstractAdaptor.
  - Qt's 'const QDBusAbstractAdaptorPrivate *QDBusAbstractAdaptor::d_func()
    const': takes in Python what 'QDBusAbstractAdaptorPrivate
    *QDBusAbstractAdaptor::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDBusAbstractAdaptor is created at the first use, not by
    'QDBusAbstractAdaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusAbstractAdaptor.
  - Qt tells when it has removed the C++ QDBusAbstractAdaptor. Every call on
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
    Calls Qt's 'QString QDBusAbstractAdaptor::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractadaptor.html#tr

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
    #  QString QDBusAbstractAdaptor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QDBusAbstractAdaptor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusAbstractAdaptor'

  #  A C++ QDBusAbstractAdaptor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusAbstractAdaptor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusAbstractAdaptor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusAbstractAdaptor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QDBusAbstractAdaptor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def autoRelaySignals(self) -> bool:
    """
    Calls Qt's 'bool QDBusAbstractAdaptor::autoRelaySignals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptor.html#autoRelaySignals
    """
    #  bool QDBusAbstractAdaptor::autoRelaySignals() const
    return self.uglySide.call(
        'ritual_ZNK20QDBusAbstractAdaptor16autoRelaySignalsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoRelaySignals(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusAbstractAdaptor::setAutoRelaySignals(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptor.html#setAutoRelaySignals

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusAbstractAdaptor::setAutoRelaySignals(bool enable)
    self.uglySide.call(
        'ritual_ZN20QDBusAbstractAdaptor19setAutoRelaySignalsEb', enable,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QDBusAbstractAdaptor::QDBusAbstractAdaptor(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptor.html#QDBusAbstractAdaptor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusAbstractAdaptor::QDBusAbstractAdaptor(QObject *parent)
    self._noteCreation(QDBusAbstractAdaptor, lambda: Rituals.call(
        'ritual_ZN20QDBusAbstractAdaptorC1EP7QObject',
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

  def d_func(self) -> Optional[QDBusAbstractAdaptorPrivate]:
    """
    Calls Qt's 'QDBusAbstractAdaptorPrivate *QDBusAbstractAdaptor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusabstractadaptor.html#d_func

    Returns
    -------

    Optional[QDBusAbstractAdaptorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusAbstractAdaptorPrivate *QDBusAbstractAdaptor::d_func()
    address = self.uglySide.call('ritual_ZN20QDBusAbstractAdaptor6d_funcEv')
    from . import QDBusAbstractAdaptorPrivate
    return QDBusAbstractAdaptorPrivate._cuteAt(address)
