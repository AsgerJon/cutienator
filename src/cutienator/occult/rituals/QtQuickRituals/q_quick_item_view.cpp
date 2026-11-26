//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickItemView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItemView : QQuickItemView {
  using QQuickItemView::updatePolish;
  using QQuickItemView::componentComplete;
  using QQuickItemView::geometryChange;
  using QQuickItemView::minYExtent;
  using QQuickItemView::maxYExtent;
  using QQuickItemView::minXExtent;
  using QQuickItemView::maxXExtent;
  using QQuickItemView::initItem;
};

//  A QQuickItemView that Python can take functions over in. Every QQuickItemView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall1)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall2)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall3)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewCall5)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall6)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall8)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewCall9)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewCall10)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewCall12)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewCall13)(const void *, int, QObject *, int *);
#endif  // QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewCall14)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickItemViewCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemViewCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemViewCall18)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemViewCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall20)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall21)(const void *, int, int *);
typedef void (*CuteQQuickItemViewCall22)(const void *, int *);
typedef const QRectF * (*CuteQQuickItemViewCall23)(const void *, int *);
typedef const QRectF * (*CuteQQuickItemViewCall24)(const void *, int *);
typedef bool (*CuteQQuickItemViewCall25)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickItemViewCall26)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickItemViewCall27)(const void *, int *);
typedef void * (*CuteQQuickItemViewCall28)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemViewCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall30)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickItemViewCall31)(const void *, int *);
typedef void (*CuteQQuickItemViewCall32)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickItemViewCall33)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickItemViewCall34)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickItemViewCall35)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemViewCall36)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemViewCall37)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemViewCall38)(const void *, int *);
typedef void (*CuteQQuickItemViewCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemViewCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemViewCall41)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemViewCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemViewCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemViewCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemViewCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickItemViewCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickItemViewCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemViewCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickItemView : public QQuickItemView {
public:
  using QQuickItemView::QQuickItemView;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN14QQuickItemView24setHighlightMoveDurationEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentXEd")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentYEd")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originXEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originYEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minYExtentEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxYExtentEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minXExtentEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxXExtentEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN14QQuickItemView8initItemEiP7QObject")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[28] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[33] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
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
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setHighlightFollowsCurrentItem(bool a0)
  void setHighlightFollowsCurrentItem(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemViewCall0 call = reinterpret_cast<CuteQQuickItemViewCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemView::setHighlightFollowsCurrentItem(a0);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setHighlightMoveDuration(int a0)
  void setHighlightMoveDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemViewCall1 call = reinterpret_cast<CuteQQuickItemViewCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemView::setHighlightMoveDuration(a0);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setContentX(qreal pos)
  void setContentX(qreal pos) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemViewCall2 call = reinterpret_cast<CuteQQuickItemViewCall2>(taken[2]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickItemView::setContentX(pos);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemViewCall3 call = reinterpret_cast<CuteQQuickItemViewCall3>(taken[3]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickItemView::setContentY(pos);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::originX() const
  qreal originX() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemViewCall4 call = reinterpret_cast<CuteQQuickItemViewCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::originX();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::originY() const
  qreal originY() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemViewCall5 call = reinterpret_cast<CuteQQuickItemViewCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::originY();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemViewCall6 call = reinterpret_cast<CuteQQuickItemViewCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemView::updatePolish();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::componentComplete()
  void componentComplete() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemViewCall7 call = reinterpret_cast<CuteQQuickItemViewCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemView::componentComplete();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemViewCall8 call = reinterpret_cast<CuteQQuickItemViewCall8>(taken[8]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItemView::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::minYExtent() const
  qreal minYExtent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemViewCall9 call = reinterpret_cast<CuteQQuickItemViewCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::minYExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::maxYExtent() const
  qreal maxYExtent() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemViewCall10 call = reinterpret_cast<CuteQQuickItemViewCall10>(taken[10]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::maxYExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::minXExtent() const
  qreal minXExtent() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemViewCall11 call = reinterpret_cast<CuteQQuickItemViewCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::minXExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::maxXExtent() const
  qreal maxXExtent() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemViewCall12 call = reinterpret_cast<CuteQQuickItemViewCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::maxXExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::initItem(int index, QObject *item)
  void initItem(int index, QObject *item) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickItemViewCall13 call = reinterpret_cast<CuteQQuickItemViewCall13>(taken[13]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickItemView::initItem(index, item);
  }
#endif  // QT_CONFIG(quick_itemview)

  //  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemViewCall14 call = reinterpret_cast<CuteQQuickItemViewCall14>(taken[14]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemViewCall15 call = reinterpret_cast<CuteQQuickItemViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemViewCall16 call = reinterpret_cast<CuteQQuickItemViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemViewCall17 call = reinterpret_cast<CuteQQuickItemViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickItemViewCall18 call = reinterpret_cast<CuteQQuickItemViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::touchEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickFlickable::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemViewCall19 call = reinterpret_cast<CuteQQuickItemViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
  //  void QQuickFlickable::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickItemViewCall20 call = reinterpret_cast<CuteQQuickItemViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickFlickable::viewportMoved(Qt::Orientations orient)
  void viewportMoved(Qt::Orientations orient) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickItemViewCall21 call = reinterpret_cast<CuteQQuickItemViewCall21>(taken[21]);
      call(this, static_cast<int>(orient.toInt()), &handled);
      if (handled) return;
    }
    QQuickFlickable::viewportMoved(orient);
  }

  //  void QQuickFlickable::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickItemViewCall22 call = reinterpret_cast<CuteQQuickItemViewCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickItemViewCall23 call = reinterpret_cast<CuteQQuickItemViewCall23>(taken[23]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickItemViewCall24 call = reinterpret_cast<CuteQQuickItemViewCall24>(taken[24]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickItemViewCall25 call = reinterpret_cast<CuteQQuickItemViewCall25>(taken[25]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickItemViewCall26 call = reinterpret_cast<CuteQQuickItemViewCall26>(taken[26]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickItemViewCall27 call = reinterpret_cast<CuteQQuickItemViewCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickItemViewCall28 call = reinterpret_cast<CuteQQuickItemViewCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickItemViewCall29 call = reinterpret_cast<CuteQQuickItemViewCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickItemViewCall30 call = reinterpret_cast<CuteQQuickItemViewCall30>(taken[30]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickItemViewCall31 call = reinterpret_cast<CuteQQuickItemViewCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickItemViewCall32 call = reinterpret_cast<CuteQQuickItemViewCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickItemViewCall33 call = reinterpret_cast<CuteQQuickItemViewCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickItemViewCall34 call = reinterpret_cast<CuteQQuickItemViewCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickItemViewCall35 call = reinterpret_cast<CuteQQuickItemViewCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickItemViewCall36 call = reinterpret_cast<CuteQQuickItemViewCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickItemViewCall37 call = reinterpret_cast<CuteQQuickItemViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickItemViewCall38 call = reinterpret_cast<CuteQQuickItemViewCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickItemViewCall39 call = reinterpret_cast<CuteQQuickItemViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickItemViewCall40 call = reinterpret_cast<CuteQQuickItemViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickItemViewCall41 call = reinterpret_cast<CuteQQuickItemViewCall41>(taken[41]);
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
      CuteQQuickItemViewCall42 call = reinterpret_cast<CuteQQuickItemViewCall42>(taken[42]);
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
      CuteQQuickItemViewCall43 call = reinterpret_cast<CuteQQuickItemViewCall43>(taken[43]);
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
      CuteQQuickItemViewCall44 call = reinterpret_cast<CuteQQuickItemViewCall44>(taken[44]);
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
      CuteQQuickItemViewCall45 call = reinterpret_cast<CuteQQuickItemViewCall45>(taken[45]);
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
    if (taken[46]) {
      int handled = 0;
      CuteQQuickItemViewCall46 call = reinterpret_cast<CuteQQuickItemViewCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickItemViewCall47 call = reinterpret_cast<CuteQQuickItemViewCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickItemViewCall48 call = reinterpret_cast<CuteQQuickItemViewCall48>(taken[48]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickItemViewCall49 call = reinterpret_cast<CuteQQuickItemViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickItemViewCall50 call = reinterpret_cast<CuteQQuickItemViewCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickItemViewCall51 call = reinterpret_cast<CuteQQuickItemViewCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickItemViewCall52 call = reinterpret_cast<CuteQQuickItemViewCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickItemView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickItemView10metaObjectEv(
    const QQuickItemView *self) {
  return self->metaObject();
}

//  void *QQuickItemView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickItemView11qt_metacastEPKc(
    QQuickItemView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickItemView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickItemView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickItemView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickItemView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickItemView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemView::tr(s, c, n));
}

//  void QQuickItemView::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView24qt_qmlMarker_uncreatableEv(
    QQuickItemView *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickItemView::QQuickItemView(QQuickFlickablePrivate &dd, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickItemView *ritual_ZN14QQuickItemViewC1ER22QQuickFlickablePrivateP10QQuickItem(
    QQuickFlickablePrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickItemView(*dd, parent);
}

//  QQuickItemView::~QQuickItemView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemViewD1Ev(QQuickItemView *self) {
  delete self;
}

//  QVariant QQuickItemView::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickItemView5modelEv(const QQuickItemView *self) {
  return new QVariant(self->model());
}

//  void QQuickItemView::setModel(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView8setModelERK8QVariant(
    QQuickItemView *self,
    const QVariant *a0) {
  self->setModel(*a0);
}

//  QQmlComponent *QQuickItemView::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickItemView8delegateEv(
    const QQuickItemView *self) {
  return self->delegate();
}

