"""
QRemoteObjectHostPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectHostPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRemoteObjectHostBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRemoteObjectHost


class QRemoteObjectHostPrivate(QRemoteObjectHostBasePrivate):
  """
  The cute side of Qt's QRemoteObjectHostPrivate: a plain Python object
  standing in front of one C++ QRemoteObjectHostPrivate.

  It is built on the cute 'QRemoteObjectHostBasePrivate', as Qt's
  QRemoteObjectHostPrivate is built on Qt's QRemoteObjectHostBasePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectHostPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectHostPrivate::~QRemoteObjectHostPrivate()': the
    destructor: Python never removes a C++ QRemoteObjectHostPrivate.
  - Qt's 'const QRemoteObjectHost *QRemoteObjectHostPrivate::q_func() const':
    takes in Python what 'QRemoteObjectHost
    *QRemoteObjectHostPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 leans on 'QRemoteObjectHostBasePrivate;
  1 leans on 'QRemoteObjectSourceBase.

  What to expect
  --------------

  - The C++ QRemoteObjectHostPrivate is created at the first use, not by
    'QRemoteObjectHostPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectHostPrivate.
  - Each name of Qt's QRemoteObjectHostPrivate that has no cute function yet,
    '__init__', 'setHostUrlHostImpl', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectHostPrivate'

  #  A C++ QRemoteObjectHostPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectHostPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectHostPrivate::QRemoteObjectHostPrivate()': leans on
    'QRemoteObjectSourceBase::qobjectPropertyOffset', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostPrivate.__init__' has no cute function yet. Qt's "
        "'QRemoteObjectHostPrivate::QRemoteObjectHostPrivate()': leans on "
        "'QRemoteObjectSourceBase::qobjectPropertyOffset', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[QRemoteObjectHost]:
    """
    Calls Qt's 'QRemoteObjectHost *QRemoteObjectHostPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostprivate.html#q_func

    Returns
    -------

    Optional[QRemoteObjectHost]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectHost *QRemoteObjectHostPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QRemoteObjectHostPrivate6q_funcEv',
    )
    from . import QRemoteObjectHost
    return QRemoteObjectHost._cuteAt(address)

  @staticmethod
  def setHostUrlHostImpl(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectHostPrivate::setHostUrlHostImpl(const QUrl
    &hostAddress, QRemoteObjectHostBase::AllowedSchemas allowedSchemas)':
    leans on 'QRemoteObjectHostBasePrivate::setHostUrlBaseImpl(QUrl const&,
    QRemoteObjectHostBase::AllowedSchemas)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostPrivate.setHostUrlHostImpl' has no cute function "
        "yet. Qt's 'bool QRemoteObjectHostPrivate::setHostUrlHostImpl(const "
        "QUrl &hostAddress, QRemoteObjectHostBase::AllowedSchemas "
        "allowedSchemas)': leans on "
        "'QRemoteObjectHostBasePrivate::setHostUrlBaseImpl(QUrl const&, "
        "QRemoteObjectHostBase::AllowedSchemas)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
