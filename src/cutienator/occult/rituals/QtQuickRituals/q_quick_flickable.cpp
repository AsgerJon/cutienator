//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickflickable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickflickable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickFlickable may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFlickable : QQuickFlickable {
  using QQuickFlickable::childMouseEventFilter;
  using QQuickFlickable::mousePressEvent;
  using QQuickFlickable::mouseMoveEvent;
  using QQuickFlickable::mouseReleaseEvent;
  using QQuickFlickable::touchEvent;
  using QQuickFlickable::wheelEvent;
  using QQuickFlickable::timerEvent;
  using QQuickFlickable::minXExtent;
  using QQuickFlickable::minYExtent;
  using QQuickFlickable::maxXExtent;
  using QQuickFlickable::maxYExtent;
  using QQuickFlickable::componentComplete;
  using QQuickFlickable::viewportMoved;
  using QQuickFlickable::geometryChange;
  using QQuickFlickable::mouseUngrabEvent;
};

//  A QQuickFlickable that Python can take functions over in. Every QQuickFlickable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFlickableCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickFlickableCall1)(const void *, qreal, int *);
typedef qreal (*CuteQQuickFlickableCall2)(const void *, int *);
typedef qreal (*CuteQQuickFlickableCall3)(const void *, int *);
typedef bool (*CuteQQuickFlickableCall4)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickFlickableCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlickableCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlickableCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlickableCall8)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickFlickableCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlickableCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef qreal (*CuteQQuickFlickableCall11)(const void *, int *);
typedef qreal (*CuteQQuickFlickableCall12)(const void *, int *);
typedef qreal (*CuteQQuickFlickableCall13)(const void *, int *);
typedef qreal (*CuteQQuickFlickableCall14)(const void *, int *);
typedef void (*CuteQQuickFlickableCall15)(const void *, int *);
typedef void (*CuteQQuickFlickableCall16)(const void *, int, int *);
typedef void (*CuteQQuickFlickableCall17)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickFlickableCall18)(const void *, int *);
typedef const QRectF * (*CuteQQuickFlickableCall19)(const void *, int *);
typedef const QRectF * (*CuteQQuickFlickableCall20)(const void *, int *);
typedef bool (*CuteQQuickFlickableCall21)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickFlickableCall22)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickFlickableCall23)(const void *, int *);
typedef void * (*CuteQQuickFlickableCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFlickableCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlickableCall26)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickFlickableCall27)(const void *, int *);
typedef void (*CuteQQuickFlickableCall28)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickFlickableCall29)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickFlickableCall30)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickFlickableCall31)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickFlickableCall32)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickFlickableCall33)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickFlickableCall34)(const void *, int *);
typedef void (*CuteQQuickFlickableCall35)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickFlickableCall36)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickFlickableCall37)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlickableCall38)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlickableCall39)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlickableCall40)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickFlickableCall41)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickFlickableCall42)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickFlickableCall43)(const void *, int *);
typedef void (*CuteQQuickFlickableCall44)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFlickableCall45)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlickableCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlickableCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlickableCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFlickableCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFlickable : public QQuickFlickable {
public:
  using QQuickFlickable::QQuickFlickable;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentXEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentYEd")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originYEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originXEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minXExtentEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minYExtentEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxXExtentEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxYExtentEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[37] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[44] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickFlickable::setContentX(qreal pos)
  void setContentX(qreal pos) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFlickableCall0 call = reinterpret_cast<CuteQQuickFlickableCall0>(taken[0]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentX(pos);
  }

  //  void QQuickFlickable::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFlickableCall1 call = reinterpret_cast<CuteQQuickFlickableCall1>(taken[1]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentY(pos);
  }

  //  qreal QQuickFlickable::originY() const
  qreal originY() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFlickableCall2 call = reinterpret_cast<CuteQQuickFlickableCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::originY();
  }

  //  qreal QQuickFlickable::originX() const
  qreal originX() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFlickableCall3 call = reinterpret_cast<CuteQQuickFlickableCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::originX();
  }

  //  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFlickableCall4 call = reinterpret_cast<CuteQQuickFlickableCall4>(taken[4]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFlickableCall5 call = reinterpret_cast<CuteQQuickFlickableCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFlickableCall6 call = reinterpret_cast<CuteQQuickFlickableCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickFlickableCall7 call = reinterpret_cast<CuteQQuickFlickableCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickFlickableCall8 call = reinterpret_cast<CuteQQuickFlickableCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::touchEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickFlickable::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFlickableCall9 call = reinterpret_cast<CuteQQuickFlickableCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
  //  void QQuickFlickable::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFlickableCall10 call = reinterpret_cast<CuteQQuickFlickableCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  qreal QQuickFlickable::minXExtent() const
  qreal minXExtent() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFlickableCall11 call = reinterpret_cast<CuteQQuickFlickableCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::minXExtent();
  }

  //  qreal QQuickFlickable::minYExtent() const
  qreal minYExtent() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFlickableCall12 call = reinterpret_cast<CuteQQuickFlickableCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::minYExtent();
  }

  //  qreal QQuickFlickable::maxXExtent() const
  qreal maxXExtent() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFlickableCall13 call = reinterpret_cast<CuteQQuickFlickableCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::maxXExtent();
  }

  //  qreal QQuickFlickable::maxYExtent() const
  qreal maxYExtent() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFlickableCall14 call = reinterpret_cast<CuteQQuickFlickableCall14>(taken[14]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::maxYExtent();
  }

  //  void QQuickFlickable::componentComplete()
  void componentComplete() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFlickableCall15 call = reinterpret_cast<CuteQQuickFlickableCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::componentComplete();
  }

  //  void QQuickFlickable::viewportMoved(Qt::Orientations orient)
  void viewportMoved(Qt::Orientations orient) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFlickableCall16 call = reinterpret_cast<CuteQQuickFlickableCall16>(taken[16]);
      call(this, static_cast<int>(orient.toInt()), &handled);
      if (handled) return;
    }
    QQuickFlickable::viewportMoved(orient);
  }

  //  void QQuickFlickable::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFlickableCall17 call = reinterpret_cast<CuteQQuickFlickableCall17>(taken[17]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickFlickable::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickFlickable::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFlickableCall18 call = reinterpret_cast<CuteQQuickFlickableCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFlickableCall19 call = reinterpret_cast<CuteQQuickFlickableCall19>(taken[19]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFlickableCall20 call = reinterpret_cast<CuteQQuickFlickableCall20>(taken[20]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFlickableCall21 call = reinterpret_cast<CuteQQuickFlickableCall21>(taken[21]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickFlickableCall22 call = reinterpret_cast<CuteQQuickFlickableCall22>(taken[22]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickFlickableCall23 call = reinterpret_cast<CuteQQuickFlickableCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickFlickableCall24 call = reinterpret_cast<CuteQQuickFlickableCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickFlickableCall25 call = reinterpret_cast<CuteQQuickFlickableCall25>(taken[25]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickFlickableCall26 call = reinterpret_cast<CuteQQuickFlickableCall26>(taken[26]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickFlickableCall27 call = reinterpret_cast<CuteQQuickFlickableCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickFlickableCall28 call = reinterpret_cast<CuteQQuickFlickableCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickFlickableCall29 call = reinterpret_cast<CuteQQuickFlickableCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickFlickableCall30 call = reinterpret_cast<CuteQQuickFlickableCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickFlickableCall31 call = reinterpret_cast<CuteQQuickFlickableCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickFlickableCall32 call = reinterpret_cast<CuteQQuickFlickableCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickFlickableCall33 call = reinterpret_cast<CuteQQuickFlickableCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickFlickableCall34 call = reinterpret_cast<CuteQQuickFlickableCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickFlickableCall35 call = reinterpret_cast<CuteQQuickFlickableCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickFlickableCall36 call = reinterpret_cast<CuteQQuickFlickableCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickFlickableCall37 call = reinterpret_cast<CuteQQuickFlickableCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickFlickableCall38 call = reinterpret_cast<CuteQQuickFlickableCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickFlickableCall39 call = reinterpret_cast<CuteQQuickFlickableCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickFlickableCall40 call = reinterpret_cast<CuteQQuickFlickableCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickFlickableCall41 call = reinterpret_cast<CuteQQuickFlickableCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickFlickableCall42 call = reinterpret_cast<CuteQQuickFlickableCall42>(taken[42]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickFlickableCall43 call = reinterpret_cast<CuteQQuickFlickableCall43>(taken[43]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickFlickableCall44 call = reinterpret_cast<CuteQQuickFlickableCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickFlickableCall45 call = reinterpret_cast<CuteQQuickFlickableCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickFlickableCall46 call = reinterpret_cast<CuteQQuickFlickableCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickFlickableCall47 call = reinterpret_cast<CuteQQuickFlickableCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickFlickableCall48 call = reinterpret_cast<CuteQQuickFlickableCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickFlickableCall49 call = reinterpret_cast<CuteQQuickFlickableCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFlickable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickFlickable10metaObjectEv(
    const QQuickFlickable *self) {
  return self->metaObject();
}

