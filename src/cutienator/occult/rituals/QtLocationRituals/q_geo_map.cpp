//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomap_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qmargins.h>
#include <QtGui/qtransform.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoMap that Python can take functions over in. Every QGeoMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQGeoMapCall0)(const void *, int *);
typedef void (*CuteQGeoMapCall1)(const void *, int *);
typedef void (*CuteQGeoMapCall2)(const void *, int *);
typedef QString * (*CuteQGeoMapCall3)(const void *, int *);
typedef void (*CuteQGeoMapCall4)(const void *, bool, bool, bool, bool, bool, int *);
typedef bool (*CuteQGeoMapCall5)(const void *, QEvent *, int *);
typedef bool (*CuteQGeoMapCall6)(const void *, qreal, const QGeoCoordinate *, int *);
typedef const QGeoShape * (*CuteQGeoMapCall7)(const void *, int *);
typedef bool (*CuteQGeoMapCall8)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef bool (*CuteQGeoMapCall9)(const void *, const QGeoRectangle *, const QMargins *, int *);
typedef void (*CuteQGeoMapCall10)(const void *, bool, int *);
typedef void (*CuteQGeoMapCall11)(const void *, const QTransform *, int *);
typedef void * (*CuteQGeoMapCall12)(const void *, QSGNode *, QQuickWindow *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoMapCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoMapCall14)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMapCall15)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMapCall16)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMapCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMapCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMapCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoMap : public QGeoMap {
public:
  using QGeoMap::QGeoMap;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QGeoMap12capabilitiesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap12prefetchDataEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap9clearDataEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QGeoMap20copyrightsStyleSheetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap19setAcceptedGesturesEbbbbb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap11handleEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QGeoMap13visibleRegionEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectangleRK8QMargins")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap19setCopyrightVisibleEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap24setItemToWindowTransformERK10QTransform")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap16updateSceneGraphEP7QSGNodeP12QQuickWindow")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  Capabilities QGeoMap::capabilities() const
  QGeoMap::Capabilities capabilities() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoMapCall0 call = reinterpret_cast<CuteQGeoMapCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoMap::Capability>::fromInt(given);
    }
    return QGeoMap::capabilities();
  }

  //  void QGeoMap::prefetchData()
  void prefetchData() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoMapCall1 call = reinterpret_cast<CuteQGeoMapCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoMap::prefetchData();
  }

  //  void QGeoMap::clearData()
  void clearData() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoMapCall2 call = reinterpret_cast<CuteQGeoMapCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoMap::clearData();
  }

  //  QString QGeoMap::copyrightsStyleSheet() const
  QString copyrightsStyleSheet() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoMapCall3 call = reinterpret_cast<CuteQGeoMapCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGeoMap::copyrightsStyleSheet();
  }

  //  void QGeoMap::setAcceptedGestures(bool pan, bool flick, bool pinch,
  //      bool rotate, bool tilt)
  void setAcceptedGestures(
      bool pan,
      bool flick,
      bool pinch,
      bool rotate,
      bool tilt) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoMapCall4 call = reinterpret_cast<CuteQGeoMapCall4>(taken[4]);
      call(this, pan, flick, pinch, rotate, tilt, &handled);
      if (handled) return;
    }
    QGeoMap::setAcceptedGestures(pan, flick, pinch, rotate, tilt);
  }

  //  bool QGeoMap::handleEvent(QEvent *event)
  bool handleEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoMapCall5 call = reinterpret_cast<CuteQGeoMapCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGeoMap::handleEvent(event);
  }

  //  bool QGeoMap::setBearing(qreal bearing, const QGeoCoordinate
  //      &coordinate)
  bool setBearing(qreal bearing, const QGeoCoordinate &coordinate) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoMapCall6 call = reinterpret_cast<CuteQGeoMapCall6>(taken[6]);
      bool given = call(this, bearing, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoMap::setBearing(bearing, coordinate);
  }

  //  QGeoShape QGeoMap::visibleRegion() const
  QGeoShape visibleRegion() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoMapCall7 call = reinterpret_cast<CuteQGeoMapCall7>(taken[7]);
      const QGeoShape * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoMap::visibleRegion();
  }

  //  bool QGeoMap::anchorCoordinateToPoint(const QGeoCoordinate
  //      &coordinate, const QPointF &anchorPoint)
  bool anchorCoordinateToPoint(
      const QGeoCoordinate &coordinate,
      const QPointF &anchorPoint) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoMapCall8 call = reinterpret_cast<CuteQGeoMapCall8>(taken[8]);
      bool given = call(this, &coordinate, &anchorPoint, &handled);
      if (handled) return given;
    }
    return QGeoMap::anchorCoordinateToPoint(coordinate, anchorPoint);
  }

  //  bool QGeoMap::fitViewportToGeoRectangle(const QGeoRectangle
  //      &rectangle, const QMargins &borders)
  bool fitViewportToGeoRectangle(
      const QGeoRectangle &rectangle,
      const QMargins &borders) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoMapCall9 call = reinterpret_cast<CuteQGeoMapCall9>(taken[9]);
      bool given = call(this, &rectangle, &borders, &handled);
      if (handled) return given;
    }
    return QGeoMap::fitViewportToGeoRectangle(rectangle, borders);
  }

  //  void QGeoMap::setCopyrightVisible(bool visible)
  void setCopyrightVisible(bool visible) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoMapCall10 call = reinterpret_cast<CuteQGeoMapCall10>(taken[10]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QGeoMap::setCopyrightVisible(visible);
  }

  //  void QGeoMap::setItemToWindowTransform(const QTransform
  //      &itemToWindowTransform)
  void setItemToWindowTransform(
      const QTransform &itemToWindowTransform) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoMapCall11 call = reinterpret_cast<CuteQGeoMapCall11>(taken[11]);
      call(this, &itemToWindowTransform, &handled);
      if (handled) return;
    }
    QGeoMap::setItemToWindowTransform(itemToWindowTransform);
  }

  //  QSGNode *QGeoMap::updateSceneGraph(QSGNode *node, QQuickWindow
  //      *window)
  QSGNode *updateSceneGraph(QSGNode *node, QQuickWindow *window) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoMapCall12 call = reinterpret_cast<CuteQGeoMapCall12>(taken[12]);
      void * given = call(this, node, window, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoMapCall13 call = reinterpret_cast<CuteQGeoMapCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoMapCall14 call = reinterpret_cast<CuteQGeoMapCall14>(taken[14]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoMapCall15 call = reinterpret_cast<CuteQGeoMapCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoMapCall16 call = reinterpret_cast<CuteQGeoMapCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoMapCall17 call = reinterpret_cast<CuteQGeoMapCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoMapCall18 call = reinterpret_cast<CuteQGeoMapCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGeoMapCall19 call = reinterpret_cast<CuteQGeoMapCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoMap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QGeoMap10metaObjectEv(const QGeoMap *self) {
  return self->metaObject();
}

//  void *QGeoMap::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QGeoMap11qt_metacastEPKc(QGeoMap *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoMap::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QGeoMap11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoMap *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoMap::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QGeoMap2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QGeoMap::tr(s, c, n));
}

//  QGeoMapPrivate *QGeoMap::d_func()
extern "C" Q_DECL_EXPORT
QGeoMapPrivate *ritual_ZN7QGeoMap6d_funcEv(QGeoMap *self) {
  return self->d_func();
}

//  const QGeoMapPrivate *QGeoMap::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoMapPrivate *ritual_ZNK7QGeoMap6d_funcEv(const QGeoMap *self) {
  return self->d_func();
}

