//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <Qt3DExtras/private/qtext2dmaterial_p_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qblendequation.h>
#include <Qt3DRender/qblendequationarguments.h>
#include <Qt3DRender/qdepthtest.h>
#include <Qt3DRender/qabstracttexture.h>
#include <QtCore/QUrl>
#include <QtGui/QVector3D>
#include <QtGui/QVector4D>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <Qt3DCore/qgeometry.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qgeometryrenderer.h>
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <Qt3DExtras/private/distancefieldtextrenderer_p.h>
#include <Qt3DExtras/private/distancefieldtextrenderer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 145, as _ZN10Qt3DExtras15QText2DMaterial23setDistanceFieldTextureEPN10Qt3DRender16QAbstractTextureE
namespace Qt3DExtras {
inline void QText2DMaterial::setDistanceFieldTexture(Qt3DRender::QAbstractTexture *tex)
{
    Q_D(QText2DMaterial);
    d->m_distanceFieldTexture = tex;

    if (tex) {
        d->m_textureParameter->setValue(QVariant::fromValue(tex));
        d->m_textureSizeParameter->setValue(QVariant::fromValue(static_cast<float>(tex->width())));
    } else {
        d->m_textureParameter->setValue(0);
        d->m_textureSizeParameter->setValue(QVariant::fromValue(1.f));
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 139, as _ZN10Qt3DExtras15QText2DMaterial8setColorERK6QColor
namespace Qt3DExtras {
inline void QText2DMaterial::setColor(const QColor &color)
{
    Q_D(QText2DMaterial);
    d->m_colorParameter->setValue(QVariant::fromValue(color));
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 91, as _ZN10Qt3DExtras25DistanceFieldTextRendererD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline DistanceFieldTextRenderer::~DistanceFieldTextRenderer()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 95, as _ZN10Qt3DExtras25DistanceFieldTextRenderer12setGlyphDataEPN10Qt3DRender16QAbstractTextureERKSt6vectorIfSaIfEERKS4_ItSaItEE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void DistanceFieldTextRenderer::setGlyphData(Qt3DRender::QAbstractTexture *glyphTexture,
                                             const std::vector<float> &vertexData,
                                             const std::vector<quint16> &indexData)
{
    Q_D(DistanceFieldTextRenderer);

    const size_t vertexCount = vertexData.size() / 5;

    d->m_vertexBuffer->setData(QByteArray((char*) vertexData.data(), vertexData.size() * sizeof(float)));
    d->m_indexBuffer->setData(QByteArray((char*) indexData.data(), indexData.size() * sizeof(quint16)));
    d->m_positionAttr->setCount(uint(vertexCount));
    d->m_texCoordAttr->setCount(uint(vertexCount));
    d->m_indexAttr->setCount(uint(indexData.size()));

    d->m_material->setDistanceFieldTexture(glyphTexture);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 112, as _ZN10Qt3DExtras25DistanceFieldTextRenderer8setColorERK6QColor
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void DistanceFieldTextRenderer::setColor(const QColor &color)
{
    Q_D(DistanceFieldTextRenderer);
    d->m_material->setColor(color);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::DistanceFieldTextRenderer that Python can take functions over in. Every Qt3DExtras::DistanceFieldTextRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_DistanceFieldTextRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_DistanceFieldTextRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_DistanceFieldTextRenderer : public Qt3DExtras::DistanceFieldTextRenderer {
public:
  using Qt3DExtras::DistanceFieldTextRenderer::DistanceFieldTextRenderer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall0 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall1 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall2 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall3 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall4 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall5 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall6 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::DistanceFieldTextRenderer::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras25DistanceFieldTextRenderer10metaObjectEv(
    const Qt3DExtras::DistanceFieldTextRenderer *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::DistanceFieldTextRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer11qt_metacastEPKc(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::DistanceFieldTextRenderer::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DExtras::DistanceFieldTextRenderer::~DistanceFieldTextRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25DistanceFieldTextRendererD1Ev(
    Qt3DExtras::DistanceFieldTextRenderer *self) {
  delete self;
}

//  void Qt3DExtras::DistanceFieldTextRenderer::setGlyphData(Qt3DRender::QAbs
//      tractTexture *glyphTexture, const std::vector<float> &vertexData,
//      const std::vector<quint16> &indexData)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer12setGlyphDataEPN10Qt3DRender16QAbstractTextureERKSt6vectorIfSaIfEERKS4_ItSaItEE(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    Qt3DRender::QAbstractTexture *glyphTexture,
    const std::vector<float> *vertexData,
    const std::vector<quint16> *indexData) {
  self->setGlyphData(glyphTexture, *vertexData, *indexData);
}

//  void Qt3DExtras::DistanceFieldTextRenderer::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer8setColorERK6QColor(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    const QColor *color) {
  self->setColor(*color);
}

//  DistanceFieldTextRendererPrivate
//      *Qt3DExtras::DistanceFieldTextRenderer::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::DistanceFieldTextRendererPrivate *ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer6d_funcEv(
    Qt3DExtras::DistanceFieldTextRenderer *self) {
  return self->d_func();
}

//  const DistanceFieldTextRendererPrivate
//      *Qt3DExtras::DistanceFieldTextRenderer::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::DistanceFieldTextRendererPrivate *ritual_ZNK10Qt3DExtras25DistanceFieldTextRenderer6d_funcEv(
    const Qt3DExtras::DistanceFieldTextRenderer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_DistanceFieldTextRenderer,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_DistanceFieldTextRenderer(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_DistanceFieldTextRenderer *>(self)->take(key, call);
}
