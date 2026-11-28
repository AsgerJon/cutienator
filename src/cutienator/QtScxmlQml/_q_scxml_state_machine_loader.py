"""
QScxmlStateMachineLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineloader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlStateMachineLoader to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl, QVariant
  from ..QtScxml import QScxmlDataModel, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlDataModel = WAIT['QScxmlDataModel']
  QScxmlStateMachine = WAIT['QScxmlStateMachine']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlStateMachineLoader(QObject):
  """
  The cute side of Qt's QScxmlStateMachineLoader: a plain Python object
  standing in front of one C++ QScxmlStateMachineLoader.

  It is built on the cute 'QObject', as Qt's QScxmlStateMachineLoader is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlStateMachineLoader that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'stateMachine', 'source', 'setSource', 'initialValues', 'setInitialValues',
  'dataModel', 'setDataModel', 'sourceChanged', 'initialValuesChanged',
  'stateMachineChanged', 'dataModelChanged', 'parse', 'setStateMachine',
  '_qt_property_m_source_offset', '_qt_property_m_initialValues_offset',
  '_qt_property_m_dataModel_offset', '_qt_property_m_stateMachine_offset'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlStateMachineLoader::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QScxmlStateMachineLoader::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlStateMachineLoader::bindableStateMachine()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<QUrl> QScxmlStateMachineLoader::bindableSource()': gives
    a type Python has no way to take yet.
  - Qt's 'QBindable<QVariantMap>
    QScxmlStateMachineLoader::bindableInitialValues()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<QScxmlDataModel *>
    QScxmlStateMachineLoader::bindableDataModel()': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlStateMachineLoader is created at the first use, not by
    'QScxmlStateMachineLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlStateMachineLoader.
  - Qt tells when it has removed the C++ QScxmlStateMachineLoader. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlStateMachineLoader that has no cute function yet,
    'bindableDataModel', 'bindableInitialValues', 'bindableSource',
    'bindableStateMachine', holds a function that raises
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
    Calls Qt's 'QString QScxmlStateMachineLoader::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#tr

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
    #  QString QScxmlStateMachineLoader::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QScxmlStateMachineLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_source_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachineLoader::_qt_property_m_source_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html
    """
    #  size_t QScxmlStateMachineLoader::_qt_property_m_source_offset()
    return Rituals.call(
        'ritual_ZN24QScxmlStateMachineLoader28_qt_property_m_source_offsetE'
        'v',
    )

  @staticmethod
  def _qt_property_m_initialValues_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachineLoader::_qt_property_m_initialValues_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html
    """
    #  size_t QScxmlStateMachineLoader::_qt_property_m_initialValues_offset()
    return Rituals.call(
        'ritual_ZN24QScxmlStateMachineLoader35_qt_property_m_initialValues_'
        'offsetEv',
    )

  @staticmethod
  def _qt_property_m_dataModel_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachineLoader::_qt_property_m_dataModel_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html
    """
    #  size_t QScxmlStateMachineLoader::_qt_property_m_dataModel_offset()
    return Rituals.call(
        'ritual_ZN24QScxmlStateMachineLoader31_qt_property_m_dataModel_offs'
        'etEv',
    )

  @staticmethod
  def _qt_property_m_stateMachine_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachineLoader::_qt_property_m_stateMachine_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html
    """
    #  size_t QScxmlStateMachineLoader::_qt_property_m_stateMachine_offset()
    return Rituals.call(
        'ritual_ZN24QScxmlStateMachineLoader34_qt_property_m_stateMachine_o'
        'ffsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlStateMachineLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlStateMachineLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlStateMachineLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QScxmlStateMachineLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlStateMachineLoader::stateMachine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#stateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlStateMachineLoader::stateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK24QScxmlStateMachineLoader12stateMachineEv',
    )
    from ..QtScxml import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  def initialValues(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QScxmlStateMachineLoader::initialValues() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#initialValues

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QScxmlStateMachineLoader::initialValues() const
    address = self.uglySide.call(
        'ritual_ZNK24QScxmlStateMachineLoader13initialValuesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def dataModel(self) -> Optional[QScxmlDataModel]:
    """
    Calls Qt's 'QScxmlDataModel *QScxmlStateMachineLoader::dataModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#dataModel

    Returns
    -------

    Optional[QScxmlDataModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlDataModel *QScxmlStateMachineLoader::dataModel() const
    address = self.uglySide.call(
        'ritual_ZNK24QScxmlStateMachineLoader9dataModelEv',
    )
    from ..QtScxml import QScxmlDataModel
    return QScxmlDataModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QScxmlStateMachineLoader::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(QMap[str, QVariant])
  def setInitialValues(self, initialValues: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::setInitialValues(const
    QVariantMap &initialValues)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#setInitialValues

    Parameters
    ----------

    initialValues : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QScxmlStateMachineLoader::setInitialValues(const QVariantMap
    #      &initialValues)
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader16setInitialValuesERK4QMapI7QSt'
        'ring8QVariantE',
        self._valueOf(initialValues),
    )

  @overload(QScxmlDataModel)
  @overload(NoneType)
  def setDataModel(self, dataModel: Optional[QScxmlDataModel]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::setDataModel(QScxmlDataModel
    *dataModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#setDataModel

    Parameters
    ----------

    dataModel : Optional[QScxmlDataModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachineLoader::setDataModel(QScxmlDataModel
    #      *dataModel)
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader12setDataModelEP15QScxmlDataMod'
        'el',
        self._addressOf(dataModel),
    )

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def setStateMachine(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachineLoader::setStateMachine(QScxmlStateMachine
    *stateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#setStateMachine

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachineLoader::setStateMachine(QScxmlStateMachine
    #      *stateMachine)
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader15setStateMachineEP18QScxmlStat'
        'eMachine',
        self._addressOf(stateMachine),
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
    'QScxmlStateMachineLoader::QScxmlStateMachineLoader(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScxmlStateMachineLoader::QScxmlStateMachineLoader(QObject *parent)
    self._noteCreation(QScxmlStateMachineLoader, lambda: Rituals.call(
        'ritual_ZN24QScxmlStateMachineLoaderC1EP7QObject',
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

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QScxmlStateMachineLoader::source()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QScxmlStateMachineLoader::source()
    address = self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#sourceChanged
    """
    #  void QScxmlStateMachineLoader::sourceChanged()
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader13sourceChangedEv',
    )

  def initialValuesChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::initialValuesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#initialValuesChanged
    """
    #  void QScxmlStateMachineLoader::initialValuesChanged()
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader20initialValuesChangedEv',
    )

  def stateMachineChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::stateMachineChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#stateMachineChanged
    """
    #  void QScxmlStateMachineLoader::stateMachineChanged()
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader19stateMachineChangedEv',
    )

  def dataModelChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachineLoader::dataModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#dataModelChanged
    """
    #  void QScxmlStateMachineLoader::dataModelChanged()
    self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader16dataModelChangedEv',
    )

  @overload(QUrl)
  def parse(self, source: QUrl) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachineLoader::parse(const QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineloader.html#parse

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QScxmlStateMachineLoader::parse(const QUrl &source)
    return self.uglySide.call(
        'ritual_ZN24QScxmlStateMachineLoader5parseERK4QUrl',
        self._valueOf(source),
    )

  @staticmethod
  def bindableDataModel(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlDataModel *>
    QScxmlStateMachineLoader::bindableDataModel()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineLoader.bindableDataModel' has no cute function "
        "yet. Qt's 'QBindable<QScxmlDataModel *> "
        "QScxmlStateMachineLoader::bindableDataModel()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableInitialValues(*__, **_) -> Never:
    """
    Qt's 'QBindable<QVariantMap>
    QScxmlStateMachineLoader::bindableInitialValues()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineLoader.bindableInitialValues' has no cute "
        "function yet. Qt's 'QBindable<QVariantMap> "
        "QScxmlStateMachineLoader::bindableInitialValues()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableSource(*__, **_) -> Never:
    """
    Qt's 'QBindable<QUrl> QScxmlStateMachineLoader::bindableSource()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineLoader.bindableSource' has no cute function "
        "yet. Qt's 'QBindable<QUrl> "
        "QScxmlStateMachineLoader::bindableSource()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableStateMachine(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlStateMachineLoader::bindableStateMachine()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineLoader.bindableStateMachine' has no cute "
        "function yet. Qt's 'QBindable<QScxmlStateMachine *> "
        "QScxmlStateMachineLoader::bindableStateMachine()': gives a type "
        "Python has no way to take yet.")
