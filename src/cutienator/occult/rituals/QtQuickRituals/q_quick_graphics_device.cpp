//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickgraphicsdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickgraphicsdevice.h>

//  QQuickGraphicsDevice::QQuickGraphicsDevice()
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDeviceC1Ev() {
  return new QQuickGraphicsDevice();
}

//  QQuickGraphicsDevice::~QQuickGraphicsDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphicsDeviceD1Ev(QQuickGraphicsDevice *self) {
  delete self;
}

//  QQuickGraphicsDevice::QQuickGraphicsDevice(const QQuickGraphicsDevice
//      &other)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDeviceC1ERKS_(
    const QQuickGraphicsDevice *other) {
  return new QQuickGraphicsDevice(*other);
}

//  bool QQuickGraphicsDevice::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGraphicsDevice6isNullEv(
    const QQuickGraphicsDevice *self) {
  return self->isNull();
}

#if QT_CONFIG(opengl) || defined(Q_QDOC)
//  QQuickGraphicsDevice
//      QQuickGraphicsDevice::fromOpenGLContext(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDevice17fromOpenGLContextEP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QQuickGraphicsDevice(
      QQuickGraphicsDevice::fromOpenGLContext(
          context));
}
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)

//  QQuickGraphicsDevice QQuickGraphicsDevice::fromRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDevice7fromRhiEP4QRhi(
    QRhi *rhi) {
  return new QQuickGraphicsDevice(QQuickGraphicsDevice::fromRhi(rhi));
}

//  QQuickGraphicsDevice QQuickGraphicsDevice::fromRhiAdapter(QRhiAdapter
//      *adapter)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDevice14fromRhiAdapterEP11QRhiAdapter(
    QRhiAdapter *adapter) {
  return new QQuickGraphicsDevice(
      QQuickGraphicsDevice::fromRhiAdapter(
          adapter));
}

//  void QQuickGraphicsDevice::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGraphicsDevice6detachEv(QQuickGraphicsDevice *self) {
  self->detach();
}
