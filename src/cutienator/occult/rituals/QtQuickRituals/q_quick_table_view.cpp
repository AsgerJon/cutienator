//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTableView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTableView : QQuickTableView {
  using QQuickTableView::geometryChange;
  using QQuickTableView::viewportMoved;
  using QQuickTableView::keyPressEvent;
  using QQuickTableView::eventFilter;
  using QQuickTableView::componentFinalized;
};

//  A QQuickTableView that Python can take functions over in. Every QQuickTableView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
typedef const QModelIndex * (*CuteQQuickTableViewCall0)(const void *, int, int, int *);
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef const QModelIndex * (*CuteQQuickTableViewCall1)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef const QPoint * (*CuteQQuickTableViewCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTableViewCall3)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTableViewCall4)(const void *, int, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTableViewCall5)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
typedef bool (*CuteQQuickTableViewCall6)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(quick_tableview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTableViewCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTableViewCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTableViewCall9)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTableViewCall10)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTableViewCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTableViewCall12)(const void *, qreal, int *);
typedef void (*CuteQQuickTableViewCall13)(const void *, qreal, int *);
typedef qreal (*CuteQQuickTableViewCall14)(const void *, int *);
typedef qreal (*CuteQQuickTableViewCall15)(const void *, int *);
typedef bool (*CuteQQuickTableViewCall16)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTableViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTableViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTableViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTableViewCall20)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTableViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall23)(const void *, int *);
typedef void (*CuteQQuickTableViewCall24)(const void *, int *);
typedef const QRectF * (*CuteQQuickTableViewCall25)(const void *, int *);
typedef const QRectF * (*CuteQQuickTableViewCall26)(const void *, int *);
typedef bool (*CuteQQuickTableViewCall27)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTableViewCall28)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickTableViewCall29)(const void *, int *);
typedef void * (*CuteQQuickTableViewCall30)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall32)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTableViewCall33)(const void *, int *);
typedef void (*CuteQQuickTableViewCall34)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTableViewCall35)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTableViewCall36)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTableViewCall37)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTableViewCall38)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTableViewCall39)(const void *, int *);
typedef void (*CuteQQuickTableViewCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTableViewCall41)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTableViewCall42)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTableViewCall43)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTableViewCall44)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTableViewCall45)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTableViewCall46)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickTableViewCall47)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTableViewCall48)(const void *, int *);
typedef void (*CuteQQuickTableViewCall49)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTableView : public QQuickTableView {
public:
  using QQuickTableView::QQuickTableView;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
    if (!std::strcmp(key, "_ZNK15QQuickTableView10modelIndexEii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickTableView10modelIndexERK6QPoint")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN17QQmlFinalizerHook18componentFinalizedEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minXExtentEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxXExtentEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10minYExtentEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickFlickable10maxYExtentEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentXEd")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickFlickable11setContentYEd")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originYEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQuickFlickable7originXEv")) {
      taken[15] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[30] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[42] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[49] = call;
      return true;
    }
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

#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
  //  QModelIndex QQuickTableView::modelIndex(int row, int column) const
  QModelIndex modelIndex(int row, int column) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTableViewCall0 call = reinterpret_cast<CuteQQuickTableViewCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableView::modelIndex(row, column);
  }
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  QModelIndex QQuickTableView::modelIndex(const QPoint &cell) const
  QModelIndex modelIndex(const QPoint &cell) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTableViewCall1 call = reinterpret_cast<CuteQQuickTableViewCall1>(taken[1]);
      const QModelIndex * given = call(this, &cell, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableView::modelIndex(cell);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  QPoint QQuickTableView::cellAtIndex(const QModelIndex &index) const
  QPoint cellAtIndex(const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTableViewCall2 call = reinterpret_cast<CuteQQuickTableViewCall2>(taken[2]);
      const QPoint * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QQuickTableView::cellAtIndex(index);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  void QQuickTableView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTableViewCall3 call = reinterpret_cast<CuteQQuickTableViewCall3>(taken[3]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTableView::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  void QQuickTableView::viewportMoved(Qt::Orientations orientation)
  void viewportMoved(Qt::Orientations orientation) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTableViewCall4 call = reinterpret_cast<CuteQQuickTableViewCall4>(taken[4]);
      call(this, static_cast<int>(orientation.toInt()), &handled);
      if (handled) return;
    }
    QQuickTableView::viewportMoved(orientation);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  void QQuickTableView::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTableViewCall5 call = reinterpret_cast<CuteQQuickTableViewCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickTableView::keyPressEvent(e);
  }
#endif  // QT_CONFIG(quick_tableview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
  //  bool QQuickTableView::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTableViewCall6 call = reinterpret_cast<CuteQQuickTableViewCall6>(taken[6]);
      bool given = call(this, obj, event, &handled);
      if (handled) return given;
    }
    return QQuickTableView::eventFilter(obj, event);
  }
