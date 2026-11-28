"""
Qt3DCore::QAbstractAspect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qabstractaspect.h, Qt 6.12.0. Changes made here are lost.
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAspect(QObject):
  """
  The cute side of Qt's Qt3DCore::QAbstractAspect: a plain Python object
  standing in front of one C++ Qt3DCore::QAbstractAspect.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QAbstractAspect is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractAspect that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'dependencies', 'rootEntityId', 'unregisterBackendType', 'executeCommand',
  'onRegistered', 'onUnregistered', 'onEngineStartup', 'onEngineShutdown',
  'jobsDone', 'frameDone', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAbstractAspect::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QAbstractAspect::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QAbstractAspect::~QAbstractAspect()': the destructor:
    Python never removes a C++ Qt3DCore::QAbstractAspect.
  - Qt's 'void Qt3DCore::QAbstractAspect::scheduleSingleShotJob(const
    Qt3DCore::QAspectJobPtr &job)': takes a type Python has no way to hand
    over yet.
  - Qt's 'Qt3DCore::QAbstractAspect::QAbstractAspect(QAbstractAspectPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DCore::QAbstractAspect::registerBackendType(const
    QMetaObject &obj, const QBackendNodeMapperPtr &functor)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::vector<QAspectJobPtr>
    Qt3DCore::QAbstractAspect::jobsToExecute(qint64 time)': gives a type
    Python has no way to take yet.
  - Qt's 'const QAbstractAspectPrivate *Qt3DCore::QAbstractAspect::d_func()
    const': takes in Python what 'QAbstractAspectPrivate
    *Qt3DCore::QAbstractAspect::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractAspect is created at the first use, not by
    'Qt3DCore::QAbstractAspect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractAspect.
  - Qt tells when it has removed the C++ Qt3DCore::QAbstractAspect. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QAbstractAspect that has no cute function
    yet, 'jobsToExecute', 'registerBackendType', 'scheduleSingleShotJob',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString Qt3DCore::QAbstractAspect::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#tr

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
    #  QString Qt3DCore::QAbstractAspect::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore15QAbstractAspect2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractAspect'

  #  A C++ Qt3DCore::QAbstractAspect Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractAspect'

  #  The functions Qt calls itself that Qt3DCore::QAbstractAspect is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dependencies': (
          'QStringList Qt3DCore::QAbstractAspect::dependencies() const',
      ),
      'executeCommand': (
          'QVariant Qt3DCore::QAbstractAspect::executeCommand(const '
          'QStringList &)',
      ),
      'jobsToExecute': (
          'std::vector<QAspectJobPtr> '
          'Qt3DCore::QAbstractAspect::jobsToExecute(qint64)',
      ),
  }

  #  The functions Qt calls itself that Qt3DCore::QAbstractAspect is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'onRegistered': (
          ('_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onUnregistered': (
          ('_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onEngineStartup': (
          ('_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onEngineShutdown': (
          ('_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'jobsDone': (
          ('_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'frameDone': (
          ('_ZN8Qt3DCore15QAbstractAspect9frameDoneEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *Qt3DCore::QAbstractAspect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAbstractAspect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QAbstractAspect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dependencies(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DCore::QAbstractAspect::dependencies() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#dependencies

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DCore::QAbstractAspect::dependencies() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QAbstractAspect12dependenciesEv',
    )
    return QStringList._cuteOwning(address)

  def rootEntityId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'QNodeId Qt3DCore::QAbstractAspect::rootEntityId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#rootEntityId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  QNodeId Qt3DCore::QAbstractAspect::rootEntityId() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QAbstractAspect12rootEntityIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

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
    'Qt3DCore::QAbstractAspect::QAbstractAspect(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#QAbstractAspect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAbstractAspect::QAbstractAspect(QObject *parent)
    self._noteCreation(QAbstractAspect, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QAbstractAspectC1EP7QObject',
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

  @overload(QMetaObject)
  def unregisterBackendType(self, a0: QMetaObject) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::unregisterBackendType(const
    QMetaObject &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html

    Parameters
    ----------

    a0 : QMetaObject
      Passed on as a value: Qt reads the C++ QMetaObject, which stays
      Python's own.
    """
    #  void Qt3DCore::QAbstractAspect::unregisterBackendType(const
    #      QMetaObject &a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QAbstractAspect21unregisterBackendTypeERK11QMe'
        'taObject',
        self._valueOf(a0, 'QMetaObject'),
    )

  @overload(QStringList)
  def executeCommand(self, args: QStringList) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::QAbstractAspect::executeCommand(const
    QStringList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#executeCommand

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
    #  QVariant Qt3DCore::QAbstractAspect::executeCommand(const QStringList
    #      &args)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QAbstractAspect14executeCommandERK5QListI7QStr'
        'ingE',
        self._valueOf(args),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def onRegistered(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::onRegistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#onRegistered
    """
    #  void Qt3DCore::QAbstractAspect::onRegistered()
    ritual = 'ritual_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv'
    self.uglySide.call(ritual)

  def onUnregistered(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::onUnregistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#onUnregistered
    """
    #  void Qt3DCore::QAbstractAspect::onUnregistered()
    ritual = 'ritual_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv'
    self.uglySide.call(ritual)

  def onEngineStartup(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::onEngineStartup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#onEngineStartup
    """
    #  void Qt3DCore::QAbstractAspect::onEngineStartup()
    ritual = 'ritual_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv'
    self.uglySide.call(ritual)

  def onEngineShutdown(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::onEngineShutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#onEngineShutdown
    """
    #  void Qt3DCore::QAbstractAspect::onEngineShutdown()
    ritual = 'ritual_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv'
    self.uglySide.call(ritual)

  def jobsDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::jobsDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#jobsDone
    """
    #  void Qt3DCore::QAbstractAspect::jobsDone()
    ritual = 'ritual_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv'
    self.uglySide.call(ritual)

  def frameDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspect::frameDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#frameDone
    """
    #  void Qt3DCore::QAbstractAspect::frameDone()
    ritual = 'ritual_ZN8Qt3DCore15QAbstractAspect9frameDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore15QAbstractAspect9frameDoneEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[Qt3DCore.QAbstractAspectPrivate]:
    """
    Calls Qt's 'QAbstractAspectPrivate *Qt3DCore::QAbstractAspect::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspect.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspectPrivate *Qt3DCore::QAbstractAspect::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QAbstractAspect6d_funcEv',
    )
    return Qt3DCore.QAbstractAspectPrivate._cuteAt(address)

  @staticmethod
  def jobsToExecute(*__, **_) -> Never:
    """
    Qt's 'std::vector<QAspectJobPtr>
    Qt3DCore::QAbstractAspect::jobsToExecute(qint64 time)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspect.jobsToExecute' has no cute function yet. "
        "Qt's 'std::vector<QAspectJobPtr> "
        "Qt3DCore::QAbstractAspect::jobsToExecute(qint64 time)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def registerBackendType(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DCore::QAbstractAspect::registerBackendType(const
      QMetaObject &obj, const QBackendNodeMapperPtr &functor)': takes a type
      Python has no way to hand over yet.
    - Qt's 'Qt3DCore::QAbstractAspect::registerBackendType': a template: a
      pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspect.registerBackendType' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspect::registerBackendType(const QMetaObject "
        "&obj, const QBackendNodeMapperPtr &functor)': takes a type Python "
        "has no way to hand over yet. Qt's "
        "'Qt3DCore::QAbstractAspect::registerBackendType': a template: a "
        "pattern and no single function.")

  @staticmethod
  def scheduleSingleShotJob(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAbstractAspect::scheduleSingleShotJob(const
    Qt3DCore::QAspectJobPtr &job)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspect.scheduleSingleShotJob' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspect::scheduleSingleShotJob(const "
        "Qt3DCore::QAspectJobPtr &job)': takes a type Python has no way to "
        "hand over yet.")
