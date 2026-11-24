//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickimage_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtGui/qcolorspace.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickImage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickImage : QQuickImage {
  using QQuickImage::pixmapChange;
  using QQuickImage::releaseResources;
  using QQuickImage::geometryChange;
  using QQuickImage::updatePaintNode;
};

//  A QQuickImage that Python can take functions over in. Every QQuickImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQQuickImageCall0)(const void *, int *);
typedef bool (*CuteQQuickImageCall1)(const void *, int *);
typedef void * (*CuteQQuickImageCall2)(const void *, int *);
typedef void (*CuteQQuickImageCall3)(const void *, int *);
typedef void (*CuteQQuickImageCall4)(const void *, int *);
typedef void (*CuteQQuickImageCall5)(const void *, int *);
typedef void (*CuteQQuickImageCall6)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteQQuickImageCall7)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickImageCall8)(const void *, const QUrl *, int *);
typedef void (*CuteQQuickImageCall9)(const void *, const QSize *, int *);
typedef void (*CuteQQuickImageCall10)(const void *, bool, int *);
typedef void (*CuteQQuickImageCall11)(const void *, bool, int *);
typedef void (*CuteQQuickImageCall12)(const void *, int, int *);
typedef int (*CuteQQuickImageCall13)(const void *, int *);
typedef int (*CuteQQuickImageCall14)(const void *, int *);
typedef void (*CuteQQuickImageCall15)(const void *, bool, int *);
typedef void (*CuteQQuickImageCall16)(const void *, const QColorSpace *, int *);
typedef void (*CuteQQuickImageCall17)(const void *, int *);
typedef void (*CuteQQuickImageCall18)(const void *, int *);
typedef void (*CuteQQuickImageCall19)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickImageCall20)(const void *, int *);
typedef const QRectF * (*CuteQQuickImageCall21)(const void *, int *);
typedef bool (*CuteQQuickImageCall22)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickImageCall23)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCall25)(const void *, int *);
typedef void (*CuteQQuickImageCall26)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickImageCall27)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickImageCall28)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickImageCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickImageCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickImageCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageCall34)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageCall35)(const void *, int *);
typedef void (*CuteQQuickImageCall36)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickImageCall37)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickImageCall38)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickImageCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickImageCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickImageCall41)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickImageCall46)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickImageCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImage : public QQuickImage {
public:
  using QQuickImage::QQuickImage;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase12pixmapChangeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setSourceERK4QUrl")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setSourceSizeERK5QSize")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setMirrorEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase19setMirrorVerticallyEb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase15setCurrentFrameEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickImageBase12currentFrameEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickImageBase10frameCountEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase16setAutoTransformEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase4loadEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  QRectF QQuickImage::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageCall0 call = reinterpret_cast<CuteQQuickImageCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickImage::boundingRect();
  }

  //  bool QQuickImage::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageCall1 call = reinterpret_cast<CuteQQuickImageCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImage::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickImage::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageCall2 call = reinterpret_cast<CuteQQuickImageCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickImage::textureProvider();
  }

  //  void QQuickImage::emitAutoTransformBaseChanged()
  void emitAutoTransformBaseChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageCall3 call = reinterpret_cast<CuteQQuickImageCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImage::emitAutoTransformBaseChanged();
  }

  //  void QQuickImage::pixmapChange()
  void pixmapChange() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageCall4 call = reinterpret_cast<CuteQQuickImageCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImage::pixmapChange();
  }

  //  void QQuickImage::releaseResources()
  void releaseResources() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageCall5 call = reinterpret_cast<CuteQQuickImageCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageCall6 call = reinterpret_cast<CuteQQuickImageCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImageCall7 call = reinterpret_cast<CuteQQuickImageCall7>(taken[7]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickImage::updatePaintNode(a0, a1);
  }

  //  void QQuickImageBase::setSource(const QUrl &url)
  void setSource(const QUrl &url) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImageCall8 call = reinterpret_cast<CuteQQuickImageCall8>(taken[8]);
      call(this, &url, &handled);
      if (handled) return;
    }
    QQuickImageBase::setSource(url);
  }

  //  void QQuickImageBase::setSourceSize(const QSize &a0)
  void setSourceSize(const QSize &a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImageCall9 call = reinterpret_cast<CuteQQuickImageCall9>(taken[9]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickImageBase::setSourceSize(a0);
  }

  //  void QQuickImageBase::setMirror(bool mirror)
  void setMirror(bool mirror) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickImageCall10 call = reinterpret_cast<CuteQQuickImageCall10>(taken[10]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirror(mirror);
  }

  //  void QQuickImageBase::setMirrorVertically(bool mirror)
  void setMirrorVertically(bool mirror) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickImageCall11 call = reinterpret_cast<CuteQQuickImageCall11>(taken[11]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirrorVertically(mirror);
  }

  //  void QQuickImageBase::setCurrentFrame(int frame)
  void setCurrentFrame(int frame) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickImageCall12 call = reinterpret_cast<CuteQQuickImageCall12>(taken[12]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QQuickImageBase::setCurrentFrame(frame);
  }

  //  int QQuickImageBase::currentFrame() const
  int currentFrame() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickImageCall13 call = reinterpret_cast<CuteQQuickImageCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImageBase::currentFrame();
  }

  //  int QQuickImageBase::frameCount() const
  int frameCount() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickImageCall14 call = reinterpret_cast<CuteQQuickImageCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImageBase::frameCount();
  }

  //  void QQuickImageBase::setAutoTransform(bool transform)
  void setAutoTransform(bool transform) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickImageCall15 call = reinterpret_cast<CuteQQuickImageCall15>(taken[15]);
      call(this, transform, &handled);
      if (handled) return;
    }
    QQuickImageBase::setAutoTransform(transform);
  }

  //  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
  void setColorSpace(const QColorSpace &colorSpace) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickImageCall16 call = reinterpret_cast<CuteQQuickImageCall16>(taken[16]);
      call(this, &colorSpace, &handled);
      if (handled) return;
    }
    QQuickImageBase::setColorSpace(colorSpace);
  }

  //  void QQuickImageBase::load()
  void load() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickImageCall17 call = reinterpret_cast<CuteQQuickImageCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::load();
  }

  //  void QQuickImageBase::componentComplete()
  void componentComplete() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickImageCall18 call = reinterpret_cast<CuteQQuickImageCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::componentComplete();
  }

  //  void QQuickImageBase::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickImageCall19 call = reinterpret_cast<CuteQQuickImageCall19>(taken[19]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickImageBase::itemChange(change, value);
  }

  //  void QQuickImageBase::requestFinished()
  void requestFinished() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickImageCall20 call = reinterpret_cast<CuteQQuickImageCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::requestFinished();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickImageCall21 call = reinterpret_cast<CuteQQuickImageCall21>(taken[21]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickImageCall22 call = reinterpret_cast<CuteQQuickImageCall22>(taken[22]);
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
      CuteQQuickImageCall23 call = reinterpret_cast<CuteQQuickImageCall23>(taken[23]);
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
      CuteQQuickImageCall24 call = reinterpret_cast<CuteQQuickImageCall24>(taken[24]);
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
      CuteQQuickImageCall25 call = reinterpret_cast<CuteQQuickImageCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickImageCall26 call = reinterpret_cast<CuteQQuickImageCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickImageCall27 call = reinterpret_cast<CuteQQuickImageCall27>(taken[27]);
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
      CuteQQuickImageCall28 call = reinterpret_cast<CuteQQuickImageCall28>(taken[28]);
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
      CuteQQuickImageCall29 call = reinterpret_cast<CuteQQuickImageCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickImageCall30 call = reinterpret_cast<CuteQQuickImageCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickImageCall31 call = reinterpret_cast<CuteQQuickImageCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickImageCall32 call = reinterpret_cast<CuteQQuickImageCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickImageCall33 call = reinterpret_cast<CuteQQuickImageCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickImageCall34 call = reinterpret_cast<CuteQQuickImageCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickImageCall35 call = reinterpret_cast<CuteQQuickImageCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickImageCall36 call = reinterpret_cast<CuteQQuickImageCall36>(taken[36]);
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
      CuteQQuickImageCall37 call = reinterpret_cast<CuteQQuickImageCall37>(taken[37]);
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
      CuteQQuickImageCall38 call = reinterpret_cast<CuteQQuickImageCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickImageCall39 call = reinterpret_cast<CuteQQuickImageCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickImageCall40 call = reinterpret_cast<CuteQQuickImageCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickImageCall41 call = reinterpret_cast<CuteQQuickImageCall41>(taken[41]);
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
      CuteQQuickImageCall42 call = reinterpret_cast<CuteQQuickImageCall42>(taken[42]);
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
      CuteQQuickImageCall43 call = reinterpret_cast<CuteQQuickImageCall43>(taken[43]);
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
      CuteQQuickImageCall44 call = reinterpret_cast<CuteQQuickImageCall44>(taken[44]);
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
      CuteQQuickImageCall45 call = reinterpret_cast<CuteQQuickImageCall45>(taken[45]);
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
      CuteQQuickImageCall46 call = reinterpret_cast<CuteQQuickImageCall46>(taken[46]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickImageCall47 call = reinterpret_cast<CuteQQuickImageCall47>(taken[47]);
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
      CuteQQuickImageCall48 call = reinterpret_cast<CuteQQuickImageCall48>(taken[48]);
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
      CuteQQuickImageCall49 call = reinterpret_cast<CuteQQuickImageCall49>(taken[49]);
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
      CuteQQuickImageCall50 call = reinterpret_cast<CuteQQuickImageCall50>(taken[50]);
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
      CuteQQuickImageCall51 call = reinterpret_cast<CuteQQuickImageCall51>(taken[51]);
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
      CuteQQuickImageCall52 call = reinterpret_cast<CuteQQuickImageCall52>(taken[52]);
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
      CuteQQuickImageCall53 call = reinterpret_cast<CuteQQuickImageCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickImage10metaObjectEv(
    const QQuickImage *self) {
  return self->metaObject();
}

//  QString QQuickImage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickImage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImage::tr(s, c, n));
}

//  QQuickImage::QQuickImage(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickImage *ritual_ZN11QQuickImageC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickImage(parent);
}

