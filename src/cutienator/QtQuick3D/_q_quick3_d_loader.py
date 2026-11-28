"""
QQuick3DLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dloader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DLoader to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlIncubator
from . import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQml import QQmlComponent, QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQmlV4Function = WAIT['QQmlV4Function']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DLoader(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DLoader: a plain Python object standing in
  front of one C++ QQuick3DLoader.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DLoader is built on
  Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DLoader that has a ritual and that Python can
  call so far, 33 names in all: 'metaObject', 'tr', 'active', 'setActive',
  'setSource', 'source', 'sourceComponent', 'setSourceComponent',
  'resetSourceComponent', 'status', 'progress', 'asynchronous',
  'setAsynchronous', 'item', 'itemChanged', 'activeChanged', 'sourceChanged',
  'sourceComponentChanged', 'statusChanged', 'progressChanged', 'loaded',
  'asynchronousChanged', 'componentComplete', 'sourceLoaded',
  'loadFromSource', 'loadFromSourceComponent', 'clear', 'load',
  'incubatorStateChanged', 'setInitialState', 'disposeInitialPropertyValues',
  'resolveSourceUrl', 'createComponent'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DLoader::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DLoader::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DLoader::~QQuick3DLoader()': the destructor: Python never
    removes a C++ QQuick3DLoader.
  - Qt's 'QV4::ReturnedValue
    QQuick3DLoader::extractInitialPropertyValues(QQmlV4FunctionPtr args, bool
    *error)': takes a number to change where it is.

  What has no ritual
  ------------------

  4 of the 44 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuick3DLoader is created at the first use, not by
    'QQuick3DLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DLoader.
  - Qt tells when it has removed the C++ QQuick3DLoader. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DLoader that has no cute function yet,
    'extractInitialPropertyValues', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DLoader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QQuick3DLoader::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQuick3DLoader::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#tr

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
    #  QString QQuick3DLoader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuick3DLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQmlV4Function)
  @overload(NoneType)
  def resolveSourceUrl(args: Optional[QQmlV4Function]) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DLoader::resolveSourceUrl(QQmlV4FunctionPtr
    args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#resolveSourceUrl

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DLoader::resolveSourceUrl(QQmlV4FunctionPtr args)
    address = Rituals.call(
        'ritual_ZN14QQuick3DLoader16resolveSourceUrlEP14QQmlV4Function',
        CuteMixin._addressOf(args),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DLoader'

  #  A C++ QQuick3DLoader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DLoader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DLoader::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DLoader10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DLoader::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#active
    """
    #  bool QQuick3DLoader::active() const
    return self.uglySide.call('ritual_ZNK14QQuick3DLoader6activeEv')

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DLoader::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DLoader::source() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DLoader6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceComponent(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuick3DLoader::sourceComponent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#sourceComponent

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuick3DLoader::sourceComponent() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DLoader15sourceComponentEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuick3DLoader::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuick3DLoader::status() const
    return QQuick3DLoader.Status(self.uglySide.call(
        'ritual_ZNK14QQuick3DLoader6statusEv',
    ))

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuick3DLoader::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#progress
    """
    #  qreal QQuick3DLoader::progress() const
    return self.uglySide.call('ritual_ZNK14QQuick3DLoader8progressEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DLoader::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#asynchronous
    """
    #  bool QQuick3DLoader::asynchronous() const
    return self.uglySide.call('ritual_ZNK14QQuick3DLoader12asynchronousEv')

  def item(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuick3DLoader::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#item

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuick3DLoader::item() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DLoader4itemEv')
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, newVal: bool) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setActive(bool newVal)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#setActive

    Parameters
    ----------

    newVal : bool
      Passed on as it is.
    """
    #  void QQuick3DLoader::setActive(bool newVal)
    self.uglySide.call('ritual_ZN14QQuick3DLoader9setActiveEb', newVal)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def setSource(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setSource(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#setSource

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DLoader::setSource(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader9setSourceEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QUrl)
  def setSource(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setSource(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#setSource

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DLoader::setSource(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader9setSourceERK4QUrl', self._valueOf(a0),
    )

  @overload(QUrl, bool)
  def setSource(self, sourceUrl: QUrl, needsClear: bool) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setSource(const QUrl &sourceUrl, bool
    needsClear)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#setSource

    Parameters
    ----------

    sourceUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    needsClear : bool
      Passed on as it is.
    """
    #  void QQuick3DLoader::setSource(const QUrl &sourceUrl, bool needsClear)
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader9setSourceERK4QUrlb',
        self._valueOf(sourceUrl), needsClear,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setSourceComponent(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setSourceComponent(QQmlComponent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#setSourceComponent

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DLoader::setSourceComponent(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader18setSourceComponentEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(bool)
  def setAsynchronous(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setAsynchronous(bool a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#setAsynchronous

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuick3DLoader::setAsynchronous(bool a)
    self.uglySide.call('ritual_ZN14QQuick3DLoader15setAsynchronousEb', a)

  @overload(QObject)
  @overload(NoneType)
  def setInitialState(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::setInitialState(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#setInitialState

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DLoader::setInitialState(QObject *obj)
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader15setInitialStateEP7QObject',
        self._addressOf(obj, 'QObject'),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DLoader::QQuick3DLoader(QQuick3DNode *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#QQuick3DLoader

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DLoader::QQuick3DLoader(QQuick3DNode *parent)
    self._noteCreation(QQuick3DLoader, lambda: Rituals.call(
        'ritual_ZN14QQuick3DLoaderC1EP12QQuick3DNode',
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

  def resetSourceComponent(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::resetSourceComponent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#resetSourceComponent
    """
    #  void QQuick3DLoader::resetSourceComponent()
    self.uglySide.call('ritual_ZN14QQuick3DLoader20resetSourceComponentEv')

  def itemChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::itemChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#itemChanged
    """
    #  void QQuick3DLoader::itemChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader11itemChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#activeChanged
    """
    #  void QQuick3DLoader::activeChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader13activeChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#sourceChanged
    """
    #  void QQuick3DLoader::sourceChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader13sourceChangedEv')

  def sourceComponentChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::sourceComponentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#sourceComponentChanged
    """
    #  void QQuick3DLoader::sourceComponentChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader22sourceComponentChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#statusChanged
    """
    #  void QQuick3DLoader::statusChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader13statusChangedEv')

  def progressChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::progressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#progressChanged
    """
    #  void QQuick3DLoader::progressChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader15progressChangedEv')

  def loaded(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::loaded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#loaded
    """
    #  void QQuick3DLoader::loaded()
    self.uglySide.call('ritual_ZN14QQuick3DLoader6loadedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#asynchronousChanged
    """
    #  void QQuick3DLoader::asynchronousChanged()
    self.uglySide.call('ritual_ZN14QQuick3DLoader19asynchronousChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#componentComplete
    """
    #  void QQuick3DLoader::componentComplete()
    ritual = 'ritual_ZN14QQuick3DLoader17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DLoader17componentCompleteEv'
    self.uglySide.call(ritual)

  def sourceLoaded(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::sourceLoaded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#sourceLoaded
    """
    #  void QQuick3DLoader::sourceLoaded()
    self.uglySide.call('ritual_ZN14QQuick3DLoader12sourceLoadedEv')

  def loadFromSource(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::loadFromSource()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#loadFromSource
    """
    #  void QQuick3DLoader::loadFromSource()
    self.uglySide.call('ritual_ZN14QQuick3DLoader14loadFromSourceEv')

  def loadFromSourceComponent(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::loadFromSourceComponent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#loadFromSourceComponent
    """
    #  void QQuick3DLoader::loadFromSourceComponent()
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader23loadFromSourceComponentEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#clear
    """
    #  void QQuick3DLoader::clear()
    self.uglySide.call('ritual_ZN14QQuick3DLoader5clearEv')

  def load(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dloader.html#load
    """
    #  void QQuick3DLoader::load()
    self.uglySide.call('ritual_ZN14QQuick3DLoader4loadEv')

  @overload(QQmlIncubator.Status)
  def incubatorStateChanged(self, status: QQmlIncubator.Status) -> None:
    """
    Calls Qt's 'void
    QQuick3DLoader::incubatorStateChanged(QQmlIncubator::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#incubatorStateChanged

    Parameters
    ----------

    status : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQuick3DLoader::incubatorStateChanged(QQmlIncubator::Status
    #      status)
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader21incubatorStateChangedEN13QQmlIncubator6'
        'StatusE',
        status.value,
    )

  def disposeInitialPropertyValues(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::disposeInitialPropertyValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#disposeInitialPropertyValues
    """
    #  void QQuick3DLoader::disposeInitialPropertyValues()
    self.uglySide.call(
        'ritual_ZN14QQuick3DLoader28disposeInitialPropertyValuesEv',
    )

  def createComponent(self) -> None:
    """
    Calls Qt's 'void QQuick3DLoader::createComponent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloader.html#createComponent
    """
    #  void QQuick3DLoader::createComponent()
    self.uglySide.call('ritual_ZN14QQuick3DLoader15createComponentEv')

  @staticmethod
  def extractInitialPropertyValues(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QQuick3DLoader::extractInitialPropertyValues(QQmlV4FunctionPtr args, bool
    *error)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuick3DLoader.extractInitialPropertyValues' has no cute function "
        "yet. Qt's 'QV4::ReturnedValue "
        "QQuick3DLoader::extractInitialPropertyValues(QQmlV4FunctionPtr "
        "args, bool *error)': takes a number to change where it is.")
