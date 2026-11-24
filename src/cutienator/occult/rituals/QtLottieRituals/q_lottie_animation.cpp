//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qbytearray.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLottieAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLottieAnimation : QLottieAnimation {
  using QLottieAnimation::componentComplete;
  using QLottieAnimation::parse;
};

//  A QLottieAnimation that Python can take functions over in. Every QLottieAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLottieAnimationCall0)(const void *, QPainter *, int *);
typedef void (*CuteQLottieAnimationCall1)(const void *, int *);
typedef int (*CuteQLottieAnimationCall2)(const void *, const QByteArray *, int *);
typedef bool (*CuteQLottieAnimationCall3)(const void *, int *);
typedef void * (*CuteQLottieAnimationCall4)(const void *, int *);
typedef void * (*CuteQLottieAnimationCall5)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQLottieAnimationCall6)(const void *, int *);
typedef void (*CuteQLottieAnimationCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQLottieAnimationCall8)(const void *, int *);
typedef const QRectF * (*CuteQLottieAnimationCall9)(const void *, int *);
typedef bool (*CuteQLottieAnimationCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQLottieAnimationCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLottieAnimationCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieAnimationCall13)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQLottieAnimationCall14)(const void *, int *);
typedef void (*CuteQLottieAnimationCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQLottieAnimationCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQLottieAnimationCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQLottieAnimationCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQLottieAnimationCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQLottieAnimationCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLottieAnimationCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLottieAnimationCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLottieAnimationCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQLottieAnimationCall24)(const void *, int *);
typedef void (*CuteQLottieAnimationCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQLottieAnimationCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQLottieAnimationCall27)(const void *, QTouchEvent *, int *);
typedef void (*CuteQLottieAnimationCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQLottieAnimationCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQLottieAnimationCall30)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQLottieAnimationCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQLottieAnimationCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQLottieAnimationCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQLottieAnimationCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQLottieAnimationCall35)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQLottieAnimationCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLottieAnimationCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieAnimationCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieAnimationCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieAnimationCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieAnimationCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLottieAnimationCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLottieAnimation : public QLottieAnimation {
public:
  using QLottieAnimation::QLottieAnimation;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickPaintedItem5paintEP8QPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QLottieAnimation5parseERK10QByteArray")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[36] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QLottieAnimation::paint(QPainter *painter)
  void paint(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieAnimationCall0 call = reinterpret_cast<CuteQLottieAnimationCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QLottieAnimation::paint(painter);
  }

  //  void QLottieAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieAnimationCall1 call = reinterpret_cast<CuteQLottieAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QLottieAnimation::componentComplete();
  }

  //  int QLottieAnimation::parse(const QByteArray &jsonSource)
  int parse(const QByteArray &jsonSource) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieAnimationCall2 call = reinterpret_cast<CuteQLottieAnimationCall2>(taken[2]);
      int given = call(this, &jsonSource, &handled);
      if (handled) return given;
    }
    return QLottieAnimation::parse(jsonSource);
  }

  //  bool QQuickPaintedItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieAnimationCall3 call = reinterpret_cast<CuteQLottieAnimationCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPaintedItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieAnimationCall4 call = reinterpret_cast<CuteQLottieAnimationCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickPaintedItem::textureProvider();
  }

  //  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieAnimationCall5 call = reinterpret_cast<CuteQLottieAnimationCall5>(taken[5]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickPaintedItem::updatePaintNode(a0, a1);
  }

  //  void QQuickPaintedItem::releaseResources()
  void releaseResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieAnimationCall6 call = reinterpret_cast<CuteQLottieAnimationCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::releaseResources();
  }

  //  void QQuickPaintedItem::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieAnimationCall7 call = reinterpret_cast<CuteQLottieAnimationCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::itemChange(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieAnimationCall8 call = reinterpret_cast<CuteQLottieAnimationCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieAnimationCall9 call = reinterpret_cast<CuteQLottieAnimationCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieAnimationCall10 call = reinterpret_cast<CuteQLottieAnimationCall10>(taken[10]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieAnimationCall11 call = reinterpret_cast<CuteQLottieAnimationCall11>(taken[11]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieAnimationCall12 call = reinterpret_cast<CuteQLottieAnimationCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQLottieAnimationCall13 call = reinterpret_cast<CuteQLottieAnimationCall13>(taken[13]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQLottieAnimationCall14 call = reinterpret_cast<CuteQLottieAnimationCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLottieAnimationCall15 call = reinterpret_cast<CuteQLottieAnimationCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLottieAnimationCall16 call = reinterpret_cast<CuteQLottieAnimationCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLottieAnimationCall17 call = reinterpret_cast<CuteQLottieAnimationCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLottieAnimationCall18 call = reinterpret_cast<CuteQLottieAnimationCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLottieAnimationCall19 call = reinterpret_cast<CuteQLottieAnimationCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLottieAnimationCall20 call = reinterpret_cast<CuteQLottieAnimationCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLottieAnimationCall21 call = reinterpret_cast<CuteQLottieAnimationCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLottieAnimationCall22 call = reinterpret_cast<CuteQLottieAnimationCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLottieAnimationCall23 call = reinterpret_cast<CuteQLottieAnimationCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQLottieAnimationCall24 call = reinterpret_cast<CuteQLottieAnimationCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQLottieAnimationCall25 call = reinterpret_cast<CuteQLottieAnimationCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQLottieAnimationCall26 call = reinterpret_cast<CuteQLottieAnimationCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQLottieAnimationCall27 call = reinterpret_cast<CuteQLottieAnimationCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQLottieAnimationCall28 call = reinterpret_cast<CuteQLottieAnimationCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQLottieAnimationCall29 call = reinterpret_cast<CuteQLottieAnimationCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQLottieAnimationCall30 call = reinterpret_cast<CuteQLottieAnimationCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQLottieAnimationCall31 call = reinterpret_cast<CuteQLottieAnimationCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQLottieAnimationCall32 call = reinterpret_cast<CuteQLottieAnimationCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQLottieAnimationCall33 call = reinterpret_cast<CuteQLottieAnimationCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQLottieAnimationCall34 call = reinterpret_cast<CuteQLottieAnimationCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[35]) {
      int handled = 0;
      CuteQLottieAnimationCall35 call = reinterpret_cast<CuteQLottieAnimationCall35>(taken[35]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[36]) {
      int handled = 0;
      CuteQLottieAnimationCall36 call = reinterpret_cast<CuteQLottieAnimationCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQLottieAnimationCall37 call = reinterpret_cast<CuteQLottieAnimationCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQLottieAnimationCall38 call = reinterpret_cast<CuteQLottieAnimationCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQLottieAnimationCall39 call = reinterpret_cast<CuteQLottieAnimationCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQLottieAnimationCall40 call = reinterpret_cast<CuteQLottieAnimationCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQLottieAnimationCall41 call = reinterpret_cast<CuteQLottieAnimationCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQLottieAnimationCall42 call = reinterpret_cast<CuteQLottieAnimationCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLottieAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QLottieAnimation10metaObjectEv(
    const QLottieAnimation *self) {
  return self->metaObject();
}

//  QString QLottieAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QLottieAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLottieAnimation::tr(s, c, n));
}

