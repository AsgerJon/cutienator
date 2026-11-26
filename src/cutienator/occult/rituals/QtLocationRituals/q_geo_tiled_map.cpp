//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qpoint.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qmargins.h>
#include <QtGui/qtransform.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGeoTiledMap may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGeoTiledMap : QGeoTiledMap {
  using QGeoTiledMap::updateSceneGraph;
};

//  A QGeoTiledMap that Python can take functions over in. Every QGeoTiledMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoTiledMapCall0)(const void *, int *);
typedef void (*CuteQGeoTiledMapCall1)(const void *, int *);
typedef int (*CuteQGeoTiledMapCall2)(const void *, int *);
typedef void (*CuteQGeoTiledMapCall3)(const void *, bool, int *);
typedef void (*CuteQGeoTiledMapCall4)(const void *, int, int *);
typedef void * (*CuteQGeoTiledMapCall5)(const void *, QSGNode *, QQuickWindow *, int *);
typedef QString * (*CuteQGeoTiledMapCall6)(const void *, int *);
typedef void (*CuteQGeoTiledMapCall7)(const void *, bool, bool, bool, bool, bool, int *);
typedef bool (*CuteQGeoTiledMapCall8)(const void *, QEvent *, int *);
typedef bool (*CuteQGeoTiledMapCall9)(const void *, qreal, const QGeoCoordinate *, int *);
typedef const QGeoShape * (*CuteQGeoTiledMapCall10)(const void *, int *);
typedef bool (*CuteQGeoTiledMapCall11)(const void *, const QGeoCoordinate *, const QPointF *, int *);
typedef bool (*CuteQGeoTiledMapCall12)(const void *, const QGeoRectangle *, const QMargins *, int *);
typedef void (*CuteQGeoTiledMapCall13)(const void *, const QTransform *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMapCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMapCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoTiledMap : public QGeoTiledMap {
public:
  using QGeoTiledMap::QGeoTiledMap;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QGeoMap12prefetchDataEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap9clearDataEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QGeoMap12capabilitiesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap19setCopyrightVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QGeoTiledMap10clearSceneEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap16updateSceneGraphEP7QSGNodeP12QQuickWindow")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QGeoMap20copyrightsStyleSheetEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap19setAcceptedGesturesEbbbbb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap11handleEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QGeoMap13visibleRegionEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinateRK7QPointF")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectangleRK8QMargins")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QGeoMap24setItemToWindowTransformERK10QTransform")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGeoTiledMap::prefetchData()
  void prefetchData() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTiledMapCall0 call = reinterpret_cast<CuteQGeoTiledMapCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoTiledMap::prefetchData();
  }

  //  void QGeoTiledMap::clearData()
  void clearData() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMapCall1 call = reinterpret_cast<CuteQGeoTiledMapCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoTiledMap::clearData();
  }

  //  Capabilities QGeoTiledMap::capabilities() const
  QGeoMap::Capabilities capabilities() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoTiledMapCall2 call = reinterpret_cast<CuteQGeoTiledMapCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoMap::Capability>::fromInt(given);
    }
    return QGeoTiledMap::capabilities();
  }

  //  void QGeoTiledMap::setCopyrightVisible(bool visible)
  void setCopyrightVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoTiledMapCall3 call = reinterpret_cast<CuteQGeoTiledMapCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QGeoTiledMap::setCopyrightVisible(visible);
  }

  //  void QGeoTiledMap::clearScene(int mapId)
  void clearScene(int mapId) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoTiledMapCall4 call = reinterpret_cast<CuteQGeoTiledMapCall4>(taken[4]);
      call(this, mapId, &handled);
      if (handled) return;
    }
    QGeoTiledMap::clearScene(mapId);
  }

  //  QSGNode *QGeoTiledMap::updateSceneGraph(QSGNode *a0, QQuickWindow
  //      *window)
  QSGNode *updateSceneGraph(QSGNode *a0, QQuickWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoTiledMapCall5 call = reinterpret_cast<CuteQGeoTiledMapCall5>(taken[5]);
      void * given = call(this, a0, window, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QGeoTiledMap::updateSceneGraph(a0, window);
  }

  //  QString QGeoMap::copyrightsStyleSheet() const
  QString copyrightsStyleSheet() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoTiledMapCall6 call = reinterpret_cast<CuteQGeoTiledMapCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQGeoTiledMapCall7 call = reinterpret_cast<CuteQGeoTiledMapCall7>(taken[7]);
      call(this, pan, flick, pinch, rotate, tilt, &handled);
      if (handled) return;
    }
    QGeoMap::setAcceptedGestures(pan, flick, pinch, rotate, tilt);
  }

  //  bool QGeoMap::handleEvent(QEvent *event)
  bool handleEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoTiledMapCall8 call = reinterpret_cast<CuteQGeoTiledMapCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGeoMap::handleEvent(event);
  }

  //  bool QGeoMap::setBearing(qreal bearing, const QGeoCoordinate
  //      &coordinate)
  bool setBearing(qreal bearing, const QGeoCoordinate &coordinate) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoTiledMapCall9 call = reinterpret_cast<CuteQGeoTiledMapCall9>(taken[9]);
      bool given = call(this, bearing, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoMap::setBearing(bearing, coordinate);
  }

  //  QGeoShape QGeoMap::visibleRegion() const
  QGeoShape visibleRegion() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoTiledMapCall10 call = reinterpret_cast<CuteQGeoTiledMapCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQGeoTiledMapCall11 call = reinterpret_cast<CuteQGeoTiledMapCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQGeoTiledMapCall12 call = reinterpret_cast<CuteQGeoTiledMapCall12>(taken[12]);
      bool given = call(this, &rectangle, &borders, &handled);
      if (handled) return given;
    }
    return QGeoMap::fitViewportToGeoRectangle(rectangle, borders);
  }

  //  void QGeoMap::setItemToWindowTransform(const QTransform
  //      &itemToWindowTransform)
  void setItemToWindowTransform(
      const QTransform &itemToWindowTransform) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoTiledMapCall13 call = reinterpret_cast<CuteQGeoTiledMapCall13>(taken[13]);
      call(this, &itemToWindowTransform, &handled);
      if (handled) return;
    }
    QGeoMap::setItemToWindowTransform(itemToWindowTransform);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoTiledMapCall14 call = reinterpret_cast<CuteQGeoTiledMapCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoTiledMapCall15 call = reinterpret_cast<CuteQGeoTiledMapCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoTiledMapCall16 call = reinterpret_cast<CuteQGeoTiledMapCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoTiledMapCall17 call = reinterpret_cast<CuteQGeoTiledMapCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoTiledMapCall18 call = reinterpret_cast<CuteQGeoTiledMapCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGeoTiledMapCall19 call = reinterpret_cast<CuteQGeoTiledMapCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGeoTiledMapCall20 call = reinterpret_cast<CuteQGeoTiledMapCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoTiledMap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QGeoTiledMap10metaObjectEv(
    const QGeoTiledMap *self) {
  return self->metaObject();
}

