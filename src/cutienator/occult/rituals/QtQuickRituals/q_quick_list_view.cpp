//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicklistview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicklistview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickListView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickListView : QQuickListView {
  using QQuickListView::viewportMoved;
  using QQuickListView::keyPressEvent;
  using QQuickListView::geometryChange;
  using QQuickListView::initItem;
  using QQuickListView::maxYExtent;
  using QQuickListView::maxXExtent;
};

//  A QQuickListView that Python can take functions over in. Every QQuickListView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
typedef void (*CuteQQuickListViewCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
typedef void (*CuteQQuickListViewCall1)(const void *, int, int *);
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
typedef void (*CuteQQuickListViewCall2)(const void *, int, int *);
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
typedef void (*CuteQQuickListViewCall3)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
typedef void (*CuteQQuickListViewCall4)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
typedef void (*CuteQQuickListViewCall5)(const void *, int, QObject *, int *);
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
typedef qreal (*CuteQQuickListViewCall6)(const void *, int *);
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
typedef qreal (*CuteQQuickListViewCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickListViewCall8)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickListViewCall9)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickListViewCall10)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickListViewCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickListViewCall12)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickListViewCall13)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickListViewCall14)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickListViewCall15)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickListViewCall16)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickListViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickListViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickListViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickListViewCall20)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickListViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall23)(const void *, int *);
typedef const QRectF * (*CuteQQuickListViewCall24)(const void *, int *);
typedef const QRectF * (*CuteQQuickListViewCall25)(const void *, int *);
typedef bool (*CuteQQuickListViewCall26)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickListViewCall27)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickListViewCall28)(const void *, int *);
typedef void * (*CuteQQuickListViewCall29)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickListViewCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall31)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickListViewCall32)(const void *, int *);
typedef void (*CuteQQuickListViewCall33)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickListViewCall34)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickListViewCall35)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickListViewCall36)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickListViewCall37)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickListViewCall38)(const void *, int *);
typedef void (*CuteQQuickListViewCall39)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickListViewCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickListViewCall41)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickListViewCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickListViewCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickListViewCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickListViewCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickListViewCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickListViewCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickListViewCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickListViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickListView : public QQuickListView {
public:
  using QQuickListView::QQuickListView;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZN14QQuickItemView30setHighlightFollowsCurrentItemEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZN14QQuickItemView24setHighlightMoveDurationEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZN14QQuickItemView8initItemEiP7QObject")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxYExtentEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_listview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxXExtentEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_listview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentXEd")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentYEd")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originXEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originYEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minYExtentEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minXExtentEv")) {
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
#if QT_CONFIG(quick_listview)
  //  void QQuickListView::setHighlightFollowsCurrentItem(bool a0)
  void setHighlightFollowsCurrentItem(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickListViewCall0 call = reinterpret_cast<CuteQQuickListViewCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickListView::setHighlightFollowsCurrentItem(a0);
  }
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
  //  void QQuickListView::setHighlightMoveDuration(int a0)
  void setHighlightMoveDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickListViewCall1 call = reinterpret_cast<CuteQQuickListViewCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickListView::setHighlightMoveDuration(a0);
  }
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_listview)
  //  void QQuickListView::viewportMoved(Qt::Orientations orient)
  void viewportMoved(Qt::Orientations orient) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickListViewCall2 call = reinterpret_cast<CuteQQuickListViewCall2>(taken[2]);
      call(this, static_cast<int>(orient.toInt()), &handled);
      if (handled) return;
    }
    QQuickListView::viewportMoved(orient);
  }
#endif  // QT_CONFIG(quick_listview)

#if QT_CONFIG(quick_listview)
  //  void QQuickListView::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickListViewCall3 call = reinterpret_cast<CuteQQuickListViewCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickListView::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(quick_listview)

#if QT_CONFIG(quick_listview)
  //  void QQuickListView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickListViewCall4 call = reinterpret_cast<CuteQQuickListViewCall4>(taken[4]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickListView::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_listview)