//  QQuickImage::~QQuickImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImageD1Ev(QQuickImage *self) {
  delete self;
}

//  FillMode QQuickImage::fillMode() const
extern "C" Q_DECL_EXPORT
QQuickImage::FillMode ritual_ZNK11QQuickImage8fillModeEv(
    const QQuickImage *self) {
  return self->fillMode();
}

//  void QQuickImage::setFillMode(FillMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage11setFillModeENS_8FillModeE(
    QQuickImage *self,
    QQuickImage::FillMode a0) {
  self->setFillMode(a0);
}

//  qreal QQuickImage::paintedWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickImage12paintedWidthEv(const QQuickImage *self) {
  return self->paintedWidth();
}

//  qreal QQuickImage::paintedHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickImage13paintedHeightEv(const QQuickImage *self) {
  return self->paintedHeight();
}

//  QRectF QQuickImage::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QQuickImage12boundingRectEv(const QQuickImage *self) {
  return new QRectF(self->boundingRect());
}

//  HAlignment QQuickImage::horizontalAlignment() const
extern "C" Q_DECL_EXPORT
QQuickImage::HAlignment ritual_ZNK11QQuickImage19horizontalAlignmentEv(
    const QQuickImage *self) {
  return self->horizontalAlignment();
}

//  void QQuickImage::setHorizontalAlignment(HAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage22setHorizontalAlignmentENS_10HAlignmentE(
    QQuickImage *self,
    QQuickImage::HAlignment align) {
  self->setHorizontalAlignment(align);
}

