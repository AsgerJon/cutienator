//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3dobject.h>

//  QQuick3DObject::ItemChangeData::ItemChangeData(QQuick3DObject *v)
extern "C" Q_DECL_EXPORT
QQuick3DObject::ItemChangeData *ritual_ZN14QQuick3DObject14ItemChangeDataC1EPS_(
    QQuick3DObject *v) {
  return new QQuick3DObject::ItemChangeData(v);
}

//  QQuick3DObject::ItemChangeData::ItemChangeData(QQuick3DSceneManager *v)
extern "C" Q_DECL_EXPORT
QQuick3DObject::ItemChangeData *ritual_ZN14QQuick3DObject14ItemChangeDataC1EP20QQuick3DSceneManager(
    QQuick3DSceneManager *v) {
  return new QQuick3DObject::ItemChangeData(v);
}

//  QQuick3DObject::ItemChangeData::ItemChangeData(qreal v)
extern "C" Q_DECL_EXPORT
QQuick3DObject::ItemChangeData *ritual_ZN14QQuick3DObject14ItemChangeDataC1Ed(
    qreal v) {
  return new QQuick3DObject::ItemChangeData(v);
}

//  QQuick3DObject::ItemChangeData::ItemChangeData(bool v)
extern "C" Q_DECL_EXPORT
QQuick3DObject::ItemChangeData *ritual_ZN14QQuick3DObject14ItemChangeDataC1Eb(
    bool v) {
  return new QQuick3DObject::ItemChangeData(v);
}

//  QQuick3DObject::ItemChangeData::~ItemChangeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DObject14ItemChangeDataD1Ev(
    QQuick3DObject::ItemChangeData *self) {
  delete self;
}
