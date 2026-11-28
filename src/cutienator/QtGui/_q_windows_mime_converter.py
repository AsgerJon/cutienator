"""
QWindowsMimeConverter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qwindowsmimeconverter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWindowsMimeConverter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWindowsMimeConverter: a plain Python object standing
  in front of one C++ QWindowsMimeConverter.

  What exists
  -----------

  Every function of Qt's QWindowsMimeConverter that has a ritual and that
  Python can call so far, 1 name in all: 'registerMimeType'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindowsMimeConverter::~QWindowsMimeConverter()': the destructor:
    Python never removes a C++ QWindowsMimeConverter.
  - Qt's 'bool QWindowsMimeConverter::canConvertFromMime(const FORMATETC
    &formatetc, const QMimeData *mimeData) const': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QWindowsMimeConverter::convertFromMime(const FORMATETC
    &formatetc, const QMimeData *mimeData, STGMEDIUM *pmedium) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QList<FORMATETC> QWindowsMimeConverter::formatsForMime(const
    QString &mimeType, const QMimeData *mimeData) const': gives a type Python
    has no way to take yet.
  - Qt's 'bool QWindowsMimeConverter::canConvertToMime(const QString
    &mimeType, IDataObject *pDataObj) const': names 'IDataObject', which has
    no cute class yet.
  - Qt's 'QVariant QWindowsMimeConverter::convertToMime(const QString
    &mimeType, IDataObject *pDataObj, QMetaType preferredType) const': names
    'IDataObject', which has no cute class yet.
  - Qt's 'QString QWindowsMimeConverter::mimeForFormat(const FORMATETC
    &formatetc) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QWindowsMimeConverter is created at the first use, not by
    'QWindowsMimeConverter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowsMimeConverter.
  - Each name of Qt's QWindowsMimeConverter that has no cute function yet,
    '__init__', 'canConvertFromMime', 'canConvertToMime', 'convertFromMime',
    'convertToMime', 'formatsForMime', 'mimeForFormat', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def registerMimeType(mimeType: str) -> int:
    """
    Calls Qt's 'int QWindowsMimeConverter::registerMimeType(const QString
    &mimeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsmimeconverter.html#registerMimeType

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QWindowsMimeConverter::registerMimeType(const QString &mimeType)
    return Rituals.call(
        'ritual_ZN21QWindowsMimeConverter16registerMimeTypeERK7QString',
        mimeType,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowsMimeConverter'

  #  A C++ QWindowsMimeConverter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowsMimeConverter'

  #  The functions Qt calls itself that QWindowsMimeConverter is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'canConvertFromMime': (
          'bool QWindowsMimeConverter::canConvertFromMime(const FORMATETC '
          '&, const QMimeData *) const',
      ),
      'convertFromMime': (
          'bool QWindowsMimeConverter::convertFromMime(const FORMATETC &, '
          'const QMimeData *, STGMEDIUM *) const',
      ),
      'formatsForMime': (
          'QList<FORMATETC> QWindowsMimeConverter::formatsForMime(const '
          'QString &, const QMimeData *) const',
      ),
      'canConvertToMime': (
          'bool QWindowsMimeConverter::canConvertToMime(const QString &, '
          'IDataObject *) const',
      ),
      'convertToMime': (
          'QVariant QWindowsMimeConverter::convertToMime(const QString &, '
          'IDataObject *, QMetaType) const',
      ),
      'mimeForFormat': (
          'QString QWindowsMimeConverter::mimeForFormat(const FORMATETC &) '
          'const',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWindowsMimeConverter::QWindowsMimeConverter()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.__init__' has no cute function yet. Qt's "
        "'QWindowsMimeConverter::QWindowsMimeConverter()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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
  def canConvertFromMime(*__, **_) -> Never:
    """
    Qt's 'bool QWindowsMimeConverter::canConvertFromMime(const FORMATETC
    &formatetc, const QMimeData *mimeData) const': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.canConvertFromMime' has no cute function "
        "yet. Qt's 'bool QWindowsMimeConverter::canConvertFromMime(const "
        "FORMATETC &formatetc, const QMimeData *mimeData) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def canConvertToMime(*__, **_) -> Never:
    """
    Qt's 'bool QWindowsMimeConverter::canConvertToMime(const QString
    &mimeType, IDataObject *pDataObj) const': names 'IDataObject', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.canConvertToMime' has no cute function yet. "
        "Qt's 'bool QWindowsMimeConverter::canConvertToMime(const QString "
        "&mimeType, IDataObject *pDataObj) const': names 'IDataObject', "
        "which has no cute class yet.")

  @staticmethod
  def convertFromMime(*__, **_) -> Never:
    """
    Qt's 'bool QWindowsMimeConverter::convertFromMime(const FORMATETC
    &formatetc, const QMimeData *mimeData, STGMEDIUM *pmedium) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.convertFromMime' has no cute function yet. "
        "Qt's 'bool QWindowsMimeConverter::convertFromMime(const FORMATETC "
        "&formatetc, const QMimeData *mimeData, STGMEDIUM *pmedium) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def convertToMime(*__, **_) -> Never:
    """
    Qt's 'QVariant QWindowsMimeConverter::convertToMime(const QString
    &mimeType, IDataObject *pDataObj, QMetaType preferredType) const': names
    'IDataObject', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.convertToMime' has no cute function yet. "
        "Qt's 'QVariant QWindowsMimeConverter::convertToMime(const QString "
        "&mimeType, IDataObject *pDataObj, QMetaType preferredType) const': "
        "names 'IDataObject', which has no cute class yet.")

  @staticmethod
  def formatsForMime(*__, **_) -> Never:
    """
    Qt's 'QList<FORMATETC> QWindowsMimeConverter::formatsForMime(const
    QString &mimeType, const QMimeData *mimeData) const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.formatsForMime' has no cute function yet. "
        "Qt's 'QList<FORMATETC> QWindowsMimeConverter::formatsForMime(const "
        "QString &mimeType, const QMimeData *mimeData) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mimeForFormat(*__, **_) -> Never:
    """
    Qt's 'QString QWindowsMimeConverter::mimeForFormat(const FORMATETC
    &formatetc) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWindowsMimeConverter.mimeForFormat' has no cute function yet. "
        "Qt's 'QString QWindowsMimeConverter::mimeForFormat(const FORMATETC "
        "&formatetc) const': takes a type Python has no way to hand over "
        "yet.")
