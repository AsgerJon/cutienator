//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarecontext_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSGSoftwareRenderContext'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarecontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtQuick/qquickgraphicsconfiguration.h>
#include <QtGui/qrawfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgsoftwarepainternode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareglyphnode_p.h>
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/private/qsgsoftwarespritenode_p.h>
#endif
#include <QtCore/QCoreApplication>
#include <QtCore/QElapsedTimer>
#include <QtGui/QWindow>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QSGSoftwareRenderContext.cpp, line 1, as moc:QSGSoftwareRenderContext
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN24QSGSoftwareRenderContextE_t {};
} // unnamed namespace

template <> constexpr inline auto QSGSoftwareRenderContext::qt_create_metaobjectdata<qt_meta_tag_ZN24QSGSoftwareRenderContextE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSGSoftwareRenderContext"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSGSoftwareRenderContext, qt_meta_tag_ZN24QSGSoftwareRenderContextE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSGSoftwareRenderContext::staticMetaObject = { {
    QMetaObject::SuperData::link<QSGRenderContext::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSGSoftwareRenderContextE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSGSoftwareRenderContextE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN24QSGSoftwareRenderContextE_t>.metaTypes,
    nullptr
} };

void QSGSoftwareRenderContext::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSGSoftwareRenderContext *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSGSoftwareRenderContext::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSGSoftwareRenderContext::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSGSoftwareRenderContextE_t>.strings))
        return static_cast<void*>(this);
    return QSGRenderContext::qt_metacast(_clname);
}