//  QString QQuickFlickable::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickFlickable2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFlickable::tr(s, c, n));
}

//  QQuickFlickable::QQuickFlickable(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFlickable *ritual_ZN15QQuickFlickableC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickFlickable(parent);
}

//  QQuickFlickable::~QQuickFlickable()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickableD1Ev(QQuickFlickable *self) {
  delete self;
}

//  BoundsBehavior QQuickFlickable::boundsBehavior() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickFlickable14boundsBehaviorEv(
    const QQuickFlickable *self) {
  return static_cast<int>(self->boundsBehavior().toInt());
}

//  void QQuickFlickable::setBoundsBehavior(BoundsBehavior a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable17setBoundsBehaviorE6QFlagsINS_18BoundsBehaviorFlagEE(
    QQuickFlickable *self,
    int a0) {
  self->setBoundsBehavior(
      QFlags<QQuickFlickable::BoundsBehaviorFlag>::fromInt(a0));
}

//  BoundsMovement QQuickFlickable::boundsMovement() const
extern "C" Q_DECL_EXPORT
QQuickFlickable::BoundsMovement ritual_ZNK15QQuickFlickable14boundsMovementEv(
    const QQuickFlickable *self) {
  return self->boundsMovement();
}

//  void QQuickFlickable::setBoundsMovement(BoundsMovement movement)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable17setBoundsMovementENS_14BoundsMovementE(
    QQuickFlickable *self,
    QQuickFlickable::BoundsMovement movement) {
  self->setBoundsMovement(movement);
}

