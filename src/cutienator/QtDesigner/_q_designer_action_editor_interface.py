"""
QDesignerActionEditorInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractactioneditor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QAction
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerActionEditorInterface(QWidget):
  """
  The cute side of Qt's QDesignerActionEditorInterface: a plain Python object
  standing in front of one C++ QDesignerActionEditorInterface.

  It is built on the cute 'QWidget', as Qt's QDesignerActionEditorInterface
  is built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerActionEditorInterface that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr', 'core',
  'manageAction', 'unmanageAction', 'setFormWindow'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerActionEditorInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDesignerActionEditorInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerActionEditorInterface::~QDesignerActionEditorInterface()':
    the destructor: Python never removes a C++
    QDesignerActionEditorInterface.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerActionEditorInterface is created at the first use, not
    by 'QDesignerActionEditorInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerActionEditorInterface.
  - Qt tells when it has removed the C++ QDesignerActionEditorInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDesignerActionEditorInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html#tr

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
    #  QString QDesignerActionEditorInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QDesignerActionEditorInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerActionEditorInterface'

  #  A C++ QDesignerActionEditorInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerActionEditorInterface'

  #  The functions Qt calls itself that QDesignerActionEditorInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'core': (
          ('_ZNK30QDesignerActionEditorInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'manageAction': (
          ('_ZN30QDesignerActionEditorInterface12manageActionEP7QAction',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QAction'),
           )),
      ),
      'unmanageAction': (
          ('_ZN30QDesignerActionEditorInterface14unmanageActionEP7QAction',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QAction'),
           )),
      ),
      'setFormWindow': (
          ('_ZN30QDesignerActionEditorInterface13setFormWindowEP28QDesigner'
           'FormWindowInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDesignerActionEditorInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerActionEditorInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerActionEditorInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerActionEditorInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerActionEditorInterface::core()
    #      const
    ritual = 'ritual_ZNK30QDesignerActionEditorInterface4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QDesignerActionEditorInterface4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def setFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerActionEditorInterface::setFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html#setFormWindow

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerActionEditorInterface::setFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN30QDesignerActionEditorInterface13setFormWindowEP28QDesig'
        'nerFormWindowInterface',
        self._addressOf(formWindow),
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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget],
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerActionEditorInterface::QDesignerActionEditorInterface(QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QDesignerActionEditorInterface::QDesignerActionEditorInterface(QWidget
    #      *parent, Qt::WindowFlags flags)
    self._noteCreation(QDesignerActionEditorInterface, lambda: Rituals.call(
        'ritual_ZN30QDesignerActionEditorInterfaceC1EP7QWidget6QFlagsIN2Qt1'
        '0WindowTypeEE',
        self._addressOf(parent), flags.value,
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

  @overload(QAction)
  @overload(NoneType)
  def manageAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerActionEditorInterface::manageAction(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html#manageAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerActionEditorInterface::manageAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN30QDesignerActionEditorInterface12manageActionEP7QAction',
        self._addressOf(action),
    )

  @overload(QAction)
  @overload(NoneType)
  def unmanageAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerActionEditorInterface::unmanageAction(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractioneditorinterface.html#unmanageAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerActionEditorInterface::unmanageAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN30QDesignerActionEditorInterface14unmanageActionEP7QActio'
        'n',
        self._addressOf(action),
    )