#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_listview)
  //  void QQuickListView::initItem(int index, QObject *item)
  void initItem(int index, QObject *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickListViewCall5 call = reinterpret_cast<CuteQQuickListViewCall5>(taken[5]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickListView::initItem(index, item);
  }
#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_listview)
  //  qreal QQuickListView::maxYExtent() const
  qreal maxYExtent() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickListViewCall6 call = reinterpret_cast<CuteQQuickListViewCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickListView::maxYExtent();
  }
#endif  // QT_CONFIG(quick_listview)

#if QT_CONFIG(quick_listview)
  //  qreal QQuickListView::maxXExtent() const
  qreal maxXExtent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickListViewCall7 call = reinterpret_cast<CuteQQuickListViewCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickListView::maxXExtent();
  }
#endif  // QT_CONFIG(quick_listview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setContentX(qreal pos)
  void setContentX(qreal pos) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickListViewCall8 call = reinterpret_cast<CuteQQuickListViewCall8>(taken[8]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickItemView::setContentX(pos);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickListViewCall9 call = reinterpret_cast<CuteQQuickListViewCall9>(taken[9]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickItemView::setContentY(pos);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::originX() const
  qreal originX() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickListViewCall10 call = reinterpret_cast<CuteQQuickListViewCall10>(taken[10]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::originX();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::originY() const
  qreal originY() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickListViewCall11 call = reinterpret_cast<CuteQQuickListViewCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::originY();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::updatePolish()
  void updatePolish() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickListViewCall12 call = reinterpret_cast<CuteQQuickListViewCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemView::updatePolish();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemView::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickListViewCall13 call = reinterpret_cast<CuteQQuickListViewCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemView::componentComplete();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::minYExtent() const
  qreal minYExtent() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickListViewCall14 call = reinterpret_cast<CuteQQuickListViewCall14>(taken[14]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::minYExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemView::minXExtent() const
  qreal minXExtent() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickListViewCall15 call = reinterpret_cast<CuteQQuickListViewCall15>(taken[15]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemView::minXExtent();
  }
#endif  // QT_CONFIG(quick_itemview)

  //  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickListViewCall16 call = reinterpret_cast<CuteQQuickListViewCall16>(taken[16]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickListViewCall17 call = reinterpret_cast<CuteQQuickListViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickListViewCall18 call = reinterpret_cast<CuteQQuickListViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickListViewCall19 call = reinterpret_cast<CuteQQuickListViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickListViewCall20 call = reinterpret_cast<CuteQQuickListViewCall20>(taken[20]);
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
      CuteQQuickListViewCall21 call = reinterpret_cast<CuteQQuickListViewCall21>(taken[21]);
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
      CuteQQuickListViewCall22 call = reinterpret_cast<CuteQQuickListViewCall22>(taken[22]);
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
      CuteQQuickListViewCall23 call = reinterpret_cast<CuteQQuickListViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickListViewCall24 call = reinterpret_cast<CuteQQuickListViewCall24>(taken[24]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickListViewCall25 call = reinterpret_cast<CuteQQuickListViewCall25>(taken[25]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickListViewCall26 call = reinterpret_cast<CuteQQuickListViewCall26>(taken[26]);
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
      CuteQQuickListViewCall27 call = reinterpret_cast<CuteQQuickListViewCall27>(taken[27]);
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
      CuteQQuickListViewCall28 call = reinterpret_cast<CuteQQuickListViewCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickListViewCall29 call = reinterpret_cast<CuteQQuickListViewCall29>(taken[29]);
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
      CuteQQuickListViewCall30 call = reinterpret_cast<CuteQQuickListViewCall30>(taken[30]);
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
      CuteQQuickListViewCall31 call = reinterpret_cast<CuteQQuickListViewCall31>(taken[31]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickListViewCall32 call = reinterpret_cast<CuteQQuickListViewCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickListViewCall33 call = reinterpret_cast<CuteQQuickListViewCall33>(taken[33]);
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
      CuteQQuickListViewCall34 call = reinterpret_cast<CuteQQuickListViewCall34>(taken[34]);
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
      CuteQQuickListViewCall35 call = reinterpret_cast<CuteQQuickListViewCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickListViewCall36 call = reinterpret_cast<CuteQQuickListViewCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickListViewCall37 call = reinterpret_cast<CuteQQuickListViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickListViewCall38 call = reinterpret_cast<CuteQQuickListViewCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickListViewCall39 call = reinterpret_cast<CuteQQuickListViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickListViewCall40 call = reinterpret_cast<CuteQQuickListViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickListViewCall41 call = reinterpret_cast<CuteQQuickListViewCall41>(taken[41]);
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
      CuteQQuickListViewCall42 call = reinterpret_cast<CuteQQuickListViewCall42>(taken[42]);
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
      CuteQQuickListViewCall43 call = reinterpret_cast<CuteQQuickListViewCall43>(taken[43]);
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
      CuteQQuickListViewCall44 call = reinterpret_cast<CuteQQuickListViewCall44>(taken[44]);
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
      CuteQQuickListViewCall45 call = reinterpret_cast<CuteQQuickListViewCall45>(taken[45]);
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
      CuteQQuickListViewCall46 call = reinterpret_cast<CuteQQuickListViewCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickListViewCall47 call = reinterpret_cast<CuteQQuickListViewCall47>(taken[47]);
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
      CuteQQuickListViewCall48 call = reinterpret_cast<CuteQQuickListViewCall48>(taken[48]);
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
      CuteQQuickListViewCall49 call = reinterpret_cast<CuteQQuickListViewCall49>(taken[49]);
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
      CuteQQuickListViewCall50 call = reinterpret_cast<CuteQQuickListViewCall50>(taken[50]);
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
      CuteQQuickListViewCall51 call = reinterpret_cast<CuteQQuickListViewCall51>(taken[51]);
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
      CuteQQuickListViewCall52 call = reinterpret_cast<CuteQQuickListViewCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickListView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickListView10metaObjectEv(
    const QQuickListView *self) {
  return self->metaObject();
}

//  void *QQuickListView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickListView11qt_metacastEPKc(
    QQuickListView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickListView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickListView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickListView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickListView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickListView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickListView::tr(s, c, n));
}

//  QQuickListViewPrivate *QQuickListView::d_func()
extern "C" Q_DECL_EXPORT
QQuickListViewPrivate *ritual_ZN14QQuickListView6d_funcEv(
    QQuickListView *self) {
  return self->d_func();
}

//  const QQuickListViewPrivate *QQuickListView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickListViewPrivate *ritual_ZNK14QQuickListView6d_funcEv(
    const QQuickListView *self) {
  return self->d_func();
}

//  void QQuickListView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView21qt_qmlMarker_attachedEv(
    QQuickListView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickListView::QQuickListView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZN14QQuickListViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickListView(parent);
}

//  QQuickListView::~QQuickListView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListViewD1Ev(QQuickListView *self) {
  delete self;
}

//  qreal QQuickListView::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickListView7spacingEv(const QQuickListView *self) {
  return self->spacing();
}

//  void QQuickListView::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView10setSpacingEd(
    QQuickListView *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  Orientation QQuickListView::orientation() const
extern "C" Q_DECL_EXPORT
QQuickListView::Orientation ritual_ZNK14QQuickListView11orientationEv(
    const QQuickListView *self) {
  return self->orientation();
}

//  void QQuickListView::setOrientation(Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView14setOrientationENS_11OrientationE(
    QQuickListView *self,
    QQuickListView::Orientation a0) {
  self->setOrientation(a0);
}

