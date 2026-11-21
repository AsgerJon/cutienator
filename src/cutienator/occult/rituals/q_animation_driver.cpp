//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractanimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAnimationDriver::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAnimationDriver10metaObjectEv(
    const QAnimationDriver *self) {
  return self->metaObject();
}

//  QString QAnimationDriver::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAnimationDriver2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAnimationDriver::tr(s, c, n));
}

//  QAnimationDriver::QAnimationDriver(QObject *parent)
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZN16QAnimationDriverC1EP7QObject(QObject *parent) {
  return new QAnimationDriver(parent);
}

//  QAnimationDriver::~QAnimationDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriverD1Ev(QAnimationDriver *self) {
  delete self;
}

//  void QAnimationDriver::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriver7advanceEv(QAnimationDriver *self) {
  self->advance();
}

//  void QAnimationDriver::install()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriver7installEv(QAnimationDriver *self) {
  self->install();
}

//  void QAnimationDriver::uninstall()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriver9uninstallEv(QAnimationDriver *self) {
  self->uninstall();
}

//  bool QAnimationDriver::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAnimationDriver9isRunningEv(const QAnimationDriver *self) {
  return self->isRunning();
}

//  qint64 QAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QAnimationDriver7elapsedEv(const QAnimationDriver *self) {
  return self->elapsed();
}
