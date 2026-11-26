//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformsurfacecapture_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 2. Kept as it is when the generator runs again.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformsurfacecapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qcapturablewindow.h>
#include <optional>
#include <QtCore/qpointer.h>
#include <QtGui/qscreen.h>

//  const QMetaObject *QPlatformSurfaceCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPlatformSurfaceCapture10metaObjectEv(
    const QPlatformSurfaceCapture *self) {
  return self->metaObject();
}

//  void *QPlatformSurfaceCapture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QPlatformSurfaceCapture11qt_metacastEPKc(
    QPlatformSurfaceCapture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformSurfaceCapture::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QPlatformSurfaceCapture11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformSurfaceCapture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QPlatformSurfaceCapture::setSource(Source source)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture9setSourceESt7variantIJ8QPointerI7QScreenE17QCapturableWindowEE(
    QPlatformSurfaceCapture *self,
    const QPlatformSurfaceCapture::Source *source) {
  self->setSource(*source);
}

//  Source QPlatformSurfaceCapture::source() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture::Source *ritual_ZNK23QPlatformSurfaceCapture6sourceEv(
    const QPlatformSurfaceCapture *self) {
  return new QPlatformSurfaceCapture::Source(self->source());
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

//  void QPlatformSurfaceCapture::setFrameRate(std::optional<qreal> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture12setFrameRateESt8optionalIdE(
    QPlatformSurfaceCapture *self,
    const std::optional<qreal> *a0) {
  self->setFrameRate(*a0);
}

//  std::optional<qreal> QPlatformSurfaceCapture::frameRate() const
extern "C" Q_DECL_EXPORT
std::optional<qreal> *ritual_ZNK23QPlatformSurfaceCapture9frameRateEv(
    const QPlatformSurfaceCapture *self) {
  return new std::optional<qreal>(self->frameRate());
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

//  bool QPlatformSurfaceCapture::checkScreenWithError(ScreenSource &screen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPlatformSurfaceCapture20checkScreenWithErrorER8QPointerI7QScreenE(
    QPlatformSurfaceCapture *self,
    QPlatformSurfaceCapture::ScreenSource *screen) {
  return self->checkScreenWithError(*screen);
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

//  void QPlatformSurfaceCapture::sourceChanged(WindowSource a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture13sourceChangedE17QCapturableWindow(
    QPlatformSurfaceCapture *self,
    const QCapturableWindow *a0) {
  self->sourceChanged(*a0);
}

//  void QPlatformSurfaceCapture::sourceChanged(ScreenSource a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture13sourceChangedE8QPointerI7QScreenE(
    QPlatformSurfaceCapture *self,
    const QPlatformSurfaceCapture::ScreenSource *a0) {
  self->sourceChanged(*a0);
}

//  void QPlatformSurfaceCapture::errorOccurred(Error error, QString
//      errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture13errorOccurredENS_5ErrorE7QString(
    QPlatformSurfaceCapture *self,
    QPlatformSurfaceCapture::Error error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QPlatformSurfaceCapture::frameRateChanged(std::optional<qreal> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSurfaceCapture16frameRateChangedESt8optionalIdE(
    QPlatformSurfaceCapture *self,
    const std::optional<qreal> *a0) {
  self->frameRateChanged(*a0);
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

//  a QPlatformSurfaceCapture::Source a ritual of QPlatformSurfaceCapture
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformSurfaceCapture__QPlatformSurfaceCapture_Source(
    QPlatformSurfaceCapture::Source *self) {
  delete self;
}

//  a std::optional<qreal> a ritual of QPlatformSurfaceCapture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformSurfaceCapture__std_optional_qreal(
    std::optional<qreal> *self) {
  delete self;
}

//  Type QPlatformSurfaceCapture::source<QPointer<QScreen>>() const
extern "C" Q_DECL_EXPORT
QPointer<QScreen> * ritual_ZNK23QPlatformSurfaceCapture6sourceI8QPointerI7QScreenEEET_v(const QPlatformSurfaceCapture *self) {
  return new QPointer<QScreen>(
      self->source<QPointer<QScreen>>());
}

//  Type QPlatformSurfaceCapture::source<QCapturableWindow>() const
extern "C" Q_DECL_EXPORT
QCapturableWindow * ritual_ZNK23QPlatformSurfaceCapture6sourceI17QCapturableWindowEET_v(const QPlatformSurfaceCapture *self) {
  return new QCapturableWindow(
      self->source<QCapturableWindow>());
}
