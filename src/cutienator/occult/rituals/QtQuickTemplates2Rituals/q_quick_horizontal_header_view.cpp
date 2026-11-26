//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-25: the constructor taking a
//  QQuickHorizontalHeaderViewPrivate is left out: Qt's library does not
//  offer it. Kept as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickHorizontalHeaderView that Python can take functions over in. Every QQuickHorizontalHeaderView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_tableview)
#if QT_DEPRECATED_SINCE(6, 4)
typedef const QModelIndex * (*CuteQQuickHorizontalHeaderViewCall0)(const void *, int, int, int *);
#endif  // QT_DEPRECATED_SINCE(6, 4)
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef const QModelIndex * (*CuteQQuickHorizontalHeaderViewCall1)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef const QPoint * (*CuteQQuickHorizontalHeaderViewCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickHorizontalHeaderViewCall3)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickHorizontalHeaderViewCall4)(const void *, int, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickHorizontalHeaderViewCall5)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
typedef bool (*CuteQQuickHorizontalHeaderViewCall6)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(quick_tableview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickHorizontalHeaderViewCall7)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickHorizontalHeaderViewCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickHorizontalHeaderViewCall9)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickHorizontalHeaderViewCall10)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_tableview)
typedef qreal (*CuteQQuickHorizontalHeaderViewCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_tableview)
typedef void (*CuteQQuickHorizontalHeaderViewCall12)(const void *, qreal, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall13)(const void *, qreal, int *);
typedef qreal (*CuteQQuickHorizontalHeaderViewCall14)(const void *, int *);
typedef qreal (*CuteQQuickHorizontalHeaderViewCall15)(const void *, int *);
typedef bool (*CuteQQuickHorizontalHeaderViewCall16)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall20)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickHorizontalHeaderViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall23)(const void *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall24)(const void *, int *);
typedef const QRectF * (*CuteQQuickHorizontalHeaderViewCall25)(const void *, int *);
typedef const QRectF * (*CuteQQuickHorizontalHeaderViewCall26)(const void *, int *);
typedef bool (*CuteQQuickHorizontalHeaderViewCall27)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickHorizontalHeaderViewCall28)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickHorizontalHeaderViewCall29)(const void *, int *);
typedef void * (*CuteQQuickHorizontalHeaderViewCall30)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickHorizontalHeaderViewCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall32)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall33)(const void *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall34)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickHorizontalHeaderViewCall35)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickHorizontalHeaderViewCall36)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall37)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall38)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall39)(const void *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall40)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall41)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall42)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickHorizontalHeaderViewCall43)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickHorizontalHeaderViewCall44)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickHorizontalHeaderViewCall45)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickHorizontalHeaderViewCall46)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickHorizontalHeaderViewCall47)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall48)(const void *, int *);
typedef void (*CuteQQuickHorizontalHeaderViewCall49)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHorizontalHeaderViewCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickHorizontalHeaderView : public QQuickHorizontalHeaderView {
public:
  using QQuickHorizontalHeaderView::QQuickHorizontalHeaderView;
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
      CuteQQuickHorizontalHeaderViewCall0 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall0>(taken[0]);
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
      CuteQQuickHorizontalHeaderViewCall1 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall1>(taken[1]);
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
      CuteQQuickHorizontalHeaderViewCall2 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall2>(taken[2]);
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
      CuteQQuickHorizontalHeaderViewCall3 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall3>(taken[3]);
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
      CuteQQuickHorizontalHeaderViewCall4 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall4>(taken[4]);
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
      CuteQQuickHorizontalHeaderViewCall5 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall5>(taken[5]);
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
      CuteQQuickHorizontalHeaderViewCall6 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall6>(taken[6]);
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
      CuteQQuickHorizontalHeaderViewCall7 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall7>(taken[7]);
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
      CuteQQuickHorizontalHeaderViewCall8 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall8>(taken[8]);
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
      CuteQQuickHorizontalHeaderViewCall9 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall9>(taken[9]);
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
      CuteQQuickHorizontalHeaderViewCall10 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall10>(taken[10]);
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
      CuteQQuickHorizontalHeaderViewCall11 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall11>(taken[11]);
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
      CuteQQuickHorizontalHeaderViewCall12 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall12>(taken[12]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentX(pos);
  }

  //  void QQuickFlickable::setContentY(qreal pos)
  void setContentY(qreal pos) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall13 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall13>(taken[13]);
      call(this, pos, &handled);
      if (handled) return;
    }
    QQuickFlickable::setContentY(pos);
  }

  //  qreal QQuickFlickable::originY() const
  qreal originY() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall14 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall14>(taken[14]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::originY();
  }

  //  qreal QQuickFlickable::originX() const
  qreal originX() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall15 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall15>(taken[15]);
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
      CuteQQuickHorizontalHeaderViewCall16 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall16>(taken[16]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickFlickable::childMouseEventFilter(a0, a1);
  }

  //  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall17 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mousePressEvent(event);
  }

  //  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall18 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseMoveEvent(event);
  }

  //  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall19 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseReleaseEvent(event);
  }

  //  void QQuickFlickable::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall20 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall20>(taken[20]);
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
      CuteQQuickHorizontalHeaderViewCall21 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall21>(taken[21]);
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
      CuteQQuickHorizontalHeaderViewCall22 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall22>(taken[22]);
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
      CuteQQuickHorizontalHeaderViewCall23 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::componentComplete();
  }

  //  void QQuickFlickable::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall24 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFlickable::mouseUngrabEvent();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall25 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall25>(taken[25]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall26 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall26>(taken[26]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall27 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall27>(taken[27]);
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
      CuteQQuickHorizontalHeaderViewCall28 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall28>(taken[28]);
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
      CuteQQuickHorizontalHeaderViewCall29 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall30 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall30>(taken[30]);
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
      CuteQQuickHorizontalHeaderViewCall31 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall31>(taken[31]);
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
      CuteQQuickHorizontalHeaderViewCall32 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall32>(taken[32]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall33 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall34 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall34>(taken[34]);
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
      CuteQQuickHorizontalHeaderViewCall35 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall35>(taken[35]);
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
      CuteQQuickHorizontalHeaderViewCall36 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall37 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall38 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall39 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall40 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall41 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall42 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall42>(taken[42]);
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
      CuteQQuickHorizontalHeaderViewCall43 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall43>(taken[43]);
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
      CuteQQuickHorizontalHeaderViewCall44 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall44>(taken[44]);
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
      CuteQQuickHorizontalHeaderViewCall45 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall45>(taken[45]);
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
      CuteQQuickHorizontalHeaderViewCall46 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall46>(taken[46]);
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
      CuteQQuickHorizontalHeaderViewCall47 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall47>(taken[47]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall48 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickHorizontalHeaderViewCall49 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall49>(taken[49]);
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
      CuteQQuickHorizontalHeaderViewCall50 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall50>(taken[50]);
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
      CuteQQuickHorizontalHeaderViewCall51 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall51>(taken[51]);
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
      CuteQQuickHorizontalHeaderViewCall52 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall52>(taken[52]);
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
      CuteQQuickHorizontalHeaderViewCall53 call = reinterpret_cast<CuteQQuickHorizontalHeaderViewCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickHorizontalHeaderView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickHorizontalHeaderView10metaObjectEv(
    const QQuickHorizontalHeaderView *self) {
  return self->metaObject();
}

//  void *QQuickHorizontalHeaderView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuickHorizontalHeaderView11qt_metacastEPKc(
    QQuickHorizontalHeaderView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QQuickHorizontalHeaderView::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickHorizontalHeaderView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickHorizontalHeaderView::tr(s, c, n));
}