//  QGeoMap::~QGeoMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMapD1Ev(QGeoMap *self) {
  delete self;
}

//  void QGeoMap::setViewportSize(const QSize &viewportSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap15setViewportSizeERK5QSize(
    QGeoMap *self,
    const QSize *viewportSize) {
  self->setViewportSize(*viewportSize);
}

//  QSize QGeoMap::viewportSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QGeoMap12viewportSizeEv(const QGeoMap *self) {
  return new QSize(self->viewportSize());
}

//  int QGeoMap::viewportWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QGeoMap13viewportWidthEv(const QGeoMap *self) {
  return self->viewportWidth();
}

//  int QGeoMap::viewportHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QGeoMap14viewportHeightEv(const QGeoMap *self) {
  return self->viewportHeight();
}

//  const QGeoCameraData &QGeoMap::cameraData() const
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_ZNK7QGeoMap10cameraDataEv(const QGeoMap *self) {
  return new QGeoCameraData(self->cameraData());
}

//  QGeoCameraCapabilities QGeoMap::cameraCapabilities() const
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZNK7QGeoMap18cameraCapabilitiesEv(
    const QGeoMap *self) {
  return new QGeoCameraCapabilities(self->cameraCapabilities());
}

//  Capabilities QGeoMap::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QGeoMap12capabilitiesEv(const QGeoMap *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  void QGeoMap::setActiveMapType(const QGeoMapType &mapType)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap16setActiveMapTypeERK11QGeoMapType(
    QGeoMap *self,
    const QGeoMapType *mapType) {
  self->setActiveMapType(*mapType);
}