//  VAlignment QQuickImage::verticalAlignment() const
extern "C" Q_DECL_EXPORT
QQuickImage::VAlignment ritual_ZNK11QQuickImage17verticalAlignmentEv(
    const QQuickImage *self) {
  return self->verticalAlignment();
}

//  void QQuickImage::setVerticalAlignment(VAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage20setVerticalAlignmentENS_10VAlignmentE(
    QQuickImage *self,
    QQuickImage::VAlignment align) {
  self->setVerticalAlignment(align);
}

//  bool QQuickImage::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickImage17isTextureProviderEv(const QQuickImage *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuickImage::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK11QQuickImage15textureProviderEv(
    const QQuickImage *self) {
  return self->textureProvider();
}

//  bool QQuickImage::mipmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickImage6mipmapEv(const QQuickImage *self) {
  return self->mipmap();
}

//  void QQuickImage::setMipmap(bool use)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage9setMipmapEb(QQuickImage *self, bool use) {
  self->setMipmap(use);
}

//  void QQuickImage::emitAutoTransformBaseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage28emitAutoTransformBaseChangedEv(
    QQuickImage *self) {
  self->emitAutoTransformBaseChanged();
}

//  void QQuickImage::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage20invalidateSceneGraphEv(QQuickImage *self) {
  self->invalidateSceneGraph();
}

