//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QQuickMonthModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickMonthModel10metaObjectEv(
    const QQuickMonthModel *self) {
  return self->metaObject();
}

//  void *QQuickMonthModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickMonthModel11qt_metacastEPKc(
    QQuickMonthModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMonthModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickMonthModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMonthModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QHash<int, QByteArray> QQuickMonthModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK16QQuickMonthModel9roleNamesEv(
    const QQuickMonthModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickMonthModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQuickMonthModel4dataERK11QModelIndexi(
    const QQuickMonthModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickMonthModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickMonthModel8rowCountERK11QModelIndex(
    const QQuickMonthModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QQuickMonthModel::monthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMonthModel12monthChangedEv(QQuickMonthModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "monthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "monthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthModel::yearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMonthModel11yearChangedEv(QQuickMonthModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yearChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yearChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthModel::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMonthModel13localeChangedEv(QQuickMonthModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "localeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "localeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthModel::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMonthModel12titleChangedEv(QQuickMonthModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "titleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "titleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickMonthModelPrivate *QQuickMonthModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickMonthModelPrivate *ritual_ZN16QQuickMonthModel6d_funcEv(
    QQuickMonthModel *self) {
  return self->d_func();
}

//  const QQuickMonthModelPrivate *QQuickMonthModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMonthModelPrivate *ritual_ZNK16QQuickMonthModel6d_funcEv(
    const QQuickMonthModel *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
