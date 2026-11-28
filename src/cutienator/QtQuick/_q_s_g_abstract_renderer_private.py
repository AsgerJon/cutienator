"""
QSGAbstractRendererPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGAbstractRendererPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSGAbstractRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGAbstractRenderer = WAIT['QSGAbstractRenderer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGAbstractRendererPrivate(QObjectPrivate):
  """
  The cute side of Qt's QSGAbstractRendererPrivate: a plain Python object
  standing in front of one C++ QSGAbstractRendererPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QSGAbstractRendererPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGAbstractRendererPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func', 'get'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSGAbstractRenderer *QSGAbstractRendererPrivate::q_func()
    const': takes in Python what 'QSGAbstractRenderer
    *QSGAbstractRendererPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSGAbstractRendererPrivate is created at the first use, not by
    'QSGAbstractRendererPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGAbstractRendererPrivate.
  - Each name of Qt's QSGAbstractRendererPrivate that has no cute function
    yet, 'updateProjectionMatrix', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSGAbstractRenderer)
  @overload(NoneType)
  def get(
      q: Optional[QSGAbstractRenderer],
  ) -> Optional[QSGAbstractRendererPrivate]:
    """
    Calls Qt's 'const QSGAbstractRendererPrivate
    *QSGAbstractRendererPrivate::get(const QSGAbstractRenderer *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrendererprivate.html#get

    Parameters
    ----------

    q : Optional[QSGAbstractRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGAbstractRendererPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGAbstractRendererPrivate
    #      *QSGAbstractRendererPrivate::get(const QSGAbstractRenderer *q)
    address = Rituals.call(
        'ritual_ZN26QSGAbstractRendererPrivate3getEPK19QSGAbstractRenderer',
        CuteMixin._addressOf(q),
    )
    return QSGAbstractRendererPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGAbstractRendererPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QSGAbstractRendererPrivate::QSGAbstractRendererPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrendererprivate.html
    """
    #  QSGAbstractRendererPrivate::QSGAbstractRendererPrivate()
    self._noteCreation(QSGAbstractRendererPrivate, lambda: Rituals.call(
        'ritual_ZN26QSGAbstractRendererPrivateC1Ev',
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

  def q_func(self) -> Optional[QSGAbstractRenderer]:
    """
    Calls Qt's 'QSGAbstractRenderer *QSGAbstractRendererPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrendererprivate.html#q_func

    Returns
    -------

    Optional[QSGAbstractRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGAbstractRenderer *QSGAbstractRendererPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QSGAbstractRendererPrivate6q_funcEv',
    )
    from . import QSGAbstractRenderer
    return QSGAbstractRenderer._cuteAt(address)

  @staticmethod
  def updateProjectionMatrix(*__, **_) -> Never:
    """
    Qt's 'void QSGAbstractRendererPrivate::updateProjectionMatrix()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QSGAbstractRendererPrivate.updateProjectionMatrix' has no cute "
        "function yet. Qt's 'void "
        "QSGAbstractRendererPrivate::updateProjectionMatrix()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
