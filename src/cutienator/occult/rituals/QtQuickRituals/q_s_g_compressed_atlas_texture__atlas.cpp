//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcompressedatlastexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcompressedatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgcompressedatlastexture_p.h>
#include <QtCore/QVarLengthArray>
#include <QtCore/QElapsedTimer>
#include <QtCore/QtMath>
#include <QtGui/QGuiApplication>
#include <QtGui/QScreen>
#include <QtGui/QSurface>
#include <QtGui/QWindow>
#include <QtCore/QDebug>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgcompressedtexture_p.h>
#include <QtQuick/private/qsgrhiatlastexture_p.h>
#include <QtCore/QVarLengthArray>
#include <QtCore/QElapsedTimer>
#include <QtCore/QtMath>
#include <QtGui/QWindow>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgcompressedtexture_p.h>
#include <QtQuick/private/qsgcompressedatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 89, as _ZN25QSGCompressedAtlasTexture7TextureC1EPNS_5AtlasERK5QRect14QByteArrayViewRK5QSize
namespace QSGCompressedAtlasTexture {
inline Texture::Texture(Atlas *atlas, const QRect &textureRect, QByteArrayView data, const QSize &size)
    : QSGRhiAtlasTexture::TextureBase(atlas, textureRect),
      m_nonatlas_texture(nullptr),
      m_data(data.toByteArray()),
      m_size(size)
{
    float w = atlas->size().width();
    float h = atlas->size().height();
    const QRect &r = atlasSubRect();
    // offset by half-pixel to prevent bleeding when scaling
    m_texture_coords_rect = QRectF((r.x() + .5) / w,
                                   (r.y() + .5) / h,
                                   (size.width() - 1.) / w,
                                   (size.height() - 1.) / h);
}
}  // namespace QSGCompressedAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 50, as _ZN25QSGCompressedAtlasTexture5Atlas15generateTextureEv
namespace QSGCompressedAtlasTexture {
inline bool Atlas::generateTexture()
{
    QSGCompressedTexture::FormatInfo fmt = QSGCompressedTexture::formatInfo(m_format);
    QRhiTexture::Flags flags(QRhiTexture::UsedAsTransferSource | QRhiTexture::UsedAsCompressedAtlas);
    flags.setFlag(QRhiTexture::sRGB, fmt.isSRGB);
    m_texture = m_rhi->newTexture(fmt.rhiFormat, m_size, 1, flags);
    if (!m_texture)
        return false;

    if (!m_texture->create()) {
        delete m_texture;
        m_texture = nullptr;
        return false;
    }

    qCDebug(QSG_LOG_TEXTUREIO, "Created compressed atlas of size %dx%d for format 0x%x (rhi: %d)",
            m_size.width(), m_size.height(), m_format, fmt.rhiFormat);

    return true;
}
}  // namespace QSGCompressedAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 71, as _ZN25QSGCompressedAtlasTexture5Atlas20enqueueTextureUploadEPN18QSGRhiAtlasTexture11TextureBaseEP23QRhiResourceUpdateBatch
namespace QSGCompressedAtlasTexture {
inline void Atlas::enqueueTextureUpload(QSGRhiAtlasTexture::TextureBase *t, QRhiResourceUpdateBatch *rcub)
{
    Texture *texture = static_cast<Texture *>(t);

    const QRect &r = texture->atlasSubRect();

    QRhiTextureSubresourceUploadDescription subresDesc(texture->data().constData(),
                                                       texture->sizeInBytes());
    subresDesc.setSourceSize(texture->textureSize());
    subresDesc.setDestinationTopLeft(r.topLeft());

    QRhiTextureUploadDescription desc(QRhiTextureUploadEntry(0, 0, subresDesc));
    rcub->uploadTexture(m_texture, desc);

    qCDebug(QSG_LOG_TEXTUREIO, "compressed atlastexture upload, size %dx%d format 0x%x",
            t->textureSize().width(), t->textureSize().height(), m_format);
}
}  // namespace QSGCompressedAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 324, as _ZN18QSGRhiAtlasTexture11TextureBaseC2EPNS_9AtlasBaseERK5QRect
namespace QSGRhiAtlasTexture {
inline TextureBase::TextureBase(AtlasBase *atlas, const QRect &textureRect)
    : QSGTexture(*(new QSGTexturePrivate(this)))
    , m_allocated_rect(textureRect)
    , m_atlas(atlas)
{
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 331, as _ZN18QSGRhiAtlasTexture11TextureBaseD2Ev
namespace QSGRhiAtlasTexture {
inline TextureBase::~TextureBase()
{
    m_atlas->remove(this);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 32, as _ZN25QSGCompressedAtlasTexture5AtlasD1Ev
namespace QSGCompressedAtlasTexture {
inline Atlas::~Atlas()
{
}
}  // namespace QSGCompressedAtlasTexture
//  -----------------------------------------------------------------------

//  A QSGCompressedAtlasTexture::Atlas that Python can take functions over in. Every QSGCompressedAtlasTexture::Atlas
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGCompressedAtlasTexture_AtlasCall0)(const void *, int *);
typedef void (*CuteQSGCompressedAtlasTexture_AtlasCall1)(const void *, QSGRhiAtlasTexture::TextureBase *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedAtlasTexture_AtlasCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedAtlasTexture_AtlasCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_AtlasCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_AtlasCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_AtlasCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_AtlasCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_AtlasCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGCompressedAtlasTexture_Atlas : public QSGCompressedAtlasTexture::Atlas {
public:
  using QSGCompressedAtlasTexture::Atlas::Atlas;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QSGRhiAtlasTexture9AtlasBase15generateTextureEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QSGRhiAtlasTexture9AtlasBase20enqueueTextureUploadEPNS_11TextureBaseEP23QRhiResourceUpdateBatch")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSGCompressedAtlasTexture::Atlas::generateTexture()
  bool generateTexture() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall0 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedAtlasTexture::Atlas::generateTexture();
  }

  //  void QSGCompressedAtlasTexture::Atlas::enqueueTextureUpload(QSGRhiAtl
  //      asTexture::TextureBase *t, QRhiResourceUpdateBatch *rcub)
  void enqueueTextureUpload(
      QSGRhiAtlasTexture::TextureBase *t,
      QRhiResourceUpdateBatch *rcub) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall1 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall1>(taken[1]);
      call(this, t, rcub, &handled);
      if (handled) return;
    }
    QSGCompressedAtlasTexture::Atlas::enqueueTextureUpload(t, rcub);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall2 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall3 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall4 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall5 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall6 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall7 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_AtlasCall8 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_AtlasCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGCompressedAtlasTexture::Atlas::~Atlas()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGCompressedAtlasTexture5AtlasD1Ev(
    QSGCompressedAtlasTexture::Atlas *self) {
  delete self;
}

//  bool QSGCompressedAtlasTexture::Atlas::generateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSGCompressedAtlasTexture5Atlas15generateTextureEv(
    QSGCompressedAtlasTexture::Atlas *self) {
  return self->generateTexture();
}

//  void QSGCompressedAtlasTexture::Atlas::enqueueTextureUpload(QSGRhiAtlasTe
//      xture::TextureBase *t, QRhiResourceUpdateBatch *rcub)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGCompressedAtlasTexture5Atlas20enqueueTextureUploadEPN18QSGRhiAtlasTexture11TextureBaseEP23QRhiResourceUpdateBatch(
    QSGCompressedAtlasTexture::Atlas *self,
    QSGRhiAtlasTexture::TextureBase *t,
    QRhiResourceUpdateBatch *rcub) {
  self->enqueueTextureUpload(t, rcub);
}

//  uint QSGCompressedAtlasTexture::Atlas::format() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK25QSGCompressedAtlasTexture5Atlas6formatEv(
    const QSGCompressedAtlasTexture::Atlas *self) {
  return self->format();
}

//  a Python function taken by a CuteQSGCompressedAtlasTexture_Atlas, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCompressedAtlasTexture_Atlas(
    QSGCompressedAtlasTexture::Atlas *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCompressedAtlasTexture_Atlas *>(self)->take(key, call);
}
