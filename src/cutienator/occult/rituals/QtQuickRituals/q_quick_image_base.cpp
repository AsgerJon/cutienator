//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickimagebase_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickimagebase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolorspace.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickImageBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickImageBase : QQuickImageBase {
  using QQuickImageBase::load;
  using QQuickImageBase::componentComplete;
  using QQuickImageBase::pixmapChange;
  using QQuickImageBase::itemChange;
};

//  A QQuickImageBase that Python can take functions over in. Every QQuickImageBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickImageBaseCall0)(const void *, const QUrl *, int *);
typedef void (*CuteQQuickImageBaseCall1)(const void *, const QSize *, int *);
typedef void (*CuteQQuickImageBaseCall2)(const void *, bool, int *);
typedef void (*CuteQQuickImageBaseCall3)(const void *, bool, int *);
typedef void (*CuteQQuickImageBaseCall4)(const void *, int, int *);
typedef int (*CuteQQuickImageBaseCall5)(const void *, int *);
typedef int (*CuteQQuickImageBaseCall6)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall7)(const void *, bool, int *);
typedef void (*CuteQQuickImageBaseCall8)(const void *, const QColorSpace *, int *);
typedef void (*CuteQQuickImageBaseCall9)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall10)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall11)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall12)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall13)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickImageBaseCall14)(const void *, int *);
typedef const QRectF * (*CuteQQuickImageBaseCall15)(const void *, int *);
typedef const QRectF * (*CuteQQuickImageBaseCall16)(const void *, int *);
typedef bool (*CuteQQuickImageBaseCall17)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickImageBaseCall18)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickImageBaseCall19)(const void *, int *);
typedef void * (*CuteQQuickImageBaseCall20)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageBaseCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageBaseCall22)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickImageBaseCall23)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickImageBaseCall25)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickImageBaseCall26)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickImageBaseCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickImageBaseCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickImageBaseCall29)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageBaseCall30)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageBaseCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageBaseCall32)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageBaseCall33)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall34)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickImageBaseCall35)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickImageBaseCall36)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickImageBaseCall37)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickImageBaseCall38)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickImageBaseCall39)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageBaseCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageBaseCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageBaseCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageBaseCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickImageBaseCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickImageBaseCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickImageBaseCall46)(const void *, int *);
typedef void (*CuteQQuickImageBaseCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageBaseCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageBaseCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageBaseCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageBaseCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageBaseCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageBaseCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageBase : public QQuickImageBase {
public:
  using QQuickImageBase::QQuickImageBase;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setSourceERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setSourceSizeERK5QSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase9setMirrorEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase19setMirrorVerticallyEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase15setCurrentFrameEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickImageBase12currentFrameEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickImageBase10frameCountEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase16setAutoTransformEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase4loadEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase12pixmapChangeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickImageBase15requestFinishedEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[20] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[39] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
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

  //  void QQuickImageBase::setSource(const QUrl &url)
  void setSource(const QUrl &url) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageBaseCall0 call = reinterpret_cast<CuteQQuickImageBaseCall0>(taken[0]);
      call(this, &url, &handled);
      if (handled) return;
    }
    QQuickImageBase::setSource(url);
  }

  //  void QQuickImageBase::setSourceSize(const QSize &a0)
  void setSourceSize(const QSize &a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageBaseCall1 call = reinterpret_cast<CuteQQuickImageBaseCall1>(taken[1]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickImageBase::setSourceSize(a0);
  }

  //  void QQuickImageBase::setMirror(bool mirror)
  void setMirror(bool mirror) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageBaseCall2 call = reinterpret_cast<CuteQQuickImageBaseCall2>(taken[2]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirror(mirror);
  }

  //  void QQuickImageBase::setMirrorVertically(bool mirror)
  void setMirrorVertically(bool mirror) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageBaseCall3 call = reinterpret_cast<CuteQQuickImageBaseCall3>(taken[3]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QQuickImageBase::setMirrorVertically(mirror);
  }

  //  void QQuickImageBase::setCurrentFrame(int frame)
  void setCurrentFrame(int frame) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageBaseCall4 call = reinterpret_cast<CuteQQuickImageBaseCall4>(taken[4]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QQuickImageBase::setCurrentFrame(frame);
  }

  //  int QQuickImageBase::currentFrame() const
  int currentFrame() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageBaseCall5 call = reinterpret_cast<CuteQQuickImageBaseCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImageBase::currentFrame();
  }

  //  int QQuickImageBase::frameCount() const
  int frameCount() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageBaseCall6 call = reinterpret_cast<CuteQQuickImageBaseCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickImageBase::frameCount();
  }

  //  void QQuickImageBase::setAutoTransform(bool transform)
  void setAutoTransform(bool transform) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImageBaseCall7 call = reinterpret_cast<CuteQQuickImageBaseCall7>(taken[7]);
      call(this, transform, &handled);
      if (handled) return;
    }
    QQuickImageBase::setAutoTransform(transform);
  }

  //  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
  void setColorSpace(const QColorSpace &colorSpace) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImageBaseCall8 call = reinterpret_cast<CuteQQuickImageBaseCall8>(taken[8]);
      call(this, &colorSpace, &handled);
      if (handled) return;
    }
    QQuickImageBase::setColorSpace(colorSpace);
  }

  //  void QQuickImageBase::emitAutoTransformBaseChanged()
  void emitAutoTransformBaseChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImageBaseCall9 call = reinterpret_cast<CuteQQuickImageBaseCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::emitAutoTransformBaseChanged();
  }

  //  void QQuickImageBase::load()
  void load() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickImageBaseCall10 call = reinterpret_cast<CuteQQuickImageBaseCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::load();
  }

  //  void QQuickImageBase::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickImageBaseCall11 call = reinterpret_cast<CuteQQuickImageBaseCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::componentComplete();
  }

  //  void QQuickImageBase::pixmapChange()
  void pixmapChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickImageBaseCall12 call = reinterpret_cast<CuteQQuickImageBaseCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::pixmapChange();
  }

  //  void QQuickImageBase::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickImageBaseCall13 call = reinterpret_cast<CuteQQuickImageBaseCall13>(taken[13]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickImageBase::itemChange(change, value);
  }

  //  void QQuickImageBase::requestFinished()
  void requestFinished() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickImageBaseCall14 call = reinterpret_cast<CuteQQuickImageBaseCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageBase::requestFinished();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickImageBaseCall15 call = reinterpret_cast<CuteQQuickImageBaseCall15>(taken[15]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickImageBaseCall16 call = reinterpret_cast<CuteQQuickImageBaseCall16>(taken[16]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickImageBaseCall17 call = reinterpret_cast<CuteQQuickImageBaseCall17>(taken[17]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickImageBaseCall18 call = reinterpret_cast<CuteQQuickImageBaseCall18>(taken[18]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickImageBaseCall19 call = reinterpret_cast<CuteQQuickImageBaseCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickImageBaseCall20 call = reinterpret_cast<CuteQQuickImageBaseCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickImageBaseCall21 call = reinterpret_cast<CuteQQuickImageBaseCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQQuickImageBaseCall22 call = reinterpret_cast<CuteQQuickImageBaseCall22>(taken[22]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickImageBaseCall23 call = reinterpret_cast<CuteQQuickImageBaseCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickImageBaseCall24 call = reinterpret_cast<CuteQQuickImageBaseCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickImageBaseCall25 call = reinterpret_cast<CuteQQuickImageBaseCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickImageBaseCall26 call = reinterpret_cast<CuteQQuickImageBaseCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickImageBaseCall27 call = reinterpret_cast<CuteQQuickImageBaseCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickImageBaseCall28 call = reinterpret_cast<CuteQQuickImageBaseCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickImageBaseCall29 call = reinterpret_cast<CuteQQuickImageBaseCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickImageBaseCall30 call = reinterpret_cast<CuteQQuickImageBaseCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickImageBaseCall31 call = reinterpret_cast<CuteQQuickImageBaseCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickImageBaseCall32 call = reinterpret_cast<CuteQQuickImageBaseCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickImageBaseCall33 call = reinterpret_cast<CuteQQuickImageBaseCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickImageBaseCall34 call = reinterpret_cast<CuteQQuickImageBaseCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickImageBaseCall35 call = reinterpret_cast<CuteQQuickImageBaseCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickImageBaseCall36 call = reinterpret_cast<CuteQQuickImageBaseCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickImageBaseCall37 call = reinterpret_cast<CuteQQuickImageBaseCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickImageBaseCall38 call = reinterpret_cast<CuteQQuickImageBaseCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickImageBaseCall39 call = reinterpret_cast<CuteQQuickImageBaseCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickImageBaseCall40 call = reinterpret_cast<CuteQQuickImageBaseCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickImageBaseCall41 call = reinterpret_cast<CuteQQuickImageBaseCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickImageBaseCall42 call = reinterpret_cast<CuteQQuickImageBaseCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickImageBaseCall43 call = reinterpret_cast<CuteQQuickImageBaseCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickImageBaseCall44 call = reinterpret_cast<CuteQQuickImageBaseCall44>(taken[44]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickImageBaseCall45 call = reinterpret_cast<CuteQQuickImageBaseCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickImageBaseCall46 call = reinterpret_cast<CuteQQuickImageBaseCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickImageBaseCall47 call = reinterpret_cast<CuteQQuickImageBaseCall47>(taken[47]);
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
      CuteQQuickImageBaseCall48 call = reinterpret_cast<CuteQQuickImageBaseCall48>(taken[48]);
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
      CuteQQuickImageBaseCall49 call = reinterpret_cast<CuteQQuickImageBaseCall49>(taken[49]);
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
      CuteQQuickImageBaseCall50 call = reinterpret_cast<CuteQQuickImageBaseCall50>(taken[50]);
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
      CuteQQuickImageBaseCall51 call = reinterpret_cast<CuteQQuickImageBaseCall51>(taken[51]);
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
      CuteQQuickImageBaseCall52 call = reinterpret_cast<CuteQQuickImageBaseCall52>(taken[52]);
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
      CuteQQuickImageBaseCall53 call = reinterpret_cast<CuteQQuickImageBaseCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImageBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickImageBase10metaObjectEv(
    const QQuickImageBase *self) {
  return self->metaObject();
}

//  QString QQuickImageBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickImageBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImageBase::tr(s, c, n));
}

//  void QQuickImageBase::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase24qt_qmlMarker_uncreatableEv(
    QQuickImageBase *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickImageBase::QQuickImageBase(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickImageBase *ritual_ZN15QQuickImageBaseC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickImageBase(parent);
}

//  QQuickImageBase::~QQuickImageBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBaseD1Ev(QQuickImageBase *self) {
  delete self;
}

//  Status QQuickImageBase::status() const
extern "C" Q_DECL_EXPORT
QQuickImageBase::Status ritual_ZNK15QQuickImageBase6statusEv(
    const QQuickImageBase *self) {
  return self->status();
}

//  qreal QQuickImageBase::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickImageBase8progressEv(const QQuickImageBase *self) {
  return self->progress();
}

//  QUrl QQuickImageBase::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QQuickImageBase6sourceEv(const QQuickImageBase *self) {
  return new QUrl(self->source());
}

//  void QQuickImageBase::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase9setSourceERK4QUrl(
    QQuickImageBase *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  bool QQuickImageBase::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickImageBase12asynchronousEv(
    const QQuickImageBase *self) {
  return self->asynchronous();
}

//  void QQuickImageBase::setAsynchronous(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase15setAsynchronousEb(
    QQuickImageBase *self,
    bool a0) {
  self->setAsynchronous(a0);
}

//  bool QQuickImageBase::cache() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickImageBase5cacheEv(const QQuickImageBase *self) {
  return self->cache();
}

