//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktreeview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktreeview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTreeView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTreeView : QQuickTreeView {
  using QQuickTreeView::keyPressEvent;
};

//  A QQuickTreeView that Python can take functions over in. Every QQuickTreeView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_tableview)
typedef const QModelIndex * (*CuteQQuickTreeViewCall0)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef const QPoint * (*CuteQQuickTreeViewCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
typedef const QModelIndex * (*CuteQQuickTreeViewCall2)(const void *, int, int, int *);
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTreeViewCall3)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTreeViewCall4)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTreeViewCall5)(const void *, int, int *);
#endif  // QT_CONFIG(quick_tableview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
typedef bool (*CuteQQuickTreeViewCall6)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(quick_tableview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTreeViewCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTreeViewCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTreeViewCall9)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTreeViewCall10)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickTreeViewCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickTreeViewCall12)(const void *, qreal, int *);
typedef void (*CuteQQuickTreeViewCall13)(const void *, qreal, int *);
typedef qreal (*CuteQQuickTreeViewCall14)(const void *, int *);
typedef qreal (*CuteQQuickTreeViewCall15)(const void *, int *);
typedef bool (*CuteQQuickTreeViewCall16)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTreeViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTreeViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTreeViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTreeViewCall20)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTreeViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall23)(const void *, int *);
typedef void (*CuteQQuickTreeViewCall24)(const void *, int *);
typedef const QRectF * (*CuteQQuickTreeViewCall25)(const void *, int *);
typedef const QRectF * (*CuteQQuickTreeViewCall26)(const void *, int *);
typedef bool (*CuteQQuickTreeViewCall27)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTreeViewCall28)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickTreeViewCall29)(const void *, int *);
typedef void * (*CuteQQuickTreeViewCall30)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTreeViewCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall32)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTreeViewCall33)(const void *, int *);
typedef void (*CuteQQuickTreeViewCall34)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTreeViewCall35)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTreeViewCall36)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTreeViewCall37)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTreeViewCall38)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTreeViewCall39)(const void *, int *);
typedef void (*CuteQQuickTreeViewCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTreeViewCall41)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTreeViewCall42)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTreeViewCall43)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTreeViewCall44)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTreeViewCall45)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTreeViewCall46)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickTreeViewCall47)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTreeViewCall48)(const void *, int *);
typedef void (*CuteQQuickTreeViewCall49)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTreeViewCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTreeView : public QQuickTreeView {
public:
  using QQuickTreeView::QQuickTreeView;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickTableView10modelIndexERK6QPoint")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
    if (!std::strcmp(key, "_ZNK15QQuickTableView10modelIndexEii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
    if (!std::strcmp(key, "_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE")) {
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
  //  QModelIndex QQuickTreeView::modelIndex(const QPoint &cell) const
  QModelIndex modelIndex(const QPoint &cell) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTreeViewCall0 call = reinterpret_cast<CuteQQuickTreeViewCall0>(taken[0]);
      const QModelIndex * given = call(this, &cell, &handled);
      if (handled && given) return *given;
    }
    return QQuickTreeView::modelIndex(cell);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  QPoint QQuickTreeView::cellAtIndex(const QModelIndex &index) const
  QPoint cellAtIndex(const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTreeViewCall1 call = reinterpret_cast<CuteQQuickTreeViewCall1>(taken[1]);
      const QPoint * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QQuickTreeView::cellAtIndex(index);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
  //  QModelIndex QQuickTreeView::modelIndex(int row, int column) const
  QModelIndex modelIndex(int row, int column) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTreeViewCall2 call = reinterpret_cast<CuteQQuickTreeViewCall2>(taken[2]);
      const QModelIndex * given = call(this, row, column, &handled);
      if (handled && given) return *given;
    }
    return QQuickTreeView::modelIndex(row, column);
  }
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)

  //  void QQuickTreeView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTreeViewCall3 call = reinterpret_cast<CuteQQuickTreeViewCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTreeView::keyPressEvent(event);
  }

#if QT_CONFIG(quick_tableview)
  //  void QQuickTableView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTreeViewCall4 call = reinterpret_cast<CuteQQuickTreeViewCall4>(taken[4]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTableView::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quick_tableview)

#if QT_CONFIG(quick_tableview)
  //  void QQuickTableView::viewportMoved(Qt::Orientations orientation)
  void viewportMoved(Qt::Orientations orientation) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTreeViewCall5 call = reinterpret_cast<CuteQQuickTreeViewCall5>(taken[5]);
      call(this, static_cast<int>(orientation.toInt()), &handled);
      if (handled) return;
    }
    QQuickTableView::viewportMoved(orientation);
  }
