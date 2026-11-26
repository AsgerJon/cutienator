//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 126, as _ZN18QSGRhiAtlasTexture9AtlasBaseD1Ev
namespace QSGRhiAtlasTexture {
inline AtlasBase::~AtlasBase()
{
    Q_ASSERT(!m_texture);
}
}  // namespace QSGRhiAtlasTexture

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgrhiatlastexture.cpp, line 131, as _ZN18QSGRhiAtlasTexture9AtlasBase10invalidateEv
namespace QSGRhiAtlasTexture {
inline void AtlasBase::invalidate()
{
    delete m_texture;
    m_texture = nullptr;
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
//  -----------------------------------------------------------------------

//  A QSGRhiAtlasTexture::AtlasBase that Python can take functions over in. Every QSGRhiAtlasTexture::AtlasBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRhiAtlasTexture_AtlasBaseCall0)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_AtlasBaseCall1)(const void *, QSGRhiAtlasTexture::TextureBase *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_AtlasBaseCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_AtlasBaseCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasBaseCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasBaseCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasBaseCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasBaseCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasBaseCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_AtlasBase : public QSGRhiAtlasTexture::AtlasBase {
public:
  using QSGRhiAtlasTexture::AtlasBase::AtlasBase;
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

  //  bool QSGRhiAtlasTexture::AtlasBase::generateTexture()
  bool generateTexture() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasBaseCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGRhiAtlasTexture::AtlasBase::enqueueTextureUpload(TextureBase
  //      *t, QRhiResourceUpdateBatch *resourceUpdates)
  void enqueueTextureUpload(
      QSGRhiAtlasTexture::TextureBase *t,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasBaseCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall1>(taken[1]);
      call(this, t, resourceUpdates, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasBaseCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall2>(taken[2]);
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
      CuteQSGRhiAtlasTexture_AtlasBaseCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall3>(taken[3]);
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
      CuteQSGRhiAtlasTexture_AtlasBaseCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall4>(taken[4]);
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
      CuteQSGRhiAtlasTexture_AtlasBaseCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall5>(taken[5]);
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
      CuteQSGRhiAtlasTexture_AtlasBaseCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall6>(taken[6]);
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
      CuteQSGRhiAtlasTexture_AtlasBaseCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall7>(taken[7]);
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
      CuteQSGRhiAtlasTexture_AtlasBaseCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasBaseCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiAtlasTexture::AtlasBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGRhiAtlasTexture9AtlasBase10metaObjectEv(
    const QSGRhiAtlasTexture::AtlasBase *self) {
  return self->metaObject();
}

//  void *QSGRhiAtlasTexture::AtlasBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QSGRhiAtlasTexture9AtlasBase11qt_metacastEPKc(
    QSGRhiAtlasTexture::AtlasBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRhiAtlasTexture::AtlasBase::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QSGRhiAtlasTexture9AtlasBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRhiAtlasTexture::AtlasBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSGRhiAtlasTexture::AtlasBase::~AtlasBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture9AtlasBaseD1Ev(
    QSGRhiAtlasTexture::AtlasBase *self) {
  delete self;
}

//  void QSGRhiAtlasTexture::AtlasBase::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture9AtlasBase10invalidateEv(
    QSGRhiAtlasTexture::AtlasBase *self) {
  self->invalidate();
}

//  void QSGRhiAtlasTexture::AtlasBase::commitTextureOperations(QRhiResourceU
//      pdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture9AtlasBase23commitTextureOperationsEP23QRhiResourceUpdateBatch(
    QSGRhiAtlasTexture::AtlasBase *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(resourceUpdates);
}

//  void QSGRhiAtlasTexture::AtlasBase::remove(TextureBase *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture9AtlasBase6removeEPNS_11TextureBaseE(
    QSGRhiAtlasTexture::AtlasBase *self,
    QSGRhiAtlasTexture::TextureBase *t) {
  self->remove(t);
}

//  QSGDefaultRenderContext *QSGRhiAtlasTexture::AtlasBase::renderContext()
//      const
extern "C" Q_DECL_EXPORT
QSGDefaultRenderContext *ritual_ZNK18QSGRhiAtlasTexture9AtlasBase13renderContextEv(
    const QSGRhiAtlasTexture::AtlasBase *self) {
  return self->renderContext();
}

//  QRhi *QSGRhiAtlasTexture::AtlasBase::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK18QSGRhiAtlasTexture9AtlasBase3rhiEv(
    const QSGRhiAtlasTexture::AtlasBase *self) {
  return self->rhi();
}

//  QRhiTexture *QSGRhiAtlasTexture::AtlasBase::texture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK18QSGRhiAtlasTexture9AtlasBase7textureEv(
    const QSGRhiAtlasTexture::AtlasBase *self) {
  return self->texture();
}

//  QSize QSGRhiAtlasTexture::AtlasBase::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QSGRhiAtlasTexture9AtlasBase4sizeEv(
    const QSGRhiAtlasTexture::AtlasBase *self) {
  return new QSize(self->size());
}

//  bool QSGRhiAtlasTexture::AtlasBase::generateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSGRhiAtlasTexture9AtlasBase15generateTextureEv(
    QSGRhiAtlasTexture::AtlasBase *self) {
  return self->generateTexture();
}

//  void QSGRhiAtlasTexture::AtlasBase::enqueueTextureUpload(TextureBase *t,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture9AtlasBase20enqueueTextureUploadEPNS_11TextureBaseEP23QRhiResourceUpdateBatch(
    QSGRhiAtlasTexture::AtlasBase *self,
    QSGRhiAtlasTexture::TextureBase *t,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->enqueueTextureUpload(t, resourceUpdates);
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_AtlasBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_AtlasBase(
    QSGRhiAtlasTexture::AtlasBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_AtlasBase *>(self)->take(key, call);
}
