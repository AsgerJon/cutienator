"""
Qt3DInput::QInputAspect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qinputaspect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputAspect(Qt3DCore.QAbstractAspect):
  """
  The cute side of Qt's Qt3DInput::QInputAspect: a plain Python object
  standing in front of one C++ Qt3DInput::QInputAspect.

  It is built on the cute 'Qt3DCore::QAbstractAspect', as Qt's
  Qt3DInput::QInputAspect is built on Qt's Qt3DCore::QAbstractAspect, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QInputAspect that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'createPhysicalDevice', 'availablePhysicalDevices', 'onRegistered',
  'onUnregistered', 'onEngineStartup', 'jobsDone', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QInputAspect::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QInputAspect::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QInputAspect::~QInputAspect()': the destructor: Python
    never removes a C++ Qt3DInput::QInputAspect.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DInput::QInputAspect::jobsToExecute(qint64 time)': gives a type Python
    has no way to take yet.
  - Qt's 'const QInputAspectPrivate *Qt3DInput::QInputAspect::d_func()
    const': takes in Python what 'QInputAspectPrivate
    *Qt3DInput::QInputAspect::d_func()' takes.
  - Qt's 'Qt3DInput::QInputAspect::QInputAspect(QInputAspectPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QInputAspect is created at the first use, not by
    'Qt3DInput::QInputAspect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QInputAspect.
  - Qt tells when it has removed the C++ Qt3DInput::QInputAspect. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DInput::QInputAspect::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#tr

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
    #  QString Qt3DInput::QInputAspect::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput12QInputAspect2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QInputAspect'

  #  A C++ Qt3DInput::QInputAspect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QInputAspect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QInputAspect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QInputAspect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QInputAspect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def availablePhysicalDevices(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DInput::QInputAspect::availablePhysicalDevices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QInputAspect::availablePhysicalDevices() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QInputAspect24availablePhysicalDevicesEv',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QInputAspect::QInputAspect(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#QInputAspect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QInputAspect::QInputAspect(QObject *parent)
    self._noteCreation(QInputAspect, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput12QInputAspectC1EP7QObject',
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
  def createPhysicalDevice(
      self,
      name: str,
  ) -> Optional[Qt3DInput.QAbstractPhysicalDevice]:
    """
    Calls Qt's 'QAbstractPhysicalDevice
    *Qt3DInput::QInputAspect::createPhysicalDevice(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#createPhysicalDevice

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDevice
    #      *Qt3DInput::QInputAspect::createPhysicalDevice(const QString
    #      &name)
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput12QInputAspect20createPhysicalDeviceERK7QString',
        name,
    )
    return Qt3DInput.QAbstractPhysicalDevice._cuteAt(address)

  def onRegistered(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputAspect::onRegistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#onRegistered
    """
    #  void Qt3DInput::QInputAspect::onRegistered()
    ritual = 'ritual_ZN9Qt3DInput12QInputAspect12onRegisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DInput12QInputAspect12onRegisteredEv'
    self.uglySide.call(ritual)

  def onUnregistered(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputAspect::onUnregistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#onUnregistered
    """
    #  void Qt3DInput::QInputAspect::onUnregistered()
    ritual = 'ritual_ZN9Qt3DInput12QInputAspect14onUnregisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DInput12QInputAspect14onUnregisteredEv'
    self.uglySide.call(ritual)

  def onEngineStartup(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputAspect::onEngineStartup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#onEngineStartup
    """
    #  void Qt3DInput::QInputAspect::onEngineStartup()
    ritual = 'ritual_ZN9Qt3DInput12QInputAspect15onEngineStartupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DInput12QInputAspect15onEngineStartupEv'
    self.uglySide.call(ritual)

  def jobsDone(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputAspect::jobsDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#jobsDone
    """
    #  void Qt3DInput::QInputAspect::jobsDone()
    ritual = 'ritual_ZN9Qt3DInput12QInputAspect8jobsDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DInput12QInputAspect8jobsDoneEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[Qt3DInput.QInputAspectPrivate]:
    """
    Calls Qt's 'QInputAspectPrivate *Qt3DInput::QInputAspect::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qinputaspect.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QInputAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputAspectPrivate *Qt3DInput::QInputAspect::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput12QInputAspect6d_funcEv',
    )
    return Qt3DInput.QInputAspectPrivate._cuteAt(address)
