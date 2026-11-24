//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickcontext2d_p.h"
#include "qquickcontext2dcommandbuffer_p.h"
#include "qquickcanvasitem_p.h"
#include <private/qtquickglobal_p.h>
#include <private/qquickcontext2dtexture_p.h>
#include <private/qquickitem_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/private/qquickshadereffectsource_p.h>
#endif
#include <qsgrendererinterface.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtGui/private/qguisvg_p.h>
#if QT_CONFIG(quick_path)
#include <private/qquickpath_p.h>
#endif
#include <private/qquickimage_p_p.h>
#include <qqmlinfo.h>
#include <qqmlengine.h>
#include <private/qv4domerrors_p.h>
#include <private/qv4engine_p.h>
#include <private/qv4object_p.h>
#include <private/qv4qobjectwrapper_p.h>
#include <private/qquickwindow_p.h>
#include <private/qv4value_p.h>
#include <private/qv4functionobject_p.h>
#include <private/qv4objectproto_p.h>
#include <private/qv4scopedvalue_p.h>
#include <private/qlocale_tools_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qvector.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QRunnable>
#include <QtGui/qguiapplication.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformintegration.h>
#include <private/qsgdefaultrendercontext_p.h>
#include <QtCore/qpointer.h>
#include <cmath>
#if defined(Q_OS_QNX) || defined(Q_OS_ANDROID)
#include <ctype.h>
#endif
#include "qquickcontext2dtile_p.h"
#include "qquickcontext2dtexture_p.h"
#include "qquickcontext2dtile_p.h"
#include "qquickcanvasitem_p.h"
#include <private/qquickitem_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include "qquickcontext2dcommandbuffer_p.h"
#include <QtCore/QThread>
#include <QtGui/QGuiApplication>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4166, as _ZN15QQuickContext2D15setGrabbedImageERK6QImage
inline void QQuickContext2D::setGrabbedImage(const QImage& grab)
{
    m_grabbedImage = grab;
    m_grabbed = true;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 61, as _ZN24QQuickContext2DImageTileC1Ev
inline QQuickContext2DImageTile::QQuickContext2DImageTile()
    : QQuickContext2DTile()
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 9, as _ZN19QQuickContext2DTileC2Ev
inline QQuickContext2DTile::QQuickContext2DTile()
    : m_dirty(true)
    , m_rect(QRect(0, 0, 1, 1))
    , m_device(nullptr)
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 324, as _ZN27QQuickContext2DImageTextureD1Ev
inline QQuickContext2DImageTexture::~QQuickContext2DImageTexture()
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 328, as _ZNK27QQuickContext2DImageTexture12renderTargetEv
inline QQuickCanvasItem::RenderTarget QQuickContext2DImageTexture::renderTarget() const
{
    return QQuickCanvasItem::Image;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 333, as _ZNK27QQuickContext2DImageTexture10createTileEv
inline QQuickContext2DTile* QQuickContext2DImageTexture::createTile() const
{
    return new QQuickContext2DImageTile();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 386, as _ZN27QQuickContext2DImageTexture11endPaintingEv
inline void QQuickContext2DImageTexture::endPainting()
{
    QQuickContext2DTexture::endPainting();
    if (m_onCustomThread)
        m_mutex.lock();
    m_displayImage = m_image;
    if (m_onCustomThread)
        m_mutex.unlock();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 396, as _ZN27QQuickContext2DImageTexture13compositeTileEP19QQuickContext2DTile
inline void QQuickContext2DImageTexture::compositeTile(QQuickContext2DTile* tile)
{
    Q_ASSERT(!tile->dirty());
    QQuickContext2DImageTile* t = static_cast<QQuickContext2DImageTile*>(tile);
    QRect target = t->rect().intersected(m_canvasWindow);
    if (target.isValid()) {
        QRect source = target;
        source.moveTo(source.topLeft() - t->rect().topLeft());
        target.moveTo(target.topLeft() - m_canvasWindow.topLeft());

        m_painter.begin(&m_image);
        m_painter.setCompositionMode(QPainter::CompositionMode_Source);
        m_painter.drawImage(target, t->image(), source);
        m_painter.end();
    }
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 349, as _ZN27QQuickContext2DImageTexture19textureForNextFrameEP10QSGTextureP12QQuickWindow
inline QSGTexture *QQuickContext2DImageTexture::textureForNextFrame(QSGTexture *last, QQuickWindow *window)
{
    if (m_onCustomThread)
        m_mutex.lock();

    delete last;

    QSGTexture *texture = window->createTextureFromImage(m_displayImage, QQuickWindow::TextureCanUseAtlas);
    m_dirtyTexture = false;

    if (m_onCustomThread)
        m_mutex.unlock();

    return texture;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 338, as _ZN27QQuickContext2DImageTexture9grabImageERK6QRectF
inline void QQuickContext2DImageTexture::grabImage(const QRectF& rf)
{
    Q_ASSERT(rf.isValid());
    QQuickContext2D::mutex.lock();
    if (m_context) {
        QImage grabbed = m_displayImage.copy(rf.toRect());
        m_context->setGrabbedImage(grabbed);
    }
    QQuickContext2D::mutex.unlock();
}
//  -----------------------------------------------------------------------

//  A QQuickContext2DImageTexture that Python can take functions over in. Every QQuickContext2DImageTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef int (*CuteQQuickContext2DImageTextureCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DImageTextureCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DImageTextureCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DImageTextureCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DImageTextureCall4)(const void *, QQuickContext2DTile *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DImageTextureCall5)(const void *, QSGTexture *, QQuickWindow *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DImageTextureCall6)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
typedef bool (*CuteQQuickContext2DImageTextureCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
typedef const QVector2D * (*CuteQQuickContext2DImageTextureCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef const QSize * (*CuteQQuickContext2DImageTextureCall9)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContext2DImageTextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DImageTextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DImageTextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DImageTextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DImageTextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DImageTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickContext2DImageTexture : public QQuickContext2DImageTexture {
public:
  using QQuickContext2DImageTexture::QQuickContext2DImageTexture;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK22QQuickContext2DTexture12renderTargetEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK22QQuickContext2DTexture10createTileEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture13beginPaintingEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture11endPaintingEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture13compositeTileEP19QQuickContext2DTile")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture19textureForNextFrameEP10QSGTextureP12QQuickWindow")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture9grabImageERK6QRectF")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK22QQuickContext2DTexture11scaleFactorEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
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

#if QT_CONFIG(quick_canvas)
  //  QQuickCanvasItem::RenderTarget
  //      QQuickContext2DImageTexture::renderTarget() const
  QQuickCanvasItem::RenderTarget renderTarget() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall0 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickCanvasItem::RenderTarget>(given);
    }
    return QQuickContext2DImageTexture::renderTarget();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QQuickContext2DTile *QQuickContext2DImageTexture::createTile() const
  QQuickContext2DTile *createTile() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall1 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickContext2DTile *>(given);
    }
    return QQuickContext2DImageTexture::createTile();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QPaintDevice *QQuickContext2DImageTexture::beginPainting()
  QPaintDevice *beginPainting() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall2 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QQuickContext2DImageTexture::beginPainting();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DImageTexture::endPainting()
  void endPainting() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall3 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContext2DImageTexture::endPainting();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DImageTexture::compositeTile(QQuickContext2DTile
  //      *tile)
  void compositeTile(QQuickContext2DTile *tile) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall4 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall4>(taken[4]);
      call(this, tile, &handled);
      if (handled) return;
    }
    QQuickContext2DImageTexture::compositeTile(tile);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QSGTexture
  //      *QQuickContext2DImageTexture::textureForNextFrame(QSGTexture
  //      *lastFrame, QQuickWindow *window)
  QSGTexture *textureForNextFrame(
      QSGTexture *lastFrame,
      QQuickWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall5 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall5>(taken[5]);
      void * given = call(this, lastFrame, window, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QQuickContext2DImageTexture::textureForNextFrame(lastFrame, window);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DImageTexture::grabImage(const QRectF &region)
  void grabImage(const QRectF &region) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall6 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall6>(taken[6]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QQuickContext2DImageTexture::grabImage(region);
  }
#endif  // QT_CONFIG(quick_canvas)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
  //  bool QQuickContext2DTexture::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall7 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall7>(taken[7]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickContext2DTexture::event(e);
  }
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_canvas)
  //  QVector2D QQuickContext2DTexture::scaleFactor() const
  QVector2D scaleFactor() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall8 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall8>(taken[8]);
      const QVector2D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickContext2DTexture::scaleFactor();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QSize QQuickContext2DTexture::adjustedTileSize(const QSize &ts)
  QSize adjustedTileSize(const QSize &ts) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall9 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall9>(taken[9]);
      const QSize * given = call(this, &ts, &handled);
      if (handled && given) return *given;
    }
    return QQuickContext2DTexture::adjustedTileSize(ts);
  }
#endif  // QT_CONFIG(quick_canvas)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickContext2DImageTextureCall10 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall10>(taken[10]);
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
      CuteQQuickContext2DImageTextureCall11 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall11>(taken[11]);
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
      CuteQQuickContext2DImageTextureCall12 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall12>(taken[12]);
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
      CuteQQuickContext2DImageTextureCall13 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall13>(taken[13]);
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
      CuteQQuickContext2DImageTextureCall14 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall14>(taken[14]);
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
      CuteQQuickContext2DImageTextureCall15 call = reinterpret_cast<CuteQQuickContext2DImageTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickContext2DImageTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickContext2DImageTexture10metaObjectEv(
    const QQuickContext2DImageTexture *self) {
  return self->metaObject();
}

//  QQuickContext2DImageTexture::~QQuickContext2DImageTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickContext2DImageTextureD1Ev(
    QQuickContext2DImageTexture *self) {
  delete self;
}

//  QQuickCanvasItem::RenderTarget
//      QQuickContext2DImageTexture::renderTarget() const
extern "C" Q_DECL_EXPORT
QQuickCanvasItem::RenderTarget ritual_ZNK27QQuickContext2DImageTexture12renderTargetEv(
    const QQuickContext2DImageTexture *self) {
  return self->renderTarget();
}

//  QQuickContext2DTile *QQuickContext2DImageTexture::createTile() const
extern "C" Q_DECL_EXPORT
QQuickContext2DTile *ritual_ZNK27QQuickContext2DImageTexture10createTileEv(
    const QQuickContext2DImageTexture *self) {
  return self->createTile();
}

//  void QQuickContext2DImageTexture::endPainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickContext2DImageTexture11endPaintingEv(
    QQuickContext2DImageTexture *self) {
  self->endPainting();
}

//  void QQuickContext2DImageTexture::compositeTile(QQuickContext2DTile
//      *tile)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickContext2DImageTexture13compositeTileEP19QQuickContext2DTile(
    QQuickContext2DImageTexture *self,
    QQuickContext2DTile *tile) {
  self->compositeTile(tile);
}

//  QSGTexture *QQuickContext2DImageTexture::textureForNextFrame(QSGTexture
//      *lastFrame, QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN27QQuickContext2DImageTexture19textureForNextFrameEP10QSGTextureP12QQuickWindow(
    QQuickContext2DImageTexture *self,
    QSGTexture *lastFrame,
    QQuickWindow *window) {
  return self->textureForNextFrame(lastFrame, window);
}

