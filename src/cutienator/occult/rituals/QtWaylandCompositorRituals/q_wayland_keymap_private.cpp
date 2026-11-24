//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandkeymap_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandkeymap.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandkeymap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QWaylandKeymap *QWaylandKeymapPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandKeymap *ritual_ZN21QWaylandKeymapPrivate6q_funcEv(
    QWaylandKeymapPrivate *self) {
  return self->q_func();
}

//  const QWaylandKeymap *QWaylandKeymapPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWaylandKeymap *ritual_ZNK21QWaylandKeymapPrivate6q_funcEv(
    const QWaylandKeymapPrivate *self) {
  return self->q_func();
}

//  QWaylandKeymapPrivate::QWaylandKeymapPrivate(const QString &layout, const
//      QString &variant, const QString &options, const QString &model, const
//      QString &rules)
extern "C" Q_DECL_EXPORT
QWaylandKeymapPrivate *ritual_ZN21QWaylandKeymapPrivateC1ERK7QStringS2_S2_S2_S2_(
    const QString *layout,
    const QString *variant,
    const QString *options,
    const QString *model,
    const QString *rules) {
  return new QWaylandKeymapPrivate(
      *layout,
      *variant,
      *options,
      *model,
      *rules);
}