#endif  // QT_CONFIG(quick_tableview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_tableview)
  //  void QQuickTableView::componentFinalized()
  void componentFinalized() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTableViewCall7 call = reinterpret_cast<CuteQQuickTableViewCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTableView::componentFinalized();
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  qreal QQuickTableView::minXExtent() const
  qreal minXExtent() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTableViewCall8 call = reinterpret_cast<CuteQQuickTableViewCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTableView::minXExtent();
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  qreal QQuickTableView::maxXExtent() const
  qreal maxXExtent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTableViewCall9 call = reinterpret_cast<CuteQQuickTableViewCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTableView::maxXExtent();
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  qreal QQuickTableView::minYExtent() const
  qreal minYExtent() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTableViewCall10 call = reinterpret_cast<CuteQQuickTableViewCall10>(taken[10]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTableView::minYExtent();
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  qreal QQuickTableView::maxYExtent() const
  qreal maxYExtent() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTableViewCall11 call = reinterpret_cast<CuteQQuickTableViewCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTableView::maxYExtent();
  }
#endif  // QT_CONFIG(quick_tableview)

  //  void QQuickFlickable::setContentX(qreal pos)
  void setContentX(qreal pos) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTableViewCall12 call = reinterpret_cast<CuteQQuickTableViewCall12>(taken[12]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentX(pos);
  }

  //  void QQuickFlickable::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTableViewCall13 call = reinterpret_cast<CuteQQuickTableViewCall13>(taken[13]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentY(pos);
  }

  //  qreal QQuickFlickable::originY() const
  qreal originY() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTableViewCall14 call = reinterpret_cast<CuteQQuickTableViewCall14>(taken[14]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::originY();
  }

  //  qreal QQuickFlickable::originX() const
  qreal originX() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTableViewCall15 call = reinterpret_cast<CuteQQuickTableViewCall15>(taken[15]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::originX();
  }

  //  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTableViewCall16 call = reinterpret_cast<CuteQQuickTableViewCall16>(taken[16]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTableViewCall17 call = reinterpret_cast<CuteQQuickTableViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTableViewCall18 call = reinterpret_cast<CuteQQuickTableViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTableViewCall19 call = reinterpret_cast<CuteQQuickTableViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTableViewCall20 call = reinterpret_cast<CuteQQuickTableViewCall20>(taken[20]);
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
      CuteQQuickTableViewCall21 call = reinterpret_cast<CuteQQuickTableViewCall21>(taken[21]);
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
      CuteQQuickTableViewCall22 call = reinterpret_cast<CuteQQuickTableViewCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickFlickable::componentComplete()
  void componentComplete() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTableViewCall23 call = reinterpret_cast<CuteQQuickTableViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::componentComplete();
  }

  //  void QQuickFlickable::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTableViewCall24 call = reinterpret_cast<CuteQQuickTableViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTableViewCall25 call = reinterpret_cast<CuteQQuickTableViewCall25>(taken[25]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTableViewCall26 call = reinterpret_cast<CuteQQuickTableViewCall26>(taken[26]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTableViewCall27 call = reinterpret_cast<CuteQQuickTableViewCall27>(taken[27]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTableViewCall28 call = reinterpret_cast<CuteQQuickTableViewCall28>(taken[28]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTableViewCall29 call = reinterpret_cast<CuteQQuickTableViewCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTableViewCall30 call = reinterpret_cast<CuteQQuickTableViewCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTableViewCall31 call = reinterpret_cast<CuteQQuickTableViewCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTableViewCall32 call = reinterpret_cast<CuteQQuickTableViewCall32>(taken[32]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTableViewCall33 call = reinterpret_cast<CuteQQuickTableViewCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTableViewCall34 call = reinterpret_cast<CuteQQuickTableViewCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTableViewCall35 call = reinterpret_cast<CuteQQuickTableViewCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTableViewCall36 call = reinterpret_cast<CuteQQuickTableViewCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTableViewCall37 call = reinterpret_cast<CuteQQuickTableViewCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTableViewCall38 call = reinterpret_cast<CuteQQuickTableViewCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTableViewCall39 call = reinterpret_cast<CuteQQuickTableViewCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTableViewCall40 call = reinterpret_cast<CuteQQuickTableViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTableViewCall41 call = reinterpret_cast<CuteQQuickTableViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickTableViewCall42 call = reinterpret_cast<CuteQQuickTableViewCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickTableViewCall43 call = reinterpret_cast<CuteQQuickTableViewCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickTableViewCall44 call = reinterpret_cast<CuteQQuickTableViewCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickTableViewCall45 call = reinterpret_cast<CuteQQuickTableViewCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickTableViewCall46 call = reinterpret_cast<CuteQQuickTableViewCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQQuickTableViewCall47 call = reinterpret_cast<CuteQQuickTableViewCall47>(taken[47]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickTableViewCall48 call = reinterpret_cast<CuteQQuickTableViewCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickTableViewCall49 call = reinterpret_cast<CuteQQuickTableViewCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickTableViewCall50 call = reinterpret_cast<CuteQQuickTableViewCall50>(taken[50]);
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
      CuteQQuickTableViewCall51 call = reinterpret_cast<CuteQQuickTableViewCall51>(taken[51]);
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
      CuteQQuickTableViewCall52 call = reinterpret_cast<CuteQQuickTableViewCall52>(taken[52]);
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
      CuteQQuickTableViewCall53 call = reinterpret_cast<CuteQQuickTableViewCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTableView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickTableView10metaObjectEv(
    const QQuickTableView *self) {
  return self->metaObject();
}