//  QGeoMapType QGeoMap::activeMapType() const
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZNK7QGeoMap13activeMapTypeEv(const QGeoMap *self) {
  return new QGeoMapType(self->activeMapType());
}

//  double QGeoMap::minimumZoom() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QGeoMap11minimumZoomEv(const QGeoMap *self) {
  return self->minimumZoom();
}

//  double QGeoMap::maximumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QGeoMap27maximumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoMap *self,
    const QGeoCameraData *cameraData) {
  return self->maximumCenterLatitudeAtZoom(*cameraData);
}

//  double QGeoMap::minimumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QGeoMap27minimumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoMap *self,
    const QGeoCameraData *cameraData) {
  return self->minimumCenterLatitudeAtZoom(*cameraData);
}

//  double QGeoMap::mapWidth() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QGeoMap8mapWidthEv(const QGeoMap *self) {
  return self->mapWidth();
}

//  double QGeoMap::mapHeight() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QGeoMap9mapHeightEv(const QGeoMap *self) {
  return self->mapHeight();
}

//  const QGeoProjection &QGeoMap::geoProjection() const
extern "C" Q_DECL_EXPORT
const QGeoProjection *ritual_ZNK7QGeoMap13geoProjectionEv(
    const QGeoMap *self) {
  return &(self->geoProjection());
}

//  void QGeoMap::prefetchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap12prefetchDataEv(QGeoMap *self) {
  self->prefetchData();
}

//  void QGeoMap::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap9clearDataEv(QGeoMap *self) {
  self->clearData();
}

//  ItemTypes QGeoMap::supportedMapItemTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QGeoMap21supportedMapItemTypesEv(const QGeoMap *self) {
  return static_cast<int>(self->supportedMapItemTypes().toInt());
}

//  void QGeoMap::addMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap10addMapItemEP26QDeclarativeGeoMapItemBase(
    QGeoMap *self,
    QDeclarativeGeoMapItemBase *item) {
  self->addMapItem(item);
}

//  void QGeoMap::removeMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap13removeMapItemEP26QDeclarativeGeoMapItemBase(
    QGeoMap *self,
    QDeclarativeGeoMapItemBase *item) {
  self->removeMapItem(item);
}

//  void QGeoMap::clearMapItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap13clearMapItemsEv(QGeoMap *self) {
  self->clearMapItems();
}

//  QString QGeoMap::copyrightsStyleSheet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QGeoMap20copyrightsStyleSheetEv(const QGeoMap *self) {
  return new QString(self->copyrightsStyleSheet());
}

//  void QGeoMap::setAcceptedGestures(bool pan, bool flick, bool pinch, bool
//      rotate, bool tilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap19setAcceptedGesturesEbbbbb(
    QGeoMap *self,
    bool pan,
    bool flick,
    bool pinch,
    bool rotate,
    bool tilt) {
  self->setAcceptedGestures(pan, flick, pinch, rotate, tilt);
}

