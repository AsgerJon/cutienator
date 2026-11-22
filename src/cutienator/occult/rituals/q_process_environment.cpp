//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qprocess.h>
#include <QtCore/qstring.h>

//  QProcessEnvironment::QProcessEnvironment()
extern "C" Q_DECL_EXPORT
QProcessEnvironment *ritual_ZN19QProcessEnvironmentC1Ev() {
  return new QProcessEnvironment();
}

//  QProcessEnvironment::QProcessEnvironment(Initialization a0)
extern "C" Q_DECL_EXPORT
QProcessEnvironment *ritual_ZN19QProcessEnvironmentC1ENS_14InitializationE(
    QProcessEnvironment::Initialization a0) {
  return new QProcessEnvironment(a0);
}

//  QProcessEnvironment::QProcessEnvironment(const QProcessEnvironment
//      &other)
extern "C" Q_DECL_EXPORT
QProcessEnvironment *ritual_ZN19QProcessEnvironmentC1ERKS_(
    const QProcessEnvironment *other) {
  return new QProcessEnvironment(*other);
}

//  QProcessEnvironment::~QProcessEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProcessEnvironmentD1Ev(QProcessEnvironment *self) {
  delete self;
}

//  bool QProcessEnvironment::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QProcessEnvironment7isEmptyEv(
    const QProcessEnvironment *self) {
  return self->isEmpty();
}

//  bool QProcessEnvironment::inheritsFromParent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QProcessEnvironment18inheritsFromParentEv(
    const QProcessEnvironment *self) {
  return self->inheritsFromParent();
}

//  void QProcessEnvironment::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProcessEnvironment5clearEv(QProcessEnvironment *self) {
  self->clear();
}

//  bool QProcessEnvironment::contains(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QProcessEnvironment8containsERK7QString(
    const QProcessEnvironment *self,
    const QString *name) {
  return self->contains(*name);
}

//  void QProcessEnvironment::insert(const QString &name, const QString
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProcessEnvironment6insertERK7QStringS2_(
    QProcessEnvironment *self,
    const QString *name,
    const QString *value) {
  self->insert(*name, *value);
}

//  void QProcessEnvironment::remove(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProcessEnvironment6removeERK7QString(
    QProcessEnvironment *self,
    const QString *name) {
  self->remove(*name);
}

//  QString QProcessEnvironment::value(const QString &name, const QString
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QProcessEnvironment5valueERK7QStringS2_(
    const QProcessEnvironment *self,
    const QString *name,
    const QString *defaultValue) {
  return new QString(self->value(*name, *defaultValue));
}

//  void QProcessEnvironment::insert(const QProcessEnvironment &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProcessEnvironment6insertERKS_(
    QProcessEnvironment *self,
    const QProcessEnvironment *e) {
  self->insert(*e);
}

//  QProcessEnvironment QProcessEnvironment::systemEnvironment()
extern "C" Q_DECL_EXPORT
QProcessEnvironment *ritual_ZN19QProcessEnvironment17systemEnvironmentEv() {
  return new QProcessEnvironment(QProcessEnvironment::systemEnvironment());
}

//  bool operator==(const QProcessEnvironment &lhs, const QProcessEnvironment
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QProcessEnvironmentS1_(
    const QProcessEnvironment *lhs,
    const QProcessEnvironment *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QProcessEnvironment &lhs, const QProcessEnvironment
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QProcessEnvironmentS1_(
    const QProcessEnvironment *lhs,
    const QProcessEnvironment *rhs) {
  return operator!=(*lhs, *rhs);
}
