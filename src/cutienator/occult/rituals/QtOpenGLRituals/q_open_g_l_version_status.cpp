//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglversionfunctions.h>

//  QOpenGLVersionStatus::QOpenGLVersionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionStatus *ritual_ZN20QOpenGLVersionStatusC1Ev() {
  return new QOpenGLVersionStatus();
}

//  QOpenGLVersionStatus::QOpenGLVersionStatus(int majorVersion, int
//      minorVersion, QOpenGLVersionStatus::OpenGLStatus functionStatus)
extern "C" Q_DECL_EXPORT
QOpenGLVersionStatus *ritual_ZN20QOpenGLVersionStatusC1EiiNS_12OpenGLStatusE(
    int majorVersion,
    int minorVersion,
    QOpenGLVersionStatus::OpenGLStatus functionStatus) {
  return new QOpenGLVersionStatus(
      majorVersion,
      minorVersion,
      functionStatus);
}

//  bool operator==(const QOpenGLVersionStatus &lhs, const
//      QOpenGLVersionStatus &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QOpenGLVersionStatusS1_(
    const QOpenGLVersionStatus *lhs,
    const QOpenGLVersionStatus *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpenGLVersionStatus &lhs, const
//      QOpenGLVersionStatus &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QOpenGLVersionStatusS1_(
    const QOpenGLVersionStatus *lhs,
    const QOpenGLVersionStatus *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QOpenGLVersionStatus::~QOpenGLVersionStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLVersionStatusD1Ev(QOpenGLVersionStatus *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
