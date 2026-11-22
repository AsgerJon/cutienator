//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qgenericplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qgenericplugin.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGenericPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGenericPlugin10metaObjectEv(
    const QGenericPlugin *self) {
  return self->metaObject();
}

//  QString QGenericPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGenericPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGenericPlugin::tr(s, c, n));
}

//  QGenericPlugin::~QGenericPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGenericPluginD1Ev(QGenericPlugin *self) {
  delete self;
}

//  QObject *QGenericPlugin::create(const QString &name, const QString &spec)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QGenericPlugin6createERK7QStringS2_(
    QGenericPlugin *self,
    const QString *name,
    const QString *spec) {
  return self->create(*name, *spec);
}
