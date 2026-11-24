//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativeroutemapitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativeroutemapitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtLocation/qgeoroute.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeoshape.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDeclarativeRouteMapItem that Python can take functions over in. Every QDeclarativeRouteMapItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeRouteMapItemCall0)(const void *, QDeclarativeGeoMap *, QGeoMap *, int *);
typedef void * (*CuteQDeclarativeRouteMapItemCall1)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeRouteMapItemCall2)(const void *, const QPointF *, int *);
typedef const QGeoShape * (*CuteQDeclarativeRouteMapItemCall3)(const void *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall4)(const void *, const QGeoShape *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall5)(const void *, const QGeoMapViewportChangeEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall6)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall7)(const void *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall8)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef void * (*CuteQDeclarativeRouteMapItemCall9)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall10)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeRouteMapItemCall11)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeRouteMapItemCall12)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeRouteMapItemCall13)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeRouteMapItemCall14)(const void *, int *);
typedef void * (*CuteQDeclarativeRouteMapItemCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeRouteMapItemCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRouteMapItemCall17)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall18)(const void *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall19)(const void *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall21)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeRouteMapItemCall22)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeRouteMapItemCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall29)(const void *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall30)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeRouteMapItemCall31)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeRouteMapItemCall32)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall33)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall34)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall35)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRouteMapItemCall36)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRouteMapItemCall37)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRouteMapItemCall38)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeRouteMapItemCall39)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeRouteMapItemCall40)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeRouteMapItemCall41)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeRouteMapItemCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRouteMapItemCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRouteMapItemCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRouteMapItemCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRouteMapItemCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeRouteMapItemCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeRouteMapItem : public QDeclarativeRouteMapItem {
public:
  using QDeclarativeRouteMapItem::QDeclarativeRouteMapItem;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7QGeoMap")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase20afterViewportChangedERK26QGeoMapViewportChangeEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCoordinateRK7QPointF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDeclarativePolylineMapItem::setMap(QDeclarativeGeoMap
  //      *quickMap, QGeoMap *map)
  void setMap(QDeclarativeGeoMap *quickMap, QGeoMap *map) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall0 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall0>(taken[0]);
      call(this, quickMap, map, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItem::setMap(quickMap, map);
  }

  //  QSGNode *QDeclarativePolylineMapItem::updateMapItemPaintNode(QSGNode
  //      *a0, UpdatePaintNodeData *a1)
  QSGNode *updateMapItemPaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall1 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall1>(taken[1]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativePolylineMapItem::updateMapItemPaintNode(a0, a1);
  }

  //  bool QDeclarativePolylineMapItem::contains(const QPointF &point)
  //      const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall2 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativePolylineMapItem::contains(point);
  }

  //  const QGeoShape &QDeclarativePolylineMapItem::geoShape() const
  const QGeoShape &geoShape() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall3 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall3>(taken[3]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativePolylineMapItem::geoShape();
  }

  //  void QDeclarativePolylineMapItem::setGeoShape(const QGeoShape &shape)
  void setGeoShape(const QGeoShape &shape) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall4 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall4>(taken[4]);
      call(this, &shape, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItem::setGeoShape(shape);
  }

  //  void QDeclarativePolylineMapItem::afterViewportChanged(const
  //      QGeoMapViewportChangeEvent &event)
  void afterViewportChanged(
      const QGeoMapViewportChangeEvent &event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall5 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall5>(taken[5]);
      call(this, &event, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItem::afterViewportChanged(event);
  }

  //  void QDeclarativePolylineMapItem::geometryChange(const QRectF
  //      &newGeometry, const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall6 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall6>(taken[6]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QDeclarativePolylineMapItem::updatePolish()
  void updatePolish() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall7 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItem::updatePolish();
  }

  //  void QDeclarativeGeoMapItemBase::setPositionOnMap(const
  //      QGeoCoordinate &coordinate, const QPointF &offset)
  void setPositionOnMap(
      const QGeoCoordinate &coordinate,
      const QPointF &offset) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall8 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall8>(taken[8]);
      call(this, &coordinate, &offset, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::setPositionOnMap(coordinate, offset);
  }

  //  QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall9 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall9>(taken[9]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updatePaintNode(a0, a1);
  }

  //  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
  void afterChildrenChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall10 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::afterChildrenChanged();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall11 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall11>(taken[11]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall12 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall12>(taken[12]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall13 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall13>(taken[13]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall14 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall15 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall16 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall17 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall17>(taken[17]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall18 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall19 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall20 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall21 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall22 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall23 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall24 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall25 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall26 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall27 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall28 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall29 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall30 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall31 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall32 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall33 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall34 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall35 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall36 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall36>(taken[36]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall37 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall38 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall39 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall40 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall40>(taken[40]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall41 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall42 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall43 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall44 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall45 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall46 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDeclarativeRouteMapItemCall47 call = reinterpret_cast<CuteQDeclarativeRouteMapItemCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeRouteMapItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QDeclarativeRouteMapItem10metaObjectEv(
    const QDeclarativeRouteMapItem *self) {
  return self->metaObject();
}

//  QString QDeclarativeRouteMapItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QDeclarativeRouteMapItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeRouteMapItem::tr(s, c, n));
}

//  QDeclarativeRouteMapItem::QDeclarativeRouteMapItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeRouteMapItem *ritual_ZN24QDeclarativeRouteMapItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeRouteMapItem(parent);
}

//  QDeclarativeRouteMapItem::~QDeclarativeRouteMapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeRouteMapItemD1Ev(
    QDeclarativeRouteMapItem *self) {
  delete self;
}

//  QGeoRoute QDeclarativeRouteMapItem::route() const
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZNK24QDeclarativeRouteMapItem5routeEv(
    const QDeclarativeRouteMapItem *self) {
  return new QGeoRoute(self->route());
}

//  void QDeclarativeRouteMapItem::setRoute(const QGeoRoute &route)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeRouteMapItem8setRouteERK9QGeoRoute(
    QDeclarativeRouteMapItem *self,
    const QGeoRoute *route) {
  self->setRoute(*route);
}

//  void QDeclarativeRouteMapItem::updateRoutePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeRouteMapItem15updateRoutePathEv(
    QDeclarativeRouteMapItem *self) {
  self->updateRoutePath();
}

//  void QDeclarativeRouteMapItem::setPath(const QList<QGeoCoordinate>
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeRouteMapItem7setPathERK5QListI14QGeoCoordinateE(
    QDeclarativeRouteMapItem *self,
    const QList<QGeoCoordinate> *value) {
  self->setPath(*value);
}

//  a Python function taken by a CuteQDeclarativeRouteMapItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeRouteMapItem(
    QDeclarativeRouteMapItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeRouteMapItem *>(self)->take(key, call);
}
