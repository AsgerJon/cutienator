//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmap_p_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  Only a class built on QGeoTiledMapPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGeoTiledMapPrivate : QGeoTiledMapPrivate {
  using QGeoTiledMapPrivate::changeViewportSize;
  using QGeoTiledMapPrivate::changeCameraData;
  using QGeoTiledMapPrivate::changeActiveMapType;
  using QGeoTiledMapPrivate::setVisibleArea;
  using QGeoTiledMapPrivate::visibleArea;
};

//  A QGeoTiledMapPrivate that Python can take functions over in. Every QGeoTiledMapPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoTiledMapPrivateCall0)(const void *, const QSize *, int *);
typedef void (*CuteQGeoTiledMapPrivateCall1)(const void *, const QGeoCameraData *, int *);
typedef void (*CuteQGeoTiledMapPrivateCall2)(const void *, const QGeoMapType *, int *);
typedef void (*CuteQGeoTiledMapPrivateCall3)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQGeoTiledMapPrivateCall4)(const void *, int *);
typedef int (*CuteQGeoTiledMapPrivateCall5)(const void *, int *);
typedef void (*CuteQGeoTiledMapPrivateCall6)(const void *, QDeclarativeGeoMapItemBase *, int *);
typedef void (*CuteQGeoTiledMapPrivateCall7)(const void *, QDeclarativeGeoMapItemBase *, int *);
typedef double (*CuteQGeoTiledMapPrivateCall8)(const void *, int *);
typedef double (*CuteQGeoTiledMapPrivateCall9)(const void *, int *);
typedef void (*CuteQGeoTiledMapPrivateCall10)(const void *, bool, int *);
typedef bool (*CuteQGeoTiledMapPrivateCall11)(const void *, int *);
typedef double (*CuteQGeoTiledMapPrivateCall12)(const void *, const QGeoCameraData *, int *);
typedef double (*CuteQGeoTiledMapPrivateCall13)(const void *, const QGeoCameraData *, int *);
class CuteQGeoTiledMapPrivate : public QGeoTiledMapPrivate {
public:
  using QGeoTiledMapPrivate::QGeoTiledMapPrivate;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate18changeViewportSizeERK5QSize")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate16changeCameraDataERK14QGeoCameraData")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate19changeActiveMapTypeERK11QGeoMapType")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate11visibleAreaEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate21supportedMapItemTypesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapItemBase")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoMapItemBase")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate8mapWidthEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate9mapHeightEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate19setCopyrightVisibleEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate16copyrightVisibleEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14QGeoCameraData")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14QGeoCameraData")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  void QGeoTiledMapPrivate::changeViewportSize(const QSize &size)
  void changeViewportSize(const QSize &size) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall0 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall0>(taken[0]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QGeoTiledMapPrivate::changeViewportSize(size);
  }

  //  void QGeoTiledMapPrivate::changeCameraData(const QGeoCameraData
  //      &cameraData)
  void changeCameraData(const QGeoCameraData &cameraData) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall1 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall1>(taken[1]);
      call(this, &cameraData, &handled);
      if (handled) return;
    }
    QGeoTiledMapPrivate::changeCameraData(cameraData);
  }

  //  void QGeoTiledMapPrivate::changeActiveMapType(const QGeoMapType
  //      &mapType)
  void changeActiveMapType(const QGeoMapType &mapType) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall2 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall2>(taken[2]);
      call(this, &mapType, &handled);
      if (handled) return;
    }
    QGeoTiledMapPrivate::changeActiveMapType(mapType);
  }

  //  void QGeoTiledMapPrivate::setVisibleArea(const QRectF &visibleArea)
  void setVisibleArea(const QRectF &visibleArea) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall3 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall3>(taken[3]);
      call(this, &visibleArea, &handled);
      if (handled) return;
    }
    QGeoTiledMapPrivate::setVisibleArea(visibleArea);
  }

  //  QRectF QGeoTiledMapPrivate::visibleArea() const
  QRectF visibleArea() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall4 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoTiledMapPrivate::visibleArea();
  }

  //  QGeoMap::ItemTypes QGeoMapPrivate::supportedMapItemTypes() const
  QGeoMap::ItemTypes supportedMapItemTypes() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall5 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoMap::ItemType>::fromInt(given);
    }
    return QGeoMapPrivate::supportedMapItemTypes();
  }

  //  void QGeoMapPrivate::addMapItem(QDeclarativeGeoMapItemBase *item)
  void addMapItem(QDeclarativeGeoMapItemBase *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall6 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::addMapItem(item);
  }

  //  void QGeoMapPrivate::removeMapItem(QDeclarativeGeoMapItemBase *item)
  void removeMapItem(QDeclarativeGeoMapItemBase *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall7 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall7>(taken[7]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::removeMapItem(item);
  }

  //  double QGeoMapPrivate::mapWidth() const
  double mapWidth() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall8 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall8>(taken[8]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::mapWidth();
  }

  //  double QGeoMapPrivate::mapHeight() const
  double mapHeight() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall9 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall9>(taken[9]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::mapHeight();
  }

  //  void QGeoMapPrivate::setCopyrightVisible(bool visible)
  void setCopyrightVisible(bool visible) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall10 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall10>(taken[10]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::setCopyrightVisible(visible);
  }

  //  bool QGeoMapPrivate::copyrightVisible() const
  bool copyrightVisible() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall11 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::copyrightVisible();
  }

  //  double QGeoMapPrivate::maximumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double maximumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall12 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall12>(taken[12]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::maximumCenterLatitudeAtZoom(cameraData);
  }

  //  double QGeoMapPrivate::minimumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double minimumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoTiledMapPrivateCall13 call = reinterpret_cast<CuteQGeoTiledMapPrivateCall13>(taken[13]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::minimumCenterLatitudeAtZoom(cameraData);
  }
};

