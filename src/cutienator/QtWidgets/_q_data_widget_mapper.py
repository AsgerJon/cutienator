"""
QDataWidgetMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdatawidgetmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QByteArray, QMetaObject
  from ..QtCore import QModelIndex
  from . import QAbstractItemDelegate, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemDelegate = WAIT['QAbstractItemDelegate']
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QByteArray = WAIT['QByteArray']
  QModelIndex = WAIT['QModelIndex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDataWidgetMapper(QObject):
  """
  The cute side of Qt's QDataWidgetMapper: a plain Python object standing in
  front of one C++ QDataWidgetMapper.

  It is built on the cute 'QObject', as Qt's QDataWidgetMapper is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDataWidgetMapper that has a ritual and that Python
  can call so far, 27 names in all: 'metaObject', 'tr', 'setModel', 'model',
  'setItemDelegate', 'itemDelegate', 'setRootIndex', 'rootIndex',
  'setOrientation', 'orientation', 'setSubmitPolicy', 'submitPolicy',
  'addMapping', 'removeMapping', 'mappedSection', 'mappedPropertyName',
  'mappedWidgetAt', 'clearMapping', 'currentIndex', 'revert', 'submit',
  'toFirst', 'toLast', 'toNext', 'toPrevious', 'setCurrentIndex',
  'setCurrentModelIndex'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDataWidgetMapper::~QDataWidgetMapper()': the destructor: Python
    never removes a C++ QDataWidgetMapper.

  What has no ritual
  ------------------

  9 of the 39 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QDataWidgetMapper is created at the first use, not by
    'QDataWidgetMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDataWidgetMapper.
  - Qt tells when it has removed the C++ QDataWidgetMapper. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDataWidgetMapper, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SubmitPolicy(CuteNum):
    """
    The enum 'QDataWidgetMapper::SubmitPolicy' of Qt, with the 2 names Qt
    gives in it.
    """

    AutoSubmit = Kee[int](0)
    ManualSubmit = Kee[int](1)

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
    Calls Qt's 'QString QDataWidgetMapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#tr

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
    #  QString QDataWidgetMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QDataWidgetMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDataWidgetMapper'

  #  A C++ QDataWidgetMapper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDataWidgetMapper'

  #  The functions Qt calls itself that QDataWidgetMapper is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setCurrentIndex': (
          ('_ZN17QDataWidgetMapper15setCurrentIndexEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDataWidgetMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDataWidgetMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QDataWidgetMapper::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QDataWidgetMapper::model() const
    address = self.uglySide.call('ritual_ZNK17QDataWidgetMapper5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def itemDelegate(self) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate *QDataWidgetMapper::itemDelegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#itemDelegate

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QDataWidgetMapper::itemDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper12itemDelegateEv',
    )
    from . import QAbstractItemDelegate
    return QAbstractItemDelegate._cuteAt(address)

  def rootIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QDataWidgetMapper::rootIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#rootIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QDataWidgetMapper::rootIndex() const
    address = self.uglySide.call('ritual_ZNK17QDataWidgetMapper9rootIndexEv')
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QDataWidgetMapper::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QDataWidgetMapper::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper11orientationEv',
    ))

  def submitPolicy(self) -> SubmitPolicy:
    """
    Calls Qt's 'SubmitPolicy QDataWidgetMapper::submitPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#submitPolicy

    Returns
    -------

    SubmitPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SubmitPolicy(number)'
      gives.
    """
    #  SubmitPolicy QDataWidgetMapper::submitPolicy() const
    return QDataWidgetMapper.SubmitPolicy(self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper12submitPolicyEv',
    ))

  @overload(QWidget)
  @overload(NoneType)
  def mappedSection(self, widget: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QDataWidgetMapper::mappedSection(QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#mappedSection

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QDataWidgetMapper::mappedSection(QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper13mappedSectionEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def mappedPropertyName(self, widget: Optional[QWidget]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDataWidgetMapper::mappedPropertyName(QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#mappedPropertyName

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDataWidgetMapper::mappedPropertyName(QWidget *widget)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper18mappedPropertyNameEP7QWidget',
        self._addressOf(widget),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def mappedWidgetAt(self, section: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDataWidgetMapper::mappedWidgetAt(int section)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#mappedWidgetAt

    Parameters
    ----------

    section : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDataWidgetMapper::mappedWidgetAt(int section) const
    address = self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper14mappedWidgetAtEi', section,
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QDataWidgetMapper::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#currentIndex
    """
    #  int QDataWidgetMapper::currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QDataWidgetMapper12currentIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDataWidgetMapper::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QAbstractItemDelegate)
  @overload(NoneType)
  def setItemDelegate(
      self,
      delegate: Optional[QAbstractItemDelegate],
  ) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setItemDelegate(QAbstractItemDelegate
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#setItemDelegate

    Parameters
    ----------

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDataWidgetMapper::setItemDelegate(QAbstractItemDelegate
    #      *delegate)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper15setItemDelegateEP21QAbstractItemDele'
        'gate',
        self._addressOf(delegate),
    )

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setRootIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QDataWidgetMapper::setRootIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper12setRootIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(Qt.Orientation)
  def setOrientation(self, aOrientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setOrientation(Qt::Orientation
    aOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#setOrientation

    Parameters
    ----------

    aOrientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QDataWidgetMapper::setOrientation(Qt::Orientation aOrientation)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper14setOrientationEN2Qt11OrientationE',
        aOrientation.value,
    )

  @overload(SubmitPolicy)
  def setSubmitPolicy(self, policy: SubmitPolicy) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setSubmitPolicy(SubmitPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#setSubmitPolicy

    Parameters
    ----------

    policy : SubmitPolicy
      Passed on as its number.
    """
    #  void QDataWidgetMapper::setSubmitPolicy(SubmitPolicy policy)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper15setSubmitPolicyENS_12SubmitPolicyE',
        policy.value,
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QDataWidgetMapper::setCurrentIndex(int index)
    ritual = 'ritual_ZN17QDataWidgetMapper15setCurrentIndexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDataWidgetMapper15setCurrentIndexEi'
    self.uglySide.call(ritual, index)

  @overload(QModelIndex)
  def setCurrentModelIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::setCurrentModelIndex(const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#setCurrentModelIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QDataWidgetMapper::setCurrentModelIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper20setCurrentModelIndexERK11QModelIndex',
        self._valueOf(index),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDataWidgetMapper::QDataWidgetMapper(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#QDataWidgetMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDataWidgetMapper::QDataWidgetMapper(QObject *parent)
    self._noteCreation(QDataWidgetMapper, lambda: Rituals.call(
        'ritual_ZN17QDataWidgetMapperC1EP7QObject',
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

  @overload(QWidget, int)
  @overload(NoneType, int)
  def addMapping(self, widget: Optional[QWidget], section: int) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::addMapping(QWidget *widget, int
    section)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#addMapping

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    section : int
      Passed on as it is.
    """
    #  void QDataWidgetMapper::addMapping(QWidget *widget, int section)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper10addMappingEP7QWidgeti',
        self._addressOf(widget), section,
    )

  @overload(QWidget, int, QByteArray)
  @overload(NoneType, int, QByteArray)
  def addMapping(
      self,
      widget: Optional[QWidget],
      section: int,
      propertyName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::addMapping(QWidget *widget, int
    section, const QByteArray &propertyName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#addMapping

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    section : int
      Passed on as it is.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QDataWidgetMapper::addMapping(QWidget *widget, int section, const
    #      QByteArray &propertyName)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper10addMappingEP7QWidgetiRK10QByteArray',
        self._addressOf(widget), section, self._valueOf(propertyName),
    )

  @overload(QWidget)
  @overload(NoneType)
  def removeMapping(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::removeMapping(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#removeMapping

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDataWidgetMapper::removeMapping(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN17QDataWidgetMapper13removeMappingEP7QWidget',
        self._addressOf(widget),
    )

  def clearMapping(self) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::clearMapping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatawidgetmapper.html#clearMapping
    """
    #  void QDataWidgetMapper::clearMapping()
    self.uglySide.call('ritual_ZN17QDataWidgetMapper12clearMappingEv')

  def revert(self) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::revert()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#revert
    """
    #  void QDataWidgetMapper::revert()
    self.uglySide.call('ritual_ZN17QDataWidgetMapper6revertEv')

  def submit(self) -> bool:
    """
    Calls Qt's 'bool QDataWidgetMapper::submit()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#submit
    """
    #  bool QDataWidgetMapper::submit()
    return self.uglySide.call('ritual_ZN17QDataWidgetMapper6submitEv')

  def toFirst(self) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::toFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#toFirst
    """
    #  void QDataWidgetMapper::toFirst()
    self.uglySide.call('ritual_ZN17QDataWidgetMapper7toFirstEv')

  def toLast(self) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::toLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#toLast
    """
    #  void QDataWidgetMapper::toLast()
    self.uglySide.call('ritual_ZN17QDataWidgetMapper6toLastEv')

  def toNext(self) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::toNext()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#toNext
    """
    #  void QDataWidgetMapper::toNext()
    self.uglySide.call('ritual_ZN17QDataWidgetMapper6toNextEv')

  def toPrevious(self) -> None:
    """
    Calls Qt's 'void QDataWidgetMapper::toPrevious()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatawidgetmapper.html#toPrevious
    """
    #  void QDataWidgetMapper::toPrevious()
    self.uglySide.call('ritual_ZN17QDataWidgetMapper10toPreviousEv')
