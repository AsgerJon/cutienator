//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QtTaskTree::QTaskInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QtTaskTree14QTaskInterface10metaObjectEv(
    const QtTaskTree::QTaskInterface *self) {
  return self->metaObject();
}

//  QString QtTaskTree::QTaskInterface::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QtTaskTree14QTaskInterface2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtTaskTree::QTaskInterface::tr(s, c, n));
}

//  QtTaskTree::QTaskInterface::QTaskInterface()
extern "C" Q_DECL_EXPORT
QtTaskTree::QTaskInterface *ritual_ZN10QtTaskTree14QTaskInterfaceC1Ev() {
  return new QtTaskTree::QTaskInterface();
}