//  QQuickTransition *QQuickFlickable::rebound() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickFlickable7reboundEv(
    const QQuickFlickable *self) {
  return self->rebound();
}

//  void QQuickFlickable::setRebound(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable10setReboundEP16QQuickTransition(
    QQuickFlickable *self,
    QQuickTransition *transition) {
  self->setRebound(transition);
}

//  qreal QQuickFlickable::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable12contentWidthEv(
    const QQuickFlickable *self) {
  return self->contentWidth();
}

//  void QQuickFlickable::setContentWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable15setContentWidthEd(
    QQuickFlickable *self,
    qreal a0) {
  self->setContentWidth(a0);
}

//  qreal QQuickFlickable::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable13contentHeightEv(
    const QQuickFlickable *self) {
  return self->contentHeight();
}

//  void QQuickFlickable::setContentHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable16setContentHeightEd(
    QQuickFlickable *self,
    qreal a0) {
  self->setContentHeight(a0);
}

//  qreal QQuickFlickable::contentX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable8contentXEv(const QQuickFlickable *self) {
  return self->contentX();
}

//  void QQuickFlickable::setContentX(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable11setContentXEd(
    QQuickFlickable *self,
    qreal pos) {
  self->setContentX(pos);
}

//  qreal QQuickFlickable::contentY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable8contentYEv(const QQuickFlickable *self) {
  return self->contentY();
}

//  void QQuickFlickable::setContentY(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable11setContentYEd(
    QQuickFlickable *self,
    qreal pos) {
  self->setContentY(pos);
}

//  qreal QQuickFlickable::topMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable9topMarginEv(const QQuickFlickable *self) {
  return self->topMargin();
}

//  void QQuickFlickable::setTopMargin(qreal m)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable12setTopMarginEd(
    QQuickFlickable *self,
    qreal m) {
  self->setTopMargin(m);
}

//  qreal QQuickFlickable::bottomMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable12bottomMarginEv(
    const QQuickFlickable *self) {
  return self->bottomMargin();
}

