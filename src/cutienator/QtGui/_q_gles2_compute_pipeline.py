"""
QGles2ComputePipeline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2ComputePipeline to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRhiComputePipeline

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGles2ComputePipeline(QRhiComputePipeline):
  """
  The cute side of Qt's QGles2ComputePipeline: a plain Python object standing
  in front of one C++ QGles2ComputePipeline.

  It is built on the cute 'QRhiComputePipeline', as Qt's
  QGles2ComputePipeline is built on Qt's QRhiComputePipeline, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2ComputePipeline that has a ritual and that
  Python can call so far, 2 names in all: 'destroy', 'create'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2ComputePipeline::~QGles2ComputePipeline()': the destructor:
    Python never removes a C++ QGles2ComputePipeline.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'QRhiGles2.

  What to expect
  --------------

  - The C++ QGles2ComputePipeline is created at the first use, not by
    'QGles2ComputePipeline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2ComputePipeline.
  - Each name of Qt's QGles2ComputePipeline that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2ComputePipeline'

  #  A C++ QGles2ComputePipeline Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2ComputePipeline'

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
    Qt's 'QGles2ComputePipeline::QGles2ComputePipeline(QRhiImplementation
    *rhi)': leans on 'QRhiGles2::trySaveToDiskCache(unsigned int, QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGles2ComputePipeline.__init__' has no cute function yet. Qt's "
        "'QGles2ComputePipeline::QGles2ComputePipeline(QRhiImplementation "
        "*rhi)': leans on 'QRhiGles2::trySaveToDiskCache(unsigned int, "
        "QByteArray const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QGles2ComputePipeline::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2computepipeline.html#destroy
    """
    #  void QGles2ComputePipeline::destroy()
    ritual = 'ritual_ZN21QGles2ComputePipeline7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QGles2ComputePipeline7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QGles2ComputePipeline::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2computepipeline.html#create
    """
    #  bool QGles2ComputePipeline::create()
    return self.uglySide.call('ritual_ZN21QGles2ComputePipeline6createEv')
