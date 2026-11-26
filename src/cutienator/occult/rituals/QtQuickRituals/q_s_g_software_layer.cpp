//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarelayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarelayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwarepixmaprenderer_p.h>
#include <QtQuick/private/qsgsoftwarepixmaprenderer_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/QSGSimpleRectNode>
#include <QtCore/QElapsedTimer>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 165, as _ZN16QSGSoftwareLayer11invalidatedEv
inline void QSGSoftwareLayer::invalidated()
{
    delete m_renderer;
    m_renderer = nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 27, as _ZN25QSGSoftwarePixmapRenderer11renderSceneEv
inline void QSGSoftwarePixmapRenderer::renderScene()
{
    QSGRenderer::renderScene();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 77, as _ZN25QSGSoftwarePixmapRenderer17setProjectionRectERK5QRect
inline void QSGSoftwarePixmapRenderer::setProjectionRect(const QRect &projectionRect)
{
    m_projectionRect = projectionRect;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 16, as _ZN25QSGSoftwarePixmapRendererC1EP16QSGRenderContext
inline QSGSoftwarePixmapRenderer::QSGSoftwarePixmapRenderer(QSGRenderContext *context)
    : QSGAbstractSoftwareRenderer(context)
{

}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 33, as _ZNK16QSGSoftwareLayer13comparisonKeyEv
inline qint64 QSGSoftwareLayer::comparisonKey() const
{
    return 0;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 38, as _ZNK16QSGSoftwareLayer11textureSizeEv
inline QSize QSGSoftwareLayer::textureSize() const
{
    return m_pixmap.size();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 43, as _ZNK16QSGSoftwareLayer15hasAlphaChannelEv
inline bool QSGSoftwareLayer::hasAlphaChannel() const
{
    return m_pixmap.hasAlphaChannel();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 48, as _ZNK16QSGSoftwareLayer10hasMipmapsEv
inline bool QSGSoftwareLayer::hasMipmaps() const
{
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 53, as _ZN16QSGSoftwareLayer13updateTextureEv
inline bool QSGSoftwareLayer::updateTexture()
{
    bool doGrab = (m_live || m_grab) && m_dirtyTexture;
    if (doGrab)
        grab();
    if (m_grab)
        emit scheduledUpdateCompleted();
    m_grab = false;
    return doGrab;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 64, as _ZN16QSGSoftwareLayer7setItemEP7QSGNode
inline void QSGSoftwareLayer::setItem(QSGNode *item)
{
    if (item == m_item)
        return;
    m_item = item;

    if (m_live && !m_item)
        m_pixmap = QPixmap();

    markDirtyTexture();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 76, as _ZN16QSGSoftwareLayer7setRectERK6QRectF
inline void QSGSoftwareLayer::setRect(const QRectF &rect)
{
    if (rect == m_rect)
        return;
    m_rect = rect;
    markDirtyTexture();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 84, as _ZN16QSGSoftwareLayer7setSizeERK5QSize
inline void QSGSoftwareLayer::setSize(const QSize &size)
{
    if (size == m_size)
        return;
    m_size = size;

    if (m_live && m_size.isNull())
        m_pixmap = QPixmap();

    markDirtyTexture();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 96, as _ZN16QSGSoftwareLayer14scheduleUpdateEv
inline void QSGSoftwareLayer::scheduleUpdate()
{
    if (m_grab)
        return;
    m_grab = true;
    if (m_dirtyTexture) {
        emit updateRequested();
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 106, as _ZNK16QSGSoftwareLayer7toImageEv
inline QImage QSGSoftwareLayer::toImage() const
{
    return m_pixmap.toImage();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 111, as _ZN16QSGSoftwareLayer7setLiveEb
inline void QSGSoftwareLayer::setLive(bool live)
{
    if (live == m_live)
        return;
    m_live = live;

    if (m_live && (!m_item || m_size.isNull()))
        m_pixmap = QPixmap();

    markDirtyTexture();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 123, as _ZN16QSGSoftwareLayer12setRecursiveEb
inline void QSGSoftwareLayer::setRecursive(bool recursive)
{
    m_recursive = recursive;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 128, as _ZN16QSGSoftwareLayer9setFormatEN8QSGLayer6FormatE
inline void QSGSoftwareLayer::setFormat(Format)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 132, as _ZN16QSGSoftwareLayer13setHasMipmapsEb
inline void QSGSoftwareLayer::setHasMipmaps(bool)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 136, as _ZN16QSGSoftwareLayer19setDevicePixelRatioEd
inline void QSGSoftwareLayer::setDevicePixelRatio(qreal ratio)
{
    m_device_pixel_ratio = ratio;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 141, as _ZN16QSGSoftwareLayer19setMirrorHorizontalEb
inline void QSGSoftwareLayer::setMirrorHorizontal(bool mirror)
{
    if (m_mirrorHorizontal == mirror)
        return;
    m_mirrorHorizontal = mirror;
    markDirtyTexture();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 149, as _ZN16QSGSoftwareLayer17setMirrorVerticalEb
inline void QSGSoftwareLayer::setMirrorVertical(bool mirror)
{
    if (m_mirrorVertical == mirror)
        return;
    m_mirrorVertical = mirror;
    markDirtyTexture();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 157, as _ZN16QSGSoftwareLayer16markDirtyTextureEv
inline void QSGSoftwareLayer::markDirtyTexture()
{
    m_dirtyTexture = true;
    if (m_live || m_grab) {
        emit updateRequested();
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 28, as _ZN16QSGSoftwareLayerD1Ev
inline QSGSoftwareLayer::~QSGSoftwareLayer()
{
    invalidated();
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareLayer that Python can take functions over in. Every QSGSoftwareLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQSGSoftwareLayerCall0)(const void *, int *);
typedef const QSize * (*CuteQSGSoftwareLayerCall1)(const void *, int *);
typedef bool (*CuteQSGSoftwareLayerCall2)(const void *, int *);
typedef bool (*CuteQSGSoftwareLayerCall3)(const void *, int *);
typedef bool (*CuteQSGSoftwareLayerCall4)(const void *, int *);
typedef void (*CuteQSGSoftwareLayerCall5)(const void *, QSGNode *, int *);
typedef void (*CuteQSGSoftwareLayerCall6)(const void *, const QRectF *, int *);
typedef void (*CuteQSGSoftwareLayerCall7)(const void *, const QSize *, int *);
typedef void (*CuteQSGSoftwareLayerCall8)(const void *, int *);
typedef const QImage * (*CuteQSGSoftwareLayerCall9)(const void *, int *);
typedef void (*CuteQSGSoftwareLayerCall10)(const void *, bool, int *);
typedef void (*CuteQSGSoftwareLayerCall11)(const void *, bool, int *);
typedef void (*CuteQSGSoftwareLayerCall12)(const void *, int, int *);
typedef void (*CuteQSGSoftwareLayerCall13)(const void *, bool, int *);
typedef void (*CuteQSGSoftwareLayerCall14)(const void *, qreal, int *);
typedef void (*CuteQSGSoftwareLayerCall15)(const void *, bool, int *);
typedef void (*CuteQSGSoftwareLayerCall16)(const void *, bool, int *);
typedef void (*CuteQSGSoftwareLayerCall17)(const void *, int, int *);
typedef void (*CuteQSGSoftwareLayerCall18)(const void *, int *);
typedef void (*CuteQSGSoftwareLayerCall19)(const void *, int *);
typedef void * (*CuteQSGSoftwareLayerCall20)(const void *, int *);
typedef const QRectF * (*CuteQSGSoftwareLayerCall21)(const void *, int *);
typedef bool (*CuteQSGSoftwareLayerCall22)(const void *, int *);
typedef void * (*CuteQSGSoftwareLayerCall23)(const void *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQSGSoftwareLayerCall24)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareLayerCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareLayerCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareLayerCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareLayerCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareLayerCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareLayerCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareLayerCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareLayer : public QSGSoftwareLayer {
public:
  using QSGSoftwareLayer::QSGSoftwareLayer;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QSGDynamicTexture13updateTextureEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setItemEP7QSGNode")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setRectERK6QRectF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setSizeERK5QSize")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer14scheduleUpdateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSGLayer7toImageEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setLiveEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer12setRecursiveEb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer9setFormatENS_6FormatE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer13setHasMipmapsEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer19setDevicePixelRatioEd")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer19setMirrorHorizontalEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer17setMirrorVerticalEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer10setSamplesEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer16markDirtyTextureEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer11invalidatedEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  qint64 QSGSoftwareLayer::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall0 call = reinterpret_cast<CuteQSGSoftwareLayerCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareLayer::comparisonKey();
  }

  //  QSize QSGSoftwareLayer::textureSize() const
  QSize textureSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall1 call = reinterpret_cast<CuteQSGSoftwareLayerCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareLayer::textureSize();
  }

  //  bool QSGSoftwareLayer::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall2 call = reinterpret_cast<CuteQSGSoftwareLayerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareLayer::hasAlphaChannel();
  }

  //  bool QSGSoftwareLayer::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall3 call = reinterpret_cast<CuteQSGSoftwareLayerCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareLayer::hasMipmaps();
  }

  //  bool QSGSoftwareLayer::updateTexture()
  bool updateTexture() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall4 call = reinterpret_cast<CuteQSGSoftwareLayerCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareLayer::updateTexture();
  }

  //  void QSGSoftwareLayer::setItem(QSGNode *item)
  void setItem(QSGNode *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall5 call = reinterpret_cast<CuteQSGSoftwareLayerCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setItem(item);
  }

  //  void QSGSoftwareLayer::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall6 call = reinterpret_cast<CuteQSGSoftwareLayerCall6>(taken[6]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setRect(rect);
  }

  //  void QSGSoftwareLayer::setSize(const QSize &size)
  void setSize(const QSize &size) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall7 call = reinterpret_cast<CuteQSGSoftwareLayerCall7>(taken[7]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setSize(size);
  }

  //  void QSGSoftwareLayer::scheduleUpdate()
  void scheduleUpdate() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall8 call = reinterpret_cast<CuteQSGSoftwareLayerCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::scheduleUpdate();
  }

  //  QImage QSGSoftwareLayer::toImage() const
  QImage toImage() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall9 call = reinterpret_cast<CuteQSGSoftwareLayerCall9>(taken[9]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareLayer::toImage();
  }

  //  void QSGSoftwareLayer::setLive(bool live)
  void setLive(bool live) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall10 call = reinterpret_cast<CuteQSGSoftwareLayerCall10>(taken[10]);
      call(this, live, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setLive(live);
  }

  //  void QSGSoftwareLayer::setRecursive(bool recursive)
  void setRecursive(bool recursive) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall11 call = reinterpret_cast<CuteQSGSoftwareLayerCall11>(taken[11]);
      call(this, recursive, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setRecursive(recursive);
  }

  //  void QSGSoftwareLayer::setFormat(Format a0)
  void setFormat(QSGLayer::Format a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall12 call = reinterpret_cast<CuteQSGSoftwareLayerCall12>(taken[12]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setFormat(a0);
  }

  //  void QSGSoftwareLayer::setHasMipmaps(bool a0)
  void setHasMipmaps(bool a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall13 call = reinterpret_cast<CuteQSGSoftwareLayerCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setHasMipmaps(a0);
  }

  //  void QSGSoftwareLayer::setDevicePixelRatio(qreal ratio)
  void setDevicePixelRatio(qreal ratio) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall14 call = reinterpret_cast<CuteQSGSoftwareLayerCall14>(taken[14]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setDevicePixelRatio(ratio);
  }

  //  void QSGSoftwareLayer::setMirrorHorizontal(bool mirror)
  void setMirrorHorizontal(bool mirror) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall15 call = reinterpret_cast<CuteQSGSoftwareLayerCall15>(taken[15]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setMirrorHorizontal(mirror);
  }

  //  void QSGSoftwareLayer::setMirrorVertical(bool mirror)
  void setMirrorVertical(bool mirror) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall16 call = reinterpret_cast<CuteQSGSoftwareLayerCall16>(taken[16]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setMirrorVertical(mirror);
  }

  //  void QSGSoftwareLayer::setSamples(int a0)
  void setSamples(int a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall17 call = reinterpret_cast<CuteQSGSoftwareLayerCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::setSamples(a0);
  }

  //  void QSGSoftwareLayer::markDirtyTexture()
  void markDirtyTexture() override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall18 call = reinterpret_cast<CuteQSGSoftwareLayerCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::markDirtyTexture();
  }

  //  void QSGSoftwareLayer::invalidated()
  void invalidated() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall19 call = reinterpret_cast<CuteQSGSoftwareLayerCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QSGSoftwareLayer::invalidated();
  }

  //  QRhiTexture *QSGTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall20 call = reinterpret_cast<CuteQSGSoftwareLayerCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGTexture::rhiTexture();
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall21 call = reinterpret_cast<CuteQSGSoftwareLayerCall21>(taken[21]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall22 call = reinterpret_cast<CuteQSGSoftwareLayerCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexture::isAtlasTexture();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall23 call = reinterpret_cast<CuteQSGSoftwareLayerCall23>(taken[23]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGTexture::removedFromAtlas(resourceUpdates);
  }

  //  void QSGTexture::commitTextureOperations(QRhi *rhi,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall24 call = reinterpret_cast<CuteQSGSoftwareLayerCall24>(taken[24]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGTexture::commitTextureOperations(rhi, resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall25 call = reinterpret_cast<CuteQSGSoftwareLayerCall25>(taken[25]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall26 call = reinterpret_cast<CuteQSGSoftwareLayerCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall27 call = reinterpret_cast<CuteQSGSoftwareLayerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall28 call = reinterpret_cast<CuteQSGSoftwareLayerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall29 call = reinterpret_cast<CuteQSGSoftwareLayerCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall30 call = reinterpret_cast<CuteQSGSoftwareLayerCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSGSoftwareLayerCall31 call = reinterpret_cast<CuteQSGSoftwareLayerCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGSoftwareLayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSGSoftwareLayer10metaObjectEv(
    const QSGSoftwareLayer *self) {
  return self->metaObject();
}

//  void *QSGSoftwareLayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSGSoftwareLayer11qt_metacastEPKc(
    QSGSoftwareLayer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwareLayer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSGSoftwareLayer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwareLayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSGSoftwareLayer::~QSGSoftwareLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayerD1Ev(QSGSoftwareLayer *self) {
  delete self;
}

//  const QPixmap &QSGSoftwareLayer::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK16QSGSoftwareLayer6pixmapEv(
    const QSGSoftwareLayer *self) {
  return new QPixmap(self->pixmap());
}

//  qint64 QSGSoftwareLayer::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QSGSoftwareLayer13comparisonKeyEv(
    const QSGSoftwareLayer *self) {
  return self->comparisonKey();
}

//  QSize QSGSoftwareLayer::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QSGSoftwareLayer11textureSizeEv(
    const QSGSoftwareLayer *self) {
  return new QSize(self->textureSize());
}

//  bool QSGSoftwareLayer::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGSoftwareLayer15hasAlphaChannelEv(
    const QSGSoftwareLayer *self) {
  return self->hasAlphaChannel();
}

//  bool QSGSoftwareLayer::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGSoftwareLayer10hasMipmapsEv(
    const QSGSoftwareLayer *self) {
  return self->hasMipmaps();
}

//  bool QSGSoftwareLayer::updateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGSoftwareLayer13updateTextureEv(QSGSoftwareLayer *self) {
  return self->updateTexture();
}

//  void QSGSoftwareLayer::setItem(QSGNode *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer7setItemEP7QSGNode(
    QSGSoftwareLayer *self,
    QSGNode *item) {
  self->setItem(item);
}

//  void QSGSoftwareLayer::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer7setRectERK6QRectF(
    QSGSoftwareLayer *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGSoftwareLayer::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer7setSizeERK5QSize(
    QSGSoftwareLayer *self,
    const QSize *size) {
  self->setSize(*size);
}

//  void QSGSoftwareLayer::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer14scheduleUpdateEv(QSGSoftwareLayer *self) {
  self->scheduleUpdate();
}

//  QImage QSGSoftwareLayer::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK16QSGSoftwareLayer7toImageEv(
    const QSGSoftwareLayer *self) {
  return new QImage(self->toImage());
}

//  void QSGSoftwareLayer::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer7setLiveEb(
    QSGSoftwareLayer *self,
    bool live) {
  self->setLive(live);
}

//  void QSGSoftwareLayer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer12setRecursiveEb(
    QSGSoftwareLayer *self,
    bool recursive) {
  self->setRecursive(recursive);
}

//  void QSGSoftwareLayer::setFormat(Format a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer9setFormatEN8QSGLayer6FormatE(
    QSGSoftwareLayer *self,
    QSGLayer::Format a0) {
  self->setFormat(a0);
}

//  void QSGSoftwareLayer::setHasMipmaps(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer13setHasMipmapsEb(
    QSGSoftwareLayer *self,
    bool a0) {
  self->setHasMipmaps(a0);
}

