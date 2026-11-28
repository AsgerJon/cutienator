"""
QQuickLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickloader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickLoader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickImplicitSizeItem, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QUrl
  from ..QtQml import QJSValue, QQmlComponent
  from . import QQuickLoaderPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLoader(QQuickImplicitSizeItem):
  """
  The cute side of Qt's QQuickLoader: a plain Python object standing in front
  of one C++ QQuickLoader.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's QQuickLoader is
  built on Qt's QQuickImplicitSizeItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLoader that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'tr', 'active', 'setActive',
  'setSource', 'source', 'setSourceWithoutResolve', 'sourceComponent',
  'setSourceComponent', 'resetSourceComponent', 'status', 'progress',
  'asynchronous', 'setAsynchronous', 'item', 'itemChanged', 'activeChanged',
  'sourceChanged', 'sourceComponentChanged', 'statusChanged',
  'progressChanged', 'loaded', 'asynchronousChanged', 'geometryChange',
  'componentComplete', 'itemChange', 'setSourceUrlHelper', 'loadFromSource',
  'loadFromSourceComponent', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLoader::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickLoader::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickLoader::~QQuickLoader()': the destructor: Python never
    removes a C++ QQuickLoader.
  - Qt's 'const QQuickLoaderPrivate *QQuickLoader::d_func() const': takes in
    Python what 'QQuickLoaderPrivate *QQuickLoader::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickLoader is created at the first use, not by
    'QQuickLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLoader.
  - Qt tells when it has removed the C++ QQuickLoader. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickLoader, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QQuickLoader::Status' of Qt, with the 4 names Qt gives in it.
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
    Calls Qt's 'QString QQuickLoader::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#tr

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
    #  QString QQuickLoader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLoader'

  #  A C++ QQuickLoader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLoader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLoader::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickLoader10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuickLoader::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#active
    """
    #  bool QQuickLoader::active() const
    return self.uglySide.call('ritual_ZNK12QQuickLoader6activeEv')

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLoader::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLoader::source() const
    address = self.uglySide.call('ritual_ZNK12QQuickLoader6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceComponent(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickLoader::sourceComponent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#sourceComponent

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickLoader::sourceComponent() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickLoader15sourceComponentEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickLoader::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickLoader::status() const
    return QQuickLoader.Status(self.uglySide.call(
        'ritual_ZNK12QQuickLoader6statusEv',
    ))

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickLoader::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#progress
    """
    #  qreal QQuickLoader::progress() const
    return self.uglySide.call('ritual_ZNK12QQuickLoader8progressEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool QQuickLoader::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#asynchronous
    """
    #  bool QQuickLoader::asynchronous() const
    return self.uglySide.call('ritual_ZNK12QQuickLoader12asynchronousEv')

  def item(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickLoader::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#item

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickLoader::item() const
    address = self.uglySide.call('ritual_ZNK12QQuickLoader4itemEv')
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, newVal: bool) -> None:
    """
    Calls Qt's 'void QQuickLoader::setActive(bool newVal)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#setActive

    Parameters
    ----------

    newVal : bool
      Passed on as it is.
    """
    #  void QQuickLoader::setActive(bool newVal)
    self.uglySide.call('ritual_ZN12QQuickLoader9setActiveEb', newVal)

  @overload(QUrl, QJSValue)
  def setSource(self, source: QUrl, initialProperties: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickLoader::setSource(const QUrl &source, QJSValue
    initialProperties)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    initialProperties : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickLoader::setSource(const QUrl &source, QJSValue
    #      initialProperties)
    self.uglySide.call(
        'ritual_ZN12QQuickLoader9setSourceERK4QUrl8QJSValue',
        self._valueOf(source), self._valueOf(initialProperties),
    )

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickLoader::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickLoader::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN12QQuickLoader9setSourceERK4QUrl', self._valueOf(source),
    )

  @overload(QUrl, bool)
  def setSource(self, sourceUrl: QUrl, needsClear: bool) -> None:
    """
    Calls Qt's 'void QQuickLoader::setSource(const QUrl &sourceUrl, bool
    needsClear)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#setSource

    Parameters
    ----------

    sourceUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    needsClear : bool
      Passed on as it is.
    """
    #  void QQuickLoader::setSource(const QUrl &sourceUrl, bool needsClear)
    self.uglySide.call(
        'ritual_ZN12QQuickLoader9setSourceERK4QUrlb',
        self._valueOf(sourceUrl), needsClear,
    )

  @overload(QUrl)
  def setSourceWithoutResolve(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickLoader::setSourceWithoutResolve(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#setSourceWithoutResolve

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickLoader::setSourceWithoutResolve(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN12QQuickLoader23setSourceWithoutResolveERK4QUrl',
        self._valueOf(source),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setSourceComponent(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickLoader::setSourceComponent(QQmlComponent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#setSourceComponent

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLoader::setSourceComponent(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN12QQuickLoader18setSourceComponentEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(bool)
  def setAsynchronous(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuickLoader::setAsynchronous(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#setAsynchronous

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuickLoader::setAsynchronous(bool a)
    self.uglySide.call('ritual_ZN12QQuickLoader15setAsynchronousEb', a)

  @overload(QUrl)
  def setSourceUrlHelper(self, unresolvedUrl: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLoader::setSourceUrlHelper(const QUrl
    &unresolvedUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#setSourceUrlHelper

    Parameters
    ----------

    unresolvedUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLoader::setSourceUrlHelper(const QUrl &unresolvedUrl)
    address = self.uglySide.call(
        'ritual_ZN12QQuickLoader18setSourceUrlHelperERK4QUrl',
        self._valueOf(unresolvedUrl),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickLoader::QQuickLoader(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#QQuickLoader

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickLoader::QQuickLoader(QQuickItem *parent)
    self._noteCreation(QQuickLoader, lambda: Rituals.call(
        'ritual_ZN12QQuickLoaderC1EP10QQuickItem', self._addressOf(parent),
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
    Calls Qt's 'void QQuickLoader::resetSourceComponent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#resetSourceComponent
    """
    #  void QQuickLoader::resetSourceComponent()
    self.uglySide.call('ritual_ZN12QQuickLoader20resetSourceComponentEv')

  def itemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::itemChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#itemChanged
    """
    #  void QQuickLoader::itemChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader11itemChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#activeChanged
    """
    #  void QQuickLoader::activeChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader13activeChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#sourceChanged
    """
    #  void QQuickLoader::sourceChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader13sourceChangedEv')

  def sourceComponentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::sourceComponentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#sourceComponentChanged
    """
    #  void QQuickLoader::sourceComponentChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader22sourceComponentChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#statusChanged
    """
    #  void QQuickLoader::statusChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader13statusChangedEv')

  def progressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::progressChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#progressChanged
    """
    #  void QQuickLoader::progressChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader15progressChangedEv')

  def loaded(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::loaded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#loaded
    """
    #  void QQuickLoader::loaded()
    self.uglySide.call('ritual_ZN12QQuickLoader6loadedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#asynchronousChanged
    """
    #  void QQuickLoader::asynchronousChanged()
    self.uglySide.call('ritual_ZN12QQuickLoader19asynchronousChangedEv')

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickLoader::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickLoader::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN12QQuickLoader14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLoader14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#componentComplete
    """
    #  void QQuickLoader::componentComplete()
    ritual = 'ritual_ZN12QQuickLoader17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLoader17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickLoader::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickLoader::itemChange(ItemChange change, const ItemChangeData
    #      &value)
    ritual = (
        'ritual_ZN12QQuickLoader10itemChangeEN10QQuickItem10ItemChangeERKNS'
        '0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickLoader10itemChangeEN10QQuickItem10ItemChang'
          'eERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def loadFromSource(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::loadFromSource()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#loadFromSource
    """
    #  void QQuickLoader::loadFromSource()
    self.uglySide.call('ritual_ZN12QQuickLoader14loadFromSourceEv')

  def loadFromSourceComponent(self) -> None:
    """
    Calls Qt's 'void QQuickLoader::loadFromSourceComponent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloader.html#loadFromSourceComponent
    """
    #  void QQuickLoader::loadFromSourceComponent()
    self.uglySide.call('ritual_ZN12QQuickLoader23loadFromSourceComponentEv')

  def d_func(self) -> Optional[QQuickLoaderPrivate]:
    """
    Calls Qt's 'QQuickLoaderPrivate *QQuickLoader::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloader.html#d_func

    Returns
    -------

    Optional[QQuickLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLoaderPrivate *QQuickLoader::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickLoader6d_funcEv')
    from . import QQuickLoaderPrivate
    return QQuickLoaderPrivate._cuteAt(address)
