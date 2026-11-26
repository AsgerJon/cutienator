//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>

//  const QMetaObject *qdesigner_internal::DesignerPixmapCache::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal19DesignerPixmapCache10metaObjectEv(
    const qdesigner_internal::DesignerPixmapCache *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::DesignerPixmapCache::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal19DesignerPixmapCache11qt_metacastEPKc(
    qdesigner_internal::DesignerPixmapCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      qdesigner_internal::DesignerPixmapCache::qt_metacall(QMetaObject::Cal
//      l a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal19DesignerPixmapCache11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::DesignerPixmapCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::DesignerPixmapCache::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal19DesignerPixmapCache2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::DesignerPixmapCache::tr(s, c, n));
}

//  qdesigner_internal::DesignerPixmapCache::DesignerPixmapCache(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerPixmapCache *ritual_ZN18qdesigner_internal19DesignerPixmapCacheC1EP7QObject(
    QObject *parent) {
  return new qdesigner_internal::DesignerPixmapCache(parent);
}

//  QPixmap qdesigner_internal::DesignerPixmapCache::pixmap(const
//      PropertySheetPixmapValue &value) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK18qdesigner_internal19DesignerPixmapCache6pixmapERKNS_24PropertySheetPixmapValueE(
    const qdesigner_internal::DesignerPixmapCache *self,
    const qdesigner_internal::PropertySheetPixmapValue *value) {
  return new QPixmap(self->pixmap(*value));
}

//  void qdesigner_internal::DesignerPixmapCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19DesignerPixmapCache5clearEv(
    qdesigner_internal::DesignerPixmapCache *self) {
  self->clear();
}

//  void qdesigner_internal::DesignerPixmapCache::reloaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19DesignerPixmapCache8reloadedEv(
    qdesigner_internal::DesignerPixmapCache *self) {
  self->reloaded();
}