//  void QSGSoftwareLayer::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer19setDevicePixelRatioEd(
    QSGSoftwareLayer *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  void QSGSoftwareLayer::setMirrorHorizontal(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer19setMirrorHorizontalEb(
    QSGSoftwareLayer *self,
    bool mirror) {
  self->setMirrorHorizontal(mirror);
}

//  void QSGSoftwareLayer::setMirrorVertical(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer17setMirrorVerticalEb(
    QSGSoftwareLayer *self,
    bool mirror) {
  self->setMirrorVertical(mirror);
}

//  void QSGSoftwareLayer::setSamples(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer10setSamplesEi(
    QSGSoftwareLayer *self,
    int a0) {
  self->setSamples(a0);
}

//  void QSGSoftwareLayer::markDirtyTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer16markDirtyTextureEv(
    QSGSoftwareLayer *self) {
  self->markDirtyTexture();
}

//  void QSGSoftwareLayer::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGSoftwareLayer11invalidatedEv(QSGSoftwareLayer *self) {
  self->invalidated();
}

//  a Python function taken by a CuteQSGSoftwareLayer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareLayer(
    QSGSoftwareLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareLayer *>(self)->take(key, call);
}

//  qint64 QSGSoftwareLayer::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QSGSoftwareLayer13comparisonKeyEv(
    const QSGSoftwareLayer *self) {
  return self->QSGSoftwareLayer::comparisonKey();
}

