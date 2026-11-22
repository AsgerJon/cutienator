"""
QErrorMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qerrormessage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QErrorMessage(QDialog):
  """
  The cute side of Qt's QErrorMessage: a plain Python object standing in
  front of one C++ QErrorMessage.

  It is built on the cute 'QDialog', as Qt's QErrorMessage is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QErrorMessage that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'qtHandler',
  'showMessage', 'done', 'changeEvent'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QErrorMessage::~QErrorMessage()': the destructor: Python never
    removes a C++ QErrorMessage.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QErrorMessage is created at the first use, not by
    'QErrorMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QErrorMessage.
  - Qt tells when it has removed the C++ QErrorMessage. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QErrorMessage::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#tr

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
    #  QString QErrorMessage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QErrorMessage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qtHandler() -> Optional[QErrorMessage]:
    """
    Calls Qt's 'QErrorMessage *QErrorMessage::qtHandler()'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#qtHandler

    Returns
    -------

    Optional[QErrorMessage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QErrorMessage *QErrorMessage::qtHandler()
    address = Rituals.call('ritual_ZN13QErrorMessage9qtHandlerEv')
    return QErrorMessage._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QErrorMessage'

  #  A C++ QErrorMessage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QErrorMessage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QErrorMessage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QErrorMessage::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QErrorMessage10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QErrorMessage::QErrorMessage(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#QErrorMessage

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QErrorMessage::QErrorMessage(QWidget *parent)
    self._noteCreation(QErrorMessage, lambda: Rituals.call(
        'ritual_ZN13QErrorMessageC1EP7QWidget', self._addressOf(parent),
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

  @overload(str)
  def showMessage(self, message: str) -> None:
    """
    Calls Qt's 'void QErrorMessage::showMessage(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#showMessage

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QErrorMessage::showMessage(const QString &message)
    self.uglySide.call(
        'ritual_ZN13QErrorMessage11showMessageERK7QString', message,
    )

  @overload(str, str)
  def showMessage(self, message: str, type: str) -> None:
    """
    Calls Qt's 'void QErrorMessage::showMessage(const QString &message, const
    QString &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#showMessage

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QErrorMessage::showMessage(const QString &message, const QString
    #      &type)
    self.uglySide.call(
        'ritual_ZN13QErrorMessage11showMessageERK7QStringS2_', message, type,
    )

  @overload(int)
  def done(self, a0: int) -> None:
    """
    Calls Qt's 'void QErrorMessage::done(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#done

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QErrorMessage::done(int a0)
    self.uglySide.call('ritual_own_ZN13QErrorMessage4doneEi', a0)

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QErrorMessage::changeEvent(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qerrormessage.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QErrorMessage::changeEvent(QEvent *e)
    self.uglySide.call(
        'ritual_own_ZN13QErrorMessage11changeEventEP6QEvent',
        self._addressOf(e),
    )
