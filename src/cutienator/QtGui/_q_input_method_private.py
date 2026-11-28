"""
QInputMethodPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qinputmethod_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QInputMethodPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QInputMethod, QPlatformInputContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputMethod = WAIT['QInputMethod']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputMethodPrivate(QObjectPrivate):
  """
  The cute side of Qt's QInputMethodPrivate: a plain Python object standing
  in front of one C++ QInputMethodPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QInputMethodPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputMethodPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'platformInputContext',
  'get', 'objectAcceptsInputMethod'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QInputMethod *QInputMethodPrivate::q_func() const': takes in
    Python what 'QInputMethod *QInputMethodPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QInputMethodPrivate is created at the first use, not by
    'QInputMethodPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputMethodPrivate.
  - Each name of Qt's QInputMethodPrivate that has no cute function yet,
    '_q_checkFocusObject', '_q_connectFocusObject', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QInputMethod)
  @overload(NoneType)
  def get(
      inputMethod: Optional[QInputMethod],
  ) -> Optional[QInputMethodPrivate]:
    """
    Calls Qt's 'QInputMethodPrivate *QInputMethodPrivate::get(QInputMethod
    *inputMethod)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethodprivate.html#get

    Parameters
    ----------

    inputMethod : Optional[QInputMethod]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QInputMethodPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputMethodPrivate *QInputMethodPrivate::get(QInputMethod
    #      *inputMethod)
    address = Rituals.call(
        'ritual_ZN19QInputMethodPrivate3getEP12QInputMethod',
        CuteMixin._addressOf(inputMethod),
    )
    return QInputMethodPrivate._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def objectAcceptsInputMethod(object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QInputMethodPrivate::objectAcceptsInputMethod(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodprivate.html#objectAcceptsInputMethod

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QInputMethodPrivate::objectAcceptsInputMethod(QObject *object)
    return Rituals.call(
        'ritual_ZN19QInputMethodPrivate24objectAcceptsInputMethodEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputMethodPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def platformInputContext(self) -> Optional[QPlatformInputContext]:
    """
    Calls Qt's 'QPlatformInputContext
    *QInputMethodPrivate::platformInputContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodprivate.html#platformInputContext

    Returns
    -------

    Optional[QPlatformInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformInputContext *QInputMethodPrivate::platformInputContext()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QInputMethodPrivate20platformInputContextEv',
    )
    from . import QPlatformInputContext
    return QPlatformInputContext._cuteAt(address)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QInputMethodPrivate::QInputMethodPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodprivate.html#QInputMethodPrivate
    """
    #  QInputMethodPrivate::QInputMethodPrivate()
    self._noteCreation(QInputMethodPrivate, lambda: Rituals.call(
        'ritual_ZN19QInputMethodPrivateC1Ev',
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

  def q_func(self) -> Optional[QInputMethod]:
    """
    Calls Qt's 'QInputMethod *QInputMethodPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethodprivate.html#q_func

    Returns
    -------

    Optional[QInputMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputMethod *QInputMethodPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QInputMethodPrivate6q_funcEv')
    from . import QInputMethod
    return QInputMethod._cuteAt(address)

  @staticmethod
  def _q_checkFocusObject(*__, **_) -> Never:
    """
    Qt's 'void QInputMethodPrivate::_q_checkFocusObject(QObject *object)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QInputMethodPrivate._q_checkFocusObject' has no cute function "
        "yet. Qt's 'void QInputMethodPrivate::_q_checkFocusObject(QObject "
        "*object)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def _q_connectFocusObject(*__, **_) -> Never:
    """
    Qt's 'void QInputMethodPrivate::_q_connectFocusObject()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QInputMethodPrivate._q_connectFocusObject' has no cute function "
        "yet. Qt's 'void QInputMethodPrivate::_q_connectFocusObject()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
