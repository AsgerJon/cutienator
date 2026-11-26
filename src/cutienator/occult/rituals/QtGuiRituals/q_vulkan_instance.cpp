//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvulkaninstance.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(vulkan)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if __has_include(<vulkan/vulkan.h>) || defined(Q_QDOC)
#include <QtGui/QtGui>
#include <QtGui/qvulkaninstance.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <QtGui/QVulkanInfoVector>
#include <QtGui/QVulkanLayer>
#include <QtGui/QVulkanExtension>
#include <QtGui/QVulkanInstance>

//  QVulkanInstance::QVulkanInstance()
extern "C" Q_DECL_EXPORT
QVulkanInstance *ritual_ZN15QVulkanInstanceC1Ev() {
  return new QVulkanInstance();
}

//  QVulkanInstance::~QVulkanInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstanceD1Ev(QVulkanInstance *self) {
  delete self;
}

//  QVulkanInfoVector<QVulkanLayer> QVulkanInstance::supportedLayers()
extern "C" Q_DECL_EXPORT
QVulkanInfoVector<QVulkanLayer> *ritual_ZN15QVulkanInstance15supportedLayersEv(
    QVulkanInstance *self) {
  return new QVulkanInfoVector<QVulkanLayer>(self->supportedLayers());
}

//  QVulkanInfoVector<QVulkanLayer> QVulkanInstance::supportedLayers() const
extern "C" Q_DECL_EXPORT
QVulkanInfoVector<QVulkanLayer> *ritual_ZNK15QVulkanInstance15supportedLayersEv(
    const QVulkanInstance *self) {
  return new QVulkanInfoVector<QVulkanLayer>(self->supportedLayers());
}

//  QVulkanInfoVector<QVulkanExtension>
//      QVulkanInstance::supportedExtensions()
extern "C" Q_DECL_EXPORT
QVulkanInfoVector<QVulkanExtension> *ritual_ZN15QVulkanInstance19supportedExtensionsEv(
    QVulkanInstance *self) {
  return new QVulkanInfoVector<QVulkanExtension>(
      self->supportedExtensions());
}

//  QVulkanInfoVector<QVulkanExtension>
//      QVulkanInstance::supportedExtensions() const
extern "C" Q_DECL_EXPORT
QVulkanInfoVector<QVulkanExtension> *ritual_ZNK15QVulkanInstance19supportedExtensionsEv(
    const QVulkanInstance *self) {
  return new QVulkanInfoVector<QVulkanExtension>(
      self->supportedExtensions());
}

//  QVersionNumber QVulkanInstance::supportedApiVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK15QVulkanInstance19supportedApiVersionEv(
    const QVulkanInstance *self) {
  return new QVersionNumber(self->supportedApiVersion());
}

//  void QVulkanInstance::setVkInstance(VkInstance existingVkInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance13setVkInstanceEP12VkInstance_T(
    QVulkanInstance *self,
    VkInstance existingVkInstance) {
  self->setVkInstance(existingVkInstance);
}

//  void QVulkanInstance::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance8setFlagsE6QFlagsINS_4FlagEE(
    QVulkanInstance *self,
    int flags) {
  self->setFlags(QFlags<QVulkanInstance::Flag>::fromInt(flags));
}

//  void QVulkanInstance::setLayers(const QByteArrayList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance9setLayersERK5QListI10QByteArrayE(
    QVulkanInstance *self,
    const QList<QByteArray> *layers) {
  self->setLayers(*layers);
}

//  void QVulkanInstance::setExtensions(const QByteArrayList &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance13setExtensionsERK5QListI10QByteArrayE(
    QVulkanInstance *self,
    const QList<QByteArray> *extensions) {
  self->setExtensions(*extensions);
}

//  void QVulkanInstance::setApiVersion(const QVersionNumber &vulkanVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance13setApiVersionERK14QVersionNumber(
    QVulkanInstance *self,
    const QVersionNumber *vulkanVersion) {
  self->setApiVersion(*vulkanVersion);
}

//  bool QVulkanInstance::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QVulkanInstance6createEv(QVulkanInstance *self) {
  return self->create();
}

//  void QVulkanInstance::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance7destroyEv(QVulkanInstance *self) {
  self->destroy();
}

//  bool QVulkanInstance::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QVulkanInstance7isValidEv(const QVulkanInstance *self) {
  return self->isValid();
}

//  VkResult QVulkanInstance::errorCode() const
extern "C" Q_DECL_EXPORT
VkResult *ritual_ZNK15QVulkanInstance9errorCodeEv(
    const QVulkanInstance *self) {
  return new VkResult(self->errorCode());
}

//  VkInstance QVulkanInstance::vkInstance() const
extern "C" Q_DECL_EXPORT
VkInstance *ritual_ZNK15QVulkanInstance10vkInstanceEv(
    const QVulkanInstance *self) {
  return new VkInstance(self->vkInstance());
}

//  Flags QVulkanInstance::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QVulkanInstance5flagsEv(const QVulkanInstance *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QByteArrayList QVulkanInstance::layers() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK15QVulkanInstance6layersEv(
    const QVulkanInstance *self) {
  return new QList<QByteArray>(self->layers());
}

//  QByteArrayList QVulkanInstance::extensions() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK15QVulkanInstance10extensionsEv(
    const QVulkanInstance *self) {
  return new QList<QByteArray>(self->extensions());
}

