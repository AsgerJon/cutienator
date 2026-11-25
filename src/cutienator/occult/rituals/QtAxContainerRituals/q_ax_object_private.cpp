//  Written by hand on 2026-11-25 from
//  QtAxContainer/6.12.0/QtAxContainer/private/qaxobject_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again. ActiveQt is
//  built for Windows alone, as a static library, so every function of it is
//  compiled into ours. A 'void *' is passed as an address. Qt declares no
//  constructor for it, so no object of it is made here and it has no Cute
//  class: its functions are called through objects Qt made. Nothing it
//  declares is left out.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/6.12.0/QtAxContainer/private/qaxobject_p.h>
#include <QtCore/qstring.h>

//  QAxObject *QAxObjectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAxObject *ritual_ZN16QAxObjectPrivate6q_funcEv(QAxObjectPrivate *self) {
  return self->q_func();
}

//  const QAxObject *QAxObjectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAxObject *ritual_ZNK16QAxObjectPrivate6q_funcEv(
    const QAxObjectPrivate *self) {
  return self->q_func();
}

//  void QAxObjectPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxObjectPrivate5clearEv(QAxObjectPrivate *self) {
  self->clear();
}

//  QObject *QAxObjectPrivate::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QAxObjectPrivate7qObjectEv(
    const QAxObjectPrivate *self) {
  return self->qObject();
}

//  const char *QAxObjectPrivate::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QAxObjectPrivate9classNameEv(
    const QAxObjectPrivate *self) {
  return self->className();
}

//  const QMetaObject *QAxObjectPrivate::fallbackMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAxObjectPrivate18fallbackMetaObjectEv(
    const QAxObjectPrivate *self) {
  return self->fallbackMetaObject();
}

//  const QMetaObject *QAxObjectPrivate::parentMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAxObjectPrivate16parentMetaObjectEv(
    const QAxObjectPrivate *self) {
  return self->parentMetaObject();
}

//  void QAxObjectPrivate::emitException(int code, const QString &source,
//      const QString &desc, const QString &help)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxObjectPrivate13emitExceptionEiRK7QStringS2_S2_(
    QAxObjectPrivate *self,
    int code,
    const QString *source,
    const QString *desc,
    const QString *help) {
  self->emitException(code, *source, *desc, *help);
}

//  void QAxObjectPrivate::emitPropertyChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxObjectPrivate19emitPropertyChangedERK7QString(
    QAxObjectPrivate *self,
    const QString *name) {
  self->emitPropertyChanged(*name);
}

//  void QAxObjectPrivate::emitSignal(const QString &name, int argc, void
//      *argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxObjectPrivate10emitSignalERK7QStringiPv(
    QAxObjectPrivate *self,
    const QString *name,
    int argc,
    void *argv) {
  self->emitSignal(*name, argc, argv);
}

//  QAxObjectPrivate as the QAxBasePrivate it is built on
extern "C" Q_DECL_EXPORT
QAxBasePrivate *ritual_cast_QAxObjectPrivate_QAxBasePrivate(
    QAxObjectPrivate *self) {
  return static_cast<QAxBasePrivate *>(self);
}

//  QObject *QAxObjectPrivate::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK16QAxObjectPrivate7qObjectEv(
    const QAxObjectPrivate *self) {
  return self->QAxObjectPrivate::qObject();
}

//  const QMetaObject *QAxObjectPrivate::fallbackMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_own_ZNK16QAxObjectPrivate18fallbackMetaObjectEv(
    const QAxObjectPrivate *self) {
  return self->QAxObjectPrivate::fallbackMetaObject();
}

//  const QMetaObject *QAxObjectPrivate::parentMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_own_ZNK16QAxObjectPrivate16parentMetaObjectEv(
    const QAxObjectPrivate *self) {
  return self->QAxObjectPrivate::parentMetaObject();
}

//  void QAxObjectPrivate::emitException(int code, const QString &source,
//      const QString &desc, const QString &help)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAxObjectPrivate13emitExceptionEiRK7QStringS2_S2_(
    QAxObjectPrivate *self,
    int code,
    const QString *source,
    const QString *desc,
    const QString *help) {
  self->QAxObjectPrivate::emitException(code, *source, *desc, *help);
}

//  void QAxObjectPrivate::emitPropertyChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAxObjectPrivate19emitPropertyChangedERK7QString(
    QAxObjectPrivate *self,
    const QString *name) {
  self->QAxObjectPrivate::emitPropertyChanged(*name);
}

//  void QAxObjectPrivate::emitSignal(const QString &name, int argc, void
//      *argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAxObjectPrivate10emitSignalERK7QStringiPv(
    QAxObjectPrivate *self,
    const QString *name,
    int argc,
    void *argv) {
  self->QAxObjectPrivate::emitSignal(*name, argc, argv);
}

#endif  // defined(Q_OS_WIN)
