//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickgraphicsdevice.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  what names Vulkan's types stands under '__has_include(<vulkan/vulkan.h>)'
//  as well, as in every other ritual file naming them, since Qt's
//  'qvulkaninstance.h' stands in for those types with others of its own
//  ('quint64' for 'VkImage') when Vulkan's headers are missing, which no
//  function of Qt's library takes. Kept as it is when the generator runs
//  again.
#include <QtGui/qtguiglobal.h>
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

//  QQuickGraphicsDevice &QQuickGraphicsDevice::operator=(const
//      QQuickGraphicsDevice &other)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDeviceaSERKS_(
    QQuickGraphicsDevice *self,
    const QQuickGraphicsDevice *other) {
  return &(self->operator=(*other));
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

#if QT_CONFIG(metal) || defined(Q_QDOC)
//  QQuickGraphicsDevice
//      QQuickGraphicsDevice::fromDeviceAndCommandQueue(MTLDevice *device,
//      MTLCommandQueue *commandQueue)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDevice25fromDeviceAndCommandQueueEP9MTLDeviceP15MTLCommandQueue(
    MTLDevice *device,
    MTLCommandQueue *commandQueue) {
  return new QQuickGraphicsDevice(
      QQuickGraphicsDevice::fromDeviceAndCommandQueue(
          device,
          commandQueue));
}
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
//  QQuickGraphicsDevice
//      QQuickGraphicsDevice::fromPhysicalDevice(VkPhysicalDevice
//      physicalDevice)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDevice18fromPhysicalDeviceEP18VkPhysicalDevice_T(
    VkPhysicalDevice physicalDevice) {
  return new QQuickGraphicsDevice(
      QQuickGraphicsDevice::fromPhysicalDevice(
          physicalDevice));
}
#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)

#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
//  QQuickGraphicsDevice
//      QQuickGraphicsDevice::fromDeviceObjects(VkPhysicalDevice
//      physicalDevice, VkDevice device, int queueFamilyIndex, int
//      queueIndex)
extern "C" Q_DECL_EXPORT
QQuickGraphicsDevice *ritual_ZN20QQuickGraphicsDevice17fromDeviceObjectsEP18VkPhysicalDevice_TP10VkDevice_Tii(
    VkPhysicalDevice physicalDevice,
    VkDevice device,
    int queueFamilyIndex,
    int queueIndex) {
  return new QQuickGraphicsDevice(
      QQuickGraphicsDevice::fromDeviceObjects(
          physicalDevice,
          device,
          queueFamilyIndex,
          queueIndex));
}
#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)

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