//  void QQuickImageBase::setCache(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase8setCacheEb(QQuickImageBase *self, bool a0) {
  self->setCache(a0);
}

//  QImage QQuickImageBase::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK15QQuickImageBase5imageEv(const QQuickImageBase *self) {
  return new QImage(self->image());
}

//  void QQuickImageBase::setSourceSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase13setSourceSizeERK5QSize(
    QQuickImageBase *self,
    const QSize *a0) {
  self->setSourceSize(*a0);
}

//  QSize QQuickImageBase::sourceSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QQuickImageBase10sourceSizeEv(
    const QQuickImageBase *self) {
  return new QSize(self->sourceSize());
}

//  void QQuickImageBase::resetSourceSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase15resetSourceSizeEv(QQuickImageBase *self) {
  self->resetSourceSize();
}

//  QRectF QQuickImageBase::sourceClipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QQuickImageBase14sourceClipRectEv(
    const QQuickImageBase *self) {
  return new QRectF(self->sourceClipRect());
}

//  void QQuickImageBase::setSourceClipRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase17setSourceClipRectERK6QRectF(
    QQuickImageBase *self,
    const QRectF *r) {
  self->setSourceClipRect(*r);
}

//  void QQuickImageBase::resetSourceClipRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase19resetSourceClipRectEv(
    QQuickImageBase *self) {
  self->resetSourceClipRect();
}

