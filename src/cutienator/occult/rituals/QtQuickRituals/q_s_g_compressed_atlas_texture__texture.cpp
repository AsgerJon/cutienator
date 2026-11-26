//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcompressedatlastexture_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QSGCompressedAtlasTexture::Texture' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcompressedatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QSGCompressedAtlasTexture_Texture.cpp, line 1, as moc:QSGCompressedAtlasTexture::Texture
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t {};
} // unnamed namespace

template <> constexpr inline auto QSGCompressedAtlasTexture::Texture::qt_create_metaobjectdata<qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSGCompressedAtlasTexture::Texture"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Texture, qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSGCompressedAtlasTexture::Texture::staticMetaObject = { {
    QMetaObject::SuperData::link<QSGRhiAtlasTexture::TextureBase::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t>.metaTypes,
    nullptr
} };

void QSGCompressedAtlasTexture::Texture::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Texture *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSGCompressedAtlasTexture::Texture::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSGCompressedAtlasTexture::Texture::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QSGCompressedAtlasTexture7TextureE_t>.strings))
        return static_cast<void*>(this);
    return QSGRhiAtlasTexture::TextureBase::qt_metacast(_clname);
}

int QSGCompressedAtlasTexture::Texture::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSGRhiAtlasTexture::TextureBase::qt_metacall(_c, _id, _a);
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

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 110, as _ZNK25QSGCompressedAtlasTexture7Texture15hasAlphaChannelEv
namespace QSGCompressedAtlasTexture {
inline bool Texture::hasAlphaChannel() const
{
    return !QSGCompressedTexture::formatIsOpaque(static_cast<Atlas*>(m_atlas)->format());
}
}  // namespace QSGCompressedAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 115, as _ZNK25QSGCompressedAtlasTexture7Texture16removedFromAtlasEP23QRhiResourceUpdateBatch
namespace QSGCompressedAtlasTexture {
inline QSGTexture *Texture::removedFromAtlas(QRhiResourceUpdateBatch *) const
{
    if (m_nonatlas_texture) {
        m_nonatlas_texture->setMipmapFiltering(mipmapFiltering());
        m_nonatlas_texture->setFiltering(filtering());
        return m_nonatlas_texture;
    }

    if (!m_data.isEmpty()) {
        QTextureFileData texData;
        texData.setData(m_data);
        texData.setSize(m_size);
        texData.setGLInternalFormat(static_cast<Atlas*>(m_atlas)->format());
        texData.setDataLength(m_data.size());
        texData.setDataOffset(0);
        m_nonatlas_texture = new QSGCompressedTexture(texData);
        m_nonatlas_texture->setMipmapFiltering(mipmapFiltering());
        m_nonatlas_texture->setFiltering(filtering());
    }

    return m_nonatlas_texture;
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

//  from ../qtdeclarative/src/quick/scenegraph/compressedtexture/qsgcompressedatlastexture.cpp, line 105, as _ZN25QSGCompressedAtlasTexture7TextureD1Ev
namespace QSGCompressedAtlasTexture {
inline Texture::~Texture()
{
    delete m_nonatlas_texture;
}
}  // namespace QSGCompressedAtlasTexture
//  -----------------------------------------------------------------------

//  A QSGCompressedAtlasTexture::Texture that Python can take functions over in. Every QSGCompressedAtlasTexture::Texture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSGCompressedAtlasTexture_TextureCall0)(const void *, int *);
typedef bool (*CuteQSGCompressedAtlasTexture_TextureCall1)(const void *, int *);
typedef bool (*CuteQSGCompressedAtlasTexture_TextureCall2)(const void *, int *);
typedef const QRectF * (*CuteQSGCompressedAtlasTexture_TextureCall3)(const void *, int *);
typedef void * (*CuteQSGCompressedAtlasTexture_TextureCall4)(const void *, QRhiResourceUpdateBatch *, int *);
typedef qint64 (*CuteQSGCompressedAtlasTexture_TextureCall5)(const void *, int *);
typedef void * (*CuteQSGCompressedAtlasTexture_TextureCall6)(const void *, int *);
typedef void (*CuteQSGCompressedAtlasTexture_TextureCall7)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef bool (*CuteQSGCompressedAtlasTexture_TextureCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedAtlasTexture_TextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedAtlasTexture_TextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_TextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_TextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_TextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_TextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedAtlasTexture_TextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGCompressedAtlasTexture_Texture : public QSGCompressedAtlasTexture::Texture {
public:
  using QSGCompressedAtlasTexture::Texture::Texture;
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

  //  QSize QSGCompressedAtlasTexture::Texture::textureSize() const
  QSize textureSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall0 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGCompressedAtlasTexture::Texture::textureSize();
  }

  //  bool QSGCompressedAtlasTexture::Texture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall1 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedAtlasTexture::Texture::hasAlphaChannel();
  }

  //  bool QSGCompressedAtlasTexture::Texture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall2 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedAtlasTexture::Texture::hasMipmaps();
  }

