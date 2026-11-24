//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomap_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomap_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeomap_p_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  Only a class built on QGeoMapPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGeoMapPrivate : QGeoMapPrivate {
  using QGeoMapPrivate::supportedMapItemTypes;
  using QGeoMapPrivate::addMapItem;
  using QGeoMapPrivate::removeMapItem;
  using QGeoMapPrivate::mapWidth;
  using QGeoMapPrivate::mapHeight;
  using QGeoMapPrivate::setCopyrightVisible;
  using QGeoMapPrivate::copyrightVisible;
  using QGeoMapPrivate::maximumCenterLatitudeAtZoom;
  using QGeoMapPrivate::minimumCenterLatitudeAtZoom;
  using QGeoMapPrivate::setVisibleArea;
  using QGeoMapPrivate::visibleArea;
};

//  A QGeoMapPrivate that Python can take functions over in. Every QGeoMapPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQGeoMapPrivateCall0)(const void *, int *);
typedef void (*CuteQGeoMapPrivateCall1)(const void *, QDeclarativeGeoMapItemBase *, int *);
typedef void (*CuteQGeoMapPrivateCall2)(const void *, QDeclarativeGeoMapItemBase *, int *);
typedef void (*CuteQGeoMapPrivateCall3)(const void *, const QSize *, int *);
typedef void (*CuteQGeoMapPrivateCall4)(const void *, const QGeoCameraData *, int *);
typedef void (*CuteQGeoMapPrivateCall5)(const void *, const QGeoMapType *, int *);
typedef double (*CuteQGeoMapPrivateCall6)(const void *, int *);
typedef double (*CuteQGeoMapPrivateCall7)(const void *, int *);
typedef void (*CuteQGeoMapPrivateCall8)(const void *, bool, int *);
typedef bool (*CuteQGeoMapPrivateCall9)(const void *, int *);
typedef double (*CuteQGeoMapPrivateCall10)(const void *, const QGeoCameraData *, int *);
typedef double (*CuteQGeoMapPrivateCall11)(const void *, const QGeoCameraData *, int *);
typedef void (*CuteQGeoMapPrivateCall12)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQGeoMapPrivateCall13)(const void *, int *);
class CuteQGeoMapPrivate : public QGeoMapPrivate {
public:
  using QGeoMapPrivate::QGeoMapPrivate;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate21supportedMapItemTypesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapItemBase")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoMapItemBase")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate18changeViewportSizeERK5QSize")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate16changeCameraDataERK14QGeoCameraData")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate19changeActiveMapTypeERK11QGeoMapType")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate8mapWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate9mapHeightEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate19setCopyrightVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate16copyrightVisibleEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14QGeoCameraData")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14QGeoCameraData")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QGeoMapPrivate11visibleAreaEv")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  QGeoMap::ItemTypes QGeoMapPrivate::supportedMapItemTypes() const
  QGeoMap::ItemTypes supportedMapItemTypes() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoMapPrivateCall0 call = reinterpret_cast<CuteQGeoMapPrivateCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoMap::ItemType>::fromInt(given);
    }
    return QGeoMapPrivate::supportedMapItemTypes();
  }

  //  void QGeoMapPrivate::addMapItem(QDeclarativeGeoMapItemBase *item)
  void addMapItem(QDeclarativeGeoMapItemBase *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoMapPrivateCall1 call = reinterpret_cast<CuteQGeoMapPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::addMapItem(item);
  }

  //  void QGeoMapPrivate::removeMapItem(QDeclarativeGeoMapItemBase *item)
  void removeMapItem(QDeclarativeGeoMapItemBase *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoMapPrivateCall2 call = reinterpret_cast<CuteQGeoMapPrivateCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::removeMapItem(item);
  }

  //  void QGeoMapPrivate::changeViewportSize(const QSize &size)
  void changeViewportSize(const QSize &size) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoMapPrivateCall3 call = reinterpret_cast<CuteQGeoMapPrivateCall3>(taken[3]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }

  //  void QGeoMapPrivate::changeCameraData(const QGeoCameraData
  //      &oldCameraData)
  void changeCameraData(const QGeoCameraData &oldCameraData) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoMapPrivateCall4 call = reinterpret_cast<CuteQGeoMapPrivateCall4>(taken[4]);
      call(this, &oldCameraData, &handled);
      if (handled) return;
    }
  }

  //  void QGeoMapPrivate::changeActiveMapType(const QGeoMapType &mapType)
  void changeActiveMapType(const QGeoMapType &mapType) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoMapPrivateCall5 call = reinterpret_cast<CuteQGeoMapPrivateCall5>(taken[5]);
      call(this, &mapType, &handled);
      if (handled) return;
    }
  }

  //  double QGeoMapPrivate::mapWidth() const
  double mapWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoMapPrivateCall6 call = reinterpret_cast<CuteQGeoMapPrivateCall6>(taken[6]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::mapWidth();
  }

  //  double QGeoMapPrivate::mapHeight() const
  double mapHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoMapPrivateCall7 call = reinterpret_cast<CuteQGeoMapPrivateCall7>(taken[7]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::mapHeight();
  }

  //  void QGeoMapPrivate::setCopyrightVisible(bool visible)
  void setCopyrightVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoMapPrivateCall8 call = reinterpret_cast<CuteQGeoMapPrivateCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::setCopyrightVisible(visible);
  }

  //  bool QGeoMapPrivate::copyrightVisible() const
  bool copyrightVisible() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoMapPrivateCall9 call = reinterpret_cast<CuteQGeoMapPrivateCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::copyrightVisible();
  }

  //  double QGeoMapPrivate::maximumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double maximumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoMapPrivateCall10 call = reinterpret_cast<CuteQGeoMapPrivateCall10>(taken[10]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::maximumCenterLatitudeAtZoom(cameraData);
  }

  //  double QGeoMapPrivate::minimumCenterLatitudeAtZoom(const
  //      QGeoCameraData &cameraData) const
  double minimumCenterLatitudeAtZoom(
      const QGeoCameraData &cameraData) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoMapPrivateCall11 call = reinterpret_cast<CuteQGeoMapPrivateCall11>(taken[11]);
      double given = call(this, &cameraData, &handled);
      if (handled) return given;
    }
    return QGeoMapPrivate::minimumCenterLatitudeAtZoom(cameraData);
  }

  //  void QGeoMapPrivate::setVisibleArea(const QRectF &visibleArea)
  void setVisibleArea(const QRectF &visibleArea) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoMapPrivateCall12 call = reinterpret_cast<CuteQGeoMapPrivateCall12>(taken[12]);
      call(this, &visibleArea, &handled);
      if (handled) return;
    }
    QGeoMapPrivate::setVisibleArea(visibleArea);
  }

  //  QRectF QGeoMapPrivate::visibleArea() const
  QRectF visibleArea() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoMapPrivateCall13 call = reinterpret_cast<CuteQGeoMapPrivateCall13>(taken[13]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoMapPrivate::visibleArea();
  }
};