//  QString QQuickTableView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickTableView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTableView::tr(s, c, n));
}

//  void QQuickTableView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView21qt_qmlMarker_attachedEv(
    QQuickTableView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickTableView::QQuickTableView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTableView *ritual_ZN15QQuickTableViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTableView(parent);
}

//  QQuickTableView::~QQuickTableView()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableViewD1Ev(QQuickTableView *self) {
  delete self;
}

//  int QQuickTableView::rows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView4rowsEv(const QQuickTableView *self) {
  return self->rows();
}

//  int QQuickTableView::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView7columnsEv(const QQuickTableView *self) {
  return self->columns();
}

//  qreal QQuickTableView::rowSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView10rowSpacingEv(
    const QQuickTableView *self) {
  return self->rowSpacing();
}

//  void QQuickTableView::setRowSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView13setRowSpacingEd(
    QQuickTableView *self,
    qreal spacing) {
  self->setRowSpacing(spacing);
}

//  qreal QQuickTableView::columnSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView13columnSpacingEv(
    const QQuickTableView *self) {
  return self->columnSpacing();
}

//  void QQuickTableView::setColumnSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView16setColumnSpacingEd(
    QQuickTableView *self,
    qreal spacing) {
  self->setColumnSpacing(spacing);
}

//  QJSValue QQuickTableView::rowHeightProvider() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QQuickTableView17rowHeightProviderEv(
    const QQuickTableView *self) {
  return new QJSValue(self->rowHeightProvider());
}

//  void QQuickTableView::setRowHeightProvider(const QJSValue &provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView20setRowHeightProviderERK8QJSValue(
    QQuickTableView *self,
    const QJSValue *provider) {
  self->setRowHeightProvider(*provider);
}

//  QJSValue QQuickTableView::columnWidthProvider() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QQuickTableView19columnWidthProviderEv(
    const QQuickTableView *self) {
  return new QJSValue(self->columnWidthProvider());
}

//  void QQuickTableView::setColumnWidthProvider(const QJSValue &provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView22setColumnWidthProviderERK8QJSValue(
    QQuickTableView *self,
    const QJSValue *provider) {
  self->setColumnWidthProvider(*provider);
}

//  QVariant QQuickTableView::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQuickTableView5modelEv(const QQuickTableView *self) {
  return new QVariant(self->model());
}

