//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qspritesheetitem.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qspritesheetitem.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DExtras::QSpriteSheetItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras16QSpriteSheetItem10metaObjectEv(
    const Qt3DExtras::QSpriteSheetItem *self) {
  return self->metaObject();
}

//  QString Qt3DExtras::QSpriteSheetItem::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras16QSpriteSheetItem2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QSpriteSheetItem::tr(s, c, n));
}

//  QSpriteSheetItemPrivate *Qt3DExtras::QSpriteSheetItem::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheetItemPrivate *ritual_ZN10Qt3DExtras16QSpriteSheetItem6d_funcEv(
    Qt3DExtras::QSpriteSheetItem *self) {
  return self->d_func();
}

//  const QSpriteSheetItemPrivate *Qt3DExtras::QSpriteSheetItem::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSpriteSheetItemPrivate *ritual_ZNK10Qt3DExtras16QSpriteSheetItem6d_funcEv(
    const Qt3DExtras::QSpriteSheetItem *self) {
  return self->d_func();
}
