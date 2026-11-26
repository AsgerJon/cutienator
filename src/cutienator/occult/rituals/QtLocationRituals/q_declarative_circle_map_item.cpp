//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDeclarativeCircleMapItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeCircleMapItem : QDeclarativeCircleMapItem {
  using QDeclarativeCircleMapItem::geometryChange;
  using QDeclarativeCircleMapItem::updatePolish;
  using QDeclarativeCircleMapItem::afterViewportChanged;
};

//  A QDeclarativeCircleMapItem that Python can take functions over in. Every QDeclarativeCircleMapItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeCircleMapItemCall0)(const void *, QDeclarativeGeoMap *, QGeoMap *, int *);
typedef void * (*CuteQDeclarativeCircleMapItemCall1)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef bool (*CuteQDeclarativeCircleMapItemCall2)(const void *, const QPointF *, int *);
typedef const QGeoShape * (*CuteQDeclarativeCircleMapItemCall3)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall4)(const void *, const QGeoShape *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall6)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall7)(const void *, const QGeoMapViewportChangeEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall8)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef void * (*CuteQDeclarativeCircleMapItemCall9)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall10)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeCircleMapItemCall11)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeCircleMapItemCall12)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeCircleMapItemCall13)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQDeclarativeCircleMapItemCall14)(const void *, int *);
typedef void * (*CuteQDeclarativeCircleMapItemCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeCircleMapItemCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCircleMapItemCall17)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall18)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall19)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall21)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeCircleMapItemCall22)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeCircleMapItemCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall29)(const void *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall30)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeCircleMapItemCall31)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeCircleMapItemCall32)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall33)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall34)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall35)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeCircleMapItemCall36)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeCircleMapItemCall37)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeCircleMapItemCall38)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeCircleMapItemCall39)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeCircleMapItemCall40)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeCircleMapItemCall41)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeCircleMapItemCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCircleMapItemCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCircleMapItemCall44)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCircleMapItemCall45)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCircleMapItemCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCircleMapItemCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeCircleMapItem : public QDeclarativeCircleMapItem {
public:
  using QDeclarativeCircleMapItem::QDeclarativeCircleMapItem;
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
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDeclarativeGeoMapItemBase20afterViewportChangedERK26QGeoMapViewportChangeEvent")) {
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

  //  void QDeclarativeCircleMapItem::setMap(QDeclarativeGeoMap *quickMap,
  //      QGeoMap *map)
  void setMap(QDeclarativeGeoMap *quickMap, QGeoMap *map) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall0 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall0>(taken[0]);
      call(this, quickMap, map, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItem::setMap(quickMap, map);
  }

  //  QSGNode *QDeclarativeCircleMapItem::updateMapItemPaintNode(QSGNode
  //      *a0, UpdatePaintNodeData *a1)
  QSGNode *updateMapItemPaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall1 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall1>(taken[1]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeCircleMapItem::updateMapItemPaintNode(a0, a1);
  }

  //  bool QDeclarativeCircleMapItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall2 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QDeclarativeCircleMapItem::contains(point);
  }

  //  const QGeoShape &QDeclarativeCircleMapItem::geoShape() const
  const QGeoShape &geoShape() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall3 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall3>(taken[3]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeCircleMapItem::geoShape();
  }

  //  void QDeclarativeCircleMapItem::setGeoShape(const QGeoShape &shape)
  void setGeoShape(const QGeoShape &shape) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall4 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall4>(taken[4]);
      call(this, &shape, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItem::setGeoShape(shape);
  }

  //  void QDeclarativeCircleMapItem::geometryChange(const QRectF
  //      &newGeometry, const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall5 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QDeclarativeCircleMapItem::updatePolish()
  void updatePolish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall6 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItem::updatePolish();
  }

  //  void QDeclarativeCircleMapItem::afterViewportChanged(const
  //      QGeoMapViewportChangeEvent &event)
  void afterViewportChanged(
      const QGeoMapViewportChangeEvent &event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall7 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall7>(taken[7]);
      call(this, &event, &handled);
      if (handled) return;
    }
    QDeclarativeCircleMapItem::afterViewportChanged(event);
  }

  //  void QDeclarativeGeoMapItemBase::setPositionOnMap(const
  //      QGeoCoordinate &coordinate, const QPointF &offset)
  void setPositionOnMap(
      const QGeoCoordinate &coordinate,
      const QPointF &offset) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall8 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall8>(taken[8]);
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
      CuteQDeclarativeCircleMapItemCall9 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall9>(taken[9]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QDeclarativeGeoMapItemBase::updatePaintNode(a0, a1);
  }

  //  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
  void afterChildrenChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall10 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemBase::afterChildrenChanged();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall11 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall11>(taken[11]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall12 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall12>(taken[12]);
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
      CuteQDeclarativeCircleMapItemCall13 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall13>(taken[13]);
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
      CuteQDeclarativeCircleMapItemCall14 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall15 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall15>(taken[15]);
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
      CuteQDeclarativeCircleMapItemCall16 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall16>(taken[16]);
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
      CuteQDeclarativeCircleMapItemCall17 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall17>(taken[17]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall18 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall19 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall20 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall21 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall21>(taken[21]);
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
      CuteQDeclarativeCircleMapItemCall22 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall22>(taken[22]);
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
      CuteQDeclarativeCircleMapItemCall23 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall24 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall25 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall26 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall27 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall28 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall29 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall30 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall30>(taken[30]);
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
      CuteQDeclarativeCircleMapItemCall31 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall31>(taken[31]);
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
      CuteQDeclarativeCircleMapItemCall32 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall33 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall34 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall35 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall35>(taken[35]);
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
      CuteQDeclarativeCircleMapItemCall36 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall36>(taken[36]);
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
      CuteQDeclarativeCircleMapItemCall37 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall37>(taken[37]);
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
      CuteQDeclarativeCircleMapItemCall38 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall38>(taken[38]);
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
      CuteQDeclarativeCircleMapItemCall39 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall39>(taken[39]);
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
      CuteQDeclarativeCircleMapItemCall40 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall40>(taken[40]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativeCircleMapItemCall41 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall41>(taken[41]);
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
      CuteQDeclarativeCircleMapItemCall42 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall42>(taken[42]);
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
      CuteQDeclarativeCircleMapItemCall43 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall43>(taken[43]);
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
      CuteQDeclarativeCircleMapItemCall44 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall44>(taken[44]);
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
      CuteQDeclarativeCircleMapItemCall45 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall45>(taken[45]);
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
      CuteQDeclarativeCircleMapItemCall46 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall46>(taken[46]);
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
      CuteQDeclarativeCircleMapItemCall47 call = reinterpret_cast<CuteQDeclarativeCircleMapItemCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeCircleMapItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QDeclarativeCircleMapItem10metaObjectEv(
    const QDeclarativeCircleMapItem *self) {
  return self->metaObject();
}

//  void *QDeclarativeCircleMapItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QDeclarativeCircleMapItem11qt_metacastEPKc(
    QDeclarativeCircleMapItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeCircleMapItem::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QDeclarativeCircleMapItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeCircleMapItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeCircleMapItem::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QDeclarativeCircleMapItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeCircleMapItem::tr(s, c, n));
}

//  QDeclarativeCircleMapItem::QDeclarativeCircleMapItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeCircleMapItem *ritual_ZN25QDeclarativeCircleMapItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeCircleMapItem(parent);
}