//  QGeoTiledMap *QGeoTiledMapPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGeoTiledMap *ritual_ZN19QGeoTiledMapPrivate6q_funcEv(
    QGeoTiledMapPrivate *self) {
  return self->q_func();
}

//  const QGeoTiledMap *QGeoTiledMapPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGeoTiledMap *ritual_ZNK19QGeoTiledMapPrivate6q_funcEv(
    const QGeoTiledMapPrivate *self) {
  return self->q_func();
}

//  QGeoTiledMapPrivate::QGeoTiledMapPrivate(QGeoTiledMappingManagerEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QGeoTiledMapPrivate *ritual_ZN19QGeoTiledMapPrivateC1EP29QGeoTiledMappingManagerEngine(
    QGeoTiledMappingManagerEngine *engine) {
  return new CuteQGeoTiledMapPrivate(engine);
}

//  QGeoTiledMapPrivate::~QGeoTiledMapPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivateD1Ev(QGeoTiledMapPrivate *self) {
  delete self;
}

//  QSGNode *QGeoTiledMapPrivate::updateSceneGraph(QSGNode *node,
//      QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN19QGeoTiledMapPrivate16updateSceneGraphEP7QSGNodeP12QQuickWindow(
    QGeoTiledMapPrivate *self,
    QSGNode *node,
    QQuickWindow *window) {
  return self->updateSceneGraph(node, window);
}

//  void QGeoTiledMapPrivate::updateTile(const QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate10updateTileERK12QGeoTileSpec(
    QGeoTiledMapPrivate *self,
    const QGeoTileSpec *spec) {
  self->updateTile(*spec);
}

//  void QGeoTiledMapPrivate::prefetchTiles()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate13prefetchTilesEv(
    QGeoTiledMapPrivate *self) {
  self->prefetchTiles();
}

//  QGeoMapType QGeoTiledMapPrivate::activeMapType() const
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZNK19QGeoTiledMapPrivate13activeMapTypeEv(
    const QGeoTiledMapPrivate *self) {
  return new QGeoMapType(self->activeMapType());
}