#endif  // QT_CONFIG(quick_tableview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
  //  bool QQuickTableView::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTreeViewCall6 call = reinterpret_cast<CuteQQuickTreeViewCall6>(taken[6]);
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
      CuteQQuickTreeViewCall7 call = reinterpret_cast<CuteQQuickTreeViewCall7>(taken[7]);
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
      CuteQQuickTreeViewCall8 call = reinterpret_cast<CuteQQuickTreeViewCall8>(taken[8]);
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
      CuteQQuickTreeViewCall9 call = reinterpret_cast<CuteQQuickTreeViewCall9>(taken[9]);
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
      CuteQQuickTreeViewCall10 call = reinterpret_cast<CuteQQuickTreeViewCall10>(taken[10]);
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
      CuteQQuickTreeViewCall11 call = reinterpret_cast<CuteQQuickTreeViewCall11>(taken[11]);
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
      CuteQQuickTreeViewCall12 call = reinterpret_cast<CuteQQuickTreeViewCall12>(taken[12]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentX(pos);
  }

  //  void QQuickFlickable::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTreeViewCall13 call = reinterpret_cast<CuteQQuickTreeViewCall13>(taken[13]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentY(pos);
  }

  //  qreal QQuickFlickable::originY() const
  qreal originY() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTreeViewCall14 call = reinterpret_cast<CuteQQuickTreeViewCall14>(taken[14]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::originY();
  }

  //  qreal QQuickFlickable::originX() const
  qreal originX() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTreeViewCall15 call = reinterpret_cast<CuteQQuickTreeViewCall15>(taken[15]);
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
      CuteQQuickTreeViewCall16 call = reinterpret_cast<CuteQQuickTreeViewCall16>(taken[16]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTreeViewCall17 call = reinterpret_cast<CuteQQuickTreeViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTreeViewCall18 call = reinterpret_cast<CuteQQuickTreeViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTreeViewCall19 call = reinterpret_cast<CuteQQuickTreeViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTreeViewCall20 call = reinterpret_cast<CuteQQuickTreeViewCall20>(taken[20]);
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
      CuteQQuickTreeViewCall21 call = reinterpret_cast<CuteQQuickTreeViewCall21>(taken[21]);
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
      CuteQQuickTreeViewCall22 call = reinterpret_cast<CuteQQuickTreeViewCall22>(taken[22]);
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
      CuteQQuickTreeViewCall23 call = reinterpret_cast<CuteQQuickTreeViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::componentComplete();
  }

  //  void QQuickFlickable::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTreeViewCall24 call = reinterpret_cast<CuteQQuickTreeViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTreeViewCall25 call = reinterpret_cast<CuteQQuickTreeViewCall25>(taken[25]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTreeViewCall26 call = reinterpret_cast<CuteQQuickTreeViewCall26>(taken[26]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTreeViewCall27 call = reinterpret_cast<CuteQQuickTreeViewCall27>(taken[27]);
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
      CuteQQuickTreeViewCall28 call = reinterpret_cast<CuteQQuickTreeViewCall28>(taken[28]);
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
      CuteQQuickTreeViewCall29 call = reinterpret_cast<CuteQQuickTreeViewCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTreeViewCall30 call = reinterpret_cast<CuteQQuickTreeViewCall30>(taken[30]);
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
      CuteQQuickTreeViewCall31 call = reinterpret_cast<CuteQQuickTreeViewCall31>(taken[31]);
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
      CuteQQuickTreeViewCall32 call = reinterpret_cast<CuteQQuickTreeViewCall32>(taken[32]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTreeViewCall33 call = reinterpret_cast<CuteQQuickTreeViewCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTreeViewCall34 call = reinterpret_cast<CuteQQuickTreeViewCall34>(taken[34]);
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
      CuteQQuickTreeViewCall35 call = reinterpret_cast<CuteQQuickTreeViewCall35>(taken[35]);
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
      CuteQQuickTreeViewCall36 call = reinterpret_cast<CuteQQuickTreeViewCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTreeViewCall37 call = reinterpret_cast<CuteQQuickTreeViewCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTreeViewCall38 call = reinterpret_cast<CuteQQuickTreeViewCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTreeViewCall39 call = reinterpret_cast<CuteQQuickTreeViewCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTreeViewCall40 call = reinterpret_cast<CuteQQuickTreeViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTreeViewCall41 call = reinterpret_cast<CuteQQuickTreeViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickTreeViewCall42 call = reinterpret_cast<CuteQQuickTreeViewCall42>(taken[42]);
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
      CuteQQuickTreeViewCall43 call = reinterpret_cast<CuteQQuickTreeViewCall43>(taken[43]);
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
      CuteQQuickTreeViewCall44 call = reinterpret_cast<CuteQQuickTreeViewCall44>(taken[44]);
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
      CuteQQuickTreeViewCall45 call = reinterpret_cast<CuteQQuickTreeViewCall45>(taken[45]);
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
      CuteQQuickTreeViewCall46 call = reinterpret_cast<CuteQQuickTreeViewCall46>(taken[46]);
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
      CuteQQuickTreeViewCall47 call = reinterpret_cast<CuteQQuickTreeViewCall47>(taken[47]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickTreeViewCall48 call = reinterpret_cast<CuteQQuickTreeViewCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickTreeViewCall49 call = reinterpret_cast<CuteQQuickTreeViewCall49>(taken[49]);
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
      CuteQQuickTreeViewCall50 call = reinterpret_cast<CuteQQuickTreeViewCall50>(taken[50]);
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
      CuteQQuickTreeViewCall51 call = reinterpret_cast<CuteQQuickTreeViewCall51>(taken[51]);
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
      CuteQQuickTreeViewCall52 call = reinterpret_cast<CuteQQuickTreeViewCall52>(taken[52]);
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
      CuteQQuickTreeViewCall53 call = reinterpret_cast<CuteQQuickTreeViewCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTreeView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTreeView10metaObjectEv(
    const QQuickTreeView *self) {
  return self->metaObject();
}

//  QString QQuickTreeView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTreeView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTreeView::tr(s, c, n));
}

//  QQuickTreeView::QQuickTreeView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTreeView *ritual_ZN14QQuickTreeViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTreeView(parent);
}