//  void QQuickItemView::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView11setDelegateEP13QQmlComponent(
    QQuickItemView *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  int QQuickItemView::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView5countEv(const QQuickItemView *self) {
  return self->count();
}

//  int QQuickItemView::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView12currentIndexEv(const QQuickItemView *self) {
  return self->currentIndex();
}

//  void QQuickItemView::setCurrentIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView15setCurrentIndexEi(
    QQuickItemView *self,
    int idx) {
  self->setCurrentIndex(idx);
}

//  QQuickItem *QQuickItemView::currentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickItemView11currentItemEv(
    const QQuickItemView *self) {
  return self->currentItem();
}

//  bool QQuickItemView::isWrapEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickItemView13isWrapEnabledEv(
    const QQuickItemView *self) {
  return self->isWrapEnabled();
}

//  void QQuickItemView::setWrapEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView14setWrapEnabledEb(
    QQuickItemView *self,
    bool a0) {
  self->setWrapEnabled(a0);
}

//  bool QQuickItemView::isKeyNavigationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickItemView22isKeyNavigationEnabledEv(
    const QQuickItemView *self) {
  return self->isKeyNavigationEnabled();
}

//  void QQuickItemView::setKeyNavigationEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView23setKeyNavigationEnabledEb(
    QQuickItemView *self,
    bool a0) {
  self->setKeyNavigationEnabled(a0);
}

