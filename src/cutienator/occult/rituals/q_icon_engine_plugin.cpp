//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qiconengineplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qiconengineplugin.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QIconEnginePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QIconEnginePlugin10metaObjectEv(
    const QIconEnginePlugin *self) {
  return self->metaObject();
}

//  QString QIconEnginePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QIconEnginePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIconEnginePlugin::tr(s, c, n));
}

//  QIconEnginePlugin::~QIconEnginePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconEnginePluginD1Ev(QIconEnginePlugin *self) {
  delete self;
}

//  QIconEngine *QIconEnginePlugin::create(const QString &filename)
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZN17QIconEnginePlugin6createERK7QString(
    QIconEnginePlugin *self,
    const QString *filename) {
  return self->create(*filename);
}
