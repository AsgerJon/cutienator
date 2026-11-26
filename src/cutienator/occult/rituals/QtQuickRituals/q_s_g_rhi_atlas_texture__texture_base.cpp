//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QSGRhiAtlasTexture::TextureBase' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
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

//  from QtQuick__QSGRhiAtlasTexture_TextureBase.cpp, line 1, as moc:QSGRhiAtlasTexture::TextureBase
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t {};
} // unnamed namespace

template <> constexpr inline auto QSGRhiAtlasTexture::TextureBase::qt_create_metaobjectdata<qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSGRhiAtlasTexture::TextureBase"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<TextureBase, qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSGRhiAtlasTexture::TextureBase::staticMetaObject = { {
    QMetaObject::SuperData::link<QSGTexture::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t>.metaTypes,
    nullptr
} };

void QSGRhiAtlasTexture::TextureBase::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<TextureBase *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSGRhiAtlasTexture::TextureBase::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSGRhiAtlasTexture::TextureBase::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QSGRhiAtlasTexture11TextureBaseE_t>.strings))
        return static_cast<void*>(this);
    return QSGTexture::qt_metacast(_clname);
}

int QSGRhiAtlasTexture::TextureBase::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSGTexture::qt_metacall(_c, _id, _a);
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

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 153, as _ZN18QSGRhiAtlasTexture9AtlasBase6removeEPNS_11TextureBaseE
namespace QSGRhiAtlasTexture {
inline void AtlasBase::remove(TextureBase *t)
{
    QRect atlasRect = t->atlasSubRect();
    m_allocator.deallocate(atlasRect);
    m_pending_uploads.removeOne(t);
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

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 324, as _ZN18QSGRhiAtlasTexture11TextureBaseC1EPNS_9AtlasBaseERK5QRect
namespace QSGRhiAtlasTexture {
inline TextureBase::TextureBase(AtlasBase *atlas, const QRect &textureRect)
    : QSGTexture(*(new QSGTexturePrivate(this)))
    , m_allocated_rect(textureRect)
    , m_atlas(atlas)
{
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 331, as _ZN18QSGRhiAtlasTexture11TextureBaseD1Ev
namespace QSGRhiAtlasTexture {
inline TextureBase::~TextureBase()
{
    m_atlas->remove(this);
}
}  // namespace QSGRhiAtlasTexture
//  -----------------------------------------------------------------------

//  A QSGRhiAtlasTexture::TextureBase that Python can take functions over in. Every QSGRhiAtlasTexture::TextureBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQSGRhiAtlasTexture_TextureBaseCall0)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureBaseCall1)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall2)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall3)(const void *, int *);
typedef const QSize * (*CuteQSGRhiAtlasTexture_TextureBaseCall4)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall5)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall6)(const void *, int *);
typedef const QRectF * (*CuteQSGRhiAtlasTexture_TextureBaseCall7)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureBaseCall8)(const void *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_TextureBase : public QSGRhiAtlasTexture::TextureBase {
public:
  using QSGRhiAtlasTexture::TextureBase::TextureBase;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
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

  //  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::comparisonKey();
  }

  //  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall2>(taken[2]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::TextureBase::commitTextureOperations(rhi, resourceUpdates);
  }

  //  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::isAtlasTexture();
  }

  //  QSize QSGTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall8>(taken[8]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGTexture::removedFromAtlas(resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall9 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall9>(taken[9]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall10 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall10>(taken[10]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall11 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall11>(taken[11]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall12 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall12>(taken[12]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall13 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall13>(taken[13]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall14 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall14>(taken[14]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall15 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiAtlasTexture::TextureBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGRhiAtlasTexture11TextureBase10metaObjectEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->metaObject();
}

//  void *QSGRhiAtlasTexture::TextureBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QSGRhiAtlasTexture11TextureBase11qt_metacastEPKc(
    QSGRhiAtlasTexture::TextureBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRhiAtlasTexture::TextureBase::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QSGRhiAtlasTexture11TextureBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRhiAtlasTexture::TextureBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGRhiAtlasTexture::TextureBase::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSGRhiAtlasTexture11TextureBase2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGRhiAtlasTexture::TextureBase::tr(s, c, n));
}

//  QSGRhiAtlasTexture::TextureBase::TextureBase(AtlasBase *atlas, const
//      QRect &textureRect)
extern "C" Q_DECL_EXPORT
QSGRhiAtlasTexture::TextureBase *ritual_ZN18QSGRhiAtlasTexture11TextureBaseC1EPNS_9AtlasBaseERK5QRect(
    QSGRhiAtlasTexture::AtlasBase *atlas,
    const QRect *textureRect) {
  return new CuteQSGRhiAtlasTexture_TextureBase(atlas, *textureRect);
}

//  QSGRhiAtlasTexture::TextureBase::~TextureBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture11TextureBaseD1Ev(
    QSGRhiAtlasTexture::TextureBase *self) {
  delete self;
}

//  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QSGRhiAtlasTexture11TextureBase13comparisonKeyEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->comparisonKey();
}

//  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK18QSGRhiAtlasTexture11TextureBase10rhiTextureEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->rhiTexture();
}

//  void QSGRhiAtlasTexture::TextureBase::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture11TextureBase23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGRhiAtlasTexture::TextureBase *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(rhi, resourceUpdates);
}

//  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiAtlasTexture11TextureBase14isAtlasTextureEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->isAtlasTexture();
}

//  QRect QSGRhiAtlasTexture::TextureBase::atlasSubRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QSGRhiAtlasTexture11TextureBase12atlasSubRectEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return new QRect(self->atlasSubRect());
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_TextureBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_TextureBase(
    QSGRhiAtlasTexture::TextureBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_TextureBase *>(self)->take(key, call);
}

//  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase13comparisonKeyEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->QSGRhiAtlasTexture::TextureBase::comparisonKey();
}

//  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase10rhiTextureEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->QSGRhiAtlasTexture::TextureBase::rhiTexture();
}

//  void QSGRhiAtlasTexture::TextureBase::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSGRhiAtlasTexture11TextureBase23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGRhiAtlasTexture::TextureBase *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QSGRhiAtlasTexture::TextureBase::commitTextureOperations(
      rhi,
      resourceUpdates);
}

//  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase14isAtlasTextureEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->QSGRhiAtlasTexture::TextureBase::isAtlasTexture();
}
