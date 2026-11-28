"""
Qt3DCore::QCoreAspect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qcoreaspect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoreAspect(Qt3DCore.QAbstractAspect):
  """
  The cute side of Qt's Qt3DCore::QCoreAspect: a plain Python object standing
  in front of one C++ Qt3DCore::QCoreAspect.

  It is built on the cute 'Qt3DCore::QAbstractAspect', as Qt's
  Qt3DCore::QCoreAspect is built on Qt's Qt3DCore::QAbstractAspect, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QCoreAspect that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'executeCommand', 'onRegistered', 'onUnregistered', 'onEngineStartup',
  'frameDone'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QCoreAspect::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QCoreAspect::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QCoreAspect::~QCoreAspect()': the destructor: Python
    never removes a C++ Qt3DCore::QCoreAspect.
  - Qt's 'QAspectJobPtr Qt3DCore::QCoreAspect::calculateBoundingVolumeJob()
    const': gives a type Python has no way to take yet.
  - Qt's 'const QCoreAspectPrivate *Qt3DCore::QCoreAspect::d_func() const':
    takes in Python what 'QCoreAspectPrivate
    *Qt3DCore::QCoreAspect::d_func()' takes.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DCore::QCoreAspect::jobsToExecute(qint64 time)': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QCoreAspect is created at the first use, not by
    'Qt3DCore::QCoreAspect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QCoreAspect.
  - Qt tells when it has removed the C++ Qt3DCore::QCoreAspect. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QCoreAspect that has no cute function yet,
    'calculateBoundingVolumeJob', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DCore::QCoreAspect::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#tr

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
    #  QString Qt3DCore::QCoreAspect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore11QCoreAspect2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QCoreAspect'

  #  A C++ Qt3DCore::QCoreAspect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QCoreAspect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QCoreAspect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QCoreAspect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore11QCoreAspect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    'Qt3DCore::QCoreAspect::QCoreAspect(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#QCoreAspect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QCoreAspect::QCoreAspect(QObject *parent)
    self._noteCreation(QCoreAspect, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore11QCoreAspectC1EP7QObject',
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

  def d_func(self) -> Optional[Qt3DCore.QCoreAspectPrivate]:
    """
    Calls Qt's 'QCoreAspectPrivate *Qt3DCore::QCoreAspect::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QCoreAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoreAspectPrivate *Qt3DCore::QCoreAspect::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore11QCoreAspect6d_funcEv')
    return Qt3DCore.QCoreAspectPrivate._cuteAt(address)

  @overload(QStringList)
  def executeCommand(self, args: QStringList) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::QCoreAspect::executeCommand(const
    QStringList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#executeCommand

    Parameters
    ----------

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::QCoreAspect::executeCommand(const QStringList
    #      &args)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore11QCoreAspect14executeCommandERK5QListI7QStringE',
        self._valueOf(args),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def onRegistered(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreAspect::onRegistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#onRegistered
    """
    #  void Qt3DCore::QCoreAspect::onRegistered()
    ritual = 'ritual_ZN8Qt3DCore11QCoreAspect12onRegisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore11QCoreAspect12onRegisteredEv'
    self.uglySide.call(ritual)

  def onUnregistered(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreAspect::onUnregistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#onUnregistered
    """
    #  void Qt3DCore::QCoreAspect::onUnregistered()
    ritual = 'ritual_ZN8Qt3DCore11QCoreAspect14onUnregisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore11QCoreAspect14onUnregisteredEv'
    self.uglySide.call(ritual)

  def onEngineStartup(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreAspect::onEngineStartup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#onEngineStartup
    """
    #  void Qt3DCore::QCoreAspect::onEngineStartup()
    ritual = 'ritual_ZN8Qt3DCore11QCoreAspect15onEngineStartupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore11QCoreAspect15onEngineStartupEv'
    self.uglySide.call(ritual)

  def frameDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QCoreAspect::frameDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcoreaspect.html#frameDone
    """
    #  void Qt3DCore::QCoreAspect::frameDone()
    ritual = 'ritual_ZN8Qt3DCore11QCoreAspect9frameDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore11QCoreAspect9frameDoneEv'
    self.uglySide.call(ritual)

  @staticmethod
  def calculateBoundingVolumeJob(*__, **_) -> Never:
    """
    Qt's 'QAspectJobPtr Qt3DCore::QCoreAspect::calculateBoundingVolumeJob()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QCoreAspect.calculateBoundingVolumeJob' has no cute "
        "function yet. Qt's 'QAspectJobPtr "
        "Qt3DCore::QCoreAspect::calculateBoundingVolumeJob() const': gives "
        "a type Python has no way to take yet.")