//  void QQuickFlickable::setBottomMargin(qreal m)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable15setBottomMarginEd(
    QQuickFlickable *self,
    qreal m) {
  self->setBottomMargin(m);
}

//  qreal QQuickFlickable::leftMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable10leftMarginEv(
    const QQuickFlickable *self) {
  return self->leftMargin();
}

//  void QQuickFlickable::setLeftMargin(qreal m)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable13setLeftMarginEd(
    QQuickFlickable *self,
    qreal m) {
  self->setLeftMargin(m);
}

//  qreal QQuickFlickable::rightMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable11rightMarginEv(
    const QQuickFlickable *self) {
  return self->rightMargin();
}

//  void QQuickFlickable::setRightMargin(qreal m)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14setRightMarginEd(
    QQuickFlickable *self,
    qreal m) {
  self->setRightMargin(m);
}

//  qreal QQuickFlickable::originY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable7originYEv(const QQuickFlickable *self) {
  return self->originY();
}

//  qreal QQuickFlickable::originX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable7originXEv(const QQuickFlickable *self) {
  return self->originX();
}

//  bool QQuickFlickable::isMoving() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable8isMovingEv(const QQuickFlickable *self) {
  return self->isMoving();
}

//  bool QQuickFlickable::isMovingHorizontally() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable20isMovingHorizontallyEv(
    const QQuickFlickable *self) {
  return self->isMovingHorizontally();
}

//  bool QQuickFlickable::isMovingVertically() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable18isMovingVerticallyEv(
    const QQuickFlickable *self) {
  return self->isMovingVertically();
}

//  bool QQuickFlickable::isFlicking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable10isFlickingEv(const QQuickFlickable *self) {
  return self->isFlicking();
}

//  bool QQuickFlickable::isFlickingHorizontally() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable22isFlickingHorizontallyEv(
    const QQuickFlickable *self) {
  return self->isFlickingHorizontally();
}

//  bool QQuickFlickable::isFlickingVertically() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable20isFlickingVerticallyEv(
    const QQuickFlickable *self) {
  return self->isFlickingVertically();
}

//  bool QQuickFlickable::isDragging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable10isDraggingEv(const QQuickFlickable *self) {
  return self->isDragging();
}

//  bool QQuickFlickable::isDraggingHorizontally() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable22isDraggingHorizontallyEv(
    const QQuickFlickable *self) {
  return self->isDraggingHorizontally();
}

//  bool QQuickFlickable::isDraggingVertically() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable20isDraggingVerticallyEv(
    const QQuickFlickable *self) {
  return self->isDraggingVertically();
}

//  int QQuickFlickable::pressDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickFlickable10pressDelayEv(const QQuickFlickable *self) {
  return self->pressDelay();
}

//  void QQuickFlickable::setPressDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable13setPressDelayEi(
    QQuickFlickable *self,
    int delay) {
  self->setPressDelay(delay);
}

//  qreal QQuickFlickable::maximumFlickVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable20maximumFlickVelocityEv(
    const QQuickFlickable *self) {
  return self->maximumFlickVelocity();
}

//  void QQuickFlickable::setMaximumFlickVelocity(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable23setMaximumFlickVelocityEd(
    QQuickFlickable *self,
    qreal a0) {
  self->setMaximumFlickVelocity(a0);
}

//  qreal QQuickFlickable::flickDeceleration() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable17flickDecelerationEv(
    const QQuickFlickable *self) {
  return self->flickDeceleration();
}

//  void QQuickFlickable::setFlickDeceleration(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable20setFlickDecelerationEd(
    QQuickFlickable *self,
    qreal a0) {
  self->setFlickDeceleration(a0);
}

//  bool QQuickFlickable::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable13isInteractiveEv(
    const QQuickFlickable *self) {
  return self->isInteractive();
}

//  void QQuickFlickable::setInteractive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14setInteractiveEb(
    QQuickFlickable *self,
    bool a0) {
  self->setInteractive(a0);
}

//  qreal QQuickFlickable::horizontalVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable18horizontalVelocityEv(
    const QQuickFlickable *self) {
  return self->horizontalVelocity();
}

//  qreal QQuickFlickable::verticalVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable16verticalVelocityEv(
    const QQuickFlickable *self) {
  return self->verticalVelocity();
}