//  int QQuickItemView::cacheBuffer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView11cacheBufferEv(const QQuickItemView *self) {
  return self->cacheBuffer();
}

//  void QQuickItemView::setCacheBuffer(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView14setCacheBufferEi(
    QQuickItemView *self,
    int a0) {
  self->setCacheBuffer(a0);
}

//  int QQuickItemView::displayMarginBeginning() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView22displayMarginBeginningEv(
    const QQuickItemView *self) {
  return self->displayMarginBeginning();
}

//  void QQuickItemView::setDisplayMarginBeginning(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView25setDisplayMarginBeginningEi(
    QQuickItemView *self,
    int a0) {
  self->setDisplayMarginBeginning(a0);
}

//  int QQuickItemView::displayMarginEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView16displayMarginEndEv(
    const QQuickItemView *self) {
  return self->displayMarginEnd();
}

//  void QQuickItemView::setDisplayMarginEnd(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView19setDisplayMarginEndEi(
    QQuickItemView *self,
    int a0) {
  self->setDisplayMarginEnd(a0);
}

//  Qt::LayoutDirection QQuickItemView::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK14QQuickItemView15layoutDirectionEv(
    const QQuickItemView *self) {
  return self->layoutDirection();
}

//  void QQuickItemView::setLayoutDirection(Qt::LayoutDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QQuickItemView *self,
    Qt::LayoutDirection a0) {
  self->setLayoutDirection(a0);
}

