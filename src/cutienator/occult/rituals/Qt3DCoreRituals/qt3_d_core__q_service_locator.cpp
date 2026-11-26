//  Written by hand on 2026-11-25 from
//  Qt3DCore/6.12.0/Qt3DCore/private/qservicelocator_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again. Exported, but
//  without a virtual function: no Cute class and no 'take'. Not written:
//  'service' (a template). Also added by hand on 2026-11-25, instances of
//  templates of the class: 3.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/qservicelocator_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractframeadvanceservice_p.h>

//  QServiceLocator::QServiceLocator(QAspectEngine *aspectEngine)
extern "C" Q_DECL_EXPORT
Qt3DCore::QServiceLocator *ritual_ZN8Qt3DCore15QServiceLocatorC1EPNS_13QAspectEngineE(
    Qt3DCore::QAspectEngine *aspectEngine) {
  return new Qt3DCore::QServiceLocator(aspectEngine);
}

//  QServiceLocator::~QServiceLocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QServiceLocatorD1Ev(
    Qt3DCore::QServiceLocator *self) {
  delete self;
}

//  void QServiceLocator::registerServiceProvider(int serviceType,
//      QAbstractServiceProvider *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QServiceLocator23registerServiceProviderEiPNS_24QAbstractServiceProviderE(
    Qt3DCore::QServiceLocator *self,
    int serviceType,
    Qt3DCore::QAbstractServiceProvider *provider) {
  self->registerServiceProvider(serviceType, provider);
}

//  void QServiceLocator::unregisterServiceProvider(int serviceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QServiceLocator25unregisterServiceProviderEi(
    Qt3DCore::QServiceLocator *self,
    int serviceType) {
  self->unregisterServiceProvider(serviceType);
}

//  int QServiceLocator::serviceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore15QServiceLocator12serviceCountEv(
    const Qt3DCore::QServiceLocator *self) {
  return self->serviceCount();
}

//  QSystemInformationService *QServiceLocator::systemInformation()
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationService *ritual_ZN8Qt3DCore15QServiceLocator17systemInformationEv(
    Qt3DCore::QServiceLocator *self) {
  return self->systemInformation();
}

//  QOpenGLInformationService *QServiceLocator::openGLInformation()
extern "C" Q_DECL_EXPORT
Qt3DCore::QOpenGLInformationService *ritual_ZN8Qt3DCore15QServiceLocator17openGLInformationEv(
    Qt3DCore::QServiceLocator *self) {
  return self->openGLInformation();
}

//  QAbstractFrameAdvanceService *QServiceLocator::frameAdvanceService()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrameAdvanceService *ritual_ZN8Qt3DCore15QServiceLocator19frameAdvanceServiceEv(
    Qt3DCore::QServiceLocator *self) {
  return self->frameAdvanceService();
}

//  QEventFilterService *QServiceLocator::eventFilterService()
extern "C" Q_DECL_EXPORT
Qt3DCore::QEventFilterService *ritual_ZN8Qt3DCore15QServiceLocator18eventFilterServiceEv(
    Qt3DCore::QServiceLocator *self) {
  return self->eventFilterService();
}

//  QDownloadHelperService *QServiceLocator::downloadHelperService()
extern "C" Q_DECL_EXPORT
Qt3DCore::QDownloadHelperService *ritual_ZN8Qt3DCore15QServiceLocator21downloadHelperServiceEv(
    Qt3DCore::QServiceLocator *self) {
  return self->downloadHelperService();
}

//  QAbstractServiceProvider *QServiceLocator::_q_getServiceHelper(int type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractServiceProvider *ritual_ZN8Qt3DCore15QServiceLocator19_q_getServiceHelperEi(
    Qt3DCore::QServiceLocator *self,
    int type) {
  return self->_q_getServiceHelper(type);
}

//  QServiceLocatorPrivate *Qt3DCore::QServiceLocator::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QServiceLocatorPrivate *ritual_ZN8Qt3DCore15QServiceLocator6d_funcEv(
    Qt3DCore::QServiceLocator *self) {
  return self->d_func();
}

//  const QServiceLocatorPrivate *Qt3DCore::QServiceLocator::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QServiceLocatorPrivate *ritual_ZNK8Qt3DCore15QServiceLocator6d_funcEv(
    const Qt3DCore::QServiceLocator *self) {
  return self->d_func();
}

//  Qt3DCore::QAbstractServiceProvider
//      *Qt3DCore::QServiceLocator::service<Qt3DCore::QAbstractServiceProvider>(int
//      serviceType)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractServiceProvider * ritual_ZN8Qt3DCore15QServiceLocator7serviceINS_24QAbstractServiceProviderEEEPT_i(
    Qt3DCore::QServiceLocator *self,
    int serviceType) {
  return self->service<Qt3DCore::QAbstractServiceProvider>(serviceType);
}

//  Qt3DCore::QSystemInformationService
//      *Qt3DCore::QServiceLocator::service<Qt3DCore::QSystemInformationService>(int
//      serviceType)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationService * ritual_ZN8Qt3DCore15QServiceLocator7serviceINS_25QSystemInformationServiceEEEPT_i(
    Qt3DCore::QServiceLocator *self,
    int serviceType) {
  return self->service<Qt3DCore::QSystemInformationService>(serviceType);
}

//  Qt3DCore::QAbstractFrameAdvanceService
//      *Qt3DCore::QServiceLocator::service<Qt3DCore::QAbstractFrameAdvanceService>(int
//      serviceType)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrameAdvanceService * ritual_ZN8Qt3DCore15QServiceLocator7serviceINS_28QAbstractFrameAdvanceServiceEEEPT_i(
    Qt3DCore::QServiceLocator *self,
    int serviceType) {
  return self->service<Qt3DCore::QAbstractFrameAdvanceService>(serviceType);
}