//  QGeoMap *QGeoMapPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZN14QGeoMapPrivate6q_funcEv(QGeoMapPrivate *self) {
  return self->q_func();
}

//  const QGeoMap *QGeoMapPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGeoMap *ritual_ZNK14QGeoMapPrivate6q_funcEv(
    const QGeoMapPrivate *self) {
  return self->q_func();
}

//  QGeoMapPrivate::~QGeoMapPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivateD1Ev(QGeoMapPrivate *self) {
  delete self;
}

//  void QGeoMapPrivate::setCameraCapabilities(const QGeoCameraCapabilities
//      &cameraCapabilities)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate21setCameraCapabilitiesERK22QGeoCameraCapabilities(
    QGeoMapPrivate *self,
    const QGeoCameraCapabilities *cameraCapabilities) {
  self->setCameraCapabilities(*cameraCapabilities);
}

//  const QGeoCameraCapabilities &QGeoMapPrivate::cameraCapabilities() const
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZNK14QGeoMapPrivate18cameraCapabilitiesEv(
    const QGeoMapPrivate *self) {
  return new QGeoCameraCapabilities(self->cameraCapabilities());
}

//  QGeoMap::ItemTypes QGeoMapPrivate::supportedMapItemTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QGeoMapPrivate21supportedMapItemTypesEv(
    const QGeoMapPrivate *self) {
  return static_cast<int>(self->supportedMapItemTypes().toInt());
}

//  void QGeoMapPrivate::addMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapItemBase(
    QGeoMapPrivate *self,
    QDeclarativeGeoMapItemBase *item) {
  self->addMapItem(item);
}

//  void QGeoMapPrivate::removeMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoMapItemBase(
    QGeoMapPrivate *self,
    QDeclarativeGeoMapItemBase *item) {
  self->removeMapItem(item);
}

//  void QGeoMapPrivate::changeViewportSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate18changeViewportSizeERK5QSize(
    QGeoMapPrivate *self,
    const QSize *size) {
  self->changeViewportSize(*size);
}

//  void QGeoMapPrivate::changeCameraData(const QGeoCameraData
//      &oldCameraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate16changeCameraDataERK14QGeoCameraData(
    QGeoMapPrivate *self,
    const QGeoCameraData *oldCameraData) {
  self->changeCameraData(*oldCameraData);
}