//  QDeclarativeCircleMapItem::~QDeclarativeCircleMapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItemD1Ev(
    QDeclarativeCircleMapItem *self) {
  delete self;
}

//  void QDeclarativeCircleMapItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeCircleMapItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->setMap(quickMap, map);
}

//  QSGNode *QDeclarativeCircleMapItem::updateMapItemPaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN25QDeclarativeCircleMapItem22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeCircleMapItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updateMapItemPaintNode(a0, a1);
}

//  QGeoCoordinate QDeclarativeCircleMapItem::center()
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN25QDeclarativeCircleMapItem6centerEv(
    QDeclarativeCircleMapItem *self) {
  return new QGeoCoordinate(self->center());
}

//  void QDeclarativeCircleMapItem::setCenter(const QGeoCoordinate &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem9setCenterERK14QGeoCoordinate(
    QDeclarativeCircleMapItem *self,
    const QGeoCoordinate *center) {
  self->setCenter(*center);
}

//  qreal QDeclarativeCircleMapItem::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QDeclarativeCircleMapItem6radiusEv(
    const QDeclarativeCircleMapItem *self) {
  return self->radius();
}

//  void QDeclarativeCircleMapItem::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem9setRadiusEd(
    QDeclarativeCircleMapItem *self,
    qreal radius) {
  self->setRadius(radius);
}

//  QColor QDeclarativeCircleMapItem::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QDeclarativeCircleMapItem5colorEv(
    const QDeclarativeCircleMapItem *self) {
  return new QColor(self->color());
}

//  void QDeclarativeCircleMapItem::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem8setColorERK6QColor(
    QDeclarativeCircleMapItem *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QDeclarativeMapLineProperties *QDeclarativeCircleMapItem::border()
extern "C" Q_DECL_EXPORT
QDeclarativeMapLineProperties *ritual_ZN25QDeclarativeCircleMapItem6borderEv(
    QDeclarativeCircleMapItem *self) {
  return self->border();
}