//  QLottieAnimation::QLottieAnimation(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QLottieAnimation *ritual_ZN16QLottieAnimationC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQLottieAnimation(parent);
}

//  QLottieAnimation::~QLottieAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimationD1Ev(QLottieAnimation *self) {
  delete self;
}

//  void QLottieAnimation::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation5paintEP8QPainter(
    QLottieAnimation *self,
    QPainter *painter) {
  self->paint(painter);
}

//  Status QLottieAnimation::status() const
extern "C" Q_DECL_EXPORT
QLottieAnimation::Status ritual_ZNK16QLottieAnimation6statusEv(
    const QLottieAnimation *self) {
  return self->status();
}

//  QUrl QLottieAnimation::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QLottieAnimation6sourceEv(const QLottieAnimation *self) {
  return new QUrl(self->source());
}

//  void QLottieAnimation::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation9setSourceERK4QUrl(
    QLottieAnimation *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  int QLottieAnimation::frameRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QLottieAnimation9frameRateEv(const QLottieAnimation *self) {
  return self->frameRate();
}

//  void QLottieAnimation::setFrameRate(int frameRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation12setFrameRateEi(
    QLottieAnimation *self,
    int frameRate) {
  self->setFrameRate(frameRate);
}

//  void QLottieAnimation::resetFrameRate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation14resetFrameRateEv(QLottieAnimation *self) {
  self->resetFrameRate();
}

//  Quality QLottieAnimation::quality() const
extern "C" Q_DECL_EXPORT
QLottieAnimation::Quality ritual_ZNK16QLottieAnimation7qualityEv(
    const QLottieAnimation *self) {
  return self->quality();
}

//  void QLottieAnimation::setQuality(Quality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation10setQualityENS_7QualityE(
    QLottieAnimation *self,
    QLottieAnimation::Quality quality) {
  self->setQuality(quality);
}

//  Direction QLottieAnimation::direction() const
extern "C" Q_DECL_EXPORT
QLottieAnimation::Direction ritual_ZNK16QLottieAnimation9directionEv(
    const QLottieAnimation *self) {
  return self->direction();
}

//  void QLottieAnimation::setDirection(Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation12setDirectionENS_9DirectionE(
    QLottieAnimation *self,
    QLottieAnimation::Direction direction) {
  self->setDirection(direction);
}

//  int QLottieAnimation::startFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QLottieAnimation10startFrameEv(
    const QLottieAnimation *self) {
  return self->startFrame();
}

