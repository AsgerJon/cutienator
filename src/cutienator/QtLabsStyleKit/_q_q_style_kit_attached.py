"""
QQStyleKitAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQStyleKitAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQStyleKitDebug, QQStyleKitStyle


class QQStyleKitAttached(QObject):
  """
  The cute side of Qt's QQStyleKitAttached: a plain Python object standing in
  front of one C++ QQStyleKitAttached.

  It is built on the cute 'QObject', as Qt's QQStyleKitAttached is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitAttached that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'style', 'styleUrl',
  'debug', 'styleLoaded', 'styleChanged', 'styleUrlChanged',
  'transitionsEnabledChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitAttached::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQStyleKitAttached::~QQStyleKitAttached()': the destructor: Python
    never removes a C++ QQStyleKitAttached.

  What has no ritual
  ------------------

  8 of the 19 functions Qt declares: 6 leans on 'QQStyleKitAttached; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QQStyleKitAttached is created at the first use, not by
    'QQStyleKitAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitAttached.
  - Qt tells when it has removed the C++ QQStyleKitAttached. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitAttached that has no cute function yet,
    '__init__', 'setStyle', 'setStyleUrl', 'setTransitionsEnabled',
    'transitionsEnabled', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitAttached'

  #  A C++ QQStyleKitAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitAttached::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQStyleKitAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def style(self) -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QQStyleKitAttached::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitattached.html#style

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QQStyleKitAttached::style() const
    address = self.uglySide.call('ritual_ZNK18QQStyleKitAttached5styleEv')
    from . import QQStyleKitStyle
    return QQStyleKitStyle._cuteAt(address)

  def styleUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQStyleKitAttached::styleUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitattached.html#styleUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQStyleKitAttached::styleUrl() const
    address = self.uglySide.call('ritual_ZNK18QQStyleKitAttached8styleUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def debug(self) -> Optional[QQStyleKitDebug]:
    """
    Calls Qt's 'QQStyleKitDebug *QQStyleKitAttached::debug() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitattached.html#debug

    Returns
    -------

    Optional[QQStyleKitDebug]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitDebug *QQStyleKitAttached::debug() const
    address = self.uglySide.call('ritual_ZNK18QQStyleKitAttached5debugEv')
    from . import QQStyleKitDebug
    return QQStyleKitDebug._cuteAt(address)

  def styleLoaded(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitAttached::styleLoaded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitattached.html#styleLoaded
    """
    #  bool QQStyleKitAttached::styleLoaded() const
    return self.uglySide.call(
        'ritual_ZNK18QQStyleKitAttached11styleLoadedEv',
    )

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
    Qt's 'QQStyleKitAttached::QQStyleKitAttached(QObject *parent)': leans on
    'QQStyleKitAttached::s_instance', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitAttached.__init__' has no cute function yet. Qt's "
        "'QQStyleKitAttached::QQStyleKitAttached(QObject *parent)': leans "
        "on 'QQStyleKitAttached::s_instance', which Qt's source does not "
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

  def styleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitAttached::styleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitattached.html#styleChanged
    """
    #  void QQStyleKitAttached::styleChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitAttached12styleChangedEv')

  def styleUrlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitAttached::styleUrlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitattached.html#styleUrlChanged
    """
    #  void QQStyleKitAttached::styleUrlChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitAttached15styleUrlChangedEv')

  def transitionsEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitAttached::transitionsEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitattached.html#transitionsEnabledChanged
    """
    #  void QQStyleKitAttached::transitionsEnabledChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitAttached25transitionsEnabledChangedEv',
    )

  @staticmethod
  def setStyle(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitAttached::setStyle(QQStyleKitStyle *style)': leans
    on 'QQStyleKitAttached::styleChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitAttached.setStyle' has no cute function yet. Qt's 'void "
        "QQStyleKitAttached::setStyle(QQStyleKitStyle *style)': leans on "
        "'QQStyleKitAttached::styleChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setStyleUrl(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitAttached::setStyleUrl(const QUrl &styleUrl)': leans
    on 'QQStyleKitAttached::styleChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitAttached.setStyleUrl' has no cute function yet. Qt's "
        "'void QQStyleKitAttached::setStyleUrl(const QUrl &styleUrl)': "
        "leans on 'QQStyleKitAttached::styleChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setTransitionsEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitAttached::setTransitionsEnabled(bool enabled)':
    leans on 'QQStyleKitAttached::s_transitionsEnabled', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitAttached.setTransitionsEnabled' has no cute function "
        "yet. Qt's 'void QQStyleKitAttached::setTransitionsEnabled(bool "
        "enabled)': leans on 'QQStyleKitAttached::s_transitionsEnabled', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def transitionsEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitAttached::transitionsEnabled() const': leans on
    'QQStyleKitAttached::s_transitionsEnabled', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitAttached.transitionsEnabled' has no cute function yet. "
        "Qt's 'bool QQStyleKitAttached::transitionsEnabled() const': leans "
        "on 'QQStyleKitAttached::s_transitionsEnabled', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