//  bool QQuickFlickable::isAtXEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable8isAtXEndEv(const QQuickFlickable *self) {
  return self->isAtXEnd();
}

//  bool QQuickFlickable::isAtXBeginning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable14isAtXBeginningEv(
    const QQuickFlickable *self) {
  return self->isAtXBeginning();
}

//  bool QQuickFlickable::isAtYEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable8isAtYEndEv(const QQuickFlickable *self) {
  return self->isAtYEnd();
}

//  bool QQuickFlickable::isAtYBeginning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable14isAtYBeginningEv(
    const QQuickFlickable *self) {
  return self->isAtYBeginning();
}

//  QQuickItem *QQuickFlickable::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickFlickable11contentItemEv(
    const QQuickFlickable *self) {
  return self->contentItem();
}

//  FlickableDirection QQuickFlickable::flickableDirection() const
extern "C" Q_DECL_EXPORT
QQuickFlickable::FlickableDirection ritual_ZNK15QQuickFlickable18flickableDirectionEv(
    const QQuickFlickable *self) {
  return self->flickableDirection();
}

//  void QQuickFlickable::setFlickableDirection(FlickableDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable21setFlickableDirectionENS_18FlickableDirectionE(
    QQuickFlickable *self,
    QQuickFlickable::FlickableDirection a0) {
  self->setFlickableDirection(a0);
}

//  bool QQuickFlickable::pixelAligned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable12pixelAlignedEv(
    const QQuickFlickable *self) {
  return self->pixelAligned();
}

//  void QQuickFlickable::setPixelAligned(bool align)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable15setPixelAlignedEb(
    QQuickFlickable *self,
    bool align) {
  self->setPixelAligned(align);
}

//  bool QQuickFlickable::synchronousDrag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable15synchronousDragEv(
    const QQuickFlickable *self) {
  return self->synchronousDrag();
}

//  void QQuickFlickable::setSynchronousDrag(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable18setSynchronousDragEb(
    QQuickFlickable *self,
    bool v) {
  self->setSynchronousDrag(v);
}

//  Qt::MouseButtons QQuickFlickable::acceptedButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickFlickable15acceptedButtonsEv(
    const QQuickFlickable *self) {
  return static_cast<int>(self->acceptedButtons().toInt());
}

//  void QQuickFlickable::setAcceptedButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable18setAcceptedButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QQuickFlickable *self,
    int buttons) {
  self->setAcceptedButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  qreal QQuickFlickable::horizontalOvershoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable19horizontalOvershootEv(
    const QQuickFlickable *self) {
  return self->horizontalOvershoot();
}

//  qreal QQuickFlickable::verticalOvershoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable17verticalOvershootEv(
    const QQuickFlickable *self) {
  return self->verticalOvershoot();
}

//  void QQuickFlickable::resizeContent(qreal w, qreal h, QPointF center)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable13resizeContentEdd7QPointF(
    QQuickFlickable *self,
    qreal w,
    qreal h,
    const QPointF *center) {
  self->resizeContent(w, h, *center);
}

//  void QQuickFlickable::returnToBounds()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14returnToBoundsEv(QQuickFlickable *self) {
  self->returnToBounds();
}

//  void QQuickFlickable::flick(qreal xVelocity, qreal yVelocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable5flickEdd(
    QQuickFlickable *self,
    qreal xVelocity,
    qreal yVelocity) {
  self->flick(xVelocity, yVelocity);
}

//  void QQuickFlickable::cancelFlick()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable11cancelFlickEv(QQuickFlickable *self) {
  self->cancelFlick();
}

//  void QQuickFlickable::positionViewAtChild(QQuickItem *child, PositionMode
//      mode, const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable19positionViewAtChildEP10QQuickItem6QFlagsINS_16PositionModeFlagEERK7QPointF(
    QQuickFlickable *self,
    QQuickItem *child,
    int mode,
    const QPointF *offset) {
  self->positionViewAtChild(
      child,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      *offset);
}

//  void QQuickFlickable::flickToChild(QQuickItem *child, PositionMode mode,
//      const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable12flickToChildEP10QQuickItem6QFlagsINS_16PositionModeFlagEERK7QPointF(
    QQuickFlickable *self,
    QQuickItem *child,
    int mode,
    const QPointF *offset) {
  self->flickToChild(
      child,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      *offset);
}