//  void QGeoTiledMapPrivate::onCameraCapabilitiesChanged(const
//      QGeoCameraCapabilities &oldCameraCapabilities)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate27onCameraCapabilitiesChangedERK22QGeoCameraCapabilities(
    QGeoTiledMapPrivate *self,
    const QGeoCameraCapabilities *oldCameraCapabilities) {
  self->onCameraCapabilitiesChanged(*oldCameraCapabilities);
}

//  void QGeoTiledMapPrivate::changeViewportSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate18changeViewportSizeERK5QSize(
    QGeoTiledMapPrivate *self,
    const QSize *size) {
  self->changeViewportSize(*size);
}

//  void QGeoTiledMapPrivate::changeCameraData(const QGeoCameraData
//      &cameraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate16changeCameraDataERK14QGeoCameraData(
    QGeoTiledMapPrivate *self,
    const QGeoCameraData *cameraData) {
  self->changeCameraData(*cameraData);
}

//  void QGeoTiledMapPrivate::changeActiveMapType(const QGeoMapType &mapType)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate19changeActiveMapTypeERK11QGeoMapType(
    QGeoTiledMapPrivate *self,
    const QGeoMapType *mapType) {
  self->changeActiveMapType(*mapType);
}

//  void QGeoTiledMapPrivate::changeTileVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate17changeTileVersionEi(
    QGeoTiledMapPrivate *self,
    int version) {
  self->changeTileVersion(version);
}

//  void QGeoTiledMapPrivate::clearScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate10clearSceneEv(
    QGeoTiledMapPrivate *self) {
  self->clearScene();
}

//  void QGeoTiledMapPrivate::updateScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate11updateSceneEv(
    QGeoTiledMapPrivate *self) {
  self->updateScene();
}

//  void QGeoTiledMapPrivate::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTiledMapPrivate14setVisibleAreaERK6QRectF(
    QGeoTiledMapPrivate *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  QRectF QGeoTiledMapPrivate::visibleArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGeoTiledMapPrivate11visibleAreaEv(
    const QGeoTiledMapPrivate *self) {
  return new QRectF(self->visibleArea());
}

//  a Python function taken by a CuteQGeoTiledMapPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMapPrivate(
    QGeoTiledMapPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMapPrivate *>(self)->take(key, call);
}

//  void QGeoTiledMapPrivate::changeViewportSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoTiledMapPrivate18changeViewportSizeERK5QSize(
    QGeoTiledMapPrivate *self,
    const QSize *size) {
  static_cast<OwnQGeoTiledMapPrivate *>(self)->OwnQGeoTiledMapPrivate::changeViewportSize(
      *size);
}

//  void QGeoTiledMapPrivate::changeCameraData(const QGeoCameraData
//      &cameraData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoTiledMapPrivate16changeCameraDataERK14QGeoCameraData(
    QGeoTiledMapPrivate *self,
    const QGeoCameraData *cameraData) {
  static_cast<OwnQGeoTiledMapPrivate *>(self)->OwnQGeoTiledMapPrivate::changeCameraData(
      *cameraData);
}

//  void QGeoTiledMapPrivate::changeActiveMapType(const QGeoMapType &mapType)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoTiledMapPrivate19changeActiveMapTypeERK11QGeoMapType(
    QGeoTiledMapPrivate *self,
    const QGeoMapType *mapType) {
  static_cast<OwnQGeoTiledMapPrivate *>(self)->OwnQGeoTiledMapPrivate::changeActiveMapType(
      *mapType);
}

//  void QGeoTiledMapPrivate::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoTiledMapPrivate14setVisibleAreaERK6QRectF(
    QGeoTiledMapPrivate *self,
    const QRectF *visibleArea) {
  static_cast<OwnQGeoTiledMapPrivate *>(self)->OwnQGeoTiledMapPrivate::setVisibleArea(
      *visibleArea);
}

//  QRectF QGeoTiledMapPrivate::visibleArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QGeoTiledMapPrivate11visibleAreaEv(
    const QGeoTiledMapPrivate *self) {
  return new QRectF(
      static_cast<const OwnQGeoTiledMapPrivate *>(self)->OwnQGeoTiledMapPrivate::visibleArea());
}
