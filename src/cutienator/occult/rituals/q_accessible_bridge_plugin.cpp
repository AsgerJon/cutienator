//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessiblebridge.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessiblebridge.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAccessibleBridgePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QAccessibleBridgePlugin10metaObjectEv(
    const QAccessibleBridgePlugin *self) {
  return self->metaObject();
}

//  QString QAccessibleBridgePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QAccessibleBridgePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessibleBridgePlugin::tr(s, c, n));
}

//  QAccessibleBridgePlugin::~QAccessibleBridgePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAccessibleBridgePluginD1Ev(QAccessibleBridgePlugin *self) {
  delete self;
}

//  QAccessibleBridge *QAccessibleBridgePlugin::create(const QString &key)
extern "C" Q_DECL_EXPORT
QAccessibleBridge *ritual_ZN23QAccessibleBridgePlugin6createERK7QString(
    QAccessibleBridgePlugin *self,
    const QString *key) {
  return self->create(*key);
}
