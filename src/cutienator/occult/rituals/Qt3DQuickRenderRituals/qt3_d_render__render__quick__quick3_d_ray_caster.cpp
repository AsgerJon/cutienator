//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3draycaster_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3draycaster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <Qt3DRender/Qt3DRender>

//  const QMetaObject
//      *Qt3DRender::Render::Quick::Quick3DRayCaster::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick16Quick3DRayCaster10metaObjectEv(
    const Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Render::Quick::Quick3DRayCaster::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster11qt_metacastEPKc(
    Qt3DRender::Render::Quick::Quick3DRayCaster *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Render::Quick::Quick3DRayCaster::qt_metacall(QMetaObject:
//      :Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::Quick::Quick3DRayCaster *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Render::Quick::Quick3DRayCaster::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::Quick3DRayCaster::tr(
          s,
          c,
          n));
}

//  Qt3DRender::Render::Quick::Quick3DRayCaster::Quick3DRayCaster(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DRayCaster *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCasterC1EP7QObject(
    QObject *parent) {
  return new Qt3DRender::Render::Quick::Quick3DRayCaster(parent);
}

//  QQmlListProperty<QLayer>
//      Qt3DRender::Render::Quick::Quick3DRayCaster::qmlLayers()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DRender::QLayer> *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster9qmlLayersEv(
    Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return new QQmlListProperty<Qt3DRender::QLayer>(self->qmlLayers());
}

//  Quick3DRayCasterPrivate
//      *Qt3DRender::Render::Quick::Quick3DRayCaster::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster6d_funcEv(
    Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return self->d_func();
}

//  const Quick3DRayCasterPrivate
//      *Qt3DRender::Render::Quick::Quick3DRayCaster::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *ritual_ZNK10Qt3DRender6Render5Quick16Quick3DRayCaster6d_funcEv(
    const Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return self->d_func();
}

//  a QQmlListProperty<Qt3DRender::QLayer> a ritual of
//      Qt3DRender::Render::Quick::Quick3DRayCaster gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Quick_Quick3DRayCaster__QQmlListProperty_Qt3DRender_QLayer(
    QQmlListProperty<Qt3DRender::QLayer> *self) {
  delete self;
}