//  void QQuickImageBase::setMirror(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase9setMirrorEb(
    QQuickImageBase *self,
    bool mirror) {
  self->setMirror(mirror);
}

//  bool QQuickImageBase::mirror() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickImageBase6mirrorEv(const QQuickImageBase *self) {
  return self->mirror();
}

//  void QQuickImageBase::setMirrorVertically(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase19setMirrorVerticallyEb(
    QQuickImageBase *self,
    bool mirror) {
  self->setMirrorVertically(mirror);
}

//  bool QQuickImageBase::mirrorVertically() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickImageBase16mirrorVerticallyEv(
    const QQuickImageBase *self) {
  return self->mirrorVertically();
}

//  void QQuickImageBase::setCurrentFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase15setCurrentFrameEi(
    QQuickImageBase *self,
    int frame) {
  self->setCurrentFrame(frame);
}

//  int QQuickImageBase::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickImageBase12currentFrameEv(
    const QQuickImageBase *self) {
  return self->currentFrame();
}

//  int QQuickImageBase::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickImageBase10frameCountEv(const QQuickImageBase *self) {
  return self->frameCount();
}

//  void QQuickImageBase::setAutoTransform(bool transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase16setAutoTransformEb(
    QQuickImageBase *self,
    bool transform) {
  self->setAutoTransform(transform);
}

