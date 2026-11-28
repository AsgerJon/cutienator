"""
QGStreamerVideoSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qgstreamervideosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGStreamerVideoSourcePrivate to be private: it declares the class
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

  from . import QGStreamerVideoSource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGStreamerVideoSource = WAIT['QGStreamerVideoSource']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGStreamerVideoSourcePrivate(QObjectPrivate):
  """
  The cute side of Qt's QGStreamerVideoSourcePrivate: a plain Python object
  standing in front of one C++ QGStreamerVideoSourcePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QGStreamerVideoSourcePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGStreamerVideoSourcePrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func', 'get'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGStreamerVideoSource *QGStreamerVideoSourcePrivate::q_func()
    const': takes in Python what 'QGStreamerVideoSource
    *QGStreamerVideoSourcePrivate::q_func()' takes.
  - Qt's 'void
    QGStreamerVideoSourcePrivate::createPlatformCamera(QGStreamerVideoSource
    *source, GstElementOrDescription elementOrDesc, bool active)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGStreamerVideoSourcePrivate is created at the first use, not by
    'QGStreamerVideoSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGStreamerVideoSourcePrivate.
  - Each name of Qt's QGStreamerVideoSourcePrivate that has no cute function
    yet, 'createPlatformCamera', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGStreamerVideoSource)
  @overload(NoneType)
  def get(
      source: Optional[QGStreamerVideoSource],
  ) -> Optional[QGStreamerVideoSourcePrivate]:
    """
    Calls Qt's 'QGStreamerVideoSourcePrivate
    *QGStreamerVideoSourcePrivate::get(QGStreamerVideoSource *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosourceprivate.html#get

    Parameters
    ----------

    source : Optional[QGStreamerVideoSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGStreamerVideoSourcePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGStreamerVideoSourcePrivate
    #      *QGStreamerVideoSourcePrivate::get(QGStreamerVideoSource *source)
    address = Rituals.call(
        'ritual_ZN28QGStreamerVideoSourcePrivate3getEP21QGStreamerVideoSour'
        'ce',
        CuteMixin._addressOf(source),
    )
    return QGStreamerVideoSourcePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGStreamerVideoSourcePrivate'

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

  def q_func(self) -> Optional[QGStreamerVideoSource]:
    """
    Calls Qt's 'QGStreamerVideoSource
    *QGStreamerVideoSourcePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosourceprivate.html#q_func

    Returns
    -------

    Optional[QGStreamerVideoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGStreamerVideoSource *QGStreamerVideoSourcePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QGStreamerVideoSourcePrivate6q_funcEv',
    )
    from . import QGStreamerVideoSource
    return QGStreamerVideoSource._cuteAt(address)

  @staticmethod
  def createPlatformCamera(*__, **_) -> Never:
    """
    Qt's 'void
    QGStreamerVideoSourcePrivate::createPlatformCamera(QGStreamerVideoSource
    *source, GstElementOrDescription elementOrDesc, bool active)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGStreamerVideoSourcePrivate.createPlatformCamera' has no cute "
        "function yet. Qt's 'void "
        "QGStreamerVideoSourcePrivate::createPlatformCamera(QGStreamerVideoS"
        "ource *source, GstElementOrDescription elementOrDesc, bool "
        "active)': takes a type Python has no way to hand over yet.")
