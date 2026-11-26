//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qcolorspace.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickAnimatedImage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAnimatedImage : QQuickAnimatedImage {
  using QQuickAnimatedImage::load;
  using QQuickAnimatedImage::componentComplete;
};

//  A QQuickAnimatedImage that Python can take functions over in. Every QQuickAnimatedImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_animatedimage)
typedef int (*CuteQQuickAnimatedImageCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
typedef void (*CuteQQuickAnimatedImageCall1)(const void *, int, int *);
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
typedef int (*CuteQQuickAnimatedImageCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
typedef void (*CuteQQuickAnimatedImageCall3)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
typedef void (*CuteQQuickAnimatedImageCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
typedef void (*CuteQQuickAnimatedImageCall5)(const void *, int *);
#endif  // QT_CONFIG(quick_animatedimage)
typedef const QRectF * (*CuteQQuickAnimatedImageCall6)(const void *, int *);
typedef bool (*CuteQQuickAnimatedImageCall7)(const void *, int *);
typedef void * (*CuteQQuickAnimatedImageCall8)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageCall9)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageCall10)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageCall11)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteQQuickAnimatedImageCall13)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickAnimatedImageCall14)(const void *, const QSize *, int *);
typedef void (*CuteQQuickAnimatedImageCall15)(const void *, bool, int *);
typedef void (*CuteQQuickAnimatedImageCall16)(const void *, bool, int *);
typedef void (*CuteQQuickAnimatedImageCall17)(const void *, bool, int *);
typedef void (*CuteQQuickAnimatedImageCall18)(const void *, const QColorSpace *, int *);
typedef void (*CuteQQuickAnimatedImageCall19)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickAnimatedImageCall20)(const void *, int *);
typedef const QRectF * (*CuteQQuickAnimatedImageCall21)(const void *, int *);
typedef bool (*CuteQQuickAnimatedImageCall22)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickAnimatedImageCall23)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatedImageCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageCall25)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageCall26)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall27)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickAnimatedImageCall28)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickAnimatedImageCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall34)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall35)(const void *, int *);
typedef void (*CuteQQuickAnimatedImageCall36)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickAnimatedImageCall37)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickAnimatedImageCall38)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall41)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAnimatedImageCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAnimatedImageCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAnimatedImageCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAnimatedImageCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickAnimatedImageCall46)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickAnimatedImageCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatedImageCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatedImageCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnimatedImage : public QQuickAnimatedImage {
public:
  using QQuickAnimatedImage::QQuickAnimatedImage;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZNK15QQuickImageBase12currentFrameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZN15QQuickImageBase15setCurrentFrameEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZNK15QQuickImageBase10frameCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setSourceERK4QUrl")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZN15QQuickImageBase4loadEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_animatedimage)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase12pixmapChangeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setSourceSizeERK5QSize")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setMirrorEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase19setMirrorVerticallyEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase16setAutoTransformEb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase15requestFinishedEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[36] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[41] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[47] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_animatedimage)
  //  int QQuickAnimatedImage::currentFrame() const
  int currentFrame() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall0 call = reinterpret_cast<CuteQQuickAnimatedImageCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnimatedImage::currentFrame();
  }
#endif  // QT_CONFIG(quick_animatedimage)

#if QT_CONFIG(quick_animatedimage)
  //  void QQuickAnimatedImage::setCurrentFrame(int frame)
  void setCurrentFrame(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall1 call = reinterpret_cast<CuteQQuickAnimatedImageCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QQuickAnimatedImage::setCurrentFrame(frame);
  }
#endif  // QT_CONFIG(quick_animatedimage)

#if QT_CONFIG(quick_animatedimage)
  //  int QQuickAnimatedImage::frameCount() const
  int frameCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall2 call = reinterpret_cast<CuteQQuickAnimatedImageCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnimatedImage::frameCount();
  }
#endif  // QT_CONFIG(quick_animatedimage)

#if QT_CONFIG(quick_animatedimage)
  //  void QQuickAnimatedImage::setSource(const QUrl &a0)
  void setSource(const QUrl &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall3 call = reinterpret_cast<CuteQQuickAnimatedImageCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAnimatedImage::setSource(a0);
  }
#endif  // QT_CONFIG(quick_animatedimage)

#if QT_CONFIG(quick_animatedimage)
  //  void QQuickAnimatedImage::load()
  void load() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall4 call = reinterpret_cast<CuteQQuickAnimatedImageCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatedImage::load();
  }
#endif  // QT_CONFIG(quick_animatedimage)