//  void *QGeoTiledMap::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QGeoTiledMap11qt_metacastEPKc(
    QGeoTiledMap *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoTiledMap::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QGeoTiledMap11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoTiledMap *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoTiledMap::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QGeoTiledMap2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoTiledMap::tr(s, c, n));
}

//  QGeoTiledMapPrivate *QGeoTiledMap::d_func()
extern "C" Q_DECL_EXPORT
QGeoTiledMapPrivate *ritual_ZN12QGeoTiledMap6d_funcEv(QGeoTiledMap *self) {
  return self->d_func();
}

//  const QGeoTiledMapPrivate *QGeoTiledMap::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoTiledMapPrivate *ritual_ZNK12QGeoTiledMap6d_funcEv(
    const QGeoTiledMap *self) {
  return self->d_func();
}

//  QGeoTiledMap::QGeoTiledMap(QGeoTiledMappingManagerEngine *engine, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoTiledMap *ritual_ZN12QGeoTiledMapC1EP29QGeoTiledMappingManagerEngineP7QObject(
    QGeoTiledMappingManagerEngine *engine,
    QObject *parent) {
  return new CuteQGeoTiledMap(engine, parent);
}

//  QGeoTiledMap::~QGeoTiledMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMapD1Ev(QGeoTiledMap *self) {
  delete self;
}

//  QAbstractGeoTileCache *QGeoTiledMap::tileCache()
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache *ritual_ZN12QGeoTiledMap9tileCacheEv(
    QGeoTiledMap *self) {
  return self->tileCache();
}

//  QGeoTileRequestManager *QGeoTiledMap::requestManager()
extern "C" Q_DECL_EXPORT
QGeoTileRequestManager *ritual_ZN12QGeoTiledMap14requestManagerEv(
    QGeoTiledMap *self) {
  return self->requestManager();
}

