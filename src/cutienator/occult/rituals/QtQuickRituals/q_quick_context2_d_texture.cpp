//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickcontext2dtexture_p.h>
#include <QtQuick/private/qquickcontext2dtile_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qquickcontext2dcommandbuffer_p.h>
#include <QtCore/QThread>
#include <QtGui/QGuiApplication>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 300, as _ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize
inline QSize QQuickContext2DTexture::adjustedTileSize(const QSize &ts)
{
    return ts;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 32, as _ZN22QQuickContext2DTextureD1Ev
inline QQuickContext2DTexture::~QQuickContext2DTexture()
{
   clearTiles();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 228, as _ZN22QQuickContext2DTexture9tiledRectERK6QRectFRK5QSize
inline QRect QQuickContext2DTexture::tiledRect(const QRectF& window, const QSize& tileSize)
{
    if (window.isEmpty())
        return QRect();

    const int tw = tileSize.width();
    const int th = tileSize.height();
    const int h1 = window.left() / tw;
    const int v1 = window.top() / th;

    const int htiles = ((window.right() - h1 * tw) + tw - 1)/tw;
    const int vtiles = ((window.bottom() - v1 * th) + th - 1)/th;

    return QRect(h1 * tw, v1 * th, htiles * tw, vtiles * th);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 47, as _ZN22QQuickContext2DTexture13setCanvasSizeERK5QSize
inline bool QQuickContext2DTexture::setCanvasSize(const QSize &size)
{
    if (m_canvasSize != size) {
        m_canvasSize = size;
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 56, as _ZN22QQuickContext2DTexture11setTileSizeERK5QSize
inline bool QQuickContext2DTexture::setTileSize(const QSize &size)
{
    if (m_tileSize != size) {
        m_tileSize = size;
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 65, as _ZN22QQuickContext2DTexture9setSmoothEb
inline void QQuickContext2DTexture::setSmooth(bool smooth)
{
    m_smooth = smooth;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 70, as _ZN22QQuickContext2DTexture15setAntialiasingEb
inline void QQuickContext2DTexture::setAntialiasing(bool antialiasing)
{
    m_antialiasing = antialiasing;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 113, as _ZN22QQuickContext2DTexture12setDirtyRectERK5QRect
inline bool QQuickContext2DTexture::setDirtyRect(const QRect &r)
{
    bool doDirty = false;
    if (m_tiledCanvas) {
        for (QQuickContext2DTile* t : std::as_const(m_tiles)) {
            bool dirty = t->rect().intersected(r).isValid();
            t->markDirty(dirty);
            if (dirty)
                doDirty = true;
        }
    } else {
        doDirty = m_canvasWindow.intersected(r).isValid();
    }
    return doDirty;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 178, as _ZN22QQuickContext2DTexture15canvasDestroyedEv
inline bool QQuickContext2DTexture::canvasDestroyed()
{
    return m_item == nullptr;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 305, as _ZN22QQuickContext2DTexture5eventEP6QEvent
inline bool QQuickContext2DTexture::event(QEvent *e)
{
    if ((int) e->type() == QEvent::User + 1) {
        PaintEvent *pe = static_cast<PaintEvent *>(e);
        paint(pe->buffer);
        return true;
    } else if ((int) e->type() == QEvent::User + 2) {
        CanvasChangeEvent *ce = static_cast<CanvasChangeEvent *>(e);
        canvasChanged(ce->canvasSize, ce->tileSize, ce->canvasWindow, ce->dirtyRect, ce->smooth, ce->antialiasing);
        return true;
    }
    return QObject::event(e);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 294, as _ZN22QQuickContext2DTexture10clearTilesEv
inline void QQuickContext2DTexture::clearTiles()
{
    qDeleteAll(m_tiles);
    m_tiles.clear();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 244, as _ZN22QQuickContext2DTexture11createTilesERK5QRect
inline QRect QQuickContext2DTexture::createTiles(const QRect& window)
{
    QList<QQuickContext2DTile*> oldTiles = m_tiles;
    m_tiles.clear();

    if (window.isEmpty()) {
        return QRect();
    }

    QRect r = tiledRect(window, adjustedTileSize(m_tileSize));

    const int tw = m_tileSize.width();
    const int th = m_tileSize.height();
    const int h1 = window.left() / tw;
    const int v1 = window.top() / th;


    const int htiles = r.width() / tw;
    const int vtiles = r.height() / th;

    for (int yy = 0; yy < vtiles; ++yy) {
        for (int xx = 0; xx < htiles; ++xx) {
            int ht = xx + h1;
            int vt = yy + v1;

            QQuickContext2DTile* tile = nullptr;

            QPoint pos(ht * tw, vt * th);
            QRect rect(pos, m_tileSize);

            for (int i = 0; i < oldTiles.size(); i++) {
                if (oldTiles[i]->rect() == rect) {
                    tile = oldTiles.takeAt(i);
                    break;
                }
            }

            if (!tile)
                tile = createTile();

            tile->setRect(rect);
            m_tiles.append(tile);
        }
    }

    qDeleteAll(oldTiles);

    return r;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickContext2DTexture may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickContext2DTexture : QQuickContext2DTexture {
  using QQuickContext2DTexture::scaleFactor;
  using QQuickContext2DTexture::beginPainting;
  using QQuickContext2DTexture::endPainting;
  using QQuickContext2DTexture::adjustedTileSize;
};

//  A QQuickContext2DTexture that Python can take functions over in. Every QQuickContext2DTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef int (*CuteQQuickContext2DTextureCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DTextureCall1)(const void *, QSGTexture *, QQuickWindow *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
typedef bool (*CuteQQuickContext2DTextureCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DTextureCall3)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef const QVector2D * (*CuteQQuickContext2DTextureCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DTextureCall5)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DTextureCall6)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DTextureCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DTextureCall8)(const void *, QQuickContext2DTile *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef const QSize * (*CuteQQuickContext2DTextureCall9)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContext2DTextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DTextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DTextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DTextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DTextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickContext2DTexture : public QQuickContext2DTexture {
public:
  using QQuickContext2DTexture::QQuickContext2DTexture;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK22QQuickContext2DTexture12renderTargetEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture19textureForNextFrameEP10QSGTextureP12QQuickWindow")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture9grabImageERK6QRectF")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK22QQuickContext2DTexture11scaleFactorEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture13beginPaintingEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture11endPaintingEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK22QQuickContext2DTexture10createTileEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN22QQuickContext2DTexture13compositeTileEP19QQuickContext2DTile")) {
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
  //  QQuickCanvasItem::RenderTarget QQuickContext2DTexture::renderTarget()
  //      const
  QQuickCanvasItem::RenderTarget renderTarget() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall0 call = reinterpret_cast<CuteQQuickContext2DTextureCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickCanvasItem::RenderTarget>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QSGTexture *QQuickContext2DTexture::textureForNextFrame(QSGTexture
  //      *lastFrame, QQuickWindow *window)
  QSGTexture *textureForNextFrame(
      QSGTexture *lastFrame,
      QQuickWindow *window) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall1 call = reinterpret_cast<CuteQQuickContext2DTextureCall1>(taken[1]);
      void * given = call(this, lastFrame, window, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_canvas)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_canvas)
  //  bool QQuickContext2DTexture::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall2 call = reinterpret_cast<CuteQQuickContext2DTextureCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickContext2DTexture::event(e);
  }
#endif  // QT_CONFIG(quick_canvas)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DTexture::grabImage(const QRectF &region)
  void grabImage(const QRectF &region) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall3 call = reinterpret_cast<CuteQQuickContext2DTextureCall3>(taken[3]);
      call(this, &region, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QVector2D QQuickContext2DTexture::scaleFactor() const
  QVector2D scaleFactor() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall4 call = reinterpret_cast<CuteQQuickContext2DTextureCall4>(taken[4]);
      const QVector2D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickContext2DTexture::scaleFactor();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QPaintDevice *QQuickContext2DTexture::beginPainting()
  QPaintDevice *beginPainting() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall5 call = reinterpret_cast<CuteQQuickContext2DTextureCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QQuickContext2DTexture::beginPainting();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DTexture::endPainting()
  void endPainting() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall6 call = reinterpret_cast<CuteQQuickContext2DTextureCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContext2DTexture::endPainting();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QQuickContext2DTile *QQuickContext2DTexture::createTile() const
  QQuickContext2DTile *createTile() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall7 call = reinterpret_cast<CuteQQuickContext2DTextureCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickContext2DTile *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DTexture::compositeTile(QQuickContext2DTile *tile)
  void compositeTile(QQuickContext2DTile *tile) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall8 call = reinterpret_cast<CuteQQuickContext2DTextureCall8>(taken[8]);
      call(this, tile, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QSize QQuickContext2DTexture::adjustedTileSize(const QSize &ts)
  QSize adjustedTileSize(const QSize &ts) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickContext2DTextureCall9 call = reinterpret_cast<CuteQQuickContext2DTextureCall9>(taken[9]);
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
      CuteQQuickContext2DTextureCall10 call = reinterpret_cast<CuteQQuickContext2DTextureCall10>(taken[10]);
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
      CuteQQuickContext2DTextureCall11 call = reinterpret_cast<CuteQQuickContext2DTextureCall11>(taken[11]);
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
      CuteQQuickContext2DTextureCall12 call = reinterpret_cast<CuteQQuickContext2DTextureCall12>(taken[12]);
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
      CuteQQuickContext2DTextureCall13 call = reinterpret_cast<CuteQQuickContext2DTextureCall13>(taken[13]);
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
      CuteQQuickContext2DTextureCall14 call = reinterpret_cast<CuteQQuickContext2DTextureCall14>(taken[14]);
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
      CuteQQuickContext2DTextureCall15 call = reinterpret_cast<CuteQQuickContext2DTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickContext2DTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickContext2DTexture10metaObjectEv(
    const QQuickContext2DTexture *self) {
  return self->metaObject();
}

//  QQuickContext2DTexture::~QQuickContext2DTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTextureD1Ev(QQuickContext2DTexture *self) {
  delete self;
}

//  QQuickCanvasItem::RenderTarget QQuickContext2DTexture::renderTarget()
//      const
extern "C" Q_DECL_EXPORT
QQuickCanvasItem::RenderTarget ritual_ZNK22QQuickContext2DTexture12renderTargetEv(
    const QQuickContext2DTexture *self) {
  return self->renderTarget();
}

//  QRect QQuickContext2DTexture::tiledRect(const QRectF &window, const QSize
//      &tileSize)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN22QQuickContext2DTexture9tiledRectERK6QRectFRK5QSize(
    const QRectF *window,
    const QSize *tileSize) {
  return new QRect(QQuickContext2DTexture::tiledRect(*window, *tileSize));
}

//  bool QQuickContext2DTexture::setCanvasSize(const QSize &size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickContext2DTexture13setCanvasSizeERK5QSize(
    QQuickContext2DTexture *self,
    const QSize *size) {
  return self->setCanvasSize(*size);
}

//  bool QQuickContext2DTexture::setTileSize(const QSize &size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickContext2DTexture11setTileSizeERK5QSize(
    QQuickContext2DTexture *self,
    const QSize *size) {
  return self->setTileSize(*size);
}

//  void QQuickContext2DTexture::setSmooth(bool smooth)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture9setSmoothEb(
    QQuickContext2DTexture *self,
    bool smooth) {
  self->setSmooth(smooth);
}

//  void QQuickContext2DTexture::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture15setAntialiasingEb(
    QQuickContext2DTexture *self,
    bool antialiasing) {
  self->setAntialiasing(antialiasing);
}

//  bool QQuickContext2DTexture::setDirtyRect(const QRect &dirtyRect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickContext2DTexture12setDirtyRectERK5QRect(
    QQuickContext2DTexture *self,
    const QRect *dirtyRect) {
  return self->setDirtyRect(*dirtyRect);
}

//  bool QQuickContext2DTexture::canvasDestroyed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickContext2DTexture15canvasDestroyedEv(
    QQuickContext2DTexture *self) {
  return self->canvasDestroyed();
}

//  void QQuickContext2DTexture::setOnCustomThread(bool is)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture17setOnCustomThreadEb(
    QQuickContext2DTexture *self,
    bool is) {
  self->setOnCustomThread(is);
}

//  bool QQuickContext2DTexture::isOnCustomThread() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickContext2DTexture16isOnCustomThreadEv(
    const QQuickContext2DTexture *self) {
  return self->isOnCustomThread();
}

//  QSGTexture *QQuickContext2DTexture::textureForNextFrame(QSGTexture
//      *lastFrame, QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN22QQuickContext2DTexture19textureForNextFrameEP10QSGTextureP12QQuickWindow(
    QQuickContext2DTexture *self,
    QSGTexture *lastFrame,
    QQuickWindow *window) {
  return self->textureForNextFrame(lastFrame, window);
}

//  bool QQuickContext2DTexture::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickContext2DTexture5eventEP6QEvent(
    QQuickContext2DTexture *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickContext2DTexture::grabImage(const QRectF &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture9grabImageERK6QRectF(
    QQuickContext2DTexture *self,
    const QRectF *region) {
  self->grabImage(*region);
}

//  QVector2D QQuickContext2DTexture::scaleFactor() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK22QQuickContext2DTexture11scaleFactorEv(
    const QQuickContext2DTexture *self) {
  return new QVector2D(self->scaleFactor());
}

//  QPaintDevice *QQuickContext2DTexture::beginPainting()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZN22QQuickContext2DTexture13beginPaintingEv(
    QQuickContext2DTexture *self) {
  return self->beginPainting();
}

//  void QQuickContext2DTexture::endPainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture11endPaintingEv(
    QQuickContext2DTexture *self) {
  self->endPainting();
}

//  QQuickContext2DTile *QQuickContext2DTexture::createTile() const
extern "C" Q_DECL_EXPORT
QQuickContext2DTile *ritual_ZNK22QQuickContext2DTexture10createTileEv(
    const QQuickContext2DTexture *self) {
  return self->createTile();
}

//  void QQuickContext2DTexture::compositeTile(QQuickContext2DTile *tile)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture13compositeTileEP19QQuickContext2DTile(
    QQuickContext2DTexture *self,
    QQuickContext2DTile *tile) {
  self->compositeTile(tile);
}

