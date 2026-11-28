"""
QWidgetPlatformDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformdialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWidgetPlatformDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QWindow
  from ..QtWidgets import QDialog
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDialog = WAIT['QDialog']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetPlatformDialog(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWidgetPlatformDialog: a plain Python object standing
  in front of one C++ QWidgetPlatformDialog.

  C++ hands a QWidgetPlatformDialog around as a copy, so every C++
  QWidgetPlatformDialog behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWidgetPlatformDialog that has a ritual and that
  Python can call so far, 1 name in all: 'show'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetPlatformDialog::~QWidgetPlatformDialog()': the destructor:
    Python removes its C++ QWidgetPlatformDialog by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QWidgetPlatformDialog is created at the first use, not by
    'QWidgetPlatformDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWidgetPlatformDialog back gives a copy the ritual
    made for Python, in a new cute QWidgetPlatformDialog.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDialog, Qt.WindowFlags, Qt.WindowModality, QWindow)
  @overload(QDialog, Qt.WindowFlags, Qt.WindowModality, NoneType)
  @overload(NoneType, Qt.WindowFlags, Qt.WindowModality, QWindow)
  @overload(NoneType, Qt.WindowFlags, Qt.WindowModality, NoneType)
  def show(
      dialog: Optional[QDialog],
      flags: Qt.WindowFlags,
      modality: Qt.WindowModality,
      parent: Optional[QWindow],
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetPlatformDialog::show(QDialog *dialog,
    Qt::WindowFlags flags, Qt::WindowModality modality, QWindow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetplatformdialog.html#show

    Parameters
    ----------

    dialog : Optional[QDialog]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.WindowFlags
      Passed on as its number.

    modality : Qt.WindowModality
      Passed on as its number.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetPlatformDialog::show(QDialog *dialog, Qt::WindowFlags
    #      flags, Qt::WindowModality modality, QWindow *parent)
    return Rituals.call(
        'ritual_ZN21QWidgetPlatformDialog4showEP7QDialog6QFlagsIN2Qt10Windo'
        'wTypeEENS3_14WindowModalityEP7QWindow',
        CuteMixin._addressOf(dialog), flags.value, modality.value,
        CuteMixin._addressOf(parent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetPlatformDialog'

  #  Qt's '~QWidgetPlatformDialog()'. Naming it makes this a value class:
  #  Python owns every C++ QWidgetPlatformDialog behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QWidgetPlatformDialogD1Ev'

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
