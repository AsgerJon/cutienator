//  Written by hand on 2026-11-25 from
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  inline functions are called.
//  Not written: the constructor taking the listener alone, for the
//  compiler finds it ambiguous with the one that also takes the
//  types; that one is written, with both arguments.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuick3DObjectPrivate::ChangeListener::ChangeListener(
//      QQuick3DObjectChangeListener *l, ChangeTypes t = {})
extern "C" Q_DECL_EXPORT
QQuick3DObjectPrivate::ChangeListener *ritual_ZN21QQuick3DObjectPrivate14ChangeListenerC1EP28QQuick3DObjectChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuick3DObjectChangeListener *l,
    int t) {
  return new QQuick3DObjectPrivate::ChangeListener(
      l, QQuick3DObjectPrivate::ChangeTypes::fromInt(t));
}

//  bool QQuick3DObjectPrivate::ChangeListener::operator==(
//      const ChangeListener &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DObjectPrivate14ChangeListenereqERKS0_(
    const QQuick3DObjectPrivate::ChangeListener *self,
    const QQuick3DObjectPrivate::ChangeListener *other) {
  return self->operator==(*other);
}

//  QQuick3DObjectPrivate::ChangeListener::~ChangeListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate14ChangeListenerD1Ev(
    QQuick3DObjectPrivate::ChangeListener *self) {
  delete self;
}
