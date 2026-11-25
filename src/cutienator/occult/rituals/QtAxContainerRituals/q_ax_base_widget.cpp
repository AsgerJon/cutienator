//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxwidget.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours. It is
//  abstract, so no object of it is made here and it has no Cute class: its
//  functions are called through objects Qt made. Not written: the signals
//  'exception', 'propertyChanged' and 'signal'; and the constructor taking a
//  'QWidgetPrivate &', since it is abstract.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxwidget.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAxBaseWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QAxBaseWidget10metaObjectEv(
    const QAxBaseWidget *self) {
  return self->metaObject();
}

//  QString QAxBaseWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QAxBaseWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAxBaseWidget::tr(s, c, n));
}

//  QAxBaseWidget as the QAxObjectInterface it is built on
extern "C" Q_DECL_EXPORT
QAxObjectInterface *ritual_cast_QAxBaseWidget_QAxObjectInterface(
    QAxBaseWidget *self) {
  return static_cast<QAxObjectInterface *>(self);
}

#endif  // defined(Q_OS_WIN)
