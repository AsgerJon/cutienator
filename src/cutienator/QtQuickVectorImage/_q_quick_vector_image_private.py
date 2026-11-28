"""
QQuickVectorImagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimage_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickVectorImagePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickVectorImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickVectorImage = WAIT['QQuickVectorImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickVectorImagePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickVectorImagePrivate: a plain Python object
  standing in front of one C++ QQuickVectorImagePrivate.

  What exists
  -----------

  Every function of Qt's QQuickVectorImagePrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'get'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickVectorImage *QQuickVectorImagePrivate::q_func() const':
    takes in Python what 'QQuickVectorImage
    *QQuickVectorImagePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickVectorImagePrivate.

  What to expect
  --------------

  - The C++ QQuickVectorImagePrivate is created at the first use, not by
    'QQuickVectorImagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickVectorImagePrivate.
  - Each name of Qt's QQuickVectorImagePrivate that has no cute function yet,
    'loadFile', 'setSource', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickVectorImage)
  @overload(NoneType)
  def get(
      q: Optional[QQuickVectorImage],
  ) -> Optional[QQuickVectorImagePrivate]:
    """
    Calls Qt's 'QQuickVectorImagePrivate
    *QQuickVectorImagePrivate::get(QQuickVectorImage *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimageprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickVectorImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickVectorImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickVectorImagePrivate
    #      *QQuickVectorImagePrivate::get(QQuickVectorImage *q)
    address = Rituals.call(
        'ritual_ZN24QQuickVectorImagePrivate3getEP17QQuickVectorImage',
        CuteMixin._addressOf(q),
    )
    return QQuickVectorImagePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVectorImagePrivate'

  #  A C++ QQuickVectorImagePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickVectorImagePrivate'

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
    'QQuickVectorImagePrivate::QQuickVectorImagePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageprivate.html
    """
    #  QQuickVectorImagePrivate::QQuickVectorImagePrivate()
    self._noteCreation(QQuickVectorImagePrivate, lambda: Rituals.call(
        'ritual_ZN24QQuickVectorImagePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickVectorImage]:
    """
    Calls Qt's 'QQuickVectorImage *QQuickVectorImagePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageprivate.html#q_func

    Returns
    -------

    Optional[QQuickVectorImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickVectorImage *QQuickVectorImagePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickVectorImagePrivate6q_funcEv',
    )
    from . import QQuickVectorImage
    return QQuickVectorImage._cuteAt(address)

  @staticmethod
  def loadFile(*__, **_) -> Never:
    """
    Qt's 'void QQuickVectorImagePrivate::loadFile()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickVectorImageIncubator'.
    """
    raise NotImplementedError(
        "'QQuickVectorImagePrivate.loadFile' has no cute function yet. Qt's "
        "'void QQuickVectorImagePrivate::loadFile()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuickVectorImageIncubator'.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickVectorImagePrivate::setSource(const QUrl &source)':
    leans on 'QQuickVectorImagePrivate::loadFile()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickVectorImagePrivate.setSource' has no cute function yet. "
        "Qt's 'void QQuickVectorImagePrivate::setSource(const QUrl "
        "&source)': leans on 'QQuickVectorImagePrivate::loadFile()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
