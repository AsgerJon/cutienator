//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QSGRhiAtlasTexture::Texture' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
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

//  from QtQuick__QSGRhiAtlasTexture_Texture.cpp, line 1, as moc:QSGRhiAtlasTexture::Texture
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t {};
} // unnamed namespace

template <> constexpr inline auto QSGRhiAtlasTexture::Texture::qt_create_metaobjectdata<qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSGRhiAtlasTexture::Texture"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Texture, qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSGRhiAtlasTexture::Texture::staticMetaObject = { {
    QMetaObject::SuperData::link<TextureBase::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t>.metaTypes,
    nullptr
} };

void QSGRhiAtlasTexture::Texture::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Texture *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSGRhiAtlasTexture::Texture::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSGRhiAtlasTexture::Texture::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QSGRhiAtlasTexture7TextureE_t>.strings))
        return static_cast<void*>(this);
    return TextureBase::qt_metacast(_clname);
}

int QSGRhiAtlasTexture::Texture::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = TextureBase::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 354, as _ZN18QSGRhiAtlasTexture11TextureBase23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch
namespace QSGRhiAtlasTexture {
inline void TextureBase::commitTextureOperations(QRhi *rhi, QRhiResourceUpdateBatch *resourceUpdates)
{
#ifdef QT_NO_DEBUG
    Q_UNUSED(rhi);
#endif
    Q_ASSERT(rhi == m_atlas->m_rhi);
    m_atlas->commitTextureOperations(resourceUpdates);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 331, as _ZN18QSGRhiAtlasTexture11TextureBaseD2Ev
namespace QSGRhiAtlasTexture {
inline TextureBase::~TextureBase()
{
    m_atlas->remove(this);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 349, as _ZNK18QSGRhiAtlasTexture11TextureBase10rhiTextureEv
namespace QSGRhiAtlasTexture {
inline QRhiTexture *TextureBase::rhiTexture() const
{
    return m_atlas->m_texture;
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 336, as _ZNK18QSGRhiAtlasTexture11TextureBase13comparisonKeyEv
namespace QSGRhiAtlasTexture {
inline qint64 TextureBase::comparisonKey() const
{
    // We need special care here: a typical comparisonKey() implementation
    // returns a unique result when there is no underlying texture yet. This is
    // not quite ideal for atlasing however since textures with the same atlas
    // should be considered equal regardless of the state of the underlying
    // graphics resources.

    // base the comparison on the atlas ptr; this way textures for the same
    // atlas are considered equal
    return qint64(m_atlas);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 383, as _ZNK18QSGRhiAtlasTexture7Texture16removedFromAtlasEP23QRhiResourceUpdateBatch
namespace QSGRhiAtlasTexture {
inline QSGTexture *Texture::removedFromAtlas(QRhiResourceUpdateBatch *resourceUpdates) const
{
    if (!m_nonatlas_texture) {
        m_nonatlas_texture = new QSGPlainTexture;
        if (!m_image.isNull()) {
            m_nonatlas_texture->setImage(m_image);
            m_nonatlas_texture->setFiltering(filtering());
        } else {
            QSGDefaultRenderContext *rc = m_atlas->renderContext();
            QRhi *rhi = m_atlas->rhi();
            Q_ASSERT(rhi->isRecordingFrame());
            const QRect r = atlasSubRectWithoutPadding();

            QRhiTexture *extractTex = rhi->newTexture(m_atlas->texture()->format(), r.size());
            if (extractTex->create()) {
                bool ownResUpd = false;
                QRhiResourceUpdateBatch *resUpd = resourceUpdates;
                if (!resUpd) {
                    ownResUpd = true;
                    resUpd = rhi->nextResourceUpdateBatch();
                }
                QRhiTextureCopyDescription desc;
                desc.setSourceTopLeft(r.topLeft());
                desc.setPixelSize(r.size());
                resUpd->copyTexture(extractTex, m_atlas->texture(), desc);
                if (ownResUpd)
                    rc->currentFrameCommandBuffer()->resourceUpdate(resUpd);
            }

            m_nonatlas_texture->setTexture(extractTex);
            m_nonatlas_texture->setOwnsTexture(true);
            m_nonatlas_texture->setHasAlphaChannel(m_has_alpha);
            m_nonatlas_texture->setTextureSize(r.size());
        }
    }

    m_nonatlas_texture->setMipmapFiltering(mipmapFiltering());
    m_nonatlas_texture->setFiltering(filtering());
    return m_nonatlas_texture;
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

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 137, as _ZN18QSGRhiAtlasTexture9AtlasBase23commitTextureOperationsEP23QRhiResourceUpdateBatch
namespace QSGRhiAtlasTexture {
inline void AtlasBase::commitTextureOperations(QRhiResourceUpdateBatch *resourceUpdates)
{
    if (!m_allocated) {
        m_allocated = true;
        if (!generateTexture()) {
            qWarning("QSGTextureAtlas: Failed to create texture");
            return;
        }
    }

    for (TextureBase *t : std::as_const(m_pending_uploads))
        enqueueTextureUpload(t, resourceUpdates);

    m_pending_uploads.clear();
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

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 377, as _ZN18QSGRhiAtlasTexture7TextureD1Ev
namespace QSGRhiAtlasTexture {
inline Texture::~Texture()
{
    if (m_nonatlas_texture)
        delete m_nonatlas_texture;
}
}  // namespace QSGRhiAtlasTexture
//  -----------------------------------------------------------------------

//  A QSGRhiAtlasTexture::Texture that Python can take functions over in. Every QSGRhiAtlasTexture::Texture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSGRhiAtlasTexture_TextureCall0)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall1)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall2)(const void *, int *);
typedef const QRectF * (*CuteQSGRhiAtlasTexture_TextureCall3)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureCall4)(const void *, QRhiResourceUpdateBatch *, int *);
typedef qint64 (*CuteQSGRhiAtlasTexture_TextureCall5)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureCall6)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_TextureCall7)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_Texture : public QSGRhiAtlasTexture::Texture {
public:
  using QSGRhiAtlasTexture::Texture::Texture;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSize QSGRhiAtlasTexture::Texture::textureSize() const
  QSize textureSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiAtlasTexture::Texture::textureSize();
  }

  //  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::Texture::hasAlphaChannel();
  }

  //  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::Texture::hasMipmaps();
  }

  //  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiAtlasTexture::Texture::normalizedTextureSubRect();
  }

  //  QSGTexture *QSGRhiAtlasTexture::Texture::removedFromAtlas(QRhiResourc
  //      eUpdateBatch *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall4>(taken[4]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGRhiAtlasTexture::Texture::removedFromAtlas(resourceUpdates);
  }

  //  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::comparisonKey();
  }

  //  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGRhiAtlasTexture::TextureBase::rhiTexture();
  }

  //  void QSGRhiAtlasTexture::TextureBase::commitTextureOperations(QRhi
  //      *rhi, QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall7>(taken[7]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::TextureBase::commitTextureOperations(rhi, resourceUpdates);
  }

  //  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::isAtlasTexture();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall9 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall10 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall11 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall12 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall13 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall14 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall15 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiAtlasTexture::Texture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGRhiAtlasTexture7Texture10metaObjectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->metaObject();
}

//  void *QSGRhiAtlasTexture::Texture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QSGRhiAtlasTexture7Texture11qt_metacastEPKc(
    QSGRhiAtlasTexture::Texture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRhiAtlasTexture::Texture::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QSGRhiAtlasTexture7Texture11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRhiAtlasTexture::Texture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGRhiAtlasTexture::Texture::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSGRhiAtlasTexture7Texture2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGRhiAtlasTexture::Texture::tr(s, c, n));
}

