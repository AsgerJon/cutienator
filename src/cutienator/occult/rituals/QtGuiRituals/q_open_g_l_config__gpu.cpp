//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopengl_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopengl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qversionnumber.h>
#include <QtCore/qbytearray.h>

//  QOpenGLConfig::Gpu::Gpu()
extern "C" Q_DECL_EXPORT
QOpenGLConfig::Gpu *ritual_ZN13QOpenGLConfig3GpuC1Ev() {
  return new QOpenGLConfig::Gpu();
}

//  bool QOpenGLConfig::Gpu::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpenGLConfig3Gpu7isValidEv(
    const QOpenGLConfig::Gpu *self) {
  return self->isValid();
}

//  bool QOpenGLConfig::Gpu::equals(const Gpu &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpenGLConfig3Gpu6equalsERKS0_(
    const QOpenGLConfig::Gpu *self,
    const QOpenGLConfig::Gpu *other) {
  return self->equals(*other);
}

//  Gpu QOpenGLConfig::Gpu::fromDevice(uint vendorId, uint deviceId,
//      QVersionNumber driverVersion, const QByteArray &driverDescription)
extern "C" Q_DECL_EXPORT
QOpenGLConfig::Gpu *ritual_ZN13QOpenGLConfig3Gpu10fromDeviceEjj14QVersionNumberRK10QByteArray(
    uint vendorId,
    uint deviceId,
    const QVersionNumber *driverVersion,
    const QByteArray *driverDescription) {
  return new QOpenGLConfig::Gpu(
      QOpenGLConfig::Gpu::fromDevice(
          vendorId,
          deviceId,
          *driverVersion,
          *driverDescription));
}

//  Gpu QOpenGLConfig::Gpu::fromGLVendor(const QByteArray &glVendor)
extern "C" Q_DECL_EXPORT
QOpenGLConfig::Gpu *ritual_ZN13QOpenGLConfig3Gpu12fromGLVendorERK10QByteArray(
    const QByteArray *glVendor) {
  return new QOpenGLConfig::Gpu(QOpenGLConfig::Gpu::fromGLVendor(*glVendor));
}

//  Gpu QOpenGLConfig::Gpu::fromContext()
extern "C" Q_DECL_EXPORT
QOpenGLConfig::Gpu *ritual_ZN13QOpenGLConfig3Gpu11fromContextEv() {
  return new QOpenGLConfig::Gpu(QOpenGLConfig::Gpu::fromContext());
}

//  QOpenGLConfig::Gpu::~Gpu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLConfig3GpuD1Ev(QOpenGLConfig::Gpu *self) {
  delete self;
}