int QSGSoftwareRenderContext::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSGRenderContext::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 93, as _ZN24QSGSoftwareRenderContext10invalidateEv
inline void QSGSoftwareRenderContext::invalidate()
{
    qDeleteAll(m_texturesToDelete);
    m_texturesToDelete.clear();

    qDeleteAll(m_textures);
    m_textures.clear();

    Q_ASSERT(m_fontEnginesToClean.isEmpty());

    qDeleteAll(m_glyphCaches);
    m_glyphCaches.clear();

    qDeleteAll(m_staleGlyphCaches);
    m_staleGlyphCaches.clear();

    m_sg->renderContextInvalidated(this);
    emit invalidated();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 118, as _ZN24QSGSoftwareRenderContext14createRendererEN20QSGRendererInterface10RenderModeE
inline QSGRenderer *QSGSoftwareRenderContext::createRenderer(QSGRendererInterface::RenderMode)
{
    return new QSGSoftwareRenderer(this);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 124, as _ZN24QSGSoftwareRenderContext15renderNextFrameEP11QSGRenderer
inline void QSGSoftwareRenderContext::renderNextFrame(QSGRenderer *renderer)
{
    renderer->renderScene();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 113, as _ZNK24QSGSoftwareRenderContext13createTextureERK6QImagej
inline QSGTexture *QSGSoftwareRenderContext::createTexture(const QImage &image, uint flags) const
{
    return new QSGSoftwarePixmapTexture(image, flags);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 129, as _ZNK24QSGSoftwareRenderContext14maxTextureSizeEv
inline int QSGSoftwareRenderContext::maxTextureSize() const
{
    return 2048;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 10, as _ZN24QSGSoftwarePixmapTextureC1ERK6QImagej
inline QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QImage &image, uint flags)
{
    // Prevent pixmap format conversion to reduce memory consumption
    // and surprises in calling code. (See QTBUG-47328)
    if (flags & QSGRenderContext::CreateTexture_Alpha) {
        //If texture should have an alpha
        m_pixmap = QPixmap::fromImage(image, Qt::NoFormatConversion);
    } else {
        //Force opaque texture
        m_pixmap = QPixmap::fromImage(image.convertToFormat(QImage::Format_RGB32), Qt::NoFormatConversion);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 28, as _ZN24QSGSoftwareRenderContextC1EP10QSGContext
inline QSGSoftwareRenderContext::QSGSoftwareRenderContext(QSGContext *ctx)
    : QSGRenderContext(ctx)
    , m_initialized(false)
    , m_activePainter(nullptr)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 85, as _ZN24QSGSoftwareRenderContext18initializeIfNeededEv
inline void QSGSoftwareRenderContext::initializeIfNeeded()
{
    if (m_initialized)
        return;
    m_initialized = true;
    emit initialized();
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareRenderContext that Python can take functions over in. Every QSGSoftwareRenderContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwareRenderContextCall0)(const void *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall1)(const void *, QSGRenderer *, int *);
typedef void * (*CuteQSGSoftwareRenderContextCall2)(const void *, const QImage *, uint, int *);
typedef void * (*CuteQSGSoftwareRenderContextCall3)(const void *, int, int *);
typedef int (*CuteQSGSoftwareRenderContextCall4)(const void *, int *);
typedef bool (*CuteQSGSoftwareRenderContextCall5)(const void *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall6)(const void *, const QSGRenderContext::InitParams *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall7)(const void *, qreal, QRhiCommandBuffer *, const QQuickGraphicsConfiguration *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall8)(const void *, QSGRenderer *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall9)(const void *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall10)(const void *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall11)(const void *, int *);
typedef void (*CuteQSGSoftwareRenderContextCall12)(const void *, int *);
typedef void * (*CuteQSGSoftwareRenderContextCall13)(const void *, const QRawFont *, int, int *);
typedef void * (*CuteQSGSoftwareRenderContextCall14)(const void *, const QRawFont *, int *);
typedef void * (*CuteQSGSoftwareRenderContextCall15)(const void *, const QSGCompressedTextureFactory *, int *);
typedef void * (*CuteQSGSoftwareRenderContextCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareRenderContextCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareRenderContextCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderContextCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderContextCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderContextCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderContextCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderContextCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareRenderContext : public QSGSoftwareRenderContext {
public:
  using QSGSoftwareRenderContext::QSGSoftwareRenderContext;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGRenderContext10invalidateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext15renderNextFrameEP11QSGRenderer")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext13createTextureERK6QImagej")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext14createRendererEN20QSGRendererInterface10RenderModeE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext14maxTextureSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext7isValidEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext7endSyncEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10preprocessEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext21invalidateGlyphCachesEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext16flushGlyphCachesEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRawFonti")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext27compressedTextureForFactoryEPK27QSGCompressedTextureFactory")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext3rhiEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGSoftwareRenderContext::invalidate()
  void invalidate() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall0 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderContext::invalidate();
  }

  //  void QSGSoftwareRenderContext::renderNextFrame(QSGRenderer *renderer)
  void renderNextFrame(QSGRenderer *renderer) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall1 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall1>(taken[1]);
      call(this, renderer, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderContext::renderNextFrame(renderer);
  }

  //  QSGTexture *QSGSoftwareRenderContext::createTexture(const QImage
  //      &image, uint flags) const
  QSGTexture *createTexture(const QImage &image, uint flags) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall2 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall2>(taken[2]);
      void * given = call(this, &image, flags, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGSoftwareRenderContext::createTexture(image, flags);
  }

  //  QSGRenderer *QSGSoftwareRenderContext::createRenderer(QSGRendererInte
  //      rface::RenderMode a0)
  QSGRenderer *createRenderer(QSGRendererInterface::RenderMode a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall3 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall3>(taken[3]);
      void * given = call(this, static_cast<int>(a0), &handled);
      if (handled) return static_cast<QSGRenderer *>(given);
    }
    return QSGSoftwareRenderContext::createRenderer(a0);
  }

  //  int QSGSoftwareRenderContext::maxTextureSize() const
  int maxTextureSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall4 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderContext::maxTextureSize();
  }

  //  bool QSGRenderContext::isValid() const
  bool isValid() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall5 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderContext::isValid();
  }

  //  void QSGRenderContext::initialize(const InitParams *params)
  void initialize(const QSGRenderContext::InitParams *params) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall6 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall6>(taken[6]);
      call(this, params, &handled);
      if (handled) return;
    }
    QSGRenderContext::initialize(params);
  }

  //  void QSGRenderContext::prepareSync(qreal devicePixelRatio,
  //      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
  void prepareSync(
      qreal devicePixelRatio,
      QRhiCommandBuffer *cb,
      const QQuickGraphicsConfiguration &config) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall7 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall7>(taken[7]);
      call(this, devicePixelRatio, cb, &config, &handled);
      if (handled) return;
    }
    QSGRenderContext::prepareSync(devicePixelRatio, cb, config);
  }

  //  void QSGRenderContext::endNextFrame(QSGRenderer *renderer)
  void endNextFrame(QSGRenderer *renderer) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall8 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall8>(taken[8]);
      call(this, renderer, &handled);
      if (handled) return;
    }
    QSGRenderContext::endNextFrame(renderer);
  }

  //  void QSGRenderContext::endSync()
  void endSync() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall9 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::endSync();
  }

  //  void QSGRenderContext::preprocess()
  void preprocess() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall10 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::preprocess();
  }

  //  void QSGRenderContext::invalidateGlyphCaches()
  void invalidateGlyphCaches() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall11 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::invalidateGlyphCaches();
  }

  //  void QSGRenderContext::flushGlyphCaches()
  void flushGlyphCaches() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall12 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::flushGlyphCaches();
  }

  //  QSGDistanceFieldGlyphCache
  //      *QSGRenderContext::distanceFieldGlyphCache(const QRawFont &font,
  //      int renderTypeQuality)
  QSGDistanceFieldGlyphCache *distanceFieldGlyphCache(
      const QRawFont &font,
      int renderTypeQuality) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall13 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall13>(taken[13]);
      void * given = call(this, &font, renderTypeQuality, &handled);
      if (handled) return static_cast<QSGDistanceFieldGlyphCache *>(given);
    }
    return QSGRenderContext::distanceFieldGlyphCache(font, renderTypeQuality);
  }

  //  QSGCurveGlyphAtlas *QSGRenderContext::curveGlyphAtlas(const QRawFont
  //      &font)
  QSGCurveGlyphAtlas *curveGlyphAtlas(const QRawFont &font) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall14 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall14>(taken[14]);
      void * given = call(this, &font, &handled);
      if (handled) return static_cast<QSGCurveGlyphAtlas *>(given);
    }
    return QSGRenderContext::curveGlyphAtlas(font);
  }

  //  QSGTexture *QSGRenderContext::compressedTextureForFactory(const
  //      QSGCompressedTextureFactory *a0) const
  QSGTexture *compressedTextureForFactory(
      const QSGCompressedTextureFactory *a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall15 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall15>(taken[15]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGRenderContext::compressedTextureForFactory(a0);
  }

  //  QRhi *QSGRenderContext::rhi() const
  QRhi *rhi() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall16 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhi *>(given);
    }
    return QSGRenderContext::rhi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall17 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall18 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall19 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall20 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall21 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall22 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGSoftwareRenderContextCall23 call = reinterpret_cast<CuteQSGSoftwareRenderContextCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGSoftwareRenderContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QSGSoftwareRenderContext10metaObjectEv(
    const QSGSoftwareRenderContext *self) {
  return self->metaObject();
}

