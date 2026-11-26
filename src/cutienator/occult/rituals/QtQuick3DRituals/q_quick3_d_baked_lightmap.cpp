//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dbakedlightmap_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dbakedlightmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuick3DBakedLightmap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DBakedLightmap10metaObjectEv(
    const QQuick3DBakedLightmap *self) {
  return self->metaObject();
}

//  void *QQuick3DBakedLightmap::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuick3DBakedLightmap11qt_metacastEPKc(
    QQuick3DBakedLightmap *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DBakedLightmap::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuick3DBakedLightmap11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DBakedLightmap *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DBakedLightmap::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DBakedLightmap2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DBakedLightmap::tr(s, c, n));
}

//  bool QQuick3DBakedLightmap::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DBakedLightmap9isEnabledEv(
    const QQuick3DBakedLightmap *self) {
  return self->isEnabled();
}

//  QString QQuick3DBakedLightmap::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DBakedLightmap3keyEv(
    const QQuick3DBakedLightmap *self) {
  return new QString(self->key());
}

//  QString QQuick3DBakedLightmap::loadPrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DBakedLightmap10loadPrefixEv(
    const QQuick3DBakedLightmap *self) {
  return new QString(self->loadPrefix());
}

//  void QQuick3DBakedLightmap::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap10setEnabledEb(
    QQuick3DBakedLightmap *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQuick3DBakedLightmap::setKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap6setKeyERK7QString(
    QQuick3DBakedLightmap *self,
    const QString *key) {
  self->setKey(*key);
}

//  void QQuick3DBakedLightmap::setLoadPrefix(const QString &loadPrefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap13setLoadPrefixERK7QString(
    QQuick3DBakedLightmap *self,
    const QString *loadPrefix) {
  self->setLoadPrefix(*loadPrefix);
}

//  void QQuick3DBakedLightmap::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap7changedEv(
    QQuick3DBakedLightmap *self) {
  self->changed();
}

//  void QQuick3DBakedLightmap::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap14enabledChangedEv(
    QQuick3DBakedLightmap *self) {
  self->enabledChanged();
}

//  void QQuick3DBakedLightmap::keyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap10keyChangedEv(
    QQuick3DBakedLightmap *self) {
  self->keyChanged();
}

//  void QQuick3DBakedLightmap::loadPrefixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DBakedLightmap17loadPrefixChangedEv(
    QQuick3DBakedLightmap *self) {
  self->loadPrefixChanged();
}