//  Qt::LayoutDirection QQuickItemView::effectiveLayoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK14QQuickItemView24effectiveLayoutDirectionEv(
    const QQuickItemView *self) {
  return self->effectiveLayoutDirection();
}

//  VerticalLayoutDirection QQuickItemView::verticalLayoutDirection() const
extern "C" Q_DECL_EXPORT
QQuickItemView::VerticalLayoutDirection ritual_ZNK14QQuickItemView23verticalLayoutDirectionEv(
    const QQuickItemView *self) {
  return self->verticalLayoutDirection();
}

//  void QQuickItemView::setVerticalLayoutDirection(VerticalLayoutDirection
//      layoutDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView26setVerticalLayoutDirectionENS_23VerticalLayoutDirectionE(
    QQuickItemView *self,
    QQuickItemView::VerticalLayoutDirection layoutDirection) {
  self->setVerticalLayoutDirection(layoutDirection);
}

//  QQmlComponent *QQuickItemView::footer() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickItemView6footerEv(
    const QQuickItemView *self) {
  return self->footer();
}

//  void QQuickItemView::setFooter(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView9setFooterEP13QQmlComponent(
    QQuickItemView *self,
    QQmlComponent *a0) {
  self->setFooter(a0);
}

//  QQuickItem *QQuickItemView::footerItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickItemView10footerItemEv(
    const QQuickItemView *self) {
  return self->footerItem();
}

//  QQmlComponent *QQuickItemView::header() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickItemView6headerEv(
    const QQuickItemView *self) {
  return self->header();
}

//  void QQuickItemView::setHeader(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView9setHeaderEP13QQmlComponent(
    QQuickItemView *self,
    QQmlComponent *a0) {
  self->setHeader(a0);
}

