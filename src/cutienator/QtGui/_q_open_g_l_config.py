"""
QOpenGLConfig binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopengl_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QOpenGLConfig to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QVersionNumber


class QOpenGLConfig(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLConfig: a plain Python object standing in
  front of one C++ QOpenGLConfig.

  C++ hands a QOpenGLConfig around as a copy, so every C++ QOpenGLConfig
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QOpenGLConfig yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
    QString &osName, const QVersionNumber &kernelVersion, const QString
    &osVersion, const QJsonDocument &doc)': gives a type Python has no way to
    take yet.
  - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
    QString &osName, const QVersionNumber &kernelVersion, const QString
    &osVersion, const QString &fileName)': gives a type Python has no way to
    take yet.
  - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
    QJsonDocument &doc)': gives a type Python has no way to take yet.
  - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
    QString &fileName)': gives a type Python has no way to take yet.
  - Qt's 'QOpenGLConfig::~QOpenGLConfig()': the destructor: Python removes
    its C++ QOpenGLConfig by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLConfig is created at the first use, not by
    'QOpenGLConfig(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLConfig back gives a copy the ritual made for
    Python, in a new cute QOpenGLConfig.
  - Each name of Qt's QOpenGLConfig that has no cute function yet,
    'gpuFeatures', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QOpenGLConfig, each a class in here as in
  #  C++.

  class Gpu(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLConfig::Gpu: a plain Python object standing
    in front of one C++ QOpenGLConfig::Gpu.

    C++ hands a QOpenGLConfig::Gpu around as a copy, so every C++
    QOpenGLConfig::Gpu behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QOpenGLConfig::Gpu that has a ritual and that
    Python can call so far, 5 names in all: 'isValid', 'equals',
    'fromDevice', 'fromGLVendor', 'fromContext'. It can be made from Python,
    in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLConfig::Gpu::~Gpu()': the destructor: Python removes its
      C++ QOpenGLConfig::Gpu by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QOpenGLConfig::Gpu is created at the first use, not by
      'QOpenGLConfig::Gpu(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLConfig::Gpu back gives a copy the ritual
      made for Python, in a new cute QOpenGLConfig::Gpu.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']
      QVersionNumber = WAIT['QVersionNumber']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(int, int, QVersionNumber, QByteArray)
    def fromDevice(
        vendorId: int,
        deviceId: int,
        driverVersion: QVersionNumber,
        driverDescription: QByteArray,
    ) -> QOpenGLConfig.Gpu:
      """
      Calls Qt's 'Gpu QOpenGLConfig::Gpu::fromDevice(uint vendorId, uint
      deviceId, QVersionNumber driverVersion, const QByteArray
      &driverDescription)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglconfig-gpu.html#fromDevice

      Parameters
      ----------

      vendorId : int
        Passed on as it is.

      deviceId : int
        Passed on as it is.

      driverVersion : QVersionNumber
        Passed on as a value: Qt reads the C++ QVersionNumber, which stays
        Python's own.

      driverDescription : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      Returns
      -------

      QOpenGLConfig.Gpu
        A new cute QOpenGLConfig::Gpu around the copy Qt gave back. Python
        owns it.
      """
      #  Gpu QOpenGLConfig::Gpu::fromDevice(uint vendorId, uint deviceId,
      #      QVersionNumber driverVersion, const QByteArray
      #      &driverDescription)
      address = Rituals.call(
          'ritual_ZN13QOpenGLConfig3Gpu10fromDeviceEjj14QVersionNumberRK10Q'
          'ByteArray',
          vendorId, deviceId, CuteMixin._valueOf(driverVersion),
          CuteMixin._valueOf(driverDescription),
      )
      return QOpenGLConfig.Gpu._cuteOwning(address)

    @staticmethod
    @overload(QByteArray)
    def fromGLVendor(glVendor: QByteArray) -> QOpenGLConfig.Gpu:
      """
      Calls Qt's 'Gpu QOpenGLConfig::Gpu::fromGLVendor(const QByteArray
      &glVendor)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglconfig-gpu.html#fromGLVendor

      Parameters
      ----------

      glVendor : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      Returns
      -------

      QOpenGLConfig.Gpu
        A new cute QOpenGLConfig::Gpu around the copy Qt gave back. Python
        owns it.
      """
      #  Gpu QOpenGLConfig::Gpu::fromGLVendor(const QByteArray &glVendor)
      address = Rituals.call(
          'ritual_ZN13QOpenGLConfig3Gpu12fromGLVendorERK10QByteArray',
          CuteMixin._valueOf(glVendor),
      )
      return QOpenGLConfig.Gpu._cuteOwning(address)

    @staticmethod
    def fromContext() -> QOpenGLConfig.Gpu:
      """
      Calls Qt's 'Gpu QOpenGLConfig::Gpu::fromContext()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglconfig-gpu.html#fromContext

      Returns
      -------

      QOpenGLConfig.Gpu
        A new cute QOpenGLConfig::Gpu around the copy Qt gave back. Python
        owns it.
      """
      #  Gpu QOpenGLConfig::Gpu::fromContext()
      address = Rituals.call('ritual_ZN13QOpenGLConfig3Gpu11fromContextEv')
      return QOpenGLConfig.Gpu._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLConfig::Gpu'

    #  Qt's '~QOpenGLConfig::Gpu()'. Naming it makes this a value class:
    #  Python owns every C++ QOpenGLConfig::Gpu behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QOpenGLConfig3GpuD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QOpenGLConfig::Gpu::isValid() const'.

      Qt's own words: https://doc.qt.io/qt-6/qopenglconfig-gpu.html#isValid
      """
      #  bool QOpenGLConfig::Gpu::isValid() const
      return self.uglySide.call('ritual_ZNK13QOpenGLConfig3Gpu7isValidEv')

    @overload(THIS)
    def equals(self, other: QOpenGLConfig.Gpu) -> bool:
      """
      Calls Qt's 'bool QOpenGLConfig::Gpu::equals(const Gpu &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qopenglconfig-gpu.html#equals

      Parameters
      ----------

      other : QOpenGLConfig.Gpu
        Passed on as a value: Qt reads the C++ QOpenGLConfig::Gpu, which
        stays Python's own.
      """
      #  bool QOpenGLConfig::Gpu::equals(const Gpu &other) const
      return self.uglySide.call(
          'ritual_ZNK13QOpenGLConfig3Gpu6equalsERKS0_', self._valueOf(other),
      )

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QOpenGLConfig::Gpu::Gpu()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qopenglconfig-gpu.html#Gpu
      """
      #  QOpenGLConfig::Gpu::Gpu()
      self._noteCreation(QOpenGLConfig.Gpu, lambda: Rituals.call(
          'ritual_ZN13QOpenGLConfig3GpuC1Ev',
      ))

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
  __qt_class__ = 'QOpenGLConfig'

  #  Qt's '~QOpenGLConfig()'. Naming it makes this a value class: Python owns
  #  every C++ QOpenGLConfig behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QOpenGLConfigD1Ev'

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
  def gpuFeatures(*__, **_) -> Never:
    """
    - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
      QString &osName, const QVersionNumber &kernelVersion, const QString
      &osVersion, const QJsonDocument &doc)': gives a type Python has no way
      to take yet.
    - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
      QString &osName, const QVersionNumber &kernelVersion, const QString
      &osVersion, const QString &fileName)': gives a type Python has no way
      to take yet.
    - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
      QJsonDocument &doc)': gives a type Python has no way to take yet.
    - Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
      QString &fileName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLConfig.gpuFeatures' has no cute function yet. Qt's "
        "'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const "
        "QString &osName, const QVersionNumber &kernelVersion, const "
        "QString &osVersion, const QJsonDocument &doc)': gives a type "
        "Python has no way to take yet. Qt's 'QSet<QString> "
        "QOpenGLConfig::gpuFeatures(const Gpu &gpu, const QString &osName, "
        "const QVersionNumber &kernelVersion, const QString &osVersion, "
        "const QString &fileName)': gives a type Python has no way to take "
        "yet. Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu "
        "&gpu, const QJsonDocument &doc)': gives a type Python has no way "
        "to take yet. Qt's 'QSet<QString> QOpenGLConfig::gpuFeatures(const "
        "Gpu &gpu, const QString &fileName)': gives a type Python has no "
        "way to take yet.")