//  QQuickViewSection *QQuickListView::sectionCriteria()
extern "C" Q_DECL_EXPORT
QQuickViewSection *ritual_ZN14QQuickListView15sectionCriteriaEv(
    QQuickListView *self) {
  return self->sectionCriteria();
}

//  QString QQuickListView::currentSection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickListView14currentSectionEv(
    const QQuickListView *self) {
  return new QString(self->currentSection());
}

//  void QQuickListView::setHighlightFollowsCurrentItem(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView30setHighlightFollowsCurrentItemEb(
    QQuickListView *self,
    bool a0) {
  self->setHighlightFollowsCurrentItem(a0);
}

//  qreal QQuickListView::highlightMoveVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickListView21highlightMoveVelocityEv(
    const QQuickListView *self) {
  return self->highlightMoveVelocity();
}

//  void QQuickListView::setHighlightMoveVelocity(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView24setHighlightMoveVelocityEd(
    QQuickListView *self,
    qreal a0) {
  self->setHighlightMoveVelocity(a0);
}

//  qreal QQuickListView::highlightResizeVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickListView23highlightResizeVelocityEv(
    const QQuickListView *self) {
  return self->highlightResizeVelocity();
}

//  void QQuickListView::setHighlightResizeVelocity(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView26setHighlightResizeVelocityEd(
    QQuickListView *self,
    qreal a0) {
  self->setHighlightResizeVelocity(a0);
}

