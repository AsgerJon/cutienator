"""
QQuickDesignerSupportItems binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportitems_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickDesignerSupportItems to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QTypeRevision, QUrl
  from ..QtQml import QQmlContext
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQuickItem = WAIT['QQuickItem']
  QTypeRevision = WAIT['QTypeRevision']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerSupportItems(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerSupportItems: a plain Python object
  standing in front of one C++ QQuickDesignerSupportItems.

  C++ hands a QQuickDesignerSupportItems around as a copy, so every C++
  QQuickDesignerSupportItems behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerSupportItems that has a ritual and
  that Python can call so far, 9 names in all: 'createPrimitive',
  'createComponent', 'tweakObjects', 'objectWasDeleted',
  'disableNativeTextRendering', 'disableTextCursor', 'disableTransition',
  'disableBehaivour', 'stopUnifiedTimer'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QQuickDesignerSupportItems::registerFixResourcePathsForObjectCallBack(
    void (*)(QObject *) callback)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQuickDesignerSupportItems::~QQuickDesignerSupportItems()': the
    destructor: Python removes its C++ QQuickDesignerSupportItems by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickDesignerSupportItems is created at the first use, not by
    'QQuickDesignerSupportItems(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerSupportItems back gives a copy the
    ritual made for Python, in a new cute QQuickDesignerSupportItems.
  - Each name of Qt's QQuickDesignerSupportItems that has no cute function
    yet, 'registerFixResourcePathsForObjectCallBack', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, QTypeRevision, QQmlContext)
  @overload(str, QTypeRevision, NoneType)
  def createPrimitive(
      typeName: str,
      version: QTypeRevision,
      context: Optional[QQmlContext],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDesignerSupportItems::createPrimitive(const
    QString &typeName, QTypeRevision version, QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#createPrimitive

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDesignerSupportItems::createPrimitive(const QString
    #      &typeName, QTypeRevision version, QQmlContext *context)
    address = Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems15createPrimitiveERK7QString1'
        '3QTypeRevisionP11QQmlContext',
        typeName, CuteMixin._valueOf(version), CuteMixin._addressOf(context),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @staticmethod
  @overload(QUrl, QQmlContext)
  @overload(QUrl, NoneType)
  def createComponent(
      componentUrl: QUrl,
      context: Optional[QQmlContext],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDesignerSupportItems::createComponent(const
    QUrl &componentUrl, QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#createComponent

    Parameters
    ----------

    componentUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDesignerSupportItems::createComponent(const QUrl
    #      &componentUrl, QQmlContext *context)
    address = Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems15createComponentERK4QUrlP11Q'
        'QmlContext',
        CuteMixin._valueOf(componentUrl), CuteMixin._addressOf(context),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def tweakObjects(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportItems::tweakObjects(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#tweakObjects

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportItems::tweakObjects(QObject *object)
    Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems12tweakObjectsEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def objectWasDeleted(object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupportItems::objectWasDeleted(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#objectWasDeleted

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupportItems::objectWasDeleted(QObject *object)
    return Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems16objectWasDeletedEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def disableNativeTextRendering(item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportItems::disableNativeTextRendering(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportItems::disableNativeTextRendering(QQuickItem
    #      *item)
    Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems26disableNativeTextRenderingE'
        'P10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def disableTextCursor(item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportItems::disableTextCursor(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#disableTextCursor

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportItems::disableTextCursor(QQuickItem *item)
    Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems17disableTextCursorEP10QQuick'
        'Item',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def disableTransition(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportItems::disableTransition(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#disableTransition

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportItems::disableTransition(QObject *object)
    Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems17disableTransitionEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def disableBehaivour(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportItems::disableBehaivour(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#disableBehaivour

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportItems::disableBehaivour(QObject *object)
    Rituals.call(
        'ritual_ZN26QQuickDesignerSupportItems16disableBehaivourEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  def stopUnifiedTimer() -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportItems::stopUnifiedTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportitems.html#stopUnifiedTimer
    """
    #  void QQuickDesignerSupportItems::stopUnifiedTimer()
    Rituals.call('ritual_ZN26QQuickDesignerSupportItems16stopUnifiedTimerEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerSupportItems'

  #  Qt's '~QQuickDesignerSupportItems()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickDesignerSupportItems behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuickDesignerSupportItemsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def registerFixResourcePathsForObjectCallBack(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickDesignerSupportItems::registerFixResourcePathsForObjectCallBack(
    void (*)(QObject *) callback)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickDesignerSupportItems.registerFixResourcePathsForObjectCallBa"
        "ck' has no cute function yet. Qt's 'void "
        "QQuickDesignerSupportItems::registerFixResourcePathsForObjectCallBa"
        "ck(void (*)(QObject *) callback)': takes a type Python has no way "
        "to hand over yet.")
