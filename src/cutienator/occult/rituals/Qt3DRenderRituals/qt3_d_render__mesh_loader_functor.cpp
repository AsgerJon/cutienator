//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qstring.h>

//  void Qt3DRender::MeshLoaderFunctor::setNodeManagers(Render::NodeManagers
//      *managers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17MeshLoaderFunctor15setNodeManagersEPNS_6Render12NodeManagersE(
    Qt3DRender::MeshLoaderFunctor *self,
    Qt3DRender::Render::NodeManagers *managers) {
  self->setNodeManagers(managers);
}

//  Render::NodeManagers *Qt3DRender::MeshLoaderFunctor::nodeManagers() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender17MeshLoaderFunctor12nodeManagersEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return self->nodeManagers();
}

//  void Qt3DRender::MeshLoaderFunctor::setDownloaderService(Qt3DCore::QDownl
//      oadHelperService *service)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17MeshLoaderFunctor20setDownloaderServiceEPN8Qt3DCore22QDownloadHelperServiceE(
    Qt3DRender::MeshLoaderFunctor *self,
    Qt3DCore::QDownloadHelperService *service) {
  self->setDownloaderService(service);
}

//  Qt3DCore::QDownloadHelperService
//      *Qt3DRender::MeshLoaderFunctor::downloaderService() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QDownloadHelperService *ritual_ZNK10Qt3DRender17MeshLoaderFunctor17downloaderServiceEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return self->downloaderService();
}

//  void Qt3DRender::MeshLoaderFunctor::setSourceData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17MeshLoaderFunctor13setSourceDataERK10QByteArray(
    Qt3DRender::MeshLoaderFunctor *self,
    const QByteArray *data) {
  self->setSourceData(*data);
}

//  QByteArray Qt3DRender::MeshLoaderFunctor::sourceData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender17MeshLoaderFunctor10sourceDataEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return new QByteArray(self->sourceData());
}

//  QUrl Qt3DRender::MeshLoaderFunctor::sourcePath() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender17MeshLoaderFunctor10sourcePathEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return new QUrl(self->sourcePath());
}

//  Qt3DCore::QNodeId Qt3DRender::MeshLoaderFunctor::mesh() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender17MeshLoaderFunctor4meshEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return new Qt3DCore::QNodeId(self->mesh());
}

//  QString Qt3DRender::MeshLoaderFunctor::meshName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender17MeshLoaderFunctor8meshNameEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return new QString(self->meshName());
}

//  QMesh::Status Qt3DRender::MeshLoaderFunctor::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QMesh::Status ritual_ZNK10Qt3DRender17MeshLoaderFunctor6statusEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return self->status();
}

//  qintptr Qt3DRender::MeshLoaderFunctor::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DRender17MeshLoaderFunctor2idEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return self->id();
}

//  qintptr Qt3DRender::MeshLoaderFunctor::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DRender17MeshLoaderFunctor2idEv(
    const Qt3DRender::MeshLoaderFunctor *self) {
  return self->Qt3DRender::MeshLoaderFunctor::id();
}