//  QQuickHorizontalHeaderViewPrivate *QQuickHorizontalHeaderView::d_func()
extern "C" Q_DECL_EXPORT
QQuickHorizontalHeaderViewPrivate *ritual_ZN26QQuickHorizontalHeaderView6d_funcEv(
    QQuickHorizontalHeaderView *self) {
  return self->d_func();
}

//  const QQuickHorizontalHeaderViewPrivate
//      *QQuickHorizontalHeaderView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickHorizontalHeaderViewPrivate *ritual_ZNK26QQuickHorizontalHeaderView6d_funcEv(
    const QQuickHorizontalHeaderView *self) {
  return self->d_func();
}

//  QQuickHorizontalHeaderView::QQuickHorizontalHeaderView(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickHorizontalHeaderView *ritual_ZN26QQuickHorizontalHeaderViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickHorizontalHeaderView(parent);
}

//  QQuickHorizontalHeaderView::~QQuickHorizontalHeaderView()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickHorizontalHeaderViewD1Ev(
    QQuickHorizontalHeaderView *self) {
  delete self;
}

//  bool QQuickHorizontalHeaderView::movableColumns() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickHorizontalHeaderView14movableColumnsEv(
    const QQuickHorizontalHeaderView *self) {
  return self->movableColumns();
}

//  void QQuickHorizontalHeaderView::setMovableColumns(bool movableColumns)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickHorizontalHeaderView17setMovableColumnsEb(
    QQuickHorizontalHeaderView *self,
    bool movableColumns) {
  self->setMovableColumns(movableColumns);
}

//  a Python function taken by a CuteQQuickHorizontalHeaderView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickHorizontalHeaderView(
    QQuickHorizontalHeaderView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickHorizontalHeaderView *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_tableview)
