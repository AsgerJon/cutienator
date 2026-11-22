"""
QAccessibleActionInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleActionInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleActionInterface: a plain Python object
  standing in front of one C++ QAccessibleActionInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleActionInterface that has a ritual and
  that Python can call so far, 17 names in all: 'tr', 'localizedActionName',
  'localizedActionDescription', 'doAction', 'pressAction', 'increaseAction',
  'decreaseAction', 'showMenuAction', 'setFocusAction', 'showOnScreenAction',
  'toggleAction', 'scrollLeftAction', 'scrollRightAction', 'scrollUpAction',
  'scrollDownAction', 'nextPageAction', 'previousPageAction'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleActionInterface::~QAccessibleActionInterface()': the
    destructor: Python never removes a C++ QAccessibleActionInterface.

  What has no ritual
  ------------------

  7 of the 25 functions Qt declares: 4 forbidden; 2 takes or gives a type
  that cannot be passed yet; 1 the class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleActionInterface is created at the first use, not by
    'QAccessibleActionInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleActionInterface.
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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::tr(const char
    *sourceText, const char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleactioninterface.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::tr(const char *sourceText, const
    #      char *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  def pressAction() -> str:
    """
    Calls Qt's 'const QString &QAccessibleActionInterface::pressAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#pressAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::pressAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface11pressActionEv',
    )

  @staticmethod
  def increaseAction() -> str:
    """
    Calls Qt's 'const QString &QAccessibleActionInterface::increaseAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#increaseAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::increaseAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface14increaseActionEv',
    )

  @staticmethod
  def decreaseAction() -> str:
    """
    Calls Qt's 'const QString &QAccessibleActionInterface::decreaseAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#decreaseAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::decreaseAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface14decreaseActionEv',
    )

  @staticmethod
  def showMenuAction() -> str:
    """
    Calls Qt's 'const QString &QAccessibleActionInterface::showMenuAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#showMenuAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::showMenuAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface14showMenuActionEv',
    )

  @staticmethod
  def setFocusAction() -> str:
    """
    Calls Qt's 'const QString &QAccessibleActionInterface::setFocusAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#setFocusAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::setFocusAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface14setFocusActionEv',
    )

  @staticmethod
  def showOnScreenAction() -> str:
    """
    Calls Qt's 'const QString
    &QAccessibleActionInterface::showOnScreenAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#showOnScreenAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::showOnScreenAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface18showOnScreenActionEv',
    )

  @staticmethod
  def toggleAction() -> str:
    """
    Calls Qt's 'const QString &QAccessibleActionInterface::toggleAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#toggleAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QAccessibleActionInterface::toggleAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface12toggleActionEv',
    )

  @staticmethod
  def scrollLeftAction() -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::scrollLeftAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#scrollLeftAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::scrollLeftAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface16scrollLeftActionEv',
    )

  @staticmethod
  def scrollRightAction() -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::scrollRightAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#scrollRightAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::scrollRightAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface17scrollRightActionEv',
    )

  @staticmethod
  def scrollUpAction() -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::scrollUpAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#scrollUpAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::scrollUpAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface14scrollUpActionEv',
    )

  @staticmethod
  def scrollDownAction() -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::scrollDownAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#scrollDownAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::scrollDownAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface16scrollDownActionEv',
    )

  @staticmethod
  def nextPageAction() -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::nextPageAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#nextPageAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::nextPageAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface14nextPageActionEv',
    )

  @staticmethod
  def previousPageAction() -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::previousPageAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#previousPageAction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::previousPageAction()
    return Rituals.call(
        'ritual_ZN26QAccessibleActionInterface18previousPageActionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleActionInterface'

  #  A C++ QAccessibleActionInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleActionInterface'

  #  The functions Qt calls itself that QAccessibleActionInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'actionNames': (
          'QStringList QAccessibleActionInterface::actionNames() const',
      ),
      'keyBindingsForAction': (
          'QStringList '
          'QAccessibleActionInterface::keyBindingsForAction(const QString '
          '&) const',
      ),
  }

  #  The functions Qt calls itself that QAccessibleActionInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'localizedActionName': (
          ('_ZNK26QAccessibleActionInterface19localizedActionNameERK7QStrin'
           'g',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'localizedActionDescription': (
          ('_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK'
           '7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'doAction': (
          ('_ZN26QAccessibleActionInterface8doActionERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
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

  @overload(str)
  def localizedActionName(self, name: str) -> str:
    """
    Calls Qt's 'QString QAccessibleActionInterface::localizedActionName(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::localizedActionName(const QString
    #      &name) const
    ritual = (
        'ritual_ZNK26QAccessibleActionInterface19localizedActionNameERK7QSt'
        'ring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleActionInterface19localizedActionNameE'
          'RK7QString')
    return self._callAs('QAccessibleActionInterface', ritual, name)

  @overload(str)
  def localizedActionDescription(self, name: str) -> str:
    """
    Calls Qt's 'QString
    QAccessibleActionInterface::localizedActionDescription(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleActionInterface::localizedActionDescription(const
    #      QString &name) const
    ritual = (
        'ritual_ZNK26QAccessibleActionInterface26localizedActionDescription'
        'ERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleActionInterface26localizedActionDescr'
          'iptionERK7QString')
    return self._callAs('QAccessibleActionInterface', ritual, name)

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

  @overload(str)
  def doAction(self, actionName: str) -> None:
    """
    Calls Qt's 'void QAccessibleActionInterface::doAction(const QString
    &actionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleactioninterface.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleActionInterface::doAction(const QString &actionName)
    self._callAs(
        'QAccessibleActionInterface',
        'ritual_ZN26QAccessibleActionInterface8doActionERK7QString',
        actionName,
    )