//  void QQuickContext2DImageTexture::grabImage(const QRectF &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickContext2DImageTexture9grabImageERK6QRectF(
    QQuickContext2DImageTexture *self,
    const QRectF *region) {
  self->grabImage(*region);
}

//  a Python function taken by a CuteQQuickContext2DImageTexture, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DImageTexture(
    QQuickContext2DImageTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DImageTexture *>(self)->take(key, call);
}

//  QQuickCanvasItem::RenderTarget
//      QQuickContext2DImageTexture::renderTarget() const
extern "C" Q_DECL_EXPORT
QQuickCanvasItem::RenderTarget ritual_own_ZNK27QQuickContext2DImageTexture12renderTargetEv(
    const QQuickContext2DImageTexture *self) {
  return self->QQuickContext2DImageTexture::renderTarget();
}

//  void QQuickContext2DImageTexture::endPainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickContext2DImageTexture11endPaintingEv(
    QQuickContext2DImageTexture *self) {
  self->QQuickContext2DImageTexture::endPainting();
}

//  void QQuickContext2DImageTexture::compositeTile(QQuickContext2DTile
//      *tile)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickContext2DImageTexture13compositeTileEP19QQuickContext2DTile(
    QQuickContext2DImageTexture *self,
    QQuickContext2DTile *tile) {
  self->QQuickContext2DImageTexture::compositeTile(tile);
}

//  QSGTexture *QQuickContext2DImageTexture::textureForNextFrame(QSGTexture
//      *lastFrame, QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZN27QQuickContext2DImageTexture19textureForNextFrameEP10QSGTextureP12QQuickWindow(
    QQuickContext2DImageTexture *self,
    QSGTexture *lastFrame,
    QQuickWindow *window) {
  return self->QQuickContext2DImageTexture::textureForNextFrame(
      lastFrame,
      window);
}

#endif  // QT_CONFIG(quick_canvas)