//  bool QQuickImageBase::autoTransform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickImageBase13autoTransformEv(
    const QQuickImageBase *self) {
  return self->autoTransform();
}

//  QColorSpace QQuickImageBase::colorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK15QQuickImageBase10colorSpaceEv(
    const QQuickImageBase *self) {
  return new QColorSpace(self->colorSpace());
}

//  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace(
    QQuickImageBase *self,
    const QColorSpace *colorSpace) {
  self->setColorSpace(*colorSpace);
}

//  bool QQuickImageBase::retainWhileLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickImageBase18retainWhileLoadingEv(
    const QQuickImageBase *self) {
  return self->retainWhileLoading();
}

//  void QQuickImageBase::setRetainWhileLoading(bool retain)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase21setRetainWhileLoadingEb(
    QQuickImageBase *self,
    bool retain) {
  self->setRetainWhileLoading(retain);
}

//  void QQuickImageBase::resolve2xLocalFile(const QUrl &url, qreal
//      targetDevicePixelRatio, QUrl *sourceUrl, qreal
//      *sourceDevicePixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase18resolve2xLocalFileERK4QUrldPS0_Pd(
    const QUrl *url,
    qreal targetDevicePixelRatio,
    QUrl *sourceUrl,
    qreal *sourceDevicePixelRatio) {
  QQuickImageBase::resolve2xLocalFile(
      *url,
      targetDevicePixelRatio,
      sourceUrl,
      sourceDevicePixelRatio);
}

//  void QQuickImageBase::emitAutoTransformBaseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv(
    QQuickImageBase *self) {
  self->emitAutoTransformBaseChanged();
}

//  void QQuickImageBase::loadEmptyUrl()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase12loadEmptyUrlEv(QQuickImageBase *self) {
  self->loadEmptyUrl();
}

//  void QQuickImageBase::loadPixmap(const QUrl &url, LoadPixmapOptions
//      loadOptions)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase10loadPixmapERK4QUrl6QFlagsINS_16LoadPixmapOptionEE(
    QQuickImageBase *self,
    const QUrl *url,
    int loadOptions) {
  self->loadPixmap(
      *url,
      QFlags<QQuickImageBase::LoadPixmapOption>::fromInt(loadOptions));
}