//  QQuickItem *QQuickItemView::headerItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickItemView10headerItemEv(
    const QQuickItemView *self) {
  return self->headerItem();
}

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::populateTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView18populateTransitionEv(
    const QQuickItemView *self) {
  return self->populateTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setPopulateTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView21setPopulateTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setPopulateTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::addTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView13addTransitionEv(
    const QQuickItemView *self) {
  return self->addTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setAddTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView16setAddTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setAddTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::addDisplacedTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView22addDisplacedTransitionEv(
    const QQuickItemView *self) {
  return self->addDisplacedTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setAddDisplacedTransition(QQuickTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView25setAddDisplacedTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setAddDisplacedTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::moveTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView14moveTransitionEv(
    const QQuickItemView *self) {
  return self->moveTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setMoveTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView17setMoveTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setMoveTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::moveDisplacedTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView23moveDisplacedTransitionEv(
    const QQuickItemView *self) {
  return self->moveDisplacedTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setMoveDisplacedTransition(QQuickTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView26setMoveDisplacedTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setMoveDisplacedTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::removeTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView16removeTransitionEv(
    const QQuickItemView *self) {
  return self->removeTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setRemoveTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView19setRemoveTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setRemoveTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::removeDisplacedTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView25removeDisplacedTransitionEv(
    const QQuickItemView *self) {
  return self->removeDisplacedTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setRemoveDisplacedTransition(QQuickTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView28setRemoveDisplacedTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setRemoveDisplacedTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickItemView::displacedTransition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK14QQuickItemView19displacedTransitionEv(
    const QQuickItemView *self) {
  return self->displacedTransition();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::setDisplacedTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView22setDisplacedTransitionEP16QQuickTransition(
    QQuickItemView *self,
    QQuickTransition *transition) {
  self->setDisplacedTransition(transition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  QQmlComponent *QQuickItemView::highlight() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickItemView9highlightEv(
    const QQuickItemView *self) {
  return self->highlight();
}

//  void QQuickItemView::setHighlight(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12setHighlightEP13QQmlComponent(
    QQuickItemView *self,
    QQmlComponent *a0) {
  self->setHighlight(a0);
}

//  QQuickItem *QQuickItemView::highlightItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickItemView13highlightItemEv(
    const QQuickItemView *self) {
  return self->highlightItem();
}

//  bool QQuickItemView::highlightFollowsCurrentItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickItemView27highlightFollowsCurrentItemEv(
    const QQuickItemView *self) {
  return self->highlightFollowsCurrentItem();
}

//  void QQuickItemView::setHighlightFollowsCurrentItem(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb(
    QQuickItemView *self,
    bool a0) {
  self->setHighlightFollowsCurrentItem(a0);
}

//  HighlightRangeMode QQuickItemView::highlightRangeMode() const
extern "C" Q_DECL_EXPORT
QQuickItemView::HighlightRangeMode ritual_ZNK14QQuickItemView18highlightRangeModeEv(
    const QQuickItemView *self) {
  return self->highlightRangeMode();
}

//  void QQuickItemView::setHighlightRangeMode(HighlightRangeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView21setHighlightRangeModeENS_18HighlightRangeModeE(
    QQuickItemView *self,
    QQuickItemView::HighlightRangeMode mode) {
  self->setHighlightRangeMode(mode);
}

//  qreal QQuickItemView::preferredHighlightBegin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView23preferredHighlightBeginEv(
    const QQuickItemView *self) {
  return self->preferredHighlightBegin();
}

//  void QQuickItemView::setPreferredHighlightBegin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView26setPreferredHighlightBeginEd(
    QQuickItemView *self,
    qreal a0) {
  self->setPreferredHighlightBegin(a0);
}

//  void QQuickItemView::resetPreferredHighlightBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView28resetPreferredHighlightBeginEv(
    QQuickItemView *self) {
  self->resetPreferredHighlightBegin();
}

//  qreal QQuickItemView::preferredHighlightEnd() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView21preferredHighlightEndEv(
    const QQuickItemView *self) {
  return self->preferredHighlightEnd();
}

//  void QQuickItemView::setPreferredHighlightEnd(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView24setPreferredHighlightEndEd(
    QQuickItemView *self,
    qreal a0) {
  self->setPreferredHighlightEnd(a0);
}

//  void QQuickItemView::resetPreferredHighlightEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView26resetPreferredHighlightEndEv(
    QQuickItemView *self) {
  self->resetPreferredHighlightEnd();
}

//  int QQuickItemView::highlightMoveDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView21highlightMoveDurationEv(
    const QQuickItemView *self) {
  return self->highlightMoveDuration();
}

//  void QQuickItemView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView24setHighlightMoveDurationEi(
    QQuickItemView *self,
    int a0) {
  self->setHighlightMoveDuration(a0);
}

//  bool QQuickItemView::reuseItems() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickItemView10reuseItemsEv(const QQuickItemView *self) {
  return self->reuseItems();
}

//  void QQuickItemView::setReuseItems(bool reuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView13setReuseItemsEb(
    QQuickItemView *self,
    bool reuse) {
  self->setReuseItems(reuse);
}

//  void QQuickItemView::positionViewAtIndex(int index, int mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView19positionViewAtIndexEii(
    QQuickItemView *self,
    int index,
    int mode) {
  self->positionViewAtIndex(index, mode);
}

//  int QQuickItemView::indexAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickItemView7indexAtEdd(
    const QQuickItemView *self,
    qreal x,
    qreal y) {
  return self->indexAt(x, y);
}

//  QQuickItem *QQuickItemView::itemAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickItemView6itemAtEdd(
    const QQuickItemView *self,
    qreal x,
    qreal y) {
  return self->itemAt(x, y);
}

//  QQuickItem *QQuickItemView::itemAtIndex(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickItemView11itemAtIndexEi(
    const QQuickItemView *self,
    int index) {
  return self->itemAtIndex(index);
}

