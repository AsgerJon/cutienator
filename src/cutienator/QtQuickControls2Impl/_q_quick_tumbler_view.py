"""
QQuickTumblerView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquicktumblerview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTumblerView to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QVariant
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickPath = WAIT['QQuickPath']
  QRectF = WAIT['QRectF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTumblerView(QQuickItem):
  """
  The cute side of Qt's QQuickTumblerView: a plain Python object standing in
  front of one C++ QQuickTumblerView.

  It is built on the cute 'QQuickItem', as Qt's QQuickTumblerView is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTumblerView that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'delegate', 'setDelegate', 'path', 'setPath', 'modelChanged',
  'delegateChanged', 'pathChanged', 'geometryChange', 'componentComplete',
  'itemChange', 'view', 'createView', 'updateFlickDeceleration',
  'updateView', 'updateModel'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTumblerView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTumblerView::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickTumblerView is created at the first use, not by
    'QQuickTumblerView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTumblerView.
  - Qt tells when it has removed the C++ QQuickTumblerView. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTumblerView::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#tr

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
    #  QString QQuickTumblerView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickTumblerView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTumblerView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTumblerView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTumblerView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickTumblerView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTumblerView::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTumblerView::model() const
    address = self.uglySide.call('ritual_ZNK17QQuickTumblerView5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickTumblerView::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickTumblerView::delegate() const
    address = self.uglySide.call('ritual_ZNK17QQuickTumblerView8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def path(self) -> Optional[QQuickPath]:
    """
    Calls Qt's 'QQuickPath *QQuickTumblerView::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#path

    Returns
    -------

    Optional[QQuickPath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPath *QQuickTumblerView::path() const
    address = self.uglySide.call('ritual_ZNK17QQuickTumblerView4pathEv')
    from ..QtQuick import QQuickPath
    return QQuickPath._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::setModel(const QVariant &model)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#setModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickTumblerView::setModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN17QQuickTumblerView8setModelERK8QVariant',
        self._valueOf(model),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumblerView::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN17QQuickTumblerView11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QQuickPath)
  @overload(NoneType)
  def setPath(self, path: Optional[QQuickPath]) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::setPath(QQuickPath *path)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#setPath

    Parameters
    ----------

    path : Optional[QQuickPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumblerView::setPath(QQuickPath *path)
    self.uglySide.call(
        'ritual_ZN17QQuickTumblerView7setPathEP10QQuickPath',
        self._addressOf(path),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTumblerView::QQuickTumblerView(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerview.html#QQuickTumblerView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTumblerView::QQuickTumblerView(QQuickItem *parent)
    self._noteCreation(QQuickTumblerView, lambda: Rituals.call(
        'ritual_ZN17QQuickTumblerViewC1EP10QQuickItem',
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

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerview.html#modelChanged
    """
    #  void QQuickTumblerView::modelChanged()
    self.uglySide.call('ritual_ZN17QQuickTumblerView12modelChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerview.html#delegateChanged
    """
    #  void QQuickTumblerView::delegateChanged()
    self.uglySide.call('ritual_ZN17QQuickTumblerView15delegateChangedEv')

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::pathChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#pathChanged
    """
    #  void QQuickTumblerView::pathChanged()
    self.uglySide.call('ritual_ZN17QQuickTumblerView11pathChangedEv')

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTumblerView::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN17QQuickTumblerView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickTumblerView14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerview.html#componentComplete
    """
    #  void QQuickTumblerView::componentComplete()
    ritual = 'ritual_ZN17QQuickTumblerView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickTumblerView17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::itemChange(ItemChange change, const
    ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickTumblerView::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN17QQuickTumblerView10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickTumblerView10itemChangeEN10QQuickItem10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def view(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTumblerView::view()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#view

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTumblerView::view()
    address = self.uglySide.call('ritual_ZN17QQuickTumblerView4viewEv')
    return QQuickItem._cuteAt(address)

  def createView(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::createView()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#createView
    """
    #  void QQuickTumblerView::createView()
    self.uglySide.call('ritual_ZN17QQuickTumblerView10createViewEv')

  def updateFlickDeceleration(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::updateFlickDeceleration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerview.html#updateFlickDeceleration
    """
    #  void QQuickTumblerView::updateFlickDeceleration()
    self.uglySide.call(
        'ritual_ZN17QQuickTumblerView23updateFlickDecelerationEv',
    )

  def updateView(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::updateView()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#updateView
    """
    #  void QQuickTumblerView::updateView()
    self.uglySide.call('ritual_ZN17QQuickTumblerView10updateViewEv')

  def updateModel(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerView::updateModel()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerview.html#updateModel
    """
    #  void QQuickTumblerView::updateModel()
    self.uglySide.call('ritual_ZN17QQuickTumblerView11updateModelEv')