//  QVersionNumber QVulkanInstance::apiVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK15QVulkanInstance10apiVersionEv(
    const QVulkanInstance *self) {
  return new QVersionNumber(self->apiVersion());
}

//  PFN_vkVoidFunction QVulkanInstance::getInstanceProcAddr(const char *name)
extern "C" Q_DECL_EXPORT
PFN_vkVoidFunction *ritual_ZN15QVulkanInstance19getInstanceProcAddrEPKc(
    QVulkanInstance *self,
    const char *name) {
  return new PFN_vkVoidFunction(self->getInstanceProcAddr(name));
}

//  QPlatformVulkanInstance *QVulkanInstance::handle() const
extern "C" Q_DECL_EXPORT
QPlatformVulkanInstance *ritual_ZNK15QVulkanInstance6handleEv(
    const QVulkanInstance *self) {
  return self->handle();
}

//  QVulkanFunctions *QVulkanInstance::functions() const
extern "C" Q_DECL_EXPORT
QVulkanFunctions *ritual_ZNK15QVulkanInstance9functionsEv(
    const QVulkanInstance *self) {
  return self->functions();
}

//  QVulkanDeviceFunctions *QVulkanInstance::deviceFunctions(VkDevice device)
extern "C" Q_DECL_EXPORT
QVulkanDeviceFunctions *ritual_ZN15QVulkanInstance15deviceFunctionsEP10VkDevice_T(
    QVulkanInstance *self,
    VkDevice device) {
  return self->deviceFunctions(device);
}

//  void QVulkanInstance::resetDeviceFunctions(VkDevice device)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance20resetDeviceFunctionsEP10VkDevice_T(
    QVulkanInstance *self,
    VkDevice device) {
  self->resetDeviceFunctions(device);
}

//  VkSurfaceKHR QVulkanInstance::surfaceForWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
VkSurfaceKHR *ritual_ZN15QVulkanInstance16surfaceForWindowEP7QWindow(
    QWindow *window) {
  return new VkSurfaceKHR(QVulkanInstance::surfaceForWindow(window));
}

//  bool QVulkanInstance::supportsPresent(VkPhysicalDevice physicalDevice,
//      uint32_t queueFamilyIndex, QWindow *window)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QVulkanInstance15supportsPresentEP18VkPhysicalDevice_TjP7QWindow(
    QVulkanInstance *self,
    VkPhysicalDevice physicalDevice,
    uint32_t queueFamilyIndex,
    QWindow *window) {
  return self->supportsPresent(physicalDevice, queueFamilyIndex, window);
}

//  void QVulkanInstance::presentAboutToBeQueued(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance22presentAboutToBeQueuedEP7QWindow(
    QVulkanInstance *self,
    QWindow *window) {
  self->presentAboutToBeQueued(window);
}

//  void QVulkanInstance::presentQueued(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance13presentQueuedEP7QWindow(
    QVulkanInstance *self,
    QWindow *window) {
  self->presentQueued(window);
}

//  void QVulkanInstance::installDebugOutputFilter(DebugFilter filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance24installDebugOutputFilterEPFbj26VkDebugReportObjectTypeEXTmmiPKcS2_E(
    QVulkanInstance *self,
    void *filter) {
  self->installDebugOutputFilter(
      reinterpret_cast<QVulkanInstance::DebugFilter>(filter));
}

//  void QVulkanInstance::removeDebugOutputFilter(DebugFilter filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance23removeDebugOutputFilterEPFbj26VkDebugReportObjectTypeEXTmmiPKcS2_E(
    QVulkanInstance *self,
    void *filter) {
  self->removeDebugOutputFilter(
      reinterpret_cast<QVulkanInstance::DebugFilter>(filter));
}

//  void QVulkanInstance::installDebugOutputFilter(DebugUtilsFilter filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance24installDebugOutputFilterESt8functionIFb6QFlagsINS_24DebugMessageSeverityFlagEES1_INS_20DebugMessageTypeFlagEEPKvEE(
    QVulkanInstance *self,
    const QVulkanInstance::DebugUtilsFilter *filter) {
  self->installDebugOutputFilter(*filter);
}

//  void QVulkanInstance::clearDebugOutputFilters()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance23clearDebugOutputFiltersEv(
    QVulkanInstance *self) {
  self->clearDebugOutputFilters();
}

//  a QVulkanInfoVector<QVulkanLayer> a ritual of QVulkanInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanInstance__QVulkanInfoVector_QVulkanLayer(
    QVulkanInfoVector<QVulkanLayer> *self) {
  delete self;
}

//  a QVulkanInfoVector<QVulkanExtension> a ritual of QVulkanInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanInstance__QVulkanInfoVector_QVulkanExtension(
    QVulkanInfoVector<QVulkanExtension> *self) {
  delete self;
}

//  a VkResult a ritual of QVulkanInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanInstance__VkResult(VkResult *self) {
  delete self;
}

//  a VkInstance a ritual of QVulkanInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanInstance__VkInstance(VkInstance *self) {
  delete self;
}

//  a PFN_vkVoidFunction a ritual of QVulkanInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanInstance__PFN_vkVoidFunction(
    PFN_vkVoidFunction *self) {
  delete self;
}

//  a VkSurfaceKHR a ritual of QVulkanInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanInstance__VkSurfaceKHR(VkSurfaceKHR *self) {
  delete self;
}

#endif  // __has_include(<vulkan/vulkan.h>) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
