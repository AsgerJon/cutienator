"""
Qt3DRender::QShaderProgramPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qshaderprogram_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QShaderProgramPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QShaderProgramPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QShaderProgramPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QShaderProgramPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DRender::QShaderProgramPrivate is built on Qt's Qt3DCore::QNodePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderProgramPrivate that has a ritual
  and that Python can call so far, 5 names in all: 'q_func', 'setLog',
  'setStatus', 'deincludify', 'resolveAutoBindingIndices'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QShaderProgram *Qt3DRender::QShaderProgramPrivate::q_func()
    const': takes in Python what 'QShaderProgram
    *Qt3DRender::QShaderProgramPrivate::q_func()' takes.
  - Qt's 'QByteArray
    Qt3DRender::QShaderProgramPrivate::resolveAutoBindingIndices(const
    QByteArray &content, int &currentBinding, int &currentInputLocation, int
    &currentOutputLocation)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderProgramPrivate is created at the first use,
    not by 'Qt3DRender::QShaderProgramPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QShaderProgramPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, str)
  def deincludify(contents: QByteArray, filePath: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramPrivate::deincludify(const QByteArray
    &contents, const QString &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html#deincludify

    Parameters
    ----------

    contents : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramPrivate::deincludify(const
    #      QByteArray &contents, const QString &filePath)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivate11deincludifyERK10QByt'
        'eArrayRK7QString',
        CuteMixin._valueOf(contents), filePath,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(str)
  def deincludify(filePath: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramPrivate::deincludify(const QString &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html#deincludify

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramPrivate::deincludify(const
    #      QString &filePath)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivate11deincludifyERK7QStri'
        'ng',
        filePath,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def resolveAutoBindingIndices(content: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramPrivate::resolveAutoBindingIndices(const
    QByteArray &content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html

    Parameters
    ----------

    content : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DRender::QShaderProgramPrivate::resolveAutoBindingIndices(const
    #      QByteArray &content)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivate25resolveAutoBindingIn'
        'dicesERK10QByteArray',
        CuteMixin._valueOf(content),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QShaderProgramPrivate'

  #  A C++ Qt3DRender::QShaderProgramPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QShaderProgramPrivate'

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

  @overload(str)
  def setLog(self, log: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgramPrivate::setLog(const QString
    &log)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html#setLog

    Parameters
    ----------

    log : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QShaderProgramPrivate::setLog(const QString &log)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivate6setLogERK7QString',
        log,
    )

  @overload(Qt3DRender.QShaderProgram.Status)
  def setStatus(self, status: Qt3DRender.QShaderProgram.Status) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramPrivate::setStatus(QShaderProgram::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html#setStatus

    Parameters
    ----------

    status : Qt3DRender.QShaderProgram.Status
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderProgramPrivate::setStatus(QShaderProgram::
    #      Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivate9setStatusENS_14QShade'
        'rProgram6StatusE',
        status.value,
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
    'Qt3DRender::QShaderProgramPrivate::QShaderProgramPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html
    """
    #  Qt3DRender::QShaderProgramPrivate::QShaderProgramPrivate()
    self._noteCreation(QShaderProgramPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QShaderProgram]:
    """
    Calls Qt's 'QShaderProgram *Qt3DRender::QShaderProgramPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogramprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderProgram *Qt3DRender::QShaderProgramPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramPrivate6q_funcEv',
    )
    return Qt3DRender.QShaderProgram._cuteAt(address)
