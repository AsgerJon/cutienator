"""
QQuickOverlayAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickOverlayAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlComponent
  from . import QQuickOverlay
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickOverlayAttached(QObject):
  """
  The cute side of Qt's QQuickOverlayAttached: a plain Python object standing
  in front of one C++ QQuickOverlayAttached.

  It is built on the cute 'QObject', as Qt's QQuickOverlayAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickOverlayAttached that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'overlay',
  'modal', 'setModal', 'modeless', 'setModeless', 'overlayChanged',
  'modalChanged', 'modelessChanged', 'pressed', 'released'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickOverlayAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickOverlayAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickOverlayAttachedPrivate *QQuickOverlayAttached::d_func()':
    gives 'QQuickOverlayAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickOverlayAttachedPrivate *QQuickOverlayAttached::d_func()
    const': gives 'QQuickOverlayAttachedPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickOverlayAttached is created at the first use, not by
    'QQuickOverlayAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickOverlayAttached.
  - Qt tells when it has removed the C++ QQuickOverlayAttached. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickOverlayAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayattached.html#tr

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
    #  QString QQuickOverlayAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickOverlayAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickOverlayAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickOverlayAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickOverlayAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickOverlayAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def overlay(self) -> Optional[QQuickOverlay]:
    """
    Calls Qt's 'QQuickOverlay *QQuickOverlayAttached::overlay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayattached.html#overlay

    Returns
    -------

    Optional[QQuickOverlay]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickOverlay *QQuickOverlayAttached::overlay() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickOverlayAttached7overlayEv',
    )
    from . import QQuickOverlay
    return QQuickOverlay._cuteAt(address)

  def modal(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickOverlayAttached::modal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayattached.html#modal

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickOverlayAttached::modal() const
    address = self.uglySide.call('ritual_ZNK21QQuickOverlayAttached5modalEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def modeless(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickOverlayAttached::modeless() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#modeless

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickOverlayAttached::modeless() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickOverlayAttached8modelessEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlComponent)
  @overload(NoneType)
  def setModal(self, modal: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::setModal(QQmlComponent *modal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#setModal

    Parameters
    ----------

    modal : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlayAttached::setModal(QQmlComponent *modal)
    self.uglySide.call(
        'ritual_ZN21QQuickOverlayAttached8setModalEP13QQmlComponent',
        self._addressOf(modal),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setModeless(self, modeless: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::setModeless(QQmlComponent
    *modeless)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#setModeless

    Parameters
    ----------

    modeless : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickOverlayAttached::setModeless(QQmlComponent *modeless)
    self.uglySide.call(
        'ritual_ZN21QQuickOverlayAttached11setModelessEP13QQmlComponent',
        self._addressOf(modeless),
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
    'QQuickOverlayAttached::QQuickOverlayAttached(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#QQuickOverlayAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickOverlayAttached::QQuickOverlayAttached(QObject *parent)
    self._noteCreation(QQuickOverlayAttached, lambda: Rituals.call(
        'ritual_ZN21QQuickOverlayAttachedC1EP7QObject',
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

  def overlayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::overlayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#overlayChanged
    """
    #  void QQuickOverlayAttached::overlayChanged()
    self.uglySide.call('ritual_ZN21QQuickOverlayAttached14overlayChangedEv')

  def modalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::modalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#modalChanged
    """
    #  void QQuickOverlayAttached::modalChanged()
    self.uglySide.call('ritual_ZN21QQuickOverlayAttached12modalChangedEv')

  def modelessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::modelessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#modelessChanged
    """
    #  void QQuickOverlayAttached::modelessChanged()
    self.uglySide.call('ritual_ZN21QQuickOverlayAttached15modelessChangedEv')

  def pressed(self) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickoverlayattached.html#pressed
    """
    #  void QQuickOverlayAttached::pressed()
    self.uglySide.call('ritual_ZN21QQuickOverlayAttached7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QQuickOverlayAttached::released()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickoverlayattached.html#released
    """
    #  void QQuickOverlayAttached::released()
    self.uglySide.call('ritual_ZN21QQuickOverlayAttached8releasedEv')
