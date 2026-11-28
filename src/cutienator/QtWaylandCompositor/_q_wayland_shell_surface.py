"""
QWaylandShellSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandshellsurface.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWaylandCompositorExtension, QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWaylandQuickShellIntegration, QWaylandQuickShellSurfaceItem
  from . import QWaylandShellSurfacePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandQuickShellSurfaceItem = WAIT['QWaylandQuickShellSurfaceItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandShellSurface(QWaylandCompositorExtension):
  """
  The cute side of Qt's QWaylandShellSurface: a plain Python object standing
  in front of one C++ QWaylandShellSurface.

  It is built on the cute 'QWaylandCompositorExtension', as Qt's
  QWaylandShellSurface is built on Qt's QWaylandCompositorExtension, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandShellSurface that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'd_func',
  'createIntegration', 'windowType', 'isModal', 'setModal',
  'windowTypeChanged', 'modalChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandShellSurface::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandShellSurface::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandShellSurfacePrivate *QWaylandShellSurface::d_func()
    const': takes in Python what 'QWaylandShellSurfacePrivate
    *QWaylandShellSurface::d_func()' takes.
  - Qt's 'void QWaylandShellSurface::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's
    'QWaylandShellSurface::QWaylandShellSurface(QWaylandShellSurfacePrivate
    &dd)': takes a type Python has no way to hand over yet.
  - Qt's 'QWaylandShellSurface::QWaylandShellSurface(QWaylandObject
    *container, QWaylandShellSurfacePrivate &dd)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandShellSurface is created at the first use, not by
    'QWaylandShellSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandShellSurface.
  - Qt tells when it has removed the C++ QWaylandShellSurface. Every call on
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
    Calls Qt's 'QString QWaylandShellSurface::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshellsurface.html#tr

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
    #  QString QWaylandShellSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QWaylandShellSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandShellSurface'

  #  A C++ QWaylandShellSurface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandShellSurface'

  #  The functions Qt calls itself that QWaylandShellSurface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createIntegration': (
          ('_ZN20QWaylandShellSurface17createIntegrationEP29QWaylandQuickSh'
           'ellSurfaceItem',
           ('address', 'address',
            'QtWaylandCompositor:QWaylandQuickShellIntegration'),
           (
               ('address', 'address',
                'QtWaylandCompositor:QWaylandQuickShellSurfaceItem'),
           )),
      ),
      'windowType': (
          ('_ZNK20QWaylandShellSurface10windowTypeEv',
           ('int', 'enum', 'QtCore:Qt.WindowType'),
           ()),
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
    Calls Qt's 'const QMetaObject *QWaylandShellSurface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshellsurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandShellSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QWaylandShellSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def windowType(self) -> Qt.WindowType:
    """
    Calls Qt's 'Qt::WindowType QWaylandShellSurface::windowType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshellsurface.html#windowType

    Returns
    -------

    Qt.WindowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowType(number)'
      gives.
    """
    #  Qt::WindowType QWaylandShellSurface::windowType() const
    ritual = 'ritual_ZNK20QWaylandShellSurface10windowTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QWaylandShellSurface10windowTypeEv'
    return Qt.WindowType(self.uglySide.call(ritual))

  def isModal(self) -> bool:
    """
    Calls Qt's 'bool QWaylandShellSurface::isModal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshellsurface.html#isModal
    """
    #  bool QWaylandShellSurface::isModal() const
    return self.uglySide.call('ritual_ZNK20QWaylandShellSurface7isModalEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setModal(self, newModal: bool) -> None:
    """
    Calls Qt's 'void QWaylandShellSurface::setModal(bool newModal)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshellsurface.html#setModal

    Parameters
    ----------

    newModal : bool
      Passed on as it is.
    """
    #  void QWaylandShellSurface::setModal(bool newModal)
    self.uglySide.call(
        'ritual_ZN20QWaylandShellSurface8setModalEb', newModal,
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

  @overload(QWaylandObject)
  @overload(NoneType)
  def __init__(self, waylandObject: Optional[QWaylandObject]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandShellSurface::QWaylandShellSurface(QWaylandObject
    *waylandObject)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshellsurface.html#QWaylandShellSurface

    Parameters
    ----------

    waylandObject : Optional[QWaylandObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandShellSurface::QWaylandShellSurface(QWaylandObject
    #      *waylandObject)
    self._noteCreation(QWaylandShellSurface, lambda: Rituals.call(
        'ritual_ZN20QWaylandShellSurfaceC1EP14QWaylandObject',
        self._addressOf(waylandObject),
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

  def d_func(self) -> Optional[QWaylandShellSurfacePrivate]:
    """
    Calls Qt's 'QWaylandShellSurfacePrivate *QWaylandShellSurface::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshellsurface.html#d_func

    Returns
    -------

    Optional[QWaylandShellSurfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandShellSurfacePrivate *QWaylandShellSurface::d_func()
    address = self.uglySide.call('ritual_ZN20QWaylandShellSurface6d_funcEv')
    from . import QWaylandShellSurfacePrivate
    return QWaylandShellSurfacePrivate._cuteAt(address)

  @overload(QWaylandQuickShellSurfaceItem)
  @overload(NoneType)
  def createIntegration(
      self,
      item: Optional[QWaylandQuickShellSurfaceItem],
  ) -> Optional[QWaylandQuickShellIntegration]:
    """
    Calls Qt's 'QWaylandQuickShellIntegration
    *QWaylandShellSurface::createIntegration(QWaylandQuickShellSurfaceItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshellsurface.html#createIntegration

    Parameters
    ----------

    item : Optional[QWaylandQuickShellSurfaceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandQuickShellIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickShellIntegration
    #      *QWaylandShellSurface::createIntegration(
    #      QWaylandQuickShellSurfaceItem *item)
    address = self.uglySide.call(
        'ritual_ZN20QWaylandShellSurface17createIntegrationEP29QWaylandQuic'
        'kShellSurfaceItem',
        self._addressOf(item),
    )
    from . import QWaylandQuickShellIntegration
    return QWaylandQuickShellIntegration._cuteAt(address)

  def windowTypeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandShellSurface::windowTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshellsurface.html#windowTypeChanged
    """
    #  void QWaylandShellSurface::windowTypeChanged()
    self.uglySide.call(
        'ritual_ZN20QWaylandShellSurface17windowTypeChangedEv',
    )

  def modalChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandShellSurface::modalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshellsurface.html#modalChanged
    """
    #  void QWaylandShellSurface::modalChanged()
    self.uglySide.call('ritual_ZN20QWaylandShellSurface12modalChangedEv')