//  void QQuickTableView::setModel(const QVariant &newModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView8setModelERK8QVariant(
    QQuickTableView *self,
    const QVariant *newModel) {
  self->setModel(*newModel);
}

//  QQmlComponent *QQuickTableView::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK15QQuickTableView8delegateEv(
    const QQuickTableView *self) {
  return self->delegate();
}

//  void QQuickTableView::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView11setDelegateEP13QQmlComponent(
    QQuickTableView *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  bool QQuickTableView::reuseItems() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView10reuseItemsEv(const QQuickTableView *self) {
  return self->reuseItems();
}

//  void QQuickTableView::setReuseItems(bool reuseItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView13setReuseItemsEb(
    QQuickTableView *self,
    bool reuseItems) {
  self->setReuseItems(reuseItems);
}

//  void QQuickTableView::setContentWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView15setContentWidthEd(
    QQuickTableView *self,
    qreal width) {
  self->setContentWidth(width);
}

//  void QQuickTableView::setContentHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView16setContentHeightEd(
    QQuickTableView *self,
    qreal height) {
  self->setContentHeight(height);
}

//  QQuickTableView *QQuickTableView::syncView() const
extern "C" Q_DECL_EXPORT
QQuickTableView *ritual_ZNK15QQuickTableView8syncViewEv(
    const QQuickTableView *self) {
  return self->syncView();
}

//  void QQuickTableView::setSyncView(QQuickTableView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView11setSyncViewEPS_(
    QQuickTableView *self,
    QQuickTableView *view) {
  self->setSyncView(view);
}

//  Qt::Orientations QQuickTableView::syncDirection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView13syncDirectionEv(
    const QQuickTableView *self) {
  return static_cast<int>(self->syncDirection().toInt());
}

//  void QQuickTableView::setSyncDirection(Qt::Orientations direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView16setSyncDirectionE6QFlagsIN2Qt11OrientationEE(
    QQuickTableView *self,
    int direction) {
  self->setSyncDirection(QFlags<Qt::Orientation>::fromInt(direction));
}

//  QItemSelectionModel *QQuickTableView::selectionModel() const
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZNK15QQuickTableView14selectionModelEv(
    const QQuickTableView *self) {
  return self->selectionModel();
}

//  void QQuickTableView::setSelectionModel(QItemSelectionModel
//      *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView17setSelectionModelEP19QItemSelectionModel(
    QQuickTableView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  bool QQuickTableView::animate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView7animateEv(const QQuickTableView *self) {
  return self->animate();
}

//  void QQuickTableView::setAnimate(bool animate)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView10setAnimateEb(
    QQuickTableView *self,
    bool animate) {
  self->setAnimate(animate);
}

//  bool QQuickTableView::keyNavigationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView20keyNavigationEnabledEv(
    const QQuickTableView *self) {
  return self->keyNavigationEnabled();
}

//  void QQuickTableView::setKeyNavigationEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView23setKeyNavigationEnabledEb(
    QQuickTableView *self,
    bool enabled) {
  self->setKeyNavigationEnabled(enabled);
}

//  bool QQuickTableView::pointerNavigationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView24pointerNavigationEnabledEv(
    const QQuickTableView *self) {
  return self->pointerNavigationEnabled();
}

//  void QQuickTableView::setPointerNavigationEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView27setPointerNavigationEnabledEb(
    QQuickTableView *self,
    bool enabled) {
  self->setPointerNavigationEnabled(enabled);
}

//  int QQuickTableView::leftColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView10leftColumnEv(const QQuickTableView *self) {
  return self->leftColumn();
}

//  int QQuickTableView::rightColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView11rightColumnEv(const QQuickTableView *self) {
  return self->rightColumn();
}

//  int QQuickTableView::topRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView6topRowEv(const QQuickTableView *self) {
  return self->topRow();
}

//  int QQuickTableView::bottomRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView9bottomRowEv(const QQuickTableView *self) {
  return self->bottomRow();
}

//  int QQuickTableView::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView10currentRowEv(const QQuickTableView *self) {
  return self->currentRow();
}

//  int QQuickTableView::currentColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView13currentColumnEv(
    const QQuickTableView *self) {
  return self->currentColumn();
}

//  bool QQuickTableView::alternatingRows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView15alternatingRowsEv(
    const QQuickTableView *self) {
  return self->alternatingRows();
}