//  void QQuickContext2DTexture::clearTiles()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture10clearTilesEv(
    QQuickContext2DTexture *self) {
  self->clearTiles();
}

//  QSize QQuickContext2DTexture::adjustedTileSize(const QSize &ts)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize(
    QQuickContext2DTexture *self,
    const QSize *ts) {
  return new QSize(self->adjustedTileSize(*ts));
}

//  QRect QQuickContext2DTexture::createTiles(const QRect &window)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN22QQuickContext2DTexture11createTilesERK5QRect(
    QQuickContext2DTexture *self,
    const QRect *window) {
  return new QRect(self->createTiles(*window));
}

//  a Python function taken by a CuteQQuickContext2DTexture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DTexture(
    QQuickContext2DTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DTexture *>(self)->take(key, call);
}

//  QVector2D QQuickContext2DTexture::scaleFactor() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_own_ZNK22QQuickContext2DTexture11scaleFactorEv(
    const QQuickContext2DTexture *self) {
  return new QVector2D(
      static_cast<const OwnQQuickContext2DTexture *>(self)->OwnQQuickContext2DTexture::scaleFactor());
}

//  QPaintDevice *QQuickContext2DTexture::beginPainting()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZN22QQuickContext2DTexture13beginPaintingEv(
    QQuickContext2DTexture *self) {
  return static_cast<OwnQQuickContext2DTexture *>(self)->OwnQQuickContext2DTexture::beginPainting();
}

//  void QQuickContext2DTexture::endPainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickContext2DTexture11endPaintingEv(
    QQuickContext2DTexture *self) {
  static_cast<OwnQQuickContext2DTexture *>(self)->OwnQQuickContext2DTexture::endPainting();
}

//  QSize QQuickContext2DTexture::adjustedTileSize(const QSize &ts)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN22QQuickContext2DTexture16adjustedTileSizeERK5QSize(
    QQuickContext2DTexture *self,
    const QSize *ts) {
  return new QSize(
      static_cast<OwnQQuickContext2DTexture *>(self)->OwnQQuickContext2DTexture::adjustedTileSize(
          *ts));
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