//  void QGeoMapPrivate::changeActiveMapType(const QGeoMapType &mapType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate19changeActiveMapTypeERK11QGeoMapType(
    QGeoMapPrivate *self,
    const QGeoMapType *mapType) {
  self->changeActiveMapType(*mapType);
}

//  double QGeoMapPrivate::mapWidth() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoMapPrivate8mapWidthEv(const QGeoMapPrivate *self) {
  return self->mapWidth();
}

//  double QGeoMapPrivate::mapHeight() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoMapPrivate9mapHeightEv(const QGeoMapPrivate *self) {
  return self->mapHeight();
}

//  void QGeoMapPrivate::setCopyrightVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate19setCopyrightVisibleEb(
    QGeoMapPrivate *self,
    bool visible) {
  self->setCopyrightVisible(visible);
}

//  bool QGeoMapPrivate::copyrightVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGeoMapPrivate16copyrightVisibleEv(
    const QGeoMapPrivate *self) {
  return self->copyrightVisible();
}

//  double QGeoMapPrivate::maximumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoMapPrivate *self,
    const QGeoCameraData *cameraData) {
  return self->maximumCenterLatitudeAtZoom(*cameraData);
}

//  double QGeoMapPrivate::minimumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoMapPrivate *self,
    const QGeoCameraData *cameraData) {
  return self->minimumCenterLatitudeAtZoom(*cameraData);
}

//  void QGeoMapPrivate::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF(
    QGeoMapPrivate *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  QRectF QGeoMapPrivate::visibleArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QGeoMapPrivate11visibleAreaEv(
    const QGeoMapPrivate *self) {
  return new QRectF(self->visibleArea());
}

//  QRectF QGeoMapPrivate::clampVisibleArea(const QRectF &visibleArea) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QGeoMapPrivate16clampVisibleAreaERK6QRectF(
    const QGeoMapPrivate *self,
    const QRectF *visibleArea) {
  return new QRectF(self->clampVisibleArea(*visibleArea));
}

//  a Python function taken by a CuteQGeoMapPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMapPrivate(
    QGeoMapPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMapPrivate *>(self)->take(key, call);
}

//  QGeoMap::ItemTypes QGeoMapPrivate::supportedMapItemTypes() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QGeoMapPrivate21supportedMapItemTypesEv(
    const QGeoMapPrivate *self) {
  return static_cast<int>(
      static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::supportedMapItemTypes().toInt());
}

//  void QGeoMapPrivate::addMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapItemBase(
    QGeoMapPrivate *self,
    QDeclarativeGeoMapItemBase *item) {
  static_cast<OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::addMapItem(
      item);
}

//  void QGeoMapPrivate::removeMapItem(QDeclarativeGeoMapItemBase *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoMapItemBase(
    QGeoMapPrivate *self,
    QDeclarativeGeoMapItemBase *item) {
  static_cast<OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::removeMapItem(
      item);
}

//  double QGeoMapPrivate::mapWidth() const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK14QGeoMapPrivate8mapWidthEv(
    const QGeoMapPrivate *self) {
  return static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::mapWidth();
}

//  double QGeoMapPrivate::mapHeight() const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK14QGeoMapPrivate9mapHeightEv(
    const QGeoMapPrivate *self) {
  return static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::mapHeight();
}

//  void QGeoMapPrivate::setCopyrightVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGeoMapPrivate19setCopyrightVisibleEb(
    QGeoMapPrivate *self,
    bool visible) {
  static_cast<OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::setCopyrightVisible(
      visible);
}

//  bool QGeoMapPrivate::copyrightVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QGeoMapPrivate16copyrightVisibleEv(
    const QGeoMapPrivate *self) {
  return static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::copyrightVisible();
}

//  double QGeoMapPrivate::maximumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoMapPrivate *self,
    const QGeoCameraData *cameraData) {
  return static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::maximumCenterLatitudeAtZoom(
      *cameraData);
}

//  double QGeoMapPrivate::minimumCenterLatitudeAtZoom(const QGeoCameraData
//      &cameraData) const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14QGeoCameraData(
    const QGeoMapPrivate *self,
    const QGeoCameraData *cameraData) {
  return static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::minimumCenterLatitudeAtZoom(
      *cameraData);
}

//  void QGeoMapPrivate::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF(
    QGeoMapPrivate *self,
    const QRectF *visibleArea) {
  static_cast<OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::setVisibleArea(
      *visibleArea);
}

//  QRectF QGeoMapPrivate::visibleArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK14QGeoMapPrivate11visibleAreaEv(
    const QGeoMapPrivate *self) {
  return new QRectF(
      static_cast<const OwnQGeoMapPrivate *>(self)->OwnQGeoMapPrivate::visibleArea());
}
