//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickborderimage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickborderimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qcolorspace.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickBorderImage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickBorderImage : QQuickBorderImage {
  using QQuickBorderImage::load;
  using QQuickBorderImage::pixmapChange;
  using QQuickBorderImage::updatePaintNode;
};

//  A QQuickBorderImage that Python can take functions over in. Every QQuickBorderImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickBorderImageCall0)(const void *, const QUrl *, int *);
typedef void (*CuteQQuickBorderImageCall1)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall2)(const void *, int *);
typedef void * (*CuteQQuickBorderImageCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickBorderImageCall4)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall5)(const void *, const QSize *, int *);
typedef void (*CuteQQuickBorderImageCall6)(const void *, bool, int *);
typedef void (*CuteQQuickBorderImageCall7)(const void *, bool, int *);
typedef void (*CuteQQuickBorderImageCall8)(const void *, int, int *);
typedef int (*CuteQQuickBorderImageCall9)(const void *, int *);
typedef int (*CuteQQuickBorderImageCall10)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall11)(const void *, bool, int *);
typedef void (*CuteQQuickBorderImageCall12)(const void *, const QColorSpace *, int *);
typedef void (*CuteQQuickBorderImageCall13)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall14)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall15)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickBorderImageCall16)(const void *, int *);
typedef const QRectF * (*CuteQQuickBorderImageCall17)(const void *, int *);
typedef bool (*CuteQQuickBorderImageCall18)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickBorderImageCall19)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickBorderImageCall20)(const void *, int *);
typedef void * (*CuteQQuickBorderImageCall21)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBorderImageCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBorderImageCall23)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickBorderImageCall24)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickBorderImageCall26)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickBorderImageCall27)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickBorderImageCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickBorderImageCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickBorderImageCall30)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBorderImageCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBorderImageCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBorderImageCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBorderImageCall34)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall35)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickBorderImageCall36)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickBorderImageCall37)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickBorderImageCall38)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickBorderImageCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickBorderImageCall40)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBorderImageCall41)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBorderImageCall42)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBorderImageCall43)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBorderImageCall44)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickBorderImageCall45)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickBorderImageCall46)(const void *, int *);
typedef void (*CuteQQuickBorderImageCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBorderImageCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBorderImageCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBorderImageCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBorderImageCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBorderImageCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBorderImageCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickBorderImage : public QQuickBorderImage {
public:
  using QQuickBorderImage::QQuickBorderImage;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setSourceERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase4loadEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase12pixmapChangeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase15requestFinishedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setSourceSizeERK5QSize")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setMirrorEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase19setMirrorVerticallyEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase15setCurrentFrameEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickImageBase12currentFrameEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickImageBase10frameCountEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase16setAutoTransformEb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[40] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
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

  //  void QQuickBorderImage::setSource(const QUrl &url)
  void setSource(const QUrl &url) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBorderImageCall0 call = reinterpret_cast<CuteQQuickBorderImageCall0>(taken[0]);
      call(this, &url, &handled);
      if (handled) return;
    }
    QQuickBorderImage::setSource(url);
  }

  //  void QQuickBorderImage::load()
  void load() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBorderImageCall1 call = reinterpret_cast<CuteQQuickBorderImageCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBorderImage::load();
  }

  //  void QQuickBorderImage::pixmapChange()
  void pixmapChange() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBorderImageCall2 call = reinterpret_cast<CuteQQuickBorderImageCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBorderImage::pixmapChange();
  }

  //  QSGNode *QQuickBorderImage::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBorderImageCall3 call = reinterpret_cast<CuteQQuickBorderImageCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickBorderImage::updatePaintNode(a0, a1);
  }

  //  void QQuickBorderImage::requestFinished()
  void requestFinished() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBorderImageCall4 call = reinterpret_cast<CuteQQuickBorderImageCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBorderImage::requestFinished();
  }

  //  void QQuickImageBase::setSourceSize(const QSize &a0)
  void setSourceSize(const QSize &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickBorderImageCall5 call = reinterpret_cast<CuteQQuickBorderImageCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickImageBase::setSourceSize(a0);
  }

  //  void QQuickImageBase::setMirror(bool mirror)
  void setMirror(bool mirror) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickBorderImageCall6 call = reinterpret_cast<CuteQQuickBorderImageCall6>(taken[6]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirror(mirror);
  }

  //  void QQuickImageBase::setMirrorVertically(bool mirror)
  void setMirrorVertically(bool mirror) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickBorderImageCall7 call = reinterpret_cast<CuteQQuickBorderImageCall7>(taken[7]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirrorVertically(mirror);
  }

  //  void QQuickImageBase::setCurrentFrame(int frame)
  void setCurrentFrame(int frame) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickBorderImageCall8 call = reinterpret_cast<CuteQQuickBorderImageCall8>(taken[8]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QQuickImageBase::setCurrentFrame(frame);
  }

  //  int QQuickImageBase::currentFrame() const
  int currentFrame() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickBorderImageCall9 call = reinterpret_cast<CuteQQuickBorderImageCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImageBase::currentFrame();
  }

  //  int QQuickImageBase::frameCount() const
  int frameCount() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickBorderImageCall10 call = reinterpret_cast<CuteQQuickBorderImageCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImageBase::frameCount();
  }

  //  void QQuickImageBase::setAutoTransform(bool transform)
  void setAutoTransform(bool transform) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickBorderImageCall11 call = reinterpret_cast<CuteQQuickBorderImageCall11>(taken[11]);
      call(this, transform, &handled);
      if (handled) return;
    }
    QQuickImageBase::setAutoTransform(transform);
  }

  //  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
  void setColorSpace(const QColorSpace &colorSpace) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickBorderImageCall12 call = reinterpret_cast<CuteQQuickBorderImageCall12>(taken[12]);
      call(this, &colorSpace, &handled);
      if (handled) return;
    }
    QQuickImageBase::setColorSpace(colorSpace);
  }

  //  void QQuickImageBase::emitAutoTransformBaseChanged()
  void emitAutoTransformBaseChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickBorderImageCall13 call = reinterpret_cast<CuteQQuickBorderImageCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::emitAutoTransformBaseChanged();
  }

  //  void QQuickImageBase::componentComplete()
  void componentComplete() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickBorderImageCall14 call = reinterpret_cast<CuteQQuickBorderImageCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQQuickBorderImageCall15 call = reinterpret_cast<CuteQQuickBorderImageCall15>(taken[15]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickImageBase::itemChange(change, value);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickBorderImageCall16 call = reinterpret_cast<CuteQQuickBorderImageCall16>(taken[16]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickBorderImageCall17 call = reinterpret_cast<CuteQQuickBorderImageCall17>(taken[17]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickBorderImageCall18 call = reinterpret_cast<CuteQQuickBorderImageCall18>(taken[18]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickBorderImageCall19 call = reinterpret_cast<CuteQQuickBorderImageCall19>(taken[19]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickBorderImageCall20 call = reinterpret_cast<CuteQQuickBorderImageCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickBorderImageCall21 call = reinterpret_cast<CuteQQuickBorderImageCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickBorderImageCall22 call = reinterpret_cast<CuteQQuickBorderImageCall22>(taken[22]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickBorderImageCall23 call = reinterpret_cast<CuteQQuickBorderImageCall23>(taken[23]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickBorderImageCall24 call = reinterpret_cast<CuteQQuickBorderImageCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickBorderImageCall25 call = reinterpret_cast<CuteQQuickBorderImageCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickBorderImageCall26 call = reinterpret_cast<CuteQQuickBorderImageCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickBorderImageCall27 call = reinterpret_cast<CuteQQuickBorderImageCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickBorderImageCall28 call = reinterpret_cast<CuteQQuickBorderImageCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickBorderImageCall29 call = reinterpret_cast<CuteQQuickBorderImageCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickBorderImageCall30 call = reinterpret_cast<CuteQQuickBorderImageCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickBorderImageCall31 call = reinterpret_cast<CuteQQuickBorderImageCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickBorderImageCall32 call = reinterpret_cast<CuteQQuickBorderImageCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickBorderImageCall33 call = reinterpret_cast<CuteQQuickBorderImageCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickBorderImageCall34 call = reinterpret_cast<CuteQQuickBorderImageCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickBorderImageCall35 call = reinterpret_cast<CuteQQuickBorderImageCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickBorderImageCall36 call = reinterpret_cast<CuteQQuickBorderImageCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickBorderImageCall37 call = reinterpret_cast<CuteQQuickBorderImageCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickBorderImageCall38 call = reinterpret_cast<CuteQQuickBorderImageCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickBorderImageCall39 call = reinterpret_cast<CuteQQuickBorderImageCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickBorderImageCall40 call = reinterpret_cast<CuteQQuickBorderImageCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickBorderImageCall41 call = reinterpret_cast<CuteQQuickBorderImageCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickBorderImageCall42 call = reinterpret_cast<CuteQQuickBorderImageCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickBorderImageCall43 call = reinterpret_cast<CuteQQuickBorderImageCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickBorderImageCall44 call = reinterpret_cast<CuteQQuickBorderImageCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickBorderImageCall45 call = reinterpret_cast<CuteQQuickBorderImageCall45>(taken[45]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickBorderImageCall46 call = reinterpret_cast<CuteQQuickBorderImageCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickBorderImageCall47 call = reinterpret_cast<CuteQQuickBorderImageCall47>(taken[47]);
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
      CuteQQuickBorderImageCall48 call = reinterpret_cast<CuteQQuickBorderImageCall48>(taken[48]);
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
      CuteQQuickBorderImageCall49 call = reinterpret_cast<CuteQQuickBorderImageCall49>(taken[49]);
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
      CuteQQuickBorderImageCall50 call = reinterpret_cast<CuteQQuickBorderImageCall50>(taken[50]);
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
      CuteQQuickBorderImageCall51 call = reinterpret_cast<CuteQQuickBorderImageCall51>(taken[51]);
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
      CuteQQuickBorderImageCall52 call = reinterpret_cast<CuteQQuickBorderImageCall52>(taken[52]);
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
      CuteQQuickBorderImageCall53 call = reinterpret_cast<CuteQQuickBorderImageCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickBorderImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickBorderImage10metaObjectEv(
    const QQuickBorderImage *self) {
  return self->metaObject();
}

//  void *QQuickBorderImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickBorderImage11qt_metacastEPKc(
    QQuickBorderImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBorderImage::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickBorderImage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBorderImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBorderImage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickBorderImage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBorderImage::tr(s, c, n));
}

//  QQuickBorderImage::QQuickBorderImage(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickBorderImage *ritual_ZN17QQuickBorderImageC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickBorderImage(parent);
}

//  QQuickBorderImage::~QQuickBorderImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImageD1Ev(QQuickBorderImage *self) {
  delete self;
}

//  QQuickScaleGrid *QQuickBorderImage::border()
extern "C" Q_DECL_EXPORT
QQuickScaleGrid *ritual_ZN17QQuickBorderImage6borderEv(
    QQuickBorderImage *self) {
  return self->border();
}

//  TileMode QQuickBorderImage::horizontalTileMode() const
extern "C" Q_DECL_EXPORT
QQuickBorderImage::TileMode ritual_ZNK17QQuickBorderImage18horizontalTileModeEv(
    const QQuickBorderImage *self) {
  return self->horizontalTileMode();
}

//  void QQuickBorderImage::setHorizontalTileMode(TileMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage21setHorizontalTileModeENS_8TileModeE(
    QQuickBorderImage *self,
    QQuickBorderImage::TileMode a0) {
  self->setHorizontalTileMode(a0);
}

//  TileMode QQuickBorderImage::verticalTileMode() const
extern "C" Q_DECL_EXPORT
QQuickBorderImage::TileMode ritual_ZNK17QQuickBorderImage16verticalTileModeEv(
    const QQuickBorderImage *self) {
  return self->verticalTileMode();
}

//  void QQuickBorderImage::setVerticalTileMode(TileMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage19setVerticalTileModeENS_8TileModeE(
    QQuickBorderImage *self,
    QQuickBorderImage::TileMode a0) {
  self->setVerticalTileMode(a0);
}

//  void QQuickBorderImage::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage9setSourceERK4QUrl(
    QQuickBorderImage *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  void QQuickBorderImage::horizontalTileModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage25horizontalTileModeChangedEv(
    QQuickBorderImage *self) {
  self->horizontalTileModeChanged();
}

//  void QQuickBorderImage::verticalTileModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage23verticalTileModeChangedEv(
    QQuickBorderImage *self) {
  self->verticalTileModeChanged();
}

//  void QQuickBorderImage::sourceSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage17sourceSizeChangedEv(
    QQuickBorderImage *self) {
  self->sourceSizeChanged();
}