//  void QQuickFlickable::flickTo(const QPointF &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable7flickToERK7QPointF(
    QQuickFlickable *self,
    const QPointF *position) {
  self->flickTo(*position);
}

//  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickFlickable21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickFlickable *self,
    QQuickItem *a0,
    QEvent *a1) {
  return self->childMouseEventFilter(a0, a1);
}

//  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable15mousePressEventEP11QMouseEvent(
    QQuickFlickable *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14mouseMoveEventEP11QMouseEvent(
    QQuickFlickable *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable17mouseReleaseEventEP11QMouseEvent(
    QQuickFlickable *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickFlickable::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable10touchEventEP11QTouchEvent(
    QQuickFlickable *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickFlickable::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable10wheelEventEP11QWheelEvent(
    QQuickFlickable *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickFlickable::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable10timerEventEP11QTimerEvent(
    QQuickFlickable *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QQuickFlickableVisibleArea *QQuickFlickable::visibleArea()
extern "C" Q_DECL_EXPORT
QQuickFlickableVisibleArea *ritual_ZN15QQuickFlickable11visibleAreaEv(
    QQuickFlickable *self) {
  return self->visibleArea();
}

//  void QQuickFlickable::movementStarting()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable16movementStartingEv(QQuickFlickable *self) {
  self->movementStarting();
}

//  void QQuickFlickable::movementEnding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14movementEndingEv(QQuickFlickable *self) {
  self->movementEnding();
}

//  void QQuickFlickable::movementEnding(bool hMovementEnding, bool
//      vMovementEnding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14movementEndingEbb(
    QQuickFlickable *self,
    bool hMovementEnding,
    bool vMovementEnding) {
  self->movementEnding(hMovementEnding, vMovementEnding);
}

//  void QQuickFlickable::velocityTimelineCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable25velocityTimelineCompletedEv(
    QQuickFlickable *self) {
  self->velocityTimelineCompleted();
}

//  void QQuickFlickable::timelineCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable17timelineCompletedEv(QQuickFlickable *self) {
  self->timelineCompleted();
}

//  qreal QQuickFlickable::minXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable10minXExtentEv(
    const QQuickFlickable *self) {
  return self->minXExtent();
}

//  qreal QQuickFlickable::minYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable10minYExtentEv(
    const QQuickFlickable *self) {
  return self->minYExtent();
}

//  qreal QQuickFlickable::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable10maxXExtentEv(
    const QQuickFlickable *self) {
  return self->maxXExtent();
}

//  qreal QQuickFlickable::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable10maxYExtentEv(
    const QQuickFlickable *self) {
  return self->maxYExtent();
}

//  qreal QQuickFlickable::vWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable6vWidthEv(const QQuickFlickable *self) {
  return self->vWidth();
}

//  qreal QQuickFlickable::vHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickFlickable7vHeightEv(const QQuickFlickable *self) {
  return self->vHeight();
}

//  void QQuickFlickable::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable17componentCompleteEv(QQuickFlickable *self) {
  self->componentComplete();
}

//  void QQuickFlickable::viewportMoved(Qt::Orientations orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickFlickable *self,
    int orient) {
  self->viewportMoved(QFlags<Qt::Orientation>::fromInt(orient));
}

//  void QQuickFlickable::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable14geometryChangeERK6QRectFS2_(
    QQuickFlickable *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickFlickable::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickFlickable16mouseUngrabEventEv(QQuickFlickable *self) {
  self->mouseUngrabEvent();
}

//  bool QQuickFlickable::filterPointerEvent(QQuickItem *receiver,
//      QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickFlickable18filterPointerEventEP10QQuickItemP13QPointerEvent(
    QQuickFlickable *self,
    QQuickItem *receiver,
    QPointerEvent *event) {
  return self->filterPointerEvent(receiver, event);
}

//  bool QQuickFlickable::xflick() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable6xflickEv(const QQuickFlickable *self) {
  return self->xflick();
}

//  bool QQuickFlickable::yflick() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickFlickable6yflickEv(const QQuickFlickable *self) {
  return self->yflick();
}