//  QSize QSGSoftwareLayer::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK16QSGSoftwareLayer11textureSizeEv(
    const QSGSoftwareLayer *self) {
  return new QSize(self->QSGSoftwareLayer::textureSize());
}

//  bool QSGSoftwareLayer::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QSGSoftwareLayer15hasAlphaChannelEv(
    const QSGSoftwareLayer *self) {
  return self->QSGSoftwareLayer::hasAlphaChannel();
}

//  bool QSGSoftwareLayer::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QSGSoftwareLayer10hasMipmapsEv(
    const QSGSoftwareLayer *self) {
  return self->QSGSoftwareLayer::hasMipmaps();
}

//  void QSGSoftwareLayer::setItem(QSGNode *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer7setItemEP7QSGNode(
    QSGSoftwareLayer *self,
    QSGNode *item) {
  self->QSGSoftwareLayer::setItem(item);
}

//  void QSGSoftwareLayer::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer7setRectERK6QRectF(
    QSGSoftwareLayer *self,
    const QRectF *rect) {
  self->QSGSoftwareLayer::setRect(*rect);
}

//  void QSGSoftwareLayer::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer7setSizeERK5QSize(
    QSGSoftwareLayer *self,
    const QSize *size) {
  self->QSGSoftwareLayer::setSize(*size);
}