//  void QQuickItemView::positionViewAtBeginning()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView23positionViewAtBeginningEv(
    QQuickItemView *self) {
  self->positionViewAtBeginning();
}

//  void QQuickItemView::positionViewAtEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView17positionViewAtEndEv(QQuickItemView *self) {
  self->positionViewAtEnd();
}

//  void QQuickItemView::forceLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView11forceLayoutEv(QQuickItemView *self) {
  self->forceLayout();
}

//  void QQuickItemView::setContentX(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView11setContentXEd(
    QQuickItemView *self,
    qreal pos) {
  self->setContentX(pos);
}

//  void QQuickItemView::setContentY(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView11setContentYEd(
    QQuickItemView *self,
    qreal pos) {
  self->setContentY(pos);
}

//  qreal QQuickItemView::originX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView7originXEv(const QQuickItemView *self) {
  return self->originX();
}

//  qreal QQuickItemView::originY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView7originYEv(const QQuickItemView *self) {
  return self->originY();
}

//  QQmlDelegateModel::DelegateModelAccess
//      QQuickItemView::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK14QQuickItemView19delegateModelAccessEv(
    const QQuickItemView *self) {
  return self->delegateModelAccess();
}

//  void QQuickItemView::setDelegateModelAccess(QQmlDelegateModel::DelegateMo
//      delAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QQuickItemView *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  void QQuickItemView::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12modelChangedEv(QQuickItemView *self) {
  self->modelChanged();
}

//  void QQuickItemView::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView15delegateChangedEv(QQuickItemView *self) {
  self->delegateChanged();
}

//  void QQuickItemView::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12countChangedEv(QQuickItemView *self) {
  self->countChanged();
}

//  void QQuickItemView::currentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView19currentIndexChangedEv(QQuickItemView *self) {
  self->currentIndexChanged();
}

//  void QQuickItemView::currentItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView18currentItemChangedEv(QQuickItemView *self) {
  self->currentItemChanged();
}

//  void QQuickItemView::keyNavigationWrapsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView25keyNavigationWrapsChangedEv(
    QQuickItemView *self) {
  self->keyNavigationWrapsChanged();
}

//  void QQuickItemView::keyNavigationEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView27keyNavigationEnabledChangedEv(
    QQuickItemView *self) {
  self->keyNavigationEnabledChanged();
}

//  void QQuickItemView::cacheBufferChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView18cacheBufferChangedEv(QQuickItemView *self) {
  self->cacheBufferChanged();
}

//  void QQuickItemView::displayMarginBeginningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView29displayMarginBeginningChangedEv(
    QQuickItemView *self) {
  self->displayMarginBeginningChanged();
}

//  void QQuickItemView::displayMarginEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView23displayMarginEndChangedEv(
    QQuickItemView *self) {
  self->displayMarginEndChanged();
}

//  void QQuickItemView::layoutDirectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView22layoutDirectionChangedEv(
    QQuickItemView *self) {
  self->layoutDirectionChanged();
}

//  void QQuickItemView::effectiveLayoutDirectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView31effectiveLayoutDirectionChangedEv(
    QQuickItemView *self) {
  self->effectiveLayoutDirectionChanged();
}

//  void QQuickItemView::verticalLayoutDirectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView30verticalLayoutDirectionChangedEv(
    QQuickItemView *self) {
  self->verticalLayoutDirectionChanged();
}

//  void QQuickItemView::headerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView13headerChangedEv(QQuickItemView *self) {
  self->headerChanged();
}

//  void QQuickItemView::footerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView13footerChangedEv(QQuickItemView *self) {
  self->footerChanged();
}

//  void QQuickItemView::headerItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView17headerItemChangedEv(QQuickItemView *self) {
  self->headerItemChanged();
}

