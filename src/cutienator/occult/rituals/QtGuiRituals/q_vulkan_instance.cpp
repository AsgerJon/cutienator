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

//  QVersionNumber QVulkanInstance::supportedApiVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK15QVulkanInstance19supportedApiVersionEv(
    const QVulkanInstance *self) {
  return new QVersionNumber(self->supportedApiVersion());
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

//  QPlatformVulkanInstance *QVulkanInstance::handle() const
extern "C" Q_DECL_EXPORT
QPlatformVulkanInstance *ritual_ZNK15QVulkanInstance6handleEv(
    const QVulkanInstance *self) {
  return self->handle();
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

//  void QVulkanInstance::clearDebugOutputFilters()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVulkanInstance23clearDebugOutputFiltersEv(
    QVulkanInstance *self) {
  self->clearDebugOutputFilters();
}

#endif  // __has_include(<vulkan/vulkan.h>) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
