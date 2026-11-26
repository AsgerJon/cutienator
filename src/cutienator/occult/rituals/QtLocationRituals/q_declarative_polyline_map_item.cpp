//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeopath.h>
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

//  Only a class built on QDeclarativePolylineMapItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativePolylineMapItem : QDeclarativePolylineMapItem {
  using QDeclarativePolylineMapItem::afterViewportChanged;
  using QDeclarativePolylineMapItem::geometryChange;
  using QDeclarativePolylineMapItem::updatePolish;
};

//  A QDeclarativePolylineMapItem that Python can take functions over in. Every QDeclarativePolylineMapItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePolylineMapItemCall0)(const void *, QDeclarativeGeoMap *, QGeoMap *, int *);
typedef void * (*CuteQDeclarativePolylineMapItemCall1)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativePolylineMapItemCall2)(const void *, const QPointF *, int *);
typedef const QGeoShape * (*CuteQDeclarativePolylineMapItemCall3)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall4)(const void *, const QGeoShape *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall5)(const void *, const QGeoMapViewportChangeEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall6)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall7)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall8)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef void * (*CuteQDeclarativePolylineMapItemCall9)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall10)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativePolylineMapItemCall11)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativePolylineMapItemCall12)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativePolylineMapItemCall13)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativePolylineMapItemCall14)(const void *, int *);
typedef void * (*CuteQDeclarativePolylineMapItemCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePolylineMapItemCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePolylineMapItemCall17)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall18)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall19)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall21)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativePolylineMapItemCall22)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativePolylineMapItemCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall29)(const void *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall30)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativePolylineMapItemCall31)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativePolylineMapItemCall32)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall33)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall34)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall35)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativePolylineMapItemCall36)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativePolylineMapItemCall37)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativePolylineMapItemCall38)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativePolylineMapItemCall39)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativePolylineMapItemCall40)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativePolylineMapItemCall41)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePolylineMapItemCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePolylineMapItemCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePolylineMapItemCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePolylineMapItemCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePolylineMapItemCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePolylineMapItemCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativePolylineMapItem : public QDeclarativePolylineMapItem {
public:
  using QDeclarativePolylineMapItem::QDeclarativePolylineMapItem;
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
      CuteQDeclarativePolylineMapItemCall0 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall0>(taken[0]);
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
      CuteQDeclarativePolylineMapItemCall1 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall1>(taken[1]);
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
      CuteQDeclarativePolylineMapItemCall2 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativePolylineMapItem::contains(point);
  }

  //  const QGeoShape &QDeclarativePolylineMapItem::geoShape() const
  const QGeoShape &geoShape() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall3 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall3>(taken[3]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativePolylineMapItem::geoShape();
  }

  //  void QDeclarativePolylineMapItem::setGeoShape(const QGeoShape &shape)
  void setGeoShape(const QGeoShape &shape) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall4 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall4>(taken[4]);
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
      CuteQDeclarativePolylineMapItemCall5 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall5>(taken[5]);
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
      CuteQDeclarativePolylineMapItemCall6 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall6>(taken[6]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QDeclarativePolylineMapItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QDeclarativePolylineMapItem::updatePolish()
  void updatePolish() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall7 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall7>(taken[7]);
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
      CuteQDeclarativePolylineMapItemCall8 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall8>(taken[8]);
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
      CuteQDeclarativePolylineMapItemCall9 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall9>(taken[9]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updatePaintNode(a0, a1);
  }

  //  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
  void afterChildrenChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall10 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::afterChildrenChanged();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall11 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall11>(taken[11]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall12 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall12>(taken[12]);
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
      CuteQDeclarativePolylineMapItemCall13 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall13>(taken[13]);
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
      CuteQDeclarativePolylineMapItemCall14 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall15 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall15>(taken[15]);
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
      CuteQDeclarativePolylineMapItemCall16 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall16>(taken[16]);
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
      CuteQDeclarativePolylineMapItemCall17 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall17>(taken[17]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall18 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall19 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall20 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall21 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall21>(taken[21]);
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
      CuteQDeclarativePolylineMapItemCall22 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall22>(taken[22]);
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
      CuteQDeclarativePolylineMapItemCall23 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall24 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall25 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall26 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall27 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall28 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall29 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall30 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall30>(taken[30]);
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
      CuteQDeclarativePolylineMapItemCall31 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall31>(taken[31]);
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
      CuteQDeclarativePolylineMapItemCall32 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall33 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall34 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall35 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall35>(taken[35]);
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
      CuteQDeclarativePolylineMapItemCall36 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall36>(taken[36]);
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
      CuteQDeclarativePolylineMapItemCall37 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall37>(taken[37]);
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
      CuteQDeclarativePolylineMapItemCall38 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall38>(taken[38]);
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
      CuteQDeclarativePolylineMapItemCall39 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall39>(taken[39]);
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
      CuteQDeclarativePolylineMapItemCall40 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall40>(taken[40]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativePolylineMapItemCall41 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall41>(taken[41]);
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
      CuteQDeclarativePolylineMapItemCall42 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall42>(taken[42]);
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
      CuteQDeclarativePolylineMapItemCall43 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall43>(taken[43]);
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
      CuteQDeclarativePolylineMapItemCall44 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall44>(taken[44]);
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
      CuteQDeclarativePolylineMapItemCall45 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall45>(taken[45]);
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
      CuteQDeclarativePolylineMapItemCall46 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall46>(taken[46]);
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
      CuteQDeclarativePolylineMapItemCall47 call = reinterpret_cast<CuteQDeclarativePolylineMapItemCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativePolylineMapItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDeclarativePolylineMapItem10metaObjectEv(
    const QDeclarativePolylineMapItem *self) {
  return self->metaObject();
}

//  void *QDeclarativePolylineMapItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QDeclarativePolylineMapItem11qt_metacastEPKc(
    QDeclarativePolylineMapItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativePolylineMapItem::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDeclarativePolylineMapItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativePolylineMapItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativePolylineMapItem::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDeclarativePolylineMapItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativePolylineMapItem::tr(s, c, n));
}

//  QDeclarativePolylineMapItem::QDeclarativePolylineMapItem(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativePolylineMapItem *ritual_ZN27QDeclarativePolylineMapItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativePolylineMapItem(parent);
}

//  QDeclarativePolylineMapItem::~QDeclarativePolylineMapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItemD1Ev(
    QDeclarativePolylineMapItem *self) {
  delete self;
}

//  void QDeclarativePolylineMapItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativePolylineMapItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->setMap(quickMap, map);
}

//  QSGNode *QDeclarativePolylineMapItem::updateMapItemPaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN27QDeclarativePolylineMapItem22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolylineMapItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updateMapItemPaintNode(a0, a1);
}

//  int QDeclarativePolylineMapItem::pathLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDeclarativePolylineMapItem10pathLengthEv(
    const QDeclarativePolylineMapItem *self) {
  return self->pathLength();
}

//  void QDeclarativePolylineMapItem::addCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem13addCoordinateERK14QGeoCoordinate(
    QDeclarativePolylineMapItem *self,
    const QGeoCoordinate *coordinate) {
  self->addCoordinate(*coordinate);
}

//  void QDeclarativePolylineMapItem::insertCoordinate(int index, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem16insertCoordinateEiRK14QGeoCoordinate(
    QDeclarativePolylineMapItem *self,
    int index,
    const QGeoCoordinate *coordinate) {
  self->insertCoordinate(index, *coordinate);
}

//  void QDeclarativePolylineMapItem::replaceCoordinate(int index, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem17replaceCoordinateEiRK14QGeoCoordinate(
    QDeclarativePolylineMapItem *self,
    int index,
    const QGeoCoordinate *coordinate) {
  self->replaceCoordinate(index, *coordinate);
}

//  QGeoCoordinate QDeclarativePolylineMapItem::coordinateAt(int index) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK27QDeclarativePolylineMapItem12coordinateAtEi(
    const QDeclarativePolylineMapItem *self,
    int index) {
  return new QGeoCoordinate(self->coordinateAt(index));
}

//  bool QDeclarativePolylineMapItem::containsCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDeclarativePolylineMapItem18containsCoordinateERK14QGeoCoordinate(
    QDeclarativePolylineMapItem *self,
    const QGeoCoordinate *coordinate) {
  return self->containsCoordinate(*coordinate);
}

//  void QDeclarativePolylineMapItem::removeCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem16removeCoordinateERK14QGeoCoordinate(
    QDeclarativePolylineMapItem *self,
    const QGeoCoordinate *coordinate) {
  self->removeCoordinate(*coordinate);
}

//  void QDeclarativePolylineMapItem::removeCoordinate(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem16removeCoordinateEi(
    QDeclarativePolylineMapItem *self,
    int index) {
  self->removeCoordinate(index);
}

//  QList<QGeoCoordinate> QDeclarativePolylineMapItem::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK27QDeclarativePolylineMapItem4pathEv(
    const QDeclarativePolylineMapItem *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  void QDeclarativePolylineMapItem::setPath(const QList<QGeoCoordinate>
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem7setPathERK5QListI14QGeoCoordinateE(
    QDeclarativePolylineMapItem *self,
    const QList<QGeoCoordinate> *value) {
  self->setPath(*value);
}

//  void QDeclarativePolylineMapItem::setPath(const QGeoPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem7setPathERK8QGeoPath(
    QDeclarativePolylineMapItem *self,
    const QGeoPath *path) {
  self->setPath(*path);
}