//  void QGeoTiledMap::updateTile(const QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap10updateTileERK12QGeoTileSpec(
    QGeoTiledMap *self,
    const QGeoTileSpec *spec) {
  self->updateTile(*spec);
}

//  void QGeoTiledMap::setPrefetchStyle(PrefetchStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap16setPrefetchStyleENS_13PrefetchStyleE(
    QGeoTiledMap *self,
    QGeoTiledMap::PrefetchStyle style) {
  self->setPrefetchStyle(style);
}

//  void QGeoTiledMap::prefetchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap12prefetchDataEv(QGeoTiledMap *self) {
  self->prefetchData();
}

//  void QGeoTiledMap::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap9clearDataEv(QGeoTiledMap *self) {
  self->clearData();
}

//  Capabilities QGeoTiledMap::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoTiledMap12capabilitiesEv(const QGeoTiledMap *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  void QGeoTiledMap::setCopyrightVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap19setCopyrightVisibleEb(
    QGeoTiledMap *self,
    bool visible) {
  self->setCopyrightVisible(visible);
}

//  void QGeoTiledMap::clearScene(int mapId)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap10clearSceneEi(QGeoTiledMap *self, int mapId) {
  self->clearScene(mapId);
}

//  QSGNode *QGeoTiledMap::updateSceneGraph(QSGNode *a0, QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN12QGeoTiledMap16updateSceneGraphEP7QSGNodeP12QQuickWindow(
    QGeoTiledMap *self,
    QSGNode *a0,
    QQuickWindow *window) {
  return self->updateSceneGraph(a0, window);
}

//  void QGeoTiledMap::evaluateCopyrights(const QSet<QGeoTileSpec>
//      &visibleTiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap18evaluateCopyrightsERK4QSetI12QGeoTileSpecE(
    QGeoTiledMap *self,
    const QSet<QGeoTileSpec> *visibleTiles) {
  self->evaluateCopyrights(*visibleTiles);
}

//  QGeoTiledMap::QGeoTiledMap(QGeoTiledMapPrivate &dd,
//      QGeoTiledMappingManagerEngine *engine, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoTiledMap *ritual_ZN12QGeoTiledMapC1ER19QGeoTiledMapPrivateP29QGeoTiledMappingManagerEngineP7QObject(
    QGeoTiledMapPrivate *dd,
    QGeoTiledMappingManagerEngine *engine,
    QObject *parent) {
  return new CuteQGeoTiledMap(*dd, engine, parent);
}

//  void QGeoTiledMap::handleTileVersionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTiledMap24handleTileVersionChangedEv(
    QGeoTiledMap *self) {
  self->handleTileVersionChanged();
}

//  a Python function taken by a CuteQGeoTiledMap, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMap(
    QGeoTiledMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMap *>(self)->take(key, call);
}

//  void QGeoTiledMap::prefetchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGeoTiledMap12prefetchDataEv(QGeoTiledMap *self) {
  self->QGeoTiledMap::prefetchData();
}

//  void QGeoTiledMap::clearData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGeoTiledMap9clearDataEv(QGeoTiledMap *self) {
  self->QGeoTiledMap::clearData();
}

//  Capabilities QGeoTiledMap::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QGeoTiledMap12capabilitiesEv(const QGeoTiledMap *self) {
  return static_cast<int>(self->QGeoTiledMap::capabilities().toInt());
}

//  void QGeoTiledMap::setCopyrightVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGeoTiledMap19setCopyrightVisibleEb(
    QGeoTiledMap *self,
    bool visible) {
  self->QGeoTiledMap::setCopyrightVisible(visible);
}

//  void QGeoTiledMap::clearScene(int mapId)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGeoTiledMap10clearSceneEi(
    QGeoTiledMap *self,
    int mapId) {
  self->QGeoTiledMap::clearScene(mapId);
}

//  QSGNode *QGeoTiledMap::updateSceneGraph(QSGNode *a0, QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN12QGeoTiledMap16updateSceneGraphEP7QSGNodeP12QQuickWindow(
    QGeoTiledMap *self,
    QSGNode *a0,
    QQuickWindow *window) {
  return static_cast<OwnQGeoTiledMap *>(self)->OwnQGeoTiledMap::updateSceneGraph(
      a0,
      window);
}