//  QSGRhiAtlasTexture::Texture::Texture(Atlas *atlas, const QRect
//      &textureRect, const QImage &image)
extern "C" Q_DECL_EXPORT
QSGRhiAtlasTexture::Texture *ritual_ZN18QSGRhiAtlasTexture7TextureC1EPNS_5AtlasERK5QRectRK6QImage(
    QSGRhiAtlasTexture::Atlas *atlas,
    const QRect *textureRect,
    const QImage *image) {
  return new CuteQSGRhiAtlasTexture_Texture(atlas, *textureRect, *image);
}

//  QSGRhiAtlasTexture::Texture::~Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7TextureD1Ev(
    QSGRhiAtlasTexture::Texture *self) {
  delete self;
}

//  QSize QSGRhiAtlasTexture::Texture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QSGRhiAtlasTexture7Texture11textureSizeEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QSize(self->textureSize());
}

//  void QSGRhiAtlasTexture::Texture::setHasAlphaChannel(bool alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7Texture18setHasAlphaChannelEb(
    QSGRhiAtlasTexture::Texture *self,
    bool alpha) {
  self->setHasAlphaChannel(alpha);
}

//  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiAtlasTexture7Texture15hasAlphaChannelEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiAtlasTexture7Texture10hasMipmapsEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->hasMipmaps();
}

