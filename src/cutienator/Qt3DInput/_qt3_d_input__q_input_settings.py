"""
Qt3DInput::QInputSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qinputsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputSettings(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DInput::QInputSettings: a plain Python object
  standing in front of one C++ Qt3DInput::QInputSettings.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DInput::QInputSettings is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QInputSettings that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'eventSource',
  'setEventSource', 'eventSourceChanged', 'd_func', 'eventSourceDestroyed'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QInputSettings::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QInputSettings::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QInputSettings::~QInputSettings()': the destructor:
    Python never removes a C++ Qt3DInput::QInputSettings.
  - Qt's 'const QInputSettingsPrivate *Qt3DInput::QInputSettings::d_func()
    const': takes in Python what 'QInputSettingsPrivate
    *Qt3DInput::QInputSettings::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QInputSettings is created at the first use, not by
    'Qt3DInput::QInputSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QInputSettings.
  - Qt tells when it has removed the C++ Qt3DInput::QInputSettings. Every
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
    Calls Qt's 'QString Qt3DInput::QInputSettings::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#tr

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
    #  QString Qt3DInput::QInputSettings::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput14QInputSettings2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QInputSettings'

  #  A C++ Qt3DInput::QInputSettings Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QInputSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QInputSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QInputSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput14QInputSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def eventSource(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *Qt3DInput::QInputSettings::eventSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#eventSource

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *Qt3DInput::QInputSettings::eventSource() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput14QInputSettings11eventSourceEv',
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setEventSource(self, eventSource: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputSettings::setEventSource(QObject
    *eventSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#setEventSource

    Parameters
    ----------

    eventSource : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QInputSettings::setEventSource(QObject *eventSource)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QInputSettings14setEventSourceEP7QObject',
        self._addressOf(eventSource, 'QObject'),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QInputSettings::QInputSettings(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#QInputSettings

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QInputSettings::QInputSettings(Qt3DCore::QNode *parent)
    self._noteCreation(QInputSettings, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput14QInputSettingsC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(QObject)
  @overload(NoneType)
  def eventSourceChanged(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputSettings::eventSourceChanged(QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#eventSourceChanged

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QInputSettings::eventSourceChanged(QObject *a0)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QInputSettings18eventSourceChangedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  def d_func(self) -> Optional[Qt3DInput.QInputSettingsPrivate]:
    """
    Calls Qt's 'QInputSettingsPrivate *Qt3DInput::QInputSettings::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QInputSettingsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputSettingsPrivate *Qt3DInput::QInputSettings::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput14QInputSettings6d_funcEv',
    )
    return Qt3DInput.QInputSettingsPrivate._cuteAt(address)

  def eventSourceDestroyed(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputSettings::eventSourceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputsettings.html#eventSourceDestroyed
    """
    #  void Qt3DInput::QInputSettings::eventSourceDestroyed()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QInputSettings20eventSourceDestroyedEv',
    )
