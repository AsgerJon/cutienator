//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickgridview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_gridview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickgridview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickGridView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGridView : QQuickGridView {
  using QQuickGridView::viewportMoved;
  using QQuickGridView::keyPressEvent;
  using QQuickGridView::geometryChange;
  using QQuickGridView::initItem;
};

//  A QQuickGridView that Python can take functions over in. Every QQuickGridView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
typedef void (*CuteQQuickGridViewCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
typedef void (*CuteQQuickGridViewCall1)(const void *, int, int *);
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
typedef void (*CuteQQuickGridViewCall2)(const void *, int, int *);
#endif  // QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_gridview)
typedef void (*CuteQQuickGridViewCall3)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_gridview)
typedef void (*CuteQQuickGridViewCall4)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
typedef void (*CuteQQuickGridViewCall5)(const void *, int, QObject *, int *);
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickGridViewCall6)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickGridViewCall7)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickGridViewCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickGridViewCall9)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickGridViewCall10)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickGridViewCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickGridViewCall12)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickGridViewCall13)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickGridViewCall14)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickGridViewCall15)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickGridViewCall16)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickGridViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGridViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGridViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGridViewCall20)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGridViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall23)(const void *, int *);
typedef const QRectF * (*CuteQQuickGridViewCall24)(const void *, int *);
typedef const QRectF * (*CuteQQuickGridViewCall25)(const void *, int *);
typedef bool (*CuteQQuickGridViewCall26)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickGridViewCall27)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickGridViewCall28)(const void *, int *);
typedef void * (*CuteQQuickGridViewCall29)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGridViewCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall31)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickGridViewCall32)(const void *, int *);
typedef void (*CuteQQuickGridViewCall33)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickGridViewCall34)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGridViewCall35)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGridViewCall36)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGridViewCall37)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGridViewCall38)(const void *, int *);
typedef void (*CuteQQuickGridViewCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGridViewCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGridViewCall41)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGridViewCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGridViewCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGridViewCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGridViewCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickGridViewCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickGridViewCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGridViewCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGridViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGridView : public QQuickGridView {
public:
  using QQuickGridView::QQuickGridView;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
    if (!std::strcmp(key, "_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
    if (!std::strcmp(key, "_ZN14QQuickItemView24setHighlightMoveDurationEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_gridview)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_gridview)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_gridview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
    if (!std::strcmp(key, "_ZN14QQuickItemView8initItemEiP7QObject")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentXEd")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentYEd")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originXEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originYEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minYExtentEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxYExtentEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minXExtentEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxXExtentEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[29] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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
#if QT_CONFIG(quick_gridview)
  //  void QQuickGridView::setHighlightFollowsCurrentItem(bool a0)
  void setHighlightFollowsCurrentItem(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGridViewCall0 call = reinterpret_cast<CuteQQuickGridViewCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickGridView::setHighlightFollowsCurrentItem(a0);
  }
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
  //  void QQuickGridView::setHighlightMoveDuration(int a0)
  void setHighlightMoveDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGridViewCall1 call = reinterpret_cast<CuteQQuickGridViewCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickGridView::setHighlightMoveDuration(a0);
  }
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_gridview)
  //  void QQuickGridView::viewportMoved(Qt::Orientations a0)
  void viewportMoved(Qt::Orientations a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGridViewCall2 call = reinterpret_cast<CuteQQuickGridViewCall2>(taken[2]);
      call(this, static_cast<int>(a0.toInt()), &handled);
      if (handled) return;
    }
    QQuickGridView::viewportMoved(a0);
  }
#endif  // QT_CONFIG(quick_gridview)

#if QT_CONFIG(quick_gridview)
  //  void QQuickGridView::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGridViewCall3 call = reinterpret_cast<CuteQQuickGridViewCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickGridView::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(quick_gridview)

#if QT_CONFIG(quick_gridview)
  //  void QQuickGridView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGridViewCall4 call = reinterpret_cast<CuteQQuickGridViewCall4>(taken[4]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickGridView::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_gridview)

#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_gridview)
  //  void QQuickGridView::initItem(int index, QObject *item)
  void initItem(int index, QObject *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGridViewCall5 call = reinterpret_cast<CuteQQuickGridViewCall5>(taken[5]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickGridView::initItem(index, item);
  }
#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setContentX(qreal pos)
  void setContentX(qreal pos) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGridViewCall6 call = reinterpret_cast<CuteQQuickGridViewCall6>(taken[6]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickItemView::setContentX(pos);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGridViewCall7 call = reinterpret_cast<CuteQQuickGridViewCall7>(taken[7]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickItemView::setContentY(pos);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::originX() const
  qreal originX() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGridViewCall8 call = reinterpret_cast<CuteQQuickGridViewCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::originX();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::originY() const
  qreal originY() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGridViewCall9 call = reinterpret_cast<CuteQQuickGridViewCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::originY();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::updatePolish()
  void updatePolish() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGridViewCall10 call = reinterpret_cast<CuteQQuickGridViewCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemView::updatePolish();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGridViewCall11 call = reinterpret_cast<CuteQQuickGridViewCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemView::componentComplete();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::minYExtent() const
  qreal minYExtent() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGridViewCall12 call = reinterpret_cast<CuteQQuickGridViewCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::minYExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::maxYExtent() const
  qreal maxYExtent() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGridViewCall13 call = reinterpret_cast<CuteQQuickGridViewCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::maxYExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::minXExtent() const
  qreal minXExtent() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGridViewCall14 call = reinterpret_cast<CuteQQuickGridViewCall14>(taken[14]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::minXExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::maxXExtent() const
  qreal maxXExtent() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGridViewCall15 call = reinterpret_cast<CuteQQuickGridViewCall15>(taken[15]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::maxXExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

  //  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGridViewCall16 call = reinterpret_cast<CuteQQuickGridViewCall16>(taken[16]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGridViewCall17 call = reinterpret_cast<CuteQQuickGridViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGridViewCall18 call = reinterpret_cast<CuteQQuickGridViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickGridViewCall19 call = reinterpret_cast<CuteQQuickGridViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickGridViewCall20 call = reinterpret_cast<CuteQQuickGridViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::touchEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickFlickable::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickGridViewCall21 call = reinterpret_cast<CuteQQuickGridViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
  //  void QQuickFlickable::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGridViewCall22 call = reinterpret_cast<CuteQQuickGridViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickFlickable::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGridViewCall23 call = reinterpret_cast<CuteQQuickGridViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGridViewCall24 call = reinterpret_cast<CuteQQuickGridViewCall24>(taken[24]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickGridViewCall25 call = reinterpret_cast<CuteQQuickGridViewCall25>(taken[25]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickGridViewCall26 call = reinterpret_cast<CuteQQuickGridViewCall26>(taken[26]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickGridViewCall27 call = reinterpret_cast<CuteQQuickGridViewCall27>(taken[27]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGridViewCall28 call = reinterpret_cast<CuteQQuickGridViewCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickGridViewCall29 call = reinterpret_cast<CuteQQuickGridViewCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickGridViewCall30 call = reinterpret_cast<CuteQQuickGridViewCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQQuickGridViewCall31 call = reinterpret_cast<CuteQQuickGridViewCall31>(taken[31]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickGridViewCall32 call = reinterpret_cast<CuteQQuickGridViewCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickGridViewCall33 call = reinterpret_cast<CuteQQuickGridViewCall33>(taken[33]);
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
      CuteQQuickGridViewCall34 call = reinterpret_cast<CuteQQuickGridViewCall34>(taken[34]);
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
      CuteQQuickGridViewCall35 call = reinterpret_cast<CuteQQuickGridViewCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickGridViewCall36 call = reinterpret_cast<CuteQQuickGridViewCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickGridViewCall37 call = reinterpret_cast<CuteQQuickGridViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickGridViewCall38 call = reinterpret_cast<CuteQQuickGridViewCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickGridViewCall39 call = reinterpret_cast<CuteQQuickGridViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickGridViewCall40 call = reinterpret_cast<CuteQQuickGridViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickGridViewCall41 call = reinterpret_cast<CuteQQuickGridViewCall41>(taken[41]);
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
      CuteQQuickGridViewCall42 call = reinterpret_cast<CuteQQuickGridViewCall42>(taken[42]);
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
      CuteQQuickGridViewCall43 call = reinterpret_cast<CuteQQuickGridViewCall43>(taken[43]);
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
      CuteQQuickGridViewCall44 call = reinterpret_cast<CuteQQuickGridViewCall44>(taken[44]);
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
      CuteQQuickGridViewCall45 call = reinterpret_cast<CuteQQuickGridViewCall45>(taken[45]);
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
      CuteQQuickGridViewCall46 call = reinterpret_cast<CuteQQuickGridViewCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickGridViewCall47 call = reinterpret_cast<CuteQQuickGridViewCall47>(taken[47]);
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
      CuteQQuickGridViewCall48 call = reinterpret_cast<CuteQQuickGridViewCall48>(taken[48]);
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
      CuteQQuickGridViewCall49 call = reinterpret_cast<CuteQQuickGridViewCall49>(taken[49]);
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
      CuteQQuickGridViewCall50 call = reinterpret_cast<CuteQQuickGridViewCall50>(taken[50]);
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
      CuteQQuickGridViewCall51 call = reinterpret_cast<CuteQQuickGridViewCall51>(taken[51]);
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
      CuteQQuickGridViewCall52 call = reinterpret_cast<CuteQQuickGridViewCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGridView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickGridView10metaObjectEv(
    const QQuickGridView *self) {
  return self->metaObject();
}

//  void *QQuickGridView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickGridView11qt_metacastEPKc(
    QQuickGridView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGridView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickGridView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGridView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGridView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickGridView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGridView::tr(s, c, n));
}

//  QQuickGridViewPrivate *QQuickGridView::d_func()
extern "C" Q_DECL_EXPORT
QQuickGridViewPrivate *ritual_ZN14QQuickGridView6d_funcEv(
    QQuickGridView *self) {
  return self->d_func();
}

//  const QQuickGridViewPrivate *QQuickGridView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickGridViewPrivate *ritual_ZNK14QQuickGridView6d_funcEv(
    const QQuickGridView *self) {
  return self->d_func();
}

//  void QQuickGridView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView21qt_qmlMarker_attachedEv(
    QQuickGridView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickGridView::QQuickGridView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGridView *ritual_ZN14QQuickGridViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickGridView(parent);
}

//  void QQuickGridView::setHighlightFollowsCurrentItem(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView30setHighlightFollowsCurrentItemEb(
    QQuickGridView *self,
    bool a0) {
  self->setHighlightFollowsCurrentItem(a0);
}

//  void QQuickGridView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView24setHighlightMoveDurationEi(
    QQuickGridView *self,
    int a0) {
  self->setHighlightMoveDuration(a0);
}

//  Flow QQuickGridView::flow() const
extern "C" Q_DECL_EXPORT
QQuickGridView::Flow ritual_ZNK14QQuickGridView4flowEv(
    const QQuickGridView *self) {
  return self->flow();
}

//  void QQuickGridView::setFlow(Flow a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView7setFlowENS_4FlowE(
    QQuickGridView *self,
    QQuickGridView::Flow a0) {
  self->setFlow(a0);
}

