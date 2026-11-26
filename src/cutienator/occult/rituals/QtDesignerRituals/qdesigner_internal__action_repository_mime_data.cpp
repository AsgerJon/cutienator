//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(action)
#include <QtGui/qaction.h>
#endif
#include <QtGui/qpixmap.h>
#include <QtCore/qlist.h>

//  const QMetaObject
//      *qdesigner_internal::ActionRepositoryMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData10metaObjectEv(
    const qdesigner_internal::ActionRepositoryMimeData *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::ActionRepositoryMimeData::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal24ActionRepositoryMimeData11qt_metacastEPKc(
    qdesigner_internal::ActionRepositoryMimeData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ActionRepositoryMimeData::qt_metacall(QMetaObject
//      ::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal24ActionRepositoryMimeData11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ActionRepositoryMimeData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::ActionRepositoryMimeData::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal24ActionRepositoryMimeData2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      qdesigner_internal::ActionRepositoryMimeData::tr(
          s,
          c,
          n));
}

//  qdesigner_internal::ActionRepositoryMimeData::ActionRepositoryMimeData(co
//      nst ActionList &a0, Qt::DropAction dropAction)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ActionRepositoryMimeData *ritual_ZN18qdesigner_internal24ActionRepositoryMimeDataC1ERK5QListIP7QActionEN2Qt10DropActionE(
    const QList<QAction *> *a0,
    Qt::DropAction dropAction) {
  return new qdesigner_internal::ActionRepositoryMimeData(*a0, dropAction);
}

//  qdesigner_internal::ActionRepositoryMimeData::ActionRepositoryMimeData(QA
//      ction *a0, Qt::DropAction dropAction)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ActionRepositoryMimeData *ritual_ZN18qdesigner_internal24ActionRepositoryMimeDataC1EP7QActionN2Qt10DropActionE(
    QAction *a0,
    Qt::DropAction dropAction) {
  return new qdesigner_internal::ActionRepositoryMimeData(a0, dropAction);
}

//  const ActionList
//      &qdesigner_internal::ActionRepositoryMimeData::actionList() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData10actionListEv(
    const qdesigner_internal::ActionRepositoryMimeData *self) {
  return new QList<QAction *>(self->actionList());
}

//  QStringList qdesigner_internal::ActionRepositoryMimeData::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData7formatsEv(
    const qdesigner_internal::ActionRepositoryMimeData *self) {
  return new QList<QString>(self->formats());
}

//  QPixmap
//      qdesigner_internal::ActionRepositoryMimeData::actionDragPixmap(const
//      QAction *action)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN18qdesigner_internal24ActionRepositoryMimeData16actionDragPixmapEPK7QAction(
    const QAction *action) {
  return new QPixmap(
      qdesigner_internal::ActionRepositoryMimeData::actionDragPixmap(
          action));
}

//  void qdesigner_internal::ActionRepositoryMimeData::accept(QDragMoveEvent
//      *event) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData6acceptEP14QDragMoveEvent(
    const qdesigner_internal::ActionRepositoryMimeData *self,
    QDragMoveEvent *event) {
  self->accept(event);
}