//  QQuickTreeView::~QQuickTreeView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeViewD1Ev(QQuickTreeView *self) {
  delete self;
}

//  QModelIndex QQuickTreeView::rootIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QQuickTreeView9rootIndexEv(
    const QQuickTreeView *self) {
  return new QModelIndex(self->rootIndex());
}

//  void QQuickTreeView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView12setRootIndexERK11QModelIndex(
    QQuickTreeView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QQuickTreeView::resetRootIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView14resetRootIndexEv(QQuickTreeView *self) {
  self->resetRootIndex();
}

//  int QQuickTreeView::depth(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTreeView5depthEi(const QQuickTreeView *self, int row) {
  return self->depth(row);
}

//  bool QQuickTreeView::isExpanded(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTreeView10isExpandedEi(
    const QQuickTreeView *self,
    int row) {
  return self->isExpanded(row);
}

//  void QQuickTreeView::expand(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView6expandEi(QQuickTreeView *self, int row) {
  self->expand(row);
}

//  void QQuickTreeView::collapse(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView8collapseEi(QQuickTreeView *self, int row) {
  self->collapse(row);
}

//  void QQuickTreeView::toggleExpanded(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView14toggleExpandedEi(
    QQuickTreeView *self,
    int row) {
  self->toggleExpanded(row);
}

//  void QQuickTreeView::expandRecursively(int row, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView17expandRecursivelyEii(
    QQuickTreeView *self,
    int row,
    int depth) {
  self->expandRecursively(row, depth);
}

//  void QQuickTreeView::collapseRecursively(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView19collapseRecursivelyEi(
    QQuickTreeView *self,
    int row) {
  self->collapseRecursively(row);
}

//  void QQuickTreeView::expandToIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView13expandToIndexERK11QModelIndex(
    QQuickTreeView *self,
    const QModelIndex *index) {
  self->expandToIndex(*index);
}

//  QModelIndex QQuickTreeView::modelIndex(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QQuickTreeView10modelIndexERK6QPoint(
    const QQuickTreeView *self,
    const QPoint *cell) {
  return new QModelIndex(self->modelIndex(*cell));
}

//  QPoint QQuickTreeView::cellAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK14QQuickTreeView11cellAtIndexERK11QModelIndex(
    const QQuickTreeView *self,
    const QModelIndex *index) {
  return new QPoint(self->cellAtIndex(*index));
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QModelIndex QQuickTreeView::modelIndex(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QQuickTreeView10modelIndexEii(
    const QQuickTreeView *self,
    int row,
    int column) {
  return new QModelIndex(self->modelIndex(row, column));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  void QQuickTreeView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTreeView13keyPressEventEP9QKeyEvent(
    QQuickTreeView *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  QQuickTreeViewPrivate *QQuickTreeView::d_func()
extern "C" Q_DECL_EXPORT
QQuickTreeViewPrivate *ritual_ZN14QQuickTreeView6d_funcEv(
    QQuickTreeView *self) {
  return self->d_func();
}

//  const QQuickTreeViewPrivate *QQuickTreeView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTreeViewPrivate *ritual_ZNK14QQuickTreeView6d_funcEv(
    const QQuickTreeView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickTreeView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTreeView(
    QQuickTreeView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTreeView *>(self)->take(key, call);
}

//  QModelIndex QQuickTreeView::modelIndex(const QPoint &cell) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK14QQuickTreeView10modelIndexERK6QPoint(
    const QQuickTreeView *self,
    const QPoint *cell) {
  return new QModelIndex(self->QQuickTreeView::modelIndex(*cell));
}

//  QPoint QQuickTreeView::cellAtIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK14QQuickTreeView11cellAtIndexERK11QModelIndex(
    const QQuickTreeView *self,
    const QModelIndex *index) {
  return new QPoint(self->QQuickTreeView::cellAtIndex(*index));
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QModelIndex QQuickTreeView::modelIndex(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK14QQuickTreeView10modelIndexEii(
    const QQuickTreeView *self,
    int row,
    int column) {
  return new QModelIndex(self->QQuickTreeView::modelIndex(row, column));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  void QQuickTreeView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTreeView13keyPressEventEP9QKeyEvent(
    QQuickTreeView *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickTreeView *>(self)->OwnQQuickTreeView::keyPressEvent(
      event);
}