//  void QQuickTableView::setAlternatingRows(bool alternatingRows)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView18setAlternatingRowsEb(
    QQuickTableView *self,
    bool alternatingRows) {
  self->setAlternatingRows(alternatingRows);
}

//  SelectionBehavior QQuickTableView::selectionBehavior() const
extern "C" Q_DECL_EXPORT
QQuickTableView::SelectionBehavior ritual_ZNK15QQuickTableView17selectionBehaviorEv(
    const QQuickTableView *self) {
  return self->selectionBehavior();
}

//  void QQuickTableView::setSelectionBehavior(SelectionBehavior
//      selectionBehavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView20setSelectionBehaviorENS_17SelectionBehaviorE(
    QQuickTableView *self,
    QQuickTableView::SelectionBehavior selectionBehavior) {
  self->setSelectionBehavior(selectionBehavior);
}

//  SelectionMode QQuickTableView::selectionMode() const
extern "C" Q_DECL_EXPORT
QQuickTableView::SelectionMode ritual_ZNK15QQuickTableView13selectionModeEv(
    const QQuickTableView *self) {
  return self->selectionMode();
}

//  void QQuickTableView::setSelectionMode(SelectionMode selectionMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView16setSelectionModeENS_13SelectionModeE(
    QQuickTableView *self,
    QQuickTableView::SelectionMode selectionMode) {
  self->setSelectionMode(selectionMode);
}

//  bool QQuickTableView::resizableColumns() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView16resizableColumnsEv(
    const QQuickTableView *self) {
  return self->resizableColumns();
}

//  void QQuickTableView::setResizableColumns(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView19setResizableColumnsEb(
    QQuickTableView *self,
    bool enabled) {
  self->setResizableColumns(enabled);
}

//  bool QQuickTableView::resizableRows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView13resizableRowsEv(
    const QQuickTableView *self) {
  return self->resizableRows();
}

//  void QQuickTableView::setResizableRows(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView16setResizableRowsEb(
    QQuickTableView *self,
    bool enabled) {
  self->setResizableRows(enabled);
}

//  EditTriggers QQuickTableView::editTriggers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView12editTriggersEv(
    const QQuickTableView *self) {
  return static_cast<int>(self->editTriggers().toInt());
}

//  void QQuickTableView::setEditTriggers(EditTriggers editTriggers)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView15setEditTriggersE6QFlagsINS_11EditTriggerEE(
    QQuickTableView *self,
    int editTriggers) {
  self->setEditTriggers(
      QFlags<QQuickTableView::EditTrigger>::fromInt(editTriggers));
}

//  QQmlDelegateModel::DelegateModelAccess
//      QQuickTableView::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK15QQuickTableView19delegateModelAccessEv(
    const QQuickTableView *self) {
  return self->delegateModelAccess();
}

//  void QQuickTableView::setDelegateModelAccess(QQmlDelegateModel::DelegateM
//      odelAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QQuickTableView *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  void QQuickTableView::forceLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView11forceLayoutEv(QQuickTableView *self) {
  self->forceLayout();
}

//  void QQuickTableView::positionViewAtCell(const QPoint &cell,
//      QQuickFlickable::PositionMode mode, const QPointF &offset, const
//      QRectF &subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView18positionViewAtCellERK6QPoint6QFlagsIN15QQuickFlickable16PositionModeFlagEERK7QPointFRK6QRectF(
    QQuickTableView *self,
    const QPoint *cell,
    int mode,
    const QPointF *offset,
    const QRectF *subRect) {
  self->positionViewAtCell(
      *cell,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      *offset,
      *subRect);
}

//  void QQuickTableView::positionViewAtIndex(const QModelIndex &index,
//      QQuickFlickable::PositionMode mode, const QPointF &offset, const
//      QRectF &subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView19positionViewAtIndexERK11QModelIndex6QFlagsIN15QQuickFlickable16PositionModeFlagEERK7QPointFRK6QRectF(
    QQuickTableView *self,
    const QModelIndex *index,
    int mode,
    const QPointF *offset,
    const QRectF *subRect) {
  self->positionViewAtIndex(
      *index,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      *offset,
      *subRect);
}

