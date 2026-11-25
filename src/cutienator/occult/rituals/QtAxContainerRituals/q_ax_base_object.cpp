//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxobject.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours. It is
//  abstract, so no object of it is made here and it has no Cute class: its
//  functions are called through objects Qt made. Not written: the signals
//  'exception', 'propertyChanged' and 'signal'; and the constructor taking a
//  'QObjectPrivate &', since it is abstract.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxobject.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAxBaseObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QAxBaseObject10metaObjectEv(
    const QAxBaseObject *self) {
  return self->metaObject();
}

//  QString QAxBaseObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QAxBaseObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAxBaseObject::tr(s, c, n));
}

//  QAxBaseObject as the QAxObjectInterface it is built on
extern "C" Q_DECL_EXPORT
QAxObjectInterface *ritual_cast_QAxBaseObject_QAxObjectInterface(
    QAxBaseObject *self) {
  return static_cast<QAxObjectInterface *>(self);
}

#endif  // defined(Q_OS_WIN)