//  void QQuickItemView::footerItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView17footerItemChangedEv(QQuickItemView *self) {
  self->footerItemChanged();
}

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::populateTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView25populateTransitionChangedEv(
    QQuickItemView *self) {
  self->populateTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::addTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView20addTransitionChangedEv(
    QQuickItemView *self) {
  self->addTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::addDisplacedTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView29addDisplacedTransitionChangedEv(
    QQuickItemView *self) {
  self->addDisplacedTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::moveTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView21moveTransitionChangedEv(
    QQuickItemView *self) {
  self->moveTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::moveDisplacedTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView30moveDisplacedTransitionChangedEv(
    QQuickItemView *self) {
  self->moveDisplacedTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::removeTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView23removeTransitionChangedEv(
    QQuickItemView *self) {
  self->removeTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::removeDisplacedTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView32removeDisplacedTransitionChangedEv(
    QQuickItemView *self) {
  self->removeDisplacedTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemView::displacedTransitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView26displacedTransitionChangedEv(
    QQuickItemView *self) {
  self->displacedTransitionChanged();
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  void QQuickItemView::highlightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView16highlightChangedEv(QQuickItemView *self) {
  self->highlightChanged();
}

//  void QQuickItemView::highlightItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView20highlightItemChangedEv(
    QQuickItemView *self) {
  self->highlightItemChanged();
}

//  void QQuickItemView::highlightFollowsCurrentItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView34highlightFollowsCurrentItemChangedEv(
    QQuickItemView *self) {
  self->highlightFollowsCurrentItemChanged();
}

//  void QQuickItemView::highlightRangeModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView25highlightRangeModeChangedEv(
    QQuickItemView *self) {
  self->highlightRangeModeChanged();
}

//  void QQuickItemView::preferredHighlightBeginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView30preferredHighlightBeginChangedEv(
    QQuickItemView *self) {
  self->preferredHighlightBeginChanged();
}

//  void QQuickItemView::preferredHighlightEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView28preferredHighlightEndChangedEv(
    QQuickItemView *self) {
  self->preferredHighlightEndChanged();
}

//  void QQuickItemView::highlightMoveDurationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView28highlightMoveDurationChangedEv(
    QQuickItemView *self) {
  self->highlightMoveDurationChanged();
}

//  void QQuickItemView::reuseItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView17reuseItemsChangedEv(QQuickItemView *self) {
  self->reuseItemsChanged();
}

//  void QQuickItemView::delegateModelAccessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView26delegateModelAccessChangedEv(
    QQuickItemView *self) {
  self->delegateModelAccessChanged();
}

//  void QQuickItemView::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12updatePolishEv(QQuickItemView *self) {
  self->updatePolish();
}

//  void QQuickItemView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView17componentCompleteEv(QQuickItemView *self) {
  self->componentComplete();
}

//  void QQuickItemView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView14geometryChangeERK6QRectFS2_(
    QQuickItemView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  qreal QQuickItemView::minYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView10minYExtentEv(const QQuickItemView *self) {
  return self->minYExtent();
}

//  qreal QQuickItemView::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView10maxYExtentEv(const QQuickItemView *self) {
  return self->maxYExtent();
}

//  qreal QQuickItemView::minXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView10minXExtentEv(const QQuickItemView *self) {
  return self->minXExtent();
}

//  qreal QQuickItemView::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickItemView10maxXExtentEv(const QQuickItemView *self) {
  return self->maxXExtent();
}

//  void QQuickItemView::destroyRemoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView14destroyRemovedEv(QQuickItemView *self) {
  self->destroyRemoved();
}

//  void QQuickItemView::createdItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView11createdItemEiP7QObject(
    QQuickItemView *self,
    int index,
    QObject *item) {
  self->createdItem(index, item);
}

//  void QQuickItemView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView8initItemEiP7QObject(
    QQuickItemView *self,
    int index,
    QObject *item) {
  self->initItem(index, item);
}

//  void QQuickItemView::modelUpdated(const QQmlChangeSet &changeSet, bool
//      reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12modelUpdatedERK13QQmlChangeSetb(
    QQuickItemView *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->modelUpdated(*changeSet, reset);
}

//  void QQuickItemView::destroyingItem(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView14destroyingItemEP7QObject(
    QQuickItemView *self,
    QObject *item) {
  self->destroyingItem(item);
}

