//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QGeoTileSpec::QGeoTileSpec()
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_ZN12QGeoTileSpecC1Ev() {
  return new QGeoTileSpec();
}

//  QGeoTileSpec::QGeoTileSpec(const QGeoTileSpec &other)
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_ZN12QGeoTileSpecC1ERKS_(const QGeoTileSpec *other) {
  return new QGeoTileSpec(*other);
}

//  QGeoTileSpec::QGeoTileSpec(const QString &plugin, int mapId, int zoom,
//      int x, int y, int version)
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_ZN12QGeoTileSpecC1ERK7QStringiiiii(
    const QString *plugin,
    int mapId,
    int zoom,
    int x,
    int y,
    int version) {
  return new QGeoTileSpec(*plugin, mapId, zoom, x, y, version);
}

//  QGeoTileSpec::~QGeoTileSpec()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTileSpecD1Ev(QGeoTileSpec *self) {
  delete self;
}

//  QString QGeoTileSpec::plugin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QGeoTileSpec6pluginEv(const QGeoTileSpec *self) {
  return new QString(self->plugin());
}

//  void QGeoTileSpec::setZoom(int zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTileSpec7setZoomEi(QGeoTileSpec *self, int zoom) {
  self->setZoom(zoom);
}

//  int QGeoTileSpec::zoom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoTileSpec4zoomEv(const QGeoTileSpec *self) {
  return self->zoom();
}

//  void QGeoTileSpec::setX(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTileSpec4setXEi(QGeoTileSpec *self, int x) {
  self->setX(x);
}

//  int QGeoTileSpec::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoTileSpec1xEv(const QGeoTileSpec *self) {
  return self->x();
}

//  void QGeoTileSpec::setY(int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTileSpec4setYEi(QGeoTileSpec *self, int y) {
  self->setY(y);
}

//  int QGeoTileSpec::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoTileSpec1yEv(const QGeoTileSpec *self) {
  return self->y();
}

//  void QGeoTileSpec::setMapId(int mapId)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTileSpec8setMapIdEi(QGeoTileSpec *self, int mapId) {
  self->setMapId(mapId);
}

//  int QGeoTileSpec::mapId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoTileSpec5mapIdEv(const QGeoTileSpec *self) {
  return self->mapId();
}

//  void QGeoTileSpec::setVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoTileSpec10setVersionEi(QGeoTileSpec *self, int version) {
  self->setVersion(version);
}

//  int QGeoTileSpec::version() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoTileSpec7versionEv(const QGeoTileSpec *self) {
  return self->version();
}

//  bool operator==(const QGeoTileSpec &lhs, const QGeoTileSpec &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QGeoTileSpecS1_(
    const QGeoTileSpec *lhs,
    const QGeoTileSpec *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoTileSpec &lhs, const QGeoTileSpec &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QGeoTileSpecS1_(
    const QGeoTileSpec *lhs,
    const QGeoTileSpec *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QGeoTileSpec &lhs, const QGeoTileSpec &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK12QGeoTileSpecS1_(
    const QGeoTileSpec *lhs,
    const QGeoTileSpec *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool QGeoTileSpec::isEqual(const QGeoTileSpec &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGeoTileSpec7isEqualERKS_(
    const QGeoTileSpec *self,
    const QGeoTileSpec *rhs) {
  return self->isEqual(*rhs);
}

//  bool QGeoTileSpec::isLess(const QGeoTileSpec &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGeoTileSpec6isLessERKS_(
    const QGeoTileSpec *self,
    const QGeoTileSpec *rhs) {
  return self->isLess(*rhs);
}