//  qreal QQuickGridView::cellWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickGridView9cellWidthEv(const QQuickGridView *self) {
  return self->cellWidth();
}

//  void QQuickGridView::setCellWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView12setCellWidthEd(
    QQuickGridView *self,
    qreal a0) {
  self->setCellWidth(a0);
}

//  qreal QQuickGridView::cellHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickGridView10cellHeightEv(const QQuickGridView *self) {
  return self->cellHeight();
}

//  void QQuickGridView::setCellHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView13setCellHeightEd(
    QQuickGridView *self,
    qreal a0) {
  self->setCellHeight(a0);
}

//  SnapMode QQuickGridView::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickGridView::SnapMode ritual_ZNK14QQuickGridView8snapModeEv(
    const QQuickGridView *self) {
  return self->snapMode();
}

//  void QQuickGridView::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView11setSnapModeENS_8SnapModeE(
    QQuickGridView *self,
    QQuickGridView::SnapMode mode) {
  self->setSnapMode(mode);
}

//  QQuickGridViewAttached *QQuickGridView::qmlAttachedProperties(QObject
//      *a0)
extern "C" Q_DECL_EXPORT
QQuickGridViewAttached *ritual_ZN14QQuickGridView21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickGridView::qmlAttachedProperties(a0);
}