//  void QQuickImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage12pixmapChangeEv(QQuickImage *self) {
  self->pixmapChange();
}

//  void QQuickImage::updatePaintedGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage21updatePaintedGeometryEv(QQuickImage *self) {
  self->updatePaintedGeometry();
}

//  void QQuickImage::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage16releaseResourcesEv(QQuickImage *self) {
  self->releaseResources();
}

//  void QQuickImage::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickImage14geometryChangeERK6QRectFS2_(
    QQuickImage *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *QQuickImage::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN11QQuickImage15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickImage *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  QQuickImagePrivate *QQuickImage::d_func()
extern "C" Q_DECL_EXPORT
QQuickImagePrivate *ritual_ZN11QQuickImage6d_funcEv(QQuickImage *self) {
  return self->d_func();
}

//  const QQuickImagePrivate *QQuickImage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickImagePrivate *ritual_ZNK11QQuickImage6d_funcEv(
    const QQuickImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickImage, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImage(
    QQuickImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImage *>(self)->take(key, call);
}

//  QRectF QQuickImage::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK11QQuickImage12boundingRectEv(
    const QQuickImage *self) {
  return new QRectF(self->QQuickImage::boundingRect());
}

//  bool QQuickImage::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QQuickImage17isTextureProviderEv(
    const QQuickImage *self) {
  return self->QQuickImage::isTextureProvider();
}

//  QSGTextureProvider *QQuickImage::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK11QQuickImage15textureProviderEv(
    const QQuickImage *self) {
  return self->QQuickImage::textureProvider();
}

//  void QQuickImage::emitAutoTransformBaseChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickImage28emitAutoTransformBaseChangedEv(
    QQuickImage *self) {
  self->QQuickImage::emitAutoTransformBaseChanged();
}

//  void QQuickImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickImage12pixmapChangeEv(QQuickImage *self) {
  static_cast<OwnQQuickImage *>(self)->OwnQQuickImage::pixmapChange();
}

//  void QQuickImage::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickImage16releaseResourcesEv(QQuickImage *self) {
  static_cast<OwnQQuickImage *>(self)->OwnQQuickImage::releaseResources();
}

//  void QQuickImage::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickImage14geometryChangeERK6QRectFS2_(
    QQuickImage *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickImage *>(self)->OwnQQuickImage::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QSGNode *QQuickImage::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
//      *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN11QQuickImage15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickImage *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickImage *>(self)->OwnQQuickImage::updatePaintNode(
      a0,
      a1);
}
