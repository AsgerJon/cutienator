"""
Qt3DCore::QAspectJobProviderInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qaspectjobproviderinterface_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DCore::QAspectJobProviderInterface to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QAspectJobProviderInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QAspectJobProviderInterface: a plain Python
  object standing in front of one C++ Qt3DCore::QAspectJobProviderInterface.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectJobProviderInterface that has a
  ritual and that Python can call so far, 2 names in all: 'jobsDone',
  'frameDone'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DCore::QAspectJobProviderInterface::~QAspectJobProviderInterface()':
    the destructor: Python never removes a C++
    Qt3DCore::QAspectJobProviderInterface.
  - Qt's 'std::vector<QAspectJobPtr>
    Qt3DCore::QAspectJobProviderInterface::jobsToExecute(qint64 time)': gives
    a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectJobProviderInterface is created at the first
    use, not by 'Qt3DCore::QAspectJobProviderInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAspectJobProviderInterface.
  - Each name of Qt's Qt3DCore::QAspectJobProviderInterface that has no cute
    function yet, 'jobsToExecute', holds a function that raises
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
  __qt_class__ = 'Qt3DCore::QAspectJobProviderInterface'

  #  A C++ Qt3DCore::QAspectJobProviderInterface Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectJobProviderInterface'

  #  The functions Qt calls itself that Qt3DCore::QAspectJobProviderInterface
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'jobsToExecute': (
          'std::vector<QAspectJobPtr> '
          'Qt3DCore::QAspectJobProviderInterface::jobsToExecute(qint64)',
      ),
  }

  #  The functions Qt calls itself that Qt3DCore::QAspectJobProviderInterface
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'jobsDone': (
          ('_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'frameDone': (
          ('_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

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

  def jobsDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJobProviderInterface::jobsDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobproviderinterface.html#jobsDone
    """
    #  void Qt3DCore::QAspectJobProviderInterface::jobsDone()
    self._callAs(
        'Qt3DCore::QAspectJobProviderInterface',
        'ritual_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv',
    )

  def frameDone(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJobProviderInterface::frameDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobproviderinterface.html
    """
    #  void Qt3DCore::QAspectJobProviderInterface::frameDone()
    self._callAs(
        'Qt3DCore::QAspectJobProviderInterface',
        'ritual_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv',
    )

  @staticmethod
  def jobsToExecute(*__, **_) -> Never:
    """
    Qt's 'std::vector<QAspectJobPtr>
    Qt3DCore::QAspectJobProviderInterface::jobsToExecute(qint64 time)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectJobProviderInterface.jobsToExecute' has no cute "
        "function yet. Qt's 'std::vector<QAspectJobPtr> "
        "Qt3DCore::QAspectJobProviderInterface::jobsToExecute(qint64 "
        "time)': gives a type Python has no way to take yet.")
