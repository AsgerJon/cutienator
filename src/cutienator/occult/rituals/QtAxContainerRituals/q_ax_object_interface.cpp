//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxobjectinterface.h, Qt 6.12.0, from Qt's source. Kept as
//  it is when the generator runs again. ActiveQt is built for Windows alone,
//  as a static library, so every function of it is compiled into ours. A
//  'ulong' is passed as the number Windows has. All its functions are left
//  for a class built on it to write, so no object of it is made here and it
//  has no Cute class: they are called through objects Qt made.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxobjectinterface.h>
#include <QtCore/qstring.h>

//  QAxObjectInterface::~QAxObjectInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAxObjectInterfaceD1Ev(QAxObjectInterface *self) {
  delete self;
}

//  ulong QAxObjectInterface::classContext() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK18QAxObjectInterface12classContextEv(
    const QAxObjectInterface *self) {
  return self->classContext();
}

//  void QAxObjectInterface::setClassContext(ulong classContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAxObjectInterface15setClassContextEm(
    QAxObjectInterface *self,
    ulong classContext) {
  self->setClassContext(classContext);
}

//  QString QAxObjectInterface::control() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QAxObjectInterface7controlEv(
    const QAxObjectInterface *self) {
  return new QString(self->control());
}

//  void QAxObjectInterface::resetControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAxObjectInterface12resetControlEv(
    QAxObjectInterface *self) {
  self->resetControl();
}

//  bool QAxObjectInterface::setControl(const QString &c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAxObjectInterface10setControlERK7QString(
    QAxObjectInterface *self,
    const QString *c) {
  return self->setControl(*c);
}

#endif  // defined(Q_OS_WIN)
