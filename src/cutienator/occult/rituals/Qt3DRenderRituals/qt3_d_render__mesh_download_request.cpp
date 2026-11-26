//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qurl.h>
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

//  from ../qt3d/src/render/geometry/qmesh.cpp, line 374, as _ZN10Qt3DRender19MeshDownloadRequestC1EN8Qt3DCore7QNodeIdE4QUrlPNS_6Render12NodeManagersE
namespace Qt3DRender {
using namespace Qt3DCore;
inline MeshDownloadRequest::MeshDownloadRequest(Qt3DCore::QNodeId mesh, QUrl source, Render::NodeManagers *managers)
    : Qt3DCore::QDownloadRequest(source)
    , m_mesh(mesh)
    , m_nodeManagers(managers)
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/geometry/qmesh.cpp, line 383, as _ZN10Qt3DRender19MeshDownloadRequest11onCompletedEv
namespace Qt3DRender {
using namespace Qt3DCore;
inline void MeshDownloadRequest::onCompleted()
{
    if (cancelled() || !succeeded())
        return;

    if (!m_nodeManagers)
        return;

    Render::GeometryRenderer *renderer = m_nodeManagers->geometryRendererManager()->lookupResource(m_mesh);
    if (!renderer)
        return;

    QGeometryFactoryPtr geometryFactory = renderer->geometryFactory();
    if (!geometryFactory.isNull() && geometryFactory->id() == Qt3DCore::functorTypeId<MeshLoaderFunctor>()) {
        QSharedPointer<MeshLoaderFunctor> functor = qSharedPointerCast<MeshLoaderFunctor>(geometryFactory);

        // We make sure we are setting the result for the right request
        // (the functor for the mesh could have changed in the meantime)
        if (m_url == functor->sourcePath()) {
            functor->setSourceData(m_data);

            // mark the component as dirty so that the functor runs again in the correct job
            m_nodeManagers->geometryRendererManager()->addDirtyGeometryRenderer(m_mesh);
        }
    }
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  Qt3DRender::MeshDownloadRequest::MeshDownloadRequest(Qt3DCore::QNodeId
//      mesh, QUrl source, Render::NodeManagers *managers)
extern "C" Q_DECL_EXPORT
Qt3DRender::MeshDownloadRequest *ritual_ZN10Qt3DRender19MeshDownloadRequestC1EN8Qt3DCore7QNodeIdE4QUrlPNS_6Render12NodeManagersE(
    const Qt3DCore::QNodeId *mesh,
    const QUrl *source,
    Qt3DRender::Render::NodeManagers *managers) {
  return new Qt3DRender::MeshDownloadRequest(*mesh, *source, managers);
}

//  void Qt3DRender::MeshDownloadRequest::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19MeshDownloadRequest11onCompletedEv(
    Qt3DRender::MeshDownloadRequest *self) {
  self->onCompleted();
}

//  Qt3DRender::MeshDownloadRequest::~MeshDownloadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19MeshDownloadRequestD1Ev(
    Qt3DRender::MeshDownloadRequest *self) {
  delete self;
}

//  void Qt3DRender::MeshDownloadRequest::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender19MeshDownloadRequest11onCompletedEv(
    Qt3DRender::MeshDownloadRequest *self) {
  self->Qt3DRender::MeshDownloadRequest::onCompleted();
}
