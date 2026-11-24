//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionprofile.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qopenglversionprofile.h>
#include <QtGui/qsurfaceformat.h>

//  QOpenGLVersionProfile::QOpenGLVersionProfile()
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN21QOpenGLVersionProfileC1Ev() {
  return new QOpenGLVersionProfile();
}

//  QOpenGLVersionProfile::QOpenGLVersionProfile(const QSurfaceFormat
//      &format)
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN21QOpenGLVersionProfileC1ERK14QSurfaceFormat(
    const QSurfaceFormat *format) {
  return new QOpenGLVersionProfile(*format);
}

//  QOpenGLVersionProfile::QOpenGLVersionProfile(const QOpenGLVersionProfile
//      &other)
extern "C" Q_DECL_EXPORT
QOpenGLVersionProfile *ritual_ZN21QOpenGLVersionProfileC1ERKS_(
    const QOpenGLVersionProfile *other) {
  return new QOpenGLVersionProfile(*other);
}

//  QOpenGLVersionProfile::~QOpenGLVersionProfile()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLVersionProfileD1Ev(QOpenGLVersionProfile *self) {
  delete self;
}

//  void QOpenGLVersionProfile::setVersion(int majorVersion, int
//      minorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLVersionProfile10setVersionEii(
    QOpenGLVersionProfile *self,
    int majorVersion,
    int minorVersion) {
  self->setVersion(majorVersion, minorVersion);
}

//  QSurfaceFormat::OpenGLContextProfile QOpenGLVersionProfile::profile()
//      const
extern "C" Q_DECL_EXPORT
QSurfaceFormat::OpenGLContextProfile ritual_ZNK21QOpenGLVersionProfile7profileEv(
    const QOpenGLVersionProfile *self) {
  return self->profile();
}

//  void
//      QOpenGLVersionProfile::setProfile(QSurfaceFormat::OpenGLContextProfil
//      e profile)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLVersionProfile10setProfileEN14QSurfaceFormat20OpenGLContextProfileE(
    QOpenGLVersionProfile *self,
    QSurfaceFormat::OpenGLContextProfile profile) {
  self->setProfile(profile);
}

//  bool QOpenGLVersionProfile::hasProfiles() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLVersionProfile11hasProfilesEv(
    const QOpenGLVersionProfile *self) {
  return self->hasProfiles();
}

//  bool QOpenGLVersionProfile::isLegacyVersion() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLVersionProfile15isLegacyVersionEv(
    const QOpenGLVersionProfile *self) {
  return self->isLegacyVersion();
}

//  bool QOpenGLVersionProfile::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLVersionProfile7isValidEv(
    const QOpenGLVersionProfile *self) {
  return self->isValid();
}

//  bool operator==(const QOpenGLVersionProfile &lhs, const
//      QOpenGLVersionProfile &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK21QOpenGLVersionProfileS1_(
    const QOpenGLVersionProfile *lhs,
    const QOpenGLVersionProfile *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpenGLVersionProfile &lhs, const
//      QOpenGLVersionProfile &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK21QOpenGLVersionProfileS1_(
    const QOpenGLVersionProfile *lhs,
    const QOpenGLVersionProfile *rhs) {
  return operator!=(*lhs, *rhs);
}