//  void QQuickGridView::moveCurrentIndexUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView18moveCurrentIndexUpEv(QQuickGridView *self) {
  self->moveCurrentIndexUp();
}

//  void QQuickGridView::moveCurrentIndexDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView20moveCurrentIndexDownEv(
    QQuickGridView *self) {
  self->moveCurrentIndexDown();
}

//  void QQuickGridView::moveCurrentIndexLeft()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView20moveCurrentIndexLeftEv(
    QQuickGridView *self) {
  self->moveCurrentIndexLeft();
}

//  void QQuickGridView::moveCurrentIndexRight()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView21moveCurrentIndexRightEv(
    QQuickGridView *self) {
  self->moveCurrentIndexRight();
}

//  void QQuickGridView::cellWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView16cellWidthChangedEv(QQuickGridView *self) {
  self->cellWidthChanged();
}

//  void QQuickGridView::cellHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView17cellHeightChangedEv(QQuickGridView *self) {
  self->cellHeightChanged();
}

//  void QQuickGridView::highlightMoveDurationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView28highlightMoveDurationChangedEv(
    QQuickGridView *self) {
  self->highlightMoveDurationChanged();
}

//  void QQuickGridView::flowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView11flowChangedEv(QQuickGridView *self) {
  self->flowChanged();
}

