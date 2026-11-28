"""
QQuickWebEngineAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQuickWebEngineActionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineAction(QObject):
  """
  The cute side of Qt's QQuickWebEngineAction: a plain Python object standing
  in front of one C++ QQuickWebEngineAction.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineAction is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineAction that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'text',
  'iconName', 'isEnabled', 'trigger', 'triggered', 'enabledChanged',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineAction::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWebEngineAction::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineAction::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickWebEngineAction::~QQuickWebEngineAction()': the destructor:
    Python never removes a C++ QQuickWebEngineAction.
  - Qt's 'const QQuickWebEngineActionPrivate *QQuickWebEngineAction::d_func()
    const': takes in Python what 'QQuickWebEngineActionPrivate
    *QQuickWebEngineAction::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineAction is created at the first use, not by
    'QQuickWebEngineAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineAction.
  - Qt tells when it has removed the C++ QQuickWebEngineAction. Every call on
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
    Calls Qt's 'QString QQuickWebEngineAction::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineaction.html#tr

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
    #  QString QQuickWebEngineAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickWebEngineAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineAction'

  #  A C++ QQuickWebEngineAction Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebEngineAction::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineAction::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickWebEngineAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineAction::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineaction.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineAction::text() const
    return self.uglySide.call('ritual_ZNK21QQuickWebEngineAction4textEv')

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineAction::iconName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineAction::iconName() const
    return self.uglySide.call('ritual_ZNK21QQuickWebEngineAction8iconNameEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineAction::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#isEnabled
    """
    #  bool QQuickWebEngineAction::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickWebEngineAction9isEnabledEv',
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

  @overload(QVariant, str, str, bool, QObject)
  @overload(QVariant, str, str, bool, NoneType)
  def __init__(
      self,
      data: QVariant,
      text: str,
      iconName: str,
      enabled: bool,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineAction::QQuickWebEngineAction(const QVariant &data, const
    QString &text, const QString &iconName, bool enabled, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#QQuickWebEngineAction

    Parameters
    ----------

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    enabled : bool
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWebEngineAction::QQuickWebEngineAction(const QVariant &data,
    #      const QString &text, const QString &iconName, bool enabled,
    #      QObject *parent)
    self._noteCreation(QQuickWebEngineAction, lambda: Rituals.call(
        'ritual_ZN21QQuickWebEngineActionC1ERK8QVariantRK7QStringS5_bP7QObj'
        'ect',
        self._valueOf(data), text, iconName, enabled, self._addressOf(parent,
        'QObject'),
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineAction::QQuickWebEngineAction(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#QQuickWebEngineAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWebEngineAction::QQuickWebEngineAction(QObject *parent)
    self._noteCreation(QQuickWebEngineAction, lambda: Rituals.call(
        'ritual_ZN21QQuickWebEngineActionC1EP7QObject',
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

  def trigger(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineAction::trigger()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineaction.html#trigger
    """
    #  void QQuickWebEngineAction::trigger()
    self.uglySide.call('ritual_ZN21QQuickWebEngineAction7triggerEv')

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineAction::triggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#triggered
    """
    #  void QQuickWebEngineAction::triggered()
    self.uglySide.call('ritual_ZN21QQuickWebEngineAction9triggeredEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineAction::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineaction.html#enabledChanged
    """
    #  void QQuickWebEngineAction::enabledChanged()
    self.uglySide.call('ritual_ZN21QQuickWebEngineAction14enabledChangedEv')

  def d_func(self) -> Optional[QQuickWebEngineActionPrivate]:
    """
    Calls Qt's 'QQuickWebEngineActionPrivate
    *QQuickWebEngineAction::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineaction.html#d_func

    Returns
    -------

    Optional[QQuickWebEngineActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineActionPrivate *QQuickWebEngineAction::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickWebEngineAction6d_funcEv')
    from . import QQuickWebEngineActionPrivate
    return QQuickWebEngineActionPrivate._cuteAt(address)