//  void QQuickTableView::positionViewAtRow(int row,
//      QQuickFlickable::PositionMode mode, qreal offset, const QRectF
//      &subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView17positionViewAtRowEi6QFlagsIN15QQuickFlickable16PositionModeFlagEEdRK6QRectF(
    QQuickTableView *self,
    int row,
    int mode,
    qreal offset,
    const QRectF *subRect) {
  self->positionViewAtRow(
      row,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      offset,
      *subRect);
}

//  void QQuickTableView::positionViewAtColumn(int column,
//      QQuickFlickable::PositionMode mode, qreal offset, const QRectF
//      &subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView20positionViewAtColumnEi6QFlagsIN15QQuickFlickable16PositionModeFlagEEdRK6QRectF(
    QQuickTableView *self,
    int column,
    int mode,
    qreal offset,
    const QRectF *subRect) {
  self->positionViewAtColumn(
      column,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      offset,
      *subRect);
}

//  QQuickItem *QQuickTableView::itemAtCell(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickTableView10itemAtCellERK6QPoint(
    const QQuickTableView *self,
    const QPoint *cell) {
  return self->itemAtCell(*cell);
}

//  QPoint QQuickTableView::cellAtPosition(const QPointF &position, bool
//      includeSpacing) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QQuickTableView14cellAtPositionERK7QPointFb(
    const QQuickTableView *self,
    const QPointF *position,
    bool includeSpacing) {
  return new QPoint(self->cellAtPosition(*position, includeSpacing));
}

//  QPoint QQuickTableView::cellAtPosition(qreal x, qreal y, bool
//      includeSpacing) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QQuickTableView14cellAtPositionEddb(
    const QQuickTableView *self,
    qreal x,
    qreal y,
    bool includeSpacing) {
  return new QPoint(self->cellAtPosition(x, y, includeSpacing));
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QModelIndex QQuickTableView::modelIndex(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK15QQuickTableView10modelIndexEii(
    const QQuickTableView *self,
    int row,
    int column) {
  return new QModelIndex(self->modelIndex(row, column));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QPoint QQuickTableView::cellAtPos(const QPointF &position, bool
//      includeSpacing) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QQuickTableView9cellAtPosERK7QPointFb(
    const QQuickTableView *self,
    const QPointF *position,
    bool includeSpacing) {
  return new QPoint(self->cellAtPos(*position, includeSpacing));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QPoint QQuickTableView::cellAtPos(qreal x, qreal y, bool includeSpacing)
//      const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QQuickTableView9cellAtPosEddb(
    const QQuickTableView *self,
    qreal x,
    qreal y,
    bool includeSpacing) {
  return new QPoint(self->cellAtPos(x, y, includeSpacing));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  bool QQuickTableView::isColumnLoaded(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView14isColumnLoadedEi(
    const QQuickTableView *self,
    int column) {
  return self->isColumnLoaded(column);
}

//  bool QQuickTableView::isRowLoaded(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTableView11isRowLoadedEi(
    const QQuickTableView *self,
    int row) {
  return self->isRowLoaded(row);
}

//  qreal QQuickTableView::columnWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView11columnWidthEi(
    const QQuickTableView *self,
    int column) {
  return self->columnWidth(column);
}

//  qreal QQuickTableView::rowHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView9rowHeightEi(
    const QQuickTableView *self,
    int row) {
  return self->rowHeight(row);
}

//  qreal QQuickTableView::implicitColumnWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView19implicitColumnWidthEi(
    const QQuickTableView *self,
    int column) {
  return self->implicitColumnWidth(column);
}

//  qreal QQuickTableView::implicitRowHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView17implicitRowHeightEi(
    const QQuickTableView *self,
    int row) {
  return self->implicitRowHeight(row);
}

//  QModelIndex QQuickTableView::index(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK15QQuickTableView5indexEii(
    const QQuickTableView *self,
    int row,
    int column) {
  return new QModelIndex(self->index(row, column));
}

//  QModelIndex QQuickTableView::modelIndex(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK15QQuickTableView10modelIndexERK6QPoint(
    const QQuickTableView *self,
    const QPoint *cell) {
  return new QModelIndex(self->modelIndex(*cell));
}

//  QPoint QQuickTableView::cellAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex(
    const QQuickTableView *self,
    const QModelIndex *index) {
  return new QPoint(self->cellAtIndex(*index));
}

