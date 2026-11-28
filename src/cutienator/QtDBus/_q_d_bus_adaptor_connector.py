"""
QDBusAdaptorConnector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDBusAdaptorConnector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArrayView, QMetaObject, QMethodRawArguments
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMethodRawArguments = WAIT['QMethodRawArguments']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusAdaptorConnector(QObject):
  """
  The cute side of Qt's QDBusAdaptorConnector: a plain Python object standing
  in front of one C++ QDBusAdaptorConnector.

  It is built on the cute 'QObject', as Qt's QDBusAdaptorConnector is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusAdaptorConnector that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'relaySlot',
  'polish', 'relaySignal'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusAdaptorConnector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusAdaptorConnector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusAdaptorConnector::~QDBusAdaptorConnector()': the destructor:
    Python never removes a C++ QDBusAdaptorConnector.

  What has no ritual
  ------------------

  9 of the 16 functions Qt declares: 6 leans on 'QDBusAdaptorConnector; 2 not
  a gap; 1 leans on 'qDBusParametersForMethod(QMetaMethod const&,
  QList<QMetaType>&, QString&)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QDBusAdaptorConnector is created at the first use, not by
    'QDBusAdaptorConnector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusAdaptorConnector.
  - Qt tells when it has removed the C++ QDBusAdaptorConnector. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusAdaptorConnector that has no cute function yet,
    '__init__', 'addAdaptor', 'connectAllSignals', 'disconnectAllSignals',
    'relay', 'relaySlotMethodIndex', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QDBusAdaptorConnector, each a class in here
  #  as in C++.

  class AdaptorData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusAdaptorConnector::AdaptorData: a plain Python
    object standing in front of one C++ QDBusAdaptorConnector::AdaptorData.

    C++ hands a QDBusAdaptorConnector::AdaptorData around as a copy, so every
    C++ QDBusAdaptorConnector::AdaptorData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QDBusAdaptorConnector::AdaptorData that has a
    ritual and that Python can call so far, 1 name in all: '__lt__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusAdaptorConnector::AdaptorData::~AdaptorData()': the
      destructor: Python removes its C++ QDBusAdaptorConnector::AdaptorData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QDBusAdaptorConnector::AdaptorData is created at the first use,
      not by 'QDBusAdaptorConnector::AdaptorData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusAdaptorConnector::AdaptorData back gives a
      copy the ritual made for Python, in a new cute
      QDBusAdaptorConnector::AdaptorData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArrayView = WAIT['QByteArrayView']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusAdaptorConnector::AdaptorData'

    #  Qt's '~QDBusAdaptorConnector::AdaptorData()'. Naming it makes this a
    #  value class: Python owns every C++ QDBusAdaptorConnector::AdaptorData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QDBusAdaptorConnector11AdaptorDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __lt__(self, other: QDBusAdaptorConnector.AdaptorData) -> bool:
      """
      Calls Qt's 'bool QDBusAdaptorConnector::AdaptorData::operator<(const
      AdaptorData &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusadaptorconnector-adaptordata.html#operator<

      Parameters
      ----------

      other : QDBusAdaptorConnector.AdaptorData
        Passed on as a value: Qt reads the C++
        QDBusAdaptorConnector::AdaptorData, which stays Python's own.
      """
      #  bool QDBusAdaptorConnector::AdaptorData::operator<(const AdaptorData
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK21QDBusAdaptorConnector11AdaptorDataltERKS0_',
          self._valueOf(other),
      )

    @overload(str)
    def __lt__(self, other: str) -> bool:
      """
      Calls Qt's 'bool QDBusAdaptorConnector::AdaptorData::operator<(const
      QString &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusadaptorconnector-adaptordata.html#operator<

      Parameters
      ----------

      other : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QDBusAdaptorConnector::AdaptorData::operator<(const QString
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK21QDBusAdaptorConnector11AdaptorDataltERK7QString',
          other,
      )

    @overload(QByteArrayView)
    def __lt__(self, other: QByteArrayView) -> bool:
      """
      Calls Qt's 'bool
      QDBusAdaptorConnector::AdaptorData::operator<(QByteArrayView other)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusadaptorconnector-adaptordata.html#operator<

      Parameters
      ----------

      other : QByteArrayView
        Passed on as a value: Qt reads the C++ QByteArrayView, which stays
        Python's own.
      """
      #  bool QDBusAdaptorConnector::AdaptorData::operator<(QByteArrayView
      #      other) const
      return self.uglySide.call(
          'ritual_ZNK21QDBusAdaptorConnector11AdaptorDataltE14QByteArrayVie'
          'w',
          self._valueOf(other),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusAdaptorConnector'

  #  A C++ QDBusAdaptorConnector Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusAdaptorConnector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusAdaptorConnector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusadaptorconnector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusAdaptorConnector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QDBusAdaptorConnector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDBusAdaptorConnector::QDBusAdaptorConnector(QObject *parent)':
    leans on 'QDBusAdaptorConnector::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusAdaptorConnector.__init__' has no cute function yet. Qt's "
        "'QDBusAdaptorConnector::QDBusAdaptorConnector(QObject *parent)': "
        "leans on 'QDBusAdaptorConnector::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QMethodRawArguments)
  def relaySlot(self, a: QMethodRawArguments) -> None:
    """
    Calls Qt's 'void QDBusAdaptorConnector::relaySlot(QMethodRawArguments
    a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusadaptorconnector.html#relaySlot

    Parameters
    ----------

    a : QMethodRawArguments
      Passed on as a value: Qt reads the C++ QMethodRawArguments, which stays
      Python's own.
    """
    #  void QDBusAdaptorConnector::relaySlot(QMethodRawArguments a)
    self.uglySide.call(
        'ritual_ZN21QDBusAdaptorConnector9relaySlotE19QMethodRawArguments',
        self._valueOf(a),
    )

  def polish(self) -> None:
    """
    Calls Qt's 'void QDBusAdaptorConnector::polish()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusadaptorconnector.html#polish
    """
    #  void QDBusAdaptorConnector::polish()
    self.uglySide.call('ritual_ZN21QDBusAdaptorConnector6polishEv')

  @overload(QObject, QMetaObject, int, QList[QVariant])
  @overload(QObject, NoneType, int, QList[QVariant])
  @overload(NoneType, QMetaObject, int, QList[QVariant])
  @overload(NoneType, NoneType, int, QList[QVariant])
  def relaySignal(
      self,
      obj: Optional[QObject],
      metaObject: Optional[QMetaObject],
      sid: int,
      args: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QDBusAdaptorConnector::relaySignal(QObject *obj, const
    QMetaObject *metaObject, int sid, const QVariantList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusadaptorconnector.html#relaySignal

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sid : int
      Passed on as it is.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusAdaptorConnector::relaySignal(QObject *obj, const
    #      QMetaObject *metaObject, int sid, const QVariantList &args)
    self.uglySide.call(
        'ritual_ZN21QDBusAdaptorConnector11relaySignalEP7QObjectPK11QMetaOb'
        'jectiRK5QListI8QVariantE',
        self._addressOf(obj, 'QObject'), self._addressOf(metaObject,
        'QMetaObject'), sid, self._valueOf(args),
    )

  @staticmethod
  def addAdaptor(*__, **_) -> Never:
    """
    Qt's 'void QDBusAdaptorConnector::addAdaptor(QDBusAbstractAdaptor
    *adaptor)': leans on 'QDBusAdaptorConnector::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDBusAdaptorConnector.addAdaptor' has no cute function yet. Qt's "
        "'void QDBusAdaptorConnector::addAdaptor(QDBusAbstractAdaptor "
        "*adaptor)': leans on 'QDBusAdaptorConnector::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def connectAllSignals(*__, **_) -> Never:
    """
    Qt's 'void QDBusAdaptorConnector::connectAllSignals(QObject *object)':
    leans on 'QDBusAdaptorConnector::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusAdaptorConnector.connectAllSignals' has no cute function "
        "yet. Qt's 'void QDBusAdaptorConnector::connectAllSignals(QObject "
        "*object)': leans on 'QDBusAdaptorConnector::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def disconnectAllSignals(*__, **_) -> Never:
    """
    Qt's 'void QDBusAdaptorConnector::disconnectAllSignals(QObject *object)':
    leans on 'QDBusAdaptorConnector::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusAdaptorConnector.disconnectAllSignals' has no cute function "
        "yet. Qt's 'void "
        "QDBusAdaptorConnector::disconnectAllSignals(QObject *object)': "
        "leans on 'QDBusAdaptorConnector::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def relay(*__, **_) -> Never:
    """
    Qt's 'void QDBusAdaptorConnector::relay(QObject *sender, int id, void
    **a2)': leans on 'qDBusParametersForMethod(QMetaMethod const&,
    QList<QMetaType>&, QString&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusAdaptorConnector.relay' has no cute function yet. Qt's 'void "
        "QDBusAdaptorConnector::relay(QObject *sender, int id, void **a2)': "
        "leans on 'qDBusParametersForMethod(QMetaMethod const&, "
        "QList<QMetaType>&, QString&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def relaySlotMethodIndex(*__, **_) -> Never:
    """
    Qt's 'int QDBusAdaptorConnector::relaySlotMethodIndex()': leans on
    'QDBusAdaptorConnector::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusAdaptorConnector.relaySlotMethodIndex' has no cute function "
        "yet. Qt's 'int QDBusAdaptorConnector::relaySlotMethodIndex()': "
        "leans on 'QDBusAdaptorConnector::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
