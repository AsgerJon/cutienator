"""
QQuickApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickapplication_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickApplication to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlApplication

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QStyleHints

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickApplication(QQmlApplication):
  """
  The cute side of Qt's QQuickApplication: a plain Python object standing in
  front of one C++ QQuickApplication.

  It is built on the cute 'QQmlApplication', as Qt's QQuickApplication is
  built on Qt's QQmlApplication, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickApplication that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'active',
  'layoutDirection', 'supportsMultipleWindows', 'state', 'font',
  'displayName', 'setDisplayName', 'styleHints', 'activeChanged',
  'displayNameChanged', 'layoutDirectionChanged', 'stateChanged',
  'screensChanged', 'updateScreens'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickApplication::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickApplication::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickApplication::qt_qmlMarker_singleton()': one of Qt's own
    inner workings.
  - Qt's 'QQuickApplication::~QQuickApplication()': the destructor: Python
    never removes a C++ QQuickApplication.
  - Qt's 'QQmlListProperty<QQuickScreenInfo> QQuickApplication::screens()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickApplication is created at the first use, not by
    'QQuickApplication(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickApplication.
  - Qt tells when it has removed the C++ QQuickApplication. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickApplication that has no cute function yet,
    'screens', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString QQuickApplication::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#tr

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
    #  QString QQuickApplication::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickApplication2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickApplication'

  #  A C++ QQuickApplication Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickApplication::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickApplication::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickApplication10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuickApplication::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#active
    """
    #  bool QQuickApplication::active() const
    return self.uglySide.call('ritual_ZNK17QQuickApplication6activeEv')

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickApplication::layoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickApplication::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK17QQuickApplication15layoutDirectionEv',
    ))

  def supportsMultipleWindows(self) -> bool:
    """
    Calls Qt's 'bool QQuickApplication::supportsMultipleWindows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#supportsMultipleWindows
    """
    #  bool QQuickApplication::supportsMultipleWindows() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickApplication23supportsMultipleWindowsEv',
    )

  def state(self) -> Qt.ApplicationState:
    """
    Calls Qt's 'Qt::ApplicationState QQuickApplication::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#state

    Returns
    -------

    Qt.ApplicationState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ApplicationState(number)' gives.
    """
    #  Qt::ApplicationState QQuickApplication::state() const
    return Qt.ApplicationState(self.uglySide.call(
        'ritual_ZNK17QQuickApplication5stateEv',
    ))

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickApplication::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickApplication::font() const
    address = self.uglySide.call('ritual_ZNK17QQuickApplication4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def displayName(self) -> str:
    """
    Calls Qt's 'QString QQuickApplication::displayName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#displayName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickApplication::displayName() const
    return self.uglySide.call('ritual_ZNK17QQuickApplication11displayNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDisplayName(self, displayName: str) -> None:
    """
    Calls Qt's 'void QQuickApplication::setDisplayName(const QString
    &displayName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#setDisplayName

    Parameters
    ----------

    displayName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickApplication::setDisplayName(const QString &displayName)
    self.uglySide.call(
        'ritual_ZN17QQuickApplication14setDisplayNameERK7QString',
        displayName,
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
    'QQuickApplication::QQuickApplication(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#QQuickApplication

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickApplication::QQuickApplication(QObject *parent)
    self._noteCreation(QQuickApplication, lambda: Rituals.call(
        'ritual_ZN17QQuickApplicationC1EP7QObject',
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

  def styleHints(self) -> Optional[QStyleHints]:
    """
    Calls Qt's 'QStyleHints *QQuickApplication::styleHints()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplication.html#styleHints

    Returns
    -------

    Optional[QStyleHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleHints *QQuickApplication::styleHints()
    address = self.uglySide.call(
        'ritual_ZN17QQuickApplication10styleHintsEv',
    )
    from ..QtGui import QStyleHints
    return QStyleHints._cuteAt(address)

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplication::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#activeChanged
    """
    #  void QQuickApplication::activeChanged()
    self.uglySide.call('ritual_ZN17QQuickApplication13activeChangedEv')

  def displayNameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplication::displayNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#displayNameChanged
    """
    #  void QQuickApplication::displayNameChanged()
    self.uglySide.call('ritual_ZN17QQuickApplication18displayNameChangedEv')

  def layoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplication::layoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#layoutDirectionChanged
    """
    #  void QQuickApplication::layoutDirectionChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickApplication22layoutDirectionChangedEv',
    )

  @overload(Qt.ApplicationState)
  def stateChanged(self, state: Qt.ApplicationState) -> None:
    """
    Calls Qt's 'void QQuickApplication::stateChanged(Qt::ApplicationState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#stateChanged

    Parameters
    ----------

    state : Qt.ApplicationState
      Passed on as its number.
    """
    #  void QQuickApplication::stateChanged(Qt::ApplicationState state)
    self.uglySide.call(
        'ritual_ZN17QQuickApplication12stateChangedEN2Qt16ApplicationStateE',
        state.value,
    )

  def screensChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplication::screensChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#screensChanged
    """
    #  void QQuickApplication::screensChanged()
    self.uglySide.call('ritual_ZN17QQuickApplication14screensChangedEv')

  def updateScreens(self) -> None:
    """
    Calls Qt's 'void QQuickApplication::updateScreens()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplication.html#updateScreens
    """
    #  void QQuickApplication::updateScreens()
    self.uglySide.call('ritual_ZN17QQuickApplication13updateScreensEv')

  @staticmethod
  def screens(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickScreenInfo> QQuickApplication::screens()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickApplication.screens' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickScreenInfo> QQuickApplication::screens()': "
        "gives a type Python has no way to take yet.")