//  void QQuickImageBase::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase4loadEv(QQuickImageBase *self) {
  self->load();
}

//  void QQuickImageBase::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase17componentCompleteEv(QQuickImageBase *self) {
  self->componentComplete();
}

//  void QQuickImageBase::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase12pixmapChangeEv(QQuickImageBase *self) {
  self->pixmapChange();
}

//  void QQuickImageBase::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickImageBase *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickImageBase::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase15requestFinishedEv(QQuickImageBase *self) {
  self->requestFinished();
}

//  void QQuickImageBase::requestProgress(qint64 a0, qint64 a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickImageBase15requestProgressExx(
    QQuickImageBase *self,
    qint64 a0,
    qint64 a1) {
  self->requestProgress(a0, a1);
}

//  QQuickImageBasePrivate *QQuickImageBase::d_func()
extern "C" Q_DECL_EXPORT
QQuickImageBasePrivate *ritual_ZN15QQuickImageBase6d_funcEv(
    QQuickImageBase *self) {
  return self->d_func();
}

//  const QQuickImageBasePrivate *QQuickImageBase::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickImageBasePrivate *ritual_ZNK15QQuickImageBase6d_funcEv(
    const QQuickImageBase *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickImageBase, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageBase(
    QQuickImageBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageBase *>(self)->take(key, call);
}

//  void QQuickImageBase::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase9setSourceERK4QUrl(
    QQuickImageBase *self,
    const QUrl *url) {
  self->QQuickImageBase::setSource(*url);
}

//  void QQuickImageBase::setSourceSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase13setSourceSizeERK5QSize(
    QQuickImageBase *self,
    const QSize *a0) {
  self->QQuickImageBase::setSourceSize(*a0);
}

//  void QQuickImageBase::setMirror(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase9setMirrorEb(
    QQuickImageBase *self,
    bool mirror) {
  self->QQuickImageBase::setMirror(mirror);
}

//  void QQuickImageBase::setMirrorVertically(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase19setMirrorVerticallyEb(
    QQuickImageBase *self,
    bool mirror) {
  self->QQuickImageBase::setMirrorVertically(mirror);
}

//  void QQuickImageBase::setCurrentFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase15setCurrentFrameEi(
    QQuickImageBase *self,
    int frame) {
  self->QQuickImageBase::setCurrentFrame(frame);
}

//  int QQuickImageBase::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QQuickImageBase12currentFrameEv(
    const QQuickImageBase *self) {
  return self->QQuickImageBase::currentFrame();
}

//  int QQuickImageBase::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QQuickImageBase10frameCountEv(
    const QQuickImageBase *self) {
  return self->QQuickImageBase::frameCount();
}

//  void QQuickImageBase::setAutoTransform(bool transform)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase16setAutoTransformEb(
    QQuickImageBase *self,
    bool transform) {
  self->QQuickImageBase::setAutoTransform(transform);
}

//  void QQuickImageBase::setColorSpace(const QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase13setColorSpaceERK11QColorSpace(
    QQuickImageBase *self,
    const QColorSpace *colorSpace) {
  self->QQuickImageBase::setColorSpace(*colorSpace);
}

//  void QQuickImageBase::emitAutoTransformBaseChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase28emitAutoTransformBaseChangedEv(
    QQuickImageBase *self) {
  self->QQuickImageBase::emitAutoTransformBaseChanged();
}

//  void QQuickImageBase::load()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase4loadEv(QQuickImageBase *self) {
  static_cast<OwnQQuickImageBase *>(self)->OwnQQuickImageBase::load();
}

//  void QQuickImageBase::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase17componentCompleteEv(
    QQuickImageBase *self) {
  static_cast<OwnQQuickImageBase *>(self)->OwnQQuickImageBase::componentComplete();
}

//  void QQuickImageBase::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase12pixmapChangeEv(QQuickImageBase *self) {
  static_cast<OwnQQuickImageBase *>(self)->OwnQQuickImageBase::pixmapChange();
}

//  void QQuickImageBase::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickImageBase *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickImageBase *>(self)->OwnQQuickImageBase::itemChange(
      change,
      *value);
}

//  void QQuickImageBase::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickImageBase15requestFinishedEv(
    QQuickImageBase *self) {
  self->QQuickImageBase::requestFinished();
}
