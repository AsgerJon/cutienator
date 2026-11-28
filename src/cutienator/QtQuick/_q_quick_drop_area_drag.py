"""
QQuickDropAreaDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDropAreaDrag to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickDropAreaDrag(QObject):
  """
  The cute side of Qt's QQuickDropAreaDrag: a plain Python object standing in
  front of one C++ QQuickDropAreaDrag.

  It is built on the cute 'QObject', as Qt's QQuickDropAreaDrag is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDropAreaDrag that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'x', 'positionChanged',
  'sourceChanged'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDropAreaDrag::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickDropAreaDrag::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDropAreaDrag::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickDropAreaDrag::~QQuickDropAreaDrag()': the destructor: Python
    never removes a C++ QQuickDropAreaDrag.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QQuickDropAreaDrag.

  What to expect
  --------------

  - The C++ QQuickDropAreaDrag is created at the first use, not by
    'QQuickDropAreaDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDropAreaDrag.
  - Qt tells when it has removed the C++ QQuickDropAreaDrag. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDropAreaDrag that has no cute function yet,
    '__init__', 'source', 'y', holds a function that raises
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
  __qt_class__ = 'QQuickDropAreaDrag'

  #  A C++ QQuickDropAreaDrag Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDropAreaDrag'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDropAreaDrag::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdropareadrag.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDropAreaDrag::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickDropAreaDrag10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickDropAreaDrag::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdropareadrag.html#x
    """
    #  qreal QQuickDropAreaDrag::x() const
    return self.uglySide.call('ritual_ZNK18QQuickDropAreaDrag1xEv')

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
    Qt's 'QQuickDropAreaDrag::QQuickDropAreaDrag(QQuickDropAreaPrivate *d,
    QObject *parent)': leans on
    'QQuickDropAreaDrag::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickDropAreaDrag.__init__' has no cute function yet. Qt's "
        "'QQuickDropAreaDrag::QQuickDropAreaDrag(QQuickDropAreaPrivate *d, "
        "QObject *parent)': leans on "
        "'QQuickDropAreaDrag::qt_metacall(QMetaObject::Call, int, void**)', "
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDropAreaDrag::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdropareadrag.html#positionChanged
    """
    #  void QQuickDropAreaDrag::positionChanged()
    self.uglySide.call('ritual_ZN18QQuickDropAreaDrag15positionChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDropAreaDrag::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdropareadrag.html#sourceChanged
    """
    #  void QQuickDropAreaDrag::sourceChanged()
    self.uglySide.call('ritual_ZN18QQuickDropAreaDrag13sourceChangedEv')

  @staticmethod
  def source(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuickDropAreaDrag::source() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickDropAreaPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDropAreaDrag.source' has no cute function yet. Qt's "
        "'QObject *QQuickDropAreaDrag::source() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuickDropAreaPrivate'.")

  @staticmethod
  def y(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickDropAreaDrag::y() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuickDropAreaPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDropAreaDrag.y' has no cute function yet. Qt's 'qreal "
        "QQuickDropAreaDrag::y() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QQuickDropAreaPrivate'.")
