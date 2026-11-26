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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qmesh.h>
#include <Qt3DRender/private/qmesh_p.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtCore/QDebug>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#include <QtCore/QScopedPointer>
#if QT_CONFIG(mimetype)
#include <QtCore/QMimeDatabase>
#include <QtCore/QMimeType>
#endif
#include <QtCore/QBuffer>
#include <Qt3DRender/QRenderAspect>
#include <Qt3DCore/QAspectEngine>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/private/qdownloadhelperservice_p.h>
#include <Qt3DCore/private/qurlhelper_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/qgeometryloaderinterface_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DRender/private/qgeometryloaderfactory_p.h>
#include <Qt3DRender/private/geometryrenderermanager_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/qmesh.cpp, line 359, as _ZNK10Qt3DRender17MeshLoaderFunctor6equalsERKN8Qt3DCore16QGeometryFactoryE
namespace Qt3DRender {
using namespace Qt3DCore;
inline bool MeshLoaderFunctor::equals(const QGeometryFactory &other) const
{
    const MeshLoaderFunctor *otherFunctor = functor_cast<MeshLoaderFunctor>(&other);
    if (otherFunctor != nullptr)
        return (otherFunctor->m_sourcePath == m_sourcePath &&
                otherFunctor->m_sourceData.isEmpty() == m_sourceData.isEmpty() &&
                otherFunctor->m_meshName == m_meshName &&
                otherFunctor->m_downloaderService == m_downloaderService &&
                otherFunctor->m_nodeManagers == m_nodeManagers);
    return false;
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

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

//  Qt3DCore::QGeometry *Qt3DRender::MeshLoaderFunctor::operator()()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZN10Qt3DRender17MeshLoaderFunctorclEv(
    Qt3DRender::MeshLoaderFunctor *self) {
  return self->operator()();
}

//  bool Qt3DRender::MeshLoaderFunctor::equals(const
//      Qt3DCore::QGeometryFactory &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender17MeshLoaderFunctor6equalsERKN8Qt3DCore16QGeometryFactoryE(
    const Qt3DRender::MeshLoaderFunctor *self,
    const Qt3DCore::QGeometryFactory *other) {
  return self->equals(*other);
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