//  int QLottieAnimation::endFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QLottieAnimation8endFrameEv(const QLottieAnimation *self) {
  return self->endFrame();
}

//  int QLottieAnimation::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QLottieAnimation12currentFrameEv(
    const QLottieAnimation *self) {
  return self->currentFrame();
}

//  QVersionNumber QLottieAnimation::version() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK16QLottieAnimation7versionEv(
    const QLottieAnimation *self) {
  return new QVersionNumber(self->version());
}

//  void QLottieAnimation::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation5startEv(QLottieAnimation *self) {
  self->start();
}

//  void QLottieAnimation::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation4playEv(QLottieAnimation *self) {
  self->play();
}

//  void QLottieAnimation::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation5pauseEv(QLottieAnimation *self) {
  self->pause();
}

//  void QLottieAnimation::togglePause()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation11togglePauseEv(QLottieAnimation *self) {
  self->togglePause();
}

//  void QLottieAnimation::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation4stopEv(QLottieAnimation *self) {
  self->stop();
}

//  void QLottieAnimation::gotoAndPlay(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation11gotoAndPlayEi(
    QLottieAnimation *self,
    int frame) {
  self->gotoAndPlay(frame);
}

//  bool QLottieAnimation::gotoAndPlay(const QString &frameMarker)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QLottieAnimation11gotoAndPlayERK7QString(
    QLottieAnimation *self,
    const QString *frameMarker) {
  return self->gotoAndPlay(*frameMarker);
}

//  void QLottieAnimation::gotoAndStop(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation11gotoAndStopEi(
    QLottieAnimation *self,
    int frame) {
  self->gotoAndStop(frame);
}

//  bool QLottieAnimation::gotoAndStop(const QString &frameMarker)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QLottieAnimation11gotoAndStopERK7QString(
    QLottieAnimation *self,
    const QString *frameMarker) {
  return self->gotoAndStop(*frameMarker);
}

//  double QLottieAnimation::getDuration(bool inFrames)
extern "C" Q_DECL_EXPORT
double ritual_ZN16QLottieAnimation11getDurationEb(
    QLottieAnimation *self,
    bool inFrames) {
  return self->getDuration(inFrames);
}

//  QByteArray QLottieAnimation::jsonSource() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QLottieAnimation10jsonSourceEv(
    const QLottieAnimation *self) {
  return new QByteArray(self->jsonSource());
}

//  void QLottieAnimation::loadFinished(const QByteArray &json)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation12loadFinishedERK10QByteArray(
    QLottieAnimation *self,
    const QByteArray *json) {
  self->loadFinished(*json);
}

//  void QLottieAnimation::renderNextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation15renderNextFrameEv(QLottieAnimation *self) {
  self->renderNextFrame();
}

//  void QLottieAnimation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation17componentCompleteEv(
    QLottieAnimation *self) {
  self->componentComplete();
}

//  void QLottieAnimation::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation9setStatusENS_6StatusE(
    QLottieAnimation *self,
    QLottieAnimation::Status status) {
  self->setStatus(status);
}

//  void QLottieAnimation::setStartFrame(int startFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation13setStartFrameEi(
    QLottieAnimation *self,
    int startFrame) {
  self->setStartFrame(startFrame);
}

//  void QLottieAnimation::setEndFrame(int endFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation11setEndFrameEi(
    QLottieAnimation *self,
    int endFrame) {
  self->setEndFrame(endFrame);
}

//  void QLottieAnimation::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation4loadEv(QLottieAnimation *self) {
  self->load();
}

//  int QLottieAnimation::parse(const QByteArray &jsonSource)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QLottieAnimation5parseERK10QByteArray(
    QLottieAnimation *self,
    const QByteArray *jsonSource) {
  return self->parse(*jsonSource);
}

//  void QLottieAnimation::gotoFrame(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation9gotoFrameEi(
    QLottieAnimation *self,
    int frame) {
  self->gotoFrame(frame);
}

//  void QLottieAnimation::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieAnimation5resetEv(QLottieAnimation *self) {
  self->reset();
}

//  a Python function taken by a CuteQLottieAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieAnimation(
    QLottieAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieAnimation *>(self)->take(key, call);
}

//  void QLottieAnimation::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QLottieAnimation5paintEP8QPainter(
    QLottieAnimation *self,
    QPainter *painter) {
  self->QLottieAnimation::paint(painter);
}

//  void QLottieAnimation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QLottieAnimation17componentCompleteEv(
    QLottieAnimation *self) {
  static_cast<OwnQLottieAnimation *>(self)->OwnQLottieAnimation::componentComplete();
}

//  int QLottieAnimation::parse(const QByteArray &jsonSource)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN16QLottieAnimation5parseERK10QByteArray(
    QLottieAnimation *self,
    const QByteArray *jsonSource) {
  return static_cast<OwnQLottieAnimation *>(self)->OwnQLottieAnimation::parse(
      *jsonSource);
}
