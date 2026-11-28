"""
QtTaskTree::QTaskTree binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTaskTree(QObject):
  """
  The cute side of Qt's QtTaskTree::QTaskTree: a plain Python object standing
  in front of one C++ QtTaskTree::QTaskTree.

  It is built on the cute 'QObject', as Qt's QtTaskTree::QTaskTree is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QTaskTree that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'setRecipe',
  'start', 'cancel', 'isRunning', 'runBlocking', 'asyncCount', 'taskCount',
  'progressMaximum', 'progressValue', 'started', 'done', 'asyncCountChanged',
  'progressValueChanged', 'event'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtTaskTree::QTaskTree::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QtTaskTree::QTaskTree::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtTaskTree::QTaskTree::~QTaskTree()': the destructor: Python never
    removes a C++ QtTaskTree::QTaskTree.
  - Qt's 'DoneWith QtTaskTree::QTaskTree::runBlocking(const QFuture<void>
    &future)': takes a type Python has no way to hand over yet.
  - Qt's 'DoneWith QtTaskTree::QTaskTree::runBlocking(const Group &recipe,
    const QFuture<void> &future)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QtTaskTree::QTaskTree::setupStorageHandler(const StorageBase
    &storage, const StorageBase::StorageHandler &setupHandler, const
    StorageBase::StorageHandler &doneHandler)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  7 of the 33 functions Qt declares: 3 a template; 2 not a gap; 2 the
  compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtTaskTree::QTaskTree is created at the first use, not by
    'QtTaskTree::QTaskTree(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QTaskTree.
  - Qt tells when it has removed the C++ QtTaskTree::QTaskTree. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtTaskTree::QTaskTree that has no cute function yet,
    'onStorageDone', 'onStorageSetup', 'setupStorageHandler', 'wrapHandler',
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
    Calls Qt's 'QString QtTaskTree::QTaskTree::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtasktree.html#tr

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
    #  QString QtTaskTree::QTaskTree::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QtTaskTree9QTaskTree2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QTaskTree'

  #  A C++ QtTaskTree::QTaskTree Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtTaskTree_QTaskTree'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtTaskTree::QTaskTree::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtTaskTree::QTaskTree::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree9QTaskTree10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QTaskTree::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#isRunning
    """
    #  bool QtTaskTree::QTaskTree::isRunning() const
    return self.uglySide.call('ritual_ZNK10QtTaskTree9QTaskTree9isRunningEv')

  def asyncCount(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::QTaskTree::asyncCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#asyncCount
    """
    #  qsizetype QtTaskTree::QTaskTree::asyncCount() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree9QTaskTree10asyncCountEv',
    )

  def taskCount(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::QTaskTree::taskCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#taskCount
    """
    #  qsizetype QtTaskTree::QTaskTree::taskCount() const
    return self.uglySide.call('ritual_ZNK10QtTaskTree9QTaskTree9taskCountEv')

  def progressMaximum(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::QTaskTree::progressMaximum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#progressMaximum
    """
    #  qsizetype QtTaskTree::QTaskTree::progressMaximum() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree9QTaskTree15progressMaximumEv',
    )

  def progressValue(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::QTaskTree::progressValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#progressValue
    """
    #  qsizetype QtTaskTree::QTaskTree::progressValue() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree9QTaskTree13progressValueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QtTaskTree.Group'])
  def setRecipe(self, recipe: QtTaskTree.Group) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::setRecipe(const Group &recipe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#setRecipe

    Parameters
    ----------

    recipe : QtTaskTree.Group
      Passed on as a value: Qt reads the C++ QtTaskTree::Group, which stays
      Python's own.
    """
    #  void QtTaskTree::QTaskTree::setRecipe(const Group &recipe)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree9QTaskTree9setRecipeERKNS_5GroupE',
        self._valueOf(recipe),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::QTaskTree::QTaskTree()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#QTaskTree
    """
    #  QtTaskTree::QTaskTree::QTaskTree()
    self._noteCreation(QTaskTree, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9QTaskTreeC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::QTaskTree::QTaskTree(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#QTaskTree

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtTaskTree::QTaskTree::QTaskTree(QObject *parent)
    self._noteCreation(QTaskTree, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9QTaskTreeC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(WAIT['QtTaskTree.Group'])
  @overload(WAIT['QtTaskTree.Group'], QObject)
  @overload(WAIT['QtTaskTree.Group'], NoneType)
  def __init__(
      self,
      recipe: QtTaskTree.Group,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::QTaskTree::QTaskTree(const
    Group &recipe, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#QTaskTree

    Parameters
    ----------

    recipe : QtTaskTree.Group
      Passed on as a value: Qt reads the C++ QtTaskTree::Group, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtTaskTree::QTaskTree::QTaskTree(const Group &recipe, QObject *parent)
    self._noteCreation(QTaskTree, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9QTaskTreeC1ERKNS_5GroupEP7QObject',
        self._valueOf(recipe), self._addressOf(parent, 'QObject'),
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

  def start(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtasktree.html#start
    """
    #  void QtTaskTree::QTaskTree::start()
    self.uglySide.call('ritual_ZN10QtTaskTree9QTaskTree5startEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtasktree.html#cancel
    """
    #  void QtTaskTree::QTaskTree::cancel()
    self.uglySide.call('ritual_ZN10QtTaskTree9QTaskTree6cancelEv')

  @overload()
  def runBlocking(self) -> QtTaskTree.DoneWith:
    """
    Calls Qt's 'DoneWith QtTaskTree::QTaskTree::runBlocking()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#runBlocking

    Returns
    -------

    QtTaskTree.DoneWith
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtTaskTree.DoneWith(number)' gives.
    """
    #  DoneWith QtTaskTree::QTaskTree::runBlocking()
    return QtTaskTree.DoneWith(self.uglySide.call(
        'ritual_ZN10QtTaskTree9QTaskTree11runBlockingEv',
    ))

  @staticmethod
  @overload(WAIT['QtTaskTree.Group'])
  def runBlocking(recipe: QtTaskTree.Group) -> QtTaskTree.DoneWith:
    """
    Calls Qt's 'DoneWith QtTaskTree::QTaskTree::runBlocking(const Group
    &recipe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#runBlocking

    Parameters
    ----------

    recipe : QtTaskTree.Group
      Passed on as a value: Qt reads the C++ QtTaskTree::Group, which stays
      Python's own.

    Returns
    -------

    QtTaskTree.DoneWith
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtTaskTree.DoneWith(number)' gives.
    """
    #  DoneWith QtTaskTree::QTaskTree::runBlocking(const Group &recipe)
    return QtTaskTree.DoneWith(Rituals.call(
        'ritual_ZN10QtTaskTree9QTaskTree11runBlockingERKNS_5GroupE',
        CuteMixin._valueOf(recipe),
    ))

  def started(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::started()'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtasktree.html#started
    """
    #  void QtTaskTree::QTaskTree::started()
    self.uglySide.call('ritual_ZN10QtTaskTree9QTaskTree7startedEv')

  @overload(QtTaskTree.DoneWith)
  def done(self, result: QtTaskTree.DoneWith) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::done(QtTaskTree::DoneWith
    result)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtasktree.html#done

    Parameters
    ----------

    result : QtTaskTree.DoneWith
      Passed on as its number.
    """
    #  void QtTaskTree::QTaskTree::done(QtTaskTree::DoneWith result)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree9QTaskTree4doneENS_8DoneWithE', result.value,
    )

  @overload(int)
  def asyncCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::asyncCountChanged(qsizetype
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#asyncCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QtTaskTree::QTaskTree::asyncCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree9QTaskTree17asyncCountChangedEx', count,
    )

  @overload(int)
  def progressValueChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskTree::progressValueChanged(qsizetype
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtasktree.html#progressValueChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QtTaskTree::QTaskTree::progressValueChanged(qsizetype value)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree9QTaskTree20progressValueChangedEx', value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QTaskTree::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtasktree.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtTaskTree::QTaskTree::event(QEvent *event)
    ritual = 'ritual_ZN10QtTaskTree9QTaskTree5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QtTaskTree9QTaskTree5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def onStorageDone(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::QTaskTree::onStorageDone': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QTaskTree.onStorageDone' has no cute function yet. "
        "Qt's 'QtTaskTree::QTaskTree::onStorageDone': a template: a pattern "
        "and no single function.")

  @staticmethod
  def onStorageSetup(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::QTaskTree::onStorageSetup': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QTaskTree.onStorageSetup' has no cute function yet. "
        "Qt's 'QtTaskTree::QTaskTree::onStorageSetup': a template: a "
        "pattern and no single function.")

  @staticmethod
  def setupStorageHandler(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::QTaskTree::setupStorageHandler(const StorageBase
    &storage, const StorageBase::StorageHandler &setupHandler, const
    StorageBase::StorageHandler &doneHandler)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.QTaskTree.setupStorageHandler' has no cute function "
        "yet. Qt's 'void QtTaskTree::QTaskTree::setupStorageHandler(const "
        "StorageBase &storage, const StorageBase::StorageHandler "
        "&setupHandler, const StorageBase::StorageHandler &doneHandler)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def wrapHandler(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::QTaskTree::wrapHandler': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QTaskTree.wrapHandler' has no cute function yet. Qt's "
        "'QtTaskTree::QTaskTree::wrapHandler': a template: a pattern and no "
        "single function.")
