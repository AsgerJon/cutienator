"""
QQuickHeaderViewBasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickHeaderViewBasePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickTableViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QObject, QVariant
  from . import QQuickHeaderViewBase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickHeaderViewBase = WAIT['QQuickHeaderViewBase']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickHeaderViewBasePrivate(QQuickTableViewPrivate):
  """
  The cute side of Qt's QQuickHeaderViewBasePrivate: a plain Python object
  standing in front of one C++ QQuickHeaderViewBasePrivate.

  It is built on the cute 'QQuickTableViewPrivate', as Qt's
  QQuickHeaderViewBasePrivate is built on Qt's QQuickTableViewPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickHeaderViewBasePrivate that has a ritual and
  that Python can call so far, 15 names in all: 'q_func', 'get', 'init',
  'orientation', 'setOrientation', 'modelImpl', 'setModelImpl', 'syncModel',
  'syncSyncView', 'selectionSourceModel', 'initItemCallback',
  'logicalRowIndex', 'logicalColumnIndex', 'visualRowIndex',
  'visualColumnIndex'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickHeaderViewBase *QQuickHeaderViewBasePrivate::q_func()
    const': takes in Python what 'QQuickHeaderViewBase
    *QQuickHeaderViewBasePrivate::q_func()' takes.
  - Qt's 'QQuickHeaderViewBasePrivate::~QQuickHeaderViewBasePrivate()': the
    destructor: Python never removes a C++ QQuickHeaderViewBasePrivate.
  - Qt's 'const QPointer<QQuickItem>
    QQuickHeaderViewBasePrivate::delegateItemAt(int row, int col) const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QQuickHeaderViewBasePrivate is created at the first use, not by
    'QQuickHeaderViewBasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickHeaderViewBasePrivate.
  - Each name of Qt's QQuickHeaderViewBasePrivate that has no cute function
    yet, 'delegateItemAt', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickHeaderViewBase)
  @overload(NoneType)
  def get(
      q: Optional[QQuickHeaderViewBase],
  ) -> Optional[QQuickHeaderViewBasePrivate]:
    """
    Calls Qt's 'QQuickHeaderViewBasePrivate
    *QQuickHeaderViewBasePrivate::get(QQuickHeaderViewBase *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickHeaderViewBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickHeaderViewBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickHeaderViewBasePrivate
    #      *QQuickHeaderViewBasePrivate::get(QQuickHeaderViewBase *q)
    address = Rituals.call(
        'ritual_ZN27QQuickHeaderViewBasePrivate3getEP20QQuickHeaderViewBase',
        CuteMixin._addressOf(q),
    )
    return QQuickHeaderViewBasePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHeaderViewBasePrivate'

  #  A C++ QQuickHeaderViewBasePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickHeaderViewBasePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickHeaderViewBasePrivate::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickHeaderViewBasePrivate::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK27QQuickHeaderViewBasePrivate11orientationEv',
    ))

  def modelImpl(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickHeaderViewBasePrivate::modelImpl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#modelImpl

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickHeaderViewBasePrivate::modelImpl() const
    ritual = 'ritual_ZNK27QQuickHeaderViewBasePrivate9modelImplEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QQuickHeaderViewBasePrivate9modelImplEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def logicalRowIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QQuickHeaderViewBasePrivate::logicalRowIndex(const int
    visualIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#logicalRowIndex

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QQuickHeaderViewBasePrivate::logicalRowIndex(const int
    #      visualIndex) const
    return self.uglySide.call(
        'ritual_ZNK27QQuickHeaderViewBasePrivate15logicalRowIndexEi',
        visualIndex,
    )

  @overload(int)
  def logicalColumnIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QQuickHeaderViewBasePrivate::logicalColumnIndex(const int
    visualIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QQuickHeaderViewBasePrivate::logicalColumnIndex(const int
    #      visualIndex) const
    return self.uglySide.call(
        'ritual_ZNK27QQuickHeaderViewBasePrivate18logicalColumnIndexEi',
        visualIndex,
    )

  @overload(int)
  def visualRowIndex(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QQuickHeaderViewBasePrivate::visualRowIndex(const int
    logicalIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#visualRowIndex

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QQuickHeaderViewBasePrivate::visualRowIndex(const int
    #      logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK27QQuickHeaderViewBasePrivate14visualRowIndexEi',
        logicalIndex,
    )

  @overload(int)
  def visualColumnIndex(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QQuickHeaderViewBasePrivate::visualColumnIndex(const int
    logicalIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#visualColumnIndex

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QQuickHeaderViewBasePrivate::visualColumnIndex(const int
    #      logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK27QQuickHeaderViewBasePrivate17visualColumnIndexEi',
        logicalIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QQuickHeaderViewBasePrivate::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickHeaderViewBasePrivate::setOrientation(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN27QQuickHeaderViewBasePrivate14setOrientationEN2Qt11Orien'
        'tationE',
        orientation.value,
    )

  @overload(QVariant)
  def setModelImpl(self, newModel: QVariant) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBasePrivate::setModelImpl(const QVariant
    &newModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#setModelImpl

    Parameters
    ----------

    newModel : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickHeaderViewBasePrivate::setModelImpl(const QVariant
    #      &newModel)
    ritual = (
        'ritual_ZN27QQuickHeaderViewBasePrivate12setModelImplERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickHeaderViewBasePrivate12setModelImplERK8QVar'
          'iant')
    self.uglySide.call(ritual, self._valueOf(newModel))

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
    Notes what was given, for Qt's
    'QQuickHeaderViewBasePrivate::QQuickHeaderViewBasePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html
    """
    #  QQuickHeaderViewBasePrivate::QQuickHeaderViewBasePrivate()
    self._noteCreation(QQuickHeaderViewBasePrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickHeaderViewBasePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickHeaderViewBase]:
    """
    Calls Qt's 'QQuickHeaderViewBase *QQuickHeaderViewBasePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#q_func

    Returns
    -------

    Optional[QQuickHeaderViewBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickHeaderViewBase *QQuickHeaderViewBasePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickHeaderViewBasePrivate6q_funcEv',
    )
    from . import QQuickHeaderViewBase
    return QQuickHeaderViewBase._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBasePrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#init
    """
    #  void QQuickHeaderViewBasePrivate::init()
    self.uglySide.call('ritual_ZN27QQuickHeaderViewBasePrivate4initEv')

  def syncModel(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBasePrivate::syncModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#syncModel
    """
    #  void QQuickHeaderViewBasePrivate::syncModel()
    ritual = 'ritual_ZN27QQuickHeaderViewBasePrivate9syncModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickHeaderViewBasePrivate9syncModelEv'
    self.uglySide.call(ritual)

  def syncSyncView(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBasePrivate::syncSyncView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#syncSyncView
    """
    #  void QQuickHeaderViewBasePrivate::syncSyncView()
    ritual = 'ritual_ZN27QQuickHeaderViewBasePrivate12syncSyncViewEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickHeaderViewBasePrivate12syncSyncViewEv'
    self.uglySide.call(ritual)

  def selectionSourceModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel
    *QQuickHeaderViewBasePrivate::selectionSourceModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel
    #      *QQuickHeaderViewBasePrivate::selectionSourceModel()
    ritual = 'ritual_ZN27QQuickHeaderViewBasePrivate20selectionSourceModelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickHeaderViewBasePrivate20selectionSourceModel'
          'Ev')
    address = self.uglySide.call(ritual)
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItemCallback(
      self,
      modelIndex: int,
      item: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBasePrivate::initItemCallback(int
    modelIndex, QObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbaseprivate.html#initItemCallback

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickHeaderViewBasePrivate::initItemCallback(int modelIndex,
    #      QObject *item)
    ritual = (
        'ritual_ZN27QQuickHeaderViewBasePrivate16initItemCallbackEiP7QObjec'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickHeaderViewBasePrivate16initItemCallbackEiP7'
          'QObject')
    self.uglySide.call(ritual, modelIndex, self._addressOf(item, 'QObject'))

  @staticmethod
  def delegateItemAt(*__, **_) -> Never:
    """
    Qt's 'const QPointer<QQuickItem>
    QQuickHeaderViewBasePrivate::delegateItemAt(int row, int col) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickHeaderViewBasePrivate.delegateItemAt' has no cute function "
        "yet. Qt's 'const QPointer<QQuickItem> "
        "QQuickHeaderViewBasePrivate::delegateItemAt(int row, int col) "
        "const': gives a type Python has no way to take yet.")