//  bool QGeoMap::handleEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QGeoMap11handleEventEP6QEvent(QGeoMap *self, QEvent *event) {
  return self->handleEvent(event);
}

//  bool QGeoMap::setBearing(qreal bearing, const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate(
    QGeoMap *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  return self->setBearing(bearing, *coordinate);
}

//  QGeoShape QGeoMap::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK7QGeoMap13visibleRegionEv(const QGeoMap *self) {
  return new QGeoShape(self->visibleRegion());
}

//  bool QGeoMap::anchorCoordinateToPoint(const QGeoCoordinate &coordinate,
//      const QPointF &anchorPoint)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    QGeoMap *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint) {
  return self->anchorCoordinateToPoint(*coordinate, *anchorPoint);
}

//  bool QGeoMap::fitViewportToGeoRectangle(const QGeoRectangle &rectangle,
//      const QMargins &borders)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectangleRK8QMargins(
    QGeoMap *self,
    const QGeoRectangle *rectangle,
    const QMargins *borders) {
  return self->fitViewportToGeoRectangle(*rectangle, *borders);
}

//  void QGeoMap::setCopyrightVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap19setCopyrightVisibleEb(QGeoMap *self, bool visible) {
  self->setCopyrightVisible(visible);
}

//  void QGeoMap::setItemToWindowTransform(const QTransform
//      &itemToWindowTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap24setItemToWindowTransformERK10QTransform(
    QGeoMap *self,
    const QTransform *itemToWindowTransform) {
  self->setItemToWindowTransform(*itemToWindowTransform);
}

//  void QGeoMap::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap14setVisibleAreaERK6QRectF(
    QGeoMap *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  QRectF QGeoMap::visibleArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK7QGeoMap11visibleAreaEv(const QGeoMap *self) {
  return new QRectF(self->visibleArea());
}

//  QGeoMap::QGeoMap(QGeoMapPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZN7QGeoMapC1ER14QGeoMapPrivateP7QObject(
    QGeoMapPrivate *dd,
    QObject *parent) {
  return new CuteQGeoMap(*dd, parent);
}

//  void QGeoMap::setCameraData(const QGeoCameraData &cameraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap13setCameraDataERK14QGeoCameraData(
    QGeoMap *self,
    const QGeoCameraData *cameraData) {
  self->setCameraData(*cameraData);
}

//  void QGeoMap::setCameraCapabilities(const QGeoCameraCapabilities
//      &cameraCapabilities)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap21setCameraCapabilitiesERK22QGeoCameraCapabilities(
    QGeoMap *self,
    const QGeoCameraCapabilities *cameraCapabilities) {
  self->setCameraCapabilities(*cameraCapabilities);
}

//  QSGNode *QGeoMap::updateSceneGraph(QSGNode *node, QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN7QGeoMap16updateSceneGraphEP7QSGNodeP12QQuickWindow(
    QGeoMap *self,
    QSGNode *node,
    QQuickWindow *window) {
  return self->updateSceneGraph(node, window);
}

//  void QGeoMap::cameraDataChanged(const QGeoCameraData &cameraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap17cameraDataChangedERK14QGeoCameraData(
    QGeoMap *self,
    const QGeoCameraData *cameraData) {
  self->cameraDataChanged(*cameraData);
}

//  void QGeoMap::sgNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap13sgNodeChangedEv(QGeoMap *self) {
  self->sgNodeChanged();
}

//  void QGeoMap::activeMapTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap20activeMapTypeChangedEv(QGeoMap *self) {
  self->activeMapTypeChanged();
}

//  void QGeoMap::cameraCapabilitiesChanged(const QGeoCameraCapabilities
//      &oldCameraCapabilities)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap25cameraCapabilitiesChangedERK22QGeoCameraCapabilities(
    QGeoMap *self,
    const QGeoCameraCapabilities *oldCameraCapabilities) {
  self->cameraCapabilitiesChanged(*oldCameraCapabilities);
}

//  void QGeoMap::copyrightsImageChanged(const QImage &copyrightsImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap22copyrightsImageChangedERK6QImage(
    QGeoMap *self,
    const QImage *copyrightsImage) {
  self->copyrightsImageChanged(*copyrightsImage);
}