//  int QQuickTableView::rowAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView10rowAtIndexERK11QModelIndex(
    const QQuickTableView *self,
    const QModelIndex *index) {
  return self->rowAtIndex(*index);
}

//  int QQuickTableView::columnAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTableView13columnAtIndexERK11QModelIndex(
    const QQuickTableView *self,
    const QModelIndex *index) {
  return self->columnAtIndex(*index);
}

//  void QQuickTableView::setColumnWidth(int column, qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView14setColumnWidthEid(
    QQuickTableView *self,
    int column,
    qreal size) {
  self->setColumnWidth(column, size);
}

//  void QQuickTableView::clearColumnWidths()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView17clearColumnWidthsEv(QQuickTableView *self) {
  self->clearColumnWidths();
}

//  qreal QQuickTableView::explicitColumnWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView19explicitColumnWidthEi(
    const QQuickTableView *self,
    int column) {
  return self->explicitColumnWidth(column);
}

//  void QQuickTableView::setRowHeight(int row, qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView12setRowHeightEid(
    QQuickTableView *self,
    int row,
    qreal size) {
  self->setRowHeight(row, size);
}

//  void QQuickTableView::clearRowHeights()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView15clearRowHeightsEv(QQuickTableView *self) {
  self->clearRowHeights();
}

//  qreal QQuickTableView::explicitRowHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView17explicitRowHeightEi(
    const QQuickTableView *self,
    int row) {
  return self->explicitRowHeight(row);
}

//  void QQuickTableView::edit(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView4editERK11QModelIndex(
    QQuickTableView *self,
    const QModelIndex *index) {
  self->edit(*index);
}

//  void QQuickTableView::closeEditor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView11closeEditorEv(QQuickTableView *self) {
  self->closeEditor();
}

//  QQuickItem *QQuickTableView::itemAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickTableView11itemAtIndexERK11QModelIndex(
    const QQuickTableView *self,
    const QModelIndex *index) {
  return self->itemAtIndex(*index);
}

#if QT_DEPRECATED_SINCE(6, 5)
//  QQuickItem *QQuickTableView::itemAtCell(int column, int row) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickTableView10itemAtCellEii(
    const QQuickTableView *self,
    int column,
    int row) {
  return self->itemAtCell(column, row);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickTableView::positionViewAtCell(int column, int row,
//      QQuickFlickable::PositionMode mode, const QPointF &offset, const
//      QRectF &subRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView18positionViewAtCellEii6QFlagsIN15QQuickFlickable16PositionModeFlagEERK7QPointFRK6QRectF(
    QQuickTableView *self,
    int column,
    int row,
    int mode,
    const QPointF *offset,
    const QRectF *subRect) {
  self->positionViewAtCell(
      column,
      row,
      QFlags<QQuickFlickable::PositionModeFlag>::fromInt(mode),
      *offset,
      *subRect);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  void QQuickTableView::moveColumn(int source, int destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView10moveColumnEii(
    QQuickTableView *self,
    int source,
    int destination) {
  self->moveColumn(source, destination);
}

//  void QQuickTableView::moveRow(int source, int destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView7moveRowEii(
    QQuickTableView *self,
    int source,
    int destination) {
  self->moveRow(source, destination);
}

//  void QQuickTableView::clearColumnReordering()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView21clearColumnReorderingEv(
    QQuickTableView *self) {
  self->clearColumnReordering();
}

//  void QQuickTableView::clearRowReordering()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView18clearRowReorderingEv(
    QQuickTableView *self) {
  self->clearRowReordering();
}

//  QQuickTableViewAttached *QQuickTableView::qmlAttachedProperties(QObject
//      *a0)
extern "C" Q_DECL_EXPORT
QQuickTableViewAttached *ritual_ZN15QQuickTableView21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickTableView::qmlAttachedProperties(a0);
}

//  void QQuickTableView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView14geometryChangeERK6QRectFS2_(
    QQuickTableView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTableView::viewportMoved(Qt::Orientations orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickTableView *self,
    int orientation) {
  self->viewportMoved(QFlags<Qt::Orientation>::fromInt(orientation));
}

//  void QQuickTableView::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView13keyPressEventEP9QKeyEvent(
    QQuickTableView *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  bool QQuickTableView::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickTableView11eventFilterEP7QObjectP6QEvent(
    QQuickTableView *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

//  void QQuickTableView::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTableView18componentFinalizedEv(
    QQuickTableView *self) {
  self->componentFinalized();
}

