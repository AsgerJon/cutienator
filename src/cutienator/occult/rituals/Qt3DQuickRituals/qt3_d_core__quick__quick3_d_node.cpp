//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <Qt3DCore/Qt3DCore>

//  const QMetaObject *Qt3DCore::Quick::Quick3DNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick11Quick3DNode10metaObjectEv(
    const Qt3DCore::Quick::Quick3DNode *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Quick::Quick3DNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Quick11Quick3DNode11qt_metacastEPKc(
    Qt3DCore::Quick::Quick3DNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Quick::Quick3DNode::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Quick11Quick3DNode11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Quick::Quick3DNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Quick::Quick3DNode::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick11Quick3DNode2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DNode::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DNode::Quick3DNode(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DNode *ritual_ZN8Qt3DCore5Quick11Quick3DNodeC1EP7QObject(
    QObject *parent) {
  return new Qt3DCore::Quick::Quick3DNode(parent);
}

//  QQmlListProperty<QObject> Qt3DCore::Quick::Quick3DNode::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN8Qt3DCore5Quick11Quick3DNode4dataEv(
    Qt3DCore::Quick::Quick3DNode *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  QQmlListProperty<Qt3DCore::QNode>
//      Qt3DCore::Quick::Quick3DNode::childNodes()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DCore::QNode> *ritual_ZN8Qt3DCore5Quick11Quick3DNode10childNodesEv(
    Qt3DCore::Quick::Quick3DNode *self) {
  return new QQmlListProperty<Qt3DCore::QNode>(self->childNodes());
}

//  QNode *Qt3DCore::Quick::Quick3DNode::parentNode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore5Quick11Quick3DNode10parentNodeEv(
    const Qt3DCore::Quick::Quick3DNode *self) {
  return self->parentNode();
}

//  void Qt3DCore::Quick::Quick3DNode::childAppended(int idx, QObject *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick11Quick3DNode13childAppendedEiP7QObject(
    Qt3DCore::Quick::Quick3DNode *self,
    int idx,
    QObject *child) {
  self->childAppended(idx, child);
}

//  void Qt3DCore::Quick::Quick3DNode::childRemoved(int idx, QObject *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick11Quick3DNode12childRemovedEiP7QObject(
    Qt3DCore::Quick::Quick3DNode *self,
    int idx,
    QObject *child) {
  self->childRemoved(idx, child);
}

//  a QQmlListProperty<QObject> a ritual of Qt3DCore::Quick::Quick3DNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_Quick_Quick3DNode__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QQmlListProperty<Qt3DCore::QNode> a ritual of
//      Qt3DCore::Quick::Quick3DNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_Quick_Quick3DNode__QQmlListProperty_Qt3DCore_QNode(
    QQmlListProperty<Qt3DCore::QNode> *self) {
  delete self;
}
