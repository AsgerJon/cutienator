"""
QRhiRenderTargetAttachmentTracker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiRenderTargetAttachmentTracker to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRhiRenderTargetAttachmentTracker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiRenderTargetAttachmentTracker: a plain Python
  object standing in front of one C++ QRhiRenderTargetAttachmentTracker.

  C++ hands a QRhiRenderTargetAttachmentTracker around as a copy, so every
  C++ QRhiRenderTargetAttachmentTracker behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QRhiRenderTargetAttachmentTracker yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QRhiRenderTargetAttachmentTracker::~QRhiRenderTargetAttachmentTracker(
    )': the destructor: Python removes its C++
    QRhiRenderTargetAttachmentTracker by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QRhiRenderTargetAttachmentTracker is created at the first use,
    not by 'QRhiRenderTargetAttachmentTracker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiRenderTargetAttachmentTracker back gives a copy
    the ritual made for Python, in a new cute
    QRhiRenderTargetAttachmentTracker.
  - Each name of Qt's QRhiRenderTargetAttachmentTracker that has no cute
    function yet, 'isUpToDate', 'updateResIdList', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QRhiRenderTargetAttachmentTracker, each a
  #  class in here as in C++.

  class ResId(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiRenderTargetAttachmentTracker::ResId: a plain
    Python object standing in front of one C++
    QRhiRenderTargetAttachmentTracker::ResId.

    C++ hands a QRhiRenderTargetAttachmentTracker::ResId around as a copy, so
    every C++ QRhiRenderTargetAttachmentTracker::ResId behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiRenderTargetAttachmentTracker::ResId yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiRenderTargetAttachmentTracker::ResId::~ResId()': the
      destructor: Python removes its C++
      QRhiRenderTargetAttachmentTracker::ResId by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QRhiRenderTargetAttachmentTracker::ResId is created at the
      first use, not by 'QRhiRenderTargetAttachmentTracker::ResId(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiRenderTargetAttachmentTracker::ResId back gives
      a copy the ritual made for Python, in a new cute
      QRhiRenderTargetAttachmentTracker::ResId.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiRenderTargetAttachmentTracker::ResId'

    #  Qt's '~QRhiRenderTargetAttachmentTracker::ResId()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QRhiRenderTargetAttachmentTracker::ResId behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN33QRhiRenderTargetAttachmentTracker5ResIdD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiRenderTargetAttachmentTracker'

  #  Qt's '~QRhiRenderTargetAttachmentTracker()'. Naming it makes this a
  #  value class: Python owns every C++ QRhiRenderTargetAttachmentTracker
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QRhiRenderTargetAttachmentTrackerD1Ev'

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

  @staticmethod
  def isUpToDate(*__, **_) -> Never:
    """
    Qt's 'QRhiRenderTargetAttachmentTracker::isUpToDate': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QRhiRenderTargetAttachmentTracker.isUpToDate' has no cute "
        "function yet. Qt's "
        "'QRhiRenderTargetAttachmentTracker::isUpToDate': a template: a "
        "pattern and no single function.")

  @staticmethod
  def updateResIdList(*__, **_) -> Never:
    """
    Qt's 'QRhiRenderTargetAttachmentTracker::updateResIdList': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QRhiRenderTargetAttachmentTracker.updateResIdList' has no cute "
        "function yet. Qt's "
        "'QRhiRenderTargetAttachmentTracker::updateResIdList': a template: "
        "a pattern and no single function.")