//  void QQuickBorderImage::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage4loadEv(QQuickBorderImage *self) {
  self->load();
}

//  void QQuickBorderImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage12pixmapChangeEv(QQuickBorderImage *self) {
  self->pixmapChange();
}

//  QSGNode *QQuickBorderImage::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN17QQuickBorderImage15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickBorderImage *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickBorderImage::setGridScaledImage(const QQuickGridScaledImage
//      &sci)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage18setGridScaledImageERK21QQuickGridScaledImage(
    QQuickBorderImage *self,
    const QQuickGridScaledImage *sci) {
  self->setGridScaledImage(*sci);
}

//  void QQuickBorderImage::doUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage8doUpdateEv(QQuickBorderImage *self) {
  self->doUpdate();
}

//  void QQuickBorderImage::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage15requestFinishedEv(
    QQuickBorderImage *self) {
  self->requestFinished();
}

#if QT_CONFIG(qml_network)
//  void QQuickBorderImage::sciRequestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickBorderImage18sciRequestFinishedEv(
    QQuickBorderImage *self) {
  self->sciRequestFinished();
}
#endif  // QT_CONFIG(qml_network)

//  QQuickBorderImagePrivate *QQuickBorderImage::d_func()
extern "C" Q_DECL_EXPORT
QQuickBorderImagePrivate *ritual_ZN17QQuickBorderImage6d_funcEv(
    QQuickBorderImage *self) {
  return self->d_func();
}