//  int QQuickListView::highlightResizeDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickListView23highlightResizeDurationEv(
    const QQuickListView *self) {
  return self->highlightResizeDuration();
}

//  void QQuickListView::setHighlightResizeDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView26setHighlightResizeDurationEi(
    QQuickListView *self,
    int a0) {
  self->setHighlightResizeDuration(a0);
}

//  void QQuickListView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView24setHighlightMoveDurationEi(
    QQuickListView *self,
    int a0) {
  self->setHighlightMoveDuration(a0);
}

//  SnapMode QQuickListView::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickListView::SnapMode ritual_ZNK14QQuickListView8snapModeEv(
    const QQuickListView *self) {
  return self->snapMode();
}

//  void QQuickListView::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView11setSnapModeENS_8SnapModeE(
    QQuickListView *self,
    QQuickListView::SnapMode mode) {
  self->setSnapMode(mode);
}

//  HeaderPositioning QQuickListView::headerPositioning() const
extern "C" Q_DECL_EXPORT
QQuickListView::HeaderPositioning ritual_ZNK14QQuickListView17headerPositioningEv(
    const QQuickListView *self) {
  return self->headerPositioning();
}

//  void QQuickListView::setHeaderPositioning(HeaderPositioning positioning)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView20setHeaderPositioningENS_17HeaderPositioningE(
    QQuickListView *self,
    QQuickListView::HeaderPositioning positioning) {
  self->setHeaderPositioning(positioning);
}

//  FooterPositioning QQuickListView::footerPositioning() const
extern "C" Q_DECL_EXPORT
QQuickListView::FooterPositioning ritual_ZNK14QQuickListView17footerPositioningEv(
    const QQuickListView *self) {
  return self->footerPositioning();
}

//  void QQuickListView::setFooterPositioning(FooterPositioning positioning)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView20setFooterPositioningENS_17FooterPositioningE(
    QQuickListView *self,
    QQuickListView::FooterPositioning positioning) {
  self->setFooterPositioning(positioning);
}

//  QQuickListViewAttached *QQuickListView::qmlAttachedProperties(QObject
//      *a0)
extern "C" Q_DECL_EXPORT
QQuickListViewAttached *ritual_ZN14QQuickListView21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickListView::qmlAttachedProperties(a0);
}

//  void QQuickListView::incrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView21incrementCurrentIndexEv(
    QQuickListView *self) {
  self->incrementCurrentIndex();
}

//  void QQuickListView::decrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView21decrementCurrentIndexEv(
    QQuickListView *self) {
  self->decrementCurrentIndex();
}

//  void QQuickListView::spacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView14spacingChangedEv(QQuickListView *self) {
  self->spacingChanged();
}