//  QQuickTableViewPrivate *QQuickTableView::d_func()
extern "C" Q_DECL_EXPORT
QQuickTableViewPrivate *ritual_ZN15QQuickTableView6d_funcEv(
    QQuickTableView *self) {
  return self->d_func();
}

//  const QQuickTableViewPrivate *QQuickTableView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTableViewPrivate *ritual_ZNK15QQuickTableView6d_funcEv(
    const QQuickTableView *self) {
  return self->d_func();
}

//  qreal QQuickTableView::minXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView10minXExtentEv(
    const QQuickTableView *self) {
  return self->minXExtent();
}

//  qreal QQuickTableView::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView10maxXExtentEv(
    const QQuickTableView *self) {
  return self->maxXExtent();
}

//  qreal QQuickTableView::minYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView10minYExtentEv(
    const QQuickTableView *self) {
  return self->minYExtent();
}

//  qreal QQuickTableView::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTableView10maxYExtentEv(
    const QQuickTableView *self) {
  return self->maxYExtent();
}

//  QQuickTableView as the QQmlFinalizerHook it is built on
extern "C" Q_DECL_EXPORT
QQmlFinalizerHook *ritual_cast_QQuickTableView_QQmlFinalizerHook(
    QQuickTableView *self) {
  return static_cast<QQmlFinalizerHook *>(self);
}

//  a Python function taken by a CuteQQuickTableView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTableView(
    QQuickTableView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTableView *>(self)->take(key, call);
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QModelIndex QQuickTableView::modelIndex(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK15QQuickTableView10modelIndexEii(
    const QQuickTableView *self,
    int row,
    int column) {
  return new QModelIndex(self->QQuickTableView::modelIndex(row, column));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  QModelIndex QQuickTableView::modelIndex(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK15QQuickTableView10modelIndexERK6QPoint(
    const QQuickTableView *self,
    const QPoint *cell) {
  return new QModelIndex(self->QQuickTableView::modelIndex(*cell));
}

//  QPoint QQuickTableView::cellAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex(
    const QQuickTableView *self,
    const QModelIndex *index) {
  return new QPoint(self->QQuickTableView::cellAtIndex(*index));
}

//  void QQuickTableView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTableView14geometryChangeERK6QRectFS2_(
    QQuickTableView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTableView *>(self)->OwnQQuickTableView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTableView::viewportMoved(Qt::Orientations orientation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTableView13viewportMovedE6QFlagsIN2Qt11OrientationEE(
    QQuickTableView *self,
    int orientation) {
  static_cast<OwnQQuickTableView *>(self)->OwnQQuickTableView::viewportMoved(
      QFlags<Qt::Orientation>::fromInt(orientation));
}

//  void QQuickTableView::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTableView13keyPressEventEP9QKeyEvent(
    QQuickTableView *self,
    QKeyEvent *e) {
  static_cast<OwnQQuickTableView *>(self)->OwnQQuickTableView::keyPressEvent(
      e);
}

//  bool QQuickTableView::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickTableView11eventFilterEP7QObjectP6QEvent(
    QQuickTableView *self,
    QObject *obj,
    QEvent *event) {
  return static_cast<OwnQQuickTableView *>(self)->OwnQQuickTableView::eventFilter(
      obj,
      event);
}

//  void QQuickTableView::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTableView18componentFinalizedEv(
    QQuickTableView *self) {
  static_cast<OwnQQuickTableView *>(self)->OwnQQuickTableView::componentFinalized();
}

//  qreal QQuickTableView::minXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickTableView10minXExtentEv(
    const QQuickTableView *self) {
  return self->QQuickTableView::minXExtent();
}

//  qreal QQuickTableView::maxXExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickTableView10maxXExtentEv(
    const QQuickTableView *self) {
  return self->QQuickTableView::maxXExtent();
}

//  qreal QQuickTableView::minYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickTableView10minYExtentEv(
    const QQuickTableView *self) {
  return self->QQuickTableView::minYExtent();
}

//  qreal QQuickTableView::maxYExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QQuickTableView10maxYExtentEv(
    const QQuickTableView *self) {
  return self->QQuickTableView::maxYExtent();
}

#endif  // QT_CONFIG(quick_tableview)