  //  QRectF QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect()
  //      const
  QRectF normalizedTextureSubRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall3 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect();
  }

  //  QSGTexture *QSGCompressedAtlasTexture::Texture::removedFromAtlas(QRhi
  //      ResourceUpdateBatch *a0) const
  QSGTexture *removedFromAtlas(QRhiResourceUpdateBatch *a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall4 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall4>(taken[4]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGCompressedAtlasTexture::Texture::removedFromAtlas(a0);
  }

  //  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall5 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::comparisonKey();
  }

  //  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall6 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall6>(taken[6]);
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
      CuteQSGCompressedAtlasTexture_TextureCall7 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall7>(taken[7]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::TextureBase::commitTextureOperations(rhi, resourceUpdates);
  }

  //  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGCompressedAtlasTexture_TextureCall8 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall8>(taken[8]);
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
      CuteQSGCompressedAtlasTexture_TextureCall9 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall9>(taken[9]);
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
      CuteQSGCompressedAtlasTexture_TextureCall10 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall10>(taken[10]);
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
      CuteQSGCompressedAtlasTexture_TextureCall11 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall11>(taken[11]);
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
      CuteQSGCompressedAtlasTexture_TextureCall12 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall12>(taken[12]);
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
      CuteQSGCompressedAtlasTexture_TextureCall13 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall13>(taken[13]);
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
      CuteQSGCompressedAtlasTexture_TextureCall14 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall14>(taken[14]);
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
      CuteQSGCompressedAtlasTexture_TextureCall15 call = reinterpret_cast<CuteQSGCompressedAtlasTexture_TextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGCompressedAtlasTexture::Texture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QSGCompressedAtlasTexture7Texture10metaObjectEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return self->metaObject();
}

//  void *QSGCompressedAtlasTexture::Texture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QSGCompressedAtlasTexture7Texture11qt_metacastEPKc(
    QSGCompressedAtlasTexture::Texture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGCompressedAtlasTexture::Texture::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QSGCompressedAtlasTexture7Texture11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGCompressedAtlasTexture::Texture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGCompressedAtlasTexture::Texture::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QSGCompressedAtlasTexture7Texture2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGCompressedAtlasTexture::Texture::tr(s, c, n));
}

//  QSGCompressedAtlasTexture::Texture::Texture(Atlas *atlas, const QRect
//      &textureRect, QByteArrayView data, const QSize &size)
extern "C" Q_DECL_EXPORT
QSGCompressedAtlasTexture::Texture *ritual_ZN25QSGCompressedAtlasTexture7TextureC1EPNS_5AtlasERK5QRect14QByteArrayViewRK5QSize(
    QSGCompressedAtlasTexture::Atlas *atlas,
    const QRect *textureRect,
    const QByteArrayView *data,
    const QSize *size) {
  return new CuteQSGCompressedAtlasTexture_Texture(
      atlas,
      *textureRect,
      *data,
      *size);
}

//  QSGCompressedAtlasTexture::Texture::~Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGCompressedAtlasTexture7TextureD1Ev(
    QSGCompressedAtlasTexture::Texture *self) {
  delete self;
}

//  QSize QSGCompressedAtlasTexture::Texture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QSGCompressedAtlasTexture7Texture11textureSizeEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return new QSize(self->textureSize());
}

//  bool QSGCompressedAtlasTexture::Texture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSGCompressedAtlasTexture7Texture15hasAlphaChannelEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGCompressedAtlasTexture::Texture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSGCompressedAtlasTexture7Texture10hasMipmapsEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return self->hasMipmaps();
}

//  QRectF QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect()
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK25QSGCompressedAtlasTexture7Texture24normalizedTextureSubRectEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return new QRectF(self->normalizedTextureSubRect());
}

//  QSGTexture *QSGCompressedAtlasTexture::Texture::removedFromAtlas(QRhiReso
//      urceUpdateBatch *a0) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK25QSGCompressedAtlasTexture7Texture16removedFromAtlasEP23QRhiResourceUpdateBatch(
    const QSGCompressedAtlasTexture::Texture *self,
    QRhiResourceUpdateBatch *a0) {
  return self->removedFromAtlas(a0);
}

//  const QByteArray &QSGCompressedAtlasTexture::Texture::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QSGCompressedAtlasTexture7Texture4dataEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return new QByteArray(self->data());
}

//  int QSGCompressedAtlasTexture::Texture::sizeInBytes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QSGCompressedAtlasTexture7Texture11sizeInBytesEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return self->sizeInBytes();
}

//  a Python function taken by a CuteQSGCompressedAtlasTexture_Texture, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCompressedAtlasTexture_Texture(
    QSGCompressedAtlasTexture::Texture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCompressedAtlasTexture_Texture *>(self)->take(key, call);
}

//  QSize QSGCompressedAtlasTexture::Texture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK25QSGCompressedAtlasTexture7Texture11textureSizeEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return new QSize(self->QSGCompressedAtlasTexture::Texture::textureSize());
}

//  bool QSGCompressedAtlasTexture::Texture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QSGCompressedAtlasTexture7Texture15hasAlphaChannelEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return self->QSGCompressedAtlasTexture::Texture::hasAlphaChannel();
}

//  bool QSGCompressedAtlasTexture::Texture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QSGCompressedAtlasTexture7Texture10hasMipmapsEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return self->QSGCompressedAtlasTexture::Texture::hasMipmaps();
}

//  QRectF QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect()
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK25QSGCompressedAtlasTexture7Texture24normalizedTextureSubRectEv(
    const QSGCompressedAtlasTexture::Texture *self) {
  return new QRectF(
      self->QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect());
}

//  QSGTexture *QSGCompressedAtlasTexture::Texture::removedFromAtlas(QRhiReso
//      urceUpdateBatch *a0) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK25QSGCompressedAtlasTexture7Texture16removedFromAtlasEP23QRhiResourceUpdateBatch(
    const QSGCompressedAtlasTexture::Texture *self,
    QRhiResourceUpdateBatch *a0) {
  return self->QSGCompressedAtlasTexture::Texture::removedFromAtlas(a0);
}
