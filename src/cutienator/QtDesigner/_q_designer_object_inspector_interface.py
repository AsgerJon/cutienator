"""
QDesignerObjectInspectorInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractobjectinspector.h, Qt 6.12.0. Changes made here are
#  lost.
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
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerObjectInspectorInterface(QWidget):
  """
  The cute side of Qt's QDesignerObjectInspectorInterface: a plain Python
  object standing in front of one C++ QDesignerObjectInspectorInterface.

  It is built on the cute 'QWidget', as Qt's
  QDesignerObjectInspectorInterface is built on Qt's QWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerObjectInspectorInterface that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'core', 'setFormWindow'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerObjectInspectorInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDesignerObjectInspectorInterface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerObjectInspectorInterface::~QDesignerObjectInspectorInterface(
    )': the destructor: Python never removes a C++
    QDesignerObjectInspectorInterface.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerObjectInspectorInterface is created at the first use,
    not by 'QDesignerObjectInspectorInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerObjectInspectorInterface.
  - Qt tells when it has removed the C++ QDesignerObjectInspectorInterface.
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
    Calls Qt's 'QString QDesignerObjectInspectorInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerobjectinspectorinterface.html#tr

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
    #  QString QDesignerObjectInspectorInterface::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QDesignerObjectInspectorInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerObjectInspectorInterface'

  #  A C++ QDesignerObjectInspectorInterface Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerObjectInspectorInterface'

  #  The functions Qt calls itself that QDesignerObjectInspectorInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'core': (
          ('_ZNK33QDesignerObjectInspectorInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'setFormWindow': (
          ('_ZN33QDesignerObjectInspectorInterface13setFormWindowEP28QDesig'
           'nerFormWindowInterface',
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
    *QDesignerObjectInspectorInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerobjectinspectorinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerObjectInspectorInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QDesignerObjectInspectorInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerObjectInspectorInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerobjectinspectorinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *QDesignerObjectInspectorInterface::core() const
    ritual = 'ritual_ZNK33QDesignerObjectInspectorInterface4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK33QDesignerObjectInspectorInterface4coreEv'
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
    Calls Qt's 'void QDesignerObjectInspectorInterface::setFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerobjectinspectorinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerObjectInspectorInterface::setFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN33QDesignerObjectInspectorInterface13setFormWindowEP28QDe'
        'signerFormWindowInterface',
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
    'QDesignerObjectInspectorInterface::QDesignerObjectInspectorInterface(
    QWidget *parent, Qt::WindowFlags flags)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerobjectinspectorinterface.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QDesignerObjectInspectorInterface::
    #      QDesignerObjectInspectorInterface(QWidget *parent, Qt::WindowFlags
    #      flags)
    self._noteCreation(
        QDesignerObjectInspectorInterface, lambda: Rituals.call(
            'ritual_ZN33QDesignerObjectInspectorInterfaceC1EP7QWidget6QFlag'
            'sIN2Qt10WindowTypeEE',
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
