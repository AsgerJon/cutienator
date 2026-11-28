"""
QActionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qaction_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QActionPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QActionPrivate(QObjectPrivate):
  """
  The cute side of Qt's QActionPrivate: a plain Python object standing in
  front of one C++ QActionPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QActionPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QActionPrivate that has a ritual and that Python can
  call so far, 9 names in all: 'q_func', 'destroy', 'get', 'setEnabled',
  'setVisible', 'menu', 'setMenu', 'showStatusText', 'sendDataChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAction *QActionPrivate::q_func() const': takes in Python
    what 'QAction *QActionPrivate::q_func()' takes.
  - Qt's 'QActionPrivate::~QActionPrivate()': the destructor: Python never
    removes a C++ QActionPrivate.
  - Qt's 'QShortcutMap::ContextMatcher QActionPrivate::contextMatcher()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QActionPrivate::redoGrab(QShortcutMap &map)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QActionPrivate::setShortcutEnabled(bool enable, QShortcutMap
    &map)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QActionPrivate is created at the first use, not by
    'QActionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QActionPrivate.
  - Each name of Qt's QActionPrivate that has no cute function yet,
    'contextMatcher', 'redoGrab', 'redoGrabAlternate', 'setShortcutEnabled',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAction)
  @overload(NoneType)
  def get(q: Optional[QAction]) -> Optional[QActionPrivate]:
    """
    Calls Qt's 'QActionPrivate *QActionPrivate::get(QAction *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#get

    Parameters
    ----------

    q : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionPrivate *QActionPrivate::get(QAction *q)
    address = Rituals.call(
        'ritual_ZN14QActionPrivate3getEP7QAction', CuteMixin._addressOf(q),
    )
    return QActionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QActionPrivate'

  #  A C++ QActionPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QActionPrivate'

  #  The functions Qt calls itself that QActionPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'contextMatcher': (
          'QShortcutMap::ContextMatcher QActionPrivate::contextMatcher() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QActionPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'destroy': (
          ('_ZN14QActionPrivate7destroyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'menu': (
          ('_ZNK14QActionPrivate4menuEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'setMenu': (
          ('_ZN14QActionPrivate7setMenuEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
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

  def menu(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QActionPrivate::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#menu

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QActionPrivate::menu() const
    ritual = 'ritual_ZNK14QActionPrivate4menuEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QActionPrivate4menuEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, bool)
  def setEnabled(self, enable: bool, byGroup: bool) -> bool:
    """
    Calls Qt's 'bool QActionPrivate::setEnabled(bool enable, bool byGroup)'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#setEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.

    byGroup : bool
      Passed on as it is.
    """
    #  bool QActionPrivate::setEnabled(bool enable, bool byGroup)
    return self.uglySide.call(
        'ritual_ZN14QActionPrivate10setEnabledEbb', enable, byGroup,
    )

  @overload(bool)
  def setVisible(self, b: bool) -> None:
    """
    Calls Qt's 'void QActionPrivate::setVisible(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#setVisible

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QActionPrivate::setVisible(bool b)
    self.uglySide.call('ritual_ZN14QActionPrivate10setVisibleEb', b)

  @overload(QObject)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QActionPrivate::setMenu(QObject *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#setMenu

    Parameters
    ----------

    menu : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QActionPrivate::setMenu(QObject *menu)
    ritual = 'ritual_ZN14QActionPrivate7setMenuEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QActionPrivate7setMenuEP7QObject'
    self.uglySide.call(ritual, self._addressOf(menu, 'QObject'))

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
    Notes what was given, for Qt's 'QActionPrivate::QActionPrivate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#QActionPrivate
    """
    #  QActionPrivate::QActionPrivate()
    self._noteCreation(QActionPrivate, lambda: Rituals.call(
        'ritual_ZN14QActionPrivateC1Ev',
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

  def q_func(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#q_func

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QActionPrivate6q_funcEv')
    from . import QAction
    return QAction._cuteAt(address)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QActionPrivate::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#destroy
    """
    #  void QActionPrivate::destroy()
    ritual = 'ritual_ZN14QActionPrivate7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QActionPrivate7destroyEv'
    self.uglySide.call(ritual)

  @overload(QObject, str)
  @overload(NoneType, str)
  def showStatusText(self, widget: Optional[QObject], str: str) -> bool:
    """
    Calls Qt's 'bool QActionPrivate::showStatusText(QObject *widget, const
    QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qactionprivate.html#showStatusText

    Parameters
    ----------

    widget : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QActionPrivate::showStatusText(QObject *widget, const QString
    #      &str)
    return self.uglySide.call(
        'ritual_ZN14QActionPrivate14showStatusTextEP7QObjectRK7QString',
        self._addressOf(widget, 'QObject'), str,
    )

  def sendDataChanged(self) -> None:
    """
    Calls Qt's 'void QActionPrivate::sendDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qactionprivate.html#sendDataChanged
    """
    #  void QActionPrivate::sendDataChanged()
    self.uglySide.call('ritual_ZN14QActionPrivate15sendDataChangedEv')

  @staticmethod
  def contextMatcher(*__, **_) -> Never:
    """
    Qt's 'QShortcutMap::ContextMatcher QActionPrivate::contextMatcher()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QActionPrivate.contextMatcher' has no cute function yet. Qt's "
        "'QShortcutMap::ContextMatcher QActionPrivate::contextMatcher() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def redoGrab(*__, **_) -> Never:
    """
    Qt's 'void QActionPrivate::redoGrab(QShortcutMap &map)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QActionPrivate.redoGrab' has no cute function yet. Qt's 'void "
        "QActionPrivate::redoGrab(QShortcutMap &map)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def redoGrabAlternate(*__, **_) -> Never:
    """
    Qt's 'void QActionPrivate::redoGrabAlternate(QShortcutMap &map)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QActionPrivate.redoGrabAlternate' has no cute function yet. Qt's "
        "'void QActionPrivate::redoGrabAlternate(QShortcutMap &map)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setShortcutEnabled(*__, **_) -> Never:
    """
    Qt's 'void QActionPrivate::setShortcutEnabled(bool enable, QShortcutMap
    &map)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QActionPrivate.setShortcutEnabled' has no cute function yet. Qt's "
        "'void QActionPrivate::setShortcutEnabled(bool enable, QShortcutMap "
        "&map)': takes a type Python has no way to hand over yet.")