//  bool QDeclarativeCircleMapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QDeclarativeCircleMapItem8containsERK7QPointF(
    const QDeclarativeCircleMapItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  const QGeoShape &QDeclarativeCircleMapItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK25QDeclarativeCircleMapItem8geoShapeEv(
    const QDeclarativeCircleMapItem *self) {
  return new QGeoShape(self->geoShape());
}

//  void QDeclarativeCircleMapItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem11setGeoShapeERK9QGeoShape(
    QDeclarativeCircleMapItem *self,
    const QGeoShape *shape) {
  self->setGeoShape(*shape);
}

//  void QDeclarativeCircleMapItem::centerChanged(const QGeoCoordinate
//      &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem13centerChangedERK14QGeoCoordinate(
    QDeclarativeCircleMapItem *self,
    const QGeoCoordinate *center) {
  self->centerChanged(*center);
}

//  void QDeclarativeCircleMapItem::radiusChanged(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem13radiusChangedEd(
    QDeclarativeCircleMapItem *self,
    qreal radius) {
  self->radiusChanged(radius);
}

//  void QDeclarativeCircleMapItem::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem12colorChangedERK6QColor(
    QDeclarativeCircleMapItem *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QDeclarativeCircleMapItem::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem14geometryChangeERK6QRectFS2_(
    QDeclarativeCircleMapItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QDeclarativeCircleMapItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem12updatePolishEv(
    QDeclarativeCircleMapItem *self) {
  self->updatePolish();
}

//  void QDeclarativeCircleMapItem::markSourceDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem24markSourceDirtyAndUpdateEv(
    QDeclarativeCircleMapItem *self) {
  self->markSourceDirtyAndUpdate();
}

//  void QDeclarativeCircleMapItem::onLinePropertiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem23onLinePropertiesChangedEv(
    QDeclarativeCircleMapItem *self) {
  self->onLinePropertiesChanged();
}

//  void QDeclarativeCircleMapItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeCircleMapItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeCircleMapItem *self,
    const QGeoMapViewportChangeEvent *event) {
  self->afterViewportChanged(*event);
}

//  a Python function taken by a CuteQDeclarativeCircleMapItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeCircleMapItem(
    QDeclarativeCircleMapItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeCircleMapItem *>(self)->take(key, call);
}

//  void QDeclarativeCircleMapItem::setMap(QDeclarativeGeoMap *quickMap,
//      QGeoMap *map)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeCircleMapItem6setMapEP18QDeclarativeGeoMapP7QGeoMap(
    QDeclarativeCircleMapItem *self,
    QDeclarativeGeoMap *quickMap,
    QGeoMap *map) {
  self->QDeclarativeCircleMapItem::setMap(quickMap, map);
}

//  QSGNode *QDeclarativeCircleMapItem::updateMapItemPaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN25QDeclarativeCircleMapItem22updateMapItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QDeclarativeCircleMapItem *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QDeclarativeCircleMapItem::updateMapItemPaintNode(a0, a1);
}

//  bool QDeclarativeCircleMapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QDeclarativeCircleMapItem8containsERK7QPointF(
    const QDeclarativeCircleMapItem *self,
    const QPointF *point) {
  return self->QDeclarativeCircleMapItem::contains(*point);
}

//  const QGeoShape &QDeclarativeCircleMapItem::geoShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK25QDeclarativeCircleMapItem8geoShapeEv(
    const QDeclarativeCircleMapItem *self) {
  return new QGeoShape(self->QDeclarativeCircleMapItem::geoShape());
}

//  void QDeclarativeCircleMapItem::setGeoShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeCircleMapItem11setGeoShapeERK9QGeoShape(
    QDeclarativeCircleMapItem *self,
    const QGeoShape *shape) {
  self->QDeclarativeCircleMapItem::setGeoShape(*shape);
}

//  void QDeclarativeCircleMapItem::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeCircleMapItem14geometryChangeERK6QRectFS2_(
    QDeclarativeCircleMapItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQDeclarativeCircleMapItem *>(self)->OwnQDeclarativeCircleMapItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QDeclarativeCircleMapItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeCircleMapItem12updatePolishEv(
    QDeclarativeCircleMapItem *self) {
  static_cast<OwnQDeclarativeCircleMapItem *>(self)->OwnQDeclarativeCircleMapItem::updatePolish();
}

//  void QDeclarativeCircleMapItem::afterViewportChanged(const
//      QGeoMapViewportChangeEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeCircleMapItem20afterViewportChangedERK26QGeoMapViewportChangeEvent(
    QDeclarativeCircleMapItem *self,
    const QGeoMapViewportChangeEvent *event) {
  static_cast<OwnQDeclarativeCircleMapItem *>(self)->OwnQDeclarativeCircleMapItem::afterViewportChanged(
      *event);
}