//  const QQuickBorderImagePrivate *QQuickBorderImage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickBorderImagePrivate *ritual_ZNK17QQuickBorderImage6d_funcEv(
    const QQuickBorderImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickBorderImage, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBorderImage(
    QQuickBorderImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBorderImage *>(self)->take(key, call);
}

//  void QQuickBorderImage::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickBorderImage9setSourceERK4QUrl(
    QQuickBorderImage *self,
    const QUrl *url) {
  self->QQuickBorderImage::setSource(*url);
}

//  void QQuickBorderImage::load()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickBorderImage4loadEv(QQuickBorderImage *self) {
  static_cast<OwnQQuickBorderImage *>(self)->OwnQQuickBorderImage::load();
}

//  void QQuickBorderImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickBorderImage12pixmapChangeEv(
    QQuickBorderImage *self) {
  static_cast<OwnQQuickBorderImage *>(self)->OwnQQuickBorderImage::pixmapChange();
}

//  QSGNode *QQuickBorderImage::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN17QQuickBorderImage15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickBorderImage *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickBorderImage *>(self)->OwnQQuickBorderImage::updatePaintNode(
      a0,
      a1);
}

//  void QQuickBorderImage::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickBorderImage15requestFinishedEv(
    QQuickBorderImage *self) {
  self->QQuickBorderImage::requestFinished();
}