//  QPointF QQuickFlickable::computePosition(QPointF currentPosition, QRectF
//      itemRect, PositionMode mode, const QPointF &offset) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QQuickFlickable15computePositionE7QPointF6QRectF6QFlagsINS_16PositionModeFlagEERKS0_(
    const QQuickFlickable *self,
    const QPointF *currentPosition,
    const QRectF *itemRect,
    int mode,
    const QPointF *offset) {
  return new QPointF(
      self->computePosition(
          *currentPosition,
          *itemRect,
          QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
          *offset));
}

//  QQuickFlickablePrivate *QQuickFlickable::d_func()
extern "C" Q_DECL_EXPORT
QQuickFlickablePrivate *ritual_ZN15QQuickFlickable6d_funcEv(
    QQuickFlickable *self) {
  return self->d_func();
}

//  const QQuickFlickablePrivate *QQuickFlickable::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFlickablePrivate *ritual_ZNK15QQuickFlickable6d_funcEv(
    const QQuickFlickable *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickFlickable, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFlickable(
    QQuickFlickable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFlickable *>(self)->take(key, call);
}

//  void QQuickFlickable::setContentX(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable11setContentXEd(
    QQuickFlickable *self,
    qreal pos) {
  self->QQuickFlickable::setContentX(pos);
}

//  void QQuickFlickable::setContentY(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable11setContentYEd(
    QQuickFlickable *self,
    qreal pos) {
  self->QQuickFlickable::setContentY(pos);
}

//  qreal QQuickFlickable::originY() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickFlickable7originYEv(
    const QQuickFlickable *self) {
  return self->QQuickFlickable::originY();
}

//  qreal QQuickFlickable::originX() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickFlickable7originXEv(
    const QQuickFlickable *self) {
  return self->QQuickFlickable::originX();
}

//  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickFlickable21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickFlickable *self,
    QQuickItem *a0,
    QEvent *a1) {
  return static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::childMouseEventFilter(
      a0,
      a1);
}

//  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable15mousePressEventEP11QMouseEvent(
    QQuickFlickable *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::mousePressEvent(
      event);
}

//  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable14mouseMoveEventEP11QMouseEvent(
    QQuickFlickable *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::mouseMoveEvent(
      event);
}

//  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable17mouseReleaseEventEP11QMouseEvent(
    QQuickFlickable *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::mouseReleaseEvent(
      event);
}

//  void QQuickFlickable::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable10touchEventEP11QTouchEvent(
    QQuickFlickable *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::touchEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickFlickable::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable10wheelEventEP11QWheelEvent(
    QQuickFlickable *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickFlickable::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable10timerEventEP11QTimerEvent(
    QQuickFlickable *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::timerEvent(
      event);
}

//  qreal QQuickFlickable::minXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickFlickable10minXExtentEv(
    const QQuickFlickable *self) {
  return static_cast<const OwnQQuickFlickable *>(self)->OwnQQuickFlickable::minXExtent();
}

//  qreal QQuickFlickable::minYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickFlickable10minYExtentEv(
    const QQuickFlickable *self) {
  return static_cast<const OwnQQuickFlickable *>(self)->OwnQQuickFlickable::minYExtent();
}

//  qreal QQuickFlickable::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickFlickable10maxXExtentEv(
    const QQuickFlickable *self) {
  return static_cast<const OwnQQuickFlickable *>(self)->OwnQQuickFlickable::maxXExtent();
}

//  qreal QQuickFlickable::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickFlickable10maxYExtentEv(
    const QQuickFlickable *self) {
  return static_cast<const OwnQQuickFlickable *>(self)->OwnQQuickFlickable::maxYExtent();
}

//  void QQuickFlickable::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable17componentCompleteEv(
    QQuickFlickable *self) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::componentComplete();
}

//  void QQuickFlickable::viewportMoved(Qt::Orientations orient)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickFlickable *self,
    int orient) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::viewportMoved(
      QFlags<Qt::Orientation>::fromInt(orient));
}

//  void QQuickFlickable::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable14geometryChangeERK6QRectFS2_(
    QQuickFlickable *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickFlickable::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickFlickable16mouseUngrabEventEv(
    QQuickFlickable *self) {
  static_cast<OwnQQuickFlickable *>(self)->OwnQQuickFlickable::mouseUngrabEvent();
}