//  bool QDeclarativePolylineMapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativePolylineMapItem8containsERK7QPointF(
    const QDeclarativePolylineMapItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  const QGeoShape &QDeclarativePolylineMapItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK27QDeclarativePolylineMapItem8geoShapeEv(
    const QDeclarativePolylineMapItem *self) {
  return new QGeoShape(self->geoShape());
}

//  void QDeclarativePolylineMapItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem11setGeoShapeERK9QGeoShape(
    QDeclarativePolylineMapItem *self,
    const QGeoShape *shape) {
  self->setGeoShape(*shape);
}

//  QDeclarativeMapLineProperties *QDeclarativePolylineMapItem::line()
extern "C" Q_DECL_EXPORT
QDeclarativeMapLineProperties *ritual_ZN27QDeclarativePolylineMapItem4lineEv(
    QDeclarativePolylineMapItem *self) {
  return self->line();
}

//  void QDeclarativePolylineMapItem::pathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem11pathChangedEv(
    QDeclarativePolylineMapItem *self) {
  self->pathChanged();
}

//  void QDeclarativePolylineMapItem::updateAfterLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem32updateAfterLinePropertiesChangedEv(
    QDeclarativePolylineMapItem *self) {
  self->updateAfterLinePropertiesChanged();
}

//  void QDeclarativePolylineMapItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativePolylineMapItem *self,
    const QGeoMapViewportChangeEvent *event) {
  self->afterViewportChanged(*event);
}

//  void QDeclarativePolylineMapItem::geometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem14geometryChangeERK6QRectFS2_(
    QDeclarativePolylineMapItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QDeclarativePolylineMapItem::setPathFromGeoList(const
//      QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem18setPathFromGeoListERK5QListI14QGeoCoordinateE(
    QDeclarativePolylineMapItem *self,
    const QList<QGeoCoordinate> *path) {
  self->setPathFromGeoList(*path);
}

//  void QDeclarativePolylineMapItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePolylineMapItem12updatePolishEv(
    QDeclarativePolylineMapItem *self) {
  self->updatePolish();
}

//  a Python function taken by a CuteQDeclarativePolylineMapItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePolylineMapItem(
    QDeclarativePolylineMapItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePolylineMapItem *>(self)->take(key, call);
}

//  void QDeclarativePolylineMapItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativePolylineMapItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativePolylineMapItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->QDeclarativePolylineMapItem::setMap(quickMap, map);
}

//  QSGNode *QDeclarativePolylineMapItem::updateMapItemPaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN27QDeclarativePolylineMapItem22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativePolylineMapItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QDeclarativePolylineMapItem::updateMapItemPaintNode(a0, a1);
}

//  bool QDeclarativePolylineMapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QDeclarativePolylineMapItem8containsERK7QPointF(
    const QDeclarativePolylineMapItem *self,
    const QPointF *point) {
  return self->QDeclarativePolylineMapItem::contains(*point);
}

//  const QGeoShape &QDeclarativePolylineMapItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK27QDeclarativePolylineMapItem8geoShapeEv(
    const QDeclarativePolylineMapItem *self) {
  return new QGeoShape(self->QDeclarativePolylineMapItem::geoShape());
}

//  void QDeclarativePolylineMapItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativePolylineMapItem11setGeoShapeERK9QGeoShape(
    QDeclarativePolylineMapItem *self,
    const QGeoShape *shape) {
  self->QDeclarativePolylineMapItem::setGeoShape(*shape);
}

//  void QDeclarativePolylineMapItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativePolylineMapItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativePolylineMapItem *self,
    const QGeoMapViewportChangeEvent *event) {
  static_cast<OwnQDeclarativePolylineMapItem *>(self)->OwnQDeclarativePolylineMapItem::afterViewportChanged(
      *event);
}

//  void QDeclarativePolylineMapItem::geometryChange(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativePolylineMapItem14geometryChangeERK6QRectFS2_(
    QDeclarativePolylineMapItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQDeclarativePolylineMapItem *>(self)->OwnQDeclarativePolylineMapItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QDeclarativePolylineMapItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativePolylineMapItem12updatePolishEv(
    QDeclarativePolylineMapItem *self) {
  static_cast<OwnQDeclarativePolylineMapItem *>(self)->OwnQDeclarativePolylineMapItem::updatePolish();
}
