"""
QWaylandCompositorExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandcompositorextension.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QWaylandCompositorExtensionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandCompositorExtension(QWaylandObject):
  """
  The cute side of Qt's QWaylandCompositorExtension: a plain Python object
  standing in front of one C++ QWaylandCompositorExtension.

  It is built on the cute 'QWaylandObject', as Qt's
  QWaylandCompositorExtension is built on Qt's QWaylandObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandCompositorExtension that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'extensionContainer', 'setExtensionContainer', 'initialize',
  'isInitialized', 'event'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandCompositorExtension::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWaylandCompositorExtension::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandCompositorExtensionPrivate
    *QWaylandCompositorExtension::d_func() const': takes in Python what
    'QWaylandCompositorExtensionPrivate
    *QWaylandCompositorExtension::d_func()' takes.
  - Qt's 'void QWaylandCompositorExtension::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QWaylandCompositorExtension::~QWaylandCompositorExtension()': the
    destructor: Python never removes a C++ QWaylandCompositorExtension.
  - Qt's 'const struct wl_interface
    *QWaylandCompositorExtension::extensionInterface() const': gives 'struct
    wl_interface', which has no cute class yet.
  - Qt's 'QWaylandCompositorExtension::QWaylandCompositorExtension(
    QWaylandCompositorExtensionPrivate &dd)': takes a type Python has no way
    to hand over yet.
  - Qt's
    'QWaylandCompositorExtension::QWaylandCompositorExtension(QWaylandObject
    *container, QWaylandCompositorExtensionPrivate &dd)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandCompositorExtension is created at the first use, not by
    'QWaylandCompositorExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandCompositorExtension.
  - Qt tells when it has removed the C++ QWaylandCompositorExtension. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandCompositorExtension that has no cute function
    yet, 'extensionInterface', holds a function that raises
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
    Calls Qt's 'QString QWaylandCompositorExtension::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html#tr

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
    #  QString QWaylandCompositorExtension::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QWaylandCompositorExtension2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandCompositorExtension'

  #  A C++ QWaylandCompositorExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandCompositorExtension'

  #  The functions Qt calls itself that QWaylandCompositorExtension is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'extensionInterface': (
          'const struct wl_interface '
          '*QWaylandCompositorExtension::extensionInterface() const',
      ),
  }

  #  The functions Qt calls itself that QWaylandCompositorExtension is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN27QWaylandCompositorExtension10initializeEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QWaylandCompositorExtension::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandCompositorExtension::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QWaylandCompositorExtension10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def extensionContainer(self) -> Optional[QWaylandObject]:
    """
    Calls Qt's 'QWaylandObject
    *QWaylandCompositorExtension::extensionContainer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html

    Returns
    -------

    Optional[QWaylandObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandObject *QWaylandCompositorExtension::extensionContainer()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QWaylandCompositorExtension18extensionContainerEv',
    )
    return QWaylandObject._cuteAt(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QWaylandCompositorExtension::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html#isInitialized
    """
    #  bool QWaylandCompositorExtension::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK27QWaylandCompositorExtension13isInitializedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandObject)
  @overload(NoneType)
  def setExtensionContainer(
      self,
      container: Optional[QWaylandObject],
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandCompositorExtension::setExtensionContainer(QWaylandObject
    *container)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html

    Parameters
    ----------

    container : Optional[QWaylandObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositorExtension::setExtensionContainer(QWaylandObject
    #      *container)
    self.uglySide.call(
        'ritual_ZN27QWaylandCompositorExtension21setExtensionContainerEP14Q'
        'WaylandObject',
        self._addressOf(container),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandCompositorExtension::QWaylandCompositorExtension()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html
    """
    #  QWaylandCompositorExtension::QWaylandCompositorExtension()
    self._noteCreation(QWaylandCompositorExtension, lambda: Rituals.call(
        'ritual_ZN27QWaylandCompositorExtensionC1Ev',
    ))

  @overload(QWaylandObject)
  @overload(NoneType)
  def __init__(self, container: Optional[QWaylandObject]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandCompositorExtension::QWaylandCompositorExtension(QWaylandObject
    *container)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html

    Parameters
    ----------

    container : Optional[QWaylandObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandCompositorExtension::QWaylandCompositorExtension(
    #      QWaylandObject *container)
    self._noteCreation(QWaylandCompositorExtension, lambda: Rituals.call(
        'ritual_ZN27QWaylandCompositorExtensionC1EP14QWaylandObject',
        self._addressOf(container),
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

  def d_func(self) -> Optional[QWaylandCompositorExtensionPrivate]:
    """
    Calls Qt's 'QWaylandCompositorExtensionPrivate
    *QWaylandCompositorExtension::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html#d_func

    Returns
    -------

    Optional[QWaylandCompositorExtensionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositorExtensionPrivate
    #      *QWaylandCompositorExtension::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QWaylandCompositorExtension6d_funcEv',
    )
    from . import QWaylandCompositorExtensionPrivate
    return QWaylandCompositorExtensionPrivate._cuteAt(address)

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandCompositorExtension::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html#initialize
    """
    #  void QWaylandCompositorExtension::initialize()
    ritual = 'ritual_ZN27QWaylandCompositorExtension10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QWaylandCompositorExtension10initializeEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWaylandCompositorExtension::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextension.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWaylandCompositorExtension::event(QEvent *event)
    ritual = 'ritual_ZN27QWaylandCompositorExtension5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QWaylandCompositorExtension5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def extensionInterface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface
    *QWaylandCompositorExtension::extensionInterface() const': gives 'struct
    wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandCompositorExtension.extensionInterface' has no cute "
        "function yet. Qt's 'const struct wl_interface "
        "*QWaylandCompositorExtension::extensionInterface() const': gives "
        "'struct wl_interface', which has no cute class yet.")


#  Qt's 'QList<QWaylandCompositorExtension *>': the list of
#  QWaylandCompositorExtension, which 'QList[QWaylandCompositorExtension]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QWaylandCompositorExtension.
QList.createKind(
    QWaylandCompositorExtension, 'address',
    make='ritual_list_make_QWaylandCompositorExtension_ptr',
    add='ritual_list_add_QWaylandCompositorExtension_ptr',
    size='ritual_list_size_QWaylandCompositorExtension_ptr',
    at='ritual_list_at_QWaylandCompositorExtension_ptr',
    drop='ritual_list_drop_QWaylandCompositorExtension_ptr',
)
