"""Rituals opens cutienator's own shared object and runs its rituals."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import glob
import os
from typing import TYPE_CHECKING

from . import Build, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Paths = Tuple[str, ...]


class Rituals:
  """
  Runs the rituals of cutienator's own shared object. Everything is
  called on the class, since a program has one such shared object.

    Rituals.build()        # after a ritual file changed
    Rituals.call('ritual_ZNK7QObject6parentEv', address)  # run one

  Terms
  -----

  - A ritual is one function of ours that Python can call, and that
    calls one Qt function. It is named 'ritual' followed by the
    compiler's own name for that Qt function, which has the types it
    takes packed into it: 'ritual_ZNK7QObject6parentEv' calls
    'QObject::parent()'. 'Declaration.getRitualName' gives the name.
  - A ritual file is a C++ file holding rituals, in the ritual folder.
  - The target file is the shared object built from the ritual files.

  You provide
  -----------

  Nothing at run time. To add rituals, add a ritual file to the ritual
  folder and list each ritual in '__type_signatures__' below, then call
  'build'.

  Found for you
  -------------

  - 'getRitualFolder': the folder 'rituals' beside this module.
  - 'getRitualFiles': every C++ file in that folder.
  - 'getTargetFile': 'libcutienator.so' in that folder.
  - 'getQtSharedObjects': the Qt shared objects the rituals call into.

  What to expect
  --------------

  - Nothing is compiled unless 'build' is called. 'call' refuses to run
    when the target file is missing, or older than a ritual file.
  - The target file is opened at the first 'call', once.
  - A ritual that is not listed in '__type_signatures__', or that the
    target file does not offer, raises 'LookupError' naming it.
  - A wrong argument to a ritual is not caught here. C++ takes what it is
    given, and a wrong address ends the whole program.

  This class stands in for the metaclass that is planned to collect the
  shared objects.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The type of what comes back from each ritual, then of what goes into
  #  it. This says for Python what the ritual files say in C++, and the
  #  two must agree.
  #
  #  'ctypes.c_void_p' means an int that is 8 bytes wide, and nothing
  #  more. It checks nothing and knows nothing of what the number is
  #  for. Every address crosses as one. 'None' in the first place means
  #  that nothing comes back.
  #
  #  The rows below say again what 'RitualGenerator' wrote into the ritual
  #  files 'q_object.cpp', 'q_meta_object.cpp' and 'q_event.cpp': every
  #  ritual of the three, also those no cute class calls yet, since the
  #  target file offers them all and each one offered has to be listed.
  #  A bool crosses as 'c_bool', a whole number and an enum as 'c_int',
  #  text as 'c_char_p'.
  __type_signatures__ = {
      #  const QMetaObject *QObject::metaObject() const
      'ritual_ZNK7QObject10metaObjectEv': (
          ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  QObject::QObject(QObject *parent)
      'ritual_ZN7QObjectC1EPS_': (ctypes.c_void_p, ctypes.c_void_p),
      #  QObject::~QObject()
      'ritual_ZN7QObjectD1Ev': (None, ctypes.c_void_p),
      #  bool QObject::event(QEvent *event)
      'ritual_ZN7QObject5eventEP6QEvent': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  bool QObject::eventFilter(QObject *watched, QEvent *event)
      'ritual_ZN7QObject11eventFilterEPS_P6QEvent': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  bool QObject::isWidgetType() const
      'ritual_ZNK7QObject12isWidgetTypeEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  bool QObject::isWindowType() const
      'ritual_ZNK7QObject12isWindowTypeEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  bool QObject::isQuickItemType() const
      'ritual_ZNK7QObject15isQuickItemTypeEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  bool QObject::isQmlExposed() const
      'ritual_ZNK7QObject12isQmlExposedEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  bool QObject::signalsBlocked() const
      'ritual_ZNK7QObject14signalsBlockedEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  bool QObject::blockSignals(bool b)
      'ritual_ZN7QObject12blockSignalsEb': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_bool,
      ),
      #  QThread *QObject::thread() const
      'ritual_ZNK7QObject6threadEv': (ctypes.c_void_p, ctypes.c_void_p),
      #  int QObject::startTimer(int interval, Qt::TimerType timerType)
      'ritual_ZN7QObject10startTimerEiN2Qt9TimerTypeE': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int,
      ),
      #  void QObject::killTimer(int id)
      'ritual_ZN7QObject9killTimerEi': (
          None, ctypes.c_void_p, ctypes.c_int,
      ),
      #  void QObject::killTimer(Qt::TimerId id)
      'ritual_ZN7QObject9killTimerEN2Qt7TimerIdE': (
          None, ctypes.c_void_p, ctypes.c_int,
      ),
      #  void QObject::setParent(QObject *parent)
      'ritual_ZN7QObject9setParentEPS_': (
          None, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  void QObject::installEventFilter(QObject *filterObj)
      'ritual_ZN7QObject18installEventFilterEPS_': (
          None, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  void QObject::removeEventFilter(QObject *obj)
      'ritual_ZN7QObject17removeEventFilterEPS_': (
          None, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  bool QObject::disconnect(const QObject *sender, const char *signal,
      #      const QObject *receiver, const char *member)
      'ritual_ZN7QObject10disconnectEPKS_PKcS1_S3_': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p,
          ctypes.c_char_p,
      ),
      #  bool QObject::disconnect(const char *signal,
      #      const QObject *receiver, const char *member) const
      'ritual_ZNK7QObject10disconnectEPKcPKS_S1_': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p,
          ctypes.c_char_p,
      ),
      #  bool QObject::disconnect(const QObject *receiver,
      #      const char *member) const
      'ritual_ZNK7QObject10disconnectEPKS_PKc': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  void QObject::dumpObjectTree() const
      'ritual_ZNK7QObject14dumpObjectTreeEv': (None, ctypes.c_void_p),
      #  void QObject::dumpObjectInfo() const
      'ritual_ZNK7QObject14dumpObjectInfoEv': (None, ctypes.c_void_p),
      #  QBindingStorage *QObject::bindingStorage()
      'ritual_ZN7QObject14bindingStorageEv': (
          ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  const QBindingStorage *QObject::bindingStorage() const
      'ritual_ZNK7QObject14bindingStorageEv': (
          ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  QObject *QObject::parent() const
      'ritual_ZNK7QObject6parentEv': (ctypes.c_void_p, ctypes.c_void_p),
      #  bool QObject::inherits(const char *classname) const
      'ritual_ZNK7QObject8inheritsEPKc': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  void QObject::deleteLater()
      'ritual_ZN7QObject11deleteLaterEv': (None, ctypes.c_void_p),
      #  const char *QMetaObject::className() const
      'ritual_ZNK11QMetaObject9classNameEv': (
          ctypes.c_char_p, ctypes.c_void_p,
      ),
      #  const QMetaObject *QMetaObject::superClass() const
      'ritual_ZNK11QMetaObject10superClassEv': (
          ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  bool QMetaObject::inherits(const QMetaObject *metaObject) const
      'ritual_ZNK11QMetaObject8inheritsEPKS_': (
          ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  QObject *QMetaObject::cast(QObject *obj) const
      'ritual_ZNK11QMetaObject4castEP7QObject': (
          ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  const QObject *QMetaObject::cast(const QObject *obj) const
      'ritual_ZNK11QMetaObject4castEPK7QObject': (
          ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
      ),
      #  int QMetaObject::methodOffset() const
      'ritual_ZNK11QMetaObject12methodOffsetEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::enumeratorOffset() const
      'ritual_ZNK11QMetaObject16enumeratorOffsetEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::propertyOffset() const
      'ritual_ZNK11QMetaObject14propertyOffsetEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::classInfoOffset() const
      'ritual_ZNK11QMetaObject15classInfoOffsetEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::constructorCount() const
      'ritual_ZNK11QMetaObject16constructorCountEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::methodCount() const
      'ritual_ZNK11QMetaObject11methodCountEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::enumeratorCount() const
      'ritual_ZNK11QMetaObject15enumeratorCountEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::propertyCount() const
      'ritual_ZNK11QMetaObject13propertyCountEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::classInfoCount() const
      'ritual_ZNK11QMetaObject14classInfoCountEv': (
          ctypes.c_int, ctypes.c_void_p,
      ),
      #  int QMetaObject::indexOfConstructor(const char *constructor) const
      'ritual_ZNK11QMetaObject18indexOfConstructorEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  int QMetaObject::indexOfMethod(const char *method) const
      'ritual_ZNK11QMetaObject13indexOfMethodEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  int QMetaObject::indexOfSignal(const char *signal) const
      'ritual_ZNK11QMetaObject13indexOfSignalEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  int QMetaObject::indexOfSlot(const char *slot) const
      'ritual_ZNK11QMetaObject11indexOfSlotEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  int QMetaObject::indexOfEnumerator(const char *name) const
      'ritual_ZNK11QMetaObject17indexOfEnumeratorEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  int QMetaObject::indexOfProperty(const char *name) const
      'ritual_ZNK11QMetaObject15indexOfPropertyEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  int QMetaObject::indexOfClassInfo(const char *name) const
      'ritual_ZNK11QMetaObject16indexOfClassInfoEPKc': (
          ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p,
      ),
      #  bool QMetaObject::checkConnectArgs(const char *signal,
      #      const char *method)
      'ritual_ZN11QMetaObject16checkConnectArgsEPKcS1_': (
          ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p,
      ),
      #  bool QMetaObject::disconnect(const QObject *sender,
      #      int signal_index, const QObject *receiver, int method_index)
      'ritual_ZN11QMetaObject10disconnectEPK7QObjectiS2_i': (
          ctypes.c_bool, ctypes.c_void_p,
          ctypes.c_int, ctypes.c_void_p, ctypes.c_int,
      ),
      #  bool QMetaObject::disconnectOne(const QObject *sender,
      #      int signal_index, const QObject *receiver, int method_index)
      'ritual_ZN11QMetaObject13disconnectOneEPK7QObjectiS2_i': (
          ctypes.c_bool, ctypes.c_void_p,
          ctypes.c_int, ctypes.c_void_p, ctypes.c_int,
      ),
      #  void QMetaObject::connectSlotsByName(QObject *o)
      'ritual_ZN11QMetaObject18connectSlotsByNameEP7QObject': (
          None, ctypes.c_void_p,
      ),
      #  QEvent::QEvent(Type type)
      'ritual_ZN6QEventC1ENS_4TypeE': (ctypes.c_void_p, ctypes.c_int),
      #  QEvent::~QEvent()
      'ritual_ZN6QEventD1Ev': (None, ctypes.c_void_p),
      #  Type QEvent::type() const
      'ritual_ZNK6QEvent4typeEv': (ctypes.c_int, ctypes.c_void_p),
      #  bool QEvent::isAccepted() const
      'ritual_ZNK6QEvent10isAcceptedEv': (ctypes.c_bool, ctypes.c_void_p),
      #  void QEvent::accept()
      'ritual_ZN6QEvent6acceptEv': (None, ctypes.c_void_p),
      #  void QEvent::ignore()
      'ritual_ZN6QEvent6ignoreEv': (None, ctypes.c_void_p),
      #  bool QEvent::spontaneous() const
      'ritual_ZNK6QEvent11spontaneousEv': (ctypes.c_bool, ctypes.c_void_p),
      #  void QEvent::setAccepted(bool accepted)
      'ritual_ZN6QEvent11setAcceptedEb': (
          None, ctypes.c_void_p, ctypes.c_bool,
      ),
      #  bool QEvent::isInputEvent() const
      'ritual_ZNK6QEvent12isInputEventEv': (ctypes.c_bool, ctypes.c_void_p),
      #  bool QEvent::isPointerEvent() const
      'ritual_ZNK6QEvent14isPointerEventEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  bool QEvent::isSinglePointEvent() const
      'ritual_ZNK6QEvent18isSinglePointEventEv': (
          ctypes.c_bool, ctypes.c_void_p,
      ),
      #  int QEvent::registerEventType(int hint)
      'ritual_ZN6QEvent17registerEventTypeEi': (ctypes.c_int, ctypes.c_int),
      #  QEvent *QEvent::clone() const
      'ritual_ZNK6QEvent5cloneEv': (ctypes.c_void_p, ctypes.c_void_p),
  }  # type: Dict[str, Tuple[Any, ...]]

  #  The parts of Qt the rituals call into. 'System' knows the file of
  #  each part on the system Python runs on.
  __qt_parts__ = ('QtCore',)

  #  The opened target file, or None until the first call.
  __opened_target__ = None  # type: Optional[ctypes.CDLL]

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def getRitualFolder(cls) -> str:
    """
    Gives the folder holding the ritual files and the target file.

    Found for you: it is the folder 'rituals' beside this module.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, 'rituals')

  @classmethod
  def getRitualFiles(cls) -> Paths:
    """
    Gives the ritual files that 'build' compiles.

    Found for you: every file ending in '.cpp' in the ritual folder, in
    alphabetical order. Putting a file there is all it takes.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths.
    """
    pattern = os.path.join(cls.getRitualFolder(), '*.cpp')
    return (*sorted(glob.glob(pattern)),)

  @classmethod
  def getTargetFile(cls) -> str:
    """
    Gives the path of cutienator's own shared object.

    Found for you: 'libcutienator.so' in the ritual folder. Having the
    path does not mean the file is there; 'build' makes it.
    """
    return os.path.join(cls.getRitualFolder(), 'libcutienator.so')

  @classmethod
  def getQtSharedObjects(cls) -> Paths:
    """
    Gives the Qt shared objects the rituals call into.

    Found for you: one file for each part of Qt in '__qt_parts__', in
    the folder where Qt keeps its shared objects. 'System' gives the
    name the file has on the system Python runs on, which on Linux is
    'libQt6Core.so.6' for 'QtCore'.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths.
    """
    folder = Build.getQtSharedObjectFolder()
    system = System.getHere()
    names = (*(system.getQtFileName(part) for part in cls.__qt_parts__),)
    return (*(os.path.join(folder, name) for name in names),)

  @classmethod
  def getRitualNames(cls) -> Tuple[str, ...]:
    """Gives the name of every ritual listed in '__type_signatures__'."""
    return (*cls.__type_signatures__,)

  @classmethod
  def isStale(cls) -> bool:
    """
    Says whether 'build' has to be called before any ritual can run.

    Returns
    -------

    bool
      True when the target file is missing, or when a ritual file was
      changed after the target file was made.
    """
    target = cls.getTargetFile()
    if not os.path.isfile(target):
      return True
    made = os.path.getmtime(target)
    for ritualFile in cls.getRitualFiles():
      if os.path.getmtime(ritualFile) > made:
        return True
    return False

  @classmethod
  def _createOpened(cls) -> None:
    """Opens the target file and readies every listed ritual."""
    target = cls.getTargetFile()
    if cls.isStale():
      infoSpec = """The shared object '%s' is missing, or older than a
      ritual file. Call 'Rituals.build()' first."""
      raise FileNotFoundError(' '.join((infoSpec % target).split()))
    System.getHere().prepareOpening()
    opened = ctypes.CDLL(target)
    for name, (gives, *takes) in cls.__type_signatures__.items():
      try:
        ritual = getattr(opened, name)
      except AttributeError as attributeError:
        infoSpec = """The ritual '%s' is listed in 'Rituals', but '%s'
        does not offer it. No ritual file defines it."""
        info = ' '.join((infoSpec % (name, target)).split())
        raise LookupError(info) from attributeError
      ritual.restype = gives
      ritual.argtypes = takes
    cls.__opened_target__ = opened

  @classmethod
  def getOpened(cls, **kwargs) -> ctypes.CDLL:
    """
    Gives the opened target file.

    Found for you: it is opened at the first call and kept. You pass
    nothing; the keyword is for the method's own use. 'call' is the
    usual way in, and this is here for what 'call' does not cover.

    Raises
    ------

    FileNotFoundError
      The target file is missing, or older than a ritual file.

    LookupError
      A listed ritual is not offered by the target file.
    """
    if cls.__opened_target__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createOpened()
      return cls.getOpened(_recursion=True)
    return cls.__opened_target__

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

  @classmethod
  def build(cls) -> str:
    """
    Compiles every ritual file into the target file.

    Call it after adding or changing a ritual file, in a Python that has
    not run a ritual yet: a shared object that is already open cannot be
    swapped for a new one. It takes one to three seconds per ritual file.

    Returns
    -------

    str
      The full path of the target file, which now exists.

    Raises
    ------

    RuntimeError
      The target file is already open in this Python, or 'clang++' refused
      a ritual file; its own message is then included.

    FileNotFoundError
      There is no ritual file, or 'clang++' or 'qmake6' is not installed.
    """
    if cls.__opened_target__ is not None:
      infoSpec = """The shared object is already open in this Python and
      cannot be swapped. Build in a Python that has run no ritual."""
      raise RuntimeError(' '.join(infoSpec.split()))
    ritualFiles = cls.getRitualFiles()
    if not ritualFiles:
      infoSpec = """There is no ritual file in '%s'."""
      raise FileNotFoundError(infoSpec % cls.getRitualFolder())
    build = Build()
    build.setRitualFiles(*ritualFiles)
    build.setTargetFile(cls.getTargetFile())
    build.setQtSharedObjects(*cls.getQtSharedObjects())
    return build.run()

  @classmethod
  def call(cls, name: str, *args: Any) -> Any:
    """
    Runs one ritual and gives what comes back.

    Parameters
    ----------

    name : str
      The name of the ritual, as 'Declaration.getRitualName' gives
      it: 'ritual_ZNK7QObject6parentEv'. It must be listed in
      '__type_signatures__'.

    *args : Any
      What goes into the ritual, in the order the ritual file declares.
      For a ritual on an object, the address of the object comes first.
      An address is an 'int', or 'None' for nowhere.

    Returns
    -------

    Any
      What the ritual returns. An address comes back as an 'int', or as
      'None' when C++ answered nowhere.

    Raises
    ------

    LookupError
      No ritual of that name is listed.

    FileNotFoundError
      The target file is missing, or older than a ritual file.
    """
    if name not in cls.__type_signatures__:
      infoSpec = """No ritual named '%s' is listed in 'Rituals'. The
      listed ones are: %s."""
      listed = ', '.join(cls.__type_signatures__)
      raise LookupError(' '.join((infoSpec % (name, listed)).split()))
    return getattr(cls.getOpened(), name)(*args)