//  void QQuickGridView::snapModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView15snapModeChangedEv(QQuickGridView *self) {
  self->snapModeChanged();
}

//  void QQuickGridView::viewportMoved(Qt::Orientations a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickGridView *self,
    int a0) {
  self->viewportMoved(QFlags<Qt::Orientation>::fromInt(a0));
}

//  void QQuickGridView::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView13keyPressEventEP9QKeyEvent(
    QQuickGridView *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QQuickGridView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView14geometryChangeERK6QRectFS2_(
    QQuickGridView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickGridView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridView8initItemEiP7QObject(
    QQuickGridView *self,
    int index,
    QObject *item) {
  self->initItem(index, item);
}

//  a Python function taken by a CuteQQuickGridView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGridView(
    QQuickGridView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGridView *>(self)->take(key, call);
}

//  void QQuickGridView::setHighlightFollowsCurrentItem(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGridView30setHighlightFollowsCurrentItemEb(
    QQuickGridView *self,
    bool a0) {
  self->QQuickGridView::setHighlightFollowsCurrentItem(a0);
}

//  void QQuickGridView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGridView24setHighlightMoveDurationEi(
    QQuickGridView *self,
    int a0) {
  self->QQuickGridView::setHighlightMoveDuration(a0);
}

//  void QQuickGridView::viewportMoved(Qt::Orientations a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGridView13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickGridView *self,
    int a0) {
  static_cast<OwnQQuickGridView *>(self)->OwnQQuickGridView::viewportMoved(
      QFlags<Qt::Orientation>::fromInt(a0));
}

//  void QQuickGridView::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGridView13keyPressEventEP9QKeyEvent(
    QQuickGridView *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickGridView *>(self)->OwnQQuickGridView::keyPressEvent(
      a0);
}

//  void QQuickGridView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGridView14geometryChangeERK6QRectFS2_(
    QQuickGridView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickGridView *>(self)->OwnQQuickGridView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickGridView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGridView8initItemEiP7QObject(
    QQuickGridView *self,
    int index,
    QObject *item) {
  static_cast<OwnQQuickGridView *>(self)->OwnQQuickGridView::initItem(
      index,
      item);
}

#endif  // QT_CONFIG(quick_gridview)
#endif  // QT_CONFIG(quick_gridview)