#if QT_CONFIG(quick_animatedimage)
  //  void QQuickAnimatedImage::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall5 call = reinterpret_cast<CuteQQuickAnimatedImageCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatedImage::componentComplete();
  }
#endif  // QT_CONFIG(quick_animatedimage)

  //  QRectF QQuickImage::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall6 call = reinterpret_cast<CuteQQuickAnimatedImageCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickImage::boundingRect();
  }

  //  bool QQuickImage::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall7 call = reinterpret_cast<CuteQQuickAnimatedImageCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImage::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickImage::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall8 call = reinterpret_cast<CuteQQuickAnimatedImageCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickImage::textureProvider();
  }

  //  void QQuickImage::emitAutoTransformBaseChanged()
  void emitAutoTransformBaseChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall9 call = reinterpret_cast<CuteQQuickAnimatedImageCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImage::emitAutoTransformBaseChanged();
  }

  //  void QQuickImage::pixmapChange()
  void pixmapChange() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall10 call = reinterpret_cast<CuteQQuickAnimatedImageCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImage::pixmapChange();
  }

  //  void QQuickImage::releaseResources()
  void releaseResources() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall11 call = reinterpret_cast<CuteQQuickAnimatedImageCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImage::releaseResources();
  }

  //  void QQuickImage::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall12 call = reinterpret_cast<CuteQQuickAnimatedImageCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickImage::geometryChange(newGeometry, oldGeometry);
  }

  //  QSGNode *QQuickImage::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall13 call = reinterpret_cast<CuteQQuickAnimatedImageCall13>(taken[13]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickImage::updatePaintNode(a0, a1);
  }

  //  void QQuickImageBase::setSourceSize(const QSize &a0)
  void setSourceSize(const QSize &a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall14 call = reinterpret_cast<CuteQQuickAnimatedImageCall14>(taken[14]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickImageBase::setSourceSize(a0);
  }

  //  void QQuickImageBase::setMirror(bool mirror)
  void setMirror(bool mirror) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall15 call = reinterpret_cast<CuteQQuickAnimatedImageCall15>(taken[15]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirror(mirror);
  }

  //  void QQuickImageBase::setMirrorVertically(bool mirror)
  void setMirrorVertically(bool mirror) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall16 call = reinterpret_cast<CuteQQuickAnimatedImageCall16>(taken[16]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirrorVertically(mirror);
  }

  //  void QQuickImageBase::setAutoTransform(bool transform)
  void setAutoTransform(bool transform) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall17 call = reinterpret_cast<CuteQQuickAnimatedImageCall17>(taken[17]);
      call(this, transform, &handled);
      if (handled) return;
    }
    QQuickImageBase::setAutoTransform(transform);
  }

  //  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
  void setColorSpace(const QColorSpace &colorSpace) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall18 call = reinterpret_cast<CuteQQuickAnimatedImageCall18>(taken[18]);
      call(this, &colorSpace, &handled);
      if (handled) return;
    }
    QQuickImageBase::setColorSpace(colorSpace);
  }

  //  void QQuickImageBase::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall19 call = reinterpret_cast<CuteQQuickAnimatedImageCall19>(taken[19]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickImageBase::itemChange(change, value);
  }

  //  void QQuickImageBase::requestFinished()
  void requestFinished() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall20 call = reinterpret_cast<CuteQQuickAnimatedImageCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::requestFinished();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall21 call = reinterpret_cast<CuteQQuickAnimatedImageCall21>(taken[21]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall22 call = reinterpret_cast<CuteQQuickAnimatedImageCall22>(taken[22]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall23 call = reinterpret_cast<CuteQQuickAnimatedImageCall23>(taken[23]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall24 call = reinterpret_cast<CuteQQuickAnimatedImageCall24>(taken[24]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall25 call = reinterpret_cast<CuteQQuickAnimatedImageCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall26 call = reinterpret_cast<CuteQQuickAnimatedImageCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall27 call = reinterpret_cast<CuteQQuickAnimatedImageCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall28 call = reinterpret_cast<CuteQQuickAnimatedImageCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall29 call = reinterpret_cast<CuteQQuickAnimatedImageCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall30 call = reinterpret_cast<CuteQQuickAnimatedImageCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall31 call = reinterpret_cast<CuteQQuickAnimatedImageCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall32 call = reinterpret_cast<CuteQQuickAnimatedImageCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall33 call = reinterpret_cast<CuteQQuickAnimatedImageCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall34 call = reinterpret_cast<CuteQQuickAnimatedImageCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall35 call = reinterpret_cast<CuteQQuickAnimatedImageCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall36 call = reinterpret_cast<CuteQQuickAnimatedImageCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall37 call = reinterpret_cast<CuteQQuickAnimatedImageCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall38 call = reinterpret_cast<CuteQQuickAnimatedImageCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall39 call = reinterpret_cast<CuteQQuickAnimatedImageCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall40 call = reinterpret_cast<CuteQQuickAnimatedImageCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall41 call = reinterpret_cast<CuteQQuickAnimatedImageCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall42 call = reinterpret_cast<CuteQQuickAnimatedImageCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall43 call = reinterpret_cast<CuteQQuickAnimatedImageCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall44 call = reinterpret_cast<CuteQQuickAnimatedImageCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall45 call = reinterpret_cast<CuteQQuickAnimatedImageCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall46 call = reinterpret_cast<CuteQQuickAnimatedImageCall46>(taken[46]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall47 call = reinterpret_cast<CuteQQuickAnimatedImageCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall48 call = reinterpret_cast<CuteQQuickAnimatedImageCall48>(taken[48]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall49 call = reinterpret_cast<CuteQQuickAnimatedImageCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall50 call = reinterpret_cast<CuteQQuickAnimatedImageCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall51 call = reinterpret_cast<CuteQQuickAnimatedImageCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall52 call = reinterpret_cast<CuteQQuickAnimatedImageCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickAnimatedImageCall53 call = reinterpret_cast<CuteQQuickAnimatedImageCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnimatedImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickAnimatedImage10metaObjectEv(
    const QQuickAnimatedImage *self) {
  return self->metaObject();
}

//  void *QQuickAnimatedImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickAnimatedImage11qt_metacastEPKc(
    QQuickAnimatedImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAnimatedImage::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickAnimatedImage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAnimatedImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAnimatedImage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickAnimatedImage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnimatedImage::tr(s, c, n));
}

//  QQuickAnimatedImage::QQuickAnimatedImage(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickAnimatedImage *ritual_ZN19QQuickAnimatedImageC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickAnimatedImage(parent);
}

//  QQuickAnimatedImage::~QQuickAnimatedImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImageD1Ev(QQuickAnimatedImage *self) {
  delete self;
}

//  bool QQuickAnimatedImage::isPlaying() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickAnimatedImage9isPlayingEv(
    const QQuickAnimatedImage *self) {
  return self->isPlaying();
}

//  void QQuickAnimatedImage::setPlaying(bool play)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage10setPlayingEb(
    QQuickAnimatedImage *self,
    bool play) {
  self->setPlaying(play);
}