//  void QQuickListView::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView18orientationChangedEv(QQuickListView *self) {
  self->orientationChanged();
}

//  void QQuickListView::currentSectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView21currentSectionChangedEv(
    QQuickListView *self) {
  self->currentSectionChanged();
}

//  void QQuickListView::highlightMoveVelocityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView28highlightMoveVelocityChangedEv(
    QQuickListView *self) {
  self->highlightMoveVelocityChanged();
}

//  void QQuickListView::highlightResizeVelocityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView30highlightResizeVelocityChangedEv(
    QQuickListView *self) {
  self->highlightResizeVelocityChanged();
}

//  void QQuickListView::highlightResizeDurationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView30highlightResizeDurationChangedEv(
    QQuickListView *self) {
  self->highlightResizeDurationChanged();
}

//  void QQuickListView::snapModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView15snapModeChangedEv(QQuickListView *self) {
  self->snapModeChanged();
}

//  void QQuickListView::headerPositioningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView24headerPositioningChangedEv(
    QQuickListView *self) {
  self->headerPositioningChanged();
}

//  void QQuickListView::footerPositioningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView24footerPositioningChangedEv(
    QQuickListView *self) {
  self->footerPositioningChanged();
}

//  void QQuickListView::viewportMoved(Qt::Orientations orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickListView *self,
    int orient) {
  self->viewportMoved(QFlags<Qt::Orientation>::fromInt(orient));
}

//  void QQuickListView::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView13keyPressEventEP9QKeyEvent(
    QQuickListView *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QQuickListView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView14geometryChangeERK6QRectFS2_(
    QQuickListView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickListView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickListView8initItemEiP7QObject(
    QQuickListView *self,
    int index,
    QObject *item) {
  self->initItem(index, item);
}

//  qreal QQuickListView::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickListView10maxYExtentEv(const QQuickListView *self) {
  return self->maxYExtent();
}

//  qreal QQuickListView::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickListView10maxXExtentEv(const QQuickListView *self) {
  return self->maxXExtent();
}

//  a Python function taken by a CuteQQuickListView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickListView(
    QQuickListView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickListView *>(self)->take(key, call);
}

//  void QQuickListView::setHighlightFollowsCurrentItem(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickListView30setHighlightFollowsCurrentItemEb(
    QQuickListView *self,
    bool a0) {
  self->QQuickListView::setHighlightFollowsCurrentItem(a0);
}

//  void QQuickListView::setHighlightMoveDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickListView24setHighlightMoveDurationEi(
    QQuickListView *self,
    int a0) {
  self->QQuickListView::setHighlightMoveDuration(a0);
}

//  void QQuickListView::viewportMoved(Qt::Orientations orient)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickListView13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickListView *self,
    int orient) {
  static_cast<OwnQQuickListView *>(self)->OwnQQuickListView::viewportMoved(
      QFlags<Qt::Orientation>::fromInt(orient));
}

//  void QQuickListView::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickListView13keyPressEventEP9QKeyEvent(
    QQuickListView *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickListView *>(self)->OwnQQuickListView::keyPressEvent(
      a0);
}

//  void QQuickListView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickListView14geometryChangeERK6QRectFS2_(
    QQuickListView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickListView *>(self)->OwnQQuickListView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickListView::initItem(int index, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickListView8initItemEiP7QObject(
    QQuickListView *self,
    int index,
    QObject *item) {
  static_cast<OwnQQuickListView *>(self)->OwnQQuickListView::initItem(
      index,
      item);
}

//  qreal QQuickListView::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickListView10maxYExtentEv(
    const QQuickListView *self) {
  return static_cast<const OwnQQuickListView *>(self)->OwnQQuickListView::maxYExtent();
}

//  qreal QQuickListView::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QQuickListView10maxXExtentEv(
    const QQuickListView *self) {
  return static_cast<const OwnQQuickListView *>(self)->OwnQQuickListView::maxXExtent();
}

#endif  // QT_CONFIG(quick_listview)
#endif  // QT_CONFIG(quick_listview)
