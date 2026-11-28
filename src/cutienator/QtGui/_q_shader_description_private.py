"""
QShaderDescriptionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qshaderdescription_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QShaderDescriptionPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDataStream, QJsonDocument
  from . import QShaderDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDataStream = WAIT['QDataStream']
  QShaderDescription = WAIT['QShaderDescription']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderDescriptionPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderDescriptionPrivate: a plain Python object
  standing in front of one C++ QShaderDescriptionPrivate.

  C++ hands a QShaderDescriptionPrivate around as a copy, so every C++
  QShaderDescriptionPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShaderDescriptionPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'get', 'makeDoc', 'writeToStream',
  'loadFromStream'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QShaderDescriptionPrivate
    *QShaderDescriptionPrivate::get(const QShaderDescription *desc)': takes
    in Python what 'QShaderDescriptionPrivate
    *QShaderDescriptionPrivate::get(QShaderDescription *desc)' takes.
  - Qt's 'QShaderDescriptionPrivate::~QShaderDescriptionPrivate()': the
    destructor: Python removes its C++ QShaderDescriptionPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QShaderDescriptionPrivate is created at the first use, not by
    'QShaderDescriptionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShaderDescriptionPrivate back gives a copy the
    ritual made for Python, in a new cute QShaderDescriptionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QShaderDescription)
  @overload(NoneType)
  def get(
      desc: Optional[QShaderDescription],
  ) -> Optional[QShaderDescriptionPrivate]:
    """
    Calls Qt's 'QShaderDescriptionPrivate
    *QShaderDescriptionPrivate::get(QShaderDescription *desc)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescriptionprivate.html#get

    Parameters
    ----------

    desc : Optional[QShaderDescription]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QShaderDescriptionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderDescriptionPrivate
    #      *QShaderDescriptionPrivate::get(QShaderDescription *desc)
    address = Rituals.call(
        'ritual_ZN25QShaderDescriptionPrivate3getEP18QShaderDescription',
        CuteMixin._addressOf(desc),
    )
    return QShaderDescriptionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderDescriptionPrivate'

  #  Qt's '~QShaderDescriptionPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QShaderDescriptionPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QShaderDescriptionPrivateD1Ev'

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
    'QShaderDescriptionPrivate::QShaderDescriptionPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescriptionprivate.html
    """
    #  QShaderDescriptionPrivate::QShaderDescriptionPrivate()
    self._noteCreation(QShaderDescriptionPrivate, lambda: Rituals.call(
        'ritual_ZN25QShaderDescriptionPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QShaderDescriptionPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QShaderDescriptionPrivate::QShaderDescriptionPrivate(const
    QShaderDescriptionPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescriptionprivate.html

    Parameters
    ----------

    other : QShaderDescriptionPrivate
      Passed on as a value: Qt reads the C++ QShaderDescriptionPrivate, which
      stays Python's own.
    """
    #  QShaderDescriptionPrivate::QShaderDescriptionPrivate(const
    #      QShaderDescriptionPrivate &other)
    self._noteCreation(QShaderDescriptionPrivate, lambda: Rituals.call(
        'ritual_ZN25QShaderDescriptionPrivateC1ERKS_', self._valueOf(other),
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

  def makeDoc(self) -> QJsonDocument:
    """
    Calls Qt's 'QJsonDocument QShaderDescriptionPrivate::makeDoc()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescriptionprivate.html#makeDoc

    Returns
    -------

    QJsonDocument
      A new cute QJsonDocument around the copy Qt gave back. Python owns it.
    """
    #  QJsonDocument QShaderDescriptionPrivate::makeDoc()
    address = self.uglySide.call(
        'ritual_ZN25QShaderDescriptionPrivate7makeDocEv',
    )
    from ..QtCore import QJsonDocument
    return QJsonDocument._cuteOwning(address)

  @overload(QDataStream, int)
  @overload(NoneType, int)
  def writeToStream(
      self,
      stream: Optional[QDataStream],
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QShaderDescriptionPrivate::writeToStream(QDataStream
    *stream, int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescriptionprivate.html#writeToStream

    Parameters
    ----------

    stream : Optional[QDataStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : int
      Passed on as it is.
    """
    #  void QShaderDescriptionPrivate::writeToStream(QDataStream *stream, int
    #      version)
    self.uglySide.call(
        'ritual_ZN25QShaderDescriptionPrivate13writeToStreamEP11QDataStream'
        'i',
        self._addressOf(stream), version,
    )

  @overload(QDataStream, int)
  @overload(NoneType, int)
  def loadFromStream(
      self,
      stream: Optional[QDataStream],
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QShaderDescriptionPrivate::loadFromStream(QDataStream
    *stream, int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescriptionprivate.html#loadFromStream

    Parameters
    ----------

    stream : Optional[QDataStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : int
      Passed on as it is.
    """
    #  void QShaderDescriptionPrivate::loadFromStream(QDataStream *stream,
    #      int version)
    self.uglySide.call(
        'ritual_ZN25QShaderDescriptionPrivate14loadFromStreamEP11QDataStrea'
        'mi',
        self._addressOf(stream), version,
    )
