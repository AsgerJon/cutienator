//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformsurfacecapture_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformsurfacecapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QPlatformSurfaceCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPlatformSurfaceCapture10metaObjectEv(
    const QPlatformSurfaceCapture *self) {
  return self->metaObject();
}

//  QString QPlatformSurfaceCapture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QPlatformSurfaceCapture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformSurfaceCapture::tr(s, c, n));
}

//  void QPlatformSurfaceCapture::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture9setActiveEb(
    QPlatformSurfaceCapture *self,
    bool active) {
  self->setActive(active);
}

//  bool QPlatformSurfaceCapture::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformSurfaceCapture8isActiveEv(
    const QPlatformSurfaceCapture *self) {
  return self->isActive();
}

//  Error QPlatformSurfaceCapture::error() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture::Error ritual_ZNK23QPlatformSurfaceCapture5errorEv(
    const QPlatformSurfaceCapture *self) {
  return self->error();
}

//  QString QPlatformSurfaceCapture::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QPlatformSurfaceCapture11errorStringEv(
    const QPlatformSurfaceCapture *self) {
  return new QString(self->errorString());
}

//  void QPlatformSurfaceCapture::setIgnoreCursor(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture15setIgnoreCursorEb(
    QPlatformSurfaceCapture *self,
    bool a0) {
  self->setIgnoreCursor(a0);
}

//  bool QPlatformSurfaceCapture::ignoreCursor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformSurfaceCapture12ignoreCursorEv(
    const QPlatformSurfaceCapture *self) {
  return self->ignoreCursor();
}

//  void QPlatformSurfaceCapture::setIgnoreDropShadow(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture19setIgnoreDropShadowEb(
    QPlatformSurfaceCapture *self,
    bool a0) {
  self->setIgnoreDropShadow(a0);
}

//  bool QPlatformSurfaceCapture::ignoreDropShadow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformSurfaceCapture16ignoreDropShadowEv(
    const QPlatformSurfaceCapture *self) {
  return self->ignoreDropShadow();
}

//  bool QPlatformSurfaceCapture::setActiveInternal(bool a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPlatformSurfaceCapture17setActiveInternalEb(
    QPlatformSurfaceCapture *self,
    bool a0) {
  return self->setActiveInternal(a0);
}

//  void QPlatformSurfaceCapture::updateError(Error error, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture11updateErrorENS_5ErrorERK7QString(
    QPlatformSurfaceCapture *self,
    QPlatformSurfaceCapture::Error error,
    const QString *errorString) {
  self->updateError(error, *errorString);
}

//  void QPlatformSurfaceCapture::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformSurfaceCapture9setActiveEb(
    QPlatformSurfaceCapture *self,
    bool active) {
  self->QPlatformSurfaceCapture::setActive(active);
}

//  bool QPlatformSurfaceCapture::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QPlatformSurfaceCapture8isActiveEv(
    const QPlatformSurfaceCapture *self) {
  return self->QPlatformSurfaceCapture::isActive();
}
