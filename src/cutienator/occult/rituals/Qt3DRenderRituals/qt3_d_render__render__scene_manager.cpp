//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/scenemanager_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/scenemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qbytearray.h>
#include <vector>

//  Qt3DRender::Render::SceneManager::SceneManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SceneManager *ritual_ZN10Qt3DRender6Render12SceneManagerC1Ev() {
  return new Qt3DRender::Render::SceneManager();
}

//  Qt3DRender::Render::SceneManager::~SceneManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SceneManagerD1Ev(
    Qt3DRender::Render::SceneManager *self) {
  delete self;
}

//  void Qt3DRender::Render::SceneManager::setDownloadService(Qt3DCore::QDown
//      loadHelperService *service)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SceneManager18setDownloadServiceEPN8Qt3DCore22QDownloadHelperServiceE(
    Qt3DRender::Render::SceneManager *self,
    Qt3DCore::QDownloadHelperService *service) {
  self->setDownloadService(service);
}

//  void Qt3DRender::Render::SceneManager::addSceneData(const QUrl &source,
//      Qt3DCore::QNodeId sceneUuid, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SceneManager12addSceneDataERK4QUrlN8Qt3DCore7QNodeIdERK10QByteArray(
    Qt3DRender::Render::SceneManager *self,
    const QUrl *source,
    const Qt3DCore::QNodeId *sceneUuid,
    const QByteArray *data) {
  self->addSceneData(*source, *sceneUuid, *data);
}

//  std::vector<LoadSceneJobPtr>
//      Qt3DRender::Render::SceneManager::takePendingSceneLoaderJobs()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::LoadSceneJobPtr> *ritual_ZN10Qt3DRender6Render12SceneManager26takePendingSceneLoaderJobsEv(
    Qt3DRender::Render::SceneManager *self) {
  return new std::vector<Qt3DRender::Render::LoadSceneJobPtr>(
      self->takePendingSceneLoaderJobs());
}

//  void Qt3DRender::Render::SceneManager::startSceneDownload(const QUrl
//      &source, Qt3DCore::QNodeId sceneUuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SceneManager18startSceneDownloadERK4QUrlN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::SceneManager *self,
    const QUrl *source,
    const Qt3DCore::QNodeId *sceneUuid) {
  self->startSceneDownload(*source, *sceneUuid);
}

//  void Qt3DRender::Render::SceneManager::clearSceneDownload(SceneDownloader
//      *downloader)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SceneManager18clearSceneDownloadEPNS0_15SceneDownloaderE(
    Qt3DRender::Render::SceneManager *self,
    Qt3DRender::Render::SceneDownloader *downloader) {
  self->clearSceneDownload(downloader);
}

//  a std::vector<Qt3DRender::Render::LoadSceneJobPtr> a ritual of
//      Qt3DRender::Render::SceneManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_SceneManager__std_vector_Qt3DRender_Render_LoadSceneJobPtr(
    std::vector<Qt3DRender::Render::LoadSceneJobPtr> *self) {
  delete self;
}
