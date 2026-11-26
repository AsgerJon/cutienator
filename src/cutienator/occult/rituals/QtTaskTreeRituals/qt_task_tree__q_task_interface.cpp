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

//  void *QtTaskTree::QTaskInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QtTaskTree14QTaskInterface11qt_metacastEPKc(
    QtTaskTree::QTaskInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtTaskTree::QTaskInterface::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QtTaskTree14QTaskInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtTaskTree::QTaskInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QtTaskTree::QTaskInterface::QTaskInterface(QObject *parent)
extern "C" Q_DECL_EXPORT
QtTaskTree::QTaskInterface *ritual_ZN10QtTaskTree14QTaskInterfaceC1EP7QObject(
    QObject *parent) {
  return new QtTaskTree::QTaskInterface(parent);
}

//  void QtTaskTree::QTaskInterface::reportDone(DoneResult result)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree14QTaskInterface10reportDoneENS_10DoneResultE(
    QtTaskTree::QTaskInterface *self,
    QtTaskTree::DoneResult result) {
  self->reportDone(result);
}

//  void QtTaskTree::QTaskInterface::done(QtTaskTree::DoneResult result,
//      QPrivateSignal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree14QTaskInterface4doneENS_10DoneResultENS0_14QPrivateSignalE(
    QtTaskTree::QTaskInterface *self,
    QtTaskTree::DoneResult result) {
  self->done(result, QtTaskTree::QTaskInterface::QPrivateSignal());
}

//  bool QtTaskTree::QTaskInterface::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QtTaskTree14QTaskInterface5eventEP6QEvent(
    QtTaskTree::QTaskInterface *self,
    QEvent *event) {
  return self->event(event);
}
