//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *qdesigner_internal::DesignerIconCache::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17DesignerIconCache10metaObjectEv(
    const qdesigner_internal::DesignerIconCache *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::DesignerIconCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal17DesignerIconCache11qt_metacastEPKc(
    qdesigner_internal::DesignerIconCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::DesignerIconCache::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal17DesignerIconCache11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::DesignerIconCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::DesignerIconCache::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17DesignerIconCache2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::DesignerIconCache::tr(s, c, n));
}

//  qdesigner_internal::DesignerIconCache::DesignerIconCache(DesignerPixmapCa
//      che *pixmapCache, QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerIconCache *ritual_ZN18qdesigner_internal17DesignerIconCacheC1EPNS_19DesignerPixmapCacheEP7QObject(
    qdesigner_internal::DesignerPixmapCache *pixmapCache,
    QObject *parent) {
  return new qdesigner_internal::DesignerIconCache(pixmapCache, parent);
}

//  QIcon qdesigner_internal::DesignerIconCache::icon(const
//      PropertySheetIconValue &value) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK18qdesigner_internal17DesignerIconCache4iconERKNS_22PropertySheetIconValueE(
    const qdesigner_internal::DesignerIconCache *self,
    const qdesigner_internal::PropertySheetIconValue *value) {
  return new QIcon(self->icon(*value));
}

//  void qdesigner_internal::DesignerIconCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17DesignerIconCache5clearEv(
    qdesigner_internal::DesignerIconCache *self) {
  self->clear();
}

//  void qdesigner_internal::DesignerIconCache::reloaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17DesignerIconCache8reloadedEv(
    qdesigner_internal::DesignerIconCache *self) {
  self->reloaded();
}