//  void QSGSoftwareLayer::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer14scheduleUpdateEv(
    QSGSoftwareLayer *self) {
  self->QSGSoftwareLayer::scheduleUpdate();
}

//  QImage QSGSoftwareLayer::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK16QSGSoftwareLayer7toImageEv(
    const QSGSoftwareLayer *self) {
  return new QImage(self->QSGSoftwareLayer::toImage());
}

//  void QSGSoftwareLayer::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer7setLiveEb(
    QSGSoftwareLayer *self,
    bool live) {
  self->QSGSoftwareLayer::setLive(live);
}

//  void QSGSoftwareLayer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer12setRecursiveEb(
    QSGSoftwareLayer *self,
    bool recursive) {
  self->QSGSoftwareLayer::setRecursive(recursive);
}

//  void QSGSoftwareLayer::setFormat(Format a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer9setFormatEN8QSGLayer6FormatE(
    QSGSoftwareLayer *self,
    QSGLayer::Format a0) {
  self->QSGSoftwareLayer::setFormat(a0);
}

//  void QSGSoftwareLayer::setHasMipmaps(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer13setHasMipmapsEb(
    QSGSoftwareLayer *self,
    bool a0) {
  self->QSGSoftwareLayer::setHasMipmaps(a0);
}

//  void QSGSoftwareLayer::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer19setDevicePixelRatioEd(
    QSGSoftwareLayer *self,
    qreal ratio) {
  self->QSGSoftwareLayer::setDevicePixelRatio(ratio);
}

//  void QSGSoftwareLayer::setMirrorHorizontal(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer19setMirrorHorizontalEb(
    QSGSoftwareLayer *self,
    bool mirror) {
  self->QSGSoftwareLayer::setMirrorHorizontal(mirror);
}

//  void QSGSoftwareLayer::setMirrorVertical(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer17setMirrorVerticalEb(
    QSGSoftwareLayer *self,
    bool mirror) {
  self->QSGSoftwareLayer::setMirrorVertical(mirror);
}

//  void QSGSoftwareLayer::setSamples(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer10setSamplesEi(
    QSGSoftwareLayer *self,
    int a0) {
  self->QSGSoftwareLayer::setSamples(a0);
}

//  void QSGSoftwareLayer::markDirtyTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer16markDirtyTextureEv(
    QSGSoftwareLayer *self) {
  self->QSGSoftwareLayer::markDirtyTexture();
}

//  void QSGSoftwareLayer::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGSoftwareLayer11invalidatedEv(QSGSoftwareLayer *self) {
  self->QSGSoftwareLayer::invalidated();
}
