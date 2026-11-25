//  Written by hand on 2026-11-25 from
//  QtAxContainer/6.12.0/QtAxContainer/private/qaxwidget_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again. ActiveQt is
//  built for Windows alone, as a static library, so every function of it is
//  compiled into ours. A 'void *' is passed as an address. Qt declares no
//  constructor for it, so no object of it is made here and it has no Cute
//  class: its functions are called through objects Qt made. Its member
//  'container' holds a 'QAxClientSite', a class its header only names.
//  Nothing it declares is left out.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/6.12.0/QtAxContainer/private/qaxwidget_p.h>
#include <QtCore/qstring.h>

//  QAxWidget *QAxWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAxWidget *ritual_ZN16QAxWidgetPrivate6q_funcEv(QAxWidgetPrivate *self) {
  return self->q_func();
}

//  const QAxWidget *QAxWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAxWidget *ritual_ZNK16QAxWidgetPrivate6q_funcEv(
    const QAxWidgetPrivate *self) {
  return self->q_func();
}

//  void QAxWidgetPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxWidgetPrivate5clearEv(QAxWidgetPrivate *self) {
  self->clear();
}

//  QObject *QAxWidgetPrivate::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QAxWidgetPrivate7qObjectEv(
    const QAxWidgetPrivate *self) {
  return self->qObject();
}

//  const char *QAxWidgetPrivate::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QAxWidgetPrivate9classNameEv(
    const QAxWidgetPrivate *self) {
  return self->className();
}

//  const QMetaObject *QAxWidgetPrivate::fallbackMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAxWidgetPrivate18fallbackMetaObjectEv(
    const QAxWidgetPrivate *self) {
  return self->fallbackMetaObject();
}

//  const QMetaObject *QAxWidgetPrivate::parentMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAxWidgetPrivate16parentMetaObjectEv(
    const QAxWidgetPrivate *self) {
  return self->parentMetaObject();
}

//  void QAxWidgetPrivate::emitException(int code, const QString &source,
//      const QString &desc, const QString &help)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxWidgetPrivate13emitExceptionEiRK7QStringS2_S2_(
    QAxWidgetPrivate *self,
    int code,
    const QString *source,
    const QString *desc,
    const QString *help) {
  self->emitException(code, *source, *desc, *help);
}

//  void QAxWidgetPrivate::emitPropertyChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxWidgetPrivate19emitPropertyChangedERK7QString(
    QAxWidgetPrivate *self,
    const QString *name) {
  self->emitPropertyChanged(*name);
}

//  void QAxWidgetPrivate::emitSignal(const QString &name, int argc, void
//      *argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAxWidgetPrivate10emitSignalERK7QStringiPv(
    QAxWidgetPrivate *self,
    const QString *name,
    int argc,
    void *argv) {
  self->emitSignal(*name, argc, argv);
}

//  QAxWidgetPrivate as the QAxBasePrivate it is built on
extern "C" Q_DECL_EXPORT
QAxBasePrivate *ritual_cast_QAxWidgetPrivate_QAxBasePrivate(
    QAxWidgetPrivate *self) {
  return static_cast<QAxBasePrivate *>(self);
}

//  QObject *QAxWidgetPrivate::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK16QAxWidgetPrivate7qObjectEv(
    const QAxWidgetPrivate *self) {
  return self->QAxWidgetPrivate::qObject();
}

//  const QMetaObject *QAxWidgetPrivate::fallbackMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_own_ZNK16QAxWidgetPrivate18fallbackMetaObjectEv(
    const QAxWidgetPrivate *self) {
  return self->QAxWidgetPrivate::fallbackMetaObject();
}

//  const QMetaObject *QAxWidgetPrivate::parentMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_own_ZNK16QAxWidgetPrivate16parentMetaObjectEv(
    const QAxWidgetPrivate *self) {
  return self->QAxWidgetPrivate::parentMetaObject();
}

//  void QAxWidgetPrivate::emitException(int code, const QString &source,
//      const QString &desc, const QString &help)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAxWidgetPrivate13emitExceptionEiRK7QStringS2_S2_(
    QAxWidgetPrivate *self,
    int code,
    const QString *source,
    const QString *desc,
    const QString *help) {
  self->QAxWidgetPrivate::emitException(code, *source, *desc, *help);
}

//  void QAxWidgetPrivate::emitPropertyChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAxWidgetPrivate19emitPropertyChangedERK7QString(
    QAxWidgetPrivate *self,
    const QString *name) {
  self->QAxWidgetPrivate::emitPropertyChanged(*name);
}

//  void QAxWidgetPrivate::emitSignal(const QString &name, int argc, void
//      *argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAxWidgetPrivate10emitSignalERK7QStringiPv(
    QAxWidgetPrivate *self,
    const QString *name,
    int argc,
    void *argv) {
  self->QAxWidgetPrivate::emitSignal(*name, argc, argv);
}

#endif  // defined(Q_OS_WIN)