//  void *QSGSoftwareRenderContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QSGSoftwareRenderContext11qt_metacastEPKc(
    QSGSoftwareRenderContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwareRenderContext::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSGSoftwareRenderContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwareRenderContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGSoftwareRenderContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QSGSoftwareRenderContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGSoftwareRenderContext::tr(s, c, n));
}

//  QSGSoftwareRenderContext::QSGSoftwareRenderContext(QSGContext *ctx)
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderContext *ritual_ZN24QSGSoftwareRenderContextC1EP10QSGContext(
    QSGContext *ctx) {
  return new CuteQSGSoftwareRenderContext(ctx);
}

//  void QSGSoftwareRenderContext::initializeIfNeeded()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareRenderContext18initializeIfNeededEv(
    QSGSoftwareRenderContext *self) {
  self->initializeIfNeeded();
}

//  void QSGSoftwareRenderContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareRenderContext10invalidateEv(
    QSGSoftwareRenderContext *self) {
  self->invalidate();
}

//  void QSGSoftwareRenderContext::renderNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareRenderContext15renderNextFrameEP11QSGRenderer(
    QSGSoftwareRenderContext *self,
    QSGRenderer *renderer) {
  self->renderNextFrame(renderer);
}

//  QSGTexture *QSGSoftwareRenderContext::createTexture(const QImage &image,
//      uint flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK24QSGSoftwareRenderContext13createTextureERK6QImagej(
    const QSGSoftwareRenderContext *self,
    const QImage *image,
    uint flags) {
  return self->createTexture(*image, flags);
}

//  QSGRenderer *QSGSoftwareRenderContext::createRenderer(QSGRendererInterfac
//      e::RenderMode a0)
extern "C" Q_DECL_EXPORT
QSGRenderer *ritual_ZN24QSGSoftwareRenderContext14createRendererEN20QSGRendererInterface10RenderModeE(
    QSGSoftwareRenderContext *self,
    QSGRendererInterface::RenderMode a0) {
  return self->createRenderer(a0);
}

//  int QSGSoftwareRenderContext::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QSGSoftwareRenderContext14maxTextureSizeEv(
    const QSGSoftwareRenderContext *self) {
  return self->maxTextureSize();
}

//  a Python function taken by a CuteQSGSoftwareRenderContext, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareRenderContext(
    QSGSoftwareRenderContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareRenderContext *>(self)->take(key, call);
}

//  void QSGSoftwareRenderContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareRenderContext10invalidateEv(
    QSGSoftwareRenderContext *self) {
  self->QSGSoftwareRenderContext::invalidate();
}

//  void QSGSoftwareRenderContext::renderNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareRenderContext15renderNextFrameEP11QSGRenderer(
    QSGSoftwareRenderContext *self,
    QSGRenderer *renderer) {
  self->QSGSoftwareRenderContext::renderNextFrame(renderer);
}

//  QSGTexture *QSGSoftwareRenderContext::createTexture(const QImage &image,
//      uint flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK24QSGSoftwareRenderContext13createTextureERK6QImagej(
    const QSGSoftwareRenderContext *self,
    const QImage *image,
    uint flags) {
  return self->QSGSoftwareRenderContext::createTexture(*image, flags);
}

//  QSGRenderer *QSGSoftwareRenderContext::createRenderer(QSGRendererInterfac
//      e::RenderMode a0)
extern "C" Q_DECL_EXPORT
QSGRenderer *ritual_own_ZN24QSGSoftwareRenderContext14createRendererEN20QSGRendererInterface10RenderModeE(
    QSGSoftwareRenderContext *self,
    QSGRendererInterface::RenderMode a0) {
  return self->QSGSoftwareRenderContext::createRenderer(a0);
}

//  int QSGSoftwareRenderContext::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QSGSoftwareRenderContext14maxTextureSizeEv(
    const QSGSoftwareRenderContext *self) {
  return self->QSGSoftwareRenderContext::maxTextureSize();
}
