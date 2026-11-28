"""
QQuickLoaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickloader_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickLoaderPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QQmlIncubator
from . import QQuickImplicitSizeItemPrivate, QQuickLoader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRectF
  from . import QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLoaderPrivate(QQuickImplicitSizeItemPrivate):
  """
  The cute side of Qt's QQuickLoaderPrivate: a plain Python object standing
  in front of one C++ QQuickLoaderPrivate.

  It is built on the cute 'QQuickImplicitSizeItemPrivate', as Qt's
  QQuickLoaderPrivate is built on Qt's QQuickImplicitSizeItemPrivate, and has
  everything that class has. Qt's QQuickLoaderPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickLoaderPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickLoaderPrivate that has a ritual and that
  Python can call so far, 16 names in all: 'q_func', 'itemGeometryChanged',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged', 'clear', 'load',
  'incubatorStateChanged', 'setInitialState', 'disposeInitialPropertyValues',
  'computeStatus', 'updateStatus', 'createComponent', 'getImplicitWidth',
  'getImplicitHeight', '_q_sourceLoaded', '_q_updateSize'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickLoader *QQuickLoaderPrivate::q_func() const': takes in
    Python what 'QQuickLoader *QQuickLoaderPrivate::q_func()' takes.
  - Qt's 'QQuickLoaderPrivate::~QQuickLoaderPrivate()': the destructor:
    Python never removes a C++ QQuickLoaderPrivate.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'non-virtual thunk to QQuickLoaderPrivate.

  What to expect
  --------------

  - The C++ QQuickLoaderPrivate is created at the first use, not by
    'QQuickLoaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLoaderPrivate.
  - Each name of Qt's QQuickLoaderPrivate that has no cute function yet,
    '__init__', 'initResize', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLoaderPrivate'

  #  A C++ QQuickLoaderPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLoaderPrivate'

  #  The functions Qt calls itself that QQuickLoaderPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuickItem20QQ'
           'uickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10QQuickIte'
           'm',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP10QQuickIt'
           'em',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def computeStatus(self) -> QQuickLoader.Status:
    """
    Calls Qt's 'QQuickLoader::Status QQuickLoaderPrivate::computeStatus()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#computeStatus

    Returns
    -------

    QQuickLoader.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickLoader.Status(number)' gives.
    """
    #  QQuickLoader::Status QQuickLoaderPrivate::computeStatus() const
    return QQuickLoader.Status(self.uglySide.call(
        'ritual_ZNK19QQuickLoaderPrivate13computeStatusEv',
    ))

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickLoaderPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#getImplicitWidth
    """
    #  qreal QQuickLoaderPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK19QQuickLoaderPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickLoaderPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def getImplicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickLoaderPrivate::getImplicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#getImplicitHeight
    """
    #  qreal QQuickLoaderPrivate::getImplicitHeight() const
    ritual = 'ritual_ZNK19QQuickLoaderPrivate17getImplicitHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickLoaderPrivate17getImplicitHeightEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setInitialState(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::setInitialState(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#setInitialState

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLoaderPrivate::setInitialState(QObject *o)
    self.uglySide.call(
        'ritual_ZN19QQuickLoaderPrivate15setInitialStateEP7QObject',
        self._addressOf(o, 'QObject'),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickLoaderPrivate::QQuickLoaderPrivate()': leans on 'non-virtual
    thunk to QQuickLoaderPrivate::itemGeometryChanged(QQuickItem*,
    QQuickGeometryChange, QRectF const&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLoaderPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickLoaderPrivate::QQuickLoaderPrivate()': leans on "
        "'non-virtual thunk to "
        "QQuickLoaderPrivate::itemGeometryChanged(QQuickItem*, "
        "QQuickGeometryChange, QRectF const&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def q_func(self) -> Optional[QQuickLoader]:
    """
    Calls Qt's 'QQuickLoader *QQuickLoaderPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloaderprivate.html#q_func

    Returns
    -------

    Optional[QQuickLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLoader *QQuickLoaderPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QQuickLoaderPrivate6q_funcEv')
    return QQuickLoader._cuteAt(address)

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      oldGeometry: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickLoaderPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuickItem2'
        '0QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuic'
          'kItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change),
        self._valueOf(oldGeometry),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::itemImplicitWidthChanged(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLoaderPrivate::itemImplicitWidthChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10QQuick'
        'Item')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10'
          'QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLoaderPrivate::itemImplicitHeightChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#itemImplicitHeightChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLoaderPrivate::itemImplicitHeightChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP10QQuic'
        'kItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP1'
          '0QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloaderprivate.html#clear
    """
    #  void QQuickLoaderPrivate::clear()
    self.uglySide.call('ritual_ZN19QQuickLoaderPrivate5clearEv')

  def load(self) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickloaderprivate.html#load
    """
    #  void QQuickLoaderPrivate::load()
    self.uglySide.call('ritual_ZN19QQuickLoaderPrivate4loadEv')

  @overload(QQmlIncubator.Status)
  def incubatorStateChanged(self, status: QQmlIncubator.Status) -> None:
    """
    Calls Qt's 'void
    QQuickLoaderPrivate::incubatorStateChanged(QQmlIncubator::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#incubatorStateChanged

    Parameters
    ----------

    status : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQuickLoaderPrivate::incubatorStateChanged(QQmlIncubator::Status
    #      status)
    self.uglySide.call(
        'ritual_ZN19QQuickLoaderPrivate21incubatorStateChangedEN13QQmlIncub'
        'ator6StatusE',
        status.value,
    )

  def disposeInitialPropertyValues(self) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::disposeInitialPropertyValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html
    """
    #  void QQuickLoaderPrivate::disposeInitialPropertyValues()
    self.uglySide.call(
        'ritual_ZN19QQuickLoaderPrivate28disposeInitialPropertyValuesEv',
    )

  def updateStatus(self) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::updateStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#updateStatus
    """
    #  void QQuickLoaderPrivate::updateStatus()
    self.uglySide.call('ritual_ZN19QQuickLoaderPrivate12updateStatusEv')

  def createComponent(self) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::createComponent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#createComponent
    """
    #  void QQuickLoaderPrivate::createComponent()
    self.uglySide.call('ritual_ZN19QQuickLoaderPrivate15createComponentEv')

  def _q_sourceLoaded(self) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::_q_sourceLoaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#_q_sourceLoaded
    """
    #  void QQuickLoaderPrivate::_q_sourceLoaded()
    self.uglySide.call('ritual_ZN19QQuickLoaderPrivate15_q_sourceLoadedEv')

  @overload()
  @overload(bool)
  def _q_updateSize(self, loaderGeometryChanged: bool = True) -> None:
    """
    Calls Qt's 'void QQuickLoaderPrivate::_q_updateSize(bool
    loaderGeometryChanged)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderprivate.html#_q_updateSize

    Parameters
    ----------

    loaderGeometryChanged : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickLoaderPrivate::_q_updateSize(bool loaderGeometryChanged)
    self.uglySide.call(
        'ritual_ZN19QQuickLoaderPrivate13_q_updateSizeEb',
        loaderGeometryChanged,
    )

  @staticmethod
  def initResize(*__, **_) -> Never:
    """
    Qt's 'void QQuickLoaderPrivate::initResize()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'watchedChanges'.
    """
    raise NotImplementedError(
        "'QQuickLoaderPrivate.initResize' has no cute function yet. Qt's "
        "'void QQuickLoaderPrivate::initResize()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'watchedChanges'.")