//  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QSGRhiAtlasTexture7Texture24normalizedTextureSubRectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRectF(self->normalizedTextureSubRect());
}

//  QRect QSGRhiAtlasTexture::Texture::atlasSubRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QSGRhiAtlasTexture7Texture12atlasSubRectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRect(self->atlasSubRect());
}

//  QRect QSGRhiAtlasTexture::Texture::atlasSubRectWithoutPadding() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QSGRhiAtlasTexture7Texture26atlasSubRectWithoutPaddingEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRect(self->atlasSubRectWithoutPadding());
}

//  QSGTexture
//      *QSGRhiAtlasTexture::Texture::removedFromAtlas(QRhiResourceUpdateBatc
//      h *resourceUpdates) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK18QSGRhiAtlasTexture7Texture16removedFromAtlasEP23QRhiResourceUpdateBatch(
    const QSGRhiAtlasTexture::Texture *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  return self->removedFromAtlas(resourceUpdates);
}

//  void QSGRhiAtlasTexture::Texture::releaseImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7Texture12releaseImageEv(
    QSGRhiAtlasTexture::Texture *self) {
  self->releaseImage();
}

//  const QImage &QSGRhiAtlasTexture::Texture::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK18QSGRhiAtlasTexture7Texture5imageEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QImage(self->image());
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_Texture, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_Texture(
    QSGRhiAtlasTexture::Texture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_Texture *>(self)->take(key, call);
}

//  QSize QSGRhiAtlasTexture::Texture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18QSGRhiAtlasTexture7Texture11textureSizeEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QSize(self->QSGRhiAtlasTexture::Texture::textureSize());
}

//  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSGRhiAtlasTexture7Texture15hasAlphaChannelEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->QSGRhiAtlasTexture::Texture::hasAlphaChannel();
}

//  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSGRhiAtlasTexture7Texture10hasMipmapsEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->QSGRhiAtlasTexture::Texture::hasMipmaps();
}

//  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK18QSGRhiAtlasTexture7Texture24normalizedTextureSubRectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRectF(
      self->QSGRhiAtlasTexture::Texture::normalizedTextureSubRect());
}

//  QSGTexture
//      *QSGRhiAtlasTexture::Texture::removedFromAtlas(QRhiResourceUpdateBatc
//      h *resourceUpdates) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK18QSGRhiAtlasTexture7Texture16removedFromAtlasEP23QRhiResourceUpdateBatch(
    const QSGRhiAtlasTexture::Texture *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  return self->QSGRhiAtlasTexture::Texture::removedFromAtlas(
      resourceUpdates);
}