//  void QQuickItemView::onItemPooled(int modelIndex, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12onItemPooledEiP7QObject(
    QQuickItemView *self,
    int modelIndex,
    QObject *object) {
  self->onItemPooled(modelIndex, object);
}

//  void QQuickItemView::onItemReused(int modelIndex, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView12onItemReusedEiP7QObject(
    QQuickItemView *self,
    int modelIndex,
    QObject *object) {
  self->onItemReused(modelIndex, object);
}

//  void QQuickItemView::animStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView11animStoppedEv(QQuickItemView *self) {
  self->animStopped();
}

//  void QQuickItemView::trackedPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickItemView22trackedPositionChangedEv(
    QQuickItemView *self) {
  self->trackedPositionChanged();
}

//  QQuickItemViewPrivate *QQuickItemView::d_func()
extern "C" Q_DECL_EXPORT
QQuickItemViewPrivate *ritual_ZN14QQuickItemView6d_funcEv(
    QQuickItemView *self) {
  return self->d_func();
}

//  const QQuickItemViewPrivate *QQuickItemView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickItemViewPrivate *ritual_ZNK14QQuickItemView6d_funcEv(
    const QQuickItemView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickItemView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemView(
    QQuickItemView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemView *>(self)->take(key, call);
}

//  void QQuickItemView::setHighlightFollowsCurrentItem(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb(
    QQuickItemView *self,
    bool a0) {
  self->QQuickItemView::setHighlightFollowsCurrentItem(a0);
}

//  void QQuickItemView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView24setHighlightMoveDurationEi(
    QQuickItemView *self,
    int a0) {
  self->QQuickItemView::setHighlightMoveDuration(a0);
}

//  void QQuickItemView::setContentX(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView11setContentXEd(
    QQuickItemView *self,
    qreal pos) {
  self->QQuickItemView::setContentX(pos);
}

//  void QQuickItemView::setContentY(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView11setContentYEd(
    QQuickItemView *self,
    qreal pos) {
  self->QQuickItemView::setContentY(pos);
}

//  qreal QQuickItemView::originX() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickItemView7originXEv(const QQuickItemView *self) {
  return self->QQuickItemView::originX();
}

//  qreal QQuickItemView::originY() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickItemView7originYEv(const QQuickItemView *self) {
  return self->QQuickItemView::originY();
}

//  void QQuickItemView::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView12updatePolishEv(QQuickItemView *self) {
  static_cast<OwnQQuickItemView *>(self)->OwnQQuickItemView::updatePolish();
}

//  void QQuickItemView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView17componentCompleteEv(
    QQuickItemView *self) {
  static_cast<OwnQQuickItemView *>(self)->OwnQQuickItemView::componentComplete();
}

//  void QQuickItemView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView14geometryChangeERK6QRectFS2_(
    QQuickItemView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickItemView *>(self)->OwnQQuickItemView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  qreal QQuickItemView::minYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickItemView10minYExtentEv(
    const QQuickItemView *self) {
  return static_cast<const OwnQQuickItemView *>(self)->OwnQQuickItemView::minYExtent();
}

//  qreal QQuickItemView::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickItemView10maxYExtentEv(
    const QQuickItemView *self) {
  return static_cast<const OwnQQuickItemView *>(self)->OwnQQuickItemView::maxYExtent();
}

//  qreal QQuickItemView::minXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickItemView10minXExtentEv(
    const QQuickItemView *self) {
  return static_cast<const OwnQQuickItemView *>(self)->OwnQQuickItemView::minXExtent();
}

//  qreal QQuickItemView::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickItemView10maxXExtentEv(
    const QQuickItemView *self) {
  return static_cast<const OwnQQuickItemView *>(self)->OwnQQuickItemView::maxXExtent();
}

//  void QQuickItemView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickItemView8initItemEiP7QObject(
    QQuickItemView *self,
    int index,
    QObject *item) {
  static_cast<OwnQQuickItemView *>(self)->OwnQQuickItemView::initItem(
      index,
      item);
}

#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_itemview)
