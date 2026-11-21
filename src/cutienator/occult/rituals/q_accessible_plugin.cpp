//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibleplugin.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAccessiblePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAccessiblePlugin10metaObjectEv(
    const QAccessiblePlugin *self) {
  return self->metaObject();
}

//  QString QAccessiblePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAccessiblePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessiblePlugin::tr(s, c, n));
}

//  QAccessiblePlugin::~QAccessiblePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessiblePluginD1Ev(QAccessiblePlugin *self) {
  delete self;
}

//  QAccessibleInterface *QAccessiblePlugin::create(const QString &key,
//      QObject *object)
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZN17QAccessiblePlugin6createERK7QStringP7QObject(
    QAccessiblePlugin *self,
    const QString *key,
    QObject *object) {
  return self->create(*key, object);
}