//  bool QQuickAnimatedImage::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickAnimatedImage8isPausedEv(
    const QQuickAnimatedImage *self) {
  return self->isPaused();
}

//  void QQuickAnimatedImage::setPaused(bool pause)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage9setPausedEb(
    QQuickAnimatedImage *self,
    bool pause) {
  self->setPaused(pause);
}

//  int QQuickAnimatedImage::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickAnimatedImage12currentFrameEv(
    const QQuickAnimatedImage *self) {
  return self->currentFrame();
}

//  void QQuickAnimatedImage::setCurrentFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage15setCurrentFrameEi(
    QQuickAnimatedImage *self,
    int frame) {
  self->setCurrentFrame(frame);
}

//  int QQuickAnimatedImage::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickAnimatedImage10frameCountEv(
    const QQuickAnimatedImage *self) {
  return self->frameCount();
}

//  qreal QQuickAnimatedImage::speed() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickAnimatedImage5speedEv(
    const QQuickAnimatedImage *self) {
  return self->speed();
}

//  void QQuickAnimatedImage::setSpeed(qreal speed)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage8setSpeedEd(
    QQuickAnimatedImage *self,
    qreal speed) {
  self->setSpeed(speed);
}

//  void QQuickAnimatedImage::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage9setSourceERK4QUrl(
    QQuickAnimatedImage *self,
    const QUrl *a0) {
  self->setSource(*a0);
}

//  int QQuickAnimatedImage::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickAnimatedImage5loopsEv(
    const QQuickAnimatedImage *self) {
  return self->loops();
}

//  void QQuickAnimatedImage::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage8setLoopsEi(
    QQuickAnimatedImage *self,
    int loops) {
  self->setLoops(loops);
}

//  FinishBehavior QQuickAnimatedImage::finishBehavior() const
extern "C" Q_DECL_EXPORT
QQuickAnimatedImage::FinishBehavior ritual_ZNK19QQuickAnimatedImage14finishBehaviorEv(
    const QQuickAnimatedImage *self) {
  return self->finishBehavior();
}

//  void QQuickAnimatedImage::setFinishBehavior(FinishBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage17setFinishBehaviorENS_14FinishBehaviorE(
    QQuickAnimatedImage *self,
    QQuickAnimatedImage::FinishBehavior behavior) {
  self->setFinishBehavior(behavior);
}

