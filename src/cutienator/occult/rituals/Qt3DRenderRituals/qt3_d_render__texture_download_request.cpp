//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qtextureimage.h>
#include <Qt3DRender/qabstracttextureimage.h>
#include <Qt3DRender/private/qtextureimage_p.h>
#include <Qt3DRender/private/qtextureimagedata_p.h>
#include <Qt3DRender/qtexturedata.h>
#include <Qt3DRender/qtexture.h>
#include <Qt3DRender/private/qtexture_p.h>
#include <QtCore/QFileInfo>
#if QT_CONFIG(mimetype)
#include <QtCore/QMimeDatabase>
#include <QtCore/QMimeType>
#endif
#include <QtCore/QBuffer>
#include <QtCore/qendian.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/qaspectengine.h>
#include <Qt3DCore/private/qdownloadhelperservice_p.h>
#include <Qt3DCore/private/qurlhelper_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/texture_p.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/texture/qtexture.cpp, line 1084, as _ZN10Qt3DRender22TextureDownloadRequestC1ERK14QSharedPointerINS_27QTextureFromSourceGeneratorEERK4QUrlPN8Qt3DCore13QAspectEngineENS9_7QNodeIdE
namespace Qt3DRender {
inline TextureDownloadRequest::TextureDownloadRequest(const QTextureFromSourceGeneratorPtr &functor,
                                               const QUrl &source,
                                               Qt3DCore::QAspectEngine *engine,
                                               Qt3DCore::QNodeId texNodeId)
    : Qt3DCore::QDownloadRequest(source)
    , m_functor(functor)
    , m_engine(engine)
    , m_texNodeId(texNodeId)
{

}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 1097, as _ZN10Qt3DRender22TextureDownloadRequest11onCompletedEv
namespace Qt3DRender {
inline void TextureDownloadRequest::onCompleted()
{
    if (cancelled() || !succeeded())
        return;

    QRenderAspectPrivate* d_aspect = QRenderAspectPrivate::findPrivate(m_engine);
    if (!d_aspect)
        return;

    Render::TextureManager *textureManager = d_aspect->m_nodeManagers->textureManager();
    Render::Texture *texture = textureManager->lookupResource(m_texNodeId);
    if (texture == nullptr)
        return;

    QTextureFromSourceGeneratorPtr oldGenerator = qSharedPointerCast<QTextureFromSourceGenerator>(texture->dataGenerator());

    // Set raw data on functor so that it can really load something
    oldGenerator->m_sourceData = m_data;

    // Mark the texture as dirty so that the functor runs again with the downloaded data
    texture->addDirtyFlag(Render::Texture::DirtyDataGenerator);
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  Qt3DRender::TextureDownloadRequest::TextureDownloadRequest(const
//      QTextureFromSourceGeneratorPtr &functor, const QUrl &url,
//      Qt3DCore::QAspectEngine *engine, Qt3DCore::QNodeId texNodeId)
extern "C" Q_DECL_EXPORT
Qt3DRender::TextureDownloadRequest *ritual_ZN10Qt3DRender22TextureDownloadRequestC1ERK14QSharedPointerINS_27QTextureFromSourceGeneratorEERK4QUrlPN8Qt3DCore13QAspectEngineENS9_7QNodeIdE(
    const Qt3DRender::QTextureFromSourceGeneratorPtr *functor,
    const QUrl *url,
    Qt3DCore::QAspectEngine *engine,
    const Qt3DCore::QNodeId *texNodeId) {
  return new Qt3DRender::TextureDownloadRequest(
      *functor,
      *url,
      engine,
      *texNodeId);
}

//  void Qt3DRender::TextureDownloadRequest::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22TextureDownloadRequest11onCompletedEv(
    Qt3DRender::TextureDownloadRequest *self) {
  self->onCompleted();
}

//  Qt3DRender::TextureDownloadRequest::~TextureDownloadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22TextureDownloadRequestD1Ev(
    Qt3DRender::TextureDownloadRequest *self) {
  delete self;
}

//  void Qt3DRender::TextureDownloadRequest::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender22TextureDownloadRequest11onCompletedEv(
    Qt3DRender::TextureDownloadRequest *self) {
  self->Qt3DRender::TextureDownloadRequest::onCompleted();
}
