//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/instancerepeater_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/instancerepeater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on InstanceRepeater may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnInstanceRepeater : InstanceRepeater {
  using InstanceRepeater::initDelegate;
};

//  const QMetaObject *InstanceRepeater::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16InstanceRepeater10metaObjectEv(
    const InstanceRepeater *self) {
  return self->metaObject();
}

//  void *InstanceRepeater::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16InstanceRepeater11qt_metacastEPKc(
    InstanceRepeater *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int InstanceRepeater::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16InstanceRepeater11qt_metacallEN11QMetaObject4CallEiPPv(
    InstanceRepeater *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString InstanceRepeater::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16InstanceRepeater2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(InstanceRepeater::tr(s, c, n));
}

//  InstanceRepeater::InstanceRepeater(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
InstanceRepeater *ritual_ZN16InstanceRepeaterC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new InstanceRepeater(parent);
}

//  QQuick3DInstancing *InstanceRepeater::instancing() const
extern "C" Q_DECL_EXPORT
QQuick3DInstancing *ritual_ZNK16InstanceRepeater10instancingEv(
    const InstanceRepeater *self) {
  return self->instancing();
}

//  void InstanceRepeater::setInstancing(QQuick3DInstancing *instancing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16InstanceRepeater13setInstancingEP18QQuick3DInstancing(
    InstanceRepeater *self,
    QQuick3DInstancing *instancing) {
  self->setInstancing(instancing);
}

//  void InstanceRepeater::instancingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16InstanceRepeater17instancingChangedEv(
    InstanceRepeater *self) {
  self->instancingChanged();
}

//  void InstanceRepeater::initDelegate(int index, QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16InstanceRepeater12initDelegateEiP12QQuick3DNode(
    InstanceRepeater *self,
    int index,
    QQuick3DNode *node) {
  self->initDelegate(index, node);
}

//  void InstanceRepeater::initDelegate(int index, QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16InstanceRepeater12initDelegateEiP12QQuick3DNode(
    InstanceRepeater *self,
    int index,
    QQuick3DNode *node) {
  static_cast<OwnInstanceRepeater *>(self)->OwnInstanceRepeater::initDelegate(
      index,
      node);
}
