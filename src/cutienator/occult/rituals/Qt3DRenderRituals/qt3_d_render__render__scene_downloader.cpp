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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/scenemanager_p.h>
#include <Qt3DCore/private/vector_helper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/io/scenemanager.cpp, line 71, as _ZN10Qt3DRender6Render15SceneDownloaderC1ERK4QUrlN8Qt3DCore7QNodeIdEPNS0_12SceneManagerE
namespace Qt3DRender::Render {
inline SceneDownloader::SceneDownloader(const QUrl &source, Qt3DCore::QNodeId sceneComponent, SceneManager *manager)
    : Qt3DCore::QDownloadRequest(source)
    , m_sceneComponent(sceneComponent)
    , m_manager(manager)
{

}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/io/scenemanager.cpp, line 79, as _ZN10Qt3DRender6Render15SceneDownloader11onCompletedEv
namespace Qt3DRender::Render {
inline void SceneDownloader::onCompleted()
{
    if (!m_manager)
        return;
    if (succeeded())
        m_manager->addSceneData(url(), m_sceneComponent, m_data);
    else
        qWarning() << "Failed to download scene at" << url();
    m_manager->clearSceneDownload(this);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::SceneDownloader::SceneDownloader(const QUrl &source,
//      Qt3DCore::QNodeId sceneComponent, SceneManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SceneDownloader *ritual_ZN10Qt3DRender6Render15SceneDownloaderC1ERK4QUrlN8Qt3DCore7QNodeIdEPNS0_12SceneManagerE(
    const QUrl *source,
    const Qt3DCore::QNodeId *sceneComponent,
    Qt3DRender::Render::SceneManager *manager) {
  return new Qt3DRender::Render::SceneDownloader(
      *source,
      *sceneComponent,
      manager);
}

//  void Qt3DRender::Render::SceneDownloader::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SceneDownloader11onCompletedEv(
    Qt3DRender::Render::SceneDownloader *self) {
  self->onCompleted();
}

//  Qt3DRender::Render::SceneDownloader::~SceneDownloader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SceneDownloaderD1Ev(
    Qt3DRender::Render::SceneDownloader *self) {
  delete self;
}

//  void Qt3DRender::Render::SceneDownloader::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15SceneDownloader11onCompletedEv(
    Qt3DRender::Render::SceneDownloader *self) {
  self->Qt3DRender::Render::SceneDownloader::onCompleted();
}