//  void QQuickAnimatedImage::playingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage14playingChangedEv(
    QQuickAnimatedImage *self) {
  self->playingChanged();
}

//  void QQuickAnimatedImage::pausedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage13pausedChangedEv(
    QQuickAnimatedImage *self) {
  self->pausedChanged();
}

//  void QQuickAnimatedImage::frameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage12frameChangedEv(
    QQuickAnimatedImage *self) {
  self->frameChanged();
}

//  void QQuickAnimatedImage::currentFrameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage19currentFrameChangedEv(
    QQuickAnimatedImage *self) {
  self->currentFrameChanged();
}

//  void QQuickAnimatedImage::frameCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage17frameCountChangedEv(
    QQuickAnimatedImage *self) {
  self->frameCountChanged();
}

//  void QQuickAnimatedImage::speedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage12speedChangedEv(
    QQuickAnimatedImage *self) {
  self->speedChanged();
}

//  void QQuickAnimatedImage::loopsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage12loopsChangedEv(
    QQuickAnimatedImage *self) {
  self->loopsChanged();
}

//  void QQuickAnimatedImage::finishBehaviorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage21finishBehaviorChangedEv(
    QQuickAnimatedImage *self) {
  self->finishBehaviorChanged();
}

//  void QQuickAnimatedImage::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage8finishedEv(QQuickAnimatedImage *self) {
  self->finished();
}

//  void QQuickAnimatedImage::movieUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage11movieUpdateEv(
    QQuickAnimatedImage *self) {
  self->movieUpdate();
}

//  void QQuickAnimatedImage::movieRequestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage20movieRequestFinishedEv(
    QQuickAnimatedImage *self) {
  self->movieRequestFinished();
}

//  void QQuickAnimatedImage::playingStatusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage20playingStatusChangedEv(
    QQuickAnimatedImage *self) {
  self->playingStatusChanged();
}

//  void QQuickAnimatedImage::onCacheChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage14onCacheChangedEv(
    QQuickAnimatedImage *self) {
  self->onCacheChanged();
}

//  void QQuickAnimatedImage::onMovieFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage15onMovieFinishedEv(
    QQuickAnimatedImage *self) {
  self->onMovieFinished();
}

//  void QQuickAnimatedImage::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage4loadEv(QQuickAnimatedImage *self) {
  self->load();
}

//  void QQuickAnimatedImage::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnimatedImage17componentCompleteEv(
    QQuickAnimatedImage *self) {
  self->componentComplete();
}

//  QQuickAnimatedImagePrivate *QQuickAnimatedImage::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnimatedImagePrivate *ritual_ZN19QQuickAnimatedImage6d_funcEv(
    QQuickAnimatedImage *self) {
  return self->d_func();
}

//  const QQuickAnimatedImagePrivate *QQuickAnimatedImage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnimatedImagePrivate *ritual_ZNK19QQuickAnimatedImage6d_funcEv(
    const QQuickAnimatedImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickAnimatedImage, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatedImage(
    QQuickAnimatedImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatedImage *>(self)->take(key, call);
}

//  int QQuickAnimatedImage::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QQuickAnimatedImage12currentFrameEv(
    const QQuickAnimatedImage *self) {
  return self->QQuickAnimatedImage::currentFrame();
}

//  void QQuickAnimatedImage::setCurrentFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnimatedImage15setCurrentFrameEi(
    QQuickAnimatedImage *self,
    int frame) {
  self->QQuickAnimatedImage::setCurrentFrame(frame);
}

//  int QQuickAnimatedImage::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QQuickAnimatedImage10frameCountEv(
    const QQuickAnimatedImage *self) {
  return self->QQuickAnimatedImage::frameCount();
}

//  void QQuickAnimatedImage::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnimatedImage9setSourceERK4QUrl(
    QQuickAnimatedImage *self,
    const QUrl *a0) {
  self->QQuickAnimatedImage::setSource(*a0);
}

//  void QQuickAnimatedImage::load()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnimatedImage4loadEv(QQuickAnimatedImage *self) {
  static_cast<OwnQQuickAnimatedImage *>(self)->OwnQQuickAnimatedImage::load();
}

//  void QQuickAnimatedImage::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnimatedImage17componentCompleteEv(
    QQuickAnimatedImage *self) {
  static_cast<OwnQQuickAnimatedImage *>(self)->OwnQQuickAnimatedImage::componentComplete();
}

#endif  // QT_CONFIG(quick_animatedimage)
#endif  // QT_CONFIG(quick_animatedimage)
