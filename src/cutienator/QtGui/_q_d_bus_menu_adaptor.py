"""
QDBusMenuAdaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusmenuadaptor_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusMenuAdaptor to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDBusMenuItem, QDBusMenuItemKeys
  from ..QtDBus import QDBusVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMenuItem = WAIT['QDBusMenuItem']
  QDBusMenuItemKeys = WAIT['QDBusMenuItemKeys']
  QDBusVariant = WAIT['QDBusVariant']


class QDBusMenuAdaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMenuAdaptor: a plain Python object standing in
  front of one C++ QDBusMenuAdaptor.

  What exists
  -----------

  Every function of Qt's QDBusMenuAdaptor that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'status', 'textDirection',
  'version', 'Event', 'GetProperty', 'ItemActivationRequested',
  'ItemsPropertiesUpdated', 'LayoutUpdated'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusMenuAdaptor::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDBusMenuAdaptor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusMenuAdaptor::~QDBusMenuAdaptor()': the destructor: Python
    never removes a C++ QDBusMenuAdaptor.

  What has no ritual
  ------------------

  9 of the 21 functions Qt declares: 3 leans on 'QDBusPlatformMenuItem; 2 not
  a gap; 2 leans on 'QDBusMenuAdaptor; 1 leans on 'operator<<(QDebug,
  QDBusMenuItem const&)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'operator<<(QDebug, QDBusMenuLayoutItem const&)', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QDBusMenuAdaptor is created at the first use, not by
    'QDBusMenuAdaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusMenuAdaptor.
  - Qt tells when it has removed the C++ QDBusMenuAdaptor. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusMenuAdaptor that has no cute function yet,
    'AboutToShow', 'AboutToShowGroup', 'EventGroup', 'GetGroupProperties',
    'GetLayout', '__init__', holds a function that raises
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
  __qt_class__ = 'QDBusMenuAdaptor'

  #  A C++ QDBusMenuAdaptor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusMenuAdaptor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusMenuAdaptor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuadaptor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusMenuAdaptor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QDBusMenuAdaptor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> str:
    """
    Calls Qt's 'QString QDBusMenuAdaptor::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuadaptor.html#status

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMenuAdaptor::status() const
    return self.uglySide.call('ritual_ZNK16QDBusMenuAdaptor6statusEv')

  def textDirection(self) -> str:
    """
    Calls Qt's 'QString QDBusMenuAdaptor::textDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuadaptor.html#textDirection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMenuAdaptor::textDirection() const
    return self.uglySide.call(
        'ritual_ZNK16QDBusMenuAdaptor13textDirectionEv',
    )

  def version(self) -> int:
    """
    Calls Qt's 'uint QDBusMenuAdaptor::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuadaptor.html#version
    """
    #  uint QDBusMenuAdaptor::version() const
    return self.uglySide.call('ritual_ZNK16QDBusMenuAdaptor7versionEv')

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
    Qt's 'QDBusMenuAdaptor::QDBusMenuAdaptor(QDBusPlatformMenu
    *topLevelMenu)': leans on
    'QDBusMenuAdaptor::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuAdaptor.__init__' has no cute function yet. Qt's "
        "'QDBusMenuAdaptor::QDBusMenuAdaptor(QDBusPlatformMenu "
        "*topLevelMenu)': leans on "
        "'QDBusMenuAdaptor::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(int, str, QDBusVariant, int)
  def Event(
      self,
      id: int,
      eventId: str,
      data: QDBusVariant,
      timestamp: int,
  ) -> None:
    """
    Calls Qt's 'void QDBusMenuAdaptor::Event(int id, const QString &eventId,
    const QDBusVariant &data, uint timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuadaptor.html#Event

    Parameters
    ----------

    id : int
      Passed on as it is.

    eventId : str
      Passed on as it is: a QString is made of it for the call.

    data : QDBusVariant
      Passed on as a value: Qt reads the C++ QDBusVariant, which stays
      Python's own.

    timestamp : int
      Passed on as it is.
    """
    #  void QDBusMenuAdaptor::Event(int id, const QString &eventId, const
    #      QDBusVariant &data, uint timestamp)
    self.uglySide.call(
        'ritual_ZN16QDBusMenuAdaptor5EventEiRK7QStringRK12QDBusVariantj',
        id, eventId, self._valueOf(data), timestamp,
    )

  @overload(int, str)
  def GetProperty(self, id: int, name: str) -> QDBusVariant:
    """
    Calls Qt's 'QDBusVariant QDBusMenuAdaptor::GetProperty(int id, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuadaptor.html#GetProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusVariant
      A new cute QDBusVariant around the copy Qt gave back. Python owns it.
    """
    #  QDBusVariant QDBusMenuAdaptor::GetProperty(int id, const QString
    #      &name)
    address = self.uglySide.call(
        'ritual_ZN16QDBusMenuAdaptor11GetPropertyEiRK7QString', id, name,
    )
    from ..QtDBus import QDBusVariant
    return QDBusVariant._cuteOwning(address)

  @overload(int, int)
  def ItemActivationRequested(self, id: int, timestamp: int) -> None:
    """
    Calls Qt's 'void QDBusMenuAdaptor::ItemActivationRequested(int id, uint
    timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuadaptor.html#ItemActivationRequested

    Parameters
    ----------

    id : int
      Passed on as it is.

    timestamp : int
      Passed on as it is.
    """
    #  void QDBusMenuAdaptor::ItemActivationRequested(int id, uint timestamp)
    self.uglySide.call(
        'ritual_ZN16QDBusMenuAdaptor23ItemActivationRequestedEij',
        id, timestamp,
    )

  @overload(QList[QDBusMenuItem], QList[QDBusMenuItemKeys])
  def ItemsPropertiesUpdated(
      self,
      updatedProps: QList[QDBusMenuItem],
      removedProps: QList[QDBusMenuItemKeys],
  ) -> None:
    """
    Calls Qt's 'void QDBusMenuAdaptor::ItemsPropertiesUpdated(const
    QDBusMenuItemList &updatedProps, const QDBusMenuItemKeysList
    &removedProps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuadaptor.html#ItemsPropertiesUpdated

    Parameters
    ----------

    updatedProps : QList[QDBusMenuItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    removedProps : QList[QDBusMenuItemKeys]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusMenuAdaptor::ItemsPropertiesUpdated(const QDBusMenuItemList
    #      &updatedProps, const QDBusMenuItemKeysList &removedProps)
    self.uglySide.call(
        'ritual_ZN16QDBusMenuAdaptor22ItemsPropertiesUpdatedERK5QListI13QDB'
        'usMenuItemERKS0_I17QDBusMenuItemKeysE',
        self._valueOf(updatedProps), self._valueOf(removedProps),
    )

  @overload(int, int)
  def LayoutUpdated(self, revision: int, parent: int) -> None:
    """
    Calls Qt's 'void QDBusMenuAdaptor::LayoutUpdated(uint revision, int
    parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuadaptor.html#LayoutUpdated

    Parameters
    ----------

    revision : int
      Passed on as it is.

    parent : int
      Passed on as it is.
    """
    #  void QDBusMenuAdaptor::LayoutUpdated(uint revision, int parent)
    self.uglySide.call(
        'ritual_ZN16QDBusMenuAdaptor13LayoutUpdatedEji', revision, parent,
    )

  @staticmethod
  def AboutToShow(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMenuAdaptor::AboutToShow(int id)': leans on
    'QDBusPlatformMenuItem::byId(int)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuAdaptor.AboutToShow' has no cute function yet. Qt's "
        "'bool QDBusMenuAdaptor::AboutToShow(int id)': leans on "
        "'QDBusPlatformMenuItem::byId(int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def AboutToShowGroup(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDBusMenuAdaptor::AboutToShowGroup(const QList<int>
    &ids, QList<int> &idErrors)': leans on
    'QDBusPlatformMenuItem::byId(int)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuAdaptor.AboutToShowGroup' has no cute function yet. Qt's "
        "'QList<int> QDBusMenuAdaptor::AboutToShowGroup(const QList<int> "
        "&ids, QList<int> &idErrors)': leans on "
        "'QDBusPlatformMenuItem::byId(int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def EventGroup(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDBusMenuAdaptor::EventGroup(const QDBusMenuEventList
    &events)': leans on 'QDBusPlatformMenuItem::byId(int)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusMenuAdaptor.EventGroup' has no cute function yet. Qt's "
        "'QList<int> QDBusMenuAdaptor::EventGroup(const QDBusMenuEventList "
        "&events)': leans on 'QDBusPlatformMenuItem::byId(int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def GetGroupProperties(*__, **_) -> Never:
    """
    Qt's 'QDBusMenuItemList QDBusMenuAdaptor::GetGroupProperties(const
    QList<int> &ids, const QStringList &propertyNames)': leans on
    'operator<<(QDebug, QDBusMenuItem const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuAdaptor.GetGroupProperties' has no cute function yet. "
        "Qt's 'QDBusMenuItemList QDBusMenuAdaptor::GetGroupProperties(const "
        "QList<int> &ids, const QStringList &propertyNames)': leans on "
        "'operator<<(QDebug, QDBusMenuItem const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def GetLayout(*__, **_) -> Never:
    """
    Qt's 'uint QDBusMenuAdaptor::GetLayout(int parentId, int recursionDepth,
    const QStringList &propertyNames, QDBusMenuLayoutItem &layout)': leans on
    'operator<<(QDebug, QDBusMenuLayoutItem const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuAdaptor.GetLayout' has no cute function yet. Qt's 'uint "
        "QDBusMenuAdaptor::GetLayout(int parentId, int recursionDepth, "
        "const QStringList &propertyNames, QDBusMenuLayoutItem &layout)': "
        "leans on 'operator<<(QDebug, QDBusMenuLayoutItem const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
