//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 363, as _ZN18QSGRhiAtlasTexture7TextureC1EPNS_5AtlasERK5QRectRK6QImage
namespace QSGRhiAtlasTexture {
inline Texture::Texture(Atlas *atlas, const QRect &textureRect, const QImage &image)
    : TextureBase(atlas, textureRect)
    , m_image(image)
    , m_has_alpha(image.hasAlphaChannel())
{
    float w = atlas->size().width();
    float h = atlas->size().height();
    QRect nopad = atlasSubRectWithoutPadding();
    m_texture_coords_rect = QRectF(nopad.x() / w,
                                   nopad.y() / h,
                                   nopad.width() / w,
                                   nopad.height() / h);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 201, as _ZN18QSGRhiAtlasTexture5Atlas15generateTextureEv
namespace QSGRhiAtlasTexture {
inline bool Atlas::generateTexture()
{
    m_texture = m_rhi->newTexture(m_format, m_size, 1, QRhiTexture::UsedAsTransferSource);
    if (!m_texture)
        return false;

    if (!m_texture->create()) {
        delete m_texture;
        m_texture = nullptr;
        return false;
    }

    return true;
}
}  // namespace QSGRhiAtlasTexture

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

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 153, as _ZN18QSGRhiAtlasTexture9AtlasBase6removeEPNS_11TextureBaseE
namespace QSGRhiAtlasTexture {
inline void AtlasBase::remove(TextureBase *t)
{
    QRect atlasRect = t->atlasSubRect();
    m_allocator.deallocate(atlasRect);
    m_pending_uploads.removeOne(t);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 185, as _ZN18QSGRhiAtlasTexture5AtlasD1Ev
namespace QSGRhiAtlasTexture {
inline Atlas::~Atlas()
{
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 189, as _ZN18QSGRhiAtlasTexture5Atlas6createERK6QImage
namespace QSGRhiAtlasTexture {
inline Texture *Atlas::create(const QImage &image)
{
    // No need to lock, as manager already locked it.
    QRect rect = m_allocator.allocate(QSize(image.width() + 2, image.height() + 2));
    if (rect.width() > 0 && rect.height() > 0) {
        Texture *t = new Texture(this, rect, image);
        m_pending_uploads << t;
        return t;
    }
    return nullptr;
}
}  // namespace QSGRhiAtlasTexture
//  -----------------------------------------------------------------------

//  A QSGRhiAtlasTexture::Atlas that Python can take functions over in. Every QSGRhiAtlasTexture::Atlas
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRhiAtlasTexture_AtlasCall0)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall1)(const void *, QSGRhiAtlasTexture::TextureBase *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_AtlasCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_AtlasCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_Atlas : public QSGRhiAtlasTexture::Atlas {
public:
  using QSGRhiAtlasTexture::Atlas::Atlas;
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

  //  bool QSGRhiAtlasTexture::Atlas::generateTexture()
  bool generateTexture() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::Atlas::generateTexture();
  }

  //  void QSGRhiAtlasTexture::Atlas::enqueueTextureUpload(TextureBase *t,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void enqueueTextureUpload(
      QSGRhiAtlasTexture::TextureBase *t,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall1>(taken[1]);
      call(this, t, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::Atlas::enqueueTextureUpload(t, resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall2>(taken[2]);
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
      CuteQSGRhiAtlasTexture_AtlasCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall3>(taken[3]);
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
      CuteQSGRhiAtlasTexture_AtlasCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall4>(taken[4]);
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
      CuteQSGRhiAtlasTexture_AtlasCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall5>(taken[5]);
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
      CuteQSGRhiAtlasTexture_AtlasCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall6>(taken[6]);
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
      CuteQSGRhiAtlasTexture_AtlasCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall7>(taken[7]);
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
      CuteQSGRhiAtlasTexture_AtlasCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGRhiAtlasTexture::Atlas::~Atlas()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture5AtlasD1Ev(
    QSGRhiAtlasTexture::Atlas *self) {
  delete self;
}

//  bool QSGRhiAtlasTexture::Atlas::generateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSGRhiAtlasTexture5Atlas15generateTextureEv(
    QSGRhiAtlasTexture::Atlas *self) {
  return self->generateTexture();
}

//  void QSGRhiAtlasTexture::Atlas::enqueueTextureUpload(TextureBase *t,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture5Atlas20enqueueTextureUploadEPNS_11TextureBaseEP23QRhiResourceUpdateBatch(
    QSGRhiAtlasTexture::Atlas *self,
    QSGRhiAtlasTexture::TextureBase *t,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->enqueueTextureUpload(t, resourceUpdates);
}

//  Texture *QSGRhiAtlasTexture::Atlas::create(const QImage &image)
extern "C" Q_DECL_EXPORT
QSGRhiAtlasTexture::Texture *ritual_ZN18QSGRhiAtlasTexture5Atlas6createERK6QImage(
    QSGRhiAtlasTexture::Atlas *self,
    const QImage *image) {
  return self->create(*image);
}

//  QRhiTexture::Format QSGRhiAtlasTexture::Atlas::format() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK18QSGRhiAtlasTexture5Atlas6formatEv(
    const QSGRhiAtlasTexture::Atlas *self) {
  return self->format();
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_Atlas, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_Atlas(
    QSGRhiAtlasTexture::Atlas *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_Atlas *>(self)->take(key, call);
}

//  bool QSGRhiAtlasTexture::Atlas::generateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QSGRhiAtlasTexture5Atlas15generateTextureEv(
    QSGRhiAtlasTexture::Atlas *self) {
  return self->QSGRhiAtlasTexture::Atlas::generateTexture();
}
