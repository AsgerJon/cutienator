//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleplugin.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QStylePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QStylePlugin10metaObjectEv(
    const QStylePlugin *self) {
  return self->metaObject();
}

//  QString QStylePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QStylePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStylePlugin::tr(s, c, n));
}

//  QStylePlugin::~QStylePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QStylePluginD1Ev(QStylePlugin *self) {
  delete self;
}

//  QStyle *QStylePlugin::create(const QString &key)
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN12QStylePlugin6createERK7QString(
    QStylePlugin *self,
    const QString *key) {
  return self->create(*key);
}
