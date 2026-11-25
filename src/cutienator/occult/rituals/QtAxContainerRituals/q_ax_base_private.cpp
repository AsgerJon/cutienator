//  Written by hand on 2026-11-25 from
//  QtAxContainer/6.12.0/QtAxContainer/private/qaxbase_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again. ActiveQt is
//  built for Windows alone, as a static library, so every function of it is
//  compiled into ours. What Windows has, as 'IDispatch', 'EXCEPINFO' and a
//  'VARIANT', is passed as an address; a 'long' as the number Windows has.
//  It is abstract, so no object of it is made here and it has no Cute class:
//  its functions are called through objects Qt made. Not written: the
//  constructor, since it is abstract.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/6.12.0/QtAxContainer/private/qaxbase_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>

//  QAxBasePrivate::~QAxBasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAxBasePrivateD1Ev(QAxBasePrivate *self) {
  delete self;
}

//  QObject *QAxBasePrivate::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK14QAxBasePrivate7qObjectEv(const QAxBasePrivate *self) {
  return self->qObject();
}

//  const char *QAxBasePrivate::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK14QAxBasePrivate9classNameEv(
    const QAxBasePrivate *self) {
  return self->className();
}

//  const QMetaObject *QAxBasePrivate::fallbackMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QAxBasePrivate18fallbackMetaObjectEv(
    const QAxBasePrivate *self) {
  return self->fallbackMetaObject();
}

//  const QMetaObject *QAxBasePrivate::parentMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QAxBasePrivate16parentMetaObjectEv(
    const QAxBasePrivate *self) {
  return self->parentMetaObject();
}

//  void QAxBasePrivate::emitException(int code, const QString &source, const
//      QString &desc, const QString &help)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAxBasePrivate13emitExceptionEiRK7QStringS2_S2_(
    QAxBasePrivate *self,
    int code,
    const QString *source,
    const QString *desc,
    const QString *help) {
  self->emitException(code, *source, *desc, *help);
}

//  void QAxBasePrivate::emitPropertyChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAxBasePrivate19emitPropertyChangedERK7QString(
    QAxBasePrivate *self,
    const QString *name) {
  self->emitPropertyChanged(*name);
}

//  void QAxBasePrivate::emitSignal(const QString &name, int argc, void
//      *argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAxBasePrivate10emitSignalERK7QStringiPv(
    QAxBasePrivate *self,
    const QString *name,
    int argc,
    void *argv) {
  self->emitSignal(*name, argc, argv);
}

//  int QAxBasePrivate::qtMetaCall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAxBasePrivate10qtMetaCallEN11QMetaObject4CallEiPPv(
    QAxBasePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qtMetaCall(a0, a1, a2);
}

//  int QAxBasePrivate::qtStaticMetaCall(QAxBase *a0, QMetaObject::Call a1,
//      int a2, void **a3)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAxBasePrivate16qtStaticMetaCallEP7QAxBaseN11QMetaObject4CallEiPPv(
    QAxBase *a0,
    QMetaObject::Call a1,
    int a2,
    void **a3) {
  return QAxBasePrivate::qtStaticMetaCall(a0, a1, a2, a3);
}

//  IDispatch *QAxBasePrivate::dispatch() const
extern "C" Q_DECL_EXPORT
IDispatch *ritual_ZNK14QAxBasePrivate8dispatchEv(
    const QAxBasePrivate *self) {
  return self->dispatch();
}

//  bool QAxBasePrivate::checkHRESULT(long hres, tagEXCEPINFO *exc, const
//      QString &name, uint argerr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QAxBasePrivate12checkHRESULTElP12tagEXCEPINFORK7QStringj(
    QAxBasePrivate *self,
    long hres,
    tagEXCEPINFO *exc,
    const QString *name,
    uint argerr) {
  return self->checkHRESULT(hres, exc, *name, argerr);
}

//  void QAxBasePrivate::handleException(tagEXCEPINFO *exc, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAxBasePrivate15handleExceptionEP12tagEXCEPINFORK7QString(
    QAxBasePrivate *self,
    tagEXCEPINFO *exc,
    const QString *name) {
  self->handleException(exc, *name);
}

//  QVariant QAxBasePrivate::VARIANTToQVariant(const VARIANT &arg, const
//      QByteArray &typeName, uint type)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QAxBasePrivate17VARIANTToQVariantERK10tagVARIANTRK10QByteArrayj(
    const VARIANT *arg,
    const QByteArray *typeName,
    uint type) {
  return new QVariant(
      QAxBasePrivate::VARIANTToQVariant(
          *arg,
          *typeName,
          type));
}

//  QMetaObject *QAxBasePrivate::metaObject()
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN14QAxBasePrivate10metaObjectEv(QAxBasePrivate *self) {
  return self->metaObject();
}

#endif  // defined(Q_OS_WIN)