//  void QGeoMap::copyrightsChanged(const QString &copyrightsHtml)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap17copyrightsChangedERK7QString(
    QGeoMap *self,
    const QString *copyrightsHtml) {
  self->copyrightsChanged(*copyrightsHtml);
}

//  void QGeoMap::copyrightsStyleSheetChanged(const QString &styleSheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap27copyrightsStyleSheetChangedERK7QString(
    QGeoMap *self,
    const QString *styleSheet) {
  self->copyrightsStyleSheetChanged(*styleSheet);
}

//  void QGeoMap::visibleAreaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QGeoMap18visibleAreaChangedEv(QGeoMap *self) {
  self->visibleAreaChanged();
}

//  a Python function taken by a CuteQGeoMap, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMap(QGeoMap *self, const char *key, void *call) {
  return static_cast<CuteQGeoMap *>(self)->take(key, call);
}

//  Capabilities QGeoMap::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QGeoMap12capabilitiesEv(const QGeoMap *self) {
  return static_cast<int>(self->QGeoMap::capabilities().toInt());
}

//  void QGeoMap::prefetchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QGeoMap12prefetchDataEv(QGeoMap *self) {
  self->QGeoMap::prefetchData();
}

//  void QGeoMap::clearData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QGeoMap9clearDataEv(QGeoMap *self) {
  self->QGeoMap::clearData();
}

//  QString QGeoMap::copyrightsStyleSheet() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK7QGeoMap20copyrightsStyleSheetEv(
    const QGeoMap *self) {
  return new QString(self->QGeoMap::copyrightsStyleSheet());
}

//  void QGeoMap::setAcceptedGestures(bool pan, bool flick, bool pinch, bool
//      rotate, bool tilt)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QGeoMap19setAcceptedGesturesEbbbbb(
    QGeoMap *self,
    bool pan,
    bool flick,
    bool pinch,
    bool rotate,
    bool tilt) {
  self->QGeoMap::setAcceptedGestures(pan, flick, pinch, rotate, tilt);
}

//  bool QGeoMap::handleEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QGeoMap11handleEventEP6QEvent(
    QGeoMap *self,
    QEvent *event) {
  return self->QGeoMap::handleEvent(event);
}

//  bool QGeoMap::setBearing(qreal bearing, const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate(
    QGeoMap *self,
    qreal bearing,
    const QGeoCoordinate *coordinate) {
  return self->QGeoMap::setBearing(bearing, *coordinate);
}

//  QGeoShape QGeoMap::visibleRegion() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_own_ZNK7QGeoMap13visibleRegionEv(const QGeoMap *self) {
  return new QGeoShape(self->QGeoMap::visibleRegion());
}

//  bool QGeoMap::anchorCoordinateToPoint(const QGeoCoordinate &coordinate,
//      const QPointF &anchorPoint)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF(
    QGeoMap *self,
    const QGeoCoordinate *coordinate,
    const QPointF *anchorPoint) {
  return self->QGeoMap::anchorCoordinateToPoint(*coordinate, *anchorPoint);
}

//  bool QGeoMap::fitViewportToGeoRectangle(const QGeoRectangle &rectangle,
//      const QMargins &borders)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectangleRK8QMargins(
    QGeoMap *self,
    const QGeoRectangle *rectangle,
    const QMargins *borders) {
  return self->QGeoMap::fitViewportToGeoRectangle(*rectangle, *borders);
}

//  void QGeoMap::setCopyrightVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QGeoMap19setCopyrightVisibleEb(
    QGeoMap *self,
    bool visible) {
  self->QGeoMap::setCopyrightVisible(visible);
}

//  void QGeoMap::setItemToWindowTransform(const QTransform
//      &itemToWindowTransform)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QGeoMap24setItemToWindowTransformERK10QTransform(
    QGeoMap *self,
    const QTransform *itemToWindowTransform) {
  self->QGeoMap::setItemToWindowTransform(*itemToWindowTransform);
}
